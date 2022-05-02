
image bg el_plazaCam = "images/day05/elysium/inside/bg_el_plazaCam.webp"
image bg el_plazaMet = "images/day05/elysium/inside/bg_el_plazaMet.webp"
image bg el_plazaWall = "images/day05/elysium/inside/bg_el_plazaWall.webp"

image bg el_cath_cave = "images/day05/elysium/inside/bg_el_cath_cave.webp"
image bg el_cath_hall = "images/day05/elysium/inside/bg_el_cath_hall.webp"
image bg el_cath_main = "images/day05/elysium/inside/bg_el_cath_main.webp"
image bg el_cath_bar = "images/day05/elysium/inside/bg_el_cath_bar.webp"

image el_tab_cth = "images/day05/elysium/inside/el_tab_cth.webp"
image el_tab_nos = "images/day05/elysium/inside/el_tab_nos.webp"
image el_tab_tsi = "images/day05/elysium/inside/el_tab_tsi.webp"
image el_tab_war = "images/day05/elysium/inside/el_tab_war.webp"

image bg_el_cath_doorFront = "images/day05/elysium/inside/bg_el_cath_doorFront.webp"
image bg_el_cath_doorSide = "images/day05/elysium/inside/bg_el_cath_doorSide.webp"

image bg el_bedroom_a = "images/day05/elysium/inside/bg_el_bedroom_a.webp"
image bg el_bedroom_b = "images/day05/elysium/inside/bg_el_bedroom_b.webp"

image bg el_bedroom_blur = "images/day05/elysium/inside/bg_el_bedroom_blur.webp"


## GUARD

image guard_body = SaturateTint("images/general/characters/elysium/guard_body.webp")
image guard_exp_mouth sad_Silentx03 = SaturateTint("images/general/characters/elysium/guard_exp_mouth_sad_Silentx03.webp")
image guard_exp_mouth sad_Silentx04 = SaturateTint("images/general/characters/elysium/guard_exp_mouth_sad_Silentx04.webp")

image guard_alone:

    contains:
        "bg_el_cath_doorFront"
        truecenter
        zoom 0.55 xpos 0.1 ypos 0.35

    contains:
        "guard_body"
        transform_anchor True
        xalign 0.5 yalign 0.111 # Guard Eyes.
        zoom 0.4 xpos 0.5 ypos -0.02

    contains:
        "guard_exp_mouth sad_Silentx03"
        truecenter
        zoom 0.4 xpos 0.5 ypos -0.02


### BUTLER

image butler_body = SaturateTint("images/general/characters/elysium/butler_body.webp")

    # exp Eybrows:
image butler_exp_eyebrows angryx01 = SaturateTint("images/general/characters/elysium/butler_exp_eyebrows_angryx01.webp")
image butler_exp_eyebrows angryx02 = SaturateTint("images/general/characters/elysium/butler_exp_eyebrows_angryx02.webp")
image butler_exp_eyebrows angryx03 = SaturateTint("images/general/characters/elysium/butler_exp_eyebrows_angryx03.webp")
image butler_exp_eyebrows normal = SaturateTint("images/general/characters/elysium/butler_exp_eyebrows_normal.webp")
image butler_exp_eyebrows serious = SaturateTint("images/general/characters/elysium/butler_exp_eyebrows_serious.webp")
image butler_exp_eyebrows surprise = SaturateTint("images/general/characters/elysium/butler_exp_eyebrows_surprise.webp")
image butler_exp_eyebrows suspiciousx01 = SaturateTint("images/general/characters/elysium/butler_exp_eyebrows_suspiciousx01.webp")
image butler_exp_eyebrows suspiciousx02 = SaturateTint("images/general/characters/elysium/butler_exp_eyebrows_suspiciousx02.webp")

    # exp eyes
image butler_exp_eyes 01 = SaturateTint("images/general/characters/elysium/butler_exp_eyes_01.webp")
image butler_exp_eyes 03 = SaturateTint("images/general/characters/elysium/butler_exp_eyes_03.webp")
image butler_exp_eyes 04 = SaturateTint("images/general/characters/elysium/butler_exp_eyes_04.webp")
image butler_exp_eyes 05 = SaturateTint("images/general/characters/elysium/butler_exp_eyes_05.webp")
image butler_exp_eyes 08 = SaturateTint("images/general/characters/elysium/butler_exp_eyes_08.webp")


image butler_exp_piris empty = Null(width=800, height=600)
image butler_exp_piris front01 = SaturateTint("images/general/characters/elysium/butler_exp_piris_front01.webp")
image butler_exp_piris front03 = SaturateTint("images/general/characters/elysium/butler_exp_piris_front03.webp")
image butler_exp_piris front04 = SaturateTint("images/general/characters/elysium/butler_exp_piris_front04.webp")
image butler_exp_piris front05 = SaturateTint("images/general/characters/elysium/butler_exp_piris_front05.webp")
image butler_exp_piris front08 = Null(width=800, height=600)

    # exp mouth
image butler_exp_mouth sad_Silentx01 = SaturateTint("images/general/characters/elysium/butler_exp_mouth_sad_Silentx01.webp")
image butler_exp_mouth sad_Silentx02 = SaturateTint("images/general/characters/elysium/butler_exp_mouth_sad_Silentx02.webp")
image butler_exp_mouth sad_Silentx03 = SaturateTint("images/general/characters/elysium/butler_exp_mouth_sad_Silentx03.webp")
image butler_exp_mouth sad_Silentx04 = SaturateTint("images/general/characters/elysium/butler_exp_mouth_sad_Silentx04.webp")
image butler_exp_mouth sad_Silentx05 = SaturateTint("images/general/characters/elysium/butler_exp_mouth_sad_Silentx05.webp")

image butler_exp_mouth sad_Talkingx01 = SaturateTint("images/general/characters/elysium/butler_exp_mouth_sad_Talkingx01.webp")
image butler_exp_mouth sad_Talkingx02 = SaturateTint("images/general/characters/elysium/butler_exp_mouth_sad_Talkingx02.webp")
image butler_exp_mouth sad_Talkingx03 = SaturateTint("images/general/characters/elysium/butler_exp_mouth_sad_Talkingx03.webp")
image butler_exp_mouth sad_Talkingx04 = SaturateTint("images/general/characters/elysium/butler_exp_mouth_sad_Talkingx04.webp")
image butler_exp_mouth sad_Talkingx05 = SaturateTint("images/general/characters/elysium/butler_exp_mouth_sad_Talkingx05.webp")
image butler_exp_mouth sad_Talkingx06 = SaturateTint("images/general/characters/elysium/butler_exp_mouth_sad_Talkingx06.webp")

transform butler_cent_pos:
    zoom 0.4 xpos 0.5 ypos 0.31 # Perfect ypose


image butler_alone:

    contains:
        "bg_el_cath_doorFront"
        truecenter
        zoom 0.55 xpos 0.78 ypos 0.35

    # contains:
    #     "day05"
    #     truecenter

    contains:
        "butler_body"
        transform_anchor True
        xalign 0.5 yalign 0.16 # Butler Eyes.
        butler_cent_pos

    contains:
        "butler_exp_eyes 04"
        truecenter
        butler_cent_pos

    contains:
        "butler_exp_piris front04"
        truecenter
        butler_cent_pos

    contains:
        "butler_exp_eyebrows suspiciousx01"
        truecenter
        butler_cent_pos

    contains:
        "butler_exp_mouth sad_Silentx03"
        truecenter
        butler_cent_pos


## RELDA ENERI

image relda_body = SaturateTint("images/general/characters/elysium/relda_body.webp")

## Relda Expressions
    ## Eyebrows
image relda_exp_eyebrows angryx01 = SaturateTint("images/general/characters/elysium/relda_exp_eyebrows_angryx01.webp")
image relda_exp_eyebrows angryx02 = SaturateTint("images/general/characters/elysium/relda_exp_eyebrows_angryx02.webp")
image relda_exp_eyebrows angryx03 = SaturateTint("images/general/characters/elysium/relda_exp_eyebrows_angryx03.webp")
image relda_exp_eyebrows angryx04 = SaturateTint("images/general/characters/elysium/relda_exp_eyebrows_angryx04.webp")
image relda_exp_eyebrows normal = SaturateTint("images/general/characters/elysium/relda_exp_eyebrows_normal.webp")
image relda_exp_eyebrows sadx01 = SaturateTint("images/general/characters/elysium/relda_exp_eyebrows_sadx01.webp")
image relda_exp_eyebrows sadx02 = SaturateTint("images/general/characters/elysium/relda_exp_eyebrows_sadx02.webp")
image relda_exp_eyebrows sadx03 = SaturateTint("images/general/characters/elysium/relda_exp_eyebrows_sadx03.webp")
image relda_exp_eyebrows serious = SaturateTint("images/general/characters/elysium/relda_exp_eyebrows_serious.webp")
image relda_exp_eyebrows surprisex01 = SaturateTint("images/general/characters/elysium/relda_exp_eyebrows_surprisex01.webp")
image relda_exp_eyebrows suspiciousx01 = SaturateTint("images/general/characters/elysium/relda_exp_eyebrows_suspiciousx01.webp")
image relda_exp_eyebrows suspiciousx02 = SaturateTint("images/general/characters/elysium/relda_exp_eyebrows_suspiciousx02.webp")
image relda_exp_eyebrows suspiciousx03 = SaturateTint("images/general/characters/elysium/relda_exp_eyebrows_suspiciousx03.webp")

    ## eyes

image relda_exp_eyes 01 = SaturateTint("images/general/characters/elysium/relda_exp_eyes_01.webp")
image relda_exp_eyes 03 = SaturateTint("images/general/characters/elysium/relda_exp_eyes_03.webp")
image relda_exp_eyes 04 = SaturateTint("images/general/characters/elysium/relda_exp_eyes_04.webp")
image relda_exp_eyes 05 = SaturateTint("images/general/characters/elysium/relda_exp_eyes_05.webp")
image relda_exp_eyes 06 = SaturateTint("images/general/characters/elysium/relda_exp_eyes_06.webp")
image relda_exp_eyes 07 = SaturateTint("images/general/characters/elysium/relda_exp_eyes_07.webp")
image relda_exp_eyes 08 = SaturateTint("images/general/characters/elysium/relda_exp_eyes_08.webp")

    ## piris


image relda_exp_piris empty = Null(width=800, height=600)

image relda_exp_piris front01 = SaturateTint("images/general/characters/elysium/relda_exp_piris_front01.webp")
image relda_exp_piris front03 = SaturateTint("images/general/characters/elysium/relda_exp_piris_front03.webp")
image relda_exp_piris front04 = SaturateTint("images/general/characters/elysium/relda_exp_piris_front04.webp")
image relda_exp_piris front05 = SaturateTint("images/general/characters/elysium/relda_exp_piris_front05.webp")
image relda_exp_piris front06 = Null(width=800, height=600)
image relda_exp_piris front07 = Null(width=800, height=600)
image relda_exp_piris front08 = Null(width=800, height=600)

image relda_exp_piris left01 = SaturateTint("images/general/characters/elysium/relda_exp_piris_left01.webp")
image relda_exp_piris left03 = SaturateTint("images/general/characters/elysium/relda_exp_piris_left03.webp")
image relda_exp_piris left04 = SaturateTint("images/general/characters/elysium/relda_exp_piris_left04.webp")
image relda_exp_piris left05 = SaturateTint("images/general/characters/elysium/relda_exp_piris_left05.webp")

image relda_exp_piris right01 = SaturateTint("images/general/characters/elysium/relda_exp_piris_right01.webp")
image relda_exp_piris right03 = SaturateTint("images/general/characters/elysium/relda_exp_piris_right03.webp")
image relda_exp_piris right04 = SaturateTint("images/general/characters/elysium/relda_exp_piris_right04.webp")
image relda_exp_piris right05 = SaturateTint("images/general/characters/elysium/relda_exp_piris_right05.webp")

    # mouth

image relda_exp_mouth happy_Silentx01 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_happy_Silentx01.webp")
image relda_exp_mouth happy_Silentx02 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_happy_Silentx02.webp")
image relda_exp_mouth happy_Silentx03 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_happy_Silentx03.webp")
image relda_exp_mouth happy_Silentx04 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_happy_Silentx04.webp")
image relda_exp_mouth happy_Silentx05 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_happy_Silentx05.webp")
image relda_exp_mouth happy_Silentx06 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_happy_Silentx06.webp")
image relda_exp_mouth happy_Silentx07 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_happy_Silentx07.webp")

image relda_exp_mouth happy_Talkingx01 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_happy_Talkingx01.webp")
image relda_exp_mouth happy_Talkingx02 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_happy_Talkingx02.webp")
image relda_exp_mouth happy_Talkingx03 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_happy_Talkingx03.webp")
image relda_exp_mouth happy_Talkingx04 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_happy_Talkingx04.webp")
image relda_exp_mouth happy_Talkingx05 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_happy_Talkingx05.webp")
image relda_exp_mouth happy_Talkingx06 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_happy_Talkingx06.webp")
image relda_exp_mouth happy_Talkingx07 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_happy_Talkingx07.webp")
image relda_exp_mouth happy_Talkingx08 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_happy_Talkingx08.webp")
image relda_exp_mouth happy_Talkingx09 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_happy_Talkingx09.webp")

image relda_exp_mouth sad_Silentx01 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Silentx01.webp")
image relda_exp_mouth sad_Silentx02 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Silentx02.webp")
image relda_exp_mouth sad_Silentx03 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Silentx03.webp")
image relda_exp_mouth sad_Silentx04 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Silentx04.webp")
image relda_exp_mouth sad_Silentx05 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Silentx05.webp")
image relda_exp_mouth sad_Silentx06 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Silentx06.webp")
image relda_exp_mouth sad_Silentx07 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Silentx07.webp")

image relda_exp_mouth sad_Talkingx01 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Talkingx01.webp")
image relda_exp_mouth sad_Talkingx02 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Talkingx02.webp")
image relda_exp_mouth sad_Talkingx03 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Talkingx03.webp")
image relda_exp_mouth sad_Talkingx04 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Talkingx04.webp")
image relda_exp_mouth sad_Talkingx05 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Talkingx05.webp")
image relda_exp_mouth sad_Talkingx06 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Talkingx06.webp")
image relda_exp_mouth sad_Talkingx07 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Talkingx07.webp")

image relda_exp_mouth sad_Talkingx001 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Talkingx001.webp")
image relda_exp_mouth sad_Talkingx002 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Talkingx002.webp")
image relda_exp_mouth sad_Talkingx003 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Talkingx003.webp")
image relda_exp_mouth sad_Talkingx004 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Talkingx004.webp")
image relda_exp_mouth sad_Talkingx005 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Talkingx005.webp")
image relda_exp_mouth sad_Talkingx006 = SaturateTint("images/general/characters/elysium/relda_exp_mouth_sad_Talkingx006.webp")


image relda_top_hair = SaturateTint("images/general/characters/elysium/relda_top_hair.webp")
image relda_top_hat = SaturateTint("images/general/characters/elysium/relda_top_hat.webp")

image relda_alone:

    contains:
        "bg_el_cath_doorFront"
        truecenter
        zoom 0.55 xpos 0.78 ypos 0.35

    contains:
        "relda_body"
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        zoom 0.4 xpos 0.5 ypos 0.252 # Perfect ypose

    contains:
        "relda_exp_eyes 03"
        truecenter
        zoom 0.4 xpos 0.5 ypos 0.252 # Perfect ypose

    contains:
        "relda_exp_piris front03"
        truecenter
        zoom 0.4 xpos 0.5 ypos 0.252 # Perfect ypose

    contains:
        "relda_exp_eyebrows sadx02"
        truecenter
        zoom 0.4 xpos 0.5 ypos 0.252 # Perfect ypose

    contains:
        "relda_exp_mouth happy_Silentx05"
        truecenter
        zoom 0.4 xpos 0.5 ypos 0.252 # Perfect ypose

    # contains:
    #     "relda_top_hair"
    #     truecenter
    #     zoom 0.4 xpos 0.5 ypos 0.252 # Perfect ypose

    contains:
        "relda_top_hat"
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        zoom 0.4 xpos 0.5 ypos 0.252 # Perfect ypose

image relda_alone_room:

    contains:
        "bg_el_bedroom_blur"
        truecenter
        rotate 90
        zoom 0.5 xpos 0.5 ypos 0.5

    contains:
        "relda_body"
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        zoom 0.4 xpos 0.5 ypos 0.252 # Perfect ypose

    contains:
        "relda_exp_eyes 04"
        truecenter
        zoom 0.4 xpos 0.5 ypos 0.252 # Perfect ypose

    contains:
        "relda_exp_piris front04"
        truecenter
        zoom 0.4 xpos 0.5 ypos 0.252 # Perfect ypose

    contains:
        "relda_exp_eyebrows serious"
        truecenter
        zoom 0.4 xpos 0.5 ypos 0.252 # Perfect ypose

    contains:
        "relda_exp_mouth happy_Silentx05"
        truecenter
        zoom 0.4 xpos 0.5 ypos 0.252 # Perfect ypose

    contains:
        "relda_top_hair"
        truecenter
        zoom 0.4 xpos 0.5 ypos 0.252 # Perfect ypose

    # contains:
    #     "relda_top_hat"
    #     transform_anchor True
    #     xalign 0.5 yalign 0.218 # Relda Eyes.
    #     zoom 0.4 xpos 0.5 ypos 0.252 # Perfect ypose


transform centerTest:
    zoom 2.5 xpos 0.5 ypos 0.5 # center

transform relda_pos_close:
    #zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
    zoom 1.0 xpos 0.5 ypos 0.252


################################################################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
################################################################################

transform neigh_pos_atLeft_body:
    transform_anchor True
    xalign 0.5 yalign 0.3019
    xzoom -1.0
    zoom 0.25 xpos 0.25 ypos 0.33

transform neigh_pos_atLeft_exp:
    truecenter
    xzoom -1.0
    zoom 0.25 xpos 0.25 ypos 0.33



image neigh_PROVE = "images/general/characters/others/neigh_PROVE.webp"

image neigh_body = SaturateTint("images/general/characters/others/neigh_body.webp")
image neigh_exp_eyebrows angryx01 = SaturateTint("images/general/characters/others/neigh_exp_eyebrows_angryx02.webp")
image neigh_exp_eyebrows angryx01 = SaturateTint("images/general/characters/others/neigh_exp_eyebrows_angryx02.webp")
image neigh_exp_eyebrows normal = SaturateTint("images/general/characters/others/neigh_exp_eyebrows_normal.webp")
image neigh_exp_eyebrows sadx01 = SaturateTint("images/general/characters/others/neigh_exp_eyebrows_sadx01.webp")
image neigh_exp_eyebrows sadx02 = SaturateTint("images/general/characters/others/neigh_exp_eyebrows_sadx02.webp")
image neigh_exp_eyebrows serious = SaturateTint("images/general/characters/others/neigh_exp_eyebrows_serious.webp")
image neigh_exp_eyebrows surprisex01 = SaturateTint("images/general/characters/others/neigh_exp_eyebrows_surprisex01.webp")
image neigh_exp_eyebrows surprisex02 = SaturateTint("images/general/characters/others/neigh_exp_eyebrows_surprisex02.webp")
image neigh_exp_eyebrows suspiciousx01 = SaturateTint("images/general/characters/others/neigh_exp_eyebrows_suspiciousx01.webp")
image neigh_exp_eyebrows suspiciousx02 = SaturateTint("images/general/characters/others/neigh_exp_eyebrows_suspiciousx02.webp")

image neigh_hairFront = SaturateTint("images/general/characters/others/neigh_hairFront.webp")

image neigh_exp_eyes 00 = SaturateTint("images/general/characters/others/neigh_exp_eyes_00.webp")
image neigh_exp_eyes 03 = SaturateTint("images/general/characters/others/neigh_exp_eyes_03.webp")

image neigh_exp_piris front00 = SaturateTint("images/general/characters/others/neigh_exp_piris_front00.webp")
image neigh_exp_piris front03 = SaturateTint("images/general/characters/others/neigh_exp_piris_front03.webp")

image neigh_exp_piris left00 = SaturateTint("images/general/characters/others/neigh_exp_piris_left00.webp")
image neigh_exp_piris left03 = SaturateTint("images/general/characters/others/neigh_exp_piris_left03.webp")

image neigh_exp_piris right00 = SaturateTint("images/general/characters/others/neigh_exp_piris_right00.webp")
image neigh_exp_piris right03 = SaturateTint("images/general/characters/others/neigh_exp_piris_right03.webp")


image neigh_exp_mouth sad_Silentx01 = SaturateTint("images/general/characters/others/neigh_exp_mouth_sad_Silentx01.webp")
image neigh_exp_mouth sad_Silentx02 = SaturateTint("images/general/characters/others/neigh_exp_mouth_sad_Silentx02.webp")
image neigh_exp_mouth sad_Silentx03 = SaturateTint("images/general/characters/others/neigh_exp_mouth_sad_Silentx03.webp")
image neigh_exp_mouth sad_Silentx04 = SaturateTint("images/general/characters/others/neigh_exp_mouth_sad_Silentx04.webp")

image neigh_exp_mouth sad_Talkingx01 = SaturateTint("images/general/characters/others/neigh_exp_mouth_sad_Talkingx01.webp")
image neigh_exp_mouth sad_Talkingx02 = SaturateTint("images/general/characters/others/neigh_exp_mouth_sad_Talkingx02.webp")
image neigh_exp_mouth sad_Talkingx03 = SaturateTint("images/general/characters/others/neigh_exp_mouth_sad_Talkingx03.webp")
image neigh_exp_mouth sad_Talkingx04 = SaturateTint("images/general/characters/others/neigh_exp_mouth_sad_Talkingx04.webp")
image neigh_exp_mouth sad_Talkingx05 = SaturateTint("images/general/characters/others/neigh_exp_mouth_sad_Talkingx05.webp")


################################################################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
################################################################################

image bg_homeElevator = SaturateTint("images/day05/bg_homeElevator.webp")

################################################################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
################################################################################

image fireTorch 01 = "images/effects/fire/fireTorch_01.webp"
image fireTorch 02 = "images/effects/fire/fireTorch_02.webp"
image fireTorch 03 = "images/effects/fire/fireTorch_03.webp"
image fireTorch 04 = "images/effects/fire/fireTorch_04.webp"
image fireTorch 05 = "images/effects/fire/fireTorch_05.webp"
image fireTorch 06 = "images/effects/fire/fireTorch_06.webp"
image fireTorch 07 = "images/effects/fire/fireTorch_07.webp"

image fireTorchB 01 = "images/effects/fire/fireTorchB_01.webp"
image fireTorchB 02 = "images/effects/fire/fireTorchB_02.webp"
image fireTorchB 03 = "images/effects/fire/fireTorchB_03.webp"
image fireTorchB 04 = "images/effects/fire/fireTorchB_04.webp"
image fireTorchB 05 = "images/effects/fire/fireTorchB_05.webp"
image fireTorchB 06 = "images/effects/fire/fireTorchB_06.webp"
image fireTorchB 07 = "images/effects/fire/fireTorchB_07.webp"



image fireTorchB_anim_01:
    "fireTorchB 01"
    block:
        pause 0.15
        "fireTorchB 02" with Dissolve(0.15)
        pause 0.15
        "fireTorchB 03" with Dissolve(0.15)
        pause 0.15
        "fireTorchB 04" with Dissolve(0.15)
        pause 0.15
        "fireTorchB 05" with Dissolve(0.15)
        pause 0.15
        "fireTorchB 06" with Dissolve(0.15)
        pause 0.15
        "fireTorchB 07" with Dissolve(0.15)
        pause 0.15
        "fireTorchB 01" with Dissolve(0.15)
        repeat

image fireTorchB_anim_02:
    "fireTorchB 01"
    block:
        pause 0.17
        "fireTorchB 02" with Dissolve(0.15)
        pause 0.12
        "fireTorchB 03" with Dissolve(0.15)
        pause 0.13
        "fireTorchB 04" with Dissolve(0.15)
        pause 0.18
        "fireTorchB 05" with Dissolve(0.15)
        pause 0.12
        "fireTorchB 06" with Dissolve(0.15)
        pause 0.19
        "fireTorchB 07" with Dissolve(0.15)
        pause 0.12
        "fireTorchB 01" with Dissolve(0.15)
        repeat

image fireTorchB_anim_03:
    "fireTorchB 03"
    block:
        pause 0.12
        "fireTorchB 04" with Dissolve(0.15)
        pause 0.18
        "fireTorchB 05" with Dissolve(0.15)
        pause 0.11
        "fireTorchB 06" with Dissolve(0.15)
        pause 0.10
        "fireTorchB 07" with Dissolve(0.15)
        pause 0.18
        "fireTorchB 01" with Dissolve(0.15)
        pause 0.17
        "fireTorchB 02" with Dissolve(0.15)
        pause 0.12
        "fireTorchB 03" with Dissolve(0.15)
        repeat

image fireTorchB_anim_04:
    "fireTorchB 05"
    block:
        pause 0.16
        "fireTorchB 06" with Dissolve(0.15)
        pause 0.12
        "fireTorchB 07" with Dissolve(0.15)
        pause 0.10
        "fireTorchB 01" with Dissolve(0.15)
        pause 0.18
        "fireTorchB 02" with Dissolve(0.15)
        pause 0.12
        "fireTorchB 03" with Dissolve(0.15)
        pause 0.15
        "fireTorchB 04" with Dissolve(0.15)
        pause 0.15
        "fireTorchB 05" with Dissolve(0.15)
        repeat


################################################################################
################################################################################
################################################################################

image bg_el_cath_dunHall_01 = "images/day05/elysium/inside/bg_el_cath_dunHall_01.webp"
image bg_el_cath_dunHall_02 = "images/day05/elysium/inside/bg_el_cath_dunHall_02.webp"
image bg_el_cath_dunHall_03 = "images/day05/elysium/inside/bg_el_cath_dunHall_03.webp"
image bg_el_cath_dunHall_04 = "images/day05/elysium/inside/bg_el_cath_dunHall_03.webp"

image bg_el_cath_dunHall_01_b = "images/day05/elysium/inside/bg_el_cath_dunHall_01_b.webp"
image bg_el_cath_dunHall_02_b = "images/day05/elysium/inside/bg_el_cath_dunHall_02_b.webp"
image bg_el_cath_dunHall_03_b = "images/day05/elysium/inside/bg_el_cath_dunHall_03_b.webp"
image bg_el_cath_dunHall_04_b = "images/day05/elysium/inside/bg_el_cath_dunHall_04_b.webp"

image bg_el_cath_dunHall_01_comp:
    contains:
        "bg_el_cath_dunHall_01"
        truecenter
        zoom 2.0
    contains:
        "bg_el_cath_dunHall_01_b"
        truecenter
        zoom 2.0
        additive 1.0
        alpha 0.0
        block:
            ease 0.55 alpha 0.2
            ease 0.52 alpha 0.0
            ease 0.53 alpha 0.3
            ease 0.54 alpha 0.0
            ease 0.52 alpha 0.15
            repeat
    contains:
        "bg_el_cath_dunHall_TorchesB_comp"
        truecenter

image bg_el_cath_dunHall_02_comp:
    contains:
        "bg_el_cath_dunHall_02"
        truecenter
        zoom 2.0
    contains:
        "bg_el_cath_dunHall_02_b"
        truecenter
        zoom 2.0
        additive 1.0
        alpha 0.0
        block:
            ease 0.55 alpha 0.2
            ease 0.52 alpha 0.0
            ease 0.53 alpha 0.3
            ease 0.54 alpha 0.0
            ease 0.52 alpha 0.15
            repeat
    contains:
        "bg_el_cath_dunHall_TorchesB_comp"
        truecenter

image bg_el_cath_dunHall_03_comp:
    contains:
        "bg_el_cath_dunHall_03"
        truecenter
        zoom 2.0
    contains:
        "bg_el_cath_dunHall_03_b"
        truecenter
        zoom 2.0
        additive 1.0
        alpha 0.0
        block:
            ease 0.55 alpha 0.2
            ease 0.52 alpha 0.0
            ease 0.53 alpha 0.3
            ease 0.54 alpha 0.0
            ease 0.52 alpha 0.15
            repeat
    contains:
        "bg_el_cath_dunHall_TorchesB_comp"
        truecenter

image bg_el_cath_dunHall_04_comp:
    contains:
        "bg_el_cath_dunHall_04"
        truecenter
        zoom 2.0
    contains:
        "bg_el_cath_dunHall_04_b"
        truecenter
        zoom 2.0
        additive 1.0
        alpha 0.0
        block:
            ease 0.55 alpha 0.2
            ease 0.52 alpha 0.0
            ease 0.53 alpha 0.3
            ease 0.54 alpha 0.0
            ease 0.52 alpha 0.15
            repeat
    contains:
        "bg_el_cath_dunHall_TorchesB_comp"
        truecenter
    
image bg_el_cath_dunHall_TorchesB_comp:

    contains: ## Right 05
        "fireTorchB_anim_01"
        transform_anchor True
        xalign 0.5 yalign 0.9
        additive 1.0
        zoom 0.07 xpos 0.65 ypos 0.5

    contains: ## Left 05
        "fireTorchB_anim_02"
        transform_anchor True
        xalign 0.5 yalign 0.9
        additive 1.0
        zoom 0.07 xpos 0.355 ypos 0.5
###
    contains: ## Right 04
        "fireTorchB_anim_02"
        transform_anchor True
        xalign 0.5 yalign 0.9
        additive 1.0
        zoom 0.1 xpos 0.71 ypos 0.465

    contains: ## Left 04
        "fireTorchB_anim_03"
        transform_anchor True
        xalign 0.5 yalign 0.9
        additive 1.0
        zoom 0.1 xpos 0.26 ypos 0.465
###
    contains: ## Right 03
        "fireTorchB_anim_03"
        transform_anchor True
        xalign 0.5 yalign 0.9
        additive 1.0
        zoom 0.2 xpos 0.88 ypos 0.4

    contains: ## Left 03
        "fireTorchB_anim_04"
        transform_anchor True
        xalign 0.5 yalign 0.9
        additive 1.0
        zoom 0.2 xpos 0.1 ypos 0.4
###
    contains: ## Right 02
        "fireTorchB_anim_01"
        transform_anchor True
        xalign 0.5 yalign 0.9
        additive 1.0
        zoom 0.4 xpos 1.27 ypos 0.23

    contains: ## Left 02
        "fireTorchB_anim_02"
        transform_anchor True
        xalign 0.5 yalign 0.9
        additive 1.0
        zoom 0.4 xpos -0.25 ypos 0.23
###
    contains: ## Right 01
        "fireTorchB_anim_03"
        transform_anchor True
        xalign 0.5 yalign 0.9
        additive 1.0
        zoom 1.0 xpos 2.4 ypos -0.2

    contains: ## Left 01
        "fireTorchB_anim_04"
        transform_anchor True
        xalign 0.5 yalign 0.9
        additive 1.0
        zoom 1.0 xpos -1.4 ypos -0.2


################################################################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
################################################################################

## wwW = WereWolf White

image wwW_body_TEST = "images/general/characters/werewolves/wwW_body_TEST.webp"

image wwW__whole_darkness = SaturateTint("images/general/characters/werewolves/wwW__whole_darkness.webp")

image wwW_body = SaturateTint("images/general/characters/werewolves/wwW_body.webp")

image wwW_exp_eyes 00 = SaturateTint("images/general/characters/werewolves/wwW_exp_eyes_00.webp")
image wwW_exp_eyes 03 = SaturateTint("images/general/characters/werewolves/wwW_exp_eyes_03.webp")
image wwW_exp_mouth happy_Silentx01 = SaturateTint("images/general/characters/werewolves/wwW_exp_mouth_happy_Silentx01.webp")
image wwW_exp_mouth sad_Silentx01 = SaturateTint("images/general/characters/werewolves/wwW_exp_mouth_sad_Silentx01.webp")
image wwW_exp_mouth happy_Talkingx01 = SaturateTint("images/general/characters/werewolves/wwW_exp_mouth_happy_Talkingx01.webp")
image wwW_exp_mouth sad_Talkingx01 = SaturateTint("images/general/characters/werewolves/wwW_exp_mouth_happy_Talkingx01.webp")


transform wwW_pos_body_center:
    transform_anchor True
    xalign 0.5 yalign 0.1364 #-13Down +14Up
    zoom 0.5 xpos 0.5 ypos -0.1 # Pose?

transform wwW_pos_exp_center:
    transform_anchor True
    xalign 0.5 yalign 0.5 #-13Down +14Up
    zoom 0.5 xpos 0.5 ypos -0.1 # Pose?

image wwW__whole_darkness_comp:

    contains:
        "bg_dark_a_blurry_02"
        truecenter
        rotate 90
        zoom 2.5
        ypos 1.3

    contains:
        "wwW__whole_darkness"
        transform_anchor True
        xalign 0.5 yalign 0.1364 #-13Down +14Up
        zoom 0.5 xpos 0.5 ypos 0.5


################################################################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
################################################################################

image bGuys_TEST = "images/day05/aftermorning/dudes/bGuys_TEST.webp"

image bGuy_a_TEST = "images/day05/aftermorning/dudes/bGuy_a_TEST.webp"
image bGuy_b_TEST = "images/day05/aftermorning/dudes/bGuy_b_TEST.webp"

transform bGuy_a_align:
    transform_anchor True
    xalign 0.5 yalign 0.2285 # a_GuyAlign # 0.0-Down 1.0-Up

transform bGuy_b_align:
    transform_anchor True
    xalign 0.5 yalign 0.2682 # b_GuyAlign

image bGuy_a_body = "images/day05/aftermorning/dudes/bGuy_a_body.webp"

image bGuy_a_exp_eyebrows angryx01 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyebrows_angryx01.webp"
image bGuy_a_exp_eyebrows angryx02 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyebrows_angryx02.webp"
image bGuy_a_exp_eyebrows angryx03 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyebrows_angryx03.webp"
image bGuy_a_exp_eyebrows angryx04 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyebrows_angryx04.webp"
image bGuy_a_exp_eyebrows normal = "images/day05/aftermorning/dudes/bGuy_a_exp_eyebrows_normal.webp"
image bGuy_a_exp_eyebrows serious = "images/day05/aftermorning/dudes/bGuy_a_exp_eyebrows_serious.webp"
image bGuy_a_exp_eyebrows surprisex01 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyebrows_surprisex01.webp"
image bGuy_a_exp_eyebrows surprisex02 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyebrows_surprisex02.webp"
image bGuy_a_exp_eyebrows suspiciousx01 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyebrows_suspiciousx01.webp"
image bGuy_a_exp_eyebrows suspiciousx02 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyebrows_suspiciousx02.webp"
image bGuy_a_exp_eyebrows suspiciousx03 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyebrows_suspiciousx03.webp"
image bGuy_a_exp_eyebrows sadx01 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyebrows_sadx01.webp"
image bGuy_a_exp_eyebrows sadx02 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyebrows_sadx02.webp"
image bGuy_a_exp_eyebrows sadx03 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyebrows_sadx03.webp"
image bGuy_a_exp_eyebrows sadx04 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyebrows_sadx04.webp"

image bGuy_a_exp_eyes 00 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyes_00.webp"
image bGuy_a_exp_eyes 02 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyes_02.webp"
image bGuy_a_exp_eyes 03 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyes_03.webp"
image bGuy_a_exp_eyes 04 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyes_04.webp"
image bGuy_a_exp_eyes 05 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyes_05.webp"
image bGuy_a_exp_eyes 06 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyes_06.webp"
image bGuy_a_exp_eyes 07 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyes_07.webp"
image bGuy_a_exp_eyes 08 = "images/day05/aftermorning/dudes/bGuy_a_exp_eyes_08.webp"

image bGuy_a_exp_piris front00 = "images/day05/aftermorning/dudes/bGuy_a_exp_piris_front00.webp"
image bGuy_a_exp_piris front02 = "images/day05/aftermorning/dudes/bGuy_a_exp_piris_front02.webp"
image bGuy_a_exp_piris front03 = "images/day05/aftermorning/dudes/bGuy_a_exp_piris_front03.webp"
image bGuy_a_exp_piris front04 = "images/day05/aftermorning/dudes/bGuy_a_exp_piris_front04.webp"
image bGuy_a_exp_piris front05 = "images/day05/aftermorning/dudes/bGuy_a_exp_piris_front05.webp"
image bGuy_a_exp_piris front06 = Null(width=800, height=600)
image bGuy_a_exp_piris front07 = Null(width=800, height=600)
image bGuy_a_exp_piris front08 = Null(width=800, height=600)

image bGuy_a_exp_piris right00 = "images/day05/aftermorning/dudes/bGuy_a_exp_piris_right00.webp"
image bGuy_a_exp_piris right02 = "images/day05/aftermorning/dudes/bGuy_a_exp_piris_right02.webp"
image bGuy_a_exp_piris right03 = "images/day05/aftermorning/dudes/bGuy_a_exp_piris_right03.webp"
image bGuy_a_exp_piris right04 = "images/day05/aftermorning/dudes/bGuy_a_exp_piris_right04.webp"
image bGuy_a_exp_piris right05 = "images/day05/aftermorning/dudes/bGuy_a_exp_piris_right05.webp"

image bGuy_a_exp_piris left00 = "images/day05/aftermorning/dudes/bGuy_a_exp_piris_left00.webp"
image bGuy_a_exp_piris left02 = "images/day05/aftermorning/dudes/bGuy_a_exp_piris_left02.webp"
image bGuy_a_exp_piris left03 = "images/day05/aftermorning/dudes/bGuy_a_exp_piris_left03.webp"
image bGuy_a_exp_piris left04 = "images/day05/aftermorning/dudes/bGuy_a_exp_piris_left04.webp"
image bGuy_a_exp_piris left05 = "images/day05/aftermorning/dudes/bGuy_a_exp_piris_left05.webp"

image bGuy_a_exp_mouth happy_Silentx01 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_happy_Silentx01.webp"
image bGuy_a_exp_mouth happy_Silentx02 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_happy_Silentx02.webp"
image bGuy_a_exp_mouth happy_Silentx03 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_happy_Silentx03.webp"
image bGuy_a_exp_mouth happy_Silentx04 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_happy_Silentx04.webp"
image bGuy_a_exp_mouth happy_Silentx05 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_happy_Silentx05.webp"
image bGuy_a_exp_mouth happy_Silentx06 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_happy_Silentx06.webp"

image bGuy_a_exp_mouth happy_Talkingx01 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_happy_Talkingx01.webp"
image bGuy_a_exp_mouth happy_Talkingx02 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_happy_Talkingx02.webp"
image bGuy_a_exp_mouth happy_Talkingx03 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_happy_Talkingx03.webp"
image bGuy_a_exp_mouth happy_Talkingx04 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_happy_Talkingx04.webp"
image bGuy_a_exp_mouth happy_Talkingx05 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_happy_Talkingx05.webp"
image bGuy_a_exp_mouth happy_Talkingx06 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_happy_Talkingx06.webp"

image bGuy_a_exp_mouth sad_Silentx01 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_sad_Silentx01.webp"
image bGuy_a_exp_mouth sad_Silentx02 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_sad_Silentx02.webp"
image bGuy_a_exp_mouth sad_Silentx03 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_sad_Silentx03.webp"
image bGuy_a_exp_mouth sad_Silentx04 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_sad_Silentx04.webp"
image bGuy_a_exp_mouth sad_Silentx05 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_sad_Silentx05.webp"
image bGuy_a_exp_mouth sad_Silentx06 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_sad_Silentx06.webp"

image bGuy_a_exp_mouth sad_Talkingx01 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_sad_Talkingx01.webp"
image bGuy_a_exp_mouth sad_Talkingx02 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_sad_Talkingx02.webp"
image bGuy_a_exp_mouth sad_Talkingx03 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_sad_Talkingx03.webp"
image bGuy_a_exp_mouth sad_Talkingx04 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_sad_Talkingx04.webp"
image bGuy_a_exp_mouth sad_Talkingx05 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_sad_Talkingx05.webp"
image bGuy_a_exp_mouth sad_Talkingx06 = "images/day05/aftermorning/dudes/bGuy_a_exp_mouth_sad_Talkingx06.webp"

###

image bGuy_b_body = "images/day05/aftermorning/dudes/bGuy_b_body.webp"

image bGuy_b_exp_eyebrows angryx01 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyebrows_angryx01.webp"
image bGuy_b_exp_eyebrows angryx02 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyebrows_angryx02.webp"
image bGuy_b_exp_eyebrows angryx03 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyebrows_angryx03.webp"
image bGuy_b_exp_eyebrows angryx04 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyebrows_angryx04.webp"
image bGuy_b_exp_eyebrows normal = "images/day05/aftermorning/dudes/bGuy_b_exp_eyebrows_normal.webp"
image bGuy_b_exp_eyebrows serious = "images/day05/aftermorning/dudes/bGuy_b_exp_eyebrows_serious.webp"
image bGuy_b_exp_eyebrows surprisex01 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyebrows_surprisex01.webp"
image bGuy_b_exp_eyebrows surprisex02 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyebrows_surprisex02.webp"
image bGuy_b_exp_eyebrows suspiciousx01 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyebrows_suspiciousx01.webp"
image bGuy_b_exp_eyebrows suspiciousx02 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyebrows_suspiciousx02.webp"
image bGuy_b_exp_eyebrows suspiciousx03 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyebrows_suspiciousx03.webp"
image bGuy_b_exp_eyebrows sadx01 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyebrows_sadx01.webp"
image bGuy_b_exp_eyebrows sadx02 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyebrows_sadx02.webp"
image bGuy_b_exp_eyebrows sadx03 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyebrows_sadx03.webp"
image bGuy_b_exp_eyebrows sadx04 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyebrows_sadx04.webp"

image bGuy_b_exp_eyes 00 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyes_00.webp"
image bGuy_b_exp_eyes 02 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyes_02.webp"
image bGuy_b_exp_eyes 03 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyes_03.webp"
image bGuy_b_exp_eyes 04 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyes_04.webp"
image bGuy_b_exp_eyes 05 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyes_05.webp"
image bGuy_b_exp_eyes 06 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyes_06.webp"
image bGuy_b_exp_eyes 07 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyes_07.webp"
image bGuy_b_exp_eyes 08 = "images/day05/aftermorning/dudes/bGuy_b_exp_eyes_08.webp"

image bGuy_b_exp_piris front00 = "images/day05/aftermorning/dudes/bGuy_b_exp_piris_front00.webp"
image bGuy_b_exp_piris front02 = "images/day05/aftermorning/dudes/bGuy_b_exp_piris_front02.webp"
image bGuy_b_exp_piris front03 = "images/day05/aftermorning/dudes/bGuy_b_exp_piris_front03.webp"
image bGuy_b_exp_piris front04 = "images/day05/aftermorning/dudes/bGuy_b_exp_piris_front04.webp"
image bGuy_b_exp_piris front05 = "images/day05/aftermorning/dudes/bGuy_b_exp_piris_front05.webp"
image bGuy_b_exp_piris front06 = Null(width=800, height=600)
image bGuy_b_exp_piris front07 = Null(width=800, height=600)
image bGuy_b_exp_piris front08 = Null(width=800, height=600)

image bGuy_b_exp_piris right00 = "images/day05/aftermorning/dudes/bGuy_b_exp_piris_right00.webp"
image bGuy_b_exp_piris right02 = "images/day05/aftermorning/dudes/bGuy_b_exp_piris_right02.webp"
image bGuy_b_exp_piris right03 = "images/day05/aftermorning/dudes/bGuy_b_exp_piris_right03.webp"
image bGuy_b_exp_piris right04 = "images/day05/aftermorning/dudes/bGuy_b_exp_piris_right04.webp"
image bGuy_b_exp_piris right05 = "images/day05/aftermorning/dudes/bGuy_b_exp_piris_right05.webp"

image bGuy_b_exp_piris left00 = "images/day05/aftermorning/dudes/bGuy_b_exp_piris_left00.webp"
image bGuy_b_exp_piris left02 = "images/day05/aftermorning/dudes/bGuy_b_exp_piris_left02.webp"
image bGuy_b_exp_piris left03 = "images/day05/aftermorning/dudes/bGuy_b_exp_piris_left03.webp"
image bGuy_b_exp_piris left04 = "images/day05/aftermorning/dudes/bGuy_b_exp_piris_left04.webp"
image bGuy_b_exp_piris left05 = "images/day05/aftermorning/dudes/bGuy_b_exp_piris_left05.webp"

image bGuy_b_exp_mouth happy_Silentx01 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_happy_Silentx01.webp"
image bGuy_b_exp_mouth happy_Silentx02 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_happy_Silentx02.webp"
image bGuy_b_exp_mouth happy_Silentx03 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_happy_Silentx03.webp"
image bGuy_b_exp_mouth happy_Silentx04 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_happy_Silentx04.webp"
image bGuy_b_exp_mouth happy_Silentx05 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_happy_Silentx05.webp"
image bGuy_b_exp_mouth happy_Silentx06 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_happy_Silentx06.webp"

image bGuy_b_exp_mouth happy_Talkingx01 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_happy_Talkingx01.webp"
image bGuy_b_exp_mouth happy_Talkingx02 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_happy_Talkingx02.webp"
image bGuy_b_exp_mouth happy_Talkingx03 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_happy_Talkingx03.webp"
image bGuy_b_exp_mouth happy_Talkingx04 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_happy_Talkingx04.webp"
image bGuy_b_exp_mouth happy_Talkingx05 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_happy_Talkingx05.webp"
image bGuy_b_exp_mouth happy_Talkingx06 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_happy_Talkingx06.webp"

image bGuy_b_exp_mouth sad_Silentx01 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_sad_Silentx01.webp"
image bGuy_b_exp_mouth sad_Silentx02 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_sad_Silentx02.webp"
image bGuy_b_exp_mouth sad_Silentx03 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_sad_Silentx03.webp"
image bGuy_b_exp_mouth sad_Silentx04 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_sad_Silentx04.webp"
image bGuy_b_exp_mouth sad_Silentx05 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_sad_Silentx05.webp"
image bGuy_b_exp_mouth sad_Silentx06 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_sad_Silentx06.webp"

image bGuy_b_exp_mouth sad_Talkingx01 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_sad_Talkingx01.webp"
image bGuy_b_exp_mouth sad_Talkingx02 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_sad_Talkingx02.webp"
image bGuy_b_exp_mouth sad_Talkingx03 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_sad_Talkingx03.webp"
image bGuy_b_exp_mouth sad_Talkingx04 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_sad_Talkingx04.webp"
image bGuy_b_exp_mouth sad_Talkingx05 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_sad_Talkingx05.webp"
image bGuy_b_exp_mouth sad_Talkingx06 = "images/day05/aftermorning/dudes/bGuy_b_exp_mouth_sad_Talkingx06.webp"