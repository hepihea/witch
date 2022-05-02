#images06




#############################################################################################################################
############################################################################################################################

# 3 Doors
image night05_hotel_bg_doors3_a_far = "images/day05/night/hotel/night05_hotel_bg_doors3_a_far.webp"
image night05_hotel_bg_doors3_a_close_original = "images/day05/night/hotel/night05_hotel_bg_doors3_a_close_original.webp"

image night05_hotel_bg_doors3_a_close_01 = "images/day05/night/hotel/night05_hotel_bg_doors3_a_close_01.webp"
image night05_hotel_bg_doors3_a_close_02 = "images/day05/night/hotel/night05_hotel_bg_doors3_a_close_02.webp"
image night05_hotel_bg_doors3_a_close_03 = "images/day05/night/hotel/night05_hotel_bg_doors3_a_close_03.webp"

image night05_hotel_doors3_exit_light = "images/day05/night/hotel/night05_hotel_doors3_exit_light.webp"
image night05_hotel_doors3_exit_empty = "images/day05/night/hotel/night05_hotel_doors3_exit_empty.webp"
image night05_hotel_doors3_exit_mask = "images/day05/night/hotel/night05_hotel_doors3_exit_mask.webp"

image night05_hotel_doors3_door_empty = "images/day05/night/hotel/night05_hotel_doors3_door_empty.webp"
image night05_hotel_doors3_door01a_open = "images/day05/night/hotel/night05_hotel_doors3_door01a_open.webp"
image night05_hotel_doors3_door02a_open = "images/day05/night/hotel/night05_hotel_doors3_door02a_open.webp"
image night05_hotel_doors3_door03a_open = "images/day05/night/hotel/night05_hotel_doors3_door03a_open.webp"


#image

##########################
#####################

image night05_hotel_doors3_door_empty_comp:

    "night05_hotel_doors3_door_empty"
    alpha 0.01

image night05_hotel_doors3_exit_empty_comp:

    "night05_hotel_doors3_exit_empty"
    alpha 0.5

image night05_hotel_doors3_exit_light_on_comp02:
    # contains:
    #     "night05_hotel_doors3_exit_light"
    #     #subpixel True
    #     #truecenter
    #     additive 1.0
    #     block:
    #         easein 0.1 alpha 1.0
    #         easein 0.1 alpha 0.5
    #         easein 0.05 alpha 0.8
    #         easein 0.15 alpha 0.4
    #         easein 0.5 alpha 0.5
    #         easein 0.2 alpha 0.9
    #         easein 0.1 alpha 1.0
    #         easein 0.5 alpha 0.5
    #         easein 2.0 alpha 1.0
    #         easein 0.1 alpha 0.5
    #         easein 0.2 alpha 0.8
    #         easein 0.11 alpha 0.2
    #         easein 2.0 alpha 1.0
    #         repeat
    contains:
        "night05_hotel_doors3_exit_mask"

transform light_flame_animation:
    #subpixel True
    additive 1.0
    alpha 0.0
    easein_quad 5.0 alpha 1.0
    block:
        easein_quad 0.1 alpha 1.0
        easeout_quad 0.15 alpha 0.92
        easein_quad 0.05 alpha 0.98
        easeout_quad 0.05 alpha 1.0
        easein_quad 0.35 alpha 0.95
        easein_quad 0.05 alpha 0.88
        easein_quad 0.5 alpha 0.9
        easein_quad 0.4 alpha 1.0
        easein_quad 0.01 alpha 0.89
        easein_quad 0.15 alpha 1.0
        easein_quad 0.2 alpha 0.9
        easein_quad 0.08 alpha 0.98
        easein_quad 0.41 alpha 0.95
        easein_quad 0.2 alpha 1.0
        repeat

transform light_flame_animation02:
    #subpixel True
    additive 1.0
    alpha 1.0
    easein_quad 5.0 alpha 0.9
    block:
        easein_quad 0.3 alpha 1.0
        easeout_quad 0.2 alpha 0.92
        easein_quad 0.15 alpha 0.98
        easeout_quad 0.02 alpha 1.0
        easein_quad 0.15 alpha 0.95
        easein_quad 0.03 alpha 0.88
        easein_quad 0.35 alpha 0.9
        easein_quad 0.4 alpha 1.0
        easein_quad 0.01 alpha 0.89
        easein_quad 0.25 alpha 1.0
        easein_quad 0.12 alpha 0.9
        easein_quad 0.08 alpha 0.98
        easein_quad 0.31 alpha 0.95
        easein_quad 0.2 alpha 1.0
        repeat

screen night05_hotel_doors3_screen():

    if night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover  "night05_hotel_doors3_door01a_open"
            idle "night05_hotel_doors3_door_empty_comp"
            hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask True
            action Jump("night05_NeusLastDate_HotelKrueger_Door_Baby")
            yanchor 0.5 xanchor 0.5
            xpos 0.227 ypos 0.466

    if night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover  "night05_hotel_doors3_door02a_open"
            idle "night05_hotel_doors3_door_empty_comp"
            hover_sound "audio/sfx/door_old_short_open02.ogg"
            focus_mask True
            action Jump("night05_NeusLastDate_HotelKrueger_Door_Childhood")
            yanchor 0.5 xanchor 0.5
            xpos 0.505 ypos 0.466

    if night05_NeusLastDate_HotelKrueger_Door_03_Marriage_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover  "night05_hotel_doors3_door03a_open"
            idle "night05_hotel_doors3_door_empty_comp"
            hover_sound "audio/sfx/door_old_short_open03.ogg"
            focus_mask True
            action Jump("night05_NeusLastDate_HotelKrueger_Door_Marriage")
            yanchor 0.5 xanchor 0.5
            xpos 0.788 ypos 0.466

    imagebutton at hover_dissolve_transform:
        #hover  "night05_hotel_doors3_exit_light_on_comp02"
        hover "night05_hotel_doors3_exit_light"
        idle "night05_hotel_doors3_exit_empty_comp"
        #idle "night05_hotel_doors3_exit_mask"
        hover_sound "audio/sfx/light_neon_on01.ogg"
        focus_mask "night05_hotel_doors3_exit_mask"
        # focus_mask True
        action Jump("night05_NeusLastDate_HotelKrueger_Door_Exit_00")
        yanchor 0.5 xanchor 0.5
        xpos 0.87 ypos 0.06

#############################################################################################################################
############################################################################################################################

# DOOR 01_Cemetery
    #gate
image bg room_01_cemetery_gate_bg = SaturateTint("images/day05/night/hotel/room_01_cemetery/gate_bg.webp")
image room_01_cemetery_gate_opened = SaturateTint("images/day05/night/hotel/room_01_cemetery/gate_opened.webp")
image room_01_cemetery_gate_closed = SaturateTint("images/day05/night/hotel/room_01_cemetery/gate_closed.webp")

image room_01_cemetery_gate_closed_comp:

    "room_01_cemetery_gate_closed"
    alpha 0.01

#####################
####################

screen night05_hotel_doors3_Cemetery_Gate_screen():
    add "bg room_01_cemetery_gate_bg" at screendissolve
    imagebutton at hover_dissolve_transform:
        hover  "room_01_cemetery_gate_opened"
        idle "room_01_cemetery_gate_closed_comp"
        #hover_sound "audio/sfx/door_old_short_open01.ogg"
        focus_mask True
        action Jump("night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Far_Beginning")
        yanchor 0.5 xanchor 0.5
        xpos 0.372 ypos 0.5

    add "night05_Cemetery_smoke_comp" at screendissolve


#######################

    #far
image bg room_01_cemetery_far_bg = SaturateTint("images/day05/night/hotel/room_01_cemetery/far_bg.webp")

image room_01_cemetery_far_tomb_01_on = "images/day05/night/hotel/room_01_cemetery/far_tomb_01_on.webp"
image room_01_cemetery_far_tomb_02_on = "images/day05/night/hotel/room_01_cemetery/far_tomb_02_on.webp"
image room_01_cemetery_far_tomb_03_on = "images/day05/night/hotel/room_01_cemetery/far_tomb_03_on.webp"
image room_01_cemetery_far_tomb_04_on = "images/day05/night/hotel/room_01_cemetery/far_tomb_04_on.webp"
image room_01_cemetery_far_tomb_05_on = "images/day05/night/hotel/room_01_cemetery/far_tomb_05_on.webp"
image room_01_cemetery_far_tomb_06_on = "images/day05/night/hotel/room_01_cemetery/far_tomb_06_on.webp"
image room_01_cemetery_far_tomb_family_on = "images/day05/night/hotel/room_01_cemetery/far_tomb_family_on.webp"

image room_01_cemetery_far_tomb_01_off = "images/day05/night/hotel/room_01_cemetery/far_tomb_01_off.webp"
image room_01_cemetery_far_tomb_02_off = "images/day05/night/hotel/room_01_cemetery/far_tomb_02_off.webp"
image room_01_cemetery_far_tomb_03_off = "images/day05/night/hotel/room_01_cemetery/far_tomb_03_off.webp"
image room_01_cemetery_far_tomb_04_off = "images/day05/night/hotel/room_01_cemetery/far_tomb_04_off.webp"
image room_01_cemetery_far_tomb_05_off = "images/day05/night/hotel/room_01_cemetery/far_tomb_05_off.webp"
image room_01_cemetery_far_tomb_06_off = "images/day05/night/hotel/room_01_cemetery/far_tomb_06_off.webp"
image room_01_cemetery_far_tomb_family_off = "images/day05/night/hotel/room_01_cemetery/far_tomb_family_off.webp"

image room_01_cemetery_far_tomb_01_PROVE = "images/day05/night/hotel/room_01_cemetery/far_tomb_01_PROVE.webp"
image room_01_cemetery_far_tomb_02_PROVE = "images/day05/night/hotel/room_01_cemetery/far_tomb_02_PROVE.webp"
image room_01_cemetery_far_tomb_03_PROVE = "images/day05/night/hotel/room_01_cemetery/far_tomb_03_PROVE.webp"
image room_01_cemetery_far_tomb_04_PROVE = "images/day05/night/hotel/room_01_cemetery/far_tomb_04_PROVE.webp"
image room_01_cemetery_far_tomb_05_PROVE = "images/day05/night/hotel/room_01_cemetery/far_tomb_05_PROVE.webp"
image room_01_cemetery_far_tomb_06_PROVE = "images/day05/night/hotel/room_01_cemetery/far_tomb_06_PROVE.webp"
image room_01_cemetery_far_tomb_family_PROVE = "images/day05/night/hotel/room_01_cemetery/far_tomb_family_PROVE.webp"

#####################
####################

image room_01_cemetery_far_tomb_family_on_comp:

    "room_01_cemetery_far_tomb_family_on"
    light_flame_animation

image room_01_cemetery_far_tomb_family_off_comp:

    "room_01_cemetery_far_tomb_family_off"
    alpha 0.01

image room_01_cemetery_far_tomb_01_on_comp:

    "room_01_cemetery_far_tomb_01_on"
    light_flame_animation

image room_01_cemetery_far_tomb_01_off_comp:

    "room_01_cemetery_far_tomb_01_off"
    alpha 0.01

image room_01_cemetery_far_tomb_02_on_comp:

    "room_01_cemetery_far_tomb_02_on"
    light_flame_animation

image room_01_cemetery_far_tomb_02_off_comp:

    "room_01_cemetery_far_tomb_02_off"
    alpha 0.01

image room_01_cemetery_far_tomb_03_on_comp:

    "room_01_cemetery_far_tomb_03_on"
    light_flame_animation

image room_01_cemetery_far_tomb_03_off_comp:

    "room_01_cemetery_far_tomb_03_off"
    alpha 0.01

image room_01_cemetery_far_tomb_04_on_comp:

    "room_01_cemetery_far_tomb_04_on"
    light_flame_animation

image room_01_cemetery_far_tomb_04_off_comp:

    "room_01_cemetery_far_tomb_04_off"
    alpha 0.01

image room_01_cemetery_far_tomb_05_on_comp:

    "room_01_cemetery_far_tomb_05_on"
    light_flame_animation

image room_01_cemetery_far_tomb_05_off_comp:

    "room_01_cemetery_far_tomb_05_off"
    alpha 0.01

image room_01_cemetery_far_tomb_06_on_comp:

    "room_01_cemetery_far_tomb_06_on"
    light_flame_animation

image room_01_cemetery_far_tomb_06_off_comp:

    "room_01_cemetery_far_tomb_06_off"
    alpha 0.01

screen night05_hotel_doors3_Cemetery_Far_screen():

    if night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_01_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover  "room_01_cemetery_far_tomb_01_on_comp"
            idle "room_01_cemetery_far_tomb_01_off_comp"
            hover_sound "audio/sfx/candle_short01.ogg"
            focus_mask "room_01_cemetery_far_tomb_01_on"
            action Jump("room_01_cemetery_far_tomb_01_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.131 ypos 0.75

    if night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_02_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover  "room_01_cemetery_far_tomb_02_on_comp"
            idle "room_01_cemetery_far_tomb_02_off_comp"
            hover_sound "audio/sfx/candle_short02.ogg"
            focus_mask "room_01_cemetery_far_tomb_02_on"
            action Jump("room_01_cemetery_far_tomb_02_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.325 ypos 0.631

    if night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_03_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover  "room_01_cemetery_far_tomb_03_on_comp"
            idle "room_01_cemetery_far_tomb_03_off_comp"
            hover_sound "audio/sfx/candle_short03.ogg"
            focus_mask "room_01_cemetery_far_tomb_03_on"
            action Jump("room_01_cemetery_far_tomb_03_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5285 ypos 0.595

    if night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_04_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover  "room_01_cemetery_far_tomb_04_on_comp"
            idle "room_01_cemetery_far_tomb_04_off_comp"
            hover_sound "audio/sfx/candle_short04.ogg"
            focus_mask "room_01_cemetery_far_tomb_04_on"
            action Jump("room_01_cemetery_far_tomb_04_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.622 ypos 0.4978

    if night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_05_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover  "room_01_cemetery_far_tomb_05_on_comp"
            idle "room_01_cemetery_far_tomb_05_off_comp"
            hover_sound "audio/sfx/candle_short05.ogg"
            focus_mask "room_01_cemetery_far_tomb_05_on"
            action Jump("room_01_cemetery_far_tomb_05_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.717 ypos 0.642

    if night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_06_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover  "room_01_cemetery_far_tomb_06_on_comp"
            idle "room_01_cemetery_far_tomb_06_off_comp"
            hover_sound "audio/sfx/candle_short04.ogg"
            focus_mask "room_01_cemetery_far_tomb_06_on"
            action Jump("room_01_cemetery_far_tomb_06_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.909 ypos 0.685

    if night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_family_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover  "room_01_cemetery_far_tomb_family_on_comp"
            idle "room_01_cemetery_far_tomb_family_off_comp"
            hover_sound "audio/sfx/candle_short03.ogg"
            focus_mask "room_01_cemetery_far_tomb_family_on"
            action Jump("room_01_cemetery_far_tomb_family_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.4795 ypos 0.48

    #add "night05_Cemetery_smoke_comp"

########################
    #close


#####################
####################

image night05_tibidabo_bracelet_bracelets = "images/day05/night/night05_tibidabo_bracelet_bracelets.webp"

image night05_tibidabo_bracelet_MCShow_mc_hand = "images/day05/night/night05_tibidabo_bracelet_MCShow_mc_hand.webp"
image night05_tibidabo_bracelet_MCShow_bracelet = "images/day05/night/night05_tibidabo_bracelet_MCShow_bracelet_[MShooter_Bracelet].webp"
image night05_tibidabo_bracelet_MCShow_necklace = "images/day05/night/night05_tibidabo_bracelet_MCShow_necklace.webp"



image night05_tibidabo_bracelet_MCShow_necklace_comp:

    contains:
        "night05_tibidabo_bracelet_MCShow_mc_hand"
        truecenter
    contains:
        "night05_tibidabo_bracelet_MCShow_necklace"
        truecenter

image night05_tibidabo_bracelet_MCShow_comp:

    contains:
        "night05_tibidabo_bracelet_MCShow_mc_hand"
        truecenter
    contains:
        "night05_tibidabo_bracelet_MCShow_bracelet"
        truecenter


image night05_tibidabo_bracelet_SheShow_n_bracelet = "images/day05/night/night05_tibidabo_bracelet_SheShow_n_bracelet_[MShooter_Bracelet].webp"
image night05_tibidabo_bracelet_SheShow_n_fingers = "images/day05/night/night05_tibidabo_bracelet_SheShow_n_fingers.webp"
image night05_tibidabo_bracelet_SheShow_n_wrist = "images/day05/night/night05_tibidabo_bracelet_SheShow_n_wrist.webp"


image night05_tibidabo_bracelet_SheShow_comp:

    contains:
        "night05_tibidabo_bracelet_SheShow_n_wrist"
        truecenter
    contains:
        "night05_tibidabo_bracelet_SheShow_n_bracelet"
        truecenter
    contains:
        "night05_tibidabo_bracelet_SheShow_n_fingers"
        truecenter

image night05_bg_cups_rideseat shadow_yes = "images/day05/night/night05_bg_cups_rideseat_shadow_yes.webp"
image night05_bg_cups_rideseat shadow_no = "images/day05/night/night05_bg_cups_rideseat_shadow_no.webp"

image bg night05_bg_cups_ridebg_01 = "images/day05/night/night05_bg_cups_ridebg_01.webp"
image bg night05_bg_cups_ridebg_02 = "images/day05/night/night05_bg_cups_ridebg_02.webp"
image bg night05_bg_cups_ridebg_03 = "images/day05/night/night05_bg_cups_ridebg_03.webp"
image bg night05_bg_cups_ridebg_04 = "images/day05/night/night05_bg_cups_ridebg_04.webp"

image bg night05_bg_cups_ridebg_comp_01:

    contains:
        "bg night05_bg_cups_ridebg_01"
        truecenter
        xzoom -1.0
        xpos 3.0

    contains:
        "bg night05_bg_cups_ridebg_01"
        truecenter
        xpos -3.0 yzoom -1.0

image bg night05_bg_cups_ridebg_comp_02:

    contains:
        "bg night05_bg_cups_ridebg_02"
        truecenter
        xzoom -1.0
        xpos 3.0

    contains:
        "bg night05_bg_cups_ridebg_02"
        truecenter
        xzoom -1.0
        xpos -3.0 yzoom -1.0

image bg night05_bg_cups_ridebg_comp_03:

    contains:
        "bg night05_bg_cups_ridebg_03"
        truecenter
        xzoom -1.0
        xpos 3.0

    contains:
        "bg night05_bg_cups_ridebg_03"
        truecenter
        xzoom -1.0
        xpos -3.0 yzoom -1.0

image bg night05_bg_cups_ridebg_comp_04:

    contains:
        "bg night05_bg_cups_ridebg_04"
        truecenter
        xzoom -1.0
        xpos 3.0

    contains:
        "bg night05_bg_cups_ridebg_04"
        truecenter
        xzoom -1.0
        xpos -3.0 yzoom -1.0

############################################################################
###########################################################################
##########################################################################

image bg night05_bg_tibidabo_bathroom = "images/day05/night/night05_bg_tibidabo_bathroom.webp"
image night05_bg_tibidabo_bathroom_person = "images/day05/night/night05_bg_tibidabo_bathroom_person.webp"

image bg night05_bg_tibidabo_bathroom_comp_01:

    contains:
        "bg night05_bg_tibidabo_bathroom"
        truecenter
    contains:
        "night05_bg_tibidabo_bathroom_person"
        truecenter

image bg night05_bg_tibidabo_bathroom_sink = "images/day05/night/night05_bg_tibidabo_bathroom_sink.webp"
image bg night05_bg_tibidabo_bathroom_toilet = "images/day05/night/night05_bg_tibidabo_bathroom_toilet.webp"
image bg night05_bg_tibidabo_bathroom_wall_door = "images/day05/night/night05_bg_tibidabo_bathroom_wall_door.webp"

############################################################################
###########################################################################
##########################################################################


## BACKGROUND

image bg night05_bg_tibidabo_bathroom_wc_PROVE = "images/day05/night/night05_bg_tibidabo_bathroom_wc_PROVE.webp"
image bg night05_bg_tibidabo_bathroom_wc_door = "images/day05/night/night05_bg_tibidabo_bathroom_wc_door.webp"
image bg night05_bg_tibidabo_bathroom_wc_wall = "images/day05/night/night05_bg_tibidabo_bathroom_wc_wall.webp"

### NEUS

image night05_tibidabo_bathroom_n_PROVE = "images/day05/night/night05_tibidabo_bathroom_n_PROVE.webp"

image night05_tibidabo_bathroom_n_arm_l down = "images/day05/night/night05_tibidabo_bathroom_n_arm_l_down.webp"
image night05_tibidabo_bathroom_n_arm_l up = "images/day05/night/night05_tibidabo_bathroom_n_arm_l_up.webp"
image night05_tibidabo_bathroom_n_arm_l_up_bracelet = "images/day05/night/night05_tibidabo_bathroom_n_arm_l_up_bracelet_[MShooter_Bracelet].webp"
image night05_tibidabo_bathroom_n_arm_r up = "images/day05/night/night05_tibidabo_bathroom_n_arm_r_up.webp"

image night05_tibidabo_bathroom_n_ass_skirt off = "images/day05/night/night05_tibidabo_bathroom_n_ass_skirt_off.webp"
image night05_tibidabo_bathroom_n_ass_skirt on = "images/day05/night/night05_tibidabo_bathroom_n_ass_skirt_on.webp"

image night05_tibidabo_bathroom_n_body = "images/day05/night/night05_tibidabo_bathroom_n_body.webp"

        ### EXPRESSIONS

    ## blush

image night05_tibidabo_bathroom_n_exp_blush 00 = "images/general/empty.webp"
image night05_tibidabo_bathroom_n_exp_blush 01 = "images/day05/night/night05_tibidabo_bathroom_n_exp_blush_01.webp"
image night05_tibidabo_bathroom_n_exp_blush 02 = "images/day05/night/night05_tibidabo_bathroom_n_exp_blush_02.webp"
image night05_tibidabo_bathroom_n_exp_blush 03 = "images/day05/night/night05_tibidabo_bathroom_n_exp_blush_03.webp"
image night05_tibidabo_bathroom_n_exp_blush 04 = "images/day05/night/night05_tibidabo_bathroom_n_exp_blush_04.webp"
image night05_tibidabo_bathroom_n_exp_blush 05 = "images/day05/night/night05_tibidabo_bathroom_n_exp_blush_05.webp"
image night05_tibidabo_bathroom_n_exp_blush 06 = "images/day05/night/night05_tibidabo_bathroom_n_exp_blush_06.webp"

    ## eyebrows

image night05_tibidabo_bathroom_n_exp_eyebrows angryx01 = "images/day05/night/night05_tibidabo_bathroom_n_exp_eyebrows_angryx01.webp"
image night05_tibidabo_bathroom_n_exp_eyebrows angryx02 = "images/day05/night/night05_tibidabo_bathroom_n_exp_eyebrows_angryx02.webp"
image night05_tibidabo_bathroom_n_exp_eyebrows angryx03 = "images/day05/night/night05_tibidabo_bathroom_n_exp_eyebrows_angryx03.webp"
image night05_tibidabo_bathroom_n_exp_eyebrows normal = "images/day05/night/night05_tibidabo_bathroom_n_exp_eyebrows_normal.webp"
image night05_tibidabo_bathroom_n_exp_eyebrows sadx01 = "images/day05/night/night05_tibidabo_bathroom_n_exp_eyebrows_sadx01.webp"
image night05_tibidabo_bathroom_n_exp_eyebrows sadx02 = "images/day05/night/night05_tibidabo_bathroom_n_exp_eyebrows_sadx02.webp"
image night05_tibidabo_bathroom_n_exp_eyebrows sadx03 = "images/day05/night/night05_tibidabo_bathroom_n_exp_eyebrows_sadx03.webp"
image night05_tibidabo_bathroom_n_exp_eyebrows sadx04 = "images/day05/night/night05_tibidabo_bathroom_n_exp_eyebrows_sadx04.webp"
image night05_tibidabo_bathroom_n_exp_eyebrows serious = "images/day05/night/night05_tibidabo_bathroom_n_exp_eyebrows_serious.webp"
image night05_tibidabo_bathroom_n_exp_eyebrows surprisex01 = "images/day05/night/night05_tibidabo_bathroom_n_exp_eyebrows_surprisex01.webp"
image night05_tibidabo_bathroom_n_exp_eyebrows surprisex02 = "images/day05/night/night05_tibidabo_bathroom_n_exp_eyebrows_surprisex02.webp"

    ## eyes

image night05_tibidabo_bathroom_n_exp_eyes 00 = "images/day05/night/night05_tibidabo_bathroom_n_exp_eyes_00[neyesp].webp"
image night05_tibidabo_bathroom_n_exp_eyes 02 = "images/day05/night/night05_tibidabo_bathroom_n_exp_eyes_02[neyesp].webp"
image night05_tibidabo_bathroom_n_exp_eyes 04 = "images/day05/night/night05_tibidabo_bathroom_n_exp_eyes_04[neyesp].webp"
image night05_tibidabo_bathroom_n_exp_eyes 05 = "images/day05/night/night05_tibidabo_bathroom_n_exp_eyes_05[neyesp].webp"
image night05_tibidabo_bathroom_n_exp_eyes 06 = "images/day05/night/night05_tibidabo_bathroom_n_exp_eyes_06[neyesp].webp"
image night05_tibidabo_bathroom_n_exp_eyes 07 = "images/day05/night/night05_tibidabo_bathroom_n_exp_eyes_07[neyesp].webp"

image night05_tibidabo_bathroom_n_exp_glasses = "images/day05/night/night05_tibidabo_bathroom_n_exp_glasses.webp"


    ## mouth

image night05_tibidabo_bathroom_n_exp_mouth happy_Silentx01 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_happy_Silentx01.webp"
image night05_tibidabo_bathroom_n_exp_mouth happy_Silentx02 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_happy_Silentx02.webp"
image night05_tibidabo_bathroom_n_exp_mouth happy_Silentx03 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_happy_Silentx03.webp"
image night05_tibidabo_bathroom_n_exp_mouth happy_Silentx04 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_happy_Silentx04.webp"
image night05_tibidabo_bathroom_n_exp_mouth happy_Silentx05 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_happy_Silentx05.webp"

image night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx01 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_happy_Talkingx01.webp"
image night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx02 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_happy_Talkingx02.webp"
image night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx03 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_happy_Talkingx03.webp"

image night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx01 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_happybiting_Silentx01.webp"
image night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx02 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_happybiting_Silentx02.webp"
image night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx03 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_happybiting_Silentx03.webp"
image night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx04 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_happybiting_Silentx04.webp"

image night05_tibidabo_bathroom_n_exp_mouth sad_Silentx01 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_sad_Silentx01.webp"
image night05_tibidabo_bathroom_n_exp_mouth sad_Silentx02 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_sad_Silentx02.webp"
image night05_tibidabo_bathroom_n_exp_mouth sad_Silentx03 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_sad_Silentx03.webp"

image night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx01 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_sad_Talkingx01.webp"
image night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx02 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_sad_Talkingx02.webp"
image night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx03 = "images/day05/night/night05_tibidabo_bathroom_n_exp_mouth_sad_Talkingx03.webp"

    ## pupils

image night05_tibidabo_bathroom_n_exp_pupils empty = "images/general/empty.webp"
image night05_tibidabo_bathroom_n_exp_pupils cameradown00 = "images/day05/night/night05_tibidabo_bathroom_n_exp_pupils_cameradown00.webp"
image night05_tibidabo_bathroom_n_exp_pupils cameradown02 = "images/day05/night/night05_tibidabo_bathroom_n_exp_pupils_cameradown02.webp"
image night05_tibidabo_bathroom_n_exp_pupils cameradown04 = "images/day05/night/night05_tibidabo_bathroom_n_exp_pupils_cameradown04.webp"
image night05_tibidabo_bathroom_n_exp_pupils camerafront00 = "images/day05/night/night05_tibidabo_bathroom_n_exp_pupils_camerafront00.webp"
image night05_tibidabo_bathroom_n_exp_pupils camerafront02 = "images/day05/night/night05_tibidabo_bathroom_n_exp_pupils_camerafront02.webp"
image night05_tibidabo_bathroom_n_exp_pupils camerafront04 = "images/day05/night/night05_tibidabo_bathroom_n_exp_pupils_camerafront04.webp"
image night05_tibidabo_bathroom_n_exp_pupils doordown00 = "images/day05/night/night05_tibidabo_bathroom_n_exp_pupils_doordown00.webp"
image night05_tibidabo_bathroom_n_exp_pupils doordown02 = "images/day05/night/night05_tibidabo_bathroom_n_exp_pupils_doordown02.webp"
image night05_tibidabo_bathroom_n_exp_pupils doordown04 = "images/day05/night/night05_tibidabo_bathroom_n_exp_pupils_doordown04.webp"
image night05_tibidabo_bathroom_n_exp_pupils doorup00 = "images/day05/night/night05_tibidabo_bathroom_n_exp_pupils_doorup00.webp"
image night05_tibidabo_bathroom_n_exp_pupils doorup02 = "images/day05/night/night05_tibidabo_bathroom_n_exp_pupils_doorup02.webp"
image night05_tibidabo_bathroom_n_exp_pupils doorup04 = "images/general/empty.webp"

    ## hair

image night05_tibidabo_bathroom_n_hair_front = "images/day05/night/night05_tibidabo_bathroom_n_hair_front.webp"

#####


transform night05_tibidabo_bathroom_n_exp_position_00a:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.5
    zoom 0.75 xpos 0.615 ypos 0.35 alpha 1.0

image night05_tibidabo_bathroom_n_comp_00a:
    
    contains:
        "bg night05_bg_tibidabo_bathroom_wc_door"
        transform_anchor True
        xalign 0.5 yalign 0.5
        ypos 1.08

    contains:
        "night05_tibidabo_bathroom_n_arm_l up"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_arm_l_up_bracelet"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_body"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_arm_r up"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_ass_skirt on"
        transform_anchor True
        xalign 0.5 yalign 1.0
        ypos 4.42 alpha 1.0

transform night05_tibidabo_bathroom_n_exp_position_default:
    transform_anchor True
    xalign 0.5 yalign 0.5
    xpos 1.318 ypos -0.365 alpha 1.0

image night05_tibidabo_bathroom_n_comp 01:
    
    contains:
        "bg night05_bg_tibidabo_bathroom_wc_door"
        transform_anchor True
        xalign 0.5 yalign 0.5
        ypos 1.08

    contains:
        "night05_tibidabo_bathroom_n_arm_l up"
        truecenter

    contains:
        ConditionSwitch(MShooter_Bracelet in MShooter_Bracelet_var, At("night05_tibidabo_bathroom_n_arm_l_up_bracelet", truecenter),
                                                "True", Null())

    contains:
        "night05_tibidabo_bathroom_n_body"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_exp_mouth happy_Silentx02"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_blush 02"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_eyes 02"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_pupils doordown02"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_eyebrows serious"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_glasses"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_hair_front"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_arm_r up"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_ass_skirt on"
        transform_anchor True
        xalign 0.5 yalign 1.0
        ypos 4.42 alpha 1.0

    
image night05_tibidabo_bathroom_n_comp 02:
    
    contains:
        "bg night05_bg_tibidabo_bathroom_wc_wall"
        transform_anchor True
        xalign 0.5 yalign 0.5
        ypos 1.08

    contains:
        "night05_tibidabo_bathroom_n_arm_l up"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_arm_l_up_bracelet"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_body"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_exp_mouth happy_Silentx03"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_blush 04"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_eyes 04"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_pupils doordown04"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_eyebrows sadx01"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_glasses"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_hair_front"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_arm_r up"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_ass_skirt on"
        transform_anchor True
        xalign 0.5 yalign 1.0
        ypos 4.42 alpha 1.0

image night05_tibidabo_bathroom_n_comp 03:
    
    contains:
        "bg night05_bg_tibidabo_bathroom_wc_wall"
        transform_anchor True
        xalign 0.5 yalign 0.5
        ypos 1.08

    contains:
        "night05_tibidabo_bathroom_n_arm_l down"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_body"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx03"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_blush 04"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_eyes 04"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_pupils camerafront04"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_eyebrows sadx02"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_glasses"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_hair_front"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_arm_r up"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_ass_skirt on"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 1.0
        ypos 4.42 # Default

        parallel:
            ease_quad 8.0 ypos 4.38 # Up
            ease_quad 8.0 ypos 4.45 # Down
            repeat

        parallel:
            ease_quad 2.0 rotate 0.2
            ease_quad 2.0 rotate -0.2
            repeat

image night05_tibidabo_bathroom_n_comp 04: #Skirt Up
    
    contains:
        "bg night05_bg_tibidabo_bathroom_wc_wall"
        transform_anchor True
        xalign 0.5 yalign 0.5
        ypos 1.08

    contains:
        "night05_tibidabo_bathroom_n_arm_l down"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_body"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx03"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_blush 04"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_eyes 04"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_pupils camerafront04"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_eyebrows sadx02"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_glasses"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_hair_front"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_arm_r up"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_ass_skirt off"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 1.0
        ypos 4.42 # Default

        parallel:
            ease_quad 8.0 ypos 4.38 # Up
            ease_quad 8.0 ypos 4.45 # Down
            repeat

        parallel:
            ease_quad 2.0 rotate 0.2
            ease_quad 2.0 rotate -0.2
            repeat

image night05_tibidabo_bathroom_n_comp 05: #Moving Fast
    
    contains:
        "bg night05_bg_tibidabo_bathroom_wc_wall"
        transform_anchor True
        xalign 0.5 yalign 0.5
        ypos 1.08

    contains:
        "night05_tibidabo_bathroom_n_arm_l down"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_body"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx04"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_blush 04"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_eyes 04"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_pupils doordown04"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_eyebrows sadx03"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_glasses"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_hair_front"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_arm_r up"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_ass_skirt off"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 1.0
        ypos 4.42 # Default

        parallel:
            ease_quad 1.0 ypos 4.3 # Up
            ease_quad 1.0 ypos 4.5 # Down
            repeat

        parallel:
            ease_quad 1.2 rotate 0.5
            ease_quad 1.5 rotate -0.4
            repeat

image night05_tibidabo_bathroom_n_comp 06: #Moving Faster
    
    contains:
        "bg night05_bg_tibidabo_bathroom_wc_wall"
        transform_anchor True
        xalign 0.5 yalign 0.5
        ypos 1.08

    contains:
        "night05_tibidabo_bathroom_n_arm_l down"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_body"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx04"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_blush 05"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_eyes 04"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_pupils camerafront04"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_eyebrows sadx03"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_exp_glasses"
        night05_tibidabo_bathroom_n_exp_position_default

    contains:
        "night05_tibidabo_bathroom_n_hair_front"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_arm_r up"
        truecenter

    contains:
        "night05_tibidabo_bathroom_n_ass_skirt off"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 1.0
        ypos 4.42 # Default

        parallel:
            ease_quad 0.5 ypos 4.28 # Up
            ease_quad 0.5 ypos 4.52 # Down
            repeat

        parallel:
            ease_quad 1.2 rotate 0.5
            ease_quad 1.5 rotate -0.4
            repeat

############################################################################################
###########################################################################################
##########################################################################################
#########################################################################################
########################################################################################
#######################################################################################



    ## New Txell

transform mtxell_body_ontheright_position:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2615
    xpos 0.75 ypos 0.2 zoom 0.222

transform mtxell_exp_ontheright_position:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.5
    xpos 0.75 ypos 0.2 zoom 0.222
##

transform mtxell_body_ontheleft_position:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2615
    xpos 0.2 ypos 0.2 zoom 0.222

transform mtxell_exp_ontheleft_position:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.5
    xpos 0.2 ypos 0.2 zoom 0.222

##

transform mtxell_body_ontheright_zoom_0_2_pos:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2615
    xpos 0.8 ypos 0.18 zoom 0.2

transform mtxell_exp_ontheright_zoom_0_2_pos:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.5
    xpos 0.8 ypos 0.18 zoom 0.2

##

transform mtxell_body_ontheright_zoom_0_3_pos:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2615
    xpos 0.8 ypos 0.2 zoom 0.3

transform mtxell_exp_ontheright_zoom_0_3_pos:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.5
    xpos 0.8 ypos 0.2 zoom 0.3
##

transform mtxell_body_ontheright_zoom_0_4_pos:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2615
    xpos 0.8 ypos 0.2 zoom 0.4

transform mtxell_exp_ontheright_zoom_0_4_pos:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.5
    xpos 0.8 ypos 0.2 zoom 0.4
###


##

transform mtxell_body_ontheleft_zoom_0_4_pos:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2615
    xpos 0.25 ypos 0.2 zoom 0.4

transform mtxell_exp_ontheleft_zoom_0_4_pos:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.5
    xpos 0.25 ypos 0.2 zoom 0.4

###

##

transform mtxell_body_center_zoom_0_4_pos:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2615
    xpos 0.5 ypos 0.2 zoom 0.4

transform mtxell_exp_center_zoom_0_4_pos:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.5
    xpos 0.5 ypos 0.2 zoom 0.4


##

transform mtxell_body_center_zoom_1_0_pos:
    transform_anchor True
    xalign 0.5 yalign 0.2615
    xpos 0.5 ypos 0.3 zoom 1.0

transform mtxell_exp_center_zoom_1_0_pos:
    transform_anchor True
    xalign 0.5 yalign 0.5
    xpos 0.5 ypos 0.3 zoom 1.0

## DryingChin

transform mtxell_body_Dchin_pos:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2615
    xpos 0.5 ypos 0.2 zoom 1.5

transform mtxell_exp_Dchin_pos:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.5
    xpos 0.5 ypos 0.2 zoom 1.5

###

transform m_txell_atright_pos_zoom0_25:
    subpixel True
    zoom 0.25

transform m_txell_atright_pos_zoom0_5:
    subpixel True
    zoom 0.5

transform m_txell_atright_pos_zoom0_75:
    subpixel True
    zoom 0.75

##

transform mtxell_body_onleftpark_comp_position:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2615
    xpos -0.1 ypos 0.55 zoom 0.35

transform mtxell_exp_onleftpark_comp_position:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.5
    xpos -0.1 ypos 0.55 zoom 0.35

image m_park_guard_comp serious:

    contains:
        "bg_dark_a"
        truecenter
        zoom 5.0

    contains:
        "m_body guard"
        mtxell_body_truecenter_position

    contains:
        "m_arm_r guard_hip"
        mtxell_body_truecenter_position

    contains:
        "m_exp_mouth serious_Silentx01"
        mtxell_exp_truecenter_position

    contains:
        "m_exp_over hat"
        mtxell_exp_truecenter_position

image m_park_guard_comp happy_Talking:

    contains:
        "bg_dark_a"
        truecenter
        zoom 5.0

    contains:
        "m_body guard"
        mtxell_body_truecenter_position

    contains:
        "m_arm_r guard_hip"
        mtxell_body_truecenter_position

    contains:
        "m_exp_mouth happy_Talkingx05"
        mtxell_exp_truecenter_position

    contains:
        "m_exp_over hat"
        mtxell_exp_truecenter_position


image m_park_guard_comp happy_Silent:

    contains:
        "bg_dark_a"
        truecenter
        zoom 5.0

    contains:
        "m_body guard"
        mtxell_body_truecenter_position

    contains:
        "m_arm_r guard_hip"
        mtxell_body_truecenter_position

    contains:
        "m_exp_mouth happy_Silentx05"
        mtxell_exp_truecenter_position

    contains:
        "m_exp_over hat"
        mtxell_exp_truecenter_position


transform mtxell_body_truecenter_position:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2615
    xpos 0.5 ypos 0.5 zoom 1.0

transform mtxell_exp_truecenter_position:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.5
    xpos 0.5 ypos 0.5 zoom 1.0


default m_exp_eyez = "front02"

label m_exp_label:

    if m_exp_eyez in ["front00", "right00", "left00", "down00"]:
        show m_exp_eyes 00
        if m_exp_eyez == "front00":
            show m_exp_piris front00
        elif m_exp_eyez == "right00":
            show m_exp_piris right00
        elif m_exp_eyez == "left00":
            show m_exp_piris left00
        elif m_exp_eyez == "down00":
            show m_exp_piris down00

    elif m_exp_eyez in ["front01", "right01", "left01", "down01"]:
        show m_exp_eyes 01
        if m_exp_eyez == "front01":
            show m_exp_piris front01
        elif m_exp_eyez == "right01":
            show m_exp_piris right01
        elif m_exp_eyez == "left01":
            show m_exp_piris left01
        elif m_exp_eyez == "down01":
            show m_exp_piris down01

    elif m_exp_eyez in ["front02", "right02", "left02", "down02"]:
        show m_exp_eyes 02
        if m_exp_eyez == "front02":
            show m_exp_piris front02
        elif m_exp_eyez == "right02":
            show m_exp_piris right02
        elif m_exp_eyez == "left02":
            show m_exp_piris left02
        elif m_exp_eyez == "down02":
            show m_exp_piris down02

    elif m_exp_eyez in ["front03", "right03", "left03", "down03"]:
        show m_exp_eyes 03
        if m_exp_eyez == "front03":
            show m_exp_piris front03
        elif m_exp_eyez == "right03":
            show m_exp_piris right03
        elif m_exp_eyez == "left03":
            show m_exp_piris left03
        elif m_exp_eyez == "down03":
            show m_exp_piris down03

    elif m_exp_eyez in ["front04", "right04", "left04", "down04"]:
        show m_exp_eyes 04
        if m_exp_eyez == "front04":
            show m_exp_piris front04
        elif m_exp_eyez == "right04":
            show m_exp_piris right04
        elif m_exp_eyez == "left04":
            show m_exp_piris left04
        elif m_exp_eyez == "down04":
            show m_exp_piris down04

    elif m_exp_eyez in ["front05", "right05", "left05", "down05"]:
        show m_exp_eyes 05
        if m_exp_eyez == "front05":
            show m_exp_piris front05
        elif m_exp_eyez == "right05":
            show m_exp_piris right05
        elif m_exp_eyez == "left05":
            show m_exp_piris left05
        elif m_exp_eyez == "down05":
            show m_exp_piris down05


    elif m_exp_eyez in ["front06", "front07", "front08", "empty"]:
        show m_exp_piris empty

        if m_exp_eyez == "front06":
            show m_exp_eyes 06
        elif m_exp_eyez == "front07":
            show m_exp_eyes 07
        elif m_exp_eyez == "front08":
            show m_exp_eyes 08

    return





# Test

image m_body_newPROVE = "images/general/characters/txell/m_body_newPROVE.webp"
image m_body_newPROVE02 = "images/general/characters/txell/m_body_newPROVE02.webp"

# Body

image m_exp_hair_front = SaturateTint("images/general/characters/txell/m_exp_hair_front.webp")

image m_bodynew naked_normal = SaturateTint("images/general/characters/txell/m_body_naked_normal.webp")
image m_bodynew naked_hips = SaturateTint("images/general/characters/txell/m_body_naked_hips.webp")
image m_bodynew naked_down = SaturateTint("images/general/characters/txell/m_body_naked_down.webp")
image m_bodynew naked_down_dirt = SaturateTint("images/general/characters/txell/m_body_naked_down_dirt.webp")
image m_bodynew naked_rest = SaturateTint("images/general/characters/txell/m_body_naked_rest.webp")

image m_bodynew relax_02 = SaturateTint("images/general/characters/txell/m_body_relax_02.webp")
image m_bodynew relax_03 = SaturateTint("images/general/characters/txell/m_body_relax_03.webp")
image m_bodynew hips_04 = SaturateTint("images/general/characters/txell/m_body_hips_04.webp")

image m_armL empty = "images/general/empty.webp"
image m_armL fingerLicking = SaturateTint("images/general/characters/txell/m_armL_fingerLicking.webp")
image m_armL fingerSucking = SaturateTint("images/general/characters/txell/m_armL_fingerSucking.webp")

# Blush

image m_exp_blush empty = "images/general/empty.webp"
image m_exp_blush 00 = SaturateTint("images/general/empty.webp")
image m_exp_blush 01 = SaturateTint("images/general/characters/txell/m_exp_blush_01.webp")
image m_exp_blush 02 = SaturateTint("images/general/characters/txell/m_exp_blush_02.webp")
image m_exp_blush 03 = SaturateTint("images/general/characters/txell/m_exp_blush_03.webp")
image m_exp_blush 04 = SaturateTint("images/general/characters/txell/m_exp_blush_04.webp")
image m_exp_blush 05 = SaturateTint("images/general/characters/txell/m_exp_blush_05.webp")
image m_exp_blush 06 = SaturateTint("images/general/characters/txell/m_exp_blush_06.webp")

# Eyebrows

image m_exp_eyebrows angryx01 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_angryx01.webp")
image m_exp_eyebrows angryx02 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_angryx02.webp")
image m_exp_eyebrows angryx03 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_angryx03.webp")
image m_exp_eyebrows angryx04 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_angryx04.webp")
image m_exp_eyebrows angryx05 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_angryx05.webp")
image m_exp_eyebrows angryx06 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_angryx06.webp")
image m_exp_eyebrows angryx07 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_angryx07.webp")
image m_exp_eyebrows normal = SaturateTint("images/general/characters/txell/m_exp_eyebrows_normal.webp")
image m_exp_eyebrows sadx01 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_sadx01.webp")
image m_exp_eyebrows sadx02 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_sadx02.webp")
image m_exp_eyebrows sadx03 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_sadx03.webp")
image m_exp_eyebrows sadx04 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_sadx04.webp")
image m_exp_eyebrows sadx05 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_sadx05.webp")
image m_exp_eyebrows sadx06 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_sadx06.webp")
image m_exp_eyebrows sadx07 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_sadx07.webp")
image m_exp_eyebrows serious = SaturateTint("images/general/characters/txell/m_exp_eyebrows_serious.webp")
image m_exp_eyebrows surprisex001 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_surprisex001.webp")
image m_exp_eyebrows surprisex002 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_surprisex002.webp")
image m_exp_eyebrows surprisex01 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_surprisex01.webp")
image m_exp_eyebrows surprisex02 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_surprisex02.webp")
image m_exp_eyebrows surprisex03 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_surprisex03.webp")
image m_exp_eyebrows surprisex04 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_surprisex04.webp")
image m_exp_eyebrows suspiciousx01 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_suspiciousx01.webp")
image m_exp_eyebrows suspiciousx02 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_suspiciousx02.webp")
image m_exp_eyebrows suspiciousx03 = SaturateTint("images/general/characters/txell/m_exp_eyebrows_suspiciousx03.webp")

# Eyes

image m_exp_eyes 00 = SaturateTint("images/general/characters/txell/m_exp_eyes_00.webp")
image m_exp_eyes 01 = SaturateTint("images/general/characters/txell/m_exp_eyes_01.webp")
image m_exp_eyes 02 = SaturateTint("images/general/characters/txell/m_exp_eyes_02.webp")
image m_exp_eyes 03 = SaturateTint("images/general/characters/txell/m_exp_eyes_03.webp")
image m_exp_eyes 04 = SaturateTint("images/general/characters/txell/m_exp_eyes_04.webp")
image m_exp_eyes 05 = SaturateTint("images/general/characters/txell/m_exp_eyes_05.webp")
image m_exp_eyes 06 = SaturateTint("images/general/characters/txell/m_exp_eyes_06.webp")
image m_exp_eyes 07 = SaturateTint("images/general/characters/txell/m_exp_eyes_07.webp")
image m_exp_eyes 08 = SaturateTint("images/general/characters/txell/m_exp_eyes_08.webp")

# Mouth

image m_exp_mouth special_tongueOut = SaturateTint("images/general/characters/txell/m_exp_mouth_special_tongueOut[mmouthp].webp")

image m_exp_mouth happybiting_Silentx01 = SaturateTint("images/general/characters/txell/m_exp_mouth_happybiting_Silentx01[mmouthp].webp")
image m_exp_mouth happybiting_Silentx02 = SaturateTint("images/general/characters/txell/m_exp_mouth_happybiting_Silentx02[mmouthp].webp")
image m_exp_mouth happybiting_Silentx03 = SaturateTint("images/general/characters/txell/m_exp_mouth_happybiting_Silentx03[mmouthp].webp")
image m_exp_mouth happybiting_Silentx04 = SaturateTint("images/general/characters/txell/m_exp_mouth_happybiting_Silentx04[mmouthp].webp")
image m_exp_mouth happybiting_Silentx05 = SaturateTint("images/general/characters/txell/m_exp_mouth_happybiting_Silentx05[mmouthp].webp")
image m_exp_mouth happybiting_Silentx06 = SaturateTint("images/general/characters/txell/m_exp_mouth_happybiting_Silentx06[mmouthp].webp")
image m_exp_mouth happybiting_Silentx07 = SaturateTint("images/general/characters/txell/m_exp_mouth_happybiting_Silentx07[mmouthp].webp")
image m_exp_mouth happybiting_Silentx08 = SaturateTint("images/general/characters/txell/m_exp_mouth_happybiting_Silentx08[mmouthp].webp")
image m_exp_mouth happybiting_Silentx09 = SaturateTint("images/general/characters/txell/m_exp_mouth_happybiting_Silentx09[mmouthp].webp")
image m_exp_mouth happybiting_Silentx10 = SaturateTint("images/general/characters/txell/m_exp_mouth_happybiting_Silentx10[mmouthp].webp")

image m_exp_mouth happy_Silentx01 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Silentx01[mmouthp].webp")
image m_exp_mouth happy_Silentx02 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Silentx02[mmouthp].webp")
image m_exp_mouth happy_Silentx03 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Silentx03[mmouthp].webp")
image m_exp_mouth happy_Silentx04 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Silentx04[mmouthp].webp")
image m_exp_mouth happy_Silentx05 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Silentx05[mmouthp].webp")
image m_exp_mouth happy_Silentx06 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Silentx06[mmouthp].webp")
image m_exp_mouth happy_Silentx07 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Silentx07[mmouthp].webp")
image m_exp_mouth happy_Silentx08 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Silentx08[mmouthp].webp")
image m_exp_mouth happy_Silentx09 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Silentx09[mmouthp].webp")
image m_exp_mouth happy_Silentx10 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Silentx10[mmouthp].webp")
image m_exp_mouth happy_Silentx11 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Silentx11[mmouthp].webp")
image m_exp_mouth happy_Silentx12 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Silentx12[mmouthp].webp")
image m_exp_mouth happy_Silentx13 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Silentx13[mmouthp].webp")
image m_exp_mouth happy_Silentx14 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Silentx14[mmouthp].webp")

image m_exp_mouth happy_Talkingx01 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Talkingx01[mmouthp].webp")
image m_exp_mouth happy_Talkingx02 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Talkingx02[mmouthp].webp")
image m_exp_mouth happy_Talkingx03 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Talkingx03[mmouthp].webp")
image m_exp_mouth happy_Talkingx04 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Talkingx04[mmouthp].webp")
image m_exp_mouth happy_Talkingx05 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Talkingx05[mmouthp].webp")
image m_exp_mouth happy_Talkingx06 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Talkingx06[mmouthp].webp")
image m_exp_mouth happy_Talkingx07 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Talkingx07[mmouthp].webp")
image m_exp_mouth happy_Talkingx08 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Talkingx08[mmouthp].webp")
image m_exp_mouth happy_Talkingx09 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Talkingx09[mmouthp].webp")
image m_exp_mouth happy_Talkingx10 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Talkingx10[mmouthp].webp")
image m_exp_mouth happy_Talkingx11 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Talkingx11[mmouthp].webp")
image m_exp_mouth happy_Talkingx12 = SaturateTint("images/general/characters/txell/m_exp_mouth_happy_Talkingx12[mmouthp].webp")

image m_exp_mouth serious_Silentx01 = SaturateTint("images/general/characters/txell/m_exp_mouth_serious_Silentx01[mmouthp].webp")

image m_exp_mouth sadbiting_Silentx01 = SaturateTint("images/general/characters/txell/m_exp_mouth_sadbiting_Silentx01[mmouthp].webp")
image m_exp_mouth sadbiting_Silentx02 = SaturateTint("images/general/characters/txell/m_exp_mouth_sadbiting_Silentx02[mmouthp].webp")
image m_exp_mouth sadbiting_Silentx03 = SaturateTint("images/general/characters/txell/m_exp_mouth_sadbiting_Silentx03[mmouthp].webp")
image m_exp_mouth sadbiting_Silentx04 = SaturateTint("images/general/characters/txell/m_exp_mouth_sadbiting_Silentx04[mmouthp].webp")
image m_exp_mouth sadbiting_Silentx05 = SaturateTint("images/general/characters/txell/m_exp_mouth_sadbiting_Silentx05[mmouthp].webp")
image m_exp_mouth sadbiting_Silentx06 = SaturateTint("images/general/characters/txell/m_exp_mouth_sadbiting_Silentx06[mmouthp].webp")
image m_exp_mouth sadbiting_Silentx07 = SaturateTint("images/general/characters/txell/m_exp_mouth_sadbiting_Silentx07[mmouthp].webp")
image m_exp_mouth sadbiting_Silentx08 = SaturateTint("images/general/characters/txell/m_exp_mouth_sadbiting_Silentx08[mmouthp].webp")
image m_exp_mouth sadbiting_Silentx09 = SaturateTint("images/general/characters/txell/m_exp_mouth_sadbiting_Silentx09[mmouthp].webp")
image m_exp_mouth sadbiting_Silentx10 = SaturateTint("images/general/characters/txell/m_exp_mouth_sadbiting_Silentx10[mmouthp].webp")
image m_exp_mouth sadbiting_Silentx11 = SaturateTint("images/general/characters/txell/m_exp_mouth_sadbiting_Silentx11[mmouthp].webp")

image m_exp_mouth sad_Silentx01 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Silentx01[mmouthp].webp")
image m_exp_mouth sad_Silentx02 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Silentx02[mmouthp].webp")
image m_exp_mouth sad_Silentx03 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Silentx03[mmouthp].webp")
image m_exp_mouth sad_Silentx04 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Silentx04[mmouthp].webp")
image m_exp_mouth sad_Silentx05 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Silentx05[mmouthp].webp")
image m_exp_mouth sad_Silentx06 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Silentx06[mmouthp].webp")
image m_exp_mouth sad_Silentx07 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Silentx07[mmouthp].webp")
image m_exp_mouth sad_Silentx08 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Silentx08[mmouthp].webp")
image m_exp_mouth sad_Silentx09 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Silentx09[mmouthp].webp")
image m_exp_mouth sad_Silentx10 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Silentx10[mmouthp].webp")
image m_exp_mouth sad_Silentx11 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Silentx11[mmouthp].webp")
image m_exp_mouth sad_Silentx12 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Silentx12[mmouthp].webp")
image m_exp_mouth sad_Silentx13 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Silentx13[mmouthp].webp")
image m_exp_mouth sad_Silentx14 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Silentx14[mmouthp].webp")
image m_exp_mouth sad_Silentx15 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Silentx15[mmouthp].webp")

image m_exp_mouth sad_Talkingx01 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx01[mmouthp].webp")
image m_exp_mouth sad_Talkingx02 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx02[mmouthp].webp")
image m_exp_mouth sad_Talkingx03 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx03[mmouthp].webp")
image m_exp_mouth sad_Talkingx04 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx04[mmouthp].webp")
image m_exp_mouth sad_Talkingx05 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx05[mmouthp].webp")
image m_exp_mouth sad_Talkingx06 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx06[mmouthp].webp")
image m_exp_mouth sad_Talkingx07 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx07[mmouthp].webp")
image m_exp_mouth sad_Talkingx08 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx08[mmouthp].webp")
image m_exp_mouth sad_Talkingx09 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx09[mmouthp].webp")
image m_exp_mouth sad_Talkingx10 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx10[mmouthp].webp")
image m_exp_mouth sad_Talkingx11 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx11[mmouthp].webp")
image m_exp_mouth sad_Talkingx12 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx12[mmouthp].webp")

image m_exp_mouth sad_Talkingx001 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx001[mmouthp].webp")
image m_exp_mouth sad_Talkingx002 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx002[mmouthp].webp")
image m_exp_mouth sad_Talkingx003 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx003[mmouthp].webp")
image m_exp_mouth sad_Talkingx004 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx004[mmouthp].webp")
image m_exp_mouth sad_Talkingx005 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx005[mmouthp].webp")
image m_exp_mouth sad_Talkingx006 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx006[mmouthp].webp")
image m_exp_mouth sad_Talkingx007 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx007[mmouthp].webp")
image m_exp_mouth sad_Talkingx008 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx008[mmouthp].webp")
image m_exp_mouth sad_Talkingx009 = SaturateTint("images/general/characters/txell/m_exp_mouth_sad_Talkingx009[mmouthp].webp")

# Piris

image m_exp_piris empty = "images/general/empty.webp"

image m_exp_piris down00 = SaturateTint("images/general/characters/txell/m_exp_piris_down00[meyesc].webp")
image m_exp_piris down01 = SaturateTint("images/general/characters/txell/m_exp_piris_down01[meyesc].webp")
image m_exp_piris down02 = SaturateTint("images/general/characters/txell/m_exp_piris_down02[meyesc].webp")
image m_exp_piris down03 = SaturateTint("images/general/characters/txell/m_exp_piris_down03[meyesc].webp")
image m_exp_piris down04 = SaturateTint("images/general/characters/txell/m_exp_piris_down04[meyesc].webp")
image m_exp_piris down05 = SaturateTint("images/general/characters/txell/m_exp_piris_down05[meyesc].webp")

image m_exp_piris front00 = SaturateTint("images/general/characters/txell/m_exp_piris_front00[meyesc].webp")
image m_exp_piris front01 = SaturateTint("images/general/characters/txell/m_exp_piris_front00[meyesc].webp")
image m_exp_piris front02 = SaturateTint("images/general/characters/txell/m_exp_piris_front02[meyesc].webp")
image m_exp_piris front03 = SaturateTint("images/general/characters/txell/m_exp_piris_front03[meyesc].webp")
image m_exp_piris front04 = SaturateTint("images/general/characters/txell/m_exp_piris_front04[meyesc].webp")
image m_exp_piris front05 = SaturateTint("images/general/characters/txell/m_exp_piris_front05[meyesc].webp")
image m_exp_piris front06 = "images/general/empty.webp"
image m_exp_piris front07 = "images/general/empty.webp"
image m_exp_piris front08 = "images/general/empty.webp"

image m_exp_piris front03_red = SaturateTint("images/general/characters/txell/m_exp_piris_front03_red.webp")

image m_exp_piris front00b = SaturateTint("images/general/characters/txell/m_exp_piris_front00b[meyesc].webp")
image m_exp_piris front01b = SaturateTint("images/general/characters/txell/m_exp_piris_front01b[meyesc].webp")
image m_exp_piris front02b = SaturateTint("images/general/characters/txell/m_exp_piris_front02b[meyesc].webp") # Don´t exist
image m_exp_piris front03b = SaturateTint("images/general/characters/txell/m_exp_piris_front03b[meyesc].webp") # Don´t exist
image m_exp_piris front04b = SaturateTint("images/general/characters/txell/m_exp_piris_front04b[meyesc].webp") # Don´t exist

image m_exp_piris left00 = SaturateTint("images/general/characters/txell/m_exp_piris_left00[meyesc].webp")
image m_exp_piris left01 = SaturateTint("images/general/characters/txell/m_exp_piris_left01[meyesc].webp")
image m_exp_piris left02 = SaturateTint("images/general/characters/txell/m_exp_piris_left02[meyesc].webp")
image m_exp_piris left03 = SaturateTint("images/general/characters/txell/m_exp_piris_left03[meyesc].webp")
image m_exp_piris left04 = SaturateTint("images/general/characters/txell/m_exp_piris_left04[meyesc].webp")
image m_exp_piris left05 = SaturateTint("images/general/characters/txell/m_exp_piris_left05[meyesc].webp")

image m_exp_piris right00 = SaturateTint("images/general/characters/txell/m_exp_piris_right00[meyesc].webp")
image m_exp_piris right01 = SaturateTint("images/general/characters/txell/m_exp_piris_right01[meyesc].webp")
image m_exp_piris right02 = SaturateTint("images/general/characters/txell/m_exp_piris_right02[meyesc].webp")
image m_exp_piris right03 = SaturateTint("images/general/characters/txell/m_exp_piris_right03[meyesc].webp")
image m_exp_piris right04 = SaturateTint("images/general/characters/txell/m_exp_piris_right04[meyesc].webp")
image m_exp_piris right05 = SaturateTint("images/general/characters/txell/m_exp_piris_right05[meyesc].webp")

## HAND

image m_hand drying = SaturateTint("images/general/characters/txell/m_hand_drying.webp")

############################################################################################
###########################################################################################

    ## Security Agent

image m_body guard = SaturateTint("images/general/characters/txell/m_body_guard.webp")
image m_arm_r guard_hip = SaturateTint("images/general/characters/txell/m_arm_r_guard_hip.webp")
image m_arm_r guard_pointing = SaturateTint("images/general/characters/txell/m_arm_r_guard_pointing.webp")
image m_exp_over hat = SaturateTint("images/general/characters/txell/m_exp_over_hat.webp")

############################################################################################
###########################################################################################
##########################################################################################
#########################################################################################
########################################################################################
#######################################################################################

image draft_metric = "images/draft_metric.webp"
image square100 = "images/square100.webp"
image greyTest = SaturateTint("images/greyTest.webp")

image bg night05_bg_castle_siege_stairs_bg = "images/day05/night/night05_bg_castle_siege_stairs_bg.webp"

image night05_bg_castle_siege_stairs_stairs_l = "images/day05/night/night05_bg_castle_siege_stairs_stairs_l.webp"
image night05_bg_castle_siege_stairs_stairs_r = "images/day05/night/night05_bg_castle_siege_stairs_stairs_r.webp"

image bg night05_bg_castle_siege_stairs_door = "images/day05/night/night05_bg_castle_siege_stairs_door.webp"

image bg night05_bg_castle_siege_stairs_comp:

    contains:
        "bg night05_bg_castle_siege_stairs_bg"
        transform_anchor True
        xalign 0.667 yalign 0.182

    #contains:
        #"red"
        #alpha 0.5


    contains:
        "night05_bg_castle_siege_stairs_stairs_l"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.505 ypos 2.63
        alpha 1.0
        block:
            easein_quad 0.5 ypos 2.5
            easeout_quad 0.5 ypos 2.7
            repeat

    contains:
        "night05_bg_castle_siege_stairs_stairs_r"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.505 ypos 2.63
        alpha 1.0
        block:
            easeout_quad 0.5 ypos 2.7
            easein_quad 0.5 ypos 2.5
            repeat


############################################################################################
###########################################################################################
##########################################################################################
#########################################################################################
########################################################################################
#######################################################################################

image Others_PROVE = "images/general/characters/others/Others_Prove.webp"




    ## DON´T FORGET: transform_anchor True

    ## Bellhop

image bellhop_body_PROVE = "images/general/characters/others/bellhop_body_PROVE.webp"
# xalign 0.5 yalign 0.239 # bellhop body align
# zoom 0.2 xpos 0.8 ypos 0.15 # bellhop pos (body and expressions)

image bellhop_arm_l_back relax = SaturateTint("images/general/characters/others/bellhop_arm_l_back_relax.webp")
image bellhop_arm_r_back relax = SaturateTint("images/general/characters/others/bellhop_arm_r_back_relax.webp")
image bellhop_arm_r_front candle = SaturateTint("images/general/characters/others/bellhop_arm_r_front_candle.webp")
image bellhop_arm_r_front holdhat_down = SaturateTint("images/general/characters/others/bellhop_arm_r_front_holdhat_down.webp")
image bellhop_arm_r_front holdhat_up = SaturateTint("images/general/characters/others/bellhop_arm_r_front_holdhat_up.webp")
image bellhop_body = SaturateTint("images/general/characters/others/bellhop_body.webp")

image bellhop_light_candle = "images/general/characters/others/bellhop_light_candle.webp"

image bellhop_exp_hat down = SaturateTint("images/general/characters/others/bellhop_exp_hat_down.webp")
image bellhop_exp_hat up = SaturateTint("images/general/characters/others/bellhop_exp_hat_up.webp")

image bellhop_exp_eyebrows serious = SaturateTint("images/general/characters/others/bellhop_exp_eyebrows_serious.webp")
image bellhop_exp_eyes 03 = SaturateTint("images/general/characters/others/bellhop_exp_eyes_03.webp")
image bellhop_exp_piris front03 = SaturateTint("images/general/characters/others/bellhop_exp_piris_front03.webp")
image bellhop_exp_piris_light front03 = SaturateTint("images/general/characters/others/bellhop_exp_piris_light_front03.webp")

image bellhop_exp_mouth happy_Silentx02 = SaturateTint("images/general/characters/others/bellhop_exp_mouth_happy_Silentx02.webp")
image bellhop_exp_mouth happy_Talkingx02 = SaturateTint("images/general/characters/others/bellhop_exp_mouth_happy_Talkingx02.webp")
image bellhop_exp_mouth sad_Silentx02 = SaturateTint("images/general/characters/others/bellhop_exp_mouth_sad_Silentx02.webp")
image bellhop_exp_mouth sad_Talkingx01 = SaturateTint("images/general/characters/others/bellhop_exp_mouth_sad_Talkingx01.webp")
image bellhop_exp_mouth sad_Talkingx02 = SaturateTint("images/general/characters/others/bellhop_exp_mouth_sad_Talkingx02.webp")
image bellhop_exp_mouth sad_Talkingx03 = SaturateTint("images/general/characters/others/bellhop_exp_mouth_sad_Talkingx03.webp")
image bellhop_exp_mouth sad_Talkingx04 = SaturateTint("images/general/characters/others/bellhop_exp_mouth_sad_Talkingx04.webp")

transform bellhop_body_align:
    transform_anchor True
    xalign 0.5 yalign 0.2425 #0.239
    xpos 0.5 ypos 0.5

transform bellhop_expressions_align:
    transform_anchor True
    xalign 0.5 yalign 0.5
    xpos 0.5 ypos 0.5

transform bellhop_atleft_pos:
    subpixel True
    zoom 0.2 xpos 0.2 ypos 0.15

transform bellhop_light_candle_trans:
    bellhop_body_align
    additive 1.0
    alpha 0.5
    block:
        easein_quad 0.15 alpha 0.5
        easein_quad 0.15 alpha 0.4
        easein_quad 0.15 alpha 0.45
        easein_quad 0.15 alpha 0.3
        easein_quad 0.15 alpha 0.4
        easein_quad 0.15 alpha 0.33
        easein_quad 0.15 alpha 0.35
        easein_quad 0.15 alpha 0.4
        easein_quad 0.15 alpha 0.2
        easein_quad 0.15 alpha 0.35
        easein_quad 0.15 alpha 0.4
        easein_quad 0.15 alpha 0.3
        easein_quad 0.15 alpha 0.33
        easein_quad 0.15 alpha 0.2
        easein_quad 0.15 alpha 0.5
        repeat



    # contains:
    #     "bellhop_flame_01"
    #     subpixel True
    #     bellhop_flame_align
    #     block:
    #         easein_quad 0.15 alpha 1.5
    #         easein_quad 0.15 alpha 0.0
    #         pause 0.15
    #         pause 0.15
    #         easein_quad 0.15 alpha 0.0
    #         repeat


image bellhop_candle_comp sad_Silent:

    contains:
        "bg_dark_a_Tint"
        truecenter
        zoom 6.0 rotate 90 ypos 2.5
    
    contains:
        "bellhop_arm_l_back relax"
        bellhop_body_align

    contains:
        "bellhop_body"
        bellhop_body_align

    contains:
        "bellhop_arm_r_front candle"
        bellhop_body_align

    # contains:
    #     "bellhop_body_PROVE"
    #     bellhop_body_align
    #     alpha 0.5

    contains:
        "bellhop_exp_mouth sad_Silentx02"
        bellhop_expressions_align

    contains:
        "bellhop_exp_hat down"
        bellhop_expressions_align

    contains:
        "bellhop_light_candle"
        bellhop_light_candle_trans

    contains:
        "bellhop_flame_anim"
        bellhop_flame_align
        additive 1.0
        zoom 0.5 xpos 0.28 ypos 1.66


image bellhop_candle_comp sad_Talkingx01:

    contains:
        "bg_dark_a_Tint"
        truecenter
        zoom 6.0 rotate 90 ypos 2.5
    
    contains:
        "bellhop_arm_l_back relax"
        bellhop_body_align

    contains:
        "bellhop_body"
        bellhop_body_align

    contains:
        "bellhop_arm_r_front candle"
        bellhop_body_align

    contains:
        "bellhop_exp_mouth sad_Talkingx01"
        bellhop_expressions_align

    contains:
        "bellhop_exp_hat down"
        bellhop_expressions_align

    contains:
        "bellhop_light_candle"
        bellhop_light_candle_trans

    contains:
        "bellhop_flame_anim"
        bellhop_flame_align
        additive 1.0
        zoom 0.5 xpos 0.28 ypos 1.66

image bellhop_candle_comp sad_Talkingx02:

    contains:
        "bg_dark_a_Tint"
        truecenter
        zoom 6.0 rotate 90 ypos 2.5
    
    contains:
        "bellhop_arm_l_back relax"
        bellhop_body_align

    contains:
        "bellhop_body"
        bellhop_body_align

    contains:
        "bellhop_arm_r_front candle"
        bellhop_body_align

    contains:
        "bellhop_exp_mouth sad_Talkingx02"
        bellhop_expressions_align

    contains:
        "bellhop_exp_hat down"
        bellhop_expressions_align

    contains:
        "bellhop_light_candle"
        bellhop_light_candle_trans

    contains:
        "bellhop_flame_anim"
        bellhop_flame_align
        additive 1.0
        zoom 0.5 xpos 0.28 ypos 1.66

image bellhop_candle_comp sad_Talkingx03:

    contains:
        "bg_dark_a_Tint"
        truecenter
        zoom 6.0 rotate 90 ypos 2.5
    
    contains:
        "bellhop_arm_l_back relax"
        bellhop_body_align

    contains:
        "bellhop_body"
        bellhop_body_align

    contains:
        "bellhop_arm_r_front candle"
        bellhop_body_align

    contains:
        "bellhop_exp_mouth sad_Talkingx03"
        bellhop_expressions_align

    contains:
        "bellhop_exp_hat down"
        bellhop_expressions_align

    contains:
        "bellhop_light_candle"
        bellhop_light_candle_trans

    contains:
        "bellhop_flame_anim"
        bellhop_flame_align
        additive 1.0
        zoom 0.5 xpos 0.28 ypos 1.66

image bellhop_candle_comp sad_Talkingx04:

    contains:
        "bg_dark_a_Tint"
        truecenter
        zoom 6.0 rotate 90 ypos 2.5
    
    contains:
        "bellhop_arm_l_back relax"
        bellhop_body_align

    contains:
        "bellhop_body"
        bellhop_body_align

    contains:
        "bellhop_arm_r_front candle"
        bellhop_body_align

    contains:
        "bellhop_exp_mouth sad_Talkingx04"
        bellhop_expressions_align

    contains:
        "bellhop_exp_hat down"
        bellhop_expressions_align

    contains:
        "bellhop_light_candle"
        bellhop_light_candle_trans

    contains:
        "bellhop_flame_anim"
        bellhop_flame_align
        additive 1.0
        zoom 0.5 xpos 0.28 ypos 1.66

#####################
##################

image bellhop_afterelevator_comp sad_Silent:

    contains:
        "white"
        truecenter
        zoom 6.0 rotate 90 ypos 2.5
    
    contains:
        "bellhop_arm_l_back relax"
        bellhop_body_align

    contains:
        "bellhop_arm_r_back relax"
        bellhop_body_align

    contains:
        "bellhop_body"
        bellhop_body_align
    
    contains:
        "bellhop_exp_mouth sad_Silentx02"
        bellhop_expressions_align

    contains:
        "bellhop_exp_eyes 03"
        bellhop_expressions_align

    contains:
        "bellhop_exp_piris front03"
        bellhop_expressions_align

    contains:
        "bellhop_exp_eyebrows serious"
        bellhop_expressions_align

    contains:
        "bellhop_exp_hat down"
        bellhop_expressions_align

    
image bellhop_afterelevator_comp sad_Talkingx03:

    contains:
        "white"
        truecenter
        zoom 6.0 rotate 90 ypos 2.5
    
    contains:
        "bellhop_arm_l_back relax"
        bellhop_body_align

    contains:
        "bellhop_body"
        bellhop_body_align
    
    contains:
        "bellhop_exp_mouth sad_Talkingx03"
        bellhop_expressions_align

    contains:
        "bellhop_exp_eyes 03"
        bellhop_expressions_align

    contains:
        "bellhop_exp_piris front03"
        bellhop_expressions_align

    contains:
        "bellhop_exp_eyebrows serious"
        bellhop_expressions_align

    contains:
        "bellhop_exp_hat down"
        bellhop_expressions_align
        
    contains:
        "bellhop_arm_r_front holdhat_down"
        bellhop_body_align
    

image bellhop_afterelevator_comp sad_Talkingx02:

    contains:
        "white"
        truecenter
        zoom 6.0 rotate 90 ypos 2.5
    
    contains:
        "bellhop_arm_l_back relax"
        bellhop_body_align

    contains:
        "bellhop_body"
        bellhop_body_align
    
    contains:
        "bellhop_exp_mouth sad_Talkingx02"
        bellhop_expressions_align

    contains:
        "bellhop_exp_eyes 03"
        bellhop_expressions_align

    contains:
        "bellhop_exp_piris front03"
        bellhop_expressions_align

    contains:
        "bellhop_exp_eyebrows serious"
        bellhop_expressions_align

    contains:
        "bellhop_exp_hat down"
        bellhop_expressions_align

    contains:
        "bellhop_arm_r_front holdhat_down"
        bellhop_body_align

image bellhop_afterelevator_comp happy_Silentx02:

    contains:
        "white"
        truecenter
        zoom 6.0 rotate 90 ypos 2.5
    
    contains:
        "bellhop_arm_l_back relax"
        bellhop_body_align

    contains:
        "bellhop_body"
        bellhop_body_align
    
    contains:
        "bellhop_exp_mouth happy_Silentx02"
        bellhop_expressions_align

    contains:
        "bellhop_exp_eyes 03"
        bellhop_expressions_align

    contains:
        "bellhop_exp_piris front03"
        bellhop_expressions_align

    contains:
        "bellhop_exp_eyebrows serious"
        bellhop_expressions_align

    contains:
        "bellhop_exp_hat down"
        bellhop_expressions_align

    contains:
        "bellhop_arm_r_front holdhat_down"
        bellhop_body_align

image bellhop_afterelevator_comp happy_Silentx02_eyes:

    contains:
        "white"
        truecenter
        zoom 6.0 rotate 90 ypos 2.5
    
    contains:
        "bellhop_arm_l_back relax"
        bellhop_body_align

    contains:
        "bellhop_body"
        bellhop_body_align
    
    contains:
        "bellhop_exp_mouth happy_Silentx02"
        bellhop_expressions_align

    contains:
        "bellhop_exp_eyes 03"
        bellhop_expressions_align

    contains:
        "bellhop_exp_piris front03"
        bellhop_expressions_align

    contains:
        "bellhop_exp_eyebrows serious"
        bellhop_expressions_align

    contains:
        "bellhop_exp_hat up"
        bellhop_expressions_align

    contains:
        "bellhop_arm_r_front holdhat_up"
        bellhop_body_align

    contains:
        "black"
        subpixel True
        truecenter
        zoom 6.0 rotate 90
        alpha 0.0
        pause 1.0
        easein_quad 3.0 alpha 1.0

    contains:
        "bellhop_exp_piris_light front03"
        subpixel True
        bellhop_expressions_align
        additive 1.0
        alpha 0.0
        pause 0.5
        easein_quad 4.0 alpha 1.0

############################################################################################
###########################################################################################
##########################################################################################

image bellhop_flame_01 = "images/general/characters/others/bellhop_flame_01.webp"
image bellhop_flame_02 = "images/general/characters/others/bellhop_flame_02.webp"
image bellhop_flame_03 = "images/general/characters/others/bellhop_flame_03.webp"
image bellhop_flame_04 = "images/general/characters/others/bellhop_flame_04.webp"
image bellhop_flame_05 = "images/general/characters/others/bellhop_flame_05.webp"

transform bellhop_flame_align:
    transform_anchor True
    xalign 0.55 yalign 0.85



image bellhop_flame_anim:

    contains:
        "bellhop_flame_01"
        subpixel True
        bellhop_flame_align
        block:
            easein_quad 0.15 alpha 1.5
            easein_quad 0.15 alpha 0.0
            pause 0.15
            pause 0.15
            easein_quad 0.15 alpha 0.0
            repeat
    contains:
        "bellhop_flame_02"
        subpixel True
        bellhop_flame_align
        block:
            easein_quad 0.15 alpha 0.0
            easein_quad 0.15 alpha 1.5
            easein_quad 0.15 alpha 0.0
            pause 0.15
            pause 0.15
            
            repeat
    contains:
        "bellhop_flame_03"
        subpixel True
        bellhop_flame_align
        block:
            pause 0.15
            easein_quad 0.15 alpha 0.0
            easein_quad 0.15 alpha 1.5
            easein_quad 0.15 alpha 0.0
            pause 0.15
            repeat
    contains:
        "bellhop_flame_04"
        subpixel True
        bellhop_flame_align
        block:
            pause 0.15
            pause 0.15
            easein_quad 0.15 alpha 0.0
            easein_quad 0.15 alpha 1.5
            easein_quad 0.15 alpha 0.0
            repeat
    contains:
        "bellhop_flame_05"
        subpixel True
        bellhop_flame_align
        block:
            easein_quad 0.15 alpha 0.0
            pause 0.15
            pause 0.15
            easein_quad 0.15 alpha 0.0
            easein_quad 0.15 alpha 1.5
            repeat



##########################################################################
#####################################
##########################################################################

    ## Neus Adult

image nadult_body_PROVE = "images/general/characters/others/nadult_body_PROVE.webp"

transform nadult_body_align:
    #transform_anchor True # DON´T USE it!
    xalign 0.5 yalign 0.244
transform nadult_expressions_align:
    xalign 0.5 yalign 0.5

transform nadult_atrigh_pos:
    subpixel True
    zoom 0.2 xpos 0.75 ypos 0.16

transform nadult_atleft_pos:
    subpixel True
    zoom 0.2 xpos 0.35 ypos 0.16 

transform nadult_center_pos:
    subpixel True
    zoom 0.2 xpos 0.5 ypos 0.16 


# xalign 0.5 yalign 0.244 # nadult body align
# zoom 0.2 xpos 0.75 ypos 0.16 # nadult pos (body and expressions) Can be WRONG

image nadult_body_hotel = SaturateTint("images/general/characters/others/nadult_body_hotel.webp")
image nadult_body_hotel_bright = SaturateTint("images/general/characters/others/nadult_body_hotel_bright.webp")

image nadult_exp_hair_front = SaturateTint("images/general/characters/others/nadult_exp_hair_front.webp")

image nadult_exp_eyebrows angryx02 = SaturateTint("images/general/characters/others/nadult_exp_eyebrows_angryx02.webp")
image nadult_exp_eyebrows normal = SaturateTint("images/general/characters/others/nadult_exp_eyebrows_normal.webp")
image nadult_exp_eyebrows serious = SaturateTint("images/general/characters/others/nadult_exp_eyebrows_serious.webp")
image nadult_exp_eyebrows surprisex02 = SaturateTint("images/general/characters/others/nadult_exp_eyebrows_surprisex02.webp")

image nadult_exp_eyes 01 = SaturateTint("images/general/characters/others/nadult_exp_eyes_01.webp")
image nadult_exp_eyes 02 = SaturateTint("images/general/characters/others/nadult_exp_eyes_02.webp")
image nadult_exp_eyes 03 = SaturateTint("images/general/characters/others/nadult_exp_eyes_03.webp")
image nadult_exp_eyes 04 = SaturateTint("images/general/characters/others/nadult_exp_eyes_04.webp")
image nadult_exp_eyes 05 = SaturateTint("images/general/characters/others/nadult_exp_eyes_05.webp")
image nadult_exp_eyes 06 = SaturateTint("images/general/characters/others/nadult_exp_eyes_06.webp")
image nadult_exp_eyes 07 = SaturateTint("images/general/characters/others/nadult_exp_eyes_07.webp")


image nadult_exp_piris empty = "images/general/empty.webp"
image nadult_exp_piris front01 = SaturateTint("images/general/characters/others/nadult_exp_piris_front01.webp")
image nadult_exp_piris front02 = SaturateTint("images/general/characters/others/nadult_exp_piris_front02.webp")
image nadult_exp_piris front03 = SaturateTint("images/general/characters/others/nadult_exp_piris_front03.webp")
image nadult_exp_piris front04 = SaturateTint("images/general/characters/others/nadult_exp_piris_front04.webp")
image nadult_exp_piris front05 = "images/general/empty.webp"
image nadult_exp_piris front06 = "images/general/empty.webp"
image nadult_exp_piris front07 = "images/general/empty.webp"

image nadult_exp_mouth happy_Silentx01 = SaturateTint("images/general/characters/others/nadult_exp_mouth_happy_Silentx01.webp")
image nadult_exp_mouth happy_Silentx02 = SaturateTint("images/general/characters/others/nadult_exp_mouth_happy_Silentx02.webp")
image nadult_exp_mouth happy_Silentx03 = SaturateTint("images/general/characters/others/nadult_exp_mouth_happy_Silentx03.webp")
image nadult_exp_mouth happy_Silentx04 = SaturateTint("images/general/characters/others/nadult_exp_mouth_happy_Silentx04.webp")
image nadult_exp_mouth happy_Silentx05 = SaturateTint("images/general/characters/others/nadult_exp_mouth_happy_Silentx05.webp")
image nadult_exp_mouth happy_Silentx06 = SaturateTint("images/general/characters/others/nadult_exp_mouth_happy_Silentx06.webp")

image nadult_exp_mouth happy_Talkingx01 = SaturateTint("images/general/characters/others/nadult_exp_mouth_happy_Talkingx01.webp")
image nadult_exp_mouth happy_Talkingx02 = SaturateTint("images/general/characters/others/nadult_exp_mouth_happy_Talkingx02.webp")
image nadult_exp_mouth happy_Talkingx03 = SaturateTint("images/general/characters/others/nadult_exp_mouth_happy_Talkingx03.webp")
image nadult_exp_mouth happy_Talkingx04 = SaturateTint("images/general/characters/others/nadult_exp_mouth_happy_Talkingx04.webp")
image nadult_exp_mouth happy_Talkingx05 = SaturateTint("images/general/characters/others/nadult_exp_mouth_happy_Talkingx05.webp")
image nadult_exp_mouth happy_Talkingx06 = SaturateTint("images/general/characters/others/nadult_exp_mouth_happy_Talkingx06.webp")

image nadult_exp_mouth sad_Silentx01 = SaturateTint("images/general/characters/others/nadult_exp_mouth_sad_Silentx01.webp")
image nadult_exp_mouth sad_Silentx02 = SaturateTint("images/general/characters/others/nadult_exp_mouth_sad_Silentx02.webp")
image nadult_exp_mouth sad_Silentx03 = SaturateTint("images/general/characters/others/nadult_exp_mouth_sad_Silentx03.webp")
image nadult_exp_mouth sad_Silentx04 = SaturateTint("images/general/characters/others/nadult_exp_mouth_sad_Silentx04.webp")
image nadult_exp_mouth sad_Silentx05 = SaturateTint("images/general/characters/others/nadult_exp_mouth_sad_Silentx05.webp")
image nadult_exp_mouth sad_Silentx06 = SaturateTint("images/general/characters/others/nadult_exp_mouth_sad_Silentx06.webp")

image nadult_exp_mouth sad_Talkingx01 = SaturateTint("images/general/characters/others/nadult_exp_mouth_sad_Talkingx01.webp")
image nadult_exp_mouth sad_Talkingx02 = SaturateTint("images/general/characters/others/nadult_exp_mouth_sad_Talkingx02.webp")
image nadult_exp_mouth sad_Talkingx03 = SaturateTint("images/general/characters/others/nadult_exp_mouth_sad_Talkingx03.webp")
image nadult_exp_mouth sad_Talkingx04 = SaturateTint("images/general/characters/others/nadult_exp_mouth_sad_Talkingx04.webp")
image nadult_exp_mouth sad_Talkingx05 = SaturateTint("images/general/characters/others/nadult_exp_mouth_sad_Talkingx05.webp")
image nadult_exp_mouth sad_Talkingx06 = SaturateTint("images/general/characters/others/nadult_exp_mouth_sad_Talkingx06.webp")


image nadult_encounter_comp:

    contains:
        "night05_hotel_hall_reception_blur"
        truecenter
        zoom 5.5 rotate 90 ypos 2.5

    contains:
        "nadult_body_hotel"
        nadult_body_align
        xpos 0.5 ypos 0.5

    contains:
        "nadult_body_hotel_bright"
        nadult_body_align
        additive 1.0
        xpos 0.5 ypos 0.5

    contains:
        "nadult_exp_eyebrows angryx02"
        nadult_expressions_align
        xpos 0.5 ypos 0.5


    contains:
        "nadult_exp_eyes 03"
        nadult_expressions_align
        xpos 0.5 ypos 0.5

    contains:
        "nadult_exp_piris front03"
        nadult_expressions_align
        xpos 0.5 ypos 0.5

    contains:
        "nadult_exp_mouth happy_Silentx03"
        nadult_expressions_align
        xpos 0.5 ypos 0.5

    contains:
        "nadult_exp_hair_front"
        nadult_expressions_align
        xpos 0.5 ypos 0.5

##########################################################################
#####################################
##########################################################################

    ## Neus Old


image nold_body_PROVE = "images/general/characters/others/nold_body_PROVE.webp"
# xalign 0.5 yalign 0.345 # nold EXPRESSIONS align
# xalign 0.5 yalign 0.2565 # nold body align
# # xalign 0.5 yalign 0.299 # nold body align (Again?) (Because here I added transform_anchor, wich was not necessary!!! dumbass!)
# zoom 0.2 xpos 0.5 ypos 0.494 # nold pos (body and expressions)

transform nold_expression_align:
    transform_anchor True
    xalign 0.5 yalign 0.345
transform nold_body_align:
    transform_anchor True
    xalign 0.5 yalign 0.299

transform nold_centerclose_pos:
    subpixel True
    zoom 0.55 xpos 0.5 ypos 0.35

transform nold_tablefar_pos:
    subpixel True
    zoom 0.17 xpos 0.72 ypos 0.48


image nold_body_hotel = SaturateTint("images/general/characters/others/nold_body_hotel.webp")

image nold_exp_glasses = SaturateTint("images/general/characters/others/nold_exp_glasses.webp")

image nold_exp_eyebrows angryx01 = SaturateTint("images/general/characters/others/nold_exp_eyebrows_angryx01.webp")
image nold_exp_eyebrows angryx02 = SaturateTint("images/general/characters/others/nold_exp_eyebrows_angryx02.webp")
image nold_exp_eyebrows angryx03 = SaturateTint("images/general/characters/others/nold_exp_eyebrows_angryx03.webp")
image nold_exp_eyebrows angryx04 = SaturateTint("images/general/characters/others/nold_exp_eyebrows_angryx04.webp")
image nold_exp_eyebrows angryx05 = SaturateTint("images/general/characters/others/nold_exp_eyebrows_angryx05.webp")
image nold_exp_eyebrows normal = SaturateTint("images/general/characters/others/nold_exp_eyebrows_normal.webp")
image nold_exp_eyebrows sadx01 = SaturateTint("images/general/characters/others/nold_exp_eyebrows_sadx01.webp")
image nold_exp_eyebrows sadx02 = SaturateTint("images/general/characters/others/nold_exp_eyebrows_sadx02.webp")
image nold_exp_eyebrows sadx03 = SaturateTint("images/general/characters/others/nold_exp_eyebrows_sadx03.webp")
image nold_exp_eyebrows sadx04 = SaturateTint("images/general/characters/others/nold_exp_eyebrows_sadx04.webp")
image nold_exp_eyebrows serious = SaturateTint("images/general/characters/others/nold_exp_eyebrows_serious.webp")
image nold_exp_eyebrows surprisex01 = SaturateTint("images/general/characters/others/nold_exp_eyebrows_surprisex01.webp")
image nold_exp_eyebrows surprisex02 = SaturateTint("images/general/characters/others/nold_exp_eyebrows_surprisex02.webp")

image nold_exp_eyes 01 = SaturateTint("images/general/characters/others/nold_exp_eyes_01.webp")
image nold_exp_eyes 03 = SaturateTint("images/general/characters/others/nold_exp_eyes_03.webp")
image nold_exp_eyes 05 = SaturateTint("images/general/characters/others/nold_exp_eyes_05.webp")
image nold_exp_eyes 07 = SaturateTint("images/general/characters/others/nold_exp_eyes_07.webp")

image nold_exp_piris empty = "images/general/empty.webp"

image nold_exp_piris front01 = SaturateTint("images/general/characters/others/nold_exp_piris_front01.webp")
image nold_exp_piris front03 = SaturateTint("images/general/characters/others/nold_exp_piris_front03.webp")
image nold_exp_piris front05 = "images/general/empty.webp"
image nold_exp_piris front07 = "images/general/empty.webp"

image nold_exp_piris left01 = SaturateTint("images/general/characters/others/nold_exp_piris_left01.webp")
image nold_exp_piris left03 = SaturateTint("images/general/characters/others/nold_exp_piris_left03.webp")

image nold_exp_mouth sad_Silentx01 = SaturateTint("images/general/characters/others/nold_exp_mouth_sad_Silentx01.webp")
image nold_exp_mouth sad_Silentx02 = SaturateTint("images/general/characters/others/nold_exp_mouth_sad_Silentx02.webp")
image nold_exp_mouth sad_Silentx03 = SaturateTint("images/general/characters/others/nold_exp_mouth_sad_Silentx03.webp")
image nold_exp_mouth sad_Talkingx01 = SaturateTint("images/general/characters/others/nold_exp_mouth_sad_Talkingx01.webp")
image nold_exp_mouth sad_Talkingx02 = SaturateTint("images/general/characters/others/nold_exp_mouth_sad_Talkingx02.webp")
image nold_exp_mouth sad_Talkingx03 = SaturateTint("images/general/characters/others/nold_exp_mouth_sad_Talkingx03.webp")
image nold_exp_mouth sad_Talkingx04 = SaturateTint("images/general/characters/others/nold_exp_mouth_sad_Talkingx04.webp")

image nold_nose = SaturateTint("images/general/characters/others/nold_nose.webp")

image nold_hands = SaturateTint("images/general/characters/others/nold_hands.webp")
image nold_overhead = SaturateTint("images/general/characters/others/nold_overhead.webp")


############################################################################################
###########################################################################################
##########################################################################################
##
##
############################################################################################
###########################################################################################
##########################################################################################


image night05_hotel_entrance_door_far = "images/day05/night/hotel/night05_hotel_entrance_door_far.webp"

image night05_hotel_entrance_door close_down = "images/day05/night/hotel/night05_hotel_entrance_door_close_down.webp"
image night05_hotel_entrance_door close_up = "images/day05/night/hotel/night05_hotel_entrance_door_close_up.webp"
image night05_hotel_entrance_door open = "images/day05/night/hotel/night05_hotel_entrance_door_open.webp"

transform lightbulb_animation_01:
    subpixel True
    block:
        easein 0.1 alpha 1.0
        easein 0.1 alpha 0.5
        easein 0.05 alpha 0.8
        easein 0.15 alpha 0.2
        easein 0.5 alpha 0.5
        easein 0.2 alpha 0.9
        easein 0.1 alpha 1.0
        easein 0.5 alpha 0.5
        easein 2.0 alpha 1.0
        easein 0.1 alpha 0.1
        easein 0.2 alpha 0.8
        easein 0.11 alpha 0.2
        easein 2.0 alpha 1.0
        repeat

transform lightbulb_animation_02:
    subpixel True
    block:
        easein 0.8 alpha 1.0
        easein 0.7 alpha 0.9
        easein 1.0 alpha 0.8
        easein 0.6 alpha 0.9
        easein 0.8 alpha 1.0
        easein 0.5 alpha 0.9
        easein 0.6 alpha 1.0
        easein 0.8 alpha 0.8
        easein 2.0 alpha 1.0
        easein 0.8 alpha 0.9
        easein 0.7 alpha 0.8
        easein 0.9 alpha 0.9
        easein 3.0 alpha 1.0
        repeat

image night05_hotel_entrance_door_far_comp:

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "night05_hotel_entrance_door_far"
        truecenter
        additive 1.0
        lightbulb_animation_01

############################################################################################
###########################################################################################
##########################################################################################
##
##
############################################################################################
###########################################################################################
##########################################################################################


image night05_hotel_hall_dark = "images/day05/night/hotel/night05_hotel_hall_dark.webp"
#image night05_hotel_hall_light = "images/day05/night/hotel/night05_hotel_hall_light.webp"

image night05_hotel_hall_light_down = "images/day05/night/hotel/night05_hotel_hall_light_down.webp"
image night05_hotel_hall_light_top = "images/day05/night/hotel/night05_hotel_hall_light_top.webp"


image night05_hotel_hall_elevator_light = "images/day05/night/hotel/night05_hotel_hall_elevator_light.webp"
#image night05_hotel_hall_reception_01_b_comp = "images/day05/night/hotel/night05_hotel_hall_reception_01.webp" ## Old
image night05_hotel_hall_reception_blur_image = "images/day05/night/hotel/night05_hotel_hall_reception_blur_image.webp"
image night05_hotel_hall_reception_01_table = "images/day05/night/hotel/night05_hotel_hall_reception_01_table.webp"

image night05_hotel_hall_reception_01_light_onTop = "images/day05/night/hotel/night05_hotel_hall_reception_01_light_onTop.webp"
image night05_hotel_hall_reception_01_light_onDown = "images/day05/night/hotel/night05_hotel_hall_reception_01_light_onDown.webp"

image night05_hotel_hall_elevator_door_l = "images/day05/night/hotel/night05_hotel_hall_elevator_door_l.webp"
image night05_hotel_hall_elevator_door_r = "images/day05/night/hotel/night05_hotel_hall_elevator_door_r.webp"

image night05_hotel_hall_elevator_door_d_l = "images/day05/night/hotel/night05_hotel_hall_elevator_door_d_l.webp"
image night05_hotel_hall_elevator_door_d_r = "images/day05/night/hotel/night05_hotel_hall_elevator_door_d_r.webp"


image night05_hotel_hall_light_01 = "images/day05/night/hotel/night05_hotel_hall_light_01.webp"
image night05_hotel_hall_light_02 = "images/day05/night/hotel/night05_hotel_hall_light_02.webp"
image night05_hotel_hall_light_03 = "images/day05/night/hotel/night05_hotel_hall_light_03.webp"
image night05_hotel_hall_light_04 = "images/day05/night/hotel/night05_hotel_hall_light_04.webp"
image night05_hotel_hall_light_05 = "images/day05/night/hotel/night05_hotel_hall_light_05.webp"
image night05_hotel_hall_light_06 = "images/day05/night/hotel/night05_hotel_hall_light_06.webp"
image night05_hotel_hall_light_07 = "images/day05/night/hotel/night05_hotel_hall_light_07.webp"
image night05_hotel_hall_light_08 = "images/day05/night/hotel/night05_hotel_hall_light_08.webp"
image night05_hotel_hall_light_09 = "images/day05/night/hotel/night05_hotel_hall_light_09.webp"
image night05_hotel_hall_light_10 = "images/day05/night/hotel/night05_hotel_hall_light_10.webp"
image night05_hotel_hall_light_11 = "images/day05/night/hotel/night05_hotel_hall_light_11.webp"
image night05_hotel_hall_light_12 = "images/day05/night/hotel/night05_hotel_hall_light_12.webp"
image night05_hotel_hall_light_13 = "images/day05/night/hotel/night05_hotel_hall_light_13.webp"

transform candle_anim_01:
    alpha 0.4
    block:
        easein_quad 0.15 alpha 0.5
        easein_quad 0.15 alpha 0.4
        easein_quad 0.15 alpha 0.45
        easein_quad 0.15 alpha 0.3
        easein_quad 0.15 alpha 0.4
        easein_quad 0.15 alpha 0.33
        easein_quad 0.15 alpha 0.35
        easein_quad 0.15 alpha 0.4
        easein_quad 0.15 alpha 0.2
        easein_quad 0.15 alpha 0.35
        easein_quad 0.15 alpha 0.4
        easein_quad 0.15 alpha 0.3
        easein_quad 0.15 alpha 0.33
        easein_quad 0.15 alpha 0.2
        easein_quad 0.15 alpha 0.5
        repeat

        # Not so sudden.
transform candle_anim_02:
    alpha 0.5
    block:
        easein_quad 0.15 alpha 0.51
        easein_quad 0.15 alpha 0.48
        easein_quad 0.15 alpha 0.45
        easein_quad 0.15 alpha 0.52
        easein_quad 0.15 alpha 0.5
        easein_quad 0.15 alpha 0.49
        easein_quad 0.15 alpha 0.51
        easein_quad 0.15 alpha 0.48
        easein_quad 0.15 alpha 0.5
        easein_quad 0.15 alpha 0.53
        easein_quad 0.15 alpha 0.48
        easein_quad 0.15 alpha 0.5
        easein_quad 0.15 alpha 0.52
        easein_quad 0.15 alpha 0.58
        easein_quad 0.15 alpha 0.5
        repeat

transform candle_anim_03:
    alpha 0.8
    block:
        easein_quad 0.15 alpha 0.91
        easein_quad 0.15 alpha 0.98
        easein_quad 0.15 alpha 0.95
        easein_quad 0.15 alpha 0.92
        easein_quad 0.15 alpha 1.0
        easein_quad 0.15 alpha 0.99
        easein_quad 0.15 alpha 0.91
        easein_quad 0.15 alpha 0.98
        easein_quad 0.15 alpha 0.8
        easein_quad 0.15 alpha 0.93
        easein_quad 0.15 alpha 0.98
        easein_quad 0.15 alpha 1.0
        easein_quad 0.15 alpha 0.92
        easein_quad 0.15 alpha 0.98
        easein_quad 0.15 alpha 1.0
        repeat

transform candle_anim_04:
    alpha 0.8
    block:
        easein_quad 0.15 alpha 0.8
        easein_quad 0.2 alpha 0.98
        easein_quad 0.12 alpha 0.95
        easein_quad 0.15 alpha 0.92
        easein_quad 0.16 alpha 0.8
        easein_quad 0.1 alpha 0.99
        easein_quad 0.13 alpha 0.91
        easein_quad 0.15 alpha 0.98
        easein_quad 0.18 alpha 0.8
        easein_quad 0.15 alpha 0.93
        easein_quad 0.17 alpha 0.98
        easein_quad 0.19 alpha 1.0
        easein_quad 0.14 alpha 0.92
        easein_quad 0.13 alpha 0.98
        easein_quad 0.15 alpha 1.0
        repeat

transform candle_anim_05:
    alpha 0.8
    block:
        easein_quad 0.15 alpha 0.85
        easein_quad 0.2 alpha 0.99
        easein_quad 0.12 alpha 0.85
        easein_quad 0.15 alpha 0.96
        easein_quad 0.16 alpha 0.99
        easein_quad 0.1 alpha 0.95
        easein_quad 0.13 alpha 0.89
        easein_quad 0.15 alpha 0.92
        easein_quad 0.18 alpha 0.98
        easein_quad 0.15 alpha 0.9
        easein_quad 0.17 alpha 1.0
        easein_quad 0.19 alpha 0.89
        easein_quad 0.14 alpha 0.95
        easein_quad 0.13 alpha 0.8
        easein_quad 0.15 alpha 1.0
        repeat

image night05_hotel_hall_light:

    contains:
        "black"
        truecenter
        zoom 2.0

    # contains:
    #     "night05_hotel_hall_dark"
    #     truecenter

    contains:
        "night05_hotel_hall_light_down"
        truecenter
        alpha 2.0

    # contains:
    #     "night05_hotel_hall_light_top"
    #     truecenter
    #     additive 1.0
    #     candle_anim_02
    #     #lightbulb_animation_02

    contains:
        "night05_hotel_hall_light_01"
        truecenter
        additive 0.5
        candle_anim_03

    contains:
        "night05_hotel_hall_light_02"
        truecenter
        additive 0.5
        pause 0.02
        candle_anim_04

    contains:
        "night05_hotel_hall_light_03"
        truecenter
        additive 0.5
        pause 0.055
        candle_anim_05

    contains:
        "night05_hotel_hall_light_04"
        truecenter
        additive 0.5
        pause 0.07
        candle_anim_04
    contains:
        "night05_hotel_hall_light_05"
        truecenter
        additive 0.5
        pause 0.08
        candle_anim_03
    contains:
        "night05_hotel_hall_light_06"
        truecenter
        additive 0.5
        pause 0.095
        candle_anim_05
    contains:
        "night05_hotel_hall_light_07"
        truecenter
        additive 0.5
        pause 0.1
        candle_anim_04
    contains:
        "night05_hotel_hall_light_08"
        truecenter
        additive 0.5
        pause 0.12
        candle_anim_03
    contains:
        "night05_hotel_hall_light_09"
        truecenter
        additive 0.5
        pause 0.13
        candle_anim_05
    contains:
        "night05_hotel_hall_light_10"
        truecenter
        additive 0.5
        pause 0.15
        candle_anim_03
    contains:
        "night05_hotel_hall_light_11"
        truecenter
        additive 0.5
        pause 0.17
        candle_anim_04
    contains:
        "night05_hotel_hall_light_12"
        truecenter
        additive 0.5
        pause 0.19
        candle_anim_03
    contains:
        "night05_hotel_hall_light_13"
        truecenter
        additive 0.5
        pause 0.2
        candle_anim_05



image night05_hotel_hall_reception_blur:

    contains:
        "black"

    contains:
        "night05_hotel_hall_reception_blur_image"
        truecenter
        alpha 0.5

    contains:
        "night05_hotel_hall_reception_blur_image"
        truecenter
        additive 1.0
        candle_anim_01

image night05_hotel_hall_reception_01:

    contains:
        "night05_hotel_hall_reception_01_light_onDown"
        truecenter
    contains:
        "night05_hotel_hall_reception_01_light_onTop"
        truecenter
        candle_anim_01

image night05_hotel_hall_comp 00:

    contains:
        "night05_hotel_hall_dark"
        truecenter


image night05_hotel_hall_comp 01:

    contains:
        "night05_hotel_hall_dark"
        truecenter

    contains:
        "night05_hotel_hall_light"
        truecenter
        #additive 1.0
        alpha 0.0
        pause 1.0
        ease 10.0 alpha 1.0
        #lightbulb_animation_02

image night05_hotel_hall_comp 02:

    # contains:
    #     "night05_hotel_hall_dark"
    #     truecenter

    contains:
        "night05_hotel_hall_light"
        truecenter
        #additive 1.0
        #lightbulb_animation_02

image night05_hotel_hall_comp 03: #elevator getting darker.

    # contains:
    #     "night05_hotel_hall_dark"
    #     truecenter

    contains:
        "night05_hotel_hall_light"
        truecenter
        #additive 1.0
        #lightbulb_animation_02

    contains:
        "night05_hotel_hall_dark"
        truecenter
        alpha 0.0
        easein_quad 5.0 alpha 1.0

image night05_hotel_hall_comp 04: #elevator getting darker.

    contains:
        "night05_hotel_hall_dark"
        truecenter

    contains:
        "black"
        truecenter
        zoom 2.0 alpha 0.0
        pause 5.0
        easein_quad 5.0 alpha 1.0

    contains:
        "night05_hotel_hall_elevator_light"
        truecenter
        additive 1.0

image night05_hotel_hall_comp 05: #elevator dark.

    contains:
        "black"
        truecenter
        zoom 2.0 alpha 1.0

    contains:
        "night05_hotel_hall_elevator_light"
        truecenter
        additive 1.0

image night05_hotel_hall_reception_comp far_01:

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "night05_hotel_hall_reception_01"
        truecenter
        #lightbulb_animation_02

image night05_hotel_hall_reception_comp far_02:

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "night05_hotel_hall_reception_01"
        truecenter
        zoom 0.5

    contains:
        "nold_body_hotel"
        nold_body_align
        nold_tablefar_pos

    contains:
        "nold_exp_eyes 03"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_exp_piris front03"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_exp_eyebrows angryx03"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_exp_mouth sad_Silentx03"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_nose"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_exp_glasses"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_overhead"
        nold_body_align
        nold_tablefar_pos

    contains:
        "night05_hotel_hall_reception_table_comp far_01"
        truecenter
        zoom 0.5

    contains:
        "nold_hands"
        nold_body_align
        nold_tablefar_pos

image night05_hotel_hall_reception_comp far_03: #Recepcionist see Nadult.

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "night05_hotel_hall_reception_01"
        truecenter
        zoom 0.5

    contains:
        "nold_body_hotel"
        nold_body_align
        nold_tablefar_pos

    contains:
        "nold_exp_eyes 01"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_exp_piris front01"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_exp_eyebrows surprisex02"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_exp_mouth sad_Talkingx01"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_nose"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_exp_glasses"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_overhead"
        nold_body_align
        nold_tablefar_pos

    contains:
        "night05_hotel_hall_reception_table_comp far_01"
        truecenter
        zoom 0.5

    contains:
        "nold_hands"
        nold_body_align
        nold_tablefar_pos

image night05_hotel_hall_reception_comp far_04: #Recepcionist see Nadult. Sad

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "night05_hotel_hall_reception_01"
        truecenter
        zoom 0.5

    contains:
        "nold_body_hotel"
        nold_body_align
        nold_tablefar_pos

    contains:
        "nold_exp_eyes 03"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_exp_piris front03"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_exp_eyebrows sadx03"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_exp_mouth sad_Silentx03"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_nose"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_exp_glasses"
        nold_expression_align
        nold_tablefar_pos

    contains:
        "nold_overhead"
        nold_body_align
        nold_tablefar_pos

    contains:
        "night05_hotel_hall_reception_table_comp far_01"
        truecenter
        zoom 0.5

    contains:
        "nold_hands"
        nold_body_align
        nold_tablefar_pos

image night05_hotel_hall_reception_table_comp far_01:

    contains:
        "night05_hotel_hall_reception_01_table"
        truecenter
        #lightbulb_animation_02

###

image tv_PROVE = "images/day01/tv_PROVE.webp"

image bg tv_background = "images/day01/tv_background.webp"
image bg tv_background_off = "images/day01/tv_background_off.webp"
image bg tv_background_movie = "images/day01/tv_background_movie.webp"
image tv_left presentador = "images/day01/tv_left_presentador.webp"
image tv_right kid = "images/day01/tv_right_kid.webp"
image tv_right sagradafamilia = "images/day01/tv_right_sagradafamilia.webp"

image bg tv_kid_comp:

    contains:
        "bg tv_background"
        truecenter
    contains:
        "tv_left presentador"
        truecenter
        xpos -0.185 ypos 0.13
    contains:
        "tv_right kid"
        truecenter
        xpos 0.755 ypos 0.27

image bg tv_sagradafamilia_comp:

    contains:
        "bg tv_background"
        truecenter
    contains:
        "tv_left presentador"
        truecenter
        xpos -0.185 ypos 0.13
    contains:
        "tv_right sagradafamilia"
        truecenter
        xpos 0.755 ypos 0.27

#########################################

# image night05_tibidabo_medic_PROVE = "images/day05/night/night05_tibidabo_medic_PROVE.webp"

image night05_tibidabo_medic_body = SaturateTint("images/day05/night/night05_tibidabo_medic_body.webp")

image night05_tibidabo_medic_body_blurry Silent = SaturateTint("images/day05/night/night05_tibidabo_medic_body_blurry_Silent.webp")
image night05_tibidabo_medic_body_blurry Talking = SaturateTint("images/day05/night/night05_tibidabo_medic_body_blurry_Talking.webp")

image night05_tibidabo_medic_hair_front = SaturateTint("images/day05/night/night05_tibidabo_medic_hair_front.webp")

image night05_tibidabo_medic_hand = SaturateTint("images/day05/night/night05_tibidabo_medic_hand.webp")
image night05_tibidabo_medic_hand blurry = SaturateTint("images/day05/night/night05_tibidabo_medic_hand_blurry.webp")
image night05_tibidabo_medic_hand empty = "images/general/empty.webp"

image night05_tibidabo_medic_exp_eyebrows angryx01 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_eyebrows_angryx01.webp")
image night05_tibidabo_medic_exp_eyebrows angryx02 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_eyebrows_angryx02.webp")
image night05_tibidabo_medic_exp_eyebrows angryx03 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_eyebrows_angryx03.webp")
image night05_tibidabo_medic_exp_eyebrows sadx01 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_eyebrows_sadx01.webp")
image night05_tibidabo_medic_exp_eyebrows sadx02 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_eyebrows_sadx02.webp")
image night05_tibidabo_medic_exp_eyebrows sadx03 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_eyebrows_sadx03.webp")
image night05_tibidabo_medic_exp_eyebrows normal = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_eyebrows_normal.webp")
image night05_tibidabo_medic_exp_eyebrows serious = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_eyebrows_serious.webp")
image night05_tibidabo_medic_exp_eyebrows surprisex01 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_eyebrows_surprisex01.webp")
image night05_tibidabo_medic_exp_eyebrows suspiciousx01 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_eyebrows_suspiciousx01.webp")
image night05_tibidabo_medic_exp_eyebrows suspiciousx02 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_eyebrows_suspiciousx02.webp")

image night05_tibidabo_medic_exp_eyes 03 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_eyes_03.webp")
image night05_tibidabo_medic_exp_eyes 05 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_eyes_05.webp")
image night05_tibidabo_medic_exp_eyes 06 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_eyes_06.webp")
image night05_tibidabo_medic_exp_eyes 07 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_eyes_07.webp")

image night05_tibidabo_medic_exp_piris empty = "images/general/empty.webp"
image night05_tibidabo_medic_exp_piris front03 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_piris_front03.webp")
image night05_tibidabo_medic_exp_piris front05 = "images/general/empty.webp"
image night05_tibidabo_medic_exp_piris front06 = "images/general/empty.webp"
image night05_tibidabo_medic_exp_piris front07 = "images/general/empty.webp"
image night05_tibidabo_medic_exp_piris right03 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_piris_right03.webp")

image night05_tibidabo_medic_exp_mouth happy_Silentx01 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_mouth_happy_Silentx01.webp")
image night05_tibidabo_medic_exp_mouth happy_Silentx02 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_mouth_happy_Silentx02.webp")
image night05_tibidabo_medic_exp_mouth happy_Silentx03 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_mouth_happy_Silentx03.webp")
image night05_tibidabo_medic_exp_mouth happy_Silentx04 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_mouth_happy_Silentx04.webp")

image night05_tibidabo_medic_exp_mouth happy_Talkingx01 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_mouth_happy_Talkingx01.webp")
image night05_tibidabo_medic_exp_mouth happy_Talkingx02 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_mouth_happy_Talkingx02.webp")
image night05_tibidabo_medic_exp_mouth happy_Talkingx03 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_mouth_happy_Talkingx03.webp")

image night05_tibidabo_medic_exp_mouth sad_Silentx01 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_mouth_sad_Silentx01.webp")
image night05_tibidabo_medic_exp_mouth sad_Silentx02 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_mouth_sad_Silentx02.webp")
image night05_tibidabo_medic_exp_mouth sad_Silentx03 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_mouth_sad_Silentx03.webp")
image night05_tibidabo_medic_exp_mouth sad_Silentx04 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_mouth_sad_Silentx04.webp")
image night05_tibidabo_medic_exp_mouth sad_Silentx05 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_mouth_sad_Silentx05.webp")

image night05_tibidabo_medic_exp_mouth sad_Talkingx01 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_mouth_sad_Talkingx01.webp")
image night05_tibidabo_medic_exp_mouth sad_Talkingx02 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_mouth_sad_Talkingx02.webp")
image night05_tibidabo_medic_exp_mouth sad_Talkingx03 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_mouth_sad_Talkingx03.webp")
image night05_tibidabo_medic_exp_mouth sad_Talkingx04 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_mouth_sad_Talkingx04.webp")
image night05_tibidabo_medic_exp_mouth sad_Talkingx05 = SaturateTint("images/day05/night/night05_tibidabo_medic_exp_mouth_sad_Talkingx05.webp")

transform night05_tibidabo_medic_exp_pos:
    subpixel True
    truecenter
    zoom 0.5
    xpos 0.397 ypos 0.379
transform night05_tibidabo_medic_body:
    subpixel True
    truecenter
    zoom 0.5


########################################################################################################
#####################################################################################################################
########################################################################################################
##############################################################################

    ## room_01 CEMETERY
    # CLOSE

image bg room_01_cemetery_close_bg = "images/day05/night/hotel/room_01_cemetery/room_01_cemetery_close_bg.webp"

image room_01_cemetery_close_bodies = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_close_bodies.webp")
image room_01_cemetery_close_door_close = "images/day05/night/hotel/room_01_cemetery/room_01_cemetery_close_door_close.webp"
image room_01_cemetery_close_door_open = "images/day05/night/hotel/room_01_cemetery/room_01_cemetery_close_door_open.webp"
image room_01_cemetery_close_door_open_light = "images/day05/night/hotel/room_01_cemetery/room_01_cemetery_close_door_open_light.webp"

image room_01_cemetery_close_light = "images/day05/night/hotel/room_01_cemetery/room_01_cemetery_close_light.webp"

image room_01_cemetery_close_head camera = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_close_head_camera.webp")
image room_01_cemetery_close_head down = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_close_head_down.webp")




image room_01_cemetery_close_door_open_light_comp:
    contains:
        "room_01_cemetery_close_door_open"
    contains:
        "room_01_cemetery_close_door_open_light"
        light_flame_animation02

image room_01_cemetery_close_light_comp:
    "room_01_cemetery_close_light"
    light_flame_animation02


image bg room_01_cemetery_close_closed_comp:

    contains:
        "bg room_01_cemetery_close_bg"
        truecenter
    contains:
        "room_01_cemetery_close_door_close"
        truecenter
    contains:
        "room_01_cemetery_close_bodies"
        truecenter
    contains:
        "room_01_cemetery_close_light_comp"
        truecenter
    contains:
        "room_01_cemetery_close_head down"
        truecenter
    

image bg room_01_cemetery_close_open_comp:

    contains:
        "bg room_01_cemetery_close_bg"
        truecenter
    contains:
        "room_01_cemetery_close_door_open_light_comp"
        truecenter
    contains:
        "room_01_cemetery_close_bodies"
        truecenter
    contains:
        "room_01_cemetery_close_head down"
        truecenter
    contains:
        "night05_Cemetery_smoke_comp"
    contains:
        "room_01_cemetery_close_light_comp"
        truecenter
    

screen night05_hotel_room01_cemetery_close_doorout_screen():
    add "bg room_01_cemetery_close_bg" at screendissolve
    add "room_01_cemetery_close_bodies" at screendissolve
    imagebutton at hover_dissolve_transform:
        hover  "room_01_cemetery_close_door_open_light_comp"
        idle "room_01_cemetery_close_door_close"
        hover_sound "audio/sfx/door_old_short_open01.ogg"
        focus_mask "room_01_cemetery_close_door_close"
        #Displayable "room_01_cemetery_close_door_close"
        action Call("night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Close_Question")
        yanchor 0.5 xanchor 0.5
        xpos 0.5 ypos 0.5

    imagebutton at hover_dissolve_transform:
        hover  "room_01_cemetery_close_head camera"
        idle "room_01_cemetery_close_head down"
        #hover_sound "audio/sfx/door_old_short_open01.ogg"
        focus_mask "room_01_cemetery_close_bodies"
        action Jump("night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Close_Couple")
        yanchor 0.5 xanchor 0.5
        xpos 0.5 ypos 0.5
    add "night05_Cemetery_smoke_comp" at screendissolve
    add "room_01_cemetery_close_light_comp" at screendissolve
    

    #add "night05_Cemetery_smoke_comp" at screendissolve

    ## room_01 CEMETERY
    # CLOSER

image bg room_01_cemetery_closer_bg = "images/day05/night/hotel/room_01_cemetery/room_01_cemetery_closer_bg.webp"

image room_01_cemetery_closer_body = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_closer_body.webp")

image room_01_cemetery_closer_head camera = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_closer_head_camera.webp")
image room_01_cemetery_closer_head down = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_closer_head_down.webp")

image room_01_cemetery_closer_light = "images/day05/night/hotel/room_01_cemetery/room_01_cemetery_closer_light.webp"

    ## room_01 CEMETERY
    # MOTHER

# bg dark_a_blurry_01

image room_01_cemetery_mother_body = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_body.webp")

image room_01_cemetery_mother_exp_eyebrows sadx01 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_eyebrows_sadx01.webp")
image room_01_cemetery_mother_exp_eyebrows sadx02 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_eyebrows_sadx02.webp")
image room_01_cemetery_mother_exp_eyebrows sadx03 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_eyebrows_sadx03.webp")
image room_01_cemetery_mother_exp_eyebrows sadx04 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_eyebrows_sadx04.webp")
image room_01_cemetery_mother_exp_eyebrows sadx05 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_eyebrows_sadx05.webp")

image room_01_cemetery_mother_exp_eyebrows serious = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_eyebrows_serious.webp")
image room_01_cemetery_mother_exp_eyebrows normal = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_eyebrows_normal.webp")

image room_01_cemetery_mother_exp_eyes 02 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_eyes_02.webp")
image room_01_cemetery_mother_exp_eyes 04 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_eyes_04.webp")
image room_01_cemetery_mother_exp_eyes 05 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_eyes_05.webp")
image room_01_cemetery_mother_exp_eyes 06 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_eyes_06.webp")
image room_01_cemetery_mother_exp_eyes 07 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_eyes_07.webp")

#image room_01_cemetery_mother_exp_piris front04 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_piris_front04.webp")

image room_01_cemetery_mother_exp_tears 02_05 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_tears_02_05.webp")
image room_01_cemetery_mother_exp_tears 04_05 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_tears_02_05.webp")
image room_01_cemetery_mother_exp_tears 05_05 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_tears_02_05.webp")
image room_01_cemetery_mother_exp_tears 06_05 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_tears_06_05.webp")
image room_01_cemetery_mother_exp_tears 07_05 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_tears_07_05.webp")

image room_01_cemetery_mother_exp_mouth sad_Talkingx03 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_mouth_sad_Talkingx03.webp")
image room_01_cemetery_mother_exp_mouth sad_Talkingx04 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_mouth_sad_Talkingx04.webp")
image room_01_cemetery_mother_exp_mouth sad_Talkingx05 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_mouth_sad_Talkingx05.webp")

image room_01_cemetery_mother_exp_mouth sad_Silentx03 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_mouth_sad_Silentx03.webp")
image room_01_cemetery_mother_exp_mouth sad_Silentx04 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_mouth_sad_Silentx04.webp")
image room_01_cemetery_mother_exp_mouth sad_Silentx05 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_mouth_sad_Silentx05.webp")
image room_01_cemetery_mother_exp_mouth sad_Silentx06 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_mouth_sad_Silentx06.webp")
image room_01_cemetery_mother_exp_mouth sad_Silentx07 = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_exp_mouth_sad_Silentx07.webp")

image room_01_cemetery_mother_hands = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_hands.webp")
image room_01_cemetery_mother_veil = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_mother_veil.webp")

image room_01_cemetery_husband_hand = SaturateTint("images/day05/night/hotel/room_01_cemetery/room_01_cemetery_husband_hand.webp")
image room_01_cemetery_husband_hand empty = "images/general/empty.webp"

transform shake_hands:
    subpixel True
    parallel:
        easein_quad 0.10 xpos 0.508
        easein_quad 0.08 xpos 0.498
        easein_quad 0.16 xpos 0.502
        easein_quad 0.09 xpos 0.498
        repeat
    parallel:
        easein_quad 0.10 ypos 0.503
        easein_quad 0.08 ypos 0.498
        easein_quad 0.06 ypos 0.502
        easein_quad 0.09 ypos 0.499
        repeat


##############################################################################################################
############################################################################################################
##############################################################################################################
############################################################################################################
##############################################################################################################
############################################################################################################
##############################################################################################################
############################################################################################################


image room_02_child_hallway_bg_dark_HD = "images/day05/night/hotel/room_02_child/room_02_child_hallway_bg_dark_HD.webp"
image room_02_child_hallway_bg_lighting_HD = "images/day05/night/hotel/room_02_child/room_02_child_hallway_bg_lighting_HD.webp"

image room_02_child_hallway_door_bright = "images/day05/night/hotel/room_02_child/room_02_child_hallway_door_bright.webp"
image room_02_child_hallway_door_bright_mask = "images/day05/night/hotel/room_02_child/room_02_child_hallway_door_bright_mask.webp"


image room_02_child_hallway_but_toy_ball = "images/day05/night/hotel/room_02_child/room_02_child_hallway_but_toy_ball.webp"
image room_02_child_hallway_but_toy_warrior = "images/day05/night/hotel/room_02_child/room_02_child_hallway_but_toy_warrior.webp"
image room_02_child_hallway_but_toy_console = "images/day05/night/hotel/room_02_child/room_02_child_hallway_but_toy_console.webp"
image room_02_child_hallway_but_toy_slingshot = "images/day05/night/hotel/room_02_child/room_02_child_hallway_but_toy_slingshot.webp"
image room_02_child_hallway_but_toy_robot = "images/day05/night/hotel/room_02_child/room_02_child_hallway_but_toy_robot.webp"
image room_02_child_hallway_but_toy_piano = "images/day05/night/hotel/room_02_child/room_02_child_hallway_but_toy_piano.webp"

image room_02_child_hallway_but_photo_01 = "images/day05/night/hotel/room_02_child/room_02_child_hallway_but_photo_01.webp"
image room_02_child_hallway_but_photo_02 = "images/day05/night/hotel/room_02_child/room_02_child_hallway_but_photo_02.webp"
image room_02_child_hallway_but_photo_03 = "images/day05/night/hotel/room_02_child/room_02_child_hallway_but_photo_03.webp"
image room_02_child_hallway_but_photo_04 = "images/day05/night/hotel/room_02_child/room_02_child_hallway_but_photo_04.webp"
image room_02_child_hallway_but_photo_05 = "images/day05/night/hotel/room_02_child/room_02_child_hallway_but_photo_05.webp"

image room_02_child_hallway_but_photo_01_image = "images/day05/night/hotel/room_02_child/room_02_child_hallway_but_photo_01_image.webp"
image room_02_child_hallway_but_photo_02_image = "images/day05/night/hotel/room_02_child/room_02_child_hallway_but_photo_02_image.webp"
image room_02_child_hallway_but_photo_03_image = "images/day05/night/hotel/room_02_child/room_02_child_hallway_but_photo_03_image.webp"
image room_02_child_hallway_but_photo_04_image = "images/day05/night/hotel/room_02_child/room_02_child_hallway_but_photo_04_image.webp"
image room_02_child_hallway_but_photo_05_image = "images/day05/night/hotel/room_02_child/room_02_child_hallway_but_photo_05_image.webp"

image room_02_child_hallway_but_photo_01_image_dark = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_hallway_but_photo_01_image.webp")
image room_02_child_hallway_but_photo_02_image_dark = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_hallway_but_photo_02_image.webp")
image room_02_child_hallway_but_photo_03_image_dark = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_hallway_but_photo_03_image.webp")
image room_02_child_hallway_but_photo_04_image_dark = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_hallway_but_photo_04_image.webp")
image room_02_child_hallway_but_photo_05_image_dark = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_hallway_but_photo_05_image.webp")


image room_02_child_hallway_but_photo_01_image_comp:

    contains:
        "room_02_child_hallway_but_photo_01_image_dark"
        truecenter

    contains:
        "room_02_child_hallway_but_photo_01_image"
        room_02_child_hallway_bg_lighting_anim_01
    contains:
        "room_02_child_hallway_but_photo_01_image"
        room_02_child_hallway_bg_lighting_anim_02

image room_02_child_hallway_but_photo_02_image_comp:

    contains:
        "room_02_child_hallway_but_photo_02_image_dark"
        truecenter

    contains:
        "room_02_child_hallway_but_photo_02_image"
        room_02_child_hallway_bg_lighting_anim_01
    contains:
        "room_02_child_hallway_but_photo_02_image"
        room_02_child_hallway_bg_lighting_anim_02

image room_02_child_hallway_but_photo_03_image_comp:

    contains:
        "room_02_child_hallway_but_photo_03_image_dark"
        truecenter

    contains:
        "room_02_child_hallway_but_photo_03_image"
        room_02_child_hallway_bg_lighting_anim_01
    contains:
        "room_02_child_hallway_but_photo_03_image"
        room_02_child_hallway_bg_lighting_anim_02

image room_02_child_hallway_but_photo_04_image_comp:

    contains:
        "room_02_child_hallway_but_photo_04_image_dark"
        truecenter

    contains:
        "room_02_child_hallway_but_photo_04_image"
        room_02_child_hallway_bg_lighting_anim_01
    contains:
        "room_02_child_hallway_but_photo_04_image"
        room_02_child_hallway_bg_lighting_anim_02

image room_02_child_hallway_but_photo_05_image_comp:

    contains:
        "room_02_child_hallway_but_photo_05_image_dark"
        truecenter

    contains:
        "room_02_child_hallway_but_photo_05_image"
        room_02_child_hallway_bg_lighting_anim_01
    contains:
        "room_02_child_hallway_but_photo_05_image"
        room_02_child_hallway_bg_lighting_anim_02



screen room_02_child_hallway_buttons_screen():

    if room_02_child_hallway_but_toy_ball_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_hallway_but_toy_ball"
            idle "empty"
            #idle "empty" #Null() ## Null no funciona...
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_hallway_but_toy_ball"
            action Jump("room_02_child_hallway_but_toy_ball_label")
            #action Function(renpy.call, label="room_02_child_hallway_but_toy_ball_label") # It´s not the best option here.
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    #add "night05_Cemetery_smoke_comp"

    if room_02_child_hallway_but_toy_warrior_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_hallway_but_toy_warrior"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_hallway_but_toy_warrior"
            action Jump("room_02_child_hallway_but_toy_warrior_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_02_child_hallway_but_toy_console_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_hallway_but_toy_console"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_hallway_but_toy_console"
            action Jump("room_02_child_hallway_but_toy_console_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_02_child_hallway_but_toy_slingshot_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_hallway_but_toy_slingshot"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_hallway_but_toy_slingshot"
            action Jump("room_02_child_hallway_but_toy_slingshot_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_02_child_hallway_but_toy_piano_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_hallway_but_toy_piano"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_hallway_but_toy_piano"
            action Jump("room_02_child_hallway_but_toy_piano_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_02_child_hallway_but_toy_robot_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_hallway_but_toy_robot"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_hallway_but_toy_robot"
            action Jump("room_02_child_hallway_but_toy_robot_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    ##
    ##
    ##

    if room_02_child_hallway_but_photo_01_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_hallway_but_photo_01"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_hallway_but_photo_01"
            action Jump("room_02_child_hallway_but_photo_01_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_02_child_hallway_but_photo_02_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_hallway_but_photo_02"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_hallway_but_photo_02"
            action Jump("room_02_child_hallway_but_photo_02_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_02_child_hallway_but_photo_03_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_hallway_but_photo_03"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_hallway_but_photo_03"
            action Jump("room_02_child_hallway_but_photo_03_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_02_child_hallway_but_photo_04_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_hallway_but_photo_04"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_hallway_but_photo_04"
            action Jump("room_02_child_hallway_but_photo_04_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_02_child_hallway_but_photo_05_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_hallway_but_photo_05"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_hallway_but_photo_05"
            action Jump("room_02_child_hallway_but_photo_05_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    ###

    if room_02_child_hallway_door_bright_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_hallway_door_bright"
            idle "empty"
            hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_hallway_door_bright_mask"
            action Jump("room_02_child_hallway_door_bright_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    

transform storm_lighting_anim_01:
    subpixel True
    alpha 0.0
    additive 1.0
    block:
        pause 1.0
        easein_quad 0.08 alpha 0.5
        easein_quad 0.7 alpha 0.0
        pause 1.0
        easein_quad 0.08 alpha 0.7
        easein_quad 0.07 alpha 0.0
        easein_quad 0.05 alpha 0.8
        easein_quad 0.05 alpha 0.0
        easein_quad 0.03 alpha 0.6
        easein_quad 0.7 alpha 0.0
        pause 5.7
        easein_quad 0.1 alpha 0.5
        easein_quad 0.7 alpha 0.0
        pause 0.3
        easein_quad 0.01 alpha 0.8
        easein_quad 0.7 alpha 0.0
        pause 17.3
        easein_quad 0.1 alpha 0.5
        easein_quad 0.7 alpha 0.0
        pause 8.8
        easein_quad 0.1 alpha 0.7
        easein_quad 0.7 alpha 0.0
        pause 0.3
        easein_quad 0.02 alpha 0.7
        easein_quad 0.07 alpha 0.0
        easein_quad 0.05 alpha 0.8
        easein_quad 0.7 alpha 0.0
        pause 5.0
        repeat

transform storm_lighting_anim_02:
    subpixel True
    alpha 0.0
    additive 1.0
    pause 1.35
    block:
        easein_quad 0.05 alpha 0.5
        easein_quad 0.7 alpha 0.0
        pause 5.2
        easein_quad 0.05 alpha 0.7
        easein_quad 0.3 alpha 0.0
        easein_quad 0.05 alpha 0.8
        easein_quad 0.04 alpha 0.0
        easein_quad 0.03 alpha 0.6
        easein_quad 0.05 alpha 0.0
        easein_quad 0.04 alpha 0.5
        easein_quad 0.05 alpha 0.0
        easein_quad 0.1 alpha 0.6
        easein_quad 0.7 alpha 0.0
        pause 8.3
        easein_quad 0.05 alpha 0.7
        easein_quad 0.3 alpha 0.0
        easein_quad 0.05 alpha 0.8
        easein_quad 0.7 alpha 0.0
        pause 2.8
        easein_quad 0.1 alpha 0.7
        easein_quad 0.7 alpha 0.0
        pause 18.6
        repeat

transform room_02_child_hallway_bg_lighting_anim_01:
    subpixel True
    truecenter
    alpha 0.0
    additive 1.0
    block:
        pause 1.0
        easein_quad 0.08 alpha 0.5
        easein_quad 0.7 alpha 0.0
        pause 1.0
        easein_quad 0.08 alpha 0.7
        easein_quad 0.07 alpha 0.0
        easein_quad 0.05 alpha 0.8
        easein_quad 0.05 alpha 0.0
        easein_quad 0.03 alpha 0.6
        easein_quad 0.7 alpha 0.0
        pause 5.7
        easein_quad 0.1 alpha 0.5
        easein_quad 0.7 alpha 0.0
        pause 0.3
        easein_quad 0.01 alpha 0.8
        easein_quad 0.7 alpha 0.0
        pause 17.3
        easein_quad 0.1 alpha 0.5
        easein_quad 0.7 alpha 0.0
        pause 8.8
        easein_quad 0.1 alpha 0.7
        easein_quad 0.7 alpha 0.0
        pause 0.3
        easein_quad 0.02 alpha 0.7
        easein_quad 0.07 alpha 0.0
        easein_quad 0.05 alpha 0.8
        easein_quad 0.7 alpha 0.0
        pause 5.0
        repeat

transform room_02_child_hallway_bg_lighting_anim_02:
    subpixel True
    truecenter
    alpha 0.0
    additive 1.0
    pause 1.35
    block:
        easein_quad 0.05 alpha 0.5
        easein_quad 0.7 alpha 0.0
        pause 5.2
        easein_quad 0.05 alpha 0.7
        easein_quad 0.3 alpha 0.0
        easein_quad 0.05 alpha 0.8
        easein_quad 0.04 alpha 0.0
        easein_quad 0.03 alpha 0.6
        easein_quad 0.05 alpha 0.0
        easein_quad 0.04 alpha 0.5
        easein_quad 0.05 alpha 0.0
        easein_quad 0.1 alpha 0.6
        easein_quad 0.7 alpha 0.0
        pause 8.3
        easein_quad 0.05 alpha 0.7
        easein_quad 0.3 alpha 0.0
        easein_quad 0.05 alpha 0.8
        easein_quad 0.7 alpha 0.0
        pause 2.8
        easein_quad 0.1 alpha 0.7
        easein_quad 0.7 alpha 0.0
        pause 18.6
        repeat

image room_02_child_hallway_bg_dark_lighting_comp:

    contains:
        "room_02_child_hallway_bg_dark_HD"
        truecenter

    contains:
        "room_02_child_hallway_bg_lighting_HD"
        room_02_child_hallway_bg_lighting_anim_01
    contains:
        "room_02_child_hallway_bg_lighting_HD"
        room_02_child_hallway_bg_lighting_anim_02


image room_02_child_hallway_bg_dark_lighting_comp_close:

    contains:
        "room_02_child_hallway_bg_dark_HD"
        truecenter

    contains:
        "room_02_child_hallway_bg_lighting_HD"
        room_02_child_hallway_bg_lighting_anim_01
    contains:
        "room_02_child_hallway_bg_lighting_HD"
        room_02_child_hallway_bg_lighting_anim_02

image room_02_child_hallway_bg_dark_lighting_comp_open:

    contains:
        "room_02_child_hallway_bg_dark_HD"
        truecenter

    contains:
        "room_02_child_hallway_bg_lighting_HD"
        room_02_child_hallway_bg_lighting_anim_01
    contains:
        "room_02_child_hallway_bg_lighting_HD"
        room_02_child_hallway_bg_lighting_anim_02
    contains:
        "room_02_child_hallway_door_bright"
        truecenter
        zoom 5.0

##############################################################################################################
####################################################################################################

image room_02_child_room_bg_dark_HD = "images/day05/night/hotel/room_02_child/room_02_child_room_bg_dark_HD.webp"
image room_02_child_room_bg_lighting_HD = "images/day05/night/hotel/room_02_child/room_02_child_room_bg_lighting_HD.webp"
image room_02_child_room_bg_PROVE = "images/day05/night/hotel/room_02_child/room_02_child_room_bg_PROVE.webp"

image room_02_child_room_bg_bedover_dark_HD = "images/day05/night/hotel/room_02_child/room_02_child_room_bg_bedover_dark_HD.webp"
image room_02_child_room_bg_bedover_lighting_HD = "images/day05/night/hotel/room_02_child/room_02_child_room_bg_bedover_lighting_HD.webp"

image room_02_child_room_but_kid_dark_HD = "images/day05/night/hotel/room_02_child/room_02_child_room_but_kid_dark_HD.webp"
image room_02_child_room_but_kid_HD = "images/day05/night/hotel/room_02_child/room_02_child_room_but_kid_HD.webp"

image room_02_child_room_but_kid_button = "images/day05/night/hotel/room_02_child/room_02_child_room_but_kid_button.webp"
image room_02_child_room_but_kid_button_mask = "images/day05/night/hotel/room_02_child/room_02_child_room_but_kid_button_mask.webp"

image room_02_child_room_but_kid_dark = "images/day05/night/hotel/room_02_child/room_02_child_room_but_kid_dark.webp"

image room_02_child_room_but_exit = "images/day05/night/hotel/room_02_child/room_02_child_room_but_exit.webp"
image room_02_child_room_but_exit_mask = "images/day05/night/hotel/room_02_child/room_02_child_room_but_exit_mask.webp"

image room_02_child_room_but_object_blood = "images/day05/night/hotel/room_02_child/room_02_child_room_but_object_blood.webp"
image room_02_child_room_but_object_blood_mask = "images/day05/night/hotel/room_02_child/room_02_child_room_but_object_blood_mask.webp"
image room_02_child_room_but_object_cigarretes = "images/day05/night/hotel/room_02_child/room_02_child_room_but_object_cigarretes.webp"
image room_02_child_room_but_object_cigarretes_mask = "images/day05/night/hotel/room_02_child/room_02_child_room_but_object_cigarretes_mask.webp"
image room_02_child_room_but_object_coctels = "images/day05/night/hotel/room_02_child/room_02_child_room_but_object_coctels.webp"
image room_02_child_room_but_object_coctels_mask = "images/day05/night/hotel/room_02_child/room_02_child_room_but_object_coctels_mask.webp"
image room_02_child_room_but_object_condom = "images/day05/night/hotel/room_02_child/room_02_child_room_but_object_condom.webp"
image room_02_child_room_but_object_condom_mask = "images/day05/night/hotel/room_02_child/room_02_child_room_but_object_condom_mask.webp"
image room_02_child_room_but_object_drugs = "images/day05/night/hotel/room_02_child/room_02_child_room_but_object_drugs.webp"
image room_02_child_room_but_object_drugs_mask = "images/day05/night/hotel/room_02_child/room_02_child_room_but_object_drugs_mask.webp"
image room_02_child_room_but_object_wine = "images/day05/night/hotel/room_02_child/room_02_child_room_but_object_wine.webp"
image room_02_child_room_but_object_wine_mask = "images/day05/night/hotel/room_02_child/room_02_child_room_but_object_wine_mask.webp"

image room_02_child_room_bg_comp:

    contains:
        "room_02_child_room_background_comp_HD"
        truecenter

    contains:
        "room_02_child_room_kidblanket_HD"
        truecenter

    contains:
        "room_02_child_room_foreground_comp_HD"
        truecenter

transform room_02_child_room_kidblanket_anim_HD:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.75
    #xpos 1.35 ypos 1.45 alpha 1.0
    xpos 1.1647 ypos 1.26
    parallel:
        ease_quad 1.0 rotate .005
        ease_quad .7 rotate -.007
        repeat
    parallel:
        easein_quad .9 yzoom 1.001
        easein_quad .6 yzoom 0.995
        repeat
    parallel:
        easein_quad 1.0 xzoom 0.995
        easein_quad .5 xzoom 1.005
        repeat

image room_02_child_room_kidblanket_HD:
    # contains:
    #     "room_02_child_room_bg_PROVE"
    #     truecenter

    contains:
        "room_02_child_room_kidblanket_dark_comp_HD"
        room_02_child_room_kidblanket_anim_HD

image room_02_child_room_kidblanket_dark_comp_HD:
    contains:
        "room_02_child_room_but_kid_dark_HD"
        truecenter

    contains:
        "room_02_child_room_but_kid_HD"
        room_02_child_hallway_bg_lighting_anim_01
    contains:
        "room_02_child_room_but_kid_HD"
        room_02_child_hallway_bg_lighting_anim_02

image room_02_child_room_background_comp_HD:

    contains:
        "room_02_child_room_bg_dark_HD"
        truecenter
    contains:
        "room_02_child_room_bg_lighting_HD"
        room_02_child_hallway_bg_lighting_anim_01
    contains:
        "room_02_child_room_bg_lighting_HD"
        room_02_child_hallway_bg_lighting_anim_02

image room_02_child_room_foreground_comp_HD:

    contains:
        "room_02_child_room_bg_bedover_dark_HD"
        truecenter

    contains:
        "room_02_child_room_bg_bedover_lighting_HD"
        room_02_child_hallway_bg_lighting_anim_01
    contains:
        "room_02_child_room_bg_bedover_lighting_HD"
        room_02_child_hallway_bg_lighting_anim_02

###

image room_02_child_room_bg_comp_close:

    contains:
        "room_02_child_room_background_comp_HD"
        truecenter

    contains:
        "room_02_child_room_kidblanket_HD"
        truecenter

    contains:
        "room_02_child_room_foreground_comp_HD"
        truecenter

image room_02_child_room_bg_comp_doorlight:

    contains:
        "room_02_child_room_background_comp_HD"
        truecenter

    contains:
        "room_02_child_room_kidblanket_HD"
        truecenter

    contains:
        "room_02_child_room_foreground_comp_HD"
        truecenter

    contains:
        "room_02_child_room_but_exit"
        truecenter
        zoom 5.0

screen room_02_child_room_buttons_screen():

    if room_02_child_room_but_object_blood_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_room_but_object_blood"
            idle "empty"
            #idle "empty" #Null() ## Null no funciona...
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_room_but_object_blood_mask"
            action Jump("room_02_child_room_but_object_blood_label")
            #action Function(renpy.call, label="room_02_child_hallway_but_toy_ball_label") # It´s not the best option here.
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_02_child_room_but_object_cigarretes_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_room_but_object_cigarretes"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_room_but_object_cigarretes_mask"
            action Jump("room_02_child_room_but_object_cigarretes_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_02_child_room_but_object_coctels_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_room_but_object_coctels"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_room_but_object_coctels_mask"
            action Jump("room_02_child_room_but_object_coctels_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_02_child_room_but_object_condom_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_room_but_object_condom"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_room_but_object_condom_mask"
            action Jump("room_02_child_room_but_object_condom_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_02_child_room_but_object_drugs_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_room_but_object_drugs"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_room_but_object_drugs_mask"
            action Jump("room_02_child_room_but_object_drugs_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_02_child_room_but_object_wine_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_02_child_room_but_object_wine"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_02_child_room_but_object_wine_mask"
            action Jump("room_02_child_room_but_object_wine_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    imagebutton at hover_dissolve_transform:
        hover "room_02_child_room_but_kid_button"
        idle "empty"
        hover_sound "audio/sfx/fall07.ogg"
        focus_mask "room_02_child_room_but_kid_button_mask"
        action Jump("room_02_child_room_but_kid_label")
        yanchor 0.5 xanchor 0.5
        xpos 0.5 ypos 0.5

    #add "room_02_child_room_foreground_comp"

    imagebutton at hover_dissolve_transform:
        hover "room_02_child_room_but_exit"
        idle "empty"
        hover_sound "audio/sfx/door_old_short_open01.ogg"
        focus_mask "room_02_child_room_but_exit_mask"
        action Jump("room_02_child_room_but_exit_label")
        yanchor 0.5 xanchor 0.5
        xpos 0.5 ypos 0.5




##############################################################################################################
####################################################################################################
##############################################################################################################
####################################################################################################
##############################################################################################################
####################################################################################################


image room_03_marriage_far_HD = "images/day05/night/hotel/room_03_church/room_03_marriage_far_HD.webp"
image room_03_marriage_far_HD_close = "images/day05/night/hotel/room_03_church/room_03_marriage_far_HD.webp"

image room_03_marriage_far_but_door = "images/day05/night/hotel/room_03_church/room_03_marriage_far_but_door.webp"
image room_03_marriage_far_but_door_mask = "images/day05/night/hotel/room_03_church/room_03_marriage_far_but_door_mask.webp"
image room_03_marriage_far_but_woman = "images/day05/night/hotel/room_03_church/room_03_marriage_far_but_woman.webp"

image room_03_marriage_far_but_object_bouquet = "images/day05/night/hotel/room_03_church/room_03_marriage_far_but_object_bouquet.webp"
image room_03_marriage_far_but_object_cake = "images/day05/night/hotel/room_03_church/room_03_marriage_far_but_object_cake.webp"
image room_03_marriage_far_but_object_chocolates = "images/day05/night/hotel/room_03_church/room_03_marriage_far_but_object_chocolates.webp"
image room_03_marriage_far_but_object_petals = "images/day05/night/hotel/room_03_church/room_03_marriage_far_but_object_petals.webp"
image room_03_marriage_far_but_object_petals_b = "images/day05/night/hotel/room_03_church/room_03_marriage_far_but_object_petals_b.webp"
image room_03_marriage_far_but_object_rings = "images/day05/night/hotel/room_03_church/room_03_marriage_far_but_object_rings.webp"
image room_03_marriage_far_but_object_vows = "images/day05/night/hotel/room_03_church/room_03_marriage_far_but_object_vows.webp"


image room_03_marriage_far_HD_door_bright:

    contains:
        "room_03_marriage_far_HD"
        truecenter

    contains:
        "room_03_marriage_far_but_door"
        truecenter
        zoom 5.0

image room_03_marriage_far_but_woman_02:
    contains:
        "room_03_marriage_far_but_woman"
        alpha 0.5
image room_03_marriage_far_but_object_bouquet_02:
    contains:
        "room_03_marriage_far_but_object_bouquet"
        alpha 0.5
image room_03_marriage_far_but_object_cake_02:
    contains:
        "room_03_marriage_far_but_object_cake"
        alpha 0.5
image room_03_marriage_far_but_object_chocolates_02:
    contains:
        "room_03_marriage_far_but_object_chocolates"
        alpha 0.5
image room_03_marriage_far_but_object_petals_02:
    contains:
        "room_03_marriage_far_but_object_petals_b"
        alpha 0.5
image room_03_marriage_far_but_object_rings_02:
    contains:
        "room_03_marriage_far_but_object_rings"
        alpha 0.5
image room_03_marriage_far_but_object_vows_02:
    contains:
        "room_03_marriage_far_but_object_vows"
        alpha 0.5

screen room_03_marriage_far_buttons_screen():

    if room_03_marriage_far_door_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_03_marriage_far_but_door"
            idle "empty"
            hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_03_marriage_far_but_door_mask"
            action Jump("room_03_marriage_far_but_door_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_03_marriage_far_woman_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_03_marriage_far_but_woman_02"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_03_marriage_far_but_woman"
            action Jump("room_03_marriage_far_but_woman_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_03_marriage_far_but_object_petals_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_03_marriage_far_but_object_petals_02"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_03_marriage_far_but_object_petals"
            action Jump("room_03_marriage_far_but_object_petals_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_03_marriage_far_but_object_bouquet_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_03_marriage_far_but_object_bouquet_02"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_03_marriage_far_but_object_bouquet"
            action Jump("room_03_marriage_far_but_object_bouquet_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_03_marriage_far_but_object_cake_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_03_marriage_far_but_object_cake_02"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_03_marriage_far_but_object_cake"
            action Jump("room_03_marriage_far_but_object_cake_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_03_marriage_far_but_object_chocolates_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_03_marriage_far_but_object_chocolates_02"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_03_marriage_far_but_object_chocolates"
            action Jump("room_03_marriage_far_but_object_chocolates_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_03_marriage_far_but_object_rings_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_03_marriage_far_but_object_rings_02"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_03_marriage_far_but_object_rings"
            action Jump("room_03_marriage_far_but_object_rings_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

    if room_03_marriage_far_but_object_vows_Cond == False:

        imagebutton at hover_dissolve_transform:
            hover "room_03_marriage_far_but_object_vows_02"
            idle "empty"
            #hover_sound "audio/sfx/door_old_short_open01.ogg"
            focus_mask "room_03_marriage_far_but_object_vows"
            action Jump("room_03_marriage_far_but_object_vows_label")
            yanchor 0.5 xanchor 0.5
            xpos 0.5 ypos 0.5

##############################


##############################

    # Room Close (KID)


image room_02_child_bed_bg = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_bg.webp")
image room_02_child_bed_bg_PROVE = "images/day05/night/hotel/room_02_child/room_02_child_bed_bg_PROVE.webp"

image room_02_child_bed_sheet 01 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_sheet_01.webp")
image room_02_child_bed_sheet 02 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_sheet_02.webp")
image room_02_child_bed_sheet 03 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_sheet_03.webp")

transform room_02_child_bed_kid_exp_pos:
    subpixel True
    truecenter
    zoom 0.5
    xpos 0.53 ypos 0.495

image room_02_child_bed_kid_exp_eyebrows empty = "images/general/empty.webp"
image room_02_child_bed_kid_exp_eyebrows angryx01 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyebrows_angryx01.webp")
image room_02_child_bed_kid_exp_eyebrows angryx02 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyebrows_angryx02.webp")
image room_02_child_bed_kid_exp_eyebrows angryx03 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyebrows_angryx03.webp")
image room_02_child_bed_kid_exp_eyebrows sadx01 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyebrows_sadx01.webp")
image room_02_child_bed_kid_exp_eyebrows sadx02 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyebrows_sadx02.webp")
image room_02_child_bed_kid_exp_eyebrows sadx03 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyebrows_sadx03.webp")
image room_02_child_bed_kid_exp_eyebrows sadx04 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyebrows_sadx04.webp")
image room_02_child_bed_kid_exp_eyebrows sadx05 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyebrows_sadx05.webp")
image room_02_child_bed_kid_exp_eyebrows sadx06 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyebrows_sadx06.webp")
image room_02_child_bed_kid_exp_eyebrows serious = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyebrows_serious.webp")
image room_02_child_bed_kid_exp_eyebrows normal = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyebrows_normal.webp")
image room_02_child_bed_kid_exp_eyebrows surprisex01 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyebrows_surprisex01.webp")
image room_02_child_bed_kid_exp_eyebrows surprisex02 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyebrows_surprisex02.webp")

image room_02_child_bed_kid_exp_eyes empty = "images/general/empty.webp"
image room_02_child_bed_kid_exp_eyes 01 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyes_01.webp")
image room_02_child_bed_kid_exp_eyes 02 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyes_02.webp")
image room_02_child_bed_kid_exp_eyes 03 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyes_03.webp")
image room_02_child_bed_kid_exp_eyes 04 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyes_04.webp")
image room_02_child_bed_kid_exp_eyes 05 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyes_05.webp")
image room_02_child_bed_kid_exp_eyes 06 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyes_06.webp")
image room_02_child_bed_kid_exp_eyes 07 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_eyes_07.webp")

image room_02_child_bed_kid_exp_tears empty = "images/general/empty.webp"
image room_02_child_bed_kid_exp_tears 01 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_tears_05.webp")
image room_02_child_bed_kid_exp_tears 02 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_tears_05.webp")
image room_02_child_bed_kid_exp_tears 03 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_tears_05.webp")
image room_02_child_bed_kid_exp_tears 04 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_tears_05.webp")
image room_02_child_bed_kid_exp_tears 05 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_tears_05.webp")
image room_02_child_bed_kid_exp_tears 06 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_tears_06.webp")
image room_02_child_bed_kid_exp_tears 07 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_tears_07.webp")

image room_02_child_bed_kid_exp_mouth empty = "images/general/empty.webp"
image room_02_child_bed_kid_exp_mouth sad_Silentx01 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_mouth_sad_Silentx01.webp")
image room_02_child_bed_kid_exp_mouth sad_Silentx02 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_mouth_sad_Silentx02.webp")
image room_02_child_bed_kid_exp_mouth sad_Silentx03 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_mouth_sad_Silentx03.webp")
image room_02_child_bed_kid_exp_mouth sad_Silentx04 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_mouth_sad_Silentx04.webp")

image room_02_child_bed_kid_exp_mouth sad_Talkingx01 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_mouth_sad_Talkingx01.webp")
image room_02_child_bed_kid_exp_mouth sad_Talkingx02 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_mouth_sad_Talkingx02.webp")
image room_02_child_bed_kid_exp_mouth sad_Talkingx03 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_mouth_sad_Talkingx03.webp")
image room_02_child_bed_kid_exp_mouth sad_Talkingx04 = SaturateTint("images/day05/night/hotel/room_02_child/room_02_child_bed_kid_exp_mouth_sad_Talkingx04.webp")


image room_02_child_bed_kid_covered:

    contains:
        "bg_dark_a_blurry_01"
        truecenter

    contains:
        "room_02_child_bed_bg"
        truecenter
        zoom 0.5

    contains:
        "room_02_child_bed_sheet 01"
        truecenter
        zoom 0.5
        parallel:
            ease_quad 1.0 rotate .005
            ease_quad .7 rotate -.007
            repeat
        parallel:
            easein_quad .9 yzoom 1.001
            easein_quad .6 yzoom 0.995
            repeat
        parallel:
            easein_quad 1.0 xzoom 0.995
            easein_quad .5 xzoom 1.005
            repeat

##############################


##############################

    # Church Close (BRIDE)

image room_03_church_close_bg = "images/day05/night/hotel/room_03_church/room_03_church_close_bg.webp"
image room_03_church_close_bg_PROVE = "images/day05/night/hotel/room_03_church/room_03_church_close_bg_PROVE.webp"

image room_03_church_close_bride_exp_eyebrows angryx01 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyebrows_angryx01.webp"
image room_03_church_close_bride_exp_eyebrows angryx02 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyebrows_angryx02.webp"
image room_03_church_close_bride_exp_eyebrows angryx03 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyebrows_angryx03.webp"
image room_03_church_close_bride_exp_eyebrows sadx01 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyebrows_sadx01.webp"
image room_03_church_close_bride_exp_eyebrows sadx02 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyebrows_sadx02.webp"
image room_03_church_close_bride_exp_eyebrows sadx03 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyebrows_sadx03.webp"
image room_03_church_close_bride_exp_eyebrows sadx04 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyebrows_sadx04.webp"
image room_03_church_close_bride_exp_eyebrows sadx05 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyebrows_sadx05.webp"
image room_03_church_close_bride_exp_eyebrows serious = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyebrows_serious.webp"
image room_03_church_close_bride_exp_eyebrows normal = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyebrows_normal.webp"
image room_03_church_close_bride_exp_eyebrows surprisex01 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyebrows_surprisex01.webp"
image room_03_church_close_bride_exp_eyebrows surprisex02 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyebrows_surprisex02.webp"

image room_03_church_close_bride_exp_eyes 02 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyes_02.webp"
image room_03_church_close_bride_exp_eyes 03 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyes_03.webp"
image room_03_church_close_bride_exp_eyes 04 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyes_04.webp"
image room_03_church_close_bride_exp_eyes 05 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyes_05.webp"
image room_03_church_close_bride_exp_eyes 06 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyes_06.webp"
image room_03_church_close_bride_exp_eyes 07 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_eyes_07.webp"

image room_03_church_close_bride_exp_tears 02 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_tears_05.webp"
image room_03_church_close_bride_exp_tears 03 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_tears_05.webp"
image room_03_church_close_bride_exp_tears 04 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_tears_05.webp"
image room_03_church_close_bride_exp_tears 05 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_tears_05.webp"
image room_03_church_close_bride_exp_tears 06 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_tears_06.webp"
image room_03_church_close_bride_exp_tears 07 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_tears_07.webp"

image room_03_church_close_bride_exp_mouth sad_Silentx01 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sad_Silentx01.webp"
image room_03_church_close_bride_exp_mouth sad_Silentx02 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sad_Silentx02.webp"
image room_03_church_close_bride_exp_mouth sad_Silentx03 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sad_Silentx03.webp"
image room_03_church_close_bride_exp_mouth sad_Silentx04 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sad_Silentx04.webp"
image room_03_church_close_bride_exp_mouth sad_Silentx05 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sad_Silentx05.webp"
image room_03_church_close_bride_exp_mouth sad_Silentx06 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sad_Silentx06.webp"

image room_03_church_close_bride_exp_mouth sadbiting_Silentx01 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sadbiting_Silentx01.webp"
image room_03_church_close_bride_exp_mouth sadbiting_Silentx02 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sadbiting_Silentx02.webp"
image room_03_church_close_bride_exp_mouth sadbiting_Silentx03 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sadbiting_Silentx03.webp"
image room_03_church_close_bride_exp_mouth sadbiting_Silentx04 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sadbiting_Silentx04.webp"
image room_03_church_close_bride_exp_mouth sadbiting_Silentx05 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sadbiting_Silentx05.webp"
image room_03_church_close_bride_exp_mouth sadbiting_Silentx06 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sadbiting_Silentx06.webp"
image room_03_church_close_bride_exp_mouth sadbiting_Silentx07 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sadbiting_Silentx07.webp"
image room_03_church_close_bride_exp_mouth sadbiting_Silentx08 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sadbiting_Silentx08.webp"

image room_03_church_close_bride_exp_mouth sad_Talkingx01 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sad_Talkingx01.webp"
image room_03_church_close_bride_exp_mouth sad_Talkingx02 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sad_Talkingx02.webp"
image room_03_church_close_bride_exp_mouth sad_Talkingx03 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sad_Talkingx03.webp"
image room_03_church_close_bride_exp_mouth sad_Talkingx04 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sad_Talkingx04.webp"
image room_03_church_close_bride_exp_mouth sad_Talkingx05 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sad_Talkingx05.webp"
image room_03_church_close_bride_exp_mouth sad_Talkingx06 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sad_Talkingx06.webp"

image room_03_church_close_bride_exp_mouth sad_Talkingx003 = "images/day05/night/hotel/room_03_church/room_03_church_close_bride_exp_mouth_sad_Talkingx003.webp"


image room_03_church_close_hair_front = "images/day05/night/hotel/room_03_church/room_03_church_close_hair_front.webp"

image room_03_church_close_head camera = "images/day05/night/hotel/room_03_church/room_03_church_close_head_camera.webp"
image room_03_church_close_head down = "images/day05/night/hotel/room_03_church/room_03_church_close_head_down.webp"

transform room_03_church_close_exp_pos:
    subpixel True
    truecenter
    zoom 0.5
    xpos 0.5 ypos 0.463

transform room_03_church_close_rest_pos:
    subpixel True
    truecenter
    zoom 0.5

image room_03_church_close_headdown_comp:

    contains:
        "room_03_church_close_bg"
        room_03_church_close_rest_pos

    contains:
        "room_03_church_close_head down"
        room_03_church_close_rest_pos