
image p_ao_sex_smack_effect:
    truecenter
    zoom 1.0
    additive 1.0
    alpha 0.5
    "hit 09"
    pause 0.05
    "hit 10"
    pause 0.05
    "hit 22"
    pause 0.05
    "hit 23"
    pause 0.05
    alpha 0.0

label p_ao_n_changes:

## SMACKS

    if p_ao_assSmacked in ["before"]:
        show p_ao_sex_smack_effect
        pause 0.15
    else:
        hide p_ao_sex_smack_effect

    if p_ao_assSmacked == "right":
        $ p_ao_assSmacksR += 1
    elif p_ao_assSmacked == "left":
        $ p_ao_assSmacksL += 1

    if p_ao_assSmacksL == 1:
        $ p_ao_mcAssSmacks_list.append("l01")
    elif p_ao_assSmacksL == 2:
        $ p_ao_mcAssSmacks_list.append("l02")
    elif p_ao_assSmacksL == 3:
        $ p_ao_mcAssSmacks_list.append("l03")
    elif p_ao_assSmacksL == 4:
        $ p_ao_mcAssSmacks_list.append("l04")
    elif p_ao_assSmacksL == 5:
        $ p_ao_mcAssSmacks_list.append("l05")

    if p_ao_assSmacksR == 1:
        $ p_ao_mcAssSmacks_list.append("r01")
    elif p_ao_assSmacksR == 2:
        $ p_ao_mcAssSmacks_list.append("r02")
    elif p_ao_assSmacksR == 3:
        $ p_ao_mcAssSmacks_list.append("r03")
    elif p_ao_assSmacksR == 4:
        $ p_ao_mcAssSmacks_list.append("r04")
    elif p_ao_assSmacksR == 5:
        $ p_ao_mcAssSmacks_list.append("r05")

    if p_ao_assSmacked != "":
        $ p_ao_assSmacked = ""
        $ p_ao_assSmack = ""


## Horns

    if p_ao_n_horns_num > 5:
        $ p_ao_n_horns = "_h_05"

    elif p_ao_n_horns_num == 0:
        $ p_ao_n_horns = ""

    else:
        $ p_ao_n_horns = "_h_0" + str(p_ao_n_horns_num)

## Reddish Dick

    if p_ao_n_dick_num > 5:
        $ p_ao_n_dick = "_r_05"

    elif p_ao_n_dick_num == 0:
        $ p_ao_n_dick = ""

    else:
        $ p_ao_n_dick = "_r_0" + str(p_ao_n_dick_num)

    return


######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##
##


image n_closefromup_p_ao_01:

    contains:
        "n_closefromup_body naked_FULL"
        truecenter

    contains:
        "n_closefromup_expression_compImage"
        truecenter

    contains:
        "n_closefromup_hair_front"
        truecenter
    

transform n_closefromup_iLight_compImage_trans:
    subpixel True
    subpixel True
    truecenter
    additive 1.0
    alpha ped_neus_whispers_sfx04

transform n_closefromup_l_iris_compImage_trans:
    subpixel True
    subpixel True
    truecenter
    alpha ped_neus_whispers_sfx04

image n_closefromup_expression_compImage:

## Blush

    contains:
        ConditionSwitch(
            nblushNumber in ["01", "02", "03", "04", "05", "06", "07", "08",], At("n_closefromup_blush [nblushNumber]", truecenter),
            "True", Null())

    # contains:
    #     "n_closefromup_blush 06"
    #     truecenter
## Eyes

    contains:
        ConditionSwitch(
            nteye in [0, "front00", "front00b", "down00", "down00b", "right00", "left00"], At("n_closefromup_eyes 00", truecenter),
            nteye in [1, "front01", "front01b", "down01", "down01b", "right01", "left01"], At("n_closefromup_eyes 01", truecenter),
            nteye in [2, "front02", "front02b", "down02", "down02b", "right02", "left02"], At("n_closefromup_eyes 02", truecenter),
            nteye in [3, "front03", "front03b", "down03", "down03b", "right03", "left03"], At("n_closefromup_eyes 03", truecenter),
            nteye in [4, "front04", "front04b", "down04", "down04b", "right04", "left04"], At("n_closefromup_eyes 04", truecenter),
            nteye in [5, "front05", "front05b", "down05", "down05b", "right05", "left05"], At("n_closefromup_eyes 05", truecenter),
            nteye in [6, "front06", "front06b", "down06", "down06b", "right06", "left06"], At("n_closefromup_eyes 06", truecenter),
            nteye in [7, "front07", "front07b", "down07", "down07b", "right07", "left07"], At("n_closefromup_eyes 07", truecenter),
            nteye in [8, "front08", "front08b", "down08", "down08b", "right08", "left08"], At("n_closefromup_eyes 08", truecenter),
            "True", At("n_closefromup_eyes 08, truecenter"))
    # contains:
    #     "n_closefromup_eyes 02"
    #     truecenter
## Iris
    
    contains:
        ConditionSwitch(
            nteye == "front00", At("n_closefromup_iris front00", truecenter),
            nteye == "front01", At("n_closefromup_iris front01", truecenter),
            nteye == "front02", At("n_closefromup_iris front02", truecenter),
            nteye == "front03", At("n_closefromup_iris front03", truecenter),
            nteye == "front04", At("n_closefromup_iris front04", truecenter),
            nteye == "front05", At("n_closefromup_iris front05", truecenter),
            nteye == "front06", At("n_closefromup_iris front06", truecenter),
            nteye == "front07", At("n_closefromup_iris front07", truecenter),
            nteye == "front08", At("n_closefromup_iris front08", truecenter),

            nteye == "front00b", At("n_closefromup_iris front00b", truecenter),
            nteye == "front01b", At("n_closefromup_iris front01b", truecenter),
            nteye == "front02b", At("n_closefromup_iris front02b", truecenter),
            nteye == "front03b", At("n_closefromup_iris front03b", truecenter),
            nteye == "front04b", At("n_closefromup_iris front04b", truecenter),
            nteye == "front05b", At("n_closefromup_iris front05b", truecenter),

            nteye == "right00", At("n_closefromup_iris right00", truecenter),
            nteye == "right01", At("n_closefromup_iris right01", truecenter),
            nteye == "right02", At("n_closefromup_iris right02", truecenter),
            nteye == "right03", At("n_closefromup_iris right03", truecenter),
            nteye == "right04", At("n_closefromup_iris right04", truecenter),
            nteye == "right05", At("n_closefromup_iris right05", truecenter),

            nteye == "left00", At("n_closefromup_iris left00", truecenter),
            nteye == "left01", At("n_closefromup_iris left01", truecenter),
            nteye == "left02", At("n_closefromup_iris left02", truecenter),
            nteye == "left03", At("n_closefromup_iris left03", truecenter),
            nteye == "left04", At("n_closefromup_iris left04", truecenter),
            nteye == "left05", At("n_closefromup_iris left05", truecenter),

            nteye == "down00", At("n_closefromup_iris down00", truecenter),
            nteye == "down01", At("n_closefromup_iris down01", truecenter),
            nteye == "down02", At("n_closefromup_iris down02", truecenter),
            nteye == "down03", At("n_closefromup_iris down03", truecenter),
            nteye == "down04", At("n_closefromup_iris down04", truecenter),
            nteye == "down05", At("n_closefromup_iris down05", truecenter),

            nteye == "up00", At("n_closefromup_iris up00", truecenter),
            nteye == "up01", At("n_closefromup_iris up01", truecenter),
            nteye == "up02", At("n_closefromup_iris up02", truecenter),
            nteye == "up03", At("n_closefromup_iris up03", truecenter),
            nteye == "up04", At("n_closefromup_iris up04", truecenter),
            nteye == "up05", At("n_closefromup_iris up05", truecenter),

            "True", At("n_closefromup_iris front08", truecenter))
    # contains:
    #     "n_closefromup_iris front02"
    #     truecenter
## Violet Iris

    contains:
        ConditionSwitch(
            nteye == "front00", At("n_closefromup_l_iris front00", n_closefromup_l_iris_compImage_trans),
            nteye == "front01", At("n_closefromup_l_iris front01", n_closefromup_l_iris_compImage_trans),
            nteye == "front02", At("n_closefromup_l_iris front02", n_closefromup_l_iris_compImage_trans),
            nteye == "front03", At("n_closefromup_l_iris front03", n_closefromup_l_iris_compImage_trans),
            nteye == "front04", At("n_closefromup_l_iris front04", n_closefromup_l_iris_compImage_trans),
            nteye == "front05", At("n_closefromup_l_iris front05", n_closefromup_l_iris_compImage_trans),
            nteye == "front06", At("n_closefromup_l_iris front06", n_closefromup_l_iris_compImage_trans),
            nteye == "front07", At("n_closefromup_l_iris front07", n_closefromup_l_iris_compImage_trans),
            nteye == "front08", At("n_closefromup_l_iris front08", n_closefromup_l_iris_compImage_trans),

            nteye == "front00b", At("n_closefromup_l_iris front00b", n_closefromup_l_iris_compImage_trans),
            nteye == "front01b", At("n_closefromup_l_iris front01b", n_closefromup_l_iris_compImage_trans),
            nteye == "front02b", At("n_closefromup_l_iris front02b", n_closefromup_l_iris_compImage_trans),
            nteye == "front03b", At("n_closefromup_l_iris front03b", n_closefromup_l_iris_compImage_trans),
            nteye == "front04b", At("n_closefromup_l_iris front04b", n_closefromup_l_iris_compImage_trans),
            nteye == "front05b", At("n_closefromup_l_iris front05b", n_closefromup_l_iris_compImage_trans),

            nteye == "right00", At("n_closefromup_l_iris right00", n_closefromup_l_iris_compImage_trans),
            nteye == "right01", At("n_closefromup_l_iris right01", n_closefromup_l_iris_compImage_trans),
            nteye == "right02", At("n_closefromup_l_iris right02", n_closefromup_l_iris_compImage_trans),
            nteye == "right03", At("n_closefromup_l_iris right03", n_closefromup_l_iris_compImage_trans),
            nteye == "right04", At("n_closefromup_l_iris right04", n_closefromup_l_iris_compImage_trans),
            nteye == "right05", At("n_closefromup_l_iris right05", n_closefromup_l_iris_compImage_trans),

            nteye == "left00", At("n_closefromup_l_iris left00", n_closefromup_l_iris_compImage_trans),
            nteye == "left01", At("n_closefromup_l_iris left01", n_closefromup_l_iris_compImage_trans),
            nteye == "left02", At("n_closefromup_l_iris left02", n_closefromup_l_iris_compImage_trans),
            nteye == "left03", At("n_closefromup_l_iris left03", n_closefromup_l_iris_compImage_trans),
            nteye == "left04", At("n_closefromup_l_iris left04", n_closefromup_l_iris_compImage_trans),
            nteye == "left05", At("n_closefromup_l_iris left05", n_closefromup_l_iris_compImage_trans),

            nteye == "down00", At("n_closefromup_l_iris down00", n_closefromup_l_iris_compImage_trans),
            nteye == "down01", At("n_closefromup_l_iris down01", n_closefromup_l_iris_compImage_trans),
            nteye == "down02", At("n_closefromup_l_iris down02", n_closefromup_l_iris_compImage_trans),
            nteye == "down03", At("n_closefromup_l_iris down03", n_closefromup_l_iris_compImage_trans),
            nteye == "down04", At("n_closefromup_l_iris down04", n_closefromup_l_iris_compImage_trans),
            nteye == "down05", At("n_closefromup_l_iris down05", n_closefromup_l_iris_compImage_trans),

            nteye == "up00", At("n_closefromup_l_iris up00", n_closefromup_l_iris_compImage_trans),
            nteye == "up01", At("n_closefromup_l_iris up01", n_closefromup_l_iris_compImage_trans),
            nteye == "up02", At("n_closefromup_l_iris up02", n_closefromup_l_iris_compImage_trans),
            nteye == "up03", At("n_closefromup_l_iris up03", n_closefromup_l_iris_compImage_trans),
            nteye == "up04", At("n_closefromup_l_iris up04", n_closefromup_l_iris_compImage_trans),
            nteye == "up05", At("n_closefromup_l_iris up05", n_closefromup_l_iris_compImage_trans),

            "True", At("n_closefromup_l_iris front08", truecenter))

    # contains:
    #     "n_closefromup_l_iris front02"
    #     truecenter
## Eyebrows
    
    contains:
        ConditionSwitch(
        ped_sex_general_expression_Cond == "closed", At("n_closefromup_eyebrows surprise_01", truecenter),
        ped_sex_general_expression_Cond in ["sharp_closed_angryx02", "sharp_closed_blood_angryx02", "sharp_open_blood_angryx02", "sharp_open_blood_angryx02"], At("n_closefromup_eyebrows angryx02", truecenter),
        "True", At("n_closefromup_eyebrows serious", truecenter))

    # contains:
    #     "n_closefromup_eyebrows serious"
    #     truecenter

## Tears #Not Finished (Necessary?)
    
    contains:
        ConditionSwitch(
            nteye in [1, "front01", "front01b", "down01", "down01b", "right01", "left01"] and ntlong == 1, At("n_closefromup_tears 01_01", truecenter),
            "True", At("n_closefromup_tears 00_00", truecenter))

    # contains:
    #     "n_closefromup_tears 02_03"
    #     truecenter
## Mouth
    
    contains:
        ConditionSwitch(
        ped_sex_general_expression_Cond == "closed", At("n_closefromup_mouth sad_Silentx02", truecenter),
        ped_sex_general_expression_Cond == "sharp_closed_angryx02", At("n_closefromup_mouth extra_sharp_closed", truecenter),
        ped_sex_general_expression_Cond == "sharp_closed_blood_angryx02", At("n_closefromup_mouth extra_sharp_closed_blood", truecenter),
        ped_sex_general_expression_Cond == "sharp_open_blood_angryx02", At("n_closefromup_mouth extra_sharp_open_blood", truecenter),
        ped_sex_general_expression_Cond == "sharp_open_blood_angryx02", At("n_closefromup_mouth extra_sharp_open_blood", truecenter),
        "True", At("n_closefromup_mouth sad_Silentx02", truecenter))

    # contains:
    #     "n_closefromup_mouth sad_Silentx02"
    #     truecenter

## Light Iris
    
    contains:
        ConditionSwitch(
            nteye == "front00", At("n_closefromup_iLight front00", n_closefromup_iLight_compImage_trans),
            nteye == "front01", At("n_closefromup_iLight front01", n_closefromup_iLight_compImage_trans),
            nteye == "front02", At("n_closefromup_iLight front02", n_closefromup_iLight_compImage_trans),
            nteye == "front03", At("n_closefromup_iLight front03", n_closefromup_iLight_compImage_trans),
            nteye == "front04", At("n_closefromup_iLight front04", n_closefromup_iLight_compImage_trans),
            nteye == "front05", At("n_closefromup_iLight front05", n_closefromup_iLight_compImage_trans),
            nteye == "front06", At("n_closefromup_iLight front06", n_closefromup_iLight_compImage_trans),
            nteye == "front07", At("n_closefromup_iLight front07", n_closefromup_iLight_compImage_trans),
            nteye == "front08", At("n_closefromup_iLight front08", n_closefromup_iLight_compImage_trans),

            nteye == "front00b", At("n_closefromup_iLight front00b", n_closefromup_iLight_compImage_trans),
            nteye == "front01b", At("n_closefromup_iLight front01b", n_closefromup_iLight_compImage_trans),
            nteye == "front02b", At("n_closefromup_iLight front02b", n_closefromup_iLight_compImage_trans),
            nteye == "front03b", At("n_closefromup_iLight front03b", n_closefromup_iLight_compImage_trans),
            nteye == "front04b", At("n_closefromup_iLight front04b", n_closefromup_iLight_compImage_trans),
            nteye == "front05b", At("n_closefromup_iLight front05b", n_closefromup_iLight_compImage_trans),

            nteye == "right00", At("n_closefromup_iLight right00", n_closefromup_iLight_compImage_trans),
            nteye == "right01", At("n_closefromup_iLight right01", n_closefromup_iLight_compImage_trans),
            nteye == "right02", At("n_closefromup_iLight right02", n_closefromup_iLight_compImage_trans),
            nteye == "right03", At("n_closefromup_iLight right03", n_closefromup_iLight_compImage_trans),
            nteye == "right04", At("n_closefromup_iLight right04", n_closefromup_iLight_compImage_trans),
            nteye == "right05", At("n_closefromup_iLight right05", n_closefromup_iLight_compImage_trans),

            nteye == "left00", At("n_closefromup_iLight left00", n_closefromup_iLight_compImage_trans),
            nteye == "left01", At("n_closefromup_iLight left01", n_closefromup_iLight_compImage_trans),
            nteye == "left02", At("n_closefromup_iLight left02", n_closefromup_iLight_compImage_trans),
            nteye == "left03", At("n_closefromup_iLight left03", n_closefromup_iLight_compImage_trans),
            nteye == "left04", At("n_closefromup_iLight left04", n_closefromup_iLight_compImage_trans),
            nteye == "left05", At("n_closefromup_iLight left05", n_closefromup_iLight_compImage_trans),

            nteye == "down00", At("n_closefromup_iLight down00", n_closefromup_iLight_compImage_trans),
            nteye == "down01", At("n_closefromup_iLight down01", n_closefromup_iLight_compImage_trans),
            nteye == "down02", At("n_closefromup_iLight down02", n_closefromup_iLight_compImage_trans),
            nteye == "down03", At("n_closefromup_iLight down03", n_closefromup_iLight_compImage_trans),
            nteye == "down04", At("n_closefromup_iLight down04", n_closefromup_iLight_compImage_trans),
            nteye == "down05", At("n_closefromup_iLight down05", n_closefromup_iLight_compImage_trans),

            nteye == "up00", At("n_closefromup_iLight up00", n_closefromup_iLight_compImage_trans),
            nteye == "up01", At("n_closefromup_iLight up01", n_closefromup_iLight_compImage_trans),
            nteye == "up02", At("n_closefromup_iLight up02", n_closefromup_iLight_compImage_trans),
            nteye == "up03", At("n_closefromup_iLight up03", n_closefromup_iLight_compImage_trans),
            nteye == "up04", At("n_closefromup_iLight up04", n_closefromup_iLight_compImage_trans),
            nteye == "up05", At("n_closefromup_iLight up05", n_closefromup_iLight_compImage_trans),

            "True", At("n_closefromup_iLight front08", truecenter))

    # contains:
    #     "n_closefromup_iLight front02"
    #     truecenter
    #     additive 1.0




    # scene bg dark_a
    # $ nteye = 8
    # show n_closefromup_body sd:
    #     n_closefromup_05_position
    # show n_closefromup_blush 02:
    #     n_closefromup_05_position
    # show n_closefromup_eyes 08:
    #     n_closefromup_05_position
    # show n_closefromup_iris front08:
    #     n_closefromup_05_position
    # show n_closefromup_l_iris front08:
    #     n_closefromup_05_position
    # show n_closefromup_eyebrows serious:
    #     n_closefromup_05_position
    # show n_closefromup_tears 08_03:
    #     n_closefromup_05_position
    # show n_closefromup_mouth sad_Silentx02:
    #     n_closefromup_05_position
    # show n_closefromup_iLight empty:
    #     n_closefromup_05_position
    #     additive 1.0
    # # show n_closefromup_bright empty:
    # #     n_closefromup_05_position
    # #     additive 1.0
    # if n_withoutGlasses_story == False and n_withoutGlasses_Cond == False:
    #     show n_closefromup_glasses:
    #         n_closefromup_05_position
    # show n_closefromup_hair_front:
    #     n_closefromup_05_position
    #     call n_closefromup_tears_tears


######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##
##

image p_ao_n_orgasm_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_n_orgasm_body.webp")
image p_ao_n_orgasm_cum = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_n_orgasm_cum.webp")
image p_ao_n_orgasm_bed = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_n_orgasm_bed.webp")
image p_ao_n_orgasm_cumTEST = "images/day05/pedrera/afterOrgasm/p_ao_n_orgasm_cumTEST.webp"

image p_ao_n_orgasm_comp:

    contains:
        "bg_dark_a_blurry_01"
        truecenter
        zoom 2.5

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 1.1 xpos 1.1 ypos -0.1 #Right

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 1.1 xpos -0.1 ypos -0.1 #Left

    contains:
        "p_ao_n_orgasm_bed"
        subpixel True
        truecenter
        block:
            ease_bounce 0.5 rotate 3
            ease 0.5 rotate -3
            ease_bounce  0.3 rotate 2
            ease 0.6 rotate -2
            repeat

    contains:
        "p_ao_n_orgasm_body"
        subpixel True
        truecenter
        block:
            ease_elastic 0.5 rotate -5
            ease_bounce 0.25 rotate 3
            ease_elastic 0.15 rotate -2
            ease_bounce 0.4 rotate 6
            easein_quad 0.5 rotate -6
            easeout_quad 0.7 rotate 7
            repeat
        

    contains:
        "p_ao_n_orgasm_cum"
        subpixel True
        transform_anchor True
        xalign 0.81 yalign 0.79
        alpha 0.75
        xpos 0.51 ypos 0.59
        zoom 0.01 alpha 0.0
        parallel:
            zoom 0.01
            easein_quad 1.0 zoom 1.0
            pause 0.25
            repeat

        parallel:
            rotate 30
            easein 1.0 rotate -50
            pause 0.25
            repeat

        parallel:
            pause 0.01
            easein_quad 0.29 alpha 1.0
            pause 0.35
            ease 0.35 alpha 0.0
            pause 0.25
            repeat 12

    contains:
        "p_ao_n_orgasm_cum"
        subpixel True
        transform_anchor True
        xalign 0.81 yalign 0.79
        alpha 0.75
        xpos 0.51 ypos 0.59
        zoom 0.01 alpha 0.0
        parallel:
            pause 0.3
            zoom 0.01
            easein_quad 1.0 zoom 1.3
            pause 0.33
            repeat

        parallel:
            pause 0.3
            rotate 30
            easein 1.0 rotate -40
            pause 0.33
            repeat

        parallel:
            pause 0.3
            pause 0.01
            easein_quad 0.29 alpha 1.0
            pause 0.35
            ease 0.35 alpha 0.0
            pause 0.33
            repeat 7

    contains:

        "night05_Cemetery_smoke_b_comp"
        truecenter
        zoom 3.0
        ypos 3.0 # Hide?
        easein_quad 30 ypos 1.0


        # block:
        #     ease 2 rotate 30
        #     ease 3 rotate -60
        #     repeat

#######

image p_ao_n_watchingYou_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_n_watchingYou_body[neyesp].webp")
image p_ao_n_watchingYou_eyes_color = "images/day05/pedrera/afterOrgasm/p_ao_n_watchingYou_eyes_color.webp"
image p_ao_n_watchingYou_eyes_bright = "images/day05/pedrera/afterOrgasm/p_ao_n_watchingYou_eyes_bright.webp"

image p_ao_n_watchingYou_comp:

    contains:
        #"bg_dark_a_blurry_01"
        "bg_ped_04"
        truecenter
        zoom 3.0

    contains:
        "p_ao_ghost_surrounded_comp"
        truecenter
        zoom 2.0 ypos 0.3

    contains:
        "p_ao_n_watchingYou_body"
        truecenter

    contains:
        "p_ao_n_watchingYou_eyes_color"
        truecenter

    contains:
        "p_ao_n_watchingYou_eyes_bright"
        truecenter
        additive 1.0

    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_pos


########################################################################################
####################################################################################################################################

image p_ao_mc_ass_bg_ground = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_bg_ground.webp")
image p_ao_mc_ass_bg_bed = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_bg_bed.webp")

image p_ao_mc_ass_n_dick_TEST = "images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_dick_TEST.webp"
image p_ao_mc_ass_n_fingers = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_fingers.webp")
image p_ao_mc_ass_n_fingers_TEST = "images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_fingers_TEST.webp"

image p_ao_mc_ass_mc_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body.webp")

image p_ao_mc_ass_mc_body_Lpart = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_Lpart.webp")
image p_ao_mc_ass_mc_body_Rpart = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_Rpart.webp")

image p_ao_mc_ass_mc_abs = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_abs.webp")
image p_ao_mc_ass_mc_dick = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_dick.webp")
image p_ao_mc_ass_mc_dick_06 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_dick_06.webp")

image p_ao_mc_ass_mc_body_asshole_below_01 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_below_01.webp")
image p_ao_mc_ass_mc_body_asshole_below_02 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_below_02.webp")
image p_ao_mc_ass_mc_body_asshole_below_03 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_below_03.webp")
image p_ao_mc_ass_mc_body_asshole_below_04 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_below_04.webp")
image p_ao_mc_ass_mc_body_asshole_below_05 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_below_05.webp")
image p_ao_mc_ass_mc_body_asshole_below_06 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_below_06.webp")


image p_ao_mc_ass_mc_body_asshole_below_f01 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_below_f01.webp")
image p_ao_mc_ass_mc_body_asshole_below_f02 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_below_f02.webp")
image p_ao_mc_ass_mc_body_asshole_below_f03 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_below_f03.webp")
image p_ao_mc_ass_mc_body_asshole_below_f04 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_below_f04.webp")
image p_ao_mc_ass_mc_body_asshole_below_f05 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_below_f05.webp")
image p_ao_mc_ass_mc_body_asshole_below_f06 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_below_f06.webp")

# image p_ao_mc_ass_mc_body_asshole_below_03_f = im.Flip("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_below_03.webp", horizontal=True)

image p_ao_mc_ass_mc_body_asshole_over_01 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_over_01.webp")
image p_ao_mc_ass_mc_body_asshole_over_02 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_over_02.webp")
image p_ao_mc_ass_mc_body_asshole_over_03 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_over_03.webp")
image p_ao_mc_ass_mc_body_asshole_over_04 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_over_04.webp")
image p_ao_mc_ass_mc_body_asshole_over_05 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_over_05.webp")
image p_ao_mc_ass_mc_body_asshole_over_06 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_over_06.webp")

image p_ao_mc_ass_mc_body_asshole_over_f01 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_over_f01.webp")
image p_ao_mc_ass_mc_body_asshole_over_f02 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_over_f02.webp")
image p_ao_mc_ass_mc_body_asshole_over_f03 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_over_f03.webp")
image p_ao_mc_ass_mc_body_asshole_over_f04 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_over_f04.webp")
image p_ao_mc_ass_mc_body_asshole_over_f05 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_over_f05.webp")
image p_ao_mc_ass_mc_body_asshole_over_f06 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_mc_body_asshole_over_f06.webp")

image p_ao_mc_ass_n_tongue_a = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_tongue_a.webp")
image p_ao_mc_ass_n_tongue_b = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_tongue_b.webp")
image p_ao_mc_ass_n_tongue_c = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_tongue_c.webp")
image p_ao_mc_ass_n_tongue_d = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_tongue_d.webp")
image p_ao_mc_ass_n_tongue_e = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_tongue_e.webp")
image p_ao_mc_ass_n_tongue_f = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_tongue_f.webp")

image p_ao_mc_ass_n_lick_head = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_lick_head.webp")
image p_ao_mc_ass_n_lick_glasses = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_lick_glasses.webp")
image p_ao_mc_ass_n_lick_head_PROVE = "images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_lick_head_PROVE.webp"

image p_ao_mc_ass_n_dick_01 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_dick_02.webp")
image p_ao_mc_ass_n_dick_02 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_dick_02.webp")
image p_ao_mc_ass_n_dick_03 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_dick_03.webp")
image p_ao_mc_ass_n_dick_04 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_dick_04.webp")
image p_ao_mc_ass_n_dick_05 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_dick_05.webp")
image p_ao_mc_ass_n_dick_06 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_dick_06.webp")

image p_ao_mc_ass_n_tail = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_tail.webp")

# image p_ao_mc_ass_n_dick_f01 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_dick_f02.webp")
# image p_ao_mc_ass_n_dick_f02 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_dick_f02.webp")
# image p_ao_mc_ass_n_dick_f03 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_dick_f03.webp")
# image p_ao_mc_ass_n_dick_f04 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_dick_f04.webp")
# image p_ao_mc_ass_n_dick_f05 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_dick_f05.webp")
# image p_ao_mc_ass_n_dick_f06 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_dick_f06.webp")


transform p_ao_mc_ass_n_lick_asshole_trans_01:
    subpixel True
    truecenter
    yzoom -1.0
    parallel:
        ease 1.2 xzoom 1.05
        ease 0.8 xzoom 0.98
        ease 0.6 xzoom 1.07
        repeat
        
    parallel:
        ease 0.5 yzoom -0.95
        ease 1.2 yzoom -1.05
        ease 0.8 yzoom -0.98
        repeat

### Neus Tongue
transform p_ao_mc_ass_n_lick_Ntongue_02:
    subpixel True
    p_ao_mcTongue_origPos
    xpos 0.88 ypos 0.7 rotate 5
    parallel:
        ease 8.0/p_ao_n_vel xpos 0.8
        ease 8.0/p_ao_n_vel xpos 0.9
        ease 8.0/p_ao_n_vel xpos 0.88
        repeat
    parallel:
        ease 8.2/p_ao_n_vel ypos 0.68
        ease 8.5/p_ao_n_vel ypos 0.72
        ease 8.8/p_ao_n_vel ypos 0.7
        repeat
    parallel:
        easein_quad 4.8/p_ao_n_vel rotate 10 # up
        ease 4.1/p_ao_n_vel rotate 0 # Down
        easeout_quad 4.3/p_ao_n_vel rotate 5
        repeat

    ### Laying Ass
    # xpos 0.88 ypos 0.25 rotate -11
    # parallel:
    #     ease 8.0/p_ao_n_vel xpos 0.86
    #     ease 8.0/p_ao_n_vel xpos 0.9
    #     ease 8.0/p_ao_n_vel xpos 0.88
    #     repeat
    # parallel:
    #     ease 8.2/p_ao_n_vel ypos 0.28
    #     ease 8.5/p_ao_n_vel ypos 0.26
    #     ease 8.8/p_ao_n_vel ypos 0.25
    #     repeat
    # parallel:
    #     easein_quad 4.8/p_ao_n_vel rotate 8 # up
    #     ease 4.1/p_ao_n_vel rotate -13 # Down
    #     easeout_quad 4.3/p_ao_n_vel rotate -11
    #     repeat

transform p_ao_mc_ass_n_lick_Ntongue_03:
    subpixel True
    p_ao_mcTongue_origPos
    # ypos 0.0 down, ypos 1.0 up
    ####xpos 0.88 ypos 0.7 rotate 5 # OLD
    xpos 1.5 ypos 0.7 rotate 2 # Beginning
    block:
        easein_quad 4.0/p_ao_n_vel xpos 1.3 ypos 0.58 rotate -2 # Introduction
        ease 4.0/p_ao_n_vel xpos 1.4 ypos 0.65 rotate 0 # Middle
        easeout_quad 4.0/p_ao_n_vel xpos 1.5 ypos 0.7 rotate 2 # Beginning
        repeat
    
transform p_ao_mc_ass_n_lick_Ntongue_04: #Long Tongue
    subpixel True
    p_ao_mcTongue_origPos
    #alpha 0.75
    # ypos 0.0 Up, ypos 1.0 Down
    ####xpos 0.88 ypos 0.7 rotate 5 # OLD
    xpos 1.5 ypos 0.7 rotate 10 # Middle
    block:
        easeout_quad 8.0/p_ao_n_vel xpos 1.0 ypos 0.68 rotate 0 # Deep
        easein_quad 8.0/p_ao_n_vel xpos 0.6 ypos 0.7 rotate -5 # Deepest
        ease_quad 8.0/p_ao_n_vel xpos 1.0 ypos 0.74 rotate 6 # Deep02
        ease 8.0/p_ao_n_vel xpos 1.5 ypos 0.7 rotate 10 # Middle
        ease 8.0/p_ao_n_vel xpos 1.8 ypos 0.7 rotate 10  # Most Out
        ease_quad 8.0/p_ao_n_vel xpos 1.5 ypos 0.7 rotate 10 # Middle
        easeout_quad 8.0/p_ao_n_vel xpos 1.0 ypos 0.74 rotate 6 # Deep02
        easein_quad 8.0/p_ao_n_vel xpos 0.6 ypos 0.7 rotate -5 # Deepest
        easeout_quad 8.0/p_ao_n_vel xpos 1.0 ypos 0.68 rotate 0 # Deep
        ease 8.0/p_ao_n_vel xpos 1.5 ypos 0.7 rotate 10 # Middle
        repeat

    # #xpos 1.0 ypos 0.68 rotate 0 # Deep
    # xpos 1.0 ypos 0.74 rotate 6 # Deep02
    # #xpos 0.6 ypos 0.7 rotate -5 # Deepest


    # block:
    #     ease 1.0 rotate 90
    #     ease 1.0 rotate -90
    #     repeat


    # block:
    #     easein_quad 4.0/p_ao_n_vel xpos 1.3 ypos 0.58 rotate -2 # Introduction
    #     ease 4.0/p_ao_n_vel xpos 1.4 ypos 0.65 rotate 0 # Middle
    #     easeout_quad 4.0/p_ao_n_vel xpos 1.5 ypos 0.7 rotate 2 # Beginning
    #     repeat

### NeusHead
transform p_ao_mc_ass_n_lick_NHead_01:
    subpixel True
    transform_anchor True
    xalign 0.151 yalign 0.4265 # lickNeusHead
    #alpha 0.75
    xpos 1.2 ypos -0.8 rotate -50 # Out, later coming.
    easein_quad 5.0 xpos 0.75 ypos 0.7 rotate 10 # Closer and breathing.
    parallel:
        ease 10.0/p_ao_n_vel xpos 0.72
        ease 12.0/p_ao_n_vel xpos 0.78
        ease 11.0/p_ao_n_vel xpos 0.75
        repeat

    parallel:
        ease 15.2/p_ao_n_vel ypos 0.71
        ease 10.5/p_ao_n_vel ypos 0.69
        ease 13.8/p_ao_n_vel ypos 0.7
        repeat
    parallel:
        ease 14.8/p_ao_n_vel rotate 15
        ease 13.1/p_ao_n_vel rotate 5
        ease 14.3/p_ao_n_vel rotate 10
        repeat

### Neus Head
transform p_ao_mc_ass_n_lick_NHead_02:
    subpixel True
    transform_anchor True
    xalign 0.151 yalign 0.4265 # lickNeusHead
    xpos 0.75 ypos 0.7 rotate 10 # Closer and breathing.
    parallel:
        ease 10.0/p_ao_n_vel xpos 0.72
        ease 12.0/p_ao_n_vel xpos 0.78
        ease 11.0/p_ao_n_vel xpos 0.75
        repeat

    parallel:
        ease 15.2/p_ao_n_vel ypos 0.71
        ease 10.5/p_ao_n_vel ypos 0.69
        ease 13.8/p_ao_n_vel ypos 0.7
        repeat
    parallel:
        ease 14.8/p_ao_n_vel rotate 15
        ease 13.1/p_ao_n_vel rotate 5
        ease 14.3/p_ao_n_vel rotate 10
        repeat
        #### If THe ass is not inverted
    # xpos 0.75 ypos 0.27 rotate -12 # Closer and breathing.
    # parallel:
    #     ease 10.0/p_ao_n_vel xpos 0.72
    #     ease 12.0/p_ao_n_vel xpos 0.78
    #     ease 11.0/p_ao_n_vel xpos 0.75
    #     repeat

    # parallel:
    #     ease 15.2/p_ao_n_vel ypos 0.3
    #     ease 10.5/p_ao_n_vel ypos 0.24
    #     ease 13.8/p_ao_n_vel ypos 0.27
    #     repeat
    # parallel:
    #     ease 14.8/p_ao_n_vel rotate -15
    #     ease 13.1/p_ao_n_vel rotate -7
    #     ease 14.3/p_ao_n_vel rotate -12
    #     repeat


### Neus Head
transform p_ao_mc_ass_n_lick_NHead_05:
    subpixel True
    transform_anchor True
    xalign 0.151 yalign 0.4265 # lickNeusHead
    xpos 0.6 ypos 0.68 rotate 20 # Closer and breathing.
    parallel:
        ease 10.0/p_ao_n_vel xpos 0.58
        ease 12.0/p_ao_n_vel xpos 0.62
        ease 11.0/p_ao_n_vel xpos 0.6
        repeat

    parallel:
        ease 15.2/p_ao_n_vel ypos 0.7
        ease 10.5/p_ao_n_vel ypos 0.67
        ease 13.8/p_ao_n_vel ypos 0.68
        repeat
    parallel:
        ease 14.8/p_ao_n_vel rotate 25
        ease 13.1/p_ao_n_vel rotate 15
        ease 14.3/p_ao_n_vel rotate 20
        repeat



transform p_ao_mc_ass_n_lick_NBreathing_01:
    #"vaporbreathing_new"
    transform_anchor True
    xalign 0.5 yalign 0.5
    zoom 4.0
    xpos 0.75 ypos 0.7 rotate 10 # Closer and breathing.
    alpha 0.0
    pause 5.0
    easein_quad 2.0 alpha 1.0

transform p_ao_mc_ass_n_lick_NBreathing_02:
    #"vaporbreathing_new"
    transform_anchor True
    xalign 0.5 yalign 0.5
    zoom 4.0
    xpos 0.75 ypos 0.7 rotate 10 # Closer and breathing.

transform p_ao_mc_ass_n_lick_MCass_general:
    truecenter
    yzoom-1.0

# transform p_ao_mc_ass_n_lick_MCass_06:
#     truecenter
#     yzoom-1.0
#     alpha 0.75

image p_ao_mc_ass_n_lick_comp_01:

    # contains:
    #     ConditionSwitch(
    #         p_ao_ground == "bed", At("p_ao_mc_ass_bg_bed", truecenter),
    #         "True", At("p_ao_mc_ass_bg_ground", truecenter))
    
    contains:
        "bg_dark_a_blurry_02"
        truecenter
        zoom 4.0

    contains:
        "p_ao_mc_ass_mc_body_Rpart"
        truecenter
        yzoom -1.0

    contains:
        "p_ao_mc_ass_mc_abs"
        truecenter
        yzoom -1.0

## MC DICK
    contains:
        "p_ao_mc_ass_mc_dick"
        truecenter
        yzoom -1.0
    # contains:
    #     ConditionSwitch(
    #         p_ao_mc_dick_num == 6, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_06_t),
    #         p_ao_mc_dick_num == 5, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_05_t),
    #         p_ao_mc_dick_num == 4, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_04_t),
    #         p_ao_mc_dick_num == 3, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_03_t),
    #         p_ao_mc_dick_num == 2, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_02_t),
    #         p_ao_mc_dick_num == 1, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_01_t),
    #         "True", At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_01_t))

## MC Ass Below
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "03_NAss", At("p_ao_mc_ass_mc_body_asshole_below_03", p_ao_mc_ass_n_lick_asshole_trans_01),
            p_ao_action_Cond == "04_NAss", At("p_ao_mc_ass_mc_body_asshole_below_04", p_ao_mc_ass_n_lick_asshole_trans_01),
            p_ao_action_Cond == "05_NAss", At("p_ao_mc_ass_mc_body_asshole_below_04", p_ao_mc_ass_n_lick_asshole_trans_01),
            "True", At("p_ao_mc_ass_mc_body_asshole_below_02", p_ao_mc_ass_n_lick_asshole_trans_01))

    # contains:
    #     "p_ao_mc_ass_mc_body_asshole_below_02"
    #     p_ao_mc_ass_n_lick_asshole_trans_01

## Neus Tongue
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "02_NAss", At("p_ao_mc_ass_n_tongue_f", p_ao_mc_ass_n_lick_Ntongue_02),
            p_ao_action_Cond == "03_NAss", At("p_ao_mc_ass_n_tongue_d", p_ao_mc_ass_n_lick_Ntongue_03),
            p_ao_action_Cond == "04_NAss", At("p_ao_mc_ass_n_tongue_b", p_ao_mc_ass_n_lick_Ntongue_04),
            p_ao_action_Cond == "05_NAss", At("p_ao_mc_ass_n_tongue_b", p_ao_mc_ass_n_lick_Ntongue_04),
            "True", Null()
            )

## MC Asshole
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "03_NAss", At("p_ao_mc_ass_mc_body_asshole_over_03", p_ao_mc_ass_n_lick_asshole_trans_01),
            p_ao_action_Cond == "04_NAss", At("p_ao_mc_ass_mc_body_asshole_over_04", p_ao_mc_ass_n_lick_asshole_trans_01),
            p_ao_action_Cond == "05_NAss", At("p_ao_mc_ass_mc_body_asshole_over_04", p_ao_mc_ass_n_lick_asshole_trans_01),
            "True", At("p_ao_mc_ass_mc_body_asshole_over_02", p_ao_mc_ass_n_lick_asshole_trans_01))

## MC Left part.

    contains:
        "p_ao_mc_ass_mc_body_Lpart"
        truecenter
        yzoom -1.0

# Neus Breath Vapor.
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "01_NAss", At("vaporbreathing_new", p_ao_mc_ass_n_lick_NBreathing_01),
            #p_ao_action_Cond == "02_NAss", At("vaporbreathing_new", p_ao_mc_ass_n_lick_NBreathing_02),
            "True", At("vaporbreathing_new", p_ao_mc_ass_n_lick_NBreathing_02))


# Neus Head
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "01_NAss", At("p_ao_mc_ass_n_lick_head", p_ao_mc_ass_n_lick_NHead_01),
            p_ao_action_Cond == "02_NAss", At("p_ao_mc_ass_n_lick_head", p_ao_mc_ass_n_lick_NHead_02),
            p_ao_action_Cond == "03_NAss", At("p_ao_mc_ass_n_lick_head", p_ao_mc_ass_n_lick_NHead_02),
            p_ao_action_Cond == "04_NAss", At("p_ao_mc_ass_n_lick_head", p_ao_mc_ass_n_lick_NHead_02),
            p_ao_action_Cond == "05_NAss", At("p_ao_mc_ass_n_lick_head", p_ao_mc_ass_n_lick_NHead_05),
            "True", Null())

# Neus Glasses
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "01_NAss", At("p_ao_mc_ass_n_lick_glasses", p_ao_mc_ass_n_lick_NHead_01),
            p_ao_action_Cond == "02_NAss", At("p_ao_mc_ass_n_lick_glasses", p_ao_mc_ass_n_lick_NHead_02),
            p_ao_action_Cond == "03_NAss", At("p_ao_mc_ass_n_lick_glasses", p_ao_mc_ass_n_lick_NHead_02),
            p_ao_action_Cond == "04_NAss", At("p_ao_mc_ass_n_lick_glasses", p_ao_mc_ass_n_lick_NHead_02),
            p_ao_action_Cond == "05_NAss", At("p_ao_mc_ass_n_lick_glasses", p_ao_mc_ass_n_lick_NHead_05),
            "True", Null())

    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_pos

################################################################
################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################
################################################################



transform mc_dick_origPos:
    transform_anchor True
    ##xalign 0.886 yalign 0.5 # Old
    xalign 0.8242 yalign 0.5 # Don't touch.

transform p_ao_mcTongue_origPos:
    transform_anchor True
    xalign 0.886 yalign 0.5 # Don't touch



image p_ao_mc_ass_n_dick_TEST_comp:

    contains:
        "p_ao_mc_ass_n_dick_TEST"
        mc_dick_origPos
        xpos 1.0 ypos 1.0


image p_ao_mc_ass_n_hips = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_mc_ass_n_hips[p_ao_n_hipsImg].webp")

image p_ao_mc_ass_comp 01:

    contains:
        ConditionSwitch(
            p_ao_ground == "bed", At("p_ao_mc_ass_bg_bed", truecenter),
            "True", At("p_ao_mc_ass_bg_ground", truecenter))

    contains:
        "p_ao_mc_ass_mc_body"
        truecenter

    contains:
        "p_ao_mc_ass_n_fingers"
        subpixel True
        transform_anchor True
        xalign 0.85 yalign 0.09 # Don't touch.
        xpos 3.0 ypos -2.5 rotate 20
        ease 3.0 xpos 2.2 ypos -2.0 rotate 0 # Top Tip
        block:
            easein 2.0 xpos 1.4 ypos -2.6 rotate -25 # Middle
            easeout 2.0 xpos 0.5 ypos -2.7 rotate -50 # Base anus.
            easein 2.0 xpos 1.4 ypos -2.6 rotate -25 # Middle
            easeout 2.0 xpos 2.2 ypos -2.0 rotate 0 # Top Tip
            repeat

    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_pos

image p_ao_mc_ass_comp 02:

    contains:
        "p_ao_mc_ass_bg_ground"
        truecenter

    contains:
        "p_ao_mc_ass_mc_body"
        truecenter

    contains:
        "p_ao_mc_ass_n_fingers"
        subpixel True
        transform_anchor True
        xalign 0.85 yalign 0.09 # Don't touch.
        xpos 2.2 ypos -2.0 rotate 0 # Top Tip
        block:
            easein 2.0 xpos 1.4 ypos -2.6 rotate -25 # Middle
            easeout 2.0 xpos 0.5 ypos -2.7 rotate -50 # Base anus.
            easein 2.0 xpos 1.4 ypos -2.6 rotate -25 # Middle
            easeout 2.0 xpos 2.2 ypos -2.0 rotate 0 # Top Tip
            repeat

    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_pos


image p_ao_mc_ass_comp 03:

    contains:
        "p_ao_mc_ass_bg_ground"
        truecenter

    contains:
        "p_ao_mc_ass_mc_body"
        truecenter

    contains:
        "p_ao_mc_ass_n_dick_02"
        subpixel True
        mc_dick_origPos
        
        xpos 1.1 ypos -0.5 rotate -10 # up
        easein_quad 5.0/p_ao_n_vel xpos 0.78 ypos -0.1 rotate -30 # Touching Ass
        block:
            easein 5.0/p_ao_n_vel xpos 0.75 rotate -60
            easeout 5.0/p_ao_n_vel xpos 0.78 rotate -30
            repeat

    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_pos

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

    # Neus Tail in Missionary:

             # ypos 0.0 Up    ypos 1.0 Down      
             # xpos 0.0 Left    xpos 1.0 Right   

transform p_ao_mc_ass_n_tailt_06:
    subpixel True
    mc_dick_origPos
    rotate -15 xpos 2.0 ypos -0.4 # Out
    block:
        easein_quad 4.0/p_ao_n_vel rotate 0 xpos 0.28 ypos 0.41 # All IN
        easeout 4.0/p_ao_n_vel rotate -15 xpos 2.0 ypos -0.4 # Out
        repeat

transform p_ao_mc_ass_n_tailt_05:
    subpixel True
    mc_dick_origPos
    rotate -20 xpos 2.0 ypos -0.58 # Out
    block:
        easein_quad 4.0/p_ao_n_vel rotate -6 xpos 1.0 ypos 0.124 # In
        easeout 4.0/p_ao_n_vel rotate -20 xpos 2.0 ypos -0.58 # Out
        repeat

transform p_ao_mc_ass_n_tailt_04:
    subpixel True
    mc_dick_origPos
    rotate -20 xpos 2.0 ypos -0.52 # Out
    block:
        easein_quad 4.0/p_ao_n_vel rotate -10 xpos 1.45 ypos -0.1 # In
        easeout 4.0/p_ao_n_vel rotate -20 xpos 2.0 ypos -0.52 # Out
        repeat

transform p_ao_mc_ass_n_tailt_03:
    subpixel True
    mc_dick_origPos
    rotate -20 xpos 2.5 ypos -0.71 # Out
    block:
        easein_quad 4.0/p_ao_n_vel rotate -15 xpos 2.1 ypos -0.4 # In
        easeout 4.0/p_ao_n_vel rotate -20 xpos 2.5 ypos -0.71 # Out
        repeat

transform p_ao_mc_ass_n_tailt_02:
    subpixel True
    mc_dick_origPos
    rotate -25 xpos 2.55 ypos -0.98 # Out
    block:
        easein_quad 4.0/p_ao_n_vel rotate -20 xpos 2.4 ypos -0.7 # In
        easeout 4.0/p_ao_n_vel rotate -25 xpos 2.55 ypos -0.98 # Out
        repeat

transform p_ao_mc_ass_n_tailt_01:
    subpixel True
    mc_dick_origPos
    rotate -30 xpos 2.53 ypos -1.28 # Tease Up
    block:
        ease 4.0/p_ao_n_vel rotate -28 xpos 2.5 ypos -1.12 # Slightly In
        ease 4.0/p_ao_n_vel rotate -30 xpos 2.55 ypos -1.2 # Tease Down
        ease 4.0/p_ao_n_vel rotate -28 xpos 2.5 ypos -1.12 # Slightly In
        ease 4.0/p_ao_n_vel rotate -30 xpos 2.53 ypos -1.28 # Tease Up
        repeat
    
    #rotate -28 xpos 2.5 ypos -1.12 # Slightly In
    #rotate -30 xpos 2.55 ypos -1.2 # Tease Down


#############
    # Neus Dick in missionary
## 06
transform p_ao_mc_ass_n_dickt_06:
    subpixel True
    mc_dick_origPos
    rotate -20 xpos 2.4 ypos -0.65 # 06 Out
    block:
        easein 4.0/p_ao_n_vel rotate -5 xpos 0.7 ypos 0.29 # 06 In.
        easeout 4.0/p_ao_n_vel rotate -20 xpos 2.4 ypos -0.65 # 06 Out
        repeat

transform p_ao_mc_ass_mc_hole_06:
    subpixel True
    truecenter
    p_ao_TESTfucker
    ypos 0.45 xzoom 0.9 yzoom 0.9 # Out
    block:
        easein 4.0/p_ao_n_vel ypos 0.5 xzoom 1.1 yzoom 1.0 # In
        easeout 4.0/p_ao_n_vel ypos 0.45 xzoom 0.8 yzoom 0.85 # Out
        repeat

transform p_ao_mc_ass_mc_hips_06:
    subpixel True
    truecenter
    zoom 2.0
    alpha p_ao_n_hipsTrans
    rotate -20 xpos 2.4 ypos -0.65 # 06 Out
    block:
        easein 4.0/p_ao_n_vel rotate -5 xpos 0.7 ypos 0.29 # 06 In.
        easeout 4.0/p_ao_n_vel rotate -20 xpos 2.4 ypos -0.65 # 06 Out
        repeat

##05
transform p_ao_mc_ass_n_dickt_05:
    subpixel True
    mc_dick_origPos
    rotate -20 xpos 1.62 ypos -0.3 # 05 out
    block:
        easein 4.0/p_ao_n_vel rotate -4 xpos 0.63 ypos 0.25 # 05 In
        easeout 4.0/p_ao_n_vel rotate -20 xpos 1.62 ypos -0.3 # 05 out
        repeat

transform p_ao_mc_ass_n_dickt_05_tease:
    subpixel True
    mc_dick_origPos
    rotate -20 xpos 1.62 ypos -0.3 # 05 out
    block:
        easein 4.0/p_ao_n_vel rotate -4 xpos 1.62 ypos -0.3 # 05 out_tease
        easeout 4.0/p_ao_n_vel rotate -20 xpos 1.62 ypos -0.3 # 05 out
        repeat

transform p_ao_mc_ass_mc_hole_05:
    subpixel True
    truecenter
    p_ao_TESTfucker
    ypos 0.45 xzoom 0.8 yzoom 0.8 # 05 out
    block:
        easein 4.0/p_ao_n_vel ypos 0.5 xzoom 1.15 yzoom 1.0 # 05 In
        easeout 4.0/p_ao_n_vel ypos 0.45 xzoom 0.8 yzoom 0.8 # 05 out
        repeat

transform p_ao_mc_ass_mc_hole_05_stop:
    subpixel True
    truecenter
    p_ao_TESTfucker
    ypos 0.45 xzoom 0.8 yzoom 0.8 # 05 out
    easein 12.0/p_ao_n_vel ypos 0.5 xzoom 1.15 yzoom 1.0 # 05 In

transform p_ao_mc_ass_mc_hole_trembling:
    subpixel True
    truecenter
    p_ao_TESTfucker
    ypos 0.45 xzoom 0.8 yzoom 0.8 # 05 out
    block:
        easein_quad 1.0 xzoom 0.85 yzoom 0.8
        easein_quad 1.0 xzoom 0.8 yzoom 0.85
        repeat

transform p_ao_mc_ass_mc_hips_05:
    subpixel True
    truecenter
    zoom 2.0
    alpha p_ao_n_hipsTrans
    rotate -20 xpos 1.62 ypos -0.3 # 05 out
    block:
        easein 4.0/p_ao_n_vel rotate -4 xpos 0.63 ypos 0.25 # 05 In
        easeout 4.0/p_ao_n_vel rotate -20 xpos 1.62 ypos -0.3 # 05 out
        repeat

##04
transform p_ao_mc_ass_n_dickt_04:
    subpixel True
    mc_dick_origPos
    rotate -20 xpos 1.2 ypos -0.02 # 04 Out
    block:
        easein 4.0/p_ao_n_vel rotate -4 xpos 0.6 ypos 0.3 # 04 In
        easeout 4.0/p_ao_n_vel rotate -20 xpos 1.2 ypos -0.02 # 04 Out
        repeat

transform p_ao_mc_ass_n_dickt_04_tease:
    subpixel True
    mc_dick_origPos
    rotate -20 xpos 1.2 ypos -0.02 # 04 Out
    block:
        easein 4.0/p_ao_n_vel rotate -10 xpos 1.2 ypos -0.02 # 04 Out_Tease
        easeout 4.0/p_ao_n_vel rotate -20 xpos 1.2 ypos -0.02 # 04 Out
        repeat

transform p_ao_mc_ass_mc_hole_04:
    subpixel True
    truecenter
    p_ao_TESTfucker
    ypos 0.5 xzoom 0.8 yzoom 0.7 # 04 Out
    block:
        easein 4.0/p_ao_n_vel ypos 0.5 xzoom 1.15 yzoom 1.0 # 04 In
        easeout 4.0/p_ao_n_vel ypos 0.5 xzoom 0.8 yzoom 0.82 # 04 Out
        repeat

transform p_ao_mc_ass_mc_hips_04:
    subpixel True
    truecenter
    zoom 2.0
    alpha p_ao_n_hipsTrans
    rotate -20 xpos 1.2 ypos -0.02 # 04 Out
    block:
        easein 4.0/p_ao_n_vel rotate -4 xpos 0.6 ypos 0.3 # 04 In
        easeout 4.0/p_ao_n_vel rotate -20 xpos 1.2 ypos -0.02 # 04 Out
        repeat

##03
transform p_ao_mc_ass_n_dickt_03:
    subpixel True
    mc_dick_origPos
    rotate -20 xpos 0.85 ypos 0.18 # 03 Out
    block:
        easein 4.0/p_ao_n_vel rotate -4 xpos 0.55 ypos 0.31 # 03 In
        easeout 4.0/p_ao_n_vel rotate -20 xpos 0.85 ypos 0.18 # 03 Out
        repeat

transform p_ao_mc_ass_mc_hole_03:
    subpixel True
    truecenter
    p_ao_TESTfucker
    ypos 0.5 xzoom 0.7 yzoom 0.83 # 03 Out
    block:
        easein 4.0/p_ao_n_vel ypos 0.5 xzoom 1.15 yzoom 1.0 # 03 In
        easeout 4.0/p_ao_n_vel ypos 0.5 xzoom 0.7 yzoom 0.83 # 03 Out
        repeat

transform p_ao_mc_ass_mc_hips_03:
    subpixel True
    truecenter
    zoom 2.0
    alpha p_ao_n_hipsTrans
    rotate -20 xpos 0.85 ypos 0.18 # 03 Out
    block:
        easein 4.0/p_ao_n_vel rotate -4 xpos 0.55 ypos 0.31 # 03 In
        easeout 4.0/p_ao_n_vel rotate -20 xpos 0.85 ypos 0.18 # 03 Out
        repeat

##02
transform p_ao_mc_ass_n_dickt_02:
    subpixel True
    mc_dick_origPos
    rotate -18 xpos 0.84 ypos 0.18 # 02 Out
    block:
        easein 4.0/p_ao_n_vel rotate -4 xpos 0.53 ypos 0.31 # 02 In
        easeout 4.0/p_ao_n_vel rotate -18 xpos 0.84 ypos 0.18 # 02 Out
        repeat
transform p_ao_mc_ass_n_dickt_02_stop:
    subpixel True
    mc_dick_origPos
    rotate -18 xpos 0.84 ypos 0.18 # 02 Out
    easein 12.0/p_ao_n_vel rotate -4 xpos 0.53 ypos 0.31 # 02 In

transform p_ao_mc_ass_mc_hole_02:
    subpixel True
    truecenter
    p_ao_TESTfucker
    ypos 0.5 xzoom 0.65 yzoom 0.85 # 02 Out
    block:
        easein 4.0/p_ao_n_vel ypos 0.5 xzoom 1.0 yzoom 1.0 # 02 In
        easeout 4.0/p_ao_n_vel ypos 0.5 xzoom 0.65 yzoom 0.85 # 02 Out
        repeat
transform p_ao_mc_ass_mc_hole_02_stop:
    subpixel True
    truecenter
    p_ao_TESTfucker
    ypos 0.5 xzoom 0.65 yzoom 0.85 # 02 Out
    easein 12.0/p_ao_n_vel ypos 0.5 xzoom 1.0 yzoom 1.0 # 02 In

transform p_ao_mc_ass_mc_hips_02:
    subpixel True
    truecenter
    zoom 2.0
    alpha p_ao_n_hipsTrans
    rotate -18 xpos 0.84 ypos 0.18 # 02 Out
    block:
        easein 4.0/p_ao_n_vel rotate -4 xpos 0.53 ypos 0.31 # 02 In
        easeout 4.0/p_ao_n_vel rotate -18 xpos 0.84 ypos 0.18 # 02 Out
        repeat
transform p_ao_mc_ass_mc_hips_02_stop_trans:
    subpixel True
    truecenter
    alpha 0.0
    zoom 2.0
    rotate -18 xpos 0.84 ypos 0.18 # 02 Out
    easein 12.0/p_ao_n_vel rotate -4 xpos 0.53 ypos 0.31 alpha 1.0# 02 In

transform p_ao_mc_ass_mc_hips_02_stop:
    subpixel True
    truecenter
    alpha p_ao_n_hipsTrans
    zoom 2.0
    rotate -18 xpos 0.84 ypos 0.18 # 02 Out
    easein 12.0/p_ao_n_vel rotate -4 xpos 0.53 ypos 0.31 # 02 In

##01
transform p_ao_mc_ass_n_dickt_01:
    mc_dick_origPos

transform p_ao_mc_ass_mc_hole_01:
    truecenter
    p_ao_TESTfucker

## Xpos+1.0 == Right // Ypos+1.0 == Down


transform p_ao_TESTfucker:
    truecenter
    alpha 1.0


## MC DICK

transform p_ao_mc_ass_mc_dick_06_t:
    subpixel True
    mc_dick_origPos
    rotate 50 xpos -0.29 ypos -0.45
    parallel:
        ease 0.8 xzoom 1.03
        ease 1.0 xzoom 0.98
        repeat
    parallel:
        ease 1.1 yzoom 0.99
        ease 0.9 yzoom 1.02
        repeat

transform p_ao_mc_ass_mc_dick_05_t:
    subpixel True
    mc_dick_origPos
    xzoom 0.895 yzoom 0.903 rotate 50 xpos -0.29 ypos -0.45
    parallel:
        ease 0.8 xzoom 0.905
        ease 1.0 xzoom 0.895
        repeat
    parallel:
        ease 1.1 yzoom 0.897
        ease 0.9 yzoom 0.903
        repeat
transform p_ao_mc_ass_mc_dick_04_t:
    mc_dick_origPos
    xzoom 0.68 yzoom 0.77  rotate 45 xpos -0.29 ypos -0.45
transform p_ao_mc_ass_mc_dick_03_t:
    mc_dick_origPos
    xzoom 0.45 yzoom 0.65  rotate 40 xpos -0.29 ypos -0.45
transform p_ao_mc_ass_mc_dick_02_t:
    mc_dick_origPos
    xzoom 0.35 yzoom 0.5  rotate 35 xpos -0.29 ypos -0.45
transform p_ao_mc_ass_mc_dick_01_t:
    mc_dick_origPos
    xzoom 0.25 yzoom 0.4 rotate 30 xpos -0.29 ypos -0.45


image p_ao_mc_ass_comp 04: # Penetration.
    
    contains:
        ConditionSwitch(
            p_ao_ground == "bed", At("p_ao_mc_ass_bg_bed", truecenter),
            "True", At("p_ao_mc_ass_bg_ground", truecenter))
    # contains:
    #     "p_ao_mc_ass_bg_ground"
    #     truecenter

## MC assBack

    contains:
        "p_ao_mc_ass_mc_body_Rpart"
        truecenter

## abs

## Asshole Below
    
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "05_tease", At("p_ao_mc_ass_mc_body_asshole_below_03", p_ao_mc_ass_mc_hole_trembling),
            p_ao_action_Cond == "04_tease", At("p_ao_mc_ass_mc_body_asshole_below_03", p_ao_mc_ass_mc_hole_trembling),

            p_ao_action_Cond in ("06", "tail_06"), At("p_ao_mc_ass_mc_body_asshole_below_06", p_ao_mc_ass_mc_hole_06),
            p_ao_action_Cond in ("05", "tail_05"), At("p_ao_mc_ass_mc_body_asshole_below_05", p_ao_mc_ass_mc_hole_05),
            p_ao_action_Cond in ("04", "tail_04"), At("p_ao_mc_ass_mc_body_asshole_below_04", p_ao_mc_ass_mc_hole_04),
            p_ao_action_Cond in ("03", "tail_03"), At("p_ao_mc_ass_mc_body_asshole_below_03", p_ao_mc_ass_mc_hole_03),
            p_ao_action_Cond in ("02", "tail_02"), At("p_ao_mc_ass_mc_body_asshole_below_02", p_ao_mc_ass_mc_hole_02),
            p_ao_action_Cond in ("02_stop", "02_stop_trans"), At("p_ao_mc_ass_mc_body_asshole_below_02", p_ao_mc_ass_mc_hole_02_stop),
            p_ao_action_Cond in ("01", "tail_01"), At("p_ao_mc_ass_mc_body_asshole_below_01", p_ao_mc_ass_mc_hole_01),
            "True", Null())
    # contains:
    #     "p_ao_mc_ass_mc_body_asshole_below_05"
    #     truecenter

# Neus DICK

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "05_tease", At("p_ao_mc_ass_n_dick_05", p_ao_mc_ass_n_dickt_05_tease),
            p_ao_action_Cond == "04_tease", At("p_ao_mc_ass_n_dick_04", p_ao_mc_ass_n_dickt_04_tease),
            p_ao_action_Cond == "06", At("p_ao_mc_ass_n_dick_06", p_ao_mc_ass_n_dickt_06),
            p_ao_action_Cond == "05", At("p_ao_mc_ass_n_dick_05", p_ao_mc_ass_n_dickt_05),
            p_ao_action_Cond == "04", At("p_ao_mc_ass_n_dick_04", p_ao_mc_ass_n_dickt_04),
            p_ao_action_Cond == "03", At("p_ao_mc_ass_n_dick_03", p_ao_mc_ass_n_dickt_03),
            p_ao_action_Cond in ("02_stop", "02_stop_trans"), At("p_ao_mc_ass_n_dick_02", p_ao_mc_ass_n_dickt_02_stop),
            p_ao_action_Cond == "02", At("p_ao_mc_ass_n_dick_02", p_ao_mc_ass_n_dickt_02),
            #p_ao_action_Cond == "01", At("p_ao_mc_ass_n_dick_02", p_ao_mc_ass_n_dick_01),
            "True", Null())

# Neus Tail

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "tail_06", At("p_ao_mc_ass_n_tail", p_ao_mc_ass_n_tailt_06),
            p_ao_action_Cond == "tail_05", At("p_ao_mc_ass_n_tail", p_ao_mc_ass_n_tailt_05),
            p_ao_action_Cond == "tail_04", At("p_ao_mc_ass_n_tail", p_ao_mc_ass_n_tailt_04),
            p_ao_action_Cond == "tail_03", At("p_ao_mc_ass_n_tail", p_ao_mc_ass_n_tailt_03),
            p_ao_action_Cond == "tail_02", At("p_ao_mc_ass_n_tail", p_ao_mc_ass_n_tailt_02),
            p_ao_action_Cond == "tail_01", At("p_ao_mc_ass_n_tail", p_ao_mc_ass_n_tailt_01),
            "True", Null())

    # contains:
    #     "p_ao_mc_ass_n_tail"
    #     #subpixel True
    #     mc_dick_origPos
    #     rotate -30 xpos 2.55 ypos -1.2 # Teasing
    #     #rotate 0 xpos 0.7 ypos -0.1 # All IN
    #     # block:
    #     #     easein 4.0/p_ao_n_vel rotate -5 xpos 0.7 ypos 0.29 # 06 In.
    #     #     easeout 4.0/p_ao_n_vel rotate -20 xpos 2.4 ypos -0.65 # 06 Out
    #     #     repeat

## Open Asshole

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "05_tease", At("p_ao_mc_ass_mc_body_asshole_over_03", p_ao_mc_ass_mc_hole_trembling),
            p_ao_action_Cond == "04_tease", At("p_ao_mc_ass_mc_body_asshole_over_03", p_ao_mc_ass_mc_hole_trembling),

            p_ao_action_Cond in ("06", "tail_06"), At("p_ao_mc_ass_mc_body_asshole_over_06", p_ao_mc_ass_mc_hole_06),
            p_ao_action_Cond in ("05", "tail_05"), At("p_ao_mc_ass_mc_body_asshole_over_05", p_ao_mc_ass_mc_hole_05),
            p_ao_action_Cond in ("04", "tail_04"), At("p_ao_mc_ass_mc_body_asshole_over_04", p_ao_mc_ass_mc_hole_04),
            p_ao_action_Cond in ("03", "tail_03"), At("p_ao_mc_ass_mc_body_asshole_over_03", p_ao_mc_ass_mc_hole_03),
            p_ao_action_Cond in ("02", "tail_02"), At("p_ao_mc_ass_mc_body_asshole_over_02", p_ao_mc_ass_mc_hole_02),
            p_ao_action_Cond in ("02_stop", "02_stop_trans"), At("p_ao_mc_ass_mc_body_asshole_over_02", p_ao_mc_ass_mc_hole_02_stop),
            p_ao_action_Cond in ("01", "tail_01"), At("p_ao_mc_ass_mc_body_asshole_over_01", p_ao_mc_ass_mc_hole_01),
            "True", Null())

## MC Dick

    contains:
        ConditionSwitch(
            p_ao_mc_dick_num == 6, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_06_t),
            p_ao_mc_dick_num == 5, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_05_t),
            p_ao_mc_dick_num == 4, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_04_t),
            p_ao_mc_dick_num == 3, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_03_t),
            p_ao_mc_dick_num == 2, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_02_t),
            p_ao_mc_dick_num == 1, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_01_t),
            "True", At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_01_t))
    # contains:
    #     "p_ao_mc_ass_mc_dick"
    #     truecenter
    #     alpha 0.5


# MC assFront

    contains:
        "p_ao_mc_ass_mc_body_Lpart"
        p_ao_TESTfucker

# Tongue

## Testicles

    contains:
        ConditionSwitch(
            p_ao_action_b_Cond in ["tongueAss00"], At("p_ao_mc_ass_n_tongue_a", p_ao_mc_ass_tongues_move_00),
            p_ao_action_b_Cond in ["tongueAss01", "tongueAss02", "tongueAss03"], At("p_ao_mc_ass_n_tongue_a", p_ao_mc_ass_tongues_move_01),
            "True", Null())

## Base Testicles
    contains:
        ConditionSwitch(
            p_ao_action_b_Cond in ["tongueAss02", "tongueAss03"], At("p_ao_mc_ass_n_tongue_a", p_ao_mc_ass_tongues_move_02),
            "True", Null())

## Asshole from blowjob
    contains:
        ConditionSwitch(
            p_ao_action_b_Cond in ["tongueAss03"], At("p_ao_mc_ass_n_tongue_a", p_ao_mc_ass_tongues_move_03),
            "True", Null())

# Neus Hips

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "06", At("p_ao_mc_ass_n_hips", p_ao_mc_ass_mc_hips_06),
            p_ao_action_Cond == "05", At("p_ao_mc_ass_n_hips", p_ao_mc_ass_mc_hips_05),
            p_ao_action_Cond == "04", At("p_ao_mc_ass_n_hips", p_ao_mc_ass_mc_hips_04),
            p_ao_action_Cond == "03", At("p_ao_mc_ass_n_hips", p_ao_mc_ass_mc_hips_03),
            p_ao_action_Cond == "02_stop", At("p_ao_mc_ass_n_hips", p_ao_mc_ass_mc_hips_02_stop),
            p_ao_action_Cond == "02_stop_trans", At("p_ao_mc_ass_n_hips", p_ao_mc_ass_mc_hips_02_stop),
            p_ao_action_Cond == "02", At("p_ao_mc_ass_n_hips", p_ao_mc_ass_mc_hips_02),
            #p_ao_action_Cond == "01", At("p_ao_mc_ass_n_dick_01", p_ao_mc_ass_n_dick_01),
            "True", Null())

    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_BIGpos


## Doggy Transform Neus Dicks
##06

transform p_ao_mc_ass_n_dick_d05_tease:
    subpixel True
    mc_dick_origPos
    rotate -10 xpos 1.87 ypos 0.45 # 05 DownTease
    #rotate 4 xpos 2.0 ypos 0.45 # 05 UpTease
    block:
        easein 4.0/p_ao_n_vel rotate 4 xpos 2.0 ypos 0.45 # 05 UpTease
        easeout 4.0/p_ao_n_vel rotate -10 xpos 1.87 ypos 0.45 # 05 DownTease
        repeat

transform p_ao_mc_ass_n_dick_d04_tease:
    subpixel True
    mc_dick_origPos
    rotate -7 xpos 1.4 ypos 0.52 # 04 DownTease
    #rotate 10 xpos 1.5 ypos 0.52 # 04 UpTease
    block:
        easein 4.0/p_ao_n_vel rotate 10 xpos 1.5 ypos 0.52 # 04 UpTease
        easeout 4.0/p_ao_n_vel rotate -7 xpos 1.4 ypos 0.52 # 04 DownTease
        repeat

transform p_ao_mc_ass_n_dick_d06:
    subpixel True
    mc_dick_origPos
    rotate -5 xpos 2.55 ypos 0.38 # 06 Out
    #rotate 24 xpos 0.6 ypos 0.74 # 06 In
    block:
        easein 4.0/p_ao_n_vel rotate 24 xpos 0.6 ypos 0.74 # 06 In
        easeout 4.0/p_ao_n_vel rotate -5 xpos 2.55 ypos 0.38 # 06 Out
        repeat

##05
transform p_ao_mc_ass_n_dick_d05:
    subpixel True
    mc_dick_origPos
    rotate -5 xpos 1.7 ypos 0.45 # 05 out
    #rotate 20 xpos 0.6 ypos 0.74 # 05 In
    block:
        easein 4.0/p_ao_n_vel rotate 20 xpos 0.6 ypos 0.77 # 05 In
        easeout 4.0/p_ao_n_vel rotate -5 xpos 1.7 ypos 0.45 # 05 out
        repeat

transform p_ao_mc_ass_n_dick_d05_stop:
    subpixel True
    mc_dick_origPos
    rotate -5 xpos 1.7 ypos 0.45 # 05 out
    #rotate 20 xpos 0.6 ypos 0.74 # 05 In
    easein 12.0/p_ao_n_vel rotate 20 xpos 0.6 ypos 0.77 # 05 In


##04
transform p_ao_mc_ass_n_dick_d04:
    subpixel True
    mc_dick_origPos
    rotate -5 xpos 1.3 ypos 0.52 # 04 Out
    #rotate 18 xpos 0.53 ypos 0.74 # 04 In
    block:
        easein 4.0/p_ao_n_vel rotate 18 xpos 0.53 ypos 0.74 # 04 In
        easeout 4.0/p_ao_n_vel rotate -5 xpos 1.3 ypos 0.52 # 04 Out
        repeat

##03
transform p_ao_mc_ass_n_dick_d03:
    subpixel True
    mc_dick_origPos
    rotate -5 xpos 0.9 ypos 0.6 # 03 Out
    #rotate 15 xpos 0.53 ypos 0.69 # 03 In
    block:
        easein 4.0/p_ao_n_vel rotate 15 xpos 0.53 ypos 0.69 # 03 In
        easeout 4.0/p_ao_n_vel rotate -5 xpos 0.9 ypos 0.6 # 03 Out
        repeat

##02
transform p_ao_mc_ass_n_dick_d02:
    subpixel True
    mc_dick_origPos
    rotate -5 xpos 0.84 ypos 0.61 # 02 Out
    #rotate 12 xpos 0.52 ypos 0.68 # 02 In
    block:
        easein 4.0/p_ao_n_vel rotate 12 xpos 0.52 ypos 0.68 # 02 In
        easeout 4.0/p_ao_n_vel rotate -5 xpos 0.84 ypos 0.61 # 02 Out
        repeat

##01
# transform p_ao_mc_ass_n_dick_d01:
#     subpixel True
#     mc_dick_origPos
#     rotate -20 xpos 1.2 ypos -0.02 # 04 Out
#     # block:
#     #     easein 4.0/p_ao_n_vel rotate -4 xpos 0.6 ypos 0.3 # 04 In
#     #     easeout 4.0/p_ao_n_vel rotate -20 xpos 1.2 ypos -0.02 # 04 Out
#     #     repeat


image p_ao_mc_ass_comp 04_doggy: # Doggy Penetration.
    
    # contains:
    #     ConditionSwitch(
    #         p_ao_ground == "bed", At("p_ao_mc_ass_bg_bed", truecenter),
    #         "True", At("p_ao_mc_ass_bg_ground", truecenter))
    
    contains:
        "bg_dark_a_blurry_02"
        truecenter
        zoom 4.0

## MC assBack

    contains:
        "p_ao_mc_ass_mc_body_Rpart"
        truecenter
        yzoom -1.0

## abs

## Asshole Below
    
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "05_stop", At("p_ao_mc_ass_mc_body_asshole_below_f05", p_ao_mc_ass_mc_hole_05_stop),
            p_ao_action_Cond == "05_tease", At("p_ao_mc_ass_mc_body_asshole_below_f03", p_ao_mc_ass_mc_hole_trembling),
            p_ao_action_Cond == "04_tease", At("p_ao_mc_ass_mc_body_asshole_below_f03", p_ao_mc_ass_mc_hole_trembling),

            p_ao_action_Cond == "06", At("p_ao_mc_ass_mc_body_asshole_below_f06", p_ao_mc_ass_mc_hole_06),
            p_ao_action_Cond == "05", At("p_ao_mc_ass_mc_body_asshole_below_f05", p_ao_mc_ass_mc_hole_05),
            p_ao_action_Cond == "04", At("p_ao_mc_ass_mc_body_asshole_below_f04", p_ao_mc_ass_mc_hole_04),
            p_ao_action_Cond == "03", At("p_ao_mc_ass_mc_body_asshole_below_f03", p_ao_mc_ass_mc_hole_03),
            p_ao_action_Cond == "02", At("p_ao_mc_ass_mc_body_asshole_below_f02", p_ao_mc_ass_mc_hole_02),
            p_ao_action_Cond in ("02_stop", "02_stop_trans"), At("p_ao_mc_ass_mc_body_asshole_below_f02", p_ao_mc_ass_mc_hole_02_stop),
            p_ao_action_Cond == "01", At("p_ao_mc_ass_mc_body_asshole_below_f01", p_ao_mc_ass_mc_hole_01),
            "True", Null())
    # contains:
    #     "p_ao_mc_ass_mc_body_asshole_below_05"
    #     truecenter

# Neus DICK

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "05_stop", At("p_ao_mc_ass_n_dick_05", p_ao_mc_ass_n_dick_d05_stop),
            p_ao_action_Cond == "05_tease", At("p_ao_mc_ass_n_dick_05", p_ao_mc_ass_n_dick_d05_tease),
            p_ao_action_Cond == "04_tease", At("p_ao_mc_ass_n_dick_04", p_ao_mc_ass_n_dick_d04_tease),
            p_ao_action_Cond == "06", At("p_ao_mc_ass_n_dick_06", p_ao_mc_ass_n_dick_d06),
            p_ao_action_Cond == "05", At("p_ao_mc_ass_n_dick_05", p_ao_mc_ass_n_dick_d05),
            p_ao_action_Cond == "04", At("p_ao_mc_ass_n_dick_04", p_ao_mc_ass_n_dick_d04),
            p_ao_action_Cond == "03", At("p_ao_mc_ass_n_dick_03", p_ao_mc_ass_n_dick_d03),
            #p_ao_action_Cond in ("02_stop", "02_stop_trans"), At("p_ao_mc_ass_n_dick_02", p_ao_mc_ass_n_dick_d02_stop),
            p_ao_action_Cond == "02", At("p_ao_mc_ass_n_dick_02", p_ao_mc_ass_n_dick_d02),
            #p_ao_action_Cond == "01", At("p_ao_mc_ass_n_dick_01", p_ao_mc_ass_n_dick_d01),
            "True", Null())

## Open Asshole

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "05_stop", At("p_ao_mc_ass_mc_body_asshole_over_f05", p_ao_mc_ass_mc_hole_05_stop),
            p_ao_action_Cond == "05_tease", At("p_ao_mc_ass_mc_body_asshole_over_f03", p_ao_mc_ass_mc_hole_trembling),
            p_ao_action_Cond == "04_tease", At("p_ao_mc_ass_mc_body_asshole_over_f03", p_ao_mc_ass_mc_hole_trembling),

            p_ao_action_Cond == "06", At("p_ao_mc_ass_mc_body_asshole_over_f06", p_ao_mc_ass_mc_hole_06),
            p_ao_action_Cond == "05", At("p_ao_mc_ass_mc_body_asshole_over_f05", p_ao_mc_ass_mc_hole_05),
            p_ao_action_Cond == "04", At("p_ao_mc_ass_mc_body_asshole_over_f04", p_ao_mc_ass_mc_hole_04),
            p_ao_action_Cond == "03", At("p_ao_mc_ass_mc_body_asshole_over_f03", p_ao_mc_ass_mc_hole_03),
            p_ao_action_Cond == "02", At("p_ao_mc_ass_mc_body_asshole_over_f02", p_ao_mc_ass_mc_hole_02),
            p_ao_action_Cond in ("02_stop", "02_stop_trans"), At("p_ao_mc_ass_mc_body_asshole_over_f02", p_ao_mc_ass_mc_hole_02_stop),
            p_ao_action_Cond == "01", At("p_ao_mc_ass_mc_body_asshole_over_f01", p_ao_mc_ass_mc_hole_01),
            "True", Null())

## MC Dick

    # contains:
    #     ConditionSwitch(
    #         p_ao_mc_dick_num == 6, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_06_t),
    #         p_ao_mc_dick_num == 5, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_05_t),
    #         p_ao_mc_dick_num == 4, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_04_t),
    #         p_ao_mc_dick_num == 3, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_03_t),
    #         p_ao_mc_dick_num == 2, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_02_t),
    #         p_ao_mc_dick_num == 1, At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_01_t),
    #         "True", At("p_ao_mc_ass_mc_dick_06", p_ao_mc_ass_mc_dick_01_t))

    contains:
        "p_ao_mc_ass_mc_dick"
        truecenter
        yzoom -1.0


# MC assFront

    contains:
        "p_ao_mc_ass_mc_body_Lpart"
        p_ao_TESTfucker
        yzoom -1.0

#### Tongue
    # ## Testicles

#     contains:
#         ConditionSwitch(
#             p_ao_action_b_Cond in ["tongueAss00"], At("p_ao_mc_ass_n_tongue_a", p_ao_mc_ass_tongues_move_00),
#             p_ao_action_b_Cond in ["tongueAss01", "tongueAss02", "tongueAss03"], At("p_ao_mc_ass_n_tongue_a", p_ao_mc_ass_tongues_move_01),
#             "True", Null())

# ## Base Testicles
#     contains:
#         ConditionSwitch(
#             p_ao_action_b_Cond in ["tongueAss02", "tongueAss03"], At("p_ao_mc_ass_n_tongue_a", p_ao_mc_ass_tongues_move_02),
#             "True", Null())

# ## Asshole from blowjob
#     contains:
#         ConditionSwitch(
#             p_ao_action_b_Cond in ["tongueAss03"], At("p_ao_mc_ass_n_tongue_a", p_ao_mc_ass_tongues_move_03),
#             "True", Null())

# Neus Hips

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "06", At("p_ao_mc_ass_n_hips", p_ao_mc_ass_mc_hips_06),
            p_ao_action_Cond == "05", At("p_ao_mc_ass_n_hips", p_ao_mc_ass_mc_hips_05),
            p_ao_action_Cond == "04", At("p_ao_mc_ass_n_hips", p_ao_mc_ass_mc_hips_04),
            p_ao_action_Cond == "03", At("p_ao_mc_ass_n_hips", p_ao_mc_ass_mc_hips_03),
            p_ao_action_Cond == "02_stop", At("p_ao_mc_ass_n_hips", p_ao_mc_ass_mc_hips_02_stop),
            p_ao_action_Cond == "02_stop_trans", At("p_ao_mc_ass_n_hips", p_ao_mc_ass_mc_hips_02_stop),
            p_ao_action_Cond == "02", At("p_ao_mc_ass_n_hips", p_ao_mc_ass_mc_hips_02),
            #p_ao_action_Cond == "01", At("p_ao_mc_ass_n_dick_01", p_ao_mc_ass_n_dick_01),
            "True", Null())

    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_BIGpos

########################################################################################
####################################################################################################################################

# Her tongues appearing licking your ass.


transform p_ao_mc_ass_tongues_move_00:
    subpixel True
    transform_anchor True
    p_ao_mcTongue_origPos

    xpos -0.1 ypos -4.3 rotate -100
    easein_quad 10.0/p_ao_n_vel xpos 0.1 ypos -3.6 rotate -85 # Testicles

    parallel:
        ease 2.0/p_ao_n_vel rotate -82
        ease 2.0/p_ao_n_vel rotate -86
        repeat
    parallel:
        ease 3.5/p_ao_n_vel ypos -3.7
        ease 3.0/p_ao_n_vel ypos -3.4
        repeat
    parallel:
        ease 3.0/p_ao_n_vel xpos 0.12
        ease 4.5/p_ao_n_vel xpos 0.08
        repeat

transform p_ao_mc_ass_tongues_move_01:
    subpixel True
    transform_anchor True
    p_ao_mcTongue_origPos

    xpos 0.1 ypos -3.6 rotate -85 # Testicles

    parallel:
        ease 2.0/p_ao_n_vel rotate -82
        ease 2.0/p_ao_n_vel rotate -86
        repeat
    parallel:
        ease 3.5/p_ao_n_vel ypos -3.7
        ease 3.0/p_ao_n_vel ypos -3.4
        repeat
    parallel:
        ease 3.0/p_ao_n_vel xpos 0.12
        ease 4.5/p_ao_n_vel xpos 0.08
        repeat

transform p_ao_mc_ass_tongues_move_02:
    subpixel True
    transform_anchor True
    p_ao_mcTongue_origPos

    #xpos 0.1 ypos -3.6 rotate -85 # Testicles
    xpos 0.1 ypos -3.4 rotate -92 # Base Testicles

    parallel:
        ease 2.3/p_ao_n_vel rotate -95
        ease 2.0/p_ao_n_vel rotate -90
        repeat
    parallel:
        ease 3.5/p_ao_n_vel ypos -3.3
        ease 3.0/p_ao_n_vel ypos -3.6
        repeat
    parallel:
        ease 2.5/p_ao_n_vel xpos 0.12
        ease 3.0/p_ao_n_vel xpos 0.08
        repeat
    
transform p_ao_mc_ass_tongues_move_03:
    subpixel True
    transform_anchor True
    p_ao_mcTongue_origPos

    xpos 0.12 ypos -2.6 rotate -102 # Asshole

    parallel:
        ease 2.4/p_ao_n_vel rotate -100
        ease 2.6/p_ao_n_vel rotate -103
        repeat
    parallel:
        ease 3.0/p_ao_n_vel ypos -2.7
        ease 3.6/p_ao_n_vel ypos -2.4
        repeat
    parallel:
        ease 2.3/p_ao_n_vel xpos 0.1
        ease 3.5/p_ao_n_vel xpos 0.13
        repeat

########################################################################################
####################################################################################################################################

image p_ao_mc_ass_tongues_comp 01:

    contains:
        "p_ao_mc_ass_bg_bed"
        truecenter

    contains:
        "p_ao_mc_ass_mc_body_Rpart"
        truecenter

    # contains:
    #     "p_ao_mc_ass_mc_abs"
    #     truecenter

    contains:
        "p_ao_mc_ass_mc_dick"
        truecenter

    contains:
        "p_ao_mc_ass_mc_body_Lpart"
        truecenter

# Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())


image p_ao_mc_ass_tongues_comp 02:

    contains:
        "bg dark_HD"
        truecenter
        zoom 1.5

    contains:
        "p_ao_mc_ass_bg_bed"
        truecenter

    contains:
        "p_ao_mc_ass_mc_body_Rpart"
        truecenter

    # contains:
    #     "p_ao_mc_ass_mc_abs"
    #     truecenter

    contains:
        "p_ao_mc_ass_mc_dick"
        truecenter

    contains:
        "p_ao_mc_ass_mc_body_Lpart"
        truecenter

    # contains:
    #     "p_ao_mc_ass_n_tongue_a"
    #     transform_anchor True
    #     p_ao_mcTongue_origPos
    #     #alpha 0.5
    #     xpos 0.76 ypos -2.5 rotate -85
    #     parallel:
    #         ease 3.8/p_ao_n_vel rotate -83
    #         ease 5.2/p_ao_n_vel rotate -87
    #         repeat
    #     parallel:
    #         ease 3.3/p_ao_n_vel xpos 0.74
    #         ease 4.5/p_ao_n_vel xpos 0.78
    #         repeat
    #     parallel:
    #         ease 4.2/p_ao_n_vel ypos -2.2
    #         ease 5.4/p_ao_n_vel ypos -2.6
    #         repeat

## Testicles

    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["tongueAss00"], At("p_ao_mc_ass_n_tongue_a", p_ao_mc_ass_tongues_move_00),
            p_ao_action_Cond in ["tongueAss01", "tongueAss02", "tongueAss03"], At("p_ao_mc_ass_n_tongue_a", p_ao_mc_ass_tongues_move_01),
            "True", Null())

## Base Testicles
    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["tongueAss02", "tongueAss03"], At("p_ao_mc_ass_n_tongue_a", p_ao_mc_ass_tongues_move_02),
            "True", Null())

## Asshole from blowjob
    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["tongueAss03"], At("p_ao_mc_ass_n_tongue_a", p_ao_mc_ass_tongues_move_03),
            "True", Null())

# Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())

transform p_ao_mc_ass_tongueAss_invertedAss:
    truecenter
    xzoom -1.0
    rotate 160


image p_ao_mc_ass_tongueAss_invert_comp 01:

    contains:
        "bg dark_HD"
        truecenter
        zoom 1.5

    contains:
        "p_ao_mc_ass_bg_bed"
        truecenter

    contains:
        "p_ao_mc_ass_mc_body_Rpart"
        p_ao_mc_ass_tongueAss_invertedAss

    # contains:
    #     "p_ao_mc_ass_mc_abs"
    #     p_ao_mc_ass_tongueAss_invertedAss

    contains:
        "p_ao_mc_ass_mc_dick"
        p_ao_mc_ass_tongueAss_invertedAss

    contains:
        "p_ao_mc_ass_mc_body_Lpart"
        p_ao_mc_ass_tongueAss_invertedAss

    contains:
        "p_ao_mc_ass_n_tongue_a"
        subpixel True
        transform_anchor True
        p_ao_mcTongue_origPos
        #alpha 0.5
        xpos 0.76 ypos -2.5 rotate -85
        parallel:
            ease 3.8/p_ao_n_vel rotate -83
            ease 5.2/p_ao_n_vel rotate -87
            repeat
        parallel:
            ease 3.3/p_ao_n_vel xpos 0.74
            ease 4.5/p_ao_n_vel xpos 0.78
            repeat
        parallel:
            ease 4.2/p_ao_n_vel ypos -2.2
            ease 5.4/p_ao_n_vel ypos -2.6
            repeat

# Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())


########################################################################################
####################################################################################################################################
########################################################################################
####################################################################################################################################
########################################################################################
####################################################################################################################################

## CRASHING BALLS

image p_ao_n_grabBalls = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_n_grabBalls.webp")

image p_ao_n_grabBalls_comp 01:

    contains:
        "bg_dark_a_blurry_01"
        truecenter
        zoom 4.0

    contains:
        "p_ao_n_grabBalls"
        truecenter

# Smoke
    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_pos

########################################################################################
####################################################################################################################################

## NIPPLE BITE-LICK

transform p_ao_n_nipple_n_lick_move:
    subpixel True
    truecenter
    parallel:
        ease 5.0 ypos 0.55
        ease 5.2 ypos 0.3
        repeat
    parallel:
        ease 3.1 xpos 0.48
        ease 3.0 xpos 0.6
        repeat
    parallel:
        ease 3.5 rotate 8
        ease 4.0 rotate -5
        repeat

image p_ao_n_nipple_mc = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_n_nipple_mc.webp")
image p_ao_n_nipple_n_bite = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_n_nipple_n_bite.webp")
image p_ao_n_nipple_n_lick = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_n_nipple_n_lick.webp")

image p_ao_n_nipple_comp:

    contains:
        "bg_dark_a_blurry_01"
        truecenter
        zoom 4.0

    contains:
        "p_ao_n_nipple_mc"
        truecenter

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "biteNipple", At("p_ao_n_nipple_n_bite", truecenter),
            "True", Null())

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "lickNipple", At("p_ao_n_nipple_n_lick", p_ao_n_nipple_n_lick_move),
            "True", Null())

# Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())



########################################################################################
####################################################################################################################################

## NEUS FROM BACK

image p_ao_n_behindLook_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_n_behindLook_body[neyesp].webp")
image p_ao_n_behindLook_iLight = "images/day05/pedrera/afterOrgasm/p_ao_n_behindLook_iLight.webp"
image p_ao_n_behindLook_l_iris = "images/day05/pedrera/afterOrgasm/p_ao_n_behindLook_l_iris.webp"
image p_ao_n_behindLook_hairFront = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_n_behindLook_hairFront[p_ao_n_horns].webp")

transform p_ao_n_behindLook_iLight_pos:
    subpixel True
    truecenter
    additive 1.0
    alpha ped_neus_whispers_sfx04

transform p_ao_n_behindLook_l_iris_pos:
    subpixel True
    truecenter
    alpha ped_neus_whispers_sfx04

transform p_ao_n_behindLook_bg_pos:
    truecenter
    zoom 4.0

image p_ao_n_behindLook_comp:

    contains:
        ConditionSwitch(
            pday_day == 6, At("morning04_bg bedroom_neus_a", p_ao_n_behindLook_bg_pos),

            "True", At("bg_dark_a_blurry_01", p_ao_n_behindLook_bg_pos))

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 3.0 ypos 1.9

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 3.0 ypos -1.1 rotate 180

# Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())

    contains:
        "p_ao_n_behindLook_body"
        truecenter

    contains:
        "p_ao_n_behindLook_l_iris"
        p_ao_n_behindLook_l_iris_pos


    contains:
        "p_ao_n_behindLook_iLight"
        p_ao_n_behindLook_iLight_pos

    contains:
        "p_ao_n_behindLook_hairFront"
        truecenter



image p_ao_n_orgasmAfter = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_n_orgasmAfter.webp")

image p_ao_n_orgasmAfter_comp:

    contains:
        "p_ao_n_orgasmAfter"
        truecenter

# Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())




########################################################################################
####################################################################################################################################

########################################################################################
####################################################################################################################################

image p_ao_neusShouting_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_neusShouting_body[neyesp].webp")
image p_ao_neusShouting_eye_bright = "images/day05/pedrera/afterOrgasm/p_ao_neusShouting_eye_bright.webp"
image p_ao_neusShouting_eye_color = "images/day05/pedrera/afterOrgasm/p_ao_neusShouting_eye_color.webp"
image p_ao_neusShouting_glasses = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_neusShouting_glasses.webp")
image p_ao_neusShouting_hairFront = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_neusShouting_hairFront.webp")

image p_ao_neusShouting_comp empty = Null(width=800, height=600)

image p_ao_neusShouting_comp:

    contains:
        "black"
        truecenter
        zoom 8.0

    contains:
        "bg_dark_a_blurry_01"
        truecenter
        zoom 4.0

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 1.5 xpos 0.65 ypos 1.3 # DownLeft

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 1.5 xpos 0.65 ypos -0.1 rotate 180 # UpLeft

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 1.5 xpos 1.45 ypos 1.3 # Down RIght

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 1.5 xpos 1.45 ypos -0.1 rotate 180 # UpRight

    contains:
        "p_ao_neusShouting_body"
        truecenter
    contains:
        "p_ao_neusShouting_eye_color"
        truecenter

    contains:
        "p_ao_neusShouting_eye_bright"
        additive 1.0
        truecenter

    # contains:
    #     "p_ao_neusShouting_glasses"
    #     truecenter

    contains:
        "p_ao_neusShouting_hairFront"
        truecenter

image p_ao_ghost_ceiling = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_ghost_ceiling.webp")

## TESTING
image p_ao_ghost_standing = "images/day05/pedrera/afterOrgasm/p_ao_ghost_standing.webp"
image p_ao_ghost_sorrounded = "images/day05/pedrera/afterOrgasm/p_ao_ghost_sorrounded.webp"
image p_ao_ghost_test = "images/day05/pedrera/afterOrgasm/p_ao_ghost_test.webp"


## Ghost
image p_ao_ghost_body_01 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_body_01[pwawSysImage].webp"
image p_ao_ghost_body_02 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_body_02[pwawSysImage].webp"
image p_ao_ghost_body_03 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_body_03[pwawSysImage].webp"
image p_ao_ghost_body_04 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_body_04[pwawSysImage].webp"
image p_ao_ghost_body_05 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_body_05[pwawSysImage].webp"

image p_ao_ghost_eyes_01 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_eyes_01[pwawSysImage].webp"
image p_ao_ghost_eyes_02 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_eyes_02[pwawSysImage].webp"
image p_ao_ghost_eyes_03 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_eyes_03[pwawSysImage].webp"
image p_ao_ghost_eyes_04 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_eyes_04[pwawSysImage].webp"
image p_ao_ghost_eyes_05 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_eyes_05[pwawSysImage].webp"

image p_ao_ghost_body_All_01 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_body_All_01.webp"
image p_ao_ghost_body_All_02 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_body_All_02.webp"
image p_ao_ghost_body_All_03 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_body_All_03.webp"
image p_ao_ghost_body_All_04 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_body_All_04.webp"
image p_ao_ghost_body_All_05 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_body_All_05.webp"

image p_ao_ghost_body_All_01_32 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_body_All_01_32.webp"
image p_ao_ghost_body_All_02_32 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_body_All_02_32.webp"
image p_ao_ghost_body_All_03_32 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_body_All_03_32.webp"
image p_ao_ghost_body_All_04_32 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_body_All_04_32.webp"
image p_ao_ghost_body_All_05_32 = "images/day05/pedrera/afterOrgasm/p_ao_ghost_body_All_05_32.webp"


image p_ao_ghost_comp_00:
    
    contains:
        "p_ao_ghost_eyes_01"
        p_ao_ghost_body_pos


image p_ao_ghost_comp_01:
    
    contains:
        "p_ao_ghost_body_01"
        #subpixel True
        p_ao_ghost_body_pos
        parallel:
            pause 5.0
            "p_ao_ghost_body_02" with Dissolve(3.3)
            pause 5.0
            "p_ao_ghost_body_03" with Dissolve(2.8)
            pause 5.0
            "p_ao_ghost_body_04" with Dissolve(3.0)
            pause 5.0
            "p_ao_ghost_body_05" with Dissolve(3.2)
            pause 5.0
            "p_ao_ghost_body_01" with Dissolve(3.1)
            repeat
        parallel:
            easein_quad 5.1 alpha 0.9
            easein_quad 4.4 alpha 0.7
            ease 6.1 alpha 0.8
            ease 3.2 alpha 0.75
            ease 5.2 alpha 1.0
            repeat

    contains:
        "p_ao_ghost_eyes_01"
        #subpixel True
        p_ao_ghost_body_pos
        additive 1.0
        parallel:
            pause 5.0
            "p_ao_ghost_eyes_02" with Dissolve(3.2)
            pause 5.0
            "p_ao_ghost_eyes_03" with Dissolve(2.9)
            pause 5.0
            "p_ao_ghost_eyes_04" with Dissolve(3.3)
            pause 5.0
            "p_ao_ghost_eyes_05" with Dissolve(2.8)
            pause 5.0
            "p_ao_ghost_eyes_01" with Dissolve(3.1)
            repeat
        parallel:
            easein_quad 5.0 alpha 0.8
            easein_quad 4.5 alpha 0.5
            ease 6.0 alpha 0.95
            ease 3.0 alpha 0.4
            ease 5.0 alpha 1.0
            repeat

image p_ao_ghost_comp_02:
    
    contains:
        "p_ao_ghost_body_02"
        #subpixel True
        p_ao_ghost_body_pos
        parallel:
            pause 5.0
            "p_ao_ghost_body_03" with Dissolve(3.3)
            pause 5.0
            "p_ao_ghost_body_05" with Dissolve(3.0)
            pause 5.0
            "p_ao_ghost_body_01" with Dissolve(3.2)
            pause 5.0
            "p_ao_ghost_body_04" with Dissolve(3.0)
            pause 5.0
            "p_ao_ghost_body_02" with Dissolve(4.0)
            repeat
        parallel:
            easein_quad 5.4 alpha 0.8
            easein_quad 3.6 alpha 1.0
            ease 6.1 alpha 0.6
            ease 3.8 alpha 0.75
            ease 4.4 alpha 1.0
            repeat

    contains:
        "p_ao_ghost_eyes_03"
        #subpixel True
        p_ao_ghost_body_pos
        additive 1.0
        parallel:
            pause 5.0
            "p_ao_ghost_eyes_05" with Dissolve(3.3)
            pause 5.0
            "p_ao_ghost_eyes_04" with Dissolve(3.0)
            pause 5.0
            "p_ao_ghost_eyes_02" with Dissolve(3.2)
            pause 5.0
            "p_ao_ghost_eyes_01" with Dissolve(3.0)
            pause 5.0
            "p_ao_ghost_eyes_03" with Dissolve(4.0)
            repeat
        parallel:
            easein_quad 5.5 alpha 1.0
            easein_quad 3.4 alpha 0.7
            ease 6.3 alpha 0.4
            ease 4.0 alpha 0.9
            ease 4.3 alpha 0.7
            repeat

image p_ao_ghost_comp_03:
    
    contains:
        "p_ao_ghost_body_03"
        #subpixel True
        p_ao_ghost_body_pos
        parallel:
            pause 5.0
            "p_ao_ghost_body_05" with Dissolve(3.4)
            pause 5.0
            "p_ao_ghost_body_03" with Dissolve(3.3)
            pause 5.0
            "p_ao_ghost_body_02" with Dissolve(3.2)
            pause 5.0
            "p_ao_ghost_body_01" with Dissolve(3.0)
            pause 5.0
            "p_ao_ghost_body_03" with Dissolve(2.8)
            repeat
        parallel:
            easein_quad 4.3 alpha 0.75
            easein_quad 4.1 alpha 1.0
            ease 6.3 alpha 0.8
            ease 4.0 alpha 0.9
            ease 5.0 alpha 1.0
            repeat

    contains:
        "p_ao_ghost_eyes_02"
        #subpixel True
        p_ao_ghost_body_pos
        additive 1.0
        parallel:
            pause 5.0
            "p_ao_ghost_eyes_04" with Dissolve(3.4)
            pause 5.0
            "p_ao_ghost_eyes_03" with Dissolve(3.3)
            pause 5.0
            "p_ao_ghost_eyes_05" with Dissolve(3.2)
            pause 5.0
            "p_ao_ghost_eyes_01" with Dissolve(3.0)
            pause 5.0
            "p_ao_ghost_eyes_02" with Dissolve(2.8)
            repeat
        parallel:
            easein_quad 4.0 alpha 0.6
            easein_quad 4.0 alpha 1.0
            ease 6.3 alpha 0.75
            ease 4.0 alpha 0.4
            ease 5.0 alpha 1.0
            repeat

image p_ao_ghost_comp_04:
    
    contains:
        "p_ao_ghost_body_04"
        #subpixel True
        p_ao_ghost_body_pos
        parallel:
            pause 5.0
            "p_ao_ghost_body_02" with Dissolve(4.0)
            pause 5.0
            "p_ao_ghost_body_01" with Dissolve(3.2)
            pause 5.0
            "p_ao_ghost_body_03" with Dissolve(2.5)
            pause 5.0
            "p_ao_ghost_body_04" with Dissolve(3.7)
            pause 5.0
            "p_ao_ghost_body_05" with Dissolve(4.1)
            repeat
        parallel:
            easein_quad 4.5 alpha 1.0
            easein_quad 5.3 alpha 0.6
            ease 5.2 alpha 0.8
            ease 4.6 alpha 0.9
            ease 5.0 alpha 0.85
            repeat

    contains:
        "p_ao_ghost_eyes_04"
        #subpixel True
        p_ao_ghost_body_pos
        additive 1.0
        parallel:
            pause 5.0
            "p_ao_ghost_eyes_03" with Dissolve(4.0)
            pause 5.0
            "p_ao_ghost_eyes_02" with Dissolve(3.2)
            pause 5.0
            "p_ao_ghost_eyes_01" with Dissolve(2.5)
            pause 5.0
            "p_ao_ghost_eyes_03" with Dissolve(3.7)
            pause 5.0
            "p_ao_ghost_eyes_02" with Dissolve(4.1)
            repeat
        parallel:
            easein_quad 4.3 alpha 0.8
            easein_quad 5.0 alpha 0.9
            ease 5.0 alpha 0.8
            ease 4.5 alpha 0.99
            ease 5.9 alpha 0.91
            repeat

image p_ao_ghost_comp_05:
    
    contains:
        "p_ao_ghost_body_05"
        #subpixel True
        p_ao_ghost_body_pos
        parallel:
            pause 5.0
            "p_ao_ghost_body_04" with Dissolve(3.5)
            pause 5.0
            "p_ao_ghost_body_03" with Dissolve(3.2)
            pause 5.0
            "p_ao_ghost_body_02" with Dissolve(2.7)
            pause 5.0
            "p_ao_ghost_body_01" with Dissolve(4.0)
            pause 5.0
            "p_ao_ghost_body_05" with Dissolve(3.5)
            repeat
        parallel:
            easein_quad 4.4 alpha 0.8
            easein_quad 6.5 alpha 0.75
            ease 3.4 alpha 0.8
            ease 6.8 alpha 0.9
            ease 4.3 alpha 1.0
            repeat

    contains:
        "p_ao_ghost_eyes_05"
        #subpixel True
        p_ao_ghost_body_pos
        additive 1.0
        parallel:
            pause 5.0
            "p_ao_ghost_eyes_04" with Dissolve(3.5)
            pause 5.0
            "p_ao_ghost_eyes_03" with Dissolve(3.2)
            pause 5.0
            "p_ao_ghost_eyes_02" with Dissolve(2.7)
            pause 5.0
            "p_ao_ghost_eyes_01" with Dissolve(4.0)
            pause 5.0
            "p_ao_ghost_eyes_05" with Dissolve(3.5)
            repeat
        parallel:
            easein_quad 4.6 alpha 0.6
            easein_quad 6.2 alpha 0.4
            ease 3.3 alpha 0.8
            ease 6.3 alpha 0.6
            ease 4.5 alpha 1.0
            repeat


transform p_ao_ghost_body_pos:
    transform_anchor True
    xalign 0.5 yalign 0.266 # Don't touch.
    zoom pwawSysZoom 

default ghost_sM = 2.5

image p_ao_ghost_surrounded_comp empty = Null(width=800, height=600)

transform p_ao_ghost_transp:
    subpixel False
    #alpha ped_neus_whispers_sfx04
    #alpha 1.0

image p_ao_ghost_surrounded_comp:
    "p_ao_ghost_surrounded_comp_pre"
    truecenter
    alpha ped_neus_whispers_sfx04

image p_ao_ghost_surrounded_comp_pre:

    contains:
        ConditionSwitch(
            ped_neus_whispers_sfx04 >= 0.8, At("p_ao_ghost_surrounded_comp_04"),
            ped_neus_whispers_sfx04 >= 0.6, At("p_ao_ghost_surrounded_comp_03"),
            ped_neus_whispers_sfx04 >= 0.4, At("p_ao_ghost_surrounded_comp_02"),
            ped_neus_whispers_sfx04 >= 0.2, At("p_ao_ghost_surrounded_comp_01"),
            "True", Null())

image p_ao_ghost_surrounded_comp_01:

    # B08
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.27*ghost_sM  xpos 0.877 ypos 0.167 rotate 220 # B08
        p_ao_ghost_transp
    # B07
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.24*ghost_sM  xpos 0.375 ypos 0.73 rotate 10 # B07
        p_ao_ghost_transp
    # B06
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.25*ghost_sM  xpos 0.555 ypos 0.692 rotate -5 # B06
        p_ao_ghost_transp
    # B05
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.25*ghost_sM  xpos 0.876 ypos 0.673 rotate -11 # B05
        p_ao_ghost_transp
    # B04
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.25*ghost_sM  xpos 0.15 ypos 0.47 rotate 71 # B04
        p_ao_ghost_transp
    # B03
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.28*ghost_sM xpos 0.09 ypos 0.13 rotate 122 # B03
        p_ao_ghost_transp

    # contains:
    #     "border_darkness_03"
    #     truecenter
    #     zoom 1.0
    #     p_ao_ghost_transp

    

image p_ao_ghost_surrounded_comp_02:

    # C18
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.77 ypos 0.6 rotate -30 # C18
        p_ao_ghost_transp
    # C17
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.18*ghost_sM  xpos 0.72 ypos 0.2 rotate 197 # C17
        p_ao_ghost_transp
    # C16
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.964 ypos 0.44 rotate -82 # C16
        p_ao_ghost_transp
    # C15
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.1 ypos 0.3 rotate 70 # C15
        p_ao_ghost_transp
    # C14
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.3 ypos 0.23 rotate 116 # C14
        p_ao_ghost_transp
    # C13
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.21*ghost_sM  xpos 0.345 ypos 0.095 rotate 145 # C13
        p_ao_ghost_transp
    # C12
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.21*ghost_sM  xpos 0.474 ypos 0.135 rotate 173 # C12
        p_ao_ghost_transp
    # C11
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.64 ypos 0.11 rotate 195 # C11
        p_ao_ghost_transp
    # C10
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.18*ghost_sM  xpos 0.84 ypos 0.4 rotate -135 # C10
        p_ao_ghost_transp
    # C09
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.2 ypos 0.15 rotate 133 # C09
        p_ao_ghost_transp
    # B08
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.27*ghost_sM  xpos 0.877 ypos 0.167 rotate 220 # B08
        p_ao_ghost_transp
    # B07
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.24*ghost_sM  xpos 0.375 ypos 0.73 rotate 10 # B07
        p_ao_ghost_transp
    # B06
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.25*ghost_sM  xpos 0.555 ypos 0.692 rotate -5 # B06
        p_ao_ghost_transp
    # B05
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.25*ghost_sM  xpos 0.876 ypos 0.673 rotate -11 # B05
        p_ao_ghost_transp
    # B04
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.25*ghost_sM  xpos 0.15 ypos 0.47 rotate 71 # B04
        p_ao_ghost_transp
    # B03
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.28*ghost_sM xpos 0.09 ypos 0.13 rotate 122 # B03
        p_ao_ghost_transp

    # contains:
    #     "border_darkness_03"
    #     truecenter
    #     zoom 1.0
    #     p_ao_ghost_transp


image p_ao_ghost_surrounded_comp_03:
    
    # D26
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.145*ghost_sM  xpos 0.594 ypos 0.235 rotate 185 # D26
        p_ao_ghost_transp
    # D25
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.145*ghost_sM  xpos 0.755 ypos 0.335 rotate -148 # D25
        p_ao_ghost_transp
    # D24
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.15*ghost_sM  xpos 0.29 ypos 0.63 rotate 17 # D24
        p_ao_ghost_transp
    # D23
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.14*ghost_sM  xpos 0.67 ypos 0.67 rotate -10 # D23
        p_ao_ghost_transp
    # D22
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.15*ghost_sM  xpos 0.88 ypos 0.54 rotate -45 # D22
        p_ao_ghost_transp
    # D21
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.15*ghost_sM  xpos 0.215 ypos 0.36 rotate 116 # D21
        p_ao_ghost_transp
    # C20
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.5 ypos 0.526 rotate -2 # C20
        p_ao_ghost_transp
    # C19
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.175 ypos 0.665 rotate 43 # C19
        p_ao_ghost_transp
    # C18
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.77 ypos 0.6 rotate -30 # C18
        p_ao_ghost_transp
    # C17
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.18*ghost_sM  xpos 0.72 ypos 0.2 rotate 197 # C17
        p_ao_ghost_transp
    # C16
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.964 ypos 0.44 rotate -82 # C16
        p_ao_ghost_transp
    # C15
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.1 ypos 0.3 rotate 70 # C15
        p_ao_ghost_transp
    # C14
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.3 ypos 0.23 rotate 116 # C14
        p_ao_ghost_transp
    # C13
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.21*ghost_sM  xpos 0.345 ypos 0.095 rotate 145 # C13
        p_ao_ghost_transp
    # C12
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.21*ghost_sM  xpos 0.474 ypos 0.135 rotate 173 # C12
        p_ao_ghost_transp
    # C11
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.64 ypos 0.11 rotate 195 # C11
        p_ao_ghost_transp
    # C10
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.18*ghost_sM  xpos 0.84 ypos 0.4 rotate -135 # C10
        p_ao_ghost_transp
    # C09
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.2 ypos 0.15 rotate 133 # C09
        p_ao_ghost_transp
    # B08
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.27*ghost_sM  xpos 0.877 ypos 0.167 rotate 220 # B08
        p_ao_ghost_transp
    # B07
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.24*ghost_sM  xpos 0.375 ypos 0.73 rotate 10 # B07
        p_ao_ghost_transp
    # B06
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.25*ghost_sM  xpos 0.555 ypos 0.692 rotate -5 # B06
        p_ao_ghost_transp
    # B05
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.25*ghost_sM  xpos 0.876 ypos 0.673 rotate -11 # B05
        p_ao_ghost_transp
    # B04
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.25*ghost_sM  xpos 0.15 ypos 0.47 rotate 71 # B04
        p_ao_ghost_transp
    # B03
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.28*ghost_sM xpos 0.09 ypos 0.13 rotate 122 # B03
        p_ao_ghost_transp

    # contains:
    #     "border_darkness_03"
    #     truecenter
    #     zoom 1.0
    #     p_ao_ghost_transp

image p_ao_ghost_surrounded_comp_04:

    # D35
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.14*ghost_sM  xpos 0.39 ypos 0.48 rotate 15 # D35
        p_ao_ghost_transp
    # D34
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.13*ghost_sM  xpos 0.623 ypos 0.565 rotate -17 # D34
        p_ao_ghost_transp
    # D33
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.14*ghost_sM  xpos 0.7 ypos 0.464 rotate -110 # D33
        p_ao_ghost_transp
    # D32
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.165*ghost_sM  xpos 0.58 ypos 0.38 rotate -170 # D32
        p_ao_ghost_transp
    # D31
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.15*ghost_sM  xpos 0.487 ypos 0.36 rotate -192 # D31
        p_ao_ghost_transp
    # D30
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.15*ghost_sM  xpos 0.4 ypos 0.33 rotate -200 # D30
        p_ao_ghost_transp
    # D29
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.15*ghost_sM  xpos 0.32 ypos 0.39 rotate 88 # D29
        p_ao_ghost_transp
    # D28
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.15*ghost_sM  xpos 0.66 ypos 0.365 rotate -111 # D28
        p_ao_ghost_transp
    # D27
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.14*ghost_sM  xpos 0.28 ypos 0.51 rotate 54 # D27
        p_ao_ghost_transp
    # D26
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.145*ghost_sM  xpos 0.594 ypos 0.235 rotate 185 # D26
        p_ao_ghost_transp
    # D25
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.145*ghost_sM  xpos 0.755 ypos 0.335 rotate -148 # D25
        p_ao_ghost_transp
    # D24
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.15*ghost_sM  xpos 0.29 ypos 0.63 rotate 17 # D24
        p_ao_ghost_transp
    # D23
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.14*ghost_sM  xpos 0.67 ypos 0.67 rotate -10 # D23
        p_ao_ghost_transp
    # D22
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.15*ghost_sM  xpos 0.88 ypos 0.54 rotate -45 # D22
        p_ao_ghost_transp
    # D21
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.15*ghost_sM  xpos 0.215 ypos 0.36 rotate 116 # D21
        p_ao_ghost_transp
    # C20
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.5 ypos 0.526 rotate -2 # C20
        p_ao_ghost_transp
    # C19
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.175 ypos 0.665 rotate 43 # C19
        p_ao_ghost_transp
    # C18
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.77 ypos 0.6 rotate -30 # C18
        p_ao_ghost_transp
    # C17
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.18*ghost_sM  xpos 0.72 ypos 0.2 rotate 197 # C17
        p_ao_ghost_transp
    # C16
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.964 ypos 0.44 rotate -82 # C16
        p_ao_ghost_transp
    # C15
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.1 ypos 0.3 rotate 70 # C15
        p_ao_ghost_transp
    # C14
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.3 ypos 0.23 rotate 116 # C14
        p_ao_ghost_transp
    # C13
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.21*ghost_sM  xpos 0.345 ypos 0.095 rotate 145 # C13
        p_ao_ghost_transp
    # C12
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.21*ghost_sM  xpos 0.474 ypos 0.135 rotate 173 # C12
        p_ao_ghost_transp
    # C11
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.64 ypos 0.11 rotate 195 # C11
        p_ao_ghost_transp
    # C10
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.18*ghost_sM  xpos 0.84 ypos 0.4 rotate -135 # C10
        p_ao_ghost_transp
    # C09
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.2 ypos 0.15 rotate 133 # C09
        p_ao_ghost_transp
    # B08
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.27*ghost_sM  xpos 0.877 ypos 0.167 rotate 220 # B08
        p_ao_ghost_transp
    # B07
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.24*ghost_sM  xpos 0.375 ypos 0.73 rotate 10 # B07
        p_ao_ghost_transp
    # B06
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.25*ghost_sM  xpos 0.555 ypos 0.692 rotate -5 # B06
        p_ao_ghost_transp
    # B05
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.25*ghost_sM  xpos 0.876 ypos 0.673 rotate -11 # B05
        p_ao_ghost_transp
    # B04
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.25*ghost_sM  xpos 0.15 ypos 0.47 rotate 71 # B04
        p_ao_ghost_transp
    # B03
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.28*ghost_sM xpos 0.09 ypos 0.13 rotate 122 # B03
        p_ao_ghost_transp

    contains:
        "border_darkness_03"
        truecenter
        zoom 1.0
        p_ao_ghost_transp




################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################

image p_ao_ghost_standing_comp empty = Null(width=800, height=600)

default p_ao_ghost_standing_resolution = ""

image p_ao_ghost_standing_comp:
    "p_ao_ghost_standing_comp_pre"
    truecenter
    alpha ped_neus_whispers_sfx04

image p_ao_ghost_standing_comp_pre:
    contains:
        ConditionSwitch(

            pwawSysImage == "_32" and ped_neus_whispers_sfx04 >= 0.8, At("p_ao_ghost_body_All_05_32", p_ao_ghost_body_All_trans_32),
            pwawSysImage == "_32" and ped_neus_whispers_sfx04 >= 0.6, At("p_ao_ghost_body_All_04_32", p_ao_ghost_body_All_trans_32),
            pwawSysImage == "_32" and ped_neus_whispers_sfx04 >= 0.4, At("p_ao_ghost_body_All_03_32", p_ao_ghost_body_All_trans_32),
            pwawSysImage == "_32" and ped_neus_whispers_sfx04 >= 0.2, At("p_ao_ghost_body_All_02_32", p_ao_ghost_body_All_trans_32),
            pwawSysImage == "_32" and ped_neus_whispers_sfx04 >= 0.1, At("p_ao_ghost_body_All_01_32", p_ao_ghost_body_All_trans_32),

            p_ao_ghost_standing_resolution == "low" and ped_neus_whispers_sfx04 >= 0.8, At("p_ao_ghost_body_All_05", p_ao_ghost_body_All_trans),
            p_ao_ghost_standing_resolution == "low" and ped_neus_whispers_sfx04 >= 0.6, At("p_ao_ghost_body_All_04", p_ao_ghost_body_All_trans),
            p_ao_ghost_standing_resolution == "low" and ped_neus_whispers_sfx04 >= 0.4, At("p_ao_ghost_body_All_03", p_ao_ghost_body_All_trans),
            p_ao_ghost_standing_resolution == "low" and ped_neus_whispers_sfx04 >= 0.2, At("p_ao_ghost_body_All_02", p_ao_ghost_body_All_trans),
            p_ao_ghost_standing_resolution == "low" and ped_neus_whispers_sfx04 >= 0.1, At("p_ao_ghost_body_All_01", p_ao_ghost_body_All_trans),
            ped_neus_whispers_sfx04 >= 0.8, At("p_ao_ghost_standing_comp_04"),
            ped_neus_whispers_sfx04 >= 0.6, At("p_ao_ghost_standing_comp_03"),
            ped_neus_whispers_sfx04 >= 0.4, At("p_ao_ghost_standing_comp_02"),
            ped_neus_whispers_sfx04 >= 0.2, At("p_ao_ghost_standing_comp_01"),
            "True", Null())


transform p_ao_ghost_body_All_trans_32:
    #subpixel True
    truecenter
    zoom 1.25 # Image is 0.4 of the original, which is 0.5=100%
    block:
        easein_quad 2.5 alpha 0.6
        easein_quad 1.8 alpha 1.0
        easein_quad 2.0 alpha 0.75
        easein_quad 1.6 alpha 1.0
        easein_quad 2.3 alpha 0.5
        easein_quad 1.0 alpha 0.95
        repeat


transform p_ao_ghost_body_All_trans:
    #subpixel True
    truecenter
    zoom 0.5
    block:
        easein_quad 2.5 alpha 0.6
        easein_quad 1.8 alpha 1.0
        easein_quad 2.0 alpha 0.75
        easein_quad 1.6 alpha 1.0
        easein_quad 2.3 alpha 0.5
        easein_quad 1.0 alpha 0.95
        repeat


image p_ao_ghost_standing_comp_01:

    # B08
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.24*ghost_sM  xpos 0.082 ypos 0.59 # B08
        p_ao_ghost_transp
    # B07
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.28*ghost_sM  xpos 0.41 ypos 0.62 # B07
        p_ao_ghost_transp
    # B06
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.28*ghost_sM  xpos 0.67 ypos 0.665 # B06
        p_ao_ghost_transp
    # B05
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.3*ghost_sM  xpos 0.885 ypos 0.71 # B05
        p_ao_ghost_transp
    # B04
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.26*ghost_sM xpos 0.225 ypos 0.695 # B04
        p_ao_ghost_transp

image p_ao_ghost_standing_comp_02:


    # F25
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.18*ghost_sM  xpos 0.252 ypos 0.222 # F25
        p_ao_ghost_transp
    # F24
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.16*ghost_sM  xpos 0.125 ypos 0.19 # F24
        p_ao_ghost_transp
    # F23
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.18*ghost_sM  xpos 0.97 ypos 0.35 # F23
        p_ao_ghost_transp
    # F22
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.175*ghost_sM  xpos 0.4 ypos 0.19 # F22
        p_ao_ghost_transp
    # F21
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.178*ghost_sM  xpos 0.635 ypos 0.22 # F21
        p_ao_ghost_transp
    # F20
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.175*ghost_sM  xpos 0.75 ypos 0.25 # F20 # no reference
        p_ao_ghost_transp
    # E19
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.17*ghost_sM  xpos 0.061 ypos 0.276 # E19
        p_ao_ghost_transp
    # E18
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.175*ghost_sM  xpos 0.85 ypos 0.38 # E18
        p_ao_ghost_transp
    # E17
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.61 ypos 0.34 # E17
        p_ao_ghost_transp
    # E16
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.19*ghost_sM  xpos 0.36 ypos 0.3 # E16
        p_ao_ghost_transp
    # D15
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.19*ghost_sM  xpos 0.19 ypos 0.335 # D15
        p_ao_ghost_transp
    # D14
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.47 ypos 0.38 # D14
        p_ao_ghost_transp
    # C13
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.06 ypos 0.4 # C13
        p_ao_ghost_transp
    # C12
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.19*ghost_sM  xpos 0.915 ypos 0.5 # C12
        p_ao_ghost_transp
    # C11
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.235*ghost_sM  xpos 0.728 ypos 0.415 # C11
        p_ao_ghost_transp
    # C10
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.3 ypos 0.45 # C10
        p_ao_ghost_transp
    # C09
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.22*ghost_sM  xpos 0.56 ypos 0.5 # C09
        p_ao_ghost_transp
    # B08
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.24*ghost_sM  xpos 0.082 ypos 0.59 # B08
        p_ao_ghost_transp
    # B07
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.28*ghost_sM  xpos 0.41 ypos 0.62 # B07
        p_ao_ghost_transp
    # B06
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.28*ghost_sM  xpos 0.67 ypos 0.665 # B06
        p_ao_ghost_transp
    # B05
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.3*ghost_sM  xpos 0.885 ypos 0.71 # B05
        p_ao_ghost_transp
    # B04
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.26*ghost_sM xpos 0.225 ypos 0.695 # B04
        p_ao_ghost_transp

image p_ao_ghost_standing_comp_03:

    # I43
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.113*ghost_sM  xpos 0.97 ypos 0.06 # I43
        p_ao_ghost_transp
    # I42
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.113*ghost_sM  xpos 0.62 ypos 0.035 # I42
        p_ao_ghost_transp
    # I41
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.128*ghost_sM  xpos 0.035 ypos 0.043 # I41
        p_ao_ghost_transp
    # I40
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.124*ghost_sM  xpos 0.246 ypos 0.043 # I40
        p_ao_ghost_transp
    # I39
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.12*ghost_sM  xpos 0.38 ypos 0.045 # I39
        p_ao_ghost_transp
    # I38
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.128*ghost_sM  xpos 0.535 ypos 0.081 # I38
        p_ao_ghost_transp
    # I37
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.12*ghost_sM  xpos 0.76 ypos 0.12 # I37
        p_ao_ghost_transp
    # I36
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.125*ghost_sM  xpos 0.883 ypos 0.106 # I36
        p_ao_ghost_transp
    # H35
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.13*ghost_sM  xpos 0.952 ypos 0.137 # H35
        p_ao_ghost_transp
    # H34
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.146*ghost_sM  xpos 0.32 ypos 0.115 # H34
        p_ao_ghost_transp
    # H33
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.14*ghost_sM  xpos 0.47 ypos 0.105 # H33
        p_ao_ghost_transp
    # H32
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.128*ghost_sM  xpos 0.115 ypos 0.09 # H32
        p_ao_ghost_transp
    # H31
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.13*ghost_sM  xpos 0.66 ypos 0.108 # H31
        p_ao_ghost_transp
    # H30
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.14*ghost_sM  xpos 0.83 ypos 0.18 # H30
        p_ao_ghost_transp
    # G29
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.156*ghost_sM  xpos 0.905 ypos 0.26 # G29
        p_ao_ghost_transp
    # G28
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.16*ghost_sM  xpos 0.03 ypos 0.15 # G28
        p_ao_ghost_transp
    # G27
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.17*ghost_sM  xpos 0.51 ypos 0.21 # G27
        p_ao_ghost_transp
    # G26
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.158*ghost_sM  xpos 0.195 ypos 0.13 # G26
        p_ao_ghost_transp
    # F25
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.18*ghost_sM  xpos 0.252 ypos 0.222 # F25
        p_ao_ghost_transp
    # F24
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.16*ghost_sM  xpos 0.125 ypos 0.19 # F24
        p_ao_ghost_transp
    # F23
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.18*ghost_sM  xpos 0.97 ypos 0.35 # F23
        p_ao_ghost_transp
    # F22
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.175*ghost_sM  xpos 0.4 ypos 0.19 # F22
        p_ao_ghost_transp
    # F21
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.178*ghost_sM  xpos 0.635 ypos 0.22 # F21
        p_ao_ghost_transp
    # F20
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.175*ghost_sM  xpos 0.75 ypos 0.25 # F20 # no reference
        p_ao_ghost_transp
    # E19
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.17*ghost_sM  xpos 0.061 ypos 0.276 # E19
        p_ao_ghost_transp
    # E18
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.175*ghost_sM  xpos 0.85 ypos 0.38 # E18
        p_ao_ghost_transp
    # E17
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.61 ypos 0.34 # E17
        p_ao_ghost_transp
    # E16
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.19*ghost_sM  xpos 0.36 ypos 0.3 # E16
        p_ao_ghost_transp
    # D15
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.19*ghost_sM  xpos 0.19 ypos 0.335 # D15
        p_ao_ghost_transp
    # D14
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.47 ypos 0.38 # D14
        p_ao_ghost_transp
    # C13
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.06 ypos 0.4 # C13
        p_ao_ghost_transp
    # C12
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.19*ghost_sM  xpos 0.915 ypos 0.5 # C12
        p_ao_ghost_transp
    # C11
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.235*ghost_sM  xpos 0.728 ypos 0.415 # C11
        p_ao_ghost_transp
    # C10
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.3 ypos 0.45 # C10
        p_ao_ghost_transp
    # C09
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.22*ghost_sM  xpos 0.56 ypos 0.5 # C09
        p_ao_ghost_transp
    # B08
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.24*ghost_sM  xpos 0.082 ypos 0.59 # B08
        p_ao_ghost_transp
    # B07
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.28*ghost_sM  xpos 0.41 ypos 0.62 # B07
        p_ao_ghost_transp
    # B06
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.28*ghost_sM  xpos 0.67 ypos 0.665 # B06
        p_ao_ghost_transp
    # B05
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.3*ghost_sM  xpos 0.885 ypos 0.71 # B05
        p_ao_ghost_transp
    # B04
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.26*ghost_sM xpos 0.225 ypos 0.695 # B04
        p_ao_ghost_transp


image p_ao_ghost_standing_comp_04:

    # K55
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.113*ghost_sM  xpos 0.92 ypos 0.01 # K55
        p_ao_ghost_transp
    # K54
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.113*ghost_sM  xpos 0.815 ypos 0.01 # K54
        p_ao_ghost_transp
    # K53
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.113*ghost_sM  xpos 0.69 ypos 0.015 # K53
        p_ao_ghost_transp
    # K52
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.113*ghost_sM  xpos 0.43 ypos 0.018 # K52
        p_ao_ghost_transp
    # K51
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.115*ghost_sM  xpos 0.32 ypos 0.03 # K51
        p_ao_ghost_transp
    # K50
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.119*ghost_sM  xpos 0.113 ypos 0.01 # K50
        p_ao_ghost_transp
    # J49
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.113*ghost_sM  xpos 0.77 ypos 0.03 # J49
        p_ao_ghost_transp
    # J48
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.113*ghost_sM  xpos 0.485 ypos 0.025 # J48
        p_ao_ghost_transp
    # J47
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.116*ghost_sM  xpos 0.183 ypos 0.034 # J47
        p_ao_ghost_transp
    # J46
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.113*ghost_sM  xpos 0.86 ypos 0.045 # J46
        p_ao_ghost_transp
    # J45
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.113*ghost_sM  xpos 0.73 ypos 0.07 # J45
        p_ao_ghost_transp
    # J44
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.113*ghost_sM  xpos 0.555 ypos 0.015 # J44
        p_ao_ghost_transp
    # I43
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.113*ghost_sM  xpos 0.97 ypos 0.06 # I43
        p_ao_ghost_transp
    # I42
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.113*ghost_sM  xpos 0.62 ypos 0.035 # I42
        p_ao_ghost_transp
    # I41
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.128*ghost_sM  xpos 0.035 ypos 0.043 # I41
        p_ao_ghost_transp
    # I40
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.124*ghost_sM  xpos 0.246 ypos 0.043 # I40
        p_ao_ghost_transp
    # I39
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.12*ghost_sM  xpos 0.38 ypos 0.045 # I39
        p_ao_ghost_transp
    # I38
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.128*ghost_sM  xpos 0.535 ypos 0.081 # I38
        p_ao_ghost_transp
    # I37
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.12*ghost_sM  xpos 0.76 ypos 0.12 # I37
        p_ao_ghost_transp
    # I36
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.125*ghost_sM  xpos 0.883 ypos 0.106 # I36
        p_ao_ghost_transp
    # H35
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.13*ghost_sM  xpos 0.952 ypos 0.137 # H35
        p_ao_ghost_transp
    # H34
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.146*ghost_sM  xpos 0.32 ypos 0.115 # H34
        p_ao_ghost_transp
    # H33
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.14*ghost_sM  xpos 0.47 ypos 0.105 # H33
        p_ao_ghost_transp
    # H32
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.128*ghost_sM  xpos 0.115 ypos 0.09 # H32
        p_ao_ghost_transp
    # H31
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.13*ghost_sM  xpos 0.66 ypos 0.108 # H31
        p_ao_ghost_transp
    # H30
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.14*ghost_sM  xpos 0.83 ypos 0.18 # H30
        p_ao_ghost_transp
    # G29
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.156*ghost_sM  xpos 0.905 ypos 0.26 # G29
        p_ao_ghost_transp
    # G28
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.16*ghost_sM  xpos 0.03 ypos 0.15 # G28
        p_ao_ghost_transp
    # G27
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.17*ghost_sM  xpos 0.51 ypos 0.21 # G27
        p_ao_ghost_transp
    # G26
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.158*ghost_sM  xpos 0.195 ypos 0.13 # G26
        p_ao_ghost_transp
    # F25
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.18*ghost_sM  xpos 0.252 ypos 0.222 # F25
        p_ao_ghost_transp
    # F24
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.16*ghost_sM  xpos 0.125 ypos 0.19 # F24
        p_ao_ghost_transp
    # F23
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.18*ghost_sM  xpos 0.97 ypos 0.35 # F23
        p_ao_ghost_transp
    # F22
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.175*ghost_sM  xpos 0.4 ypos 0.19 # F22
        p_ao_ghost_transp
    # F21
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.178*ghost_sM  xpos 0.635 ypos 0.22 # F21
        p_ao_ghost_transp
    # F20
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.175*ghost_sM  xpos 0.75 ypos 0.25 # F20 # no reference
        p_ao_ghost_transp
    # E19
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.17*ghost_sM  xpos 0.061 ypos 0.276 # E19
        p_ao_ghost_transp
    # E18
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.175*ghost_sM  xpos 0.85 ypos 0.38 # E18
        p_ao_ghost_transp
    # E17
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.61 ypos 0.34 # E17
        p_ao_ghost_transp
    # E16
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.19*ghost_sM  xpos 0.36 ypos 0.3 # E16
        p_ao_ghost_transp
    # D15
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.19*ghost_sM  xpos 0.19 ypos 0.335 # D15
        p_ao_ghost_transp
    # D14
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.47 ypos 0.38 # D14
        p_ao_ghost_transp
    # C13
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.06 ypos 0.4 # C13
        p_ao_ghost_transp
    # C12
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.19*ghost_sM  xpos 0.915 ypos 0.5 # C12
        p_ao_ghost_transp
    # C11
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.235*ghost_sM  xpos 0.728 ypos 0.415 # C11
        p_ao_ghost_transp
    # C10
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.2*ghost_sM  xpos 0.3 ypos 0.45 # C10
        p_ao_ghost_transp
    # C09
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.22*ghost_sM  xpos 0.56 ypos 0.5 # C09
        p_ao_ghost_transp
    # B08
    contains:
        "p_ao_ghost_comp_04"
        p_ao_ghost_body_pos
        zoom 0.24*ghost_sM  xpos 0.082 ypos 0.59 # B08
        p_ao_ghost_transp
    # B07
    contains:
        "p_ao_ghost_comp_05"
        p_ao_ghost_body_pos
        zoom 0.28*ghost_sM  xpos 0.41 ypos 0.62 # B07
        p_ao_ghost_transp
    # B06
    contains:
        "p_ao_ghost_comp_01"
        p_ao_ghost_body_pos
        zoom 0.28*ghost_sM  xpos 0.67 ypos 0.665 # B06
        p_ao_ghost_transp
    # B05
    contains:
        "p_ao_ghost_comp_02"
        p_ao_ghost_body_pos
        zoom 0.3*ghost_sM  xpos 0.885 ypos 0.71 # B05
        p_ao_ghost_transp
    # B04
    contains:
        "p_ao_ghost_comp_03"
        p_ao_ghost_body_pos
        zoom 0.26*ghost_sM xpos 0.225 ypos 0.695 # B04
        p_ao_ghost_transp
    # contains:
    #     "border_darkness_03"
    #     truecenter
    #     zoom 1.0
    #     #p_ao_ghost_transp

    



    

    

    
    




######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##
##

image p_ao_nMouth_tongues = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nMouth_tongues.webp")

image p_ao_nMouth_creepy_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nMouth_creepy_body.webp")
image p_ao_nMouth_creepy_frontHair = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nMouth_creepy_frontHair.webp")
image p_ao_nMouth_creepy_bright = "images/day05/pedrera/afterOrgasm/p_ao_nMouth_creepy_bright.webp"

image p_ao_nMouth_creepy_comp:

    contains:
        "bg_dark_a_blurry_01"
        truecenter
        zoom 5.0

    contains:
        "p_ao_nMouth_creepy_body"
        truecenter

    contains:
        "p_ao_nMouth_creepy_bright"
        truecenter
        additive 1.0

    contains:
        "p_ao_nMouth_creepy_frontHair"
        truecenter




######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##
##

image gensex_oral_n_lick_body = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_lick_body[neyesp].webp")
image gensex_oral_n_lick_iLight = "images/general/sex/oral/neus/gensex_oral_n_lick_iLight.webp"
image gensex_oral_n_lick_l_iris = "images/general/sex/oral/neus/gensex_oral_n_lick_l_iris.webp"
image gensex_oral_n_lick_hairFront = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_lick_hairFront[p_ao_n_horns].webp")
image gensex_oral_n_lick_legs = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_lick_legs.webp")
image gensex_oral_n_lick_rHand_below = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_lick_rHand_below.webp")
image gensex_oral_n_lick_rHand_over = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_lick_rHand_over.webp")
image gensex_oral_n_lick_lHand = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_lick_lHand.webp")


image gensex_oral_n_lick_comp_01:

    contains:
        "bg_ped_04"
        truecenter
        zoom 3.3
        #"gensex_oral_bg_grounddown"
        # truecenter
        # zoom 1.1

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 1.5 ypos 0.3

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 1.5  rotate 180 ypos -1.2

    contains:
        "gensex_oral_bg_grounddownMiddle"
        truecenter
        zoom 1.1

    contains:
        "gensex_oral_mc_body"
        truecenter
        ypos 0.65

    contains:
        "gensex_oral_mc_body_arms"
        truecenter
        ypos 0.65


    contains:
        "gensex_oral_n_lick_legs"
        truecenter

    contains:
        "gensex_oral_n_lick_body"
        truecenter

## MC_Body
    contains:
        "gensex_oral_mc_body_02"
        truecenter
        ypos 0.65

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "lickStomach", At("gensex_oral_n_lick_body", truecenter),
            "True", Null())

    contains:
        "gensex_oral_n_lick_l_iris"
        truecenter
        alpha ped_neus_whispers_sfx04

    contains:
        "gensex_oral_n_lick_iLight"
        truecenter
        alpha ped_neus_whispers_sfx04
        additive 1.0


    

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "lickStomach", At("gensex_oral_n_lick_rHand_below", truecenter),
            "True", At("gensex_oral_n_lick_rHand_over", truecenter))

    # contains:
    #     "gensex_oral_n_lick_rHand_over"
    #     truecenter

    contains:
        "gensex_oral_n_lick_lHand"
        truecenter

    contains:
        "gensex_oral_n_lick_hairFront"
        truecenter

## MC_Chest
        
    contains:
        "gensex_oral_mc_chest"
        truecenter
        ypos 0.65


    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_pos



######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##
##
image p_ao_ground_TEST = "images/day05/pedrera/afterOrgasm/p_ao_ground_TEST.webp"

image p_ao_ground_ground = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_ground_ground.webp")

image p_ao_ground_mc = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_ground_mc[mc_stat].webp")

image p_ao_ground_n_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_ground_n_body.webp")

image p_ao_ground_n_hands_crotch = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_ground_n_hands_crotch.webp")
image p_ao_ground_n_hands_dick_grab_l = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_ground_n_hands_dick_grab_l.webp")
image p_ao_ground_n_hands_dick_grab_r = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_ground_n_hands_dick_grab_r.webp")
image p_ao_ground_n_hands_dick_soft = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_ground_n_hands_dick_soft.webp")
image p_ao_ground_n_hands_foot = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_ground_n_hands_foot.webp")
image p_ao_ground_n_hands_legs_l = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_ground_n_hands_legs_l.webp")
image p_ao_ground_n_hands_legs_r = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_ground_n_hands_legs_r.webp")

image p_ao_ground_n_body_sighing = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_ground_n_body_sighing[neyesp].webp")
image p_ao_ground_n_body_biting = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_ground_n_body_biting[neyesp].webp")

image p_ao_ground_n_hair_front = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_ground_n_hair_front[p_ao_n_horns].webp")
image p_ao_ground_n_glasses = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_ground_n_glasses.webp")


transform p_ao_ground_n_body_pivot:
    xanchor 0.5 yanchor 0.5 xpos 0.46  ypos 0.5

image p_ao_ground_n_body_sighing_comp:
    contains:
        "p_ao_ground_n_body_sighing"
        p_ao_ground_n_body_pivot

    contains:
        ConditionSwitch(
            n_withoutGlasses_story == False and n_withoutGlasses_Cond == False, At("p_ao_ground_n_glasses",p_ao_ground_n_body_pivot),
            "True", Null()
            )

    contains:
        "p_ao_ground_n_hair_front"
        p_ao_ground_n_body_pivot


image p_ao_ground_n_body_biting_comp:
    contains:
        "p_ao_ground_n_body_biting"
        p_ao_ground_n_body_pivot

    contains:
        ConditionSwitch(
            n_withoutGlasses_story == False and n_withoutGlasses_Cond == False, At("p_ao_ground_n_glasses",p_ao_ground_n_body_pivot),
            "True", Null()
            )

    contains:
        "p_ao_ground_n_hair_front"
        p_ao_ground_n_body_pivot

##########################################################################################
##########################################################################################
##########################################################################################
##### TRANSFORMATIONS

transform gensex_stan_mc_04_01_dick_01_pos:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.4 # Dick Position
    xzoom -1.0 zoom 0.5 rotate -90
    xpos 0.43 ypos 0.92
    block:
        ease 10.0 rotate -89
        ease 10.0 rotate -91
        repeat

transform vaporbreathing_new_pos:
    subpixel True
    truecenter
    xpos 0.55 ypos 0.9

transform p_ao_ground_n_sighing_pos:
    subpixel True
    transform_anchor True
    xalign 0.3 yalign 0.4
    xpos 0.62 ypos 0.75 rotate -8 # Down
    block:
        ease_quad 10.0 xpos 0.6 ypos 0.8 rotate -10 # Up
        ease_quad 10.0 xpos 0.62 ypos 0.75 rotate 13 # Down
        repeat

transform p_ao_ground_n_hands_dick_grab_l_pos:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.15
    zoom 0.5
    xpos 0.688 ypos 0.34
    block:
        ease 5.0 ypos 0.4
        ease 5.0 ypos 0.3
        repeat

transform p_ao_ground_n_hands_dick_grab_r_pos:
    subpixel True
    truecenter
    zoom 0.5
    xpos 0.425 ypos 0.673
    block:
        ease 5.0 ypos 0.77
        ease 5.0 ypos 0.673
        repeat

transform p_ao_ground_n_hands_dick_soft_pos:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.15
    zoom 0.5
    xpos 0.688 ypos 0.34
    parallel:
        easein 5.0 rotate 5
        easeout 5.0 rotate -10
        repeat
    parallel:
        easein_quad 3.0 ypos 0.37
        easeout_quad 3.0 ypos 0.32
        repeat

transform p_ao_ground_n_hands_foot_pos:
    subpixel True
    transform_anchor True
    xalign 0.8 yalign 0.35
    zoom 0.5
    xpos 1.99 ypos 0.75 rotate 10
    easein_quad 10.0 xpos 1.835 ypos 0.79 rotate 0
    # block:
    #     ease 5.0 rotate -5
    #     ease 5.0 rotate 0
    #     repeat

transform p_ao_ground_n_hands_legs_r_pos:
    subpixel True
    transform_anchor True
    xalign 0.8 yalign 0.4
    zoom 0.5
    xpos 1.5 ypos 0.9 rotate 10
    easein_quad 10.0 xpos 1.335 ypos 0.915 rotate 0
    # block:
    #     ease 5.0 rotate -5
    #     ease 5.0 rotate 0
    #     repeat


transform p_ao_ground_n_hands_legs_l_pos:
    subpixel True
    transform_anchor True
    xalign 0.9 yalign 0.5
    zoom 0.5
    xpos 1.5 ypos 0.92 rotate 10
    easein_quad 10.0 xpos 1.387 ypos 0.955 rotate 0
    # block:
    #     ease 5.0 rotate -5
    #     ease 5.0 rotate 0
    #     repeat

transform p_ao_ground_n_hands_crotch_pos:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.6
    zoom 0.5
    xpos 0.73 ypos 0.8 rotate 10
    easein_quad 10.0 xpos 0.65 ypos 0.87 rotate 0
    # block:
    #     ease 5.0 rotate -5
    #     ease 5.0 rotate 0
    #     repeat

transform p_ao_ground_pos:
    truecenter
    zoom 3.5

#####
##########################################################################################
##########################################################################################
##########################################################################################


image p_ao_ground_comp:

    contains:
        ConditionSwitch(
            pdaytime == "06morning", At("morning04_bg bedroom_neus_a", p_ao_ground_pos),
            pdaytime == "05_night_Pedrera", At("bg ped_04", p_ao_ground_pos),
            "True", At("bg_dark_a_blurry_01", p_ao_ground_pos))

## Ghosts

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 0.8 xpos -0.35 ypos 0.6 # Left(HeadPart)

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 0.8 xpos 1.3 ypos 0.7 # Right(Legs Part)

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 0.8 xpos 0.5 ypos 0.63 # Center

##

    # contains:
    #     "p_ao_ground_ground"
    #     truecenter
    #     zoom 3.5

    # contains:
    #     "p_ao_ground_TEST"
    #     truecenter
    #     #alpha 0.1

    contains:
        "gensex_stan_mc_04_01_dick_01"
        gensex_stan_mc_04_01_dick_01_pos

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "sigh", 
            At("vaporbreathing_new", vaporbreathing_new_pos),
            "True", Null()
            )

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "sigh", 
            At("p_ao_ground_n_body_sighing_comp", p_ao_ground_n_sighing_pos),
            "True", Null()
            )

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "legs", 
            At("p_ao_ground_n_hands_legs_r", p_ao_ground_n_hands_legs_r_pos),
            "True", Null()
            )

    contains:
        "p_ao_ground_mc"
        truecenter

    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["over", "soft", "grab"], 
            At("p_ao_ground_n_body", truecenter),
            "True", Null()
            )

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "soft", 
            At("p_ao_ground_n_hands_dick_soft", p_ao_ground_n_hands_dick_soft_pos),
            "True", Null()
            )

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "grab", 
            At("p_ao_ground_n_hands_dick_grab_l", p_ao_ground_n_hands_dick_grab_l_pos),
            "True", Null()
            )

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "grab", 
            At("p_ao_ground_n_hands_dick_grab_r", p_ao_ground_n_hands_dick_grab_r_pos),
            "True", Null()
            )

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "foot", 
            At("p_ao_ground_n_hands_foot", p_ao_ground_n_hands_foot_pos),
            "True", Null()
            )

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "legs", 
            At("p_ao_ground_n_hands_legs_l", p_ao_ground_n_hands_legs_l_pos),
            "True", Null()
            )

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "crotch", 
            At("p_ao_ground_n_hands_crotch", p_ao_ground_n_hands_crotch_pos),
            "True", Null()
            )

    contains:
        "p_ao_ground_ground"
        truecenter
        zoom 2.5



######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##
##

image gensex_oral_n_ride_back_01_p01 = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_ride_back_01_p01.webp")

image gensex_oral_n_ride_back_stand = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_ride_back_stand.webp")

image gensex_oral_n_ride_back_01 = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_ride_back_01.webp")
image gensex_oral_n_ride_back_02 = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_ride_back_02.webp")
image gensex_oral_n_ride_back_03 = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_ride_back_03.webp")
image gensex_oral_n_ride_back_04 = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_ride_back_04.webp")
image gensex_oral_n_ride_back_05 = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_ride_back_05.webp")
image gensex_oral_n_ride_back_06 = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_ride_back_06.webp")
image gensex_oral_n_ride_back_07 = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_ride_back_07.webp")

image gensex_oral_n_ride_over_01 = Null(width=800, height=600) 
image gensex_oral_n_ride_over_02 = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_ride_over_02.webp")
image gensex_oral_n_ride_over_03 = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_ride_over_03.webp")
image gensex_oral_n_ride_over_04 = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_ride_over_04.webp")
image gensex_oral_n_ride_over_05 = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_ride_over_05.webp")
image gensex_oral_n_ride_over_06 = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_ride_over_06.webp")
image gensex_oral_n_ride_over_07 = SaturateTint("images/general/sex/oral/neus/gensex_oral_n_ride_over_07.webp")
    

default p_ao_n_vel = 1
default p_ao_dThrob_vel = 1

########################
############

image p_ao_nride_back_01_06_anim:

    truecenter
    "gensex_oral_n_ride_back_02" with Dissolve(1.0/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_back_03" with Dissolve(1.0/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_back_04" with Dissolve(1.0/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_back_05" with Dissolve(1.0/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_back_06" with Dissolve(1.0/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_back_05" with Dissolve(1.0/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_back_04" with Dissolve(1.0/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_back_03" with Dissolve(1.0/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    repeat

image p_ao_nride_over_01_06_anim:

    truecenter
    "gensex_oral_n_ride_over_02" with Dissolve(1.0/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_over_03" with Dissolve(1.0/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_over_04" with Dissolve(1.0/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_over_05" with Dissolve(1.0/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_over_06" with Dissolve(1.0/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_over_05" with Dissolve(1.0/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_over_04" with Dissolve(1.0/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_over_03" with Dissolve(1.0/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    repeat

########################
############

image p_ao_nride_back_01_07_anim:

    truecenter
    "gensex_oral_n_ride_back_02" with Dissolve(0.5/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    "gensex_oral_n_ride_back_03" with Dissolve(0.5/p_ao_n_vel)
    pause 0.75/p_ao_n_vel
    "gensex_oral_n_ride_back_04" with Dissolve(0.5/p_ao_n_vel)
    pause 1.0/p_ao_n_vel
    "gensex_oral_n_ride_back_05" with Dissolve(0.5/p_ao_n_vel)
    pause 1.25/p_ao_n_vel
    "gensex_oral_n_ride_back_06" with Dissolve(0.5/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_back_07" with Dissolve(0.5/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_back_06" with Dissolve(0.5/p_ao_n_vel)
    pause 1.25/p_ao_n_vel
    "gensex_oral_n_ride_back_05" with Dissolve(0.5/p_ao_n_vel)
    pause 1.0/p_ao_n_vel
    "gensex_oral_n_ride_back_04" with Dissolve(0.5/p_ao_n_vel)
    pause 0.75/p_ao_n_vel
    "gensex_oral_n_ride_back_03" with Dissolve(0.5/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    repeat

image p_ao_nride_over_01_07_anim:

    truecenter
    "gensex_oral_n_ride_over_02" with Dissolve(0.5/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    "gensex_oral_n_ride_over_03" with Dissolve(0.5/p_ao_n_vel)
    pause 0.75/p_ao_n_vel
    "gensex_oral_n_ride_over_04" with Dissolve(0.5/p_ao_n_vel)
    pause 1.0/p_ao_n_vel
    "gensex_oral_n_ride_over_05" with Dissolve(0.5/p_ao_n_vel)
    pause 1.25/p_ao_n_vel
    "gensex_oral_n_ride_over_06" with Dissolve(0.5/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_over_07" with Dissolve(0.5/p_ao_n_vel)
    pause 1.5/p_ao_n_vel
    "gensex_oral_n_ride_over_06" with Dissolve(0.5/p_ao_n_vel)
    pause 1.25/p_ao_n_vel
    "gensex_oral_n_ride_over_05" with Dissolve(0.5/p_ao_n_vel)
    pause 1.0/p_ao_n_vel
    "gensex_oral_n_ride_over_04" with Dissolve(0.5/p_ao_n_vel)
    pause 0.75/p_ao_n_vel
    "gensex_oral_n_ride_over_03" with Dissolve(0.5/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    repeat

########################
############

transform p_ao_nride01_move_pos:
    subpixel True
    truecenter
    block:
        easeout_quad 5/p_ao_n_vel ypos 0.55
        easein_quad 5/p_ao_n_vel ypos 0.5
        repeat

transform p_ao_smoke_appearing:
    subpixel True
    truecenter
    ypos 1.7 # Hide?
    easein_quad 100 ypos 1.0
    # easein_quad 50.0 ypos 0.5 # Full

transform p_ao_smoke_default:
    subpixel True
    truecenter
    ypos 1.2 # Hide?
    easein_quad 100 ypos 1.0
    # easein_quad 50.0 ypos 0.5 # Full


transform p_ao_nride_smoke_pos:
    subpixel True
    truecenter
    zoom 3.0
    alpha 0.75
    ypos 1.4
    easein_quad 100 ypos 1.0

transform p_ao_nride_smoke_BIGpos:
    subpixel True
    truecenter
    zoom 4.0
    alpha 0.75
    ypos 1.4
    easein_quad 100 ypos 1.0

# transform p_ao_nride_smokeB_pos:
#     truecenter
#     zoom 3.0
#     alpha 0.75
#     ypos 1.4
#     easein_quad 100 ypos 1.0

########################
############


image p_ao_ride_comp 01:

    contains:
        "bg_ped_04"
        truecenter
        zoom 3.3
        #"gensex_oral_bg_grounddown"
        # truecenter
        # zoom 1.1

    contains:
        "p_ao_ghost_standing_comp"
        truecenter

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        ypos -0.54 rotate 180



# NEUS RIDE BACK
    
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "nride01_p01", At("gensex_oral_n_ride_back_01_p01", truecenter),

            p_ao_action_Cond == "nride01_move", At("gensex_oral_n_ride_back_01", p_ao_nride01_move_pos),

            p_ao_action_Cond == "nride01", At("gensex_oral_n_ride_back_01", truecenter),
            p_ao_action_Cond == "nride02", At("gensex_oral_n_ride_back_02", truecenter),
            p_ao_action_Cond == "nride03", At("gensex_oral_n_ride_back_03", truecenter),
            p_ao_action_Cond == "nride04", At("gensex_oral_n_ride_back_04", truecenter),
            p_ao_action_Cond == "nride05", At("gensex_oral_n_ride_back_05", truecenter),
            p_ao_action_Cond == "nride06", At("gensex_oral_n_ride_back_06", truecenter),
            p_ao_action_Cond == "nride07", At("gensex_oral_n_ride_back_07", truecenter),

            p_ao_action_Cond == "nride06_anim", At("p_ao_nride_back_01_06_anim", truecenter),

            p_ao_action_Cond == "nride07_anim", At("p_ao_nride_back_01_07_anim", truecenter),

            "True", Null()
            )
    # contains:
    #     "gensex_oral_n_ride_back_02"
    #     truecenter

## MC DICK

    contains:
        "gensex_oral_mc_dick_01_wet_00"
        ped05_sex_oral_d_dick_o00_00

## NEUS RIDE OVER
    
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "nride02", At("gensex_oral_n_ride_over_02", truecenter),
            p_ao_action_Cond == "nride03", At("gensex_oral_n_ride_over_03", truecenter),
            p_ao_action_Cond == "nride04", At("gensex_oral_n_ride_over_04", truecenter),
            p_ao_action_Cond == "nride05", At("gensex_oral_n_ride_over_05", truecenter),
            p_ao_action_Cond == "nride06", At("gensex_oral_n_ride_over_06", truecenter),
            p_ao_action_Cond == "nride07", At("gensex_oral_n_ride_over_07", truecenter),

            p_ao_action_Cond == "nride06_anim", At("p_ao_nride_over_01_06_anim", truecenter),

            p_ao_action_Cond == "nride07_anim", At("p_ao_nride_over_01_07_anim", truecenter),

            "True", Null()
            )

    # contains:
    #     "gensex_oral_n_ride_over_02"
    #     truecenter
    ##

    contains:
        "gensex_oral_mc_body"
        truecenter
        ypos 0.65

## MC_Chest
        
    contains:
        "gensex_oral_mc_chest"
        truecenter
        ypos 0.65

# Smoke
    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_pos




######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##
##

# NEUS BACK RIDING

image p_ao_gensex_briding_comp PROVE:

    # contains:
    #     "gensex_briding_PROVE02"
    #     truecenter
    
    contains:
        "bg_ped_04"
        truecenter
        zoom 3.5
        #"gensex_oral_bg_grounddown"
        # truecenter
        # zoom 1.1

    contains:
        "gensex_briding_MC_body"
        gensex_briding_D_center_pos

    contains:
        "gensex_briding_N_body"
        gensex_briding_D_center_pos

    contains:
        "gensex_briding_MC_crotch"
        gensex_briding_D_center_pos

    contains:
        "gensex_briding_N_legs_over_vaginal"
        gensex_briding_D_center_pos

    # contains:
    #     "gensex_briding_D_legs_below_normal"
    #     gensex_briding_D_center_pos

    # contains:
    #     "gensex_briding_D_legs_ass_vaginal"
    #     gensex_briding_D_center_pos

    # contains:
    #     "gensex_briding_D_legs_forVaginal_fixed"
    #     gensex_briding_D_center_pos

    contains:
        "gensex_briding_MC_dick_in_naked"
        gensex_briding_D_center_pos

## MC LEGS
    contains:
        ConditionSwitch(
            p_ao_mc_legs == "stand", At("gensex_briding_MC_legs_down", gensex_briding_D_center_pos),
            "True", At("gensex_briding_MC_legs", gensex_briding_D_center_pos))

    # contains:
    #     "gensex_briding_D_open_vaginal"
    #     truecenter # Default position

    # contains:
    #     "gensex_briding_D_open_anal"
    #     truecenter
    #     ypos 0.35 #Default position
    
    contains:
        "gensex_briding_PROVE02"
        truecenter
        alpha 0.5



######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##
##


image gensex_stan02_REFERENCE = "images/general/sex/standing/gensex_stan02_REFERENCE.webp"

image gensex_stan02_mc_arm = SaturateTint("images/general/sex/standing/gensex_stan02_mc_arm.webp")
image gensex_stan02_mc_body = SaturateTint("images/general/sex/standing/gensex_stan02_mc_body.webp")
image gensex_stan02_mc_legs = SaturateTint("images/general/sex/standing/gensex_stan02_mc_legs.webp")

image gensex_stan02_n_b_back_body = SaturateTint("images/general/sex/standing/gensex_stan02_n_b_back_body[neyesp].webp")
image gensex_stan02_n_b_back_hairFront = SaturateTint("images/general/sex/standing/gensex_stan02_n_b_back_hairFront[p_ao_n_horns].webp")
image gensex_stan02_n_b_back_iLight = "images/general/sex/standing/gensex_stan02_n_b_back_iLight.webp"
image gensex_stan02_n_b_back_l_iris = "images/general/sex/standing/gensex_stan02_n_b_back_l_iris.webp"
image gensex_stan02_n_b_back_hair = SaturateTint("images/general/sex/standing/gensex_stan02_n_b_back_hair.webp")

image gensex_stan02_n_s_back_body = SaturateTint("images/general/sex/standing/gensex_stan02_n_s_back_body[neyesp].webp")
image gensex_stan02_n_s_back_hairFront = SaturateTint("images/general/sex/standing/gensex_stan02_n_s_back_hairFront.webp") #Horns not necessary.
image gensex_stan02_n_s_back_iLight = "images/general/sex/standing/gensex_stan02_n_s_back_iLight.webp"
image gensex_stan02_n_s_back_l_iris = "images/general/sex/standing/gensex_stan02_n_s_back_l_iris.webp"
image gensex_stan02_n_s_back_hair = SaturateTint("images/general/sex/standing/gensex_stan02_n_s_back_hair.webp")

image gensex_stan02_n_s_front_body = SaturateTint("images/general/sex/standing/gensex_stan02_n_s_front_body.webp")

image gensex_stan02_n_s_front_arm_ass = SaturateTint("images/general/sex/standing/gensex_stan02_n_s_front_arm_ass.webp")
image gensex_stan02_n_s_front_arm_neck = SaturateTint("images/general/sex/standing/gensex_stan02_n_s_front_arm_neck.webp")

image gensex_stan02_n_s_ride_REFERENCE = SaturateTint("images/general/sex/standing/gensex_stan02_n_s_ride_REFERENCE.webp")

image gensex_stan02_n_s_ride_01 = SaturateTint("images/general/sex/standing/gensex_stan02_n_s_ride_01.webp")
image gensex_stan02_n_s_ride_02 = SaturateTint("images/general/sex/standing/gensex_stan02_n_s_ride_02.webp")
image gensex_stan02_n_s_ride_03 = SaturateTint("images/general/sex/standing/gensex_stan02_n_s_ride_03.webp")
image gensex_stan02_n_s_ride_04 = SaturateTint("images/general/sex/standing/gensex_stan02_n_s_ride_04.webp")
image gensex_stan02_n_s_ride_05 = SaturateTint("images/general/sex/standing/gensex_stan02_n_s_ride_05.webp")
image gensex_stan02_n_s_ride_06 = SaturateTint("images/general/sex/standing/gensex_stan02_n_s_ride_06.webp")

image gensex_stan02_n_tongueNeck = SaturateTint("images/general/sex/standing/gensex_stan02_n_tongueNeck.webp")


image gensex_stan02_ground = Solid("#000", xysize=(5333, 620))
image gensex_stan02_wall = Solid("#000", xysize=(1000, 5333))

######################################################################################################
######################################################################################################
##
## DICK

transform p_ao_wall_dick_soft:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.4 # Dick Position
    xpos 1.27 ypos 0.49 
    #zoom 0.28 rotate 0 # Erected.
    #xzoom 0.2 yzoom 0.26 rotate -20 # SemiSoft
    xzoom 0.1 yzoom 0.15 rotate -45 # Soft
    #zoom 0.29

transform p_ao_wall_dick_soft_moving:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.4 # Dick Position
    xpos 1.27 ypos 0.49 
    xzoom 0.1 yzoom 0.15 rotate -45 # Soft
    block:
        ease 3.8 rotate -40
        ease 3.5 rotate -45
        repeat

transform p_ao_wall_dick_hard:
    transform_anchor True
    xalign 0.85 yalign 0.4 # Dick Position
    xpos 1.27 ypos 0.49
    zoom 0.28 rotate 0 # Erected.

transform p_ao_wall_dick_hard_stomach:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.4 # Dick Position
    xpos 1.27 ypos 0.49
    zoom 0.28 rotate 75 # Erected.

transform p_ao_wall_dick_hard_ride:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.4 # Dick Position
    xpos 1.27 ypos 0.49
    zoom 0.28 rotate 35 # Prepared to Penetrate Riding Neus.

transform p_ao_wall_dick_semiSoft:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.4 # Dick Position
    xpos 1.27 ypos 0.49
    #zoom 0.28 rotate 0 # Erected.
    xzoom 0.18 yzoom 0.2 #rotate -45 # Semi-Hars
    rotate -10 # Puntillas

transform p_ao_wall_dick_s_soft_rubbing:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.4 # Dick Position
    xpos 1.27 ypos 0.49
    #zoom 0.28 rotate 0 # Erected.
    xzoom 0.18 yzoom 0.2 #rotate -45 # Semi-Hars
    rotate 70 # When it's Semi ### When it's little: 12 # Puntillas
    block:
        pause 0.6/p_ao_n_vel
        ease 2.5/p_ao_n_vel rotate 40 # When it's semiSoft ### When it's little: -45 # No Puntillas
        pause 4.0/p_ao_n_vel
        ease 2.5/p_ao_n_vel rotate 70 # When it's semiSoft ### When it's little: 12 # Puntillas
        pause 0.4/p_ao_n_vel
        repeat

transform p_ao_wall_dick_b_semiSoft_rubbing:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.4 # Dick Position
    xpos 1.27 ypos 0.49
    #zoom 0.28 rotate 0 # Erected.
    xzoom 0.18 yzoom 0.2 #rotate -45 # Semi-Hars
    rotate 60 # When it's Semi ### When it's little: 12 # Puntillas
    block:
        pause 0.6/p_ao_n_vel
        ease 2.5/p_ao_n_vel rotate 70
        pause 4.0/p_ao_n_vel
        ease 2.5/p_ao_n_vel rotate 60
        pause 0.4/p_ao_n_vel
        repeat

transform p_ao_wall_dick_b_hard_rubbing:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.4 # Dick Position
    xpos 1.27 ypos 0.49
    #zoom 0.28 rotate 0 # Erected.
    zoom 0.28 rotate 75 # Erected.
    rotate 65 # When it's Semi ### When it's little: 12 # Puntillas
    block:
        pause 0.6/p_ao_n_vel
        ease 2.5/p_ao_n_vel rotate 72
        pause 4.0/p_ao_n_vel
        ease 2.5/p_ao_n_vel rotate 65
        pause 0.4/p_ao_n_vel
        repeat

transform p_ao_wall_dick_b_analSex:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.4 # Dick Position
    xpos 1.27 ypos 0.49
    zoom 0.28 #rotate 75 # Erected.
    rotate 15 # Anal Tip
    block:
        ease 6.0/p_ao_n_vel rotate 25 # Anal Deep
        ease 6.0/p_ao_n_vel rotate 15 # Anal Tip
        repeat

##
## MC Body

transform p_ao_wall_mc_body_static:
    truecenter
    zoom 0.4 xpos 1.28

## Neus Body

transform p_ao_wall_n_s_front_still:
    truecenter
    zoom 0.4 xpos 1.122

transform p_ao_wall_n_s_front_l_iris_still:
    truecenter
    alpha ped_neus_whispers_sfx04
    zoom 0.4 xpos 1.122

transform p_ao_wall_n_s_front_iLight_still:
    truecenter
    additive 1.0
    alpha ped_neus_whispers_sfx04
    zoom 0.4 xpos 1.122

transform p_ao_wall_n_s_back_rubbing:
    subpixel True
    truecenter
    zoom 0.4 #xpos 1.122
    #xpos 1.122 ypos 0.5 # Default
    xpos 1.14 ypos 0.5 # Puntillas
    block:
        ease 5.0/p_ao_n_vel xpos 1.14 ypos 0.61 # No Puntillas
        ease 5.0/p_ao_n_vel xpos 1.14 ypos 0.5 # Puntillas
        repeat

transform p_ao_wall_n_s_back_l_iris_rubbing:
    subpixel True
    truecenter
    alpha ped_neus_whispers_sfx04
    zoom 0.4 #xpos 1.122
    xpos 1.14 ypos 0.5 # Puntillas
    block:
        ease 5.0/p_ao_n_vel xpos 1.14 ypos 0.61 # No Puntillas
        ease 5.0/p_ao_n_vel xpos 1.14 ypos 0.5 # Puntillas
        repeat

transform p_ao_wall_n_s_back_iLight_rubbing:
    subpixel True
    truecenter
    additive 1.0
    alpha ped_neus_whispers_sfx04
    zoom 0.4 #xpos 1.122
    xpos 1.14 ypos 0.5 # Puntillas
    block:
        ease 5.0/p_ao_n_vel xpos 1.14 ypos 0.61 # No Puntillas
        ease 5.0/p_ao_n_vel xpos 1.14 ypos 0.5 # Puntillas
        repeat

transform p_ao_wall_n_b_back_rubbing:
    subpixel True
    truecenter
    zoom 0.4 #xpos 1.122
    #xpos 1.122 ypos 0.5 # Default
    xpos 1.14 ypos 0.5 # Cuclillas
    block:
        ease 5.0/p_ao_n_vel xpos 1.14 ypos 0.4 # Up
        ease 5.0/p_ao_n_vel xpos 1.14 ypos 0.5 # Cuclillas
        repeat

transform p_ao_wall_n_b_back_l_iris_rubbing:
    subpixel True
    truecenter
    zoom 0.4 #xpos 1.122
    alpha ped_neus_whispers_sfx04
    xpos 1.14 ypos 0.5 # Cuclillas
    block:
        ease 5.0/p_ao_n_vel xpos 1.14 ypos 0.4 # Up
        ease 5.0/p_ao_n_vel xpos 1.14 ypos 0.5 # Cuclillas
        repeat

transform p_ao_wall_n_b_back_iLight_rubbing:
    subpixel True
    truecenter
    additive 1.0
    alpha ped_neus_whispers_sfx04
    zoom 0.4 #xpos 1.122
    xpos 1.14 ypos 0.5 # Cuclillas
    block:
        ease 5.0/p_ao_n_vel xpos 1.14 ypos 0.4 # Up
        ease 5.0/p_ao_n_vel xpos 1.14 ypos 0.5 # Cuclillas
        repeat

transform p_ao_wall_n_b_back_analSex:
    subpixel True
    truecenter
    zoom 0.4 #xpos 1.122
    xpos 0.96 ypos 0.42 # Anal Tip
    block:
        ease 6.0/p_ao_n_vel xpos 1.14 ypos 0.5 # Anal Deep
        ease 6.0/p_ao_n_vel xpos 0.96 ypos 0.42 # Anal Tip
        repeat

transform p_ao_wall_n_b_back_l_iris_analSex:
    subpixel True
    truecenter
    alpha ped_neus_whispers_sfx04
    zoom 0.4 #xpos 1.122
    xpos 0.96 ypos 0.42 # Anal Tip
    block:
        ease 6.0/p_ao_n_vel xpos 1.14 ypos 0.5 # Anal Deep
        ease 6.0/p_ao_n_vel xpos 0.96 ypos 0.42 # Anal Tip
        repeat

transform p_ao_wall_n_b_back_iLight_analSex:
    subpixel True
    truecenter
    additive 1.0
    alpha ped_neus_whispers_sfx04
    zoom 0.4 #xpos 1.122
    xpos 0.96 ypos 0.42 # Anal Tip
    block:
        ease 6.0/p_ao_n_vel xpos 1.14 ypos 0.5 # Anal Deep
        ease 6.0/p_ao_n_vel xpos 0.96 ypos 0.42 # Anal Tip
        repeat

# neusRide_01_04
image p_ao_wall_n_s_ride_01_04:
    truecenter

    "gensex_stan02_n_s_ride_01" with Dissolve(0.4/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    "gensex_stan02_n_s_ride_02" with Dissolve(0.4/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    "gensex_stan02_n_s_ride_03" with Dissolve(0.4/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    "gensex_stan02_n_s_ride_04" with Dissolve(0.4/p_ao_n_vel)
    pause 1.0/p_ao_n_vel
    "gensex_stan02_n_s_ride_03" with Dissolve(0.4/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    "gensex_stan02_n_s_ride_02" with Dissolve(0.4/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    repeat


# neusRide_01_06
image p_ao_wall_n_s_ride_01_06:
    truecenter

    "gensex_stan02_n_s_ride_01" with Dissolve(0.4/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    "gensex_stan02_n_s_ride_02" with Dissolve(0.4/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    "gensex_stan02_n_s_ride_03" with Dissolve(0.4/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    "gensex_stan02_n_s_ride_04" with Dissolve(0.4/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    "gensex_stan02_n_s_ride_05" with Dissolve(0.4/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    "gensex_stan02_n_s_ride_06" with Dissolve(0.4/p_ao_n_vel)
    pause 1.0/p_ao_n_vel
    "gensex_stan02_n_s_ride_05" with Dissolve(0.4/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    "gensex_stan02_n_s_ride_04" with Dissolve(0.4/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    "gensex_stan02_n_s_ride_03" with Dissolve(0.4/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    "gensex_stan02_n_s_ride_02" with Dissolve(0.4/p_ao_n_vel)
    pause 0.5/p_ao_n_vel
    repeat

transform p_ao_wall_n_s_front_moving:
    subpixel True
    truecenter
    zoom 0.4 xpos 1.122
    parallel:
        ease 4.0 ypos 0.54
        ease 4.0 ypos 0.5
        repeat
    parallel:
        ease 3.8 xpos 1.121
        ease 3.2 xpos 1.123
        repeat
    parallel:
        ease 3.8 rotate -0.5
        ease 3.4 rotate 1
        repeat
## Soft Hand
# ["neusFront_still", "neusFront_abs", "neusFront_pec", "neusFront_neck"]
transform p_ao_wall_n_s_handSoft_abs:
    subpixel True

    "p_ao_ground_n_hands_dick_soft"
    transform_anchor True
    xalign 0.85 yalign 0.15
    xzoom -1.0 zoom 0.3
    
    xpos 1.18 ypos 0.35 rotate -15 # Pelvis
    ease 5 xpos 1.1 ypos 0.35 rotate -50 # Stomach

transform p_ao_wall_n_s_handSoft_pec:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.15
    xzoom -1.0 zoom 0.3
    
    xpos 1.1 ypos 0.35 rotate -50 # Stomach
    ease 5 xpos 1.12 ypos 0.25 rotate -90 # Pectoral

transform p_ao_wall_n_s_handSoft_neck:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.15
    xzoom -1.0 zoom 0.3

    xpos 1.12 ypos 0.25 rotate -90 # Pectoral
    ease 5 xpos 1.18 ypos 0.15 rotate -100 # Neck

##
## Neus Sighing

transform p_ao_wall_sig_breathing:
    truecenter
    xpos 1.22 ypos 0.6

transform p_ao_wall_sig_body:
    subpixel True
    transform_anchor True
    xalign 0.3 yalign 0.4
    xzoom -1.0
    zoom 0.63
    xpos 1.15 ypos 0.63 rotate -30 # Down
    parallel:
        ease 4.4 ypos 0.6
        ease 5.5 ypos 0.65
        repeat
    parallel:
        ease 6.2 rotate -20
        ease 5.3 rotate -32
        repeat
    parallel:
        ease 5.8 xpos 1.175
        ease 4.2 xpos 1.16
        repeat

transform p_ao_wall_sig_handballs:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.15
    xzoom -1.0
    zoom 0.36
    xpos 1.2 ypos 0.9 rotate -120
    parallel:
        ease 3.8 ypos 0.85
        ease 3.5 ypos 0.9
        repeat
    parallel:
        ease 3.2 rotate -118
        ease 3.1 rotate -120
        repeat


transform p_ao_wall_sig_handass:
    subpixel True
    transform_anchor True
    xalign 0.9 yalign 0.5
    #xzoom -1.0
    zoom 0.36
    xpos 1.28 ypos 0.83 rotate 115
    parallel:
        ease 3.2 rotate 119
        ease 3.8 rotate 115
        repeat
    parallel:
        ease 2.5 ypos 0.78
        ease 2.6 ypos 0.82
        repeat

######################################################################################################
######################################################################################################
##
##

image gensex_stan02_comp_01:

    contains:
        "bg_dark_a_blurry_02"
        truecenter
        zoom 3.5

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 0.7 ypos 0.7

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 0.7 ypos -0.3 rotate 180

# Neus Hand Ass
    
    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["neusBallsAss"], At("p_ao_ground_n_hands_legs_l", p_ao_wall_sig_handass),
            "True", Null())

# Neus Vapor

    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["neusBalls", "neusBallsAss"], At("vaporbreathing_new", p_ao_wall_sig_breathing),
            "True", Null())

# Neus Sighing
    
    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["neusBalls", "neusBallsAss"],  At("p_ao_ground_n_body_sighing_comp", p_ao_wall_sig_body),
            "True", Null())

# Neus Back(Behind) HAIR
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "neusSback", At("gensex_stan02_n_s_back_hair", p_ao_wall_n_s_front_still),
            p_ao_action_Cond == "neusSback_rubbing", At("gensex_stan02_n_s_back_hair", p_ao_wall_n_s_back_rubbing),

            p_ao_action_Cond == "neusBback", At("gensex_stan02_n_b_back_hair", p_ao_wall_n_s_front_still),
            p_ao_action_Cond in ["neusBback_rubbing", "neusBback_rubbing_hard"], At("gensex_stan02_n_b_back_hair", p_ao_wall_n_b_back_rubbing),

            p_ao_action_Cond in ["neusBback_analSex"], At("gensex_stan02_n_b_back_hair", p_ao_wall_n_b_back_analSex),

            "True", Null())

##
# DICK

    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["alone_hard"], At("gensex_stan_mc_04_01_dick 01", p_ao_wall_dick_hard),
            p_ao_action_Cond in ["neusSback", "alone_semi_soft"], At("gensex_stan_mc_04_01_dick 01", p_ao_wall_dick_semiSoft),


            p_ao_action_Cond in ["neusBalls", "neusBallsAss"], At("gensex_stan_mc_04_01_dick 01", p_ao_wall_dick_soft_moving),
            p_ao_action_Cond in ["neusFront_still", "neusFront_moving"], At("gensex_stan_mc_04_01_dick 01", p_ao_wall_dick_hard_stomach),

            p_ao_action_Cond in ["neusRide_01", "neusRide_02", "neusRide_03", "neusRide_04", "neusRide_05", "neusRide_06", "neusRide_01_04", "neusRide_01_06"], 
                At("gensex_stan_mc_04_01_dick 01", p_ao_wall_dick_hard_ride),

            p_ao_action_Cond in ["neusSback_rubbing"], At("gensex_stan_mc_04_01_dick 01", p_ao_wall_dick_s_soft_rubbing),
            p_ao_action_Cond in ["neusBback_rubbing"], At("gensex_stan_mc_04_01_dick 01", p_ao_wall_dick_b_semiSoft_rubbing),
            p_ao_action_Cond in ["neusBback_rubbing_hard"], At("gensex_stan_mc_04_01_dick 01", p_ao_wall_dick_b_hard_rubbing),

            p_ao_action_Cond in ["neusBback_analSex"], At("gensex_stan_mc_04_01_dick 01", p_ao_wall_dick_b_analSex),


            "True", At("gensex_stan_mc_04_01_dick 01", p_ao_wall_dick_soft))

##
# Neus Hand Balls
    
    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["neusBalls", "neusBallsAss"],  At("p_ao_ground_n_hands_dick_soft", p_ao_wall_sig_handballs),
            "True", Null())


###

    
    # MC BODY
    contains:
        ConditionSwitch(
            #p_ao_action_Cond == "aloneSoft", At("gensex_stan02_mc_body", p_ao_wall_mc_body_static),
            "True", At("gensex_stan02_mc_body", p_ao_wall_mc_body_static))

## Neus Tongue
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "neusTongueNeck", At("gensex_stan02_n_tongueNeck", p_ao_wall_mc_body_static),
            "True", Null())


    # MC LEGS
    contains:
        ConditionSwitch(
            #p_ao_action_Cond == "aloneSoft", At("gensex_stan02_mc_body", p_ao_wall_mc_body_static),
            "True", At("gensex_stan02_mc_legs", p_ao_wall_mc_body_static))


    # MC ARM
    contains:
        ConditionSwitch(
            #p_ao_action_Cond == "aloneSoft", At("gensex_stan02_mc_arm", p_ao_wall_mc_body_static),
            "True", At("gensex_stan02_mc_arm", p_ao_wall_mc_body_static))


##
## NEUS



# Neus (Over)
    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["neusFront_still", "neusFront_abs", "neusFront_pec", "neusFront_neck", "neusFront_neckGrab"], 
                At("gensex_stan02_n_s_front_body", p_ao_wall_n_s_front_still),

            p_ao_action_Cond == "neusFront_moving", At("gensex_stan02_n_s_front_body", p_ao_wall_n_s_front_moving),

            p_ao_action_Cond == "neusSback", At("gensex_stan02_n_s_back_body", p_ao_wall_n_s_front_still),
            p_ao_action_Cond == "neusSback_rubbing", At("gensex_stan02_n_s_back_body", p_ao_wall_n_s_back_rubbing),

            p_ao_action_Cond == "neusBback", At("gensex_stan02_n_b_back_body", p_ao_wall_n_s_front_still),
            p_ao_action_Cond in ["neusBback_rubbing", "neusBback_rubbing_hard"], At("gensex_stan02_n_b_back_body", p_ao_wall_n_b_back_rubbing),

            p_ao_action_Cond in ["neusBback_analSex"], At("gensex_stan02_n_b_back_body", p_ao_wall_n_b_back_analSex),

            "True", Null())

# EXTRAS over
# l_iris
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "neusSback", At("gensex_stan02_n_s_back_l_iris", p_ao_wall_n_s_front_l_iris_still),
            p_ao_action_Cond == "neusSback_rubbing", At("gensex_stan02_n_s_back_l_iris", p_ao_wall_n_s_back_l_iris_rubbing),

            p_ao_action_Cond == "neusBback", At("gensex_stan02_n_b_back_l_iris", p_ao_wall_n_s_front_l_iris_still),
            p_ao_action_Cond in ["neusBback_rubbing", "neusBback_rubbing_hard"], At("gensex_stan02_n_b_back_l_iris", p_ao_wall_n_b_back_l_iris_rubbing),

            p_ao_action_Cond in ["neusBback_analSex"], At("gensex_stan02_n_b_back_l_iris", p_ao_wall_n_b_back_l_iris_analSex),
            "True", Null())

# iLight
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "neusSback", At("gensex_stan02_n_s_back_iLight", p_ao_wall_n_s_front_iLight_still),
            p_ao_action_Cond == "neusSback_rubbing", At("gensex_stan02_n_s_back_iLight", p_ao_wall_n_s_back_iLight_rubbing),

            p_ao_action_Cond == "neusBback", At("gensex_stan02_n_b_back_iLight", p_ao_wall_n_s_front_iLight_still),
            p_ao_action_Cond in ["neusBback_rubbing", "neusBback_rubbing_hard"], At("gensex_stan02_n_b_back_iLight", p_ao_wall_n_b_back_iLight_rubbing),

            p_ao_action_Cond in ["neusBback_analSex"], At("gensex_stan02_n_b_back_iLight", p_ao_wall_n_b_back_iLight_analSex),
            "True", Null())

# HairFront
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "neusSback", At("gensex_stan02_n_s_back_hairFront", p_ao_wall_n_s_front_still),
            p_ao_action_Cond == "neusSback_rubbing", At("gensex_stan02_n_s_back_hairFront", p_ao_wall_n_s_back_rubbing),

            p_ao_action_Cond == "neusBback", At("gensex_stan02_n_b_back_hairFront", p_ao_wall_n_s_front_still),
            p_ao_action_Cond in ["neusBback_rubbing", "neusBback_rubbing_hard"], At("gensex_stan02_n_b_back_hairFront", p_ao_wall_n_b_back_rubbing),

            p_ao_action_Cond in ["neusBback_analSex"], At("gensex_stan02_n_b_back_hairFront", p_ao_wall_n_b_back_analSex),
            "True", Null())


# Neus Arms
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "neusFront_still", At("gensex_stan02_n_s_front_arm_ass", p_ao_wall_n_s_front_still),
            p_ao_action_Cond == "neusFront_moving", At("gensex_stan02_n_s_front_arm_ass", p_ao_wall_n_s_front_moving),

            p_ao_action_Cond == "neusFront_abs", At("p_ao_ground_n_hands_dick_soft", p_ao_wall_n_s_handSoft_abs),
            p_ao_action_Cond == "neusFront_pec", At("p_ao_ground_n_hands_dick_soft", p_ao_wall_n_s_handSoft_pec),
            p_ao_action_Cond == "neusFront_neck", At("p_ao_ground_n_hands_dick_soft", p_ao_wall_n_s_handSoft_neck),

            p_ao_action_Cond == "neusFront_neckGrab", At("gensex_stan02_n_s_front_arm_neck", p_ao_wall_n_s_front_still),

            "True", Null())


## NeusRiding

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "neusRide_01", At("gensex_stan02_n_s_ride_01", p_ao_wall_n_s_front_still),
            p_ao_action_Cond == "neusRide_02", At("gensex_stan02_n_s_ride_02", p_ao_wall_n_s_front_still),
            p_ao_action_Cond == "neusRide_03", At("gensex_stan02_n_s_ride_03", p_ao_wall_n_s_front_still),
            p_ao_action_Cond == "neusRide_04", At("gensex_stan02_n_s_ride_04", p_ao_wall_n_s_front_still),
            p_ao_action_Cond == "neusRide_05", At("gensex_stan02_n_s_ride_05", p_ao_wall_n_s_front_still),
            p_ao_action_Cond == "neusRide_06", At("gensex_stan02_n_s_ride_06", p_ao_wall_n_s_front_still),

            p_ao_action_Cond == "neusRide_01_04", At("p_ao_wall_n_s_ride_01_04", p_ao_wall_n_s_front_still),
            p_ao_action_Cond == "neusRide_01_06", At("p_ao_wall_n_s_ride_01_06", p_ao_wall_n_s_front_still),

            p_ao_action_Cond == "neusTongueNeck", At("p_ao_wall_n_s_ride_01_06", p_ao_wall_n_s_front_still),

            "True", Null())

##

###

    contains: # GROUND
        "gensex_stan02_ground"
        transform_anchor True
        xalign 0.5 yalign 0.0 # Don't touch.
        zoom 0.5 
        ypos 1.425

    contains: # WALL
        "gensex_stan02_wall"
        transform_anchor True
        xalign 0.0 yalign 0.5 # Don't touch.
        zoom 0.5
        xpos 1.382

    # contains:
        #     "gensex_stan02_REFERENCE"
        #     truecenter

    # contains:
    #     "gensex_stan02_n_s_ride_REFERENCE"
    #     truecenter
    #     alpha 0.5
    #     zoom 0.4 xpos 1.122
    
# Smoke
    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_pos



######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##
##


transform p_ao_dick_hardThrobbing:
    subpixel True
    truecenter
    ypos 0.8
    parallel:
        ease 1.25/p_ao_dThrob_vel rotate 0.1
        ease 1.5/p_ao_dThrob_vel rotate -0.1
        repeat
    parallel:
        ease 1.25/p_ao_dThrob_vel xzoom 1.01
        ease 1.75/p_ao_dThrob_vel xzoom 0.99
        repeat
    parallel:
        ease 1.75/p_ao_dThrob_vel yzoom 0.99
        ease 1.25/p_ao_dThrob_vel yzoom 1.01
        repeat

transform p_ao_dick_semiHard:
    truecenter
    ypos 0.8
    block:
        xzoom 0.8 yzoom 0.6

## TEASING
transform p_ao_back_analTeasing:
    subpixel True
    # "gensex_oral_n_back_d_b_anal_over"
    transform_anchor True
    xalign 0.5 yalign 0.71 # ANAL BACK Pivot CORRECT
    xpos 0.5 ypos -0.1
    block:
        ease 2.0/p_ao_n_vel ypos -0.08
        ease 2.0/p_ao_n_vel ypos -0.11
        repeat

transform p_ao_back_vaginalTeasing:
    subpixel True
    # "gensex_oral_n_back_d_b_vaginal_over"
    transform_anchor True
    xalign 0.5 yalign 0.74 # VAGINAL BACK Pivot CORRECT
    xpos 0.5 ypos -0.09
    block:
        ease 2.0/p_ao_n_vel ypos -0.07
        ease 2.0/p_ao_n_vel ypos -0.09
        repeat


transform p_ao_back_bodyTeasing:
    subpixel True
    #"gensex_oral_n_back_t_b_top"
    transform_anchor True
    xalign 0.5 yalign 0.87 # TOP NEUS DOWN PIVOT
    ypos -0.6
    block:
        easein 2.0/p_ao_n_vel ypos -0.5
        ease 2.0/p_ao_n_vel ypos -0.6
        repeat

##
##
# HALF
transform p_ao_back_analHalf:
    subpixel True
    # "gensex_oral_n_back_d_b_anal_over"
    transform_anchor True
    xalign 0.5 yalign 0.71 # ANAL BACK Pivot CORRECT
    xpos 0.5 ypos -0.1
    block:
        easein_quad 4.0/p_ao_n_vel ypos 0.3 # HALF
        ease 4.0/p_ao_n_vel ypos -0.1
        repeat

transform p_ao_back_vaginalHalf:
    subpixel True
    # "gensex_oral_n_back_d_b_anal_over"
    transform_anchor True
    xalign 0.5 yalign 0.74 # VAGINAL BACK Pivot CORRECT
    xpos 0.5 ypos -0.1
    block:
        easein_quad 4.0/p_ao_n_vel ypos 0.3 # HALF
        ease 4.0/p_ao_n_vel ypos -0.1
        repeat

transform p_ao_back_analHalfPlus:
    subpixel True
    # "gensex_oral_n_back_d_b_anal_over"
    transform_anchor True
    xalign 0.5 yalign 0.71 # ANAL BACK Pivot CORRECT
    xpos 0.5 ypos -0.1
    block:
        easein_quad 4.0/p_ao_n_vel ypos 0.45 # HALF
        ease 4.0/p_ao_n_vel ypos -0.1
        repeat

transform p_ao_back_vaginalHalfPlus:
    subpixel True
    # "gensex_oral_n_back_d_b_anal_over"
    transform_anchor True
    xalign 0.5 yalign 0.74 # VAGINAL BACK Pivot CORRECT
    xpos 0.5 ypos -0.1
    block:
        easein_quad 4.0/p_ao_n_vel ypos 0.45 # HALF
        ease 4.0/p_ao_n_vel ypos -0.1
        repeat

transform p_ao_back_analHalf_round:
    subpixel True
    # "gensex_oral_n_back_d_b_anal_over"
    transform_anchor True
    xalign 0.5 yalign 0.71 # ANAL BACK Pivot CORRECT
    xpos 0.5 ypos 0.2
    parallel:
        easein_quad 4.0/p_ao_n_vel ypos 0.3 # HALF
        ease 4.0/p_ao_n_vel ypos 0.2
        repeat
    parallel:
        ease 2.5/p_ao_n_vel rotate 10
        ease 2.5/p_ao_n_vel rotate -10
        repeat

transform p_ao_back_vaginalHalf_round:
    subpixel True
    # "gensex_oral_n_back_d_b_anal_over"
    transform_anchor True
    xalign 0.5 yalign 0.74 # VAGINAL BACK Pivot CORRECT
    xpos 0.5 ypos 0.2
    parallel:
        easein_quad 4.0/p_ao_n_vel ypos 0.3 # HALF
        ease 4.0/p_ao_n_vel ypos 0.2
        repeat
    parallel:
        ease 2.5/p_ao_n_vel rotate 10
        ease 2.5/p_ao_n_vel rotate -10
        repeat

##
transform p_ao_back_backHalf_round:
    subpixel True
    # "gensex_oral_n_back_d_b_anal_over"
    transform_anchor True
    xalign 0.5 yalign 0.71 # ANAL BACK Pivot CORRECT
    xpos 0.5 ypos 0.2
    block:
        easein_quad 4.0/p_ao_n_vel ypos 0.3 # HALF
        ease 4.0/p_ao_n_vel ypos 0.2
        repeat


transform p_ao_back_bodyHalf:
    subpixel True
    #"gensex_oral_n_back_t_b_top"
    transform_anchor True
    xalign 0.5 yalign 0.87 # TOP NEUS DOWN PIVOT
    ypos -0.6
    block:
        easein 4.0/p_ao_n_vel ypos 0.0
        ease 4.0/p_ao_n_vel ypos -0.6
        repeat

transform p_ao_back_bodyHalfPlus:
    subpixel True
    #"gensex_oral_n_back_t_b_top"
    transform_anchor True
    xalign 0.5 yalign 0.87 # TOP NEUS DOWN PIVOT
    ypos -0.6
    block:
        easein 4.0/p_ao_n_vel ypos 0.25
        ease 4.0/p_ao_n_vel ypos -0.6
        repeat

transform p_ao_back_bodyHalf_round:
    subpixel True
    #"gensex_oral_n_back_t_b_top"
    transform_anchor True
    xalign 0.5 yalign 0.87 # TOP NEUS DOWN PIVOT
    ypos -0.1
    block:
        easein 4.0/p_ao_n_vel ypos 0.0
        ease 4.0/p_ao_n_vel ypos -0.1
        repeat


##
##
# WHOLE
transform p_ao_back_analWhole:
    subpixel True
    # "gensex_oral_n_back_d_b_anal_over"
    transform_anchor True
    xalign 0.5 yalign 0.71 # ANAL BACK Pivot CORRECT
    xpos 0.5 ypos -0.1
    block:
        easein_quad 6.0/p_ao_n_vel ypos 0.7 # HALF
        easeout 6.0/p_ao_n_vel ypos -0.1
        repeat


transform p_ao_back_vaginalWhole:
    subpixel True
    # "gensex_oral_n_back_d_b_anal_over"
    transform_anchor True
    xalign 0.5 yalign 0.74 # VAGINAL BACK Pivot CORRECT
    xpos 0.5 ypos -0.1
    block:
        easein_quad 6.0/p_ao_n_vel ypos 0.7 # HALF
        easeout 6.0/p_ao_n_vel ypos -0.1
        repeat

transform p_ao_back_analWholeCheeks:
    subpixel True
    # "gensex_oral_n_back_d_b_anal_over"
    transform_anchor True
    xalign 0.5 yalign 0.71 # ANAL BACK Pivot CORRECT
    xpos 0.5 ypos -0.1
    parallel:
        easein_quad 6.0/p_ao_n_vel ypos 0.7 # HALF
        easeout 6.0/p_ao_n_vel ypos -0.1
        repeat
    parallel:
        pause 4.5/p_ao_n_vel
        ease 1.5/p_ao_n_vel xzoom 1.1 yzoom 0.9
        ease 1.25/p_ao_n_vel xzoom 0.98 yzoom 1.02
        ease 1.0/p_ao_n_vel xzoom 1.0 yzoom 1.0
        pause 3.75/p_ao_n_vel
        repeat

transform p_ao_back_vaginalWholeCheeks:
    subpixel True
    # "gensex_oral_n_back_d_b_anal_over"
    transform_anchor True
    xalign 0.5 yalign 0.74 # VAGINAL BACK Pivot CORRECT
    xpos 0.5 ypos -0.1
    parallel:
        easein_quad 6.0/p_ao_n_vel ypos 0.7 # HALF
        easeout 6.0/p_ao_n_vel ypos -0.1
        repeat
    parallel:
        pause 4.5/p_ao_n_vel
        ease 1.5/p_ao_n_vel xzoom 1.1 yzoom 0.9
        ease 1.25/p_ao_n_vel xzoom 0.98 yzoom 1.02
        ease 1.0/p_ao_n_vel xzoom 1.0 yzoom 1.0
        pause 3.75/p_ao_n_vel
        repeat

transform p_ao_back_bodyWhole:
    subpixel True
    #"gensex_oral_n_back_t_b_top"
    transform_anchor True
    xalign 0.5 yalign 0.87 # TOP NEUS DOWN PIVOT
    ypos -0.6 # Far
    block:
        easein 6.0/p_ao_n_vel ypos 0.6 # CloseTo dick
        easeout 6.0/p_ao_n_vel ypos -0.6
        repeat


########################
############


transform p_ao_wall_neus_b_back_background_pos:
    truecenter
    zoom 1.1

# transform p_ao_wall_neus_b_back_background_pos02:
#     truecenter
#     zoom 5.0

image p_ao_wall_neus_b_back_comp 01:

    contains:
        ConditionSwitch(
            #p_ao_background == "pedrera", At("bg_ped_04", p_ao_wall_neus_b_back_background_pos02),
            "True", At("gensex_oral_bg_ground_noShadow", p_ao_wall_neus_b_back_background_pos))

    # contains:
    #     "gensex_oral_bg_ground_noShadow"
    #     truecenter
    #     zoom 1.1

    # contains:
    #     "p_ao_ghost_standing_comp"
    #     truecenter
    # contains:
    #     "p_ao_ghost_standing_comp"
    #     truecenter
    #     ypos -0.54 rotate 180


## NEUS ASS (BELOW)

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "neusBbackAss_analTeasing", At("gensex_oral_n_back_d_b_anal_below", p_ao_back_analTeasing),
            p_ao_action_Cond == "neusBbackAss_analHalf", At("gensex_oral_n_back_d_b_anal_below", p_ao_back_analHalf),
            p_ao_action_Cond == "neusBbackAss_analHalfPlus", At("gensex_oral_n_back_d_b_anal_below", p_ao_back_analHalfPlus),
            p_ao_action_Cond == "neusBbackAss_analWhole", At("gensex_oral_n_back_d_b_anal_below", p_ao_back_analWhole),

            p_ao_action_Cond == "neusBbackAss_vaginalTeasing", At("gensex_oral_n_back_d_b_vaginal_below", p_ao_back_vaginalTeasing),
            p_ao_action_Cond == "neusBbackAss_vaginalHalf", At("gensex_oral_n_back_d_b_vaginal_below", p_ao_back_vaginalHalf),
            p_ao_action_Cond == "neusBbackAss_vaginalHalfPlus", At("gensex_oral_n_back_d_b_vaginal_below", p_ao_back_vaginalHalfPlus),
            p_ao_action_Cond == "neusBbackAss_vaginalWhole", At("gensex_oral_n_back_d_b_vaginal_below", p_ao_back_vaginalWhole),


            "True", Null())

## MC DICK

    contains:
        ConditionSwitch(
            

            p_ao_dickState_Cond == "throbbing", At("gensex_oral_mc_dick_01_wet_00", p_ao_dick_hardThrobbing),

            p_ao_action_Cond == "alone_semiHard", At("gensex_oral_mc_dick_01_wet_00", p_ao_dick_semiHard),
            
            "True", At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_d_dick_o00_00))

    contains:
        "gensex_oral_mc_body"
        truecenter
        ypos 0.65

## MC_Chest
    contains:
        "gensex_oral_mc_chest"
        truecenter
        ypos 0.65


# BASE VAGINAL-ANAL
    
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "neusBbackAss_analTeasing", At("gensex_oral_n_back_d_b_base", p_ao_back_analTeasing),
            p_ao_action_Cond == "neusBbackAss_analHalf", At("gensex_oral_n_back_d_b_base", p_ao_back_analHalf),
            p_ao_action_Cond == "neusBbackAss_analHalfPlus", At("gensex_oral_n_back_d_b_base", p_ao_back_analHalfPlus),
            p_ao_action_Cond == "neusBbackAss_analWhole", At("gensex_oral_n_back_d_b_base", p_ao_back_analWhole),

            p_ao_action_Cond == "neusBbackAss_analHalf_round", At("gensex_oral_n_back_d_b_base", p_ao_back_backHalf_round),

            p_ao_action_Cond == "neusBbackAss_vaginalTeasing", At("gensex_oral_n_back_d_b_base", p_ao_back_vaginalTeasing),
            p_ao_action_Cond == "neusBbackAss_vaginalHalf", At("gensex_oral_n_back_d_b_base", p_ao_back_vaginalHalf),
            p_ao_action_Cond == "neusBbackAss_vaginalHalfPlus", At("gensex_oral_n_back_d_b_base", p_ao_back_vaginalHalfPlus),
            p_ao_action_Cond == "neusBbackAss_vaginalWhole", At("gensex_oral_n_back_d_b_base", p_ao_back_vaginalWhole),

            
            "True", Null())

# VAGINAL-ANAL OVER

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "neusBbackAss_analTeasing", At("gensex_oral_n_back_d_b_anal_over", p_ao_back_analTeasing),
            p_ao_action_Cond == "neusBbackAss_analHalf", At("gensex_oral_n_back_d_b_anal_over", p_ao_back_analHalf),
            p_ao_action_Cond == "neusBbackAss_analHalfPlus", At("gensex_oral_n_back_d_b_anal_over", p_ao_back_analHalfPlus),
            p_ao_action_Cond == "neusBbackAss_analWhole", At("gensex_oral_n_back_d_b_anal_over", p_ao_back_analWholeCheeks),

            p_ao_action_Cond == "neusBbackAss_analHalf_round", At("gensex_oral_n_back_d_b_anal_over", p_ao_back_analHalf_round),

            p_ao_action_Cond == "neusBbackAss_vaginalTeasing", At("gensex_oral_n_back_d_b_vaginal_over", p_ao_back_vaginalTeasing),
            p_ao_action_Cond == "neusBbackAss_vaginalHalf", At("gensex_oral_n_back_d_b_vaginal_over", p_ao_back_vaginalHalf),
            p_ao_action_Cond == "neusBbackAss_vaginalHalfPlus", At("gensex_oral_n_back_d_b_vaginal_over", p_ao_back_vaginalHalfPlus),
            p_ao_action_Cond == "neusBbackAss_vaginalWhole", At("gensex_oral_n_back_d_b_vaginal_over", p_ao_back_vaginalWholeCheeks),

            
            "True", Null())

## NEUS BACK

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "neusBbackAss_analTeasing", At("gensex_oral_n_back_d_b_back", p_ao_back_analTeasing),
            p_ao_action_Cond == "neusBbackAss_analHalf", At("gensex_oral_n_back_d_b_back", p_ao_back_analHalf),
            p_ao_action_Cond == "neusBbackAss_analHalfPlus", At("gensex_oral_n_back_d_b_back", p_ao_back_analHalfPlus),
            p_ao_action_Cond == "neusBbackAss_analWhole", At("gensex_oral_n_back_d_b_back", p_ao_back_analWhole),

            p_ao_action_Cond == "neusBbackAss_analHalf_round", At("gensex_oral_n_back_d_b_back", p_ao_back_backHalf_round),

            p_ao_action_Cond == "neusBbackAss_vaginalTeasing", At("gensex_oral_n_back_d_b_back", p_ao_back_vaginalTeasing),
            p_ao_action_Cond == "neusBbackAss_vaginalHalf", At("gensex_oral_n_back_d_b_back", p_ao_back_vaginalHalf),
            p_ao_action_Cond == "neusBbackAss_vaginalHalfPlus", At("gensex_oral_n_back_d_b_back", p_ao_back_vaginalHalfPlus),
            p_ao_action_Cond == "neusBbackAss_vaginalWhole", At("gensex_oral_n_back_d_b_back", p_ao_back_vaginalWhole),

            
            "True", Null())



## TOP body NEUS

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "neusBbackAss_analTeasing", At("gensex_oral_n_back_t_b_top", p_ao_back_bodyTeasing),
            p_ao_action_Cond == "neusBbackAss_analHalf", At("gensex_oral_n_back_t_b_top", p_ao_back_bodyHalf),
            p_ao_action_Cond == "neusBbackAss_analHalfPlus", At("gensex_oral_n_back_t_b_top", p_ao_back_bodyHalfPlus),
            p_ao_action_Cond == "neusBbackAss_analWhole", At("gensex_oral_n_back_t_b_top", p_ao_back_bodyWhole),

            p_ao_action_Cond == "neusBbackAss_analHalf_round", At("gensex_oral_n_back_t_b_top", p_ao_back_bodyHalf_round),

            p_ao_action_Cond == "neusBbackAss_vaginalTeasing", At("gensex_oral_n_back_t_b_top", p_ao_back_bodyTeasing),
            p_ao_action_Cond == "neusBbackAss_vaginalHalf", At("gensex_oral_n_back_t_b_top", p_ao_back_bodyHalf),
            p_ao_action_Cond == "neusBbackAss_vaginalHalfPlus", At("gensex_oral_n_back_t_b_top", p_ao_back_bodyHalfPlus),
            p_ao_action_Cond == "neusBbackAss_vaginalWhole", At("gensex_oral_n_back_t_b_top", p_ao_back_bodyWhole),

            "True", Null())

# Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##
##


#Dick

transform ped05_sex_oral_n_dick_tongue_01: # Soft
    ##ped05_sex_oral_d_dick_o00_00
    truecenter
    ypos 0.8
    xzoom 0.48 yzoom 0.29

transform ped05_sex_oral_n_dick_tongue_02: # Soft
    ##ped05_sex_oral_d_dick_o00_00
    truecenter
    ypos 0.8
    xzoom 0.7 yzoom 0.6

transform ped05_sex_oral_n_dick_tongue_03:
    truecenter
    ypos 0.8

# LEGS
transform ped05_sex_oral_n_legs_tongue_01:
    subpixel True
    ## ped05_sex_oral_n_legs_down_action
    truecenter
    ypos 0.42 #Up
    block:
        ease 10.0/p_ao_n_vel ypos 0.45 #Down
        ease 10.0/p_ao_n_vel ypos 0.42 #Up
        repeat

transform ped05_sex_oral_n_legs_tongue_02:
    subpixel True
    ## ped05_sex_oral_n_legs_down_action
    truecenter
    ypos 0.4 #Up
    block:
        ease 10.0/p_ao_n_vel ypos 0.5 #Down
        ease 10.0/p_ao_n_vel ypos 0.4 #Up
        repeat

transform ped05_sex_oral_n_legs_tongue_03:
    subpixel True
    ## ped05_sex_oral_n_legs_down_action
    truecenter
    ypos 0.4 #Up
    block:
        ease 10.0/p_ao_n_vel ypos 0.5 #Down
        ease 10.0/p_ao_n_vel ypos 0.4 #Up
        repeat
    

# BODY
transform p_ao_sex_oral_n_body_tongue_01:
    subpixel True
    ## ped05_sex_oral_d_body_o00_00
    transform_anchor True
    xalign 0.5 yalign 0.2
    ypos 0.15 #Up
    block:
        ease 10.0/p_ao_n_vel ypos 0.23 # Down?
        ease 10.0/p_ao_n_vel ypos 0.15 #Up
        repeat

transform p_ao_sex_oral_n_body_tongue_02:
    subpixel True
    ## ped05_sex_oral_d_body_o00_00
    transform_anchor True
    xalign 0.5 yalign 0.2
    ypos 0.1 #Up
    block:
        ease 10.0/p_ao_n_vel ypos 0.25 # Down?
        ease 10.0/p_ao_n_vel ypos 0.1 #Up
        repeat

transform p_ao_sex_oral_n_body_tongue_03:
    subpixel True
    ## ped05_sex_oral_d_body_o00_00
    transform_anchor True
    xalign 0.5 yalign 0.2
    ypos 0.1 #Up
    block:
        ease 10.0/p_ao_n_vel ypos 0.25 # Down?
        ease 10.0/p_ao_n_vel ypos 0.1 #Up
        repeat
    

# HEAD

transform p_ao_sex_oral_n_frontHead_tongue_01:
    subpixel True
    ## ped05_sex_oral_d_frontHead_o00_00
    truecenter
    ypos 0.25 # Up
    block:
        ease 10.0/p_ao_n_vel ypos 0.4 #Down
        ease 10.0/p_ao_n_vel ypos 0.25 # Up
        repeat
    
transform p_ao_sex_oral_n_frontHead_tongue_02:
    subpixel True
    ## ped05_sex_oral_d_frontHead_o00_00
    truecenter
    ypos 0.0 # Up¡
    block:
        ease 10.0/p_ao_n_vel ypos 0.38 #Down
        ease 10.0/p_ao_n_vel ypos 0.0 # Up
        repeat
    
transform p_ao_sex_oral_n_frontHead_tongue_03:
    subpixel True
    ## ped05_sex_oral_d_frontHead_o00_00
    truecenter
    ypos -0.2 # Up
    block:
        ease 10.0/p_ao_n_vel ypos 0.35 # Down?
        ease 10.0/p_ao_n_vel ypos -0.2 # Up
        repeat
    

# TONGUE

transform p_ao_sex_oral_n_zextraTongue_tongue_01:
    subpixel True
    ## gensex_oral_n_zextra_tongue
    truecenter
    zoom 1.23
    ypos 0.59 # Up
    block:
        ease_back 10.0/p_ao_n_vel ypos 0.68 #Down
        ease_back 10.0/p_ao_n_vel ypos 0.59 # Up
        repeat

transform p_ao_sex_oral_n_zextraTongue_tongue_02:
    subpixel True
    ## gensex_oral_n_zextra_tongue
    truecenter
    zoom 1.0
    ypos 0.4 # Up
    block:
        ease_back 10.0/p_ao_n_vel ypos 0.66 # Down
        ease_back 10.0/p_ao_n_vel ypos 0.4 # Up
        repeat

transform p_ao_sex_oral_n_zextraTongue_tongue_03:
    subpixel True
    ## gensex_oral_n_zextra_tongue
    truecenter
    ypos 0.15 # Up
    block:
        ease_back 10.0/p_ao_n_vel ypos 0.6 # Down
        ease_back 10.0/p_ao_n_vel ypos 0.15 # Up
        repeat


image pedrera_sex_neus_oral tongue:

## BACKGROUND

    contains:
        "bg_ped_04"
        truecenter
        zoom 3.3
        #"gensex_oral_bg_grounddown"
        # truecenter
        # zoom 1.1

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 1.8 ypos 0.15

## NEUS

# Legs
    
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "lickDick_01", At("gensex_oral_n_legs down", ped05_sex_oral_n_legs_tongue_01),
            p_ao_action_Cond == "lickDick_02", At("gensex_oral_n_legs down", ped05_sex_oral_n_legs_tongue_02),
            p_ao_action_Cond == "lickDick_03", At("gensex_oral_n_legs down", ped05_sex_oral_n_legs_tongue_03),
            "True", Null())
    # contains:
    #     "gensex_oral_n_legs down"
    #     ped05_sex_oral_n_legs_tongue_03

# Hair
    
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "lickDick_01", At("gensex_oral_n_boobJob_body_hair", p_ao_sex_oral_n_body_tongue_01),
            p_ao_action_Cond == "lickDick_02", At("gensex_oral_n_boobJob_body_hair", p_ao_sex_oral_n_body_tongue_02),
            p_ao_action_Cond == "lickDick_03", At("gensex_oral_n_boobJob_body_hair", p_ao_sex_oral_n_body_tongue_03),
            "True", Null())

    # contains:
    #     "gensex_oral_n_boobJob_body_hair"
    #     p_ao_sex_oral_n_body_tongue_03

# Body

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "lickDick_01", At("gensex_oral_n_down_body", p_ao_sex_oral_n_body_tongue_01),
            p_ao_action_Cond == "lickDick_02", At("gensex_oral_n_down_body", p_ao_sex_oral_n_body_tongue_02),
            p_ao_action_Cond == "lickDick_03", At("gensex_oral_n_down_body", p_ao_sex_oral_n_body_tongue_03),
            "True", Null())

    # contains:
    #     "gensex_oral_n_down_body"
    #     p_ao_sex_oral_n_body_tongue_03

# HairNeck

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "lickDick_01", At("gensex_oral_n_frontHead_hair_back_ground", p_ao_sex_oral_n_frontHead_tongue_01),
            p_ao_action_Cond == "lickDick_02", At("gensex_oral_n_frontHead_hair_back_ground", p_ao_sex_oral_n_frontHead_tongue_02),
            p_ao_action_Cond == "lickDick_03", At("gensex_oral_n_frontHead_hair_back_ground", p_ao_sex_oral_n_frontHead_tongue_03),
            "True", Null())
    # contains:
    #     "gensex_oral_n_frontHead_hair_back_ground"
    #     p_ao_sex_oral_n_frontHead_tongue_03

# Ears

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "lickDick_01", At("gensex_oral_n_frontHead_ears down", p_ao_sex_oral_n_frontHead_tongue_01),
            p_ao_action_Cond == "lickDick_02", At("gensex_oral_n_frontHead_ears down", p_ao_sex_oral_n_frontHead_tongue_02),
            p_ao_action_Cond == "lickDick_03", At("gensex_oral_n_frontHead_ears down", p_ao_sex_oral_n_frontHead_tongue_03),
            "True", Null())

    # contains:
    #     "gensex_oral_n_frontHead_ears down"
    #     p_ao_sex_oral_n_frontHead_tongue_03

# Expressions

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "lickDick_01", At("ped_sex_oral_expression_img", p_ao_sex_oral_n_frontHead_tongue_01),
            p_ao_action_Cond == "lickDick_02", At("ped_sex_oral_expression_img", p_ao_sex_oral_n_frontHead_tongue_02),
            p_ao_action_Cond == "lickDick_03", At("ped_sex_oral_expression_img", p_ao_sex_oral_n_frontHead_tongue_03),
            "True", Null())

    # contains:
    #     "ped_sex_oral_expression_img"
    #     p_ao_sex_oral_n_frontHead_tongue_03

# FrontHair

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "lickDick_01", At("gensex_oral_n_frontHead_hair", p_ao_sex_oral_n_frontHead_tongue_01),
            p_ao_action_Cond == "lickDick_02", At("gensex_oral_n_frontHead_hair", p_ao_sex_oral_n_frontHead_tongue_02),
            p_ao_action_Cond == "lickDick_03", At("gensex_oral_n_frontHead_hair", p_ao_sex_oral_n_frontHead_tongue_03),
            "True", Null())

    # contains:
    #     "gensex_oral_n_frontHead_hair"
    #     p_ao_sex_oral_n_frontHead_tongue_03
    
###

## MC DICK

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "lickDick_01", At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_n_dick_tongue_01),
            p_ao_action_Cond == "lickDick_02", At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_n_dick_tongue_02),
            "True", At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_d_dick_o00_00))

## TONGUE

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "lickDick_01", At("gensex_oral_n_zextra_tongue_01", p_ao_sex_oral_n_zextraTongue_tongue_01),
            p_ao_action_Cond == "lickDick_02", At("gensex_oral_n_zextra_tongue_02", p_ao_sex_oral_n_zextraTongue_tongue_02),
            p_ao_action_Cond == "lickDick_03", At("gensex_oral_n_zextra_tongue_03", p_ao_sex_oral_n_zextraTongue_tongue_03),
            "True", Null())


    # contains:
    #     "gensex_oral_n_zextra_tongue_03"
    #     p_ao_sex_oral_n_zextraTongue_tongue_03

    contains:
        "gensex_oral_mc_body"
        truecenter
        ypos 0.65

## MC_Chest
    contains:
        "gensex_oral_mc_chest"
        truecenter
        ypos 0.65

# Smoke
    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_pos




######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##
##



# HEAD

transform p_ao_sex_oral_n_frontHead_kissTip_01:
    subpixel True

    ## ped05_sex_oral_d_frontHead_o00_00
    truecenter
    ypos 0.18 # Up
    parallel:
        #ease 2.5/p_ao_n_vel ypos 0.4 # Down
        ease 10.0/p_ao_n_vel ypos 0.25 # Half Soft
        ease 10.0/p_ao_n_vel ypos 0.18 # Up Soft
        repeat
    parallel:
        easein_quad 8.8/p_ao_n_vel xpos 0.52 rotate 10
        ease 7.2/p_ao_n_vel xpos 0.48 rotate -10
        repeat
    # block:
    #     ease 10.0/p_ao_n_vel ypos 0.4 #Down
    #     ease 10.0/p_ao_n_vel ypos 0.25 # Up
    #     repeat

transform p_ao_sex_oral_n_hairNeck_kissTip_01:
    subpixel True
    truecenter
    ypos 0.18 # Up
    block:
        ease 10.0/p_ao_n_vel ypos 0.25 # Half Soft
        ease 10.0/p_ao_n_vel ypos 0.18 # Up Soft
        repeat

## Hand

transform p_ao_sex_oral_n_hand_kissTip_01:
    subpixel True 
    truecenter
    zoom 0.85
    ypos 0.68 # down
    block:
        easein_quad 4.0/p_ao_n_vel  ypos 0.64 # Up
        easeout_quad 4.0/p_ao_n_vel  ypos 0.68 # Down
        repeat

image pedrera_sex_neus_oral kissingTip:

## BACKGROUND

    contains:
        "bg_ped_04"
        truecenter
        zoom 3.3
        #"gensex_oral_bg_grounddown"
        # truecenter
        # zoom 1.1

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        ypos -0.54 rotate 180


## NEUS

# Legs
    contains:
        "gensex_oral_n_legs down"
        ped05_sex_oral_n_legs_tongue_01

# # Hair

#     contains:
#         "gensex_oral_n_boobJob_body_hair"
#         p_ao_sex_oral_n_body_tongue_01

# Body

    contains:
        "gensex_oral_n_down_body"
        p_ao_sex_oral_n_body_tongue_01

# HairNeck
    contains:
        "gensex_oral_n_frontHead_hair_back_ground"
        p_ao_sex_oral_n_hairNeck_kissTip_01

# Ears

    contains:
        "gensex_oral_n_frontHead_ears down"
        p_ao_sex_oral_n_frontHead_kissTip_01

# Expressions

    contains:
        "ped_sex_oral_expression_img"
        p_ao_sex_oral_n_frontHead_kissTip_01

# FrontHair

    contains:
        "gensex_oral_n_frontHead_hair"
        p_ao_sex_oral_n_frontHead_kissTip_01
    
###


## Neus Hand

    contains:
        "gensex_oral_n_down_hand_mast_bot"
        p_ao_sex_oral_n_hand_kissTip_01

## MC DICK

    contains:
        "gensex_oral_mc_dick_01_wet_00"
        ped05_sex_oral_d_dick_o_soft

## Neus Hand

    contains:
        "gensex_oral_n_down_hand_mast_top"
        p_ao_sex_oral_n_hand_kissTip_01

## MC Body

    contains:
        "gensex_oral_mc_body"
        truecenter
        ypos 0.65

## MC_Chest
    contains:
        "gensex_oral_mc_chest"
        truecenter
        ypos 0.65

# Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())

######################################################################################################
######################################################################################################

transform p_ao_sex_oral_n_frontHead_CloseTip_01:
    #p_ao_sex_oral_n_frontHead_kissTip_01
    truecenter
    ypos 0.18 # Up
    # parallel:
    #     #ease 2.5/p_ao_n_vel ypos 0.4 # Down
    #     ease 10.0/p_ao_n_vel ypos 0.25 # Half Soft
    #     ease 10.0/p_ao_n_vel ypos 0.18 # Up Soft
    #     repeat
    # parallel:
    #     easein_quad 8.8/p_ao_n_vel xpos 0.52 rotate 10
    #     ease 7.2/p_ao_n_vel xpos 0.48 rotate -10
    #     repeat

transform p_ao_sex_oral_n_frontHead_CloseTip_Over:
    truecenter
    zoom 1.0
    ypos 0.23

image pedrera_sex_neus_oral CloseTip:

## BACKGROUND

    contains:
        "bg_ped_04"
        truecenter
        zoom 3.3
        #"gensex_oral_bg_grounddown"
        #zoom 1.1
        
        


    contains:
        "p_ao_ghost_standing_comp"
        truecenter
    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        ypos -0.54 rotate 180



## NEUS

# Legs
    contains:
        "gensex_oral_n_legs down"
        ped05_sex_oral_n_legs_tongue_01

# # Hair

#     contains:
#         "gensex_oral_n_boobJob_body_hair"
#         p_ao_sex_oral_n_body_tongue_01

# Body

    contains:
        "gensex_oral_n_down_body"
        p_ao_sex_oral_n_body_tongue_01

# HairNeck
    contains:
        "gensex_oral_n_frontHead_hair_back_ground"
        p_ao_sex_oral_n_frontHead_CloseTip_01

# Ears

    contains:
        "gensex_oral_n_frontHead_ears down"
        p_ao_sex_oral_n_frontHead_CloseTip_01

## FACE??
    contains:
        "gensex_oral_n_frontHead_face"
        p_ao_sex_oral_n_frontHead_CloseTip_01

# # Expressions

#     contains:
#         "ped_sex_oral_expression_img"
#         p_ao_sex_oral_n_frontHead_CloseTip_01

# FrontHair

    # contains:
    #     "gensex_oral_n_frontHead_hair"
    #     p_ao_sex_oral_n_frontHead_CloseTip_01
    
###


# ## Neus Hand

#     contains:
#         "gensex_oral_n_down_hand_mast_bot"
#         p_ao_sex_oral_n_hand_kissTip_01

## MC DICK

    contains:
        "gensex_oral_mc_dick_01_wet_00"
        ped05_sex_oral_d_dick_o_soft

# ## Neus Hand

#     contains:
#         "gensex_oral_n_down_hand_mast_top"
#         p_ao_sex_oral_n_hand_kissTip_01

## MC Body

    contains:
        "gensex_oral_mc_body"
        truecenter
        ypos 0.65

## MC_Chest
    contains:
        "gensex_oral_mc_chest"
        truecenter
        ypos 0.65

# No Smoke here, goes in the other layer over.


image pedrera_sex_neus_oral_CloseTipOver:


## MC DICK

    contains:
        "gensex_oral_mc_dick_01_wet_00"
        ped05_sex_oral_d_dick_o_soft

# ## Neus Hand

#     contains:
#         "gensex_oral_n_down_hand_mast_top"
#         p_ao_sex_oral_n_hand_kissTip_01

## MC Body

    contains:
        "gensex_oral_mc_body"
        truecenter
        ypos 0.65

## MC_Chest
    contains:
        "gensex_oral_mc_chest"
        truecenter
        ypos 0.65

# Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

transform p_ao_sex_oral_n_frontHead_softLicking_01:
    subpixel True
    #p_ao_sex_oral_n_frontHead_kissTip_01
        ## ped05_sex_oral_d_frontHead_o00_00
    truecenter
    ypos 0.07 # Up
    block:
        #ease 2.5/p_ao_n_vel ypos 0.4 # Down
        ease 10.0/p_ao_n_vel ypos 0.27 # Half Soft
        ease 10.0/p_ao_n_vel ypos 0.07 # Up Soft
        repeat


image pedrera_sex_neus_oral softLicking:

## BACKGROUND

    contains:
        # "gensex_oral_bg_grounddown"
        # truecenter
        # zoom 1.1
        "bg_ped_04"
        truecenter
        zoom 3.3
## NEUS

# Legs
    contains:
        "gensex_oral_n_legs down"
        ped05_sex_oral_n_legs_tongue_01


# Body

    contains:
        "gensex_oral_n_down_body"
        p_ao_sex_oral_n_body_tongue_01

# HairNeck
    contains:
        "gensex_oral_n_frontHead_hair_back_ground"
        p_ao_sex_oral_n_frontHead_softLicking_01

# Ears

    contains:
        "gensex_oral_n_frontHead_ears down"
        p_ao_sex_oral_n_frontHead_softLicking_01

# Expressions

    contains:
        "ped_sex_oral_expression_img"
        p_ao_sex_oral_n_frontHead_softLicking_01

# FrontHair

    contains:
        "gensex_oral_n_frontHead_hair"
        p_ao_sex_oral_n_frontHead_softLicking_01
    
###

# Neus Tongue

    contains:
        ConditionSwitch(
            p_ao_n_tongue == "bifid", At("gensex_oral_n_frontHead_exp_tongue_bifid_comp", p_ao_sex_oral_n_frontHead_softLicking_01),
            "True", At("gensex_oral_n_frontHead_exp_tongue_05", p_ao_sex_oral_n_frontHead_softLicking_01))

    # contains:
    #     "gensex_oral_n_frontHead_exp_tongue_05"
    #     p_ao_sex_oral_n_frontHead_softLicking_01
    # contains:
    #     "gensex_oral_n_frontHead_exp_tongue_bifid_comp"
    #     p_ao_sex_oral_n_frontHead_softLicking_01

## MC DICK

    contains:
        "gensex_oral_mc_dick_01_wet_00"
        ped05_sex_oral_d_dick_o_soft

## MC Body

    contains:
        "gensex_oral_mc_body"
        truecenter
        ypos 0.65

## MC_Chest
    contains:
        "gensex_oral_mc_chest"
        truecenter
        ypos 0.65

# Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################


image pedrera_sex_neus_oral hardLicking:

## BACKGROUND

    contains:
        # "gensex_oral_bg_grounddown"
        # truecenter
        # zoom 1.1
        "bg_ped_04"
        truecenter
        zoom 3.3

## NEUS

# Legs
    contains:
        "gensex_oral_n_legs down"
        ped05_sex_oral_n_legs_tongue_01


# Body

    contains:
        "gensex_oral_n_down_body"
        p_ao_sex_oral_n_body_tongue_01

# HairNeck
    contains:
        "gensex_oral_n_frontHead_hair_back_ground"
        p_ao_sex_oral_n_frontHead_softLicking_01

# Ears

    contains:
        "gensex_oral_n_frontHead_ears down"
        p_ao_sex_oral_n_frontHead_softLicking_01

# Expressions

    contains:
        "ped_sex_oral_expression_img"
        p_ao_sex_oral_n_frontHead_softLicking_01

# FrontHair

    contains:
        "gensex_oral_n_frontHead_hair"
        p_ao_sex_oral_n_frontHead_softLicking_01
    
###

# Neus Tongue

    contains:
        "gensex_oral_n_frontHead_exp_tongue_05"
        p_ao_sex_oral_n_frontHead_softLicking_01

## MC DICK

    contains:
        "gensex_oral_mc_dick_01_wet_00"
        ped05_sex_oral_d_dick_o00_00

## MC Body

    contains:
        "gensex_oral_mc_body"
        truecenter
        ypos 0.65

## MC_Chest
    contains:
        "gensex_oral_mc_chest"
        truecenter
        ypos 0.65

# Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##
##
default myFuckinAlpha = 1.0

## MC DICK

transform gensex_briding_MC_dick_in_moveSlow_erect_n_base:
    transform_anchor True
    xalign 0.5 yalign 0.6
    xpos 0.5 ypos 0.8

transform gensex_briding_MC_dick_in_moveSlow_erect_n_00:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.6
    xpos 0.5 ypos 0.8
    #xzoom 0.8 yzoom 0.3
    pause 10.0/p_ao_n_vel
    block:
        pause 2.0/p_ao_n_vel
        ease 2.0/p_ao_n_vel ypos 0.82
        ease 4.0/p_ao_n_vel ypos 0.8
        repeat

transform gensex_briding_MC_dick_in_moveSlow_erect_n_01:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.6
    ypos 0.8
    block:
        pause 2.0/p_ao_n_vel
        ease 2.0/p_ao_n_vel ypos 0.82
        ease 4.0/p_ao_n_vel ypos 0.8
        repeat

#############################################################################
# HER BODY
transform gensex_briding_n_body_vaginal_move_00:
    subpixel True
    gensex_briding_D_center_pos
    alpha myFuckinAlpha
    ypos -0.3 # Out of Dick
    ease 10.0/p_ao_n_vel ypos 0.15 # Over Tip
    block:
        easein 4.0/p_ao_n_vel ypos 0.2 # Over Glans
        ease 4.0/p_ao_n_vel ypos 0.15 # Over Tip
        repeat

transform gensex_briding_n_body_vaginal_move_01:
    subpixel True
    gensex_briding_D_center_pos
    alpha myFuckinAlpha
    ypos 0.15 # Over Tip
    block:
        easein 4.0/p_ao_n_vel ypos 0.2 # Over Glans
        ease 4.0/p_ao_n_vel ypos 0.15 # Over Tip
        repeat

transform gensex_briding_n_body_vaginal_move_02:
    subpixel True
    gensex_briding_D_center_pos
    alpha myFuckinAlpha
    ypos 0.15 # Over Tip
    block:
        easein 4.0/p_ao_n_vel ypos 0.35 # Half Dick
        ease 4.0/p_ao_n_vel ypos 0.15 # Over Tip
        repeat

transform gensex_briding_n_body_vaginal_move_03:
    subpixel True
    gensex_briding_D_center_pos
    alpha myFuckinAlpha
    zoom 1.0 ypos 0.15 # Over Tip
    block:
        easein 4.0/p_ao_n_vel zoom 1.05 ypos 0.6 # ALMOST IN
        ease 4.0/p_ao_n_vel zoom 1.0 ypos 0.15 # Over Tip
        repeat

transform gensex_briding_n_body_vaginal_move_04:
    subpixel True
    gensex_briding_D_center_pos
    alpha myFuckinAlpha
    #ypos 0.095 # Over Tip
    zoom 1.0 ypos 0.15
    block:
        easein 4.0/p_ao_n_vel zoom 1.1 ypos 0.8 # ALL IN
        ease 4.0/p_ao_n_vel zoom 1.0 ypos 0.15 # Over Tip
        repeat
#############################################################################
##
transform gensex_briding_n_body_Anal_move_00:
    subpixel True
    gensex_briding_D_center_pos
    alpha myFuckinAlpha
    ypos 0.25 # Out of Dick
    ease 10.0/p_ao_n_vel ypos 0.37 # Over Tip
    block:
        easein 4.0/p_ao_n_vel ypos 0.4 # OVER GLANS
        ease 4.0/p_ao_n_vel ypos 0.37 # Over Tip
        repeat

transform gensex_briding_n_body_Anal_move_01:
    subpixel True
    truecenter
    alpha myFuckinAlpha
    ypos 0.37 # Over Tip
    block:
        easein 4.0/p_ao_n_vel ypos 0.4 # OVER GLANS
        ease 4.0/p_ao_n_vel ypos 0.37 # Over Tip
        repeat

transform gensex_briding_n_body_Anal_move_02:
    subpixel True
    gensex_briding_D_center_pos
    alpha myFuckinAlpha
    ypos 0.37 # Over Tip
    block:
        easein 4.0/p_ao_n_vel ypos 0.5 # Half Dick
        ease 4.0/p_ao_n_vel ypos 0.37 # Over Tip
        repeat

transform gensex_briding_n_body_Anal_move_03:
    subpixel True
    gensex_briding_D_center_pos
    alpha myFuckinAlpha
    zoom 1.0 ypos 0.37 # Over Tip
    block:
        easein 4.0/p_ao_n_vel zoom 1.05 ypos 0.8 # ALMOST IN
        ease 4.0/p_ao_n_vel zoom 1.0 ypos 0.37 # Over Tip
        repeat

transform gensex_briding_n_body_Anal_move_04:
    subpixel True
    gensex_briding_D_center_pos
    alpha myFuckinAlpha
    zoom 1.0 ypos 0.37 # Over Tip
    block:
        easein 4.0/p_ao_n_vel zoom 1.1 ypos 1.0 # ALL IN
        ease 4.0/p_ao_n_vel zoom 1.0 ypos 0.37 # Over Tip
        repeat


#############################################################################
# HER LEGS
transform gensex_briding_n_legs_movesVaginal_00:
    subpixel True
    truecenter
    alpha myFuckinAlpha
    zoom 0.9 ypos -0.5  # Out
    ease 10.0/p_ao_n_vel zoom 0.96 ypos -0.05  # On Tip.
    block:
        easein 4.0/p_ao_n_vel zoom 0.98 ypos 0.07  # Over Glans
        ease 4.0/p_ao_n_vel zoom 0.96 ypos -0.05  # Over Tip.
        repeat

transform gensex_briding_n_legs_movesVaginal_01:
    subpixel True
    truecenter
    alpha myFuckinAlpha
    zoom 0.95 ypos -0.05  # On Tip.
    block:
        easein 4.0/p_ao_n_vel zoom 0.98 ypos 0.07  # Over Glans
        ease 4.0/p_ao_n_vel zoom 0.96 ypos -0.05  # Over Tip.
        repeat

transform gensex_briding_n_legs_movesVaginal_02:
    subpixel True
    truecenter
    alpha myFuckinAlpha
    zoom 0.96 ypos -0.05  # Over Tip.
    block:
        easein 4.0/p_ao_n_vel zoom 1.025 ypos 0.3  # Bit more Half Dick.
        ease 4.0/p_ao_n_vel zoom 0.96 ypos -0.05  # Over Tip.
        repeat

transform gensex_briding_n_legs_movesVaginal_03:
    subpixel True
    gensex_briding_D_center_pos
    alpha myFuckinAlpha
    zoom 0.96 ypos -0.05  # Over Tip.
    block:
        easein 4.0/p_ao_n_vel zoom 1.0 ypos 0.53  # Almost IN
        ease 4.0/p_ao_n_vel zoom 0.96 ypos -0.05  # Over Tip.
        repeat


transform gensex_briding_n_legs_movesVaginal_04:
    subpixel True
    truecenter
    alpha myFuckinAlpha
    zoom 0.96 ypos -0.05  # Over Tip.
    block:
        easein 4.0/p_ao_n_vel zoom 1.15 ypos 0.72  # ALL IN
        ease 4.0/p_ao_n_vel zoom 0.96 ypos -0.05  # Over Tip.
        repeat


# transform gensex_briding_n_legs_movesVaginal_03:
    subpixel True #
#     gensex_briding_D_center_pos
#     ypos -0.1 zoom 0.96 # Over Tip.
#     block:
#         ease 0.25 ypos 0.5 zoom 1.0 # Almost IN
#         ease 0.25 ypos -0.1 zoom 0.96 # Over Tip.
#         repeat

##
#############################################################################
transform gensex_briding_n_legs_movesAnal_00:
    subpixel True #
    # gensex_briding_D_legs_movesAnal_01
    truecenter
    alpha myFuckinAlpha
    ypos -0.1 zoom 0.95 # Out
    ease 10.0/p_ao_n_vel zoom 0.96 ypos 0.05 # Over Tip.
    block:
        easein 4.0/p_ao_n_vel zoom 0.98 ypos 0.22 # OVER GLANS
        ease 4.0/p_ao_n_vel zoom 0.96 ypos 0.05 # Over Tip.
        repeat

image gensex_briding_n_legs_movesAnal_00_cheecks_image: #
    # gensex_briding_D_legs_movesAnal_01
    "gensex_briding_n_legs_ass_vaginal"
    pause 8.0/p_ao_n_vel
    "gensex_briding_n_legs_ass_anal" with Dissolve(2.0/p_ao_n_vel)

transform gensex_briding_n_legs_movesAnal_00_cheecks:
    subpixel True #
    # gensex_briding_D_legs_movesAnal_01
    truecenter
    alpha myFuckinAlpha
    ypos -0.1 zoom 0.95 # Out
    ease 10.0/p_ao_n_vel zoom 0.96 ypos 0.05  # Over Tip.
    block:
        easein 4.0/p_ao_n_vel zoom 0.98 ypos 0.22 # OVER GLANS
        ease 4.0/p_ao_n_vel zoom 0.96 ypos 0.05 # Over Tip.
        repeat

transform gensex_briding_n_legs_movesAnal_01:
    subpixel True #
    # gensex_briding_D_legs_movesAnal_01
    truecenter
    #alpha myFuckinAlpha
    zoom 0.96 ypos 0.05 # Over Tip.
    block:
        easein 4.0/p_ao_n_vel zoom 0.98 ypos 0.22 # OVER GLANS
        ease 4.0/p_ao_n_vel zoom 0.96 ypos 0.05 # Over Tip.
        repeat

transform gensex_briding_n_legs_movesAnal_02:
    subpixel True # Introduction to Pussy.
    gensex_briding_D_center_pos
    #alpha myFuckinAlpha
    zoom 0.96 ypos 0.05  # Over Tip.
    block:
        easein 4.0/p_ao_n_vel zoom 1.0 ypos 0.4 # Half Dick.
        ease 4.0/p_ao_n_vel zoom 0.96 ypos 0.05  # Over Tip.
        repeat

transform gensex_briding_n_legs_movesAnal_03:
    subpixel True # Introduction to Pussy.
    gensex_briding_D_center_pos
    #alpha myFuckinAlpha
    zoom 0.96 ypos 0.05  # Over Tip.
    block:
        easein 4.0/p_ao_n_vel zoom 1.05 ypos 0.68  # Almost In
        ease 4.0/p_ao_n_vel zoom 0.96 ypos 0.05  # Over Tip.
        repeat

transform gensex_briding_n_legs_movesAnal_04:
    subpixel True # Introduction to Pussy.
    gensex_briding_D_center_pos
    #alpha myFuckinAlpha
    zoom 0.96 ypos 0.05  # Over Tip.
    block:
        easein 4.0/p_ao_n_vel zoom 1.07 ypos 0.85 # ALL IN
        ease 4.0/p_ao_n_vel zoom 0.96 ypos 0.05  # Over Tip.
        repeat

#############################################################################
## HER FUCKING VAGINA

transform gensex_briding_n_open_vaginal_move_00:
    subpixel True
    gensex_briding_D_center_pos
    #gensex_briding_D_legs_movesVaginal_01
    #zoom 0.8 # Half Dick.
    xzoom 0.55 yzoom 0.45 ypos -0.01 # Beginning
    alpha 0.0
    pause 8.0/p_ao_n_vel
    easein_quad 2.0/p_ao_n_vel alpha 1.0 
    block:
        easein 4.0/p_ao_n_vel xzoom 0.7 yzoom 0.6 ypos 0.1 # Over Glans
        ease 4.0/p_ao_n_vel xzoom 0.55 yzoom 0.5 ypos -0.01 # High Top Vaginal
        repeat

transform gensex_briding_n_open_vaginal_move_01:
    subpixel True
    truecenter
    #alpha myFuckinAlpha
    xzoom 0.55 yzoom 0.5 ypos -0.01 # High Top Vaginal
    block:
        easein 4.0/p_ao_n_vel xzoom 0.65 yzoom 0.6 ypos 0.1 # Over Glans
        ease 4.0/p_ao_n_vel xzoom 0.55 yzoom 0.5 ypos -0.01 # High Top Vaginal
        repeat

transform gensex_briding_n_open_vaginal_move_02:
    subpixel True
    gensex_briding_D_center_pos
    #alpha myFuckinAlpha
    xzoom 0.55 yzoom 0.5 ypos -0.01 # High Top Vaginal
    block:
        easein 4.0/p_ao_n_vel xzoom 0.84 yzoom 0.88 ypos 0.29 # Over Tip Vaginal
        ease 4.0/p_ao_n_vel xzoom 0.55 yzoom 0.5 ypos -0.01 # High Top Vaginal
        repeat

transform gensex_briding_n_open_vaginal_move_03:
    subpixel True
    gensex_briding_D_center_pos
    #alpha myFuckinAlpha
    xzoom 0.55 yzoom 0.5 ypos -0.01 # High Top Vaginal
    block:
        easein 4.0/p_ao_n_vel xzoom 0.95 yzoom 0.7 ypos 0.53 # Almost IN
        ease 4.0/p_ao_n_vel xzoom 0.55 yzoom 0.5 ypos -0.01 # High Top Vaginal
        repeat

transform gensex_briding_n_open_vaginal_move_04:
    subpixel True
    gensex_briding_D_center_pos
    #alpha myFuckinAlpha
    xzoom 0.55 yzoom 0.5 ypos -0.01 # High Top Vaginal
    block:
        easein 4.0/p_ao_n_vel xzoom 0.9 yzoom 0.67 ypos 0.7 # ALL IN
        ease 4.0/p_ao_n_vel xzoom 0.58 yzoom 0.5 ypos -0.01 # High Top Vaginal
        repeat

    #xzoom 1.0 yzoom 0.67 ypos 0.7 # ALL IN

#############################################################################
## HER FUCKING ASSHOLE

transform gensex_briding_n_open_anal_move_00:
    subpixel True
    # gensex_briding_D_open_anal_move_01
    truecenter
    alpha myFuckinAlpha
    xzoom 0.65 yzoom 0.5 ypos -0.03 # Tip Anal
    alpha 0.0
    pause 8.0/p_ao_n_vel
    easein_quad 2.0/p_ao_n_vel alpha 1.0 
    block:
        easein 4.0/p_ao_n_vel xzoom 0.7 yzoom 0.6 ypos 0.1 # OVER GLANS
        ease 4.0/p_ao_n_vel xzoom 0.65 yzoom 0.5 ypos -0.03 # Tip Anal
        repeat


transform gensex_briding_n_open_anal_move_01:
    subpixel True
    # gensex_briding_D_open_anal_move_01
    truecenter
    #alpha myFuckinAlpha
    xzoom 0.65 yzoom 0.5 ypos -0.03 # High Top Anal
    block:
        easein 4.0/p_ao_n_vel xzoom 0.7 yzoom 0.6 ypos 0.1 # OVER GLANS
        ease 4.0/p_ao_n_vel xzoom 0.65 yzoom 0.5 ypos -0.03 # High Top Anal
        repeat

transform gensex_briding_n_open_anal_move_02:
    subpixel True
    gensex_briding_D_center_pos
    #alpha myFuckinAlpha
    xzoom 0.65 yzoom 0.5 ypos -0.03 # High Top Anal
    block:
        easein 4.0/p_ao_n_vel xzoom 0.92 yzoom 0.86 ypos 0.29 # hALF
        ease 4.0/p_ao_n_vel xzoom 0.65 yzoom 0.5 ypos -0.03 # High Top Anal
        repeat

transform gensex_briding_n_open_anal_move_03:
    subpixel True
    gensex_briding_D_center_pos
    #alpha myFuckinAlpha
    xzoom 0.65 yzoom 0.5 ypos -0.03 # High Top Anal
    block:
        easein 4.0/p_ao_n_vel xzoom 0.98 yzoom 0.84 ypos 0.55 # Almost IN
        ease 4.0/p_ao_n_vel xzoom 0.6 yzoom 0.5 ypos -0.03 # High Top Anal
        repeat

transform gensex_briding_n_open_anal_move_04:
    subpixel True
    gensex_briding_D_center_pos
    #alpha myFuckinAlpha
    xzoom 0.65 yzoom 0.5 ypos -0.03 # High Top Anal
    block:
        easein 4.0/p_ao_n_vel xzoom 1.0 yzoom 0.6 ypos 0.72 ## ALL IN
        ease 4.0/p_ao_n_vel xzoom 0.6 yzoom 0.5 ypos -0.03 # High Top Anal
        repeat

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##

image gensex_n_briding_comp vaginal_01: # Neus Introduction to Pussy.

    # contains:
    #     ConditionSwitch(gensex_briding_bg_Cond == "deepsea", At("gensex_briding_bg deepsea", gensex_briding_bg_trans),
    #                     gensex_briding_bg_Cond == "shore", At("gensex_briding_bg shore", gensex_briding_bg_trans),
    #                     "True", Null())

## BACKGROUND
    contains:
        # "gensex_oral_bg_grounddown"
        # truecenter
        # zoom 1.1
        "bg_ped_04"
        truecenter
        zoom 3.3

## MC BODY
    contains:
        "gensex_briding_MC_body"
        gensex_briding_D_center_pos

## HER BODY BELOW
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "nbVaginalRide_00", At("gensex_briding_n_body", gensex_briding_n_body_vaginal_move_00),
            p_ao_action_Cond == "nbVaginalRide_01", At("gensex_briding_n_body", gensex_briding_n_body_vaginal_move_01),
            p_ao_action_Cond == "nbVaginalRide_02", At("gensex_briding_n_body", gensex_briding_n_body_vaginal_move_02),
            p_ao_action_Cond == "nbVaginalRide_03", At("gensex_briding_n_body", gensex_briding_n_body_vaginal_move_03),
            p_ao_action_Cond == "nbVaginalRide_04", At("gensex_briding_n_body", gensex_briding_n_body_vaginal_move_04),
            p_ao_action_Cond == "nbAnalRide_00", At("gensex_briding_n_body", gensex_briding_n_body_Anal_move_00),
            p_ao_action_Cond == "nbAnalRide_01", At("gensex_briding_n_body", gensex_briding_n_body_Anal_move_01),
            p_ao_action_Cond == "nbAnalRide_02", At("gensex_briding_n_body", gensex_briding_n_body_Anal_move_02),
            p_ao_action_Cond == "nbAnalRide_03", At("gensex_briding_n_body", gensex_briding_n_body_Anal_move_03),
            p_ao_action_Cond == "nbAnalRide_04", At("gensex_briding_n_body", gensex_briding_n_body_Anal_move_04),

            "True", Null())

## HER CROTCH
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "nbVaginalRide_00", At("gensex_briding_n_legs_below_normal", gensex_briding_n_legs_movesVaginal_00),
            p_ao_action_Cond == "nbVaginalRide_01", At("gensex_briding_n_legs_below_normal", gensex_briding_n_legs_movesVaginal_01),
            p_ao_action_Cond == "nbVaginalRide_02", At("gensex_briding_n_legs_below_normal", gensex_briding_n_legs_movesVaginal_02),
            p_ao_action_Cond == "nbVaginalRide_03", At("gensex_briding_n_legs_below_normal", gensex_briding_n_legs_movesVaginal_03),
            p_ao_action_Cond == "nbVaginalRide_04", At("gensex_briding_n_legs_below_normal", gensex_briding_n_legs_movesVaginal_04),
            p_ao_action_Cond == "nbAnalRide_00", At("gensex_briding_n_legs_below_normal", gensex_briding_n_legs_movesAnal_00),
            p_ao_action_Cond == "nbAnalRide_01", At("gensex_briding_n_legs_below_normal", gensex_briding_n_legs_movesAnal_01),
            p_ao_action_Cond == "nbAnalRide_02", At("gensex_briding_n_legs_below_normal", gensex_briding_n_legs_movesAnal_02),
            p_ao_action_Cond == "nbAnalRide_03", At("gensex_briding_n_legs_below_normal", gensex_briding_n_legs_movesAnal_03),
            p_ao_action_Cond == "nbAnalRide_04", At("gensex_briding_n_legs_below_normal", gensex_briding_n_legs_movesAnal_04),
            "True", Null())

# MC CROTCH
    contains:
        "gensex_briding_MC_crotch"
        gensex_briding_D_center_pos

# Dick

    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["nbVaginalRide_00", "nbAnalRide_00"], At("gensex_briding_MC_dick_in_naked", gensex_briding_MC_dick_in_moveSlow_erect_n_00),
            p_ao_action_Cond in ["nbVaginalRide_01", "nbVaginalRide_02", "nbVaginalRide_03", "nbVaginalRide_04", "nbAnalRide_01", "nbAnalRide_02", "nbAnalRide_03", "nbAnalRide_04"], At("gensex_briding_MC_dick_in_naked", gensex_briding_MC_dick_in_moveSlow_erect_n_01),
            "True", At("gensex_briding_MC_dick_in_naked", gensex_briding_MC_dick_in_moveSlow_erect_n_base))

    # contains:
    #     "gensex_briding_MC_dick_in_naked"
    #     gensex_briding_MC_dick_in_moveSlow_erect_n_01

## HER BODY OVER
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "nbVaginalRide_00", At("gensex_briding_n_body_over", gensex_briding_n_body_vaginal_move_00),
            p_ao_action_Cond == "nbVaginalRide_01", At("gensex_briding_n_body_over", gensex_briding_n_body_vaginal_move_01),
            p_ao_action_Cond == "nbVaginalRide_02", At("gensex_briding_n_body_over", gensex_briding_n_body_vaginal_move_02),
            p_ao_action_Cond == "nbVaginalRide_03", At("gensex_briding_n_body_over", gensex_briding_n_body_vaginal_move_03),
            p_ao_action_Cond == "nbVaginalRide_04", At("gensex_briding_n_body_over", gensex_briding_n_body_vaginal_move_04),
            p_ao_action_Cond == "nbAnalRide_00", At("gensex_briding_n_body_over_b", gensex_briding_n_body_Anal_move_00),
            p_ao_action_Cond == "nbAnalRide_01", At("gensex_briding_n_body_over_b", gensex_briding_n_body_Anal_move_01),
            p_ao_action_Cond == "nbAnalRide_02", At("gensex_briding_n_body_over_b", gensex_briding_n_body_Anal_move_02),
            p_ao_action_Cond == "nbAnalRide_03", At("gensex_briding_n_body_over_b", gensex_briding_n_body_Anal_move_03),
            p_ao_action_Cond == "nbAnalRide_04", At("gensex_briding_n_body_over_b", gensex_briding_n_body_Anal_move_04),
            "True", Null())

    # contains:
    #     ConditionSwitch(aftermorning05_Deepsea_Fuck_AnalRAW_Cond == False, At("gensex_briding_D_body_over_b", gensex_briding_D_body_vaginal_move_01),
    #                     aftermorning05_Deepsea_Fuck_AnalRAW_Cond == True, At ("gensex_briding_D_body_over_b", gensex_briding_D_body_Anal_move_01),
    #         "True", Null())

## LEGS

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "nbVaginalRide_00", At("gensex_briding_n_legs_over_vaginal", gensex_briding_n_legs_movesVaginal_00),
            p_ao_action_Cond == "nbVaginalRide_01", At("gensex_briding_n_legs_over_vaginal", gensex_briding_n_legs_movesVaginal_01),
            p_ao_action_Cond == "nbVaginalRide_02", At("gensex_briding_n_legs_over_vaginal", gensex_briding_n_legs_movesVaginal_02),
            p_ao_action_Cond == "nbVaginalRide_03", At("gensex_briding_n_legs_over_vaginal", gensex_briding_n_legs_movesVaginal_03),
            p_ao_action_Cond == "nbVaginalRide_04", At("gensex_briding_n_legs_over_vaginal", gensex_briding_n_legs_movesVaginal_04),
            p_ao_action_Cond == "nbAnalRide_00", At("gensex_briding_n_legs_over_anal", gensex_briding_n_legs_movesAnal_00),
            p_ao_action_Cond == "nbAnalRide_01", At("gensex_briding_n_legs_over_anal", gensex_briding_n_legs_movesAnal_01),
            p_ao_action_Cond == "nbAnalRide_02", At("gensex_briding_n_legs_over_anal", gensex_briding_n_legs_movesAnal_02),
            p_ao_action_Cond == "nbAnalRide_03", At("gensex_briding_n_legs_over_anal", gensex_briding_n_legs_movesAnal_03),
            p_ao_action_Cond == "nbAnalRide_04", At("gensex_briding_n_legs_over_anal", gensex_briding_n_legs_movesAnal_04),
            "True", Null())

    # contains:
    #     ConditionSwitch(aftermorning05_Deepsea_Fuck_AnalRAW_Cond == False, At("gensex_briding_D_legs_over_vaginal", gensex_briding_D_legs_movesVaginal_01_),
    #                     aftermorning05_Deepsea_Fuck_AnalRAW_Cond == True, At ("gensex_briding_D_legs_over_anal", gensex_briding_D_legs_movesAnal_01),
    #         "True", Null())

## OPEN VAGINAL/ANAL

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "nbVaginalRide_00", At("gensex_briding_n_open_vaginal", gensex_briding_n_open_vaginal_move_00),
            p_ao_action_Cond == "nbVaginalRide_01", At("gensex_briding_n_open_vaginal", gensex_briding_n_open_vaginal_move_01),
            p_ao_action_Cond == "nbVaginalRide_02", At("gensex_briding_n_open_vaginal", gensex_briding_n_open_vaginal_move_02),
            p_ao_action_Cond == "nbVaginalRide_03", At("gensex_briding_n_open_vaginal", gensex_briding_n_open_vaginal_move_03),
            p_ao_action_Cond == "nbVaginalRide_04", At("gensex_briding_n_open_vaginal", gensex_briding_n_open_vaginal_move_04),
            p_ao_action_Cond == "nbAnalRide_00", At("gensex_briding_n_open_anal", gensex_briding_n_open_anal_move_00),
            p_ao_action_Cond == "nbAnalRide_01", At("gensex_briding_n_open_anal", gensex_briding_n_open_anal_move_01),
            p_ao_action_Cond == "nbAnalRide_02", At("gensex_briding_n_open_anal", gensex_briding_n_open_anal_move_02),
            p_ao_action_Cond == "nbAnalRide_03", At("gensex_briding_n_open_anal", gensex_briding_n_open_anal_move_03),
            p_ao_action_Cond == "nbAnalRide_04", At("gensex_briding_n_open_anal", gensex_briding_n_open_anal_move_04),
            "True", Null())

    # contains:
    #     ConditionSwitch(aftermorning05_Deepsea_Fuck_AnalRAW_Cond == False, At("gensex_briding_D_open_vaginal", gensex_briding_D_open_vaginal_move_01),
    #         aftermorning05_Deepsea_Fuck_AnalRAW_Cond == True, At ("gensex_briding_D_open_anal", gensex_briding_D_open_anal_move_01),
    #         "True", Null())

## BUTTOCK CHEECKS
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "nbVaginalRide_00", At("gensex_briding_n_legs_ass_vaginal", gensex_briding_n_legs_movesVaginal_00),
            p_ao_action_Cond == "nbVaginalRide_01", At("gensex_briding_n_legs_ass_vaginal", gensex_briding_n_legs_movesVaginal_01),
            p_ao_action_Cond == "nbVaginalRide_02", At("gensex_briding_n_legs_ass_vaginal", gensex_briding_n_legs_movesVaginal_02),
            p_ao_action_Cond == "nbVaginalRide_03", At("gensex_briding_n_legs_ass_vaginal", gensex_briding_n_legs_movesVaginal_03),
            p_ao_action_Cond == "nbVaginalRide_04", At("gensex_briding_n_legs_ass_vaginal", gensex_briding_n_legs_movesVaginal_04),
            p_ao_action_Cond == "nbAnalRide_00", At("gensex_briding_n_legs_movesAnal_00_cheecks_image", gensex_briding_n_legs_movesAnal_00_cheecks),
            p_ao_action_Cond == "nbAnalRide_01", At("gensex_briding_n_legs_ass_anal", gensex_briding_n_legs_movesAnal_01),
            p_ao_action_Cond == "nbAnalRide_02", At("gensex_briding_n_legs_ass_anal", gensex_briding_n_legs_movesAnal_02),
            p_ao_action_Cond == "nbAnalRide_03", At("gensex_briding_n_legs_ass_anal", gensex_briding_n_legs_movesAnal_03),
            p_ao_action_Cond == "nbAnalRide_04", At("gensex_briding_n_legs_ass_anal", gensex_briding_n_legs_movesAnal_04),
            ## aftermorning05_Deepsea_Fuck_AnalRAW_Cond == True, At ("gensex_briding_D_legs_ass_anal", gensex_briding_D_legs_movesAnal_01),
            "True", Null())

## MC LEGS
    contains:
        ConditionSwitch(
            p_ao_mc_legs == "stand", At("gensex_briding_MC_legs_down", gensex_briding_D_center_pos),
            "True", At("gensex_briding_MC_legs", gensex_briding_D_center_pos))

    # contains:
    #     "gensex_briding_MC_legs"
    #     gensex_briding_D_center_pos

    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_pos


######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##

image p_ao_sex_legup_back_down = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_legup_back_down.webp")
image p_ao_sex_legup_back_down_a = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_legup_back_down_a.webp")
image p_ao_sex_legup_back_down_b = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_legup_back_down_b.webp")
image p_ao_sex_legup_back_down_c = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_legup_back_down_b.webp")

image p_ao_sex_legup_back_up = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_legup_back_up.webp")
image p_ao_sex_legup_back_up_a = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_legup_back_up_a.webp")
image p_ao_sex_legup_back_up_b = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_legup_back_up_b.webp")
image p_ao_sex_legup_back_up_c = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_legup_back_up_b.webp")

image p_ao_sex_legup_back_moving_01:
    "p_ao_sex_legup_back_up"

    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_legup_back_down" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_legup_back_up" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_legup_back_moving_a:
    "p_ao_sex_legup_back_up"

    block:
        pause 3.5/p_ao_n_vel
        "p_ao_sex_legup_back_down_a" with Dissolve(2.0/p_ao_n_vel)
        pause 4.5/p_ao_n_vel
        "p_ao_sex_legup_back_up_a" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_legup_back_moving_b:
    "p_ao_sex_legup_back_up"

    block:
        pause 3.0/p_ao_n_vel
        "p_ao_sex_legup_back_down_b" with Dissolve(2.0/p_ao_n_vel)
        pause 5.0/p_ao_n_vel
        "p_ao_sex_legup_back_up_b" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_legup_back_moving_c:
    "p_ao_sex_legup_back_up"

    block:
        pause 3.0/p_ao_n_vel
        "p_ao_sex_legup_back_down_c" with Dissolve(2.0/p_ao_n_vel)
        pause 5.0/p_ao_n_vel
        "p_ao_sex_legup_back_up_c" with Dissolve(2.0/p_ao_n_vel)
        repeat

transform p_ao_sex_legup_back_ground_trans:
    truecenter
    zoom 1.3
    ypos 0.9

image p_ao_sex_legup_back_comp:

    contains:
        "gensex_oral_bg_grounddown"
        truecenter
        zoom 1.3
        ypos 0.9
        # "bg_ped_04"
        # truecenter
        # zoom 3.3

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 0.0 ypos 0.75 #DownLeft

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 1.0 ypos 0.75 # DownRight

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 0.0 ypos -0.25 rotate 180 #UpLeft

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 1.0 ypos -0.25 rotate 180 #UpRight

    contains:
        ConditionSwitch(
            p_ao_ground == "ground", At("gensex_oral_bg_grounddownMiddle", p_ao_sex_legup_back_ground_trans),
            "True", At("gensex_oral_bg_grounddownMiddle_bed", p_ao_sex_legup_back_ground_trans))

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "back_up", At("p_ao_sex_legup_back_up", truecenter),
            p_ao_action_Cond == "back_down", At("p_ao_sex_legup_back_down", truecenter),
            p_ao_action_Cond == "back_moving_01", At("p_ao_sex_legup_back_moving_01", truecenter),
            p_ao_action_Cond == "back_moving_a", At("p_ao_sex_legup_back_moving_a", truecenter),
            p_ao_action_Cond == "back_moving_b", At("p_ao_sex_legup_back_moving_b", truecenter),
            p_ao_action_Cond == "back_moving_c", At("p_ao_sex_legup_back_moving_c", truecenter),
            "True", Null())

# Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())


######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##

image p_ao_sex_doggy_side_fg = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_fg.webp")

image p_ao_sex_doggy_side_mc_body_ground = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_mc_body_ground.webp")
image p_ao_sex_doggy_side_mc_body_ground_tongue = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_mc_body_ground_tongue.webp")
image p_ao_sex_doggy_side_mc_body_up = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_mc_body_up.webp")
image p_ao_sex_doggy_side_mc_body_up_hair = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_mc_body_up_hair.webp")
image p_ao_sex_doggy_side_mc_legs = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_mc_legs[p_ao_n_blur].webp")

image p_ao_sex_doggy_side_n_back_armL = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_back_armL[p_ao_n_size][p_ao_n_blur].webp")
image p_ao_sex_doggy_side_n_back_armR = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_back_armR.webp")
image p_ao_sex_doggy_side_n_back_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_back_body[p_ao_n_size][p_ao_n_blur].webp")
image p_ao_sex_doggy_side_n_back_dick_her = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_back_dick_her[p_ao_n_size][p_ao_n_blur].webp")
image p_ao_sex_doggy_side_n_back_dick_his = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_back_dick_his[p_ao_n_size][p_ao_n_blur].webp")
image p_ao_sex_doggy_side_n_back_dick_stretched = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_back_dick_stretched.webp")
image p_ao_sex_doggy_side_n_back_horns = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_back_horns.webp")

image p_ao_sex_doggy_side_n_before_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_before_body.webp")
image p_ao_sex_doggy_side_n_before_dick = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_before_dick.webp")
image p_ao_sex_doggy_side_n_before_horns = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_before_horns.webp")
image p_ao_sex_doggy_side_n_before_armL = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_before_armL.webp")

image p_ao_sex_doggy_side_n_front_armL = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_front_armL[p_ao_n_size][p_ao_n_blur].webp")
image p_ao_sex_doggy_side_n_front_armR = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_front_armR.webp")
image p_ao_sex_doggy_side_n_front_armR_hair = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_front_armR_hair[p_ao_n_size].webp")
image p_ao_sex_doggy_side_n_front_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_front_body[p_ao_n_size][p_ao_n_blur].webp")
image p_ao_sex_doggy_side_n_front_horns = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_front_horns.webp")
image p_ao_sex_doggy_side_n_front_legHair = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_front_legHair.webp")
image p_ao_sex_doggy_side_n_front_tailLong = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_front_tailLong.webp")
image p_ao_sex_doggy_side_n_front_tailShort = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_front_tailShort.webp")
image p_ao_sex_doggy_side_n_front_wingsLong = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_front_wingsLong.webp")
image p_ao_sex_doggy_side_n_front_wingsShort = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_front_wingsShort.webp")
image p_ao_sex_doggy_side_n_leg_goat = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_leg_goat.webp")
image p_ao_sex_doggy_side_n_leg_human = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_leg_human.webp")
image p_ao_sex_doggy_side_n_leg_human_big = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_n_leg_human_big.webp")

image p_ao_sex_doggy_side_mc_lSmack_l01 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_mc_lSmack_l01.webp")
image p_ao_sex_doggy_side_mc_lSmack_l02 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_mc_lSmack_l02.webp")
image p_ao_sex_doggy_side_mc_lSmack_l03 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_mc_lSmack_l03.webp")
image p_ao_sex_doggy_side_mc_lSmack_l04 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_mc_lSmack_l04.webp")
image p_ao_sex_doggy_side_mc_lSmack_l05 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_side_mc_lSmack_l05.webp")



transform p_ao_sex_doggy_side_smack:
    subpixel True
    #"smack 02"
    truecenter
    additive 1.0
    #zoom 0.2 rotate 30 xpos 0.87 ypos 0.55 # Big
    zoom 0.01 rotate 20 xpos 0.82 ypos 0.6 # Small
    alpha 0.0
    parallel:
        easein_elastic 1.0 zoom 0.25 rotate 30 xpos 0.9 ypos 0.5 # Super Big
    parallel:
        easein_quad 0.3 alpha 1.0
        easein_quad 0.3 alpha 0.0

image before_back_mcDick_image:
    "p_ao_sex_doggy_side_n_before_body"
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_doggy_side_n_back_body" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_doggy_side_n_before_body" with Dissolve(2.0/p_ao_n_vel)
        repeat

image back_front_sex_hair_image:
    "p_ao_sex_doggy_side_n_back_body"
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_doggy_side_n_front_body" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_doggy_side_n_back_body" with Dissolve(2.0/p_ao_n_vel)
        repeat

image back_front_hardSex_hair_image:
    "p_ao_sex_doggy_side_n_back_body"
    block:
        pause 2.0/p_ao_n_vel
        "p_ao_sex_doggy_side_n_front_body" with Dissolve(2.0/p_ao_n_vel)
        pause 6.0/p_ao_n_vel
        "p_ao_sex_doggy_side_n_back_body" with Dissolve(2.0/p_ao_n_vel)
        repeat


image back_front_sex_hair_arm_image:
    "p_ao_sex_doggy_side_n_back_armL"
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_doggy_side_n_front_armL" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_doggy_side_n_back_armL" with Dissolve(2.0/p_ao_n_vel)
        repeat

image back_front_hardSex_hair_arm_image:
    "p_ao_sex_doggy_side_n_back_armL"
    block:
        pause 2.0/p_ao_n_vel
        "p_ao_sex_doggy_side_n_front_armL" with Dissolve(2.0/p_ao_n_vel)
        pause 6.0/p_ao_n_vel
        "p_ao_sex_doggy_side_n_back_armL" with Dissolve(2.0/p_ao_n_vel)
        repeat


## MC ASS:
transform p_ao_sex_doggy_side_mc_legs_sex_move:
    subpixel True
    #"p_ao_sex_doggy_side_mc_legs"
    truecenter
    block:
        easeout_quad 4.0/p_ao_n_vel xpos 0.5
        easein_quad 4.0/p_ao_n_vel xpos 0.49
        repeat

transform p_ao_sex_doggy_side_mc_legs_hardSex_move:
    subpixel True
    #"p_ao_sex_doggy_side_mc_legs"
    truecenter
    block:
        easeout_quad 2.0/p_ao_n_vel xpos 0.5
        easein_quad 6.0/p_ao_n_vel xpos 0.49
        repeat

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

image p_ao_sex_doggy_side_n_before_comp_01:

    # contains:
    #     "gensex_oral_bg_grounddown"
    #     truecenter
    #     zoom 1.35

    contains:
        #"gensex_oral_bg_grounddownMiddle"
        # "bg_dark_HD"
        # truecenter
        # zoom 1.35
        "bg_ped_04"
        truecenter
        zoom 3.5

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 1.02 ypos 1.0 # DownRight

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos -0.02 ypos 1.0 # DownLeft

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 1.02 ypos -0.031 rotate 180 # UpRight

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos -0.02 ypos -0.028 rotate 180 # UpLeft

## MC Dick
    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["before_mcDick", "back_mcDick", "before_back_mcDick", "back_tongue"], At("p_ao_sex_doggy_side_n_back_dick_stretched", truecenter),
            p_ao_action_Cond in ["back_front_sex_hair", "back_front_hardSex_hair", "back_front_hardSex", "back_front_sex","back_sex_hand", "front_sex_hand", "back_sex_hair", "front_sex_hair"], At("p_ao_sex_doggy_side_n_back_dick_his", truecenter),
            "True", Null())

# Neus Leg # Little
    contains:
        ConditionSwitch(
        p_ao_action_Cond == "", At("p_ao_sex_doggy_side_n_leg_human", truecenter),
        "True", Null())


## NEUS RIGHT ARM

    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["front_knot", "front_knot_slap", "back_front_sex_hair", "back_front_hardSex_hair", "back_sex_hair", "front_sex_hair"], At("p_ao_sex_doggy_side_n_front_armR_hair", truecenter),
            "True", Null())

## Neus Body

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "before_back_mcDick", At("before_back_mcDick_image", truecenter),
            p_ao_action_Cond in ["back_front_sex_hair", "back_front_sex"],At("back_front_sex_hair_image", truecenter),
            p_ao_action_Cond in ["back_front_hardSex_hair", "back_front_hardSex"], At("back_front_hardSex_hair_image", truecenter),
            p_ao_action_Cond in ["before_hand", "before_noHand", "before_mcDick"], At("p_ao_sex_doggy_side_n_before_body", truecenter),
            p_ao_action_Cond in ["back_hand", "back_noHand", "back_mcDick", "back_sex_hair", "back_sex_hand", "back_tongue"], At("p_ao_sex_doggy_side_n_back_body", truecenter),
            p_ao_action_Cond in ["front_hand", "front_noHand", "front_knot", "front_knot_slap", "front_sex_hand", "front_sex_hair"], At("p_ao_sex_doggy_side_n_front_body", truecenter),
            "True", Null())


## MC Body

    contains:
        ConditionSwitch(
        p_ao_action_Cond in ["front_knot", "front_knot_slap", "back_front_sex_hair", "back_front_hardSex_hair", "back_sex_hair", "front_sex_hair"], At("p_ao_sex_doggy_side_mc_body_up", truecenter),
        "Null", At("p_ao_sex_doggy_side_mc_body_ground", truecenter))

# Knot MC NECK

    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["front_knot", "front_knot_slap", "back_front_sex_hair", "back_front_hardSex_hair", "back_sex_hair", "front_sex_hair"], At("p_ao_sex_doggy_side_mc_body_up_hair", truecenter),
            "True", Null())


## MC Legs
    contains:
        ConditionSwitch(
        p_ao_action_Cond in ["back_front_sex_hair", "back_front_sex"], At("p_ao_sex_doggy_side_mc_legs", p_ao_sex_doggy_side_mc_legs_sex_move),
        p_ao_action_Cond in ["back_front_hardSex_hair", "back_front_hardSex"], At("p_ao_sex_doggy_side_mc_legs", p_ao_sex_doggy_side_mc_legs_hardSex_move),
        "Null", At("p_ao_sex_doggy_side_mc_legs", truecenter))


## SMACKS
    contains:
        ConditionSwitch(
            "l05" in p_ao_mcAssSmacks_list, At("p_ao_sex_doggy_side_mc_lSmack_l05", truecenter),
            "l04" in p_ao_mcAssSmacks_list, At("p_ao_sex_doggy_side_mc_lSmack_l04", truecenter),
            "l03" in p_ao_mcAssSmacks_list, At("p_ao_sex_doggy_side_mc_lSmack_l03", truecenter),
            "l02" in p_ao_mcAssSmacks_list, At("p_ao_sex_doggy_side_mc_lSmack_l02", truecenter),
            "l01" in p_ao_mcAssSmacks_list, At("p_ao_sex_doggy_side_mc_lSmack_l01", truecenter),
            "True", Null())


# LONG TONGUE
    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["back_tongue"], At("p_ao_sex_doggy_side_mc_body_ground_tongue", truecenter),
            "True", Null())

## SMASH Ass

    contains:
        ConditionSwitch(
            p_ao_assSmack == "lSmack", At("smack 02", p_ao_sex_doggy_side_smack),
            "True", Null())

## NEUS LEFT ARM

    contains:
        ConditionSwitch(
            p_ao_assSmack == "lSmack", Null(),
            p_ao_action_Cond in ["back_front_sex", "back_front_sex_hair"], At("back_front_sex_hair_arm_image", truecenter),
            p_ao_action_Cond in ["back_front_hardSex", "back_front_hardSex_hair"], At("back_front_hardSex_hair_arm_image", truecenter),
            p_ao_action_Cond in ["front_hand", "front_knot", "front_sex_hand"], At("p_ao_sex_doggy_side_n_front_armL", truecenter),
            p_ao_action_Cond in ["back_hand", "back_tongue", "back_sex_hand"], At("p_ao_sex_doggy_side_n_back_armL", truecenter),
            p_ao_action_Cond in ["before_hand"], At("p_ao_sex_doggy_side_n_before_armL", truecenter),
            "True", Null())

    # Neus Leg # Little
    contains:
        ConditionSwitch(
        p_ao_n_size == "_big", At("p_ao_sex_doggy_side_n_leg_human_big", truecenter),
        "True", Null())

    contains:
        "p_ao_sex_doggy_side_fg"
        truecenter

# Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##

## MC DOGGYSTYLE FRONT

image p_ao_sex_doggy_front_bg_bed = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_bg_bed.webp")

image p_ao_sex_doggy_front_mc_aSmack_l01 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_mc_aSmack_l01.webp")
image p_ao_sex_doggy_front_mc_aSmack_l02 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_mc_aSmack_l02.webp")
image p_ao_sex_doggy_front_mc_aSmack_l03 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_mc_aSmack_l03.webp")
image p_ao_sex_doggy_front_mc_aSmack_l04 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_mc_aSmack_l04.webp")
image p_ao_sex_doggy_front_mc_aSmack_l05 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_mc_aSmack_l05.webp")

image p_ao_sex_doggy_front_mc_aSmack_r01 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_mc_aSmack_r01.webp")
image p_ao_sex_doggy_front_mc_aSmack_r02 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_mc_aSmack_r02.webp")
image p_ao_sex_doggy_front_mc_aSmack_r03 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_mc_aSmack_r03.webp")
image p_ao_sex_doggy_front_mc_aSmack_r04 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_mc_aSmack_r04.webp")
image p_ao_sex_doggy_front_mc_aSmack_r05 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_mc_aSmack_r05.webp")

image p_ao_sex_doggy_front_mc_ass = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_mc_ass.webp")
image p_ao_sex_doggy_front_mc_back = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_mc_back.webp")
image p_ao_sex_doggy_front_mc_front = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_mc_front.webp")


image p_ao_sex_doggy_front_n_hands = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_n_hands[p_ao_n_size].webp")


image p_ao_sex_doggy_front_n_body_back = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_n_body_back[p_ao_n_size].webp")
image p_ao_sex_doggy_front_n_back_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_n_back_body[p_ao_n_size][neyesp].webp")
image p_ao_sex_doggy_front_n_back_l_iris = "images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_n_back_l_iris[p_ao_n_size].webp"
image p_ao_sex_doggy_front_n_back_iLight = "images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_n_back_iLight[p_ao_n_size].webp"
image p_ao_sex_doggy_front_n_back_hairFront = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_n_back_hairFront[p_ao_n_size].webp")


#image p_ao_sex_doggy_front_n_body_ahead = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_n_body_ahead[p_ao_n_size].webp")
image p_ao_sex_doggy_front_n_front_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_n_front_body[p_ao_n_size][neyesp].webp")
image p_ao_sex_doggy_front_n_front_l_iris = "images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_n_front_l_iris[p_ao_n_size].webp"
image p_ao_sex_doggy_front_n_front_iLight = "images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_n_front_iLight[p_ao_n_size].webp"
image p_ao_sex_doggy_front_n_front_hairFront = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_n_front_hairFront[p_ao_n_size].webp") 

image p_ao_sex_doggy_front_TEST = "images/day05/pedrera/afterOrgasm/p_ao_sex_doggy_front_TEST.webp"

######################################################################################################
######################################################################################################


## LEFT Smack Ass
transform p_ao_sex_doggy_front_lSmack:
    subpixel True
    #"smack 02"
    truecenter
    additive 1.0
    zoom 0.02 rotate 10 xpos 0.65 ypos 0.55 # Small
    parallel:
        easein_bounce 0.5 zoom 0.22 rotate 25 xpos 0.72 ypos 0.45 # Big
    parallel:
        easein_quad 0.05 alpha 1.0
        easein_quad 0.4 alpha 0.0

## RIGHT Smack Ass

transform p_ao_sex_doggy_front_rSmack:
    subpixel True
    #"smack 02"
    # Should I change the Ypos? since in theory was designed for ypos 0.5 (and now is 0.706)
    truecenter
    additive 1.0
    zoom 0.02 rotate -10 xpos 0.35 ypos 0.55 # Small
    parallel:
        easein_bounce 0.5 zoom 0.22 rotate -25 xpos 0.3 ypos 0.45 # Big
    parallel:
        easein_quad 0.05 alpha 1.0
        easein_quad 0.4 alpha 0.0

    #zoom 0.22 rotate -25 xpos 0.3 ypos 0.45 # Big
    # zoom 0.02 rotate -10 xpos 0.35 ypos 0.55 # Small

image p_ao_sex_doggy_front_smack_effect:
    truecenter
    zoom 2.0
    additive 1.0
    alpha 0.5
    "hit 09"
    pause 0.05
    "hit 10"
    pause 0.05
    "hit 22"
    pause 0.05
    "hit 23"
    pause 0.05
    alpha 0.0

transform p_ao_sex_doggy_front_n_l_iris_pos:
    subpixel True
    truecenter
    alpha ped_neus_whispers_sfx04

transform p_ao_sex_doggy_front_n_iLight_pos:
    subpixel True
    truecenter
    additive 1.0
    alpha ped_neus_whispers_sfx04

# Normal Sex

image p_ao_sex_doggy_front_n_body_FrontSex:
    "p_ao_sex_doggy_front_n_back_body"
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_doggy_front_n_front_body" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_doggy_front_n_back_body" with Dissolve(2.0/p_ao_n_vel)
        repeat


image p_ao_sex_doggy_front_n_l_iris_FrontSex:
    alpha ped_neus_whispers_sfx04
    "p_ao_sex_doggy_front_n_back_l_iris"
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_doggy_front_n_front_l_iris" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_doggy_front_n_back_l_iris" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_doggy_front_n_iLight_FrontSex:
    alpha ped_neus_whispers_sfx04
    additive 1.0
    "p_ao_sex_doggy_front_n_back_iLight"
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_doggy_front_n_front_iLight" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_doggy_front_n_back_iLight" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_doggy_front_n_hairFront_FrontSex:
    "p_ao_sex_doggy_front_n_back_hairFront"
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_doggy_front_n_front_hairFront" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_doggy_front_n_back_hairFront" with Dissolve(2.0/p_ao_n_vel)
        repeat


## Hard Sex

image p_ao_sex_doggy_front_n_body_FrontHardSex:
    "p_ao_sex_doggy_front_n_back_body"
    block:
        pause 2.0/p_ao_n_vel
        "p_ao_sex_doggy_front_n_front_body" with Dissolve(2.0/p_ao_n_vel)
        pause 6.0/p_ao_n_vel
        "p_ao_sex_doggy_front_n_back_body" with Dissolve(2.0/p_ao_n_vel)
        repeat


image p_ao_sex_doggy_front_n_l_iris_FrontHardSex:
    alpha ped_neus_whispers_sfx04
    "p_ao_sex_doggy_front_n_back_l_iris"
    block:
        pause 2.0/p_ao_n_vel
        "p_ao_sex_doggy_front_n_front_l_iris" with Dissolve(2.0/p_ao_n_vel)
        pause 6.0/p_ao_n_vel
        "p_ao_sex_doggy_front_n_back_l_iris" with Dissolve(2.0/p_ao_n_vel)
        repeat


image p_ao_sex_doggy_front_n_iLight_FrontHardSex:
    alpha ped_neus_whispers_sfx04
    additive 1.0
    "p_ao_sex_doggy_front_n_back_iLight"
    block:
        pause 2.0/p_ao_n_vel
        "p_ao_sex_doggy_front_n_front_iLight" with Dissolve(2.0/p_ao_n_vel)
        pause 6.0/p_ao_n_vel
        "p_ao_sex_doggy_front_n_back_iLight" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_doggy_front_n_hairFront_FrontHardSex:
    "p_ao_sex_doggy_front_n_back_hairFront"
    block:
        pause 2.0/p_ao_n_vel
        "p_ao_sex_doggy_front_n_front_hairFront" with Dissolve(2.0/p_ao_n_vel)
        pause 6.0/p_ao_n_vel
        "p_ao_sex_doggy_front_n_back_hairFront" with Dissolve(2.0/p_ao_n_vel)
        repeat

############################################################################################################
############################################################################################################
##########################################################################################
############################################################################################################
############################################################################################################


transform p_ao_sex_doggy_front_mc_pos:
    truecenter
    ypos 0.706

image p_ao_sex_doggy_front_comp_01:

    contains:
        #"gensex_oral_bg_grounddownMiddle"
        "bg_dark_HD"
        truecenter
        zoom 1.35

## GHOSTS

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 0.0 ypos 0.75 #DownLeft

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 1.0 ypos 0.75 # DownRight

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 0.0 ypos -0.25 rotate 180 #UpLeft

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 1.0 ypos -0.25 rotate 180 #UpRight


## BACKGROUND bed.
    contains:
        "p_ao_sex_doggy_front_bg_bed"
        truecenter

## Neus Body

    contains:
        ConditionSwitch(
        p_ao_action_Cond in ["back_front_sex_hair", "back_front_sex"], At("p_ao_sex_doggy_front_n_body_FrontSex", truecenter),
        p_ao_action_Cond in ["back_front_hardSex_hair", "back_front_hardSex"], At("p_ao_sex_doggy_front_n_body_FrontSex", truecenter),
        p_ao_action_Cond in ["back_front_Hardsex"], At("p_ao_sex_doggy_front_n_body_FrontHardSex", truecenter),
        p_ao_action_Cond in ["ahead_hand", "ahead_noHand"], At("p_ao_sex_doggy_front_n_front_body", truecenter),
        "True", At("p_ao_sex_doggy_front_n_back_body", truecenter))


## Neus l_iris

    contains:
        ConditionSwitch(
        p_ao_action_Cond in ["back_front_sex_hair", "back_front_sex"], At("p_ao_sex_doggy_front_n_l_iris_FrontSex", truecenter),
        p_ao_action_Cond in ["back_front_hardSex_hair", "back_front_hardSex"], At("p_ao_sex_doggy_front_n_l_iris_FrontSex", truecenter),
        p_ao_action_Cond in ["back_front_Hardsex"], At("p_ao_sex_doggy_front_n_l_iris_FrontHardSex", truecenter),
        p_ao_action_Cond in ["ahead_hand", "ahead_noHand"], At("p_ao_sex_doggy_front_n_front_l_iris", p_ao_sex_doggy_front_n_l_iris_pos),
        "True", At("p_ao_sex_doggy_front_n_back_l_iris", p_ao_sex_doggy_front_n_l_iris_pos))

## Neus iLight

    contains:
        ConditionSwitch(
        p_ao_action_Cond in ["back_front_sex_hair", "back_front_sex"], At("p_ao_sex_doggy_front_n_iLight_FrontSex", truecenter),
        p_ao_action_Cond in ["back_front_hardSex_hair", "back_front_hardSex"], At("p_ao_sex_doggy_front_n_iLight_FrontSex", truecenter),
        p_ao_action_Cond in ["back_front_Hardsex"], At("p_ao_sex_doggy_front_n_iLight_FrontHardSex", truecenter),
        p_ao_action_Cond in ["ahead_hand", "ahead_noHand"], At("p_ao_sex_doggy_front_n_front_iLight", p_ao_sex_doggy_front_n_iLight_pos),
        "True", At("p_ao_sex_doggy_front_n_back_iLight", p_ao_sex_doggy_front_n_iLight_pos))


## Neus HairFront

    contains:
        ConditionSwitch(
        p_ao_action_Cond in ["back_front_sex_hair", "back_front_sex"], At("p_ao_sex_doggy_front_n_hairFront_FrontSex", truecenter),
        p_ao_action_Cond in ["back_front_hardSex_hair", "back_front_hardSex"], At("p_ao_sex_doggy_front_n_hairFront_FrontSex", truecenter),
        p_ao_action_Cond in ["back_front_Hardsex"], At("p_ao_sex_doggy_front_n_hairFront_FrontHardSex", truecenter),
        p_ao_action_Cond in ["ahead_hand", "ahead_noHand"], At("p_ao_sex_doggy_front_n_front_hairFront", truecenter),
        "True", At("p_ao_sex_doggy_front_n_back_hairFront", truecenter))

##MC ASS

    contains:
        "p_ao_sex_doggy_front_mc_ass"
        p_ao_sex_doggy_front_mc_pos


# MC LEFT Smacks ASS
    contains:
        ConditionSwitch(
            "l05" in p_ao_mcAssSmacks_list, At("p_ao_sex_doggy_front_mc_aSmack_l05", p_ao_sex_doggy_front_mc_pos),
            "l04" in p_ao_mcAssSmacks_list, At("p_ao_sex_doggy_front_mc_aSmack_l04", p_ao_sex_doggy_front_mc_pos),
            "l03" in p_ao_mcAssSmacks_list, At("p_ao_sex_doggy_front_mc_aSmack_l03", p_ao_sex_doggy_front_mc_pos),
            "l02" in p_ao_mcAssSmacks_list, At("p_ao_sex_doggy_front_mc_aSmack_l02", p_ao_sex_doggy_front_mc_pos),
            "l01" in p_ao_mcAssSmacks_list, At("p_ao_sex_doggy_front_mc_aSmack_l01", p_ao_sex_doggy_front_mc_pos),
            "True", Null())

# MC RIGHT Smacks ASS
    contains:
        ConditionSwitch(
            "r05" in p_ao_mcAssSmacks_list, At("p_ao_sex_doggy_front_mc_aSmack_r05", p_ao_sex_doggy_front_mc_pos),
            "r04" in p_ao_mcAssSmacks_list, At("p_ao_sex_doggy_front_mc_aSmack_r04", p_ao_sex_doggy_front_mc_pos),
            "r03" in p_ao_mcAssSmacks_list, At("p_ao_sex_doggy_front_mc_aSmack_r03", p_ao_sex_doggy_front_mc_pos),
            "r02" in p_ao_mcAssSmacks_list, At("p_ao_sex_doggy_front_mc_aSmack_r02", p_ao_sex_doggy_front_mc_pos),
            "r01" in p_ao_mcAssSmacks_list, At("p_ao_sex_doggy_front_mc_aSmack_r01", p_ao_sex_doggy_front_mc_pos),
            "True", Null())

## Neus Fingers:

    contains:
        ConditionSwitch(
            p_ao_assSmack in ["rSmack", "lSmack"], Null(),
            p_ao_action_Cond in ["ahead_hands", "back_hands", "back_front_hardSex", "back_front_sex"], At("p_ao_sex_doggy_front_n_hands", truecenter),
            "True", Null())

# MC BACK

    contains:
        "p_ao_sex_doggy_front_mc_back"
        p_ao_sex_doggy_front_mc_pos

# MC FRONT

    contains:
        "p_ao_sex_doggy_front_mc_front"
        p_ao_sex_doggy_front_mc_pos

## RIGHT-LEFT Smack Ass

    contains:
        ConditionSwitch(
            p_ao_assSmack == "lSmack", At("smack 02", p_ao_sex_doggy_front_lSmack),
            p_ao_assSmack == "rSmack", At("smack 02", p_ao_sex_doggy_front_rSmack),
            "True", Null())

## Smack Effect
    # contains:
    #     ConditionSwitch(
    #         p_ao_assSmack in ["lSmack", "rSmack"], At("p_ao_sex_doggy_front_smack_effect", p_ao_sex_doggy_front_mc_pos),
    #         "True", Null())

# Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())

    # contains:
    #     "p_ao_sex_doggy_front_TEST"
    #     truecenter
    #     alpha 0.5


######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##

image p_ao_sex_amazon_front_dick = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_dick.webp") #This is gonna be removed.
image p_ao_sex_amazon_front_mc_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_mc_body.webp")
image p_ao_sex_amazon_front_mc_legs = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_mc_legs.webp")
image p_ao_sex_amazon_front_mc_bed = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_mc_bed.webp")


## FEET
    #body
image p_ao_sex_amazon_front_n_feet_body_01 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_body[p_ao_n_fur]_01.webp")
image p_ao_sex_amazon_front_n_feet_body_02 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_body[p_ao_n_fur]_02.webp")
image p_ao_sex_amazon_front_n_feet_body_03 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_body[p_ao_n_fur]_03.webp")
image p_ao_sex_amazon_front_n_feet_body_04 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_body[p_ao_n_fur]_04.webp")

    # iLight
image p_ao_sex_amazon_front_n_feet_iLight_01 = "images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_iLight_01.webp"
image p_ao_sex_amazon_front_n_feet_iLight_02 = "images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_iLight_02.webp"
image p_ao_sex_amazon_front_n_feet_iLight_03 = "images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_iLight_03.webp"
image p_ao_sex_amazon_front_n_feet_iLight_04 = "images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_iLight_04.webp"
    # l_iris
image p_ao_sex_amazon_front_n_feet_l_iris_01 = "images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_l_iris_01.webp"
image p_ao_sex_amazon_front_n_feet_l_iris_02 = "images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_l_iris_02.webp"
image p_ao_sex_amazon_front_n_feet_l_iris_03 = "images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_l_iris_03.webp"
image p_ao_sex_amazon_front_n_feet_l_iris_04 = "images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_l_iris_04.webp"
    # over
image p_ao_sex_amazon_front_n_feet_over_01 = Null(width=800, height=600)
image p_ao_sex_amazon_front_n_feet_over_02 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_over[p_ao_sexPart]_02.webp")
image p_ao_sex_amazon_front_n_feet_over_03 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_over[p_ao_sexPart]_03.webp")
image p_ao_sex_amazon_front_n_feet_over_04 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_over_v_04.webp")
    # wings and Tail
image p_ao_sex_amazon_front_n_feet_wings_01 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_wings_01.webp")
image p_ao_sex_amazon_front_n_feet_wings_02 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_wings_02.webp")
image p_ao_sex_amazon_front_n_feet_wings_03 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_wings_03.webp")
image p_ao_sex_amazon_front_n_feet_wings_04 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_wings_04.webp")
    # tail Alone
image p_ao_sex_amazon_front_n_feet_tail_01 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_tail_01.webp")
image p_ao_sex_amazon_front_n_feet_tail_02 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_tail_02.webp")
image p_ao_sex_amazon_front_n_feet_tail_03 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_tail_03.webp")
image p_ao_sex_amazon_front_n_feet_tail_04 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_feet_tail_04.webp")

    # tongue

image p_ao_sex_amazon_front_n_tongue_l_02 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_tongue_l_02.webp")

    # TongueDick

image p_ao_sex_amazon_front_n_tongue_dick_00 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_tongue_dick_01.webp")
image p_ao_sex_amazon_front_n_tongue_dick_01 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_tongue_dick_01.webp")
image p_ao_sex_amazon_front_n_tongue_dick_02 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_tongue_dick_02.webp")
image p_ao_sex_amazon_front_n_tongue_dick_03 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_tongue_dick_03.webp")
image p_ao_sex_amazon_front_n_tongue_dick_04 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_tongue_dick_04.webp")
image p_ao_sex_amazon_front_n_tongue_dick_05 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_tongue_dick_05.webp")
image p_ao_sex_amazon_front_n_tongue_dick_06 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_tongue_dick_06.webp")

############################

image p_ao_sex_amazon_front_n_thigh_01 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_thigh_01.webp")
image p_ao_sex_amazon_front_n_thigh_02 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_thigh_02.webp")
image p_ao_sex_amazon_front_n_thigh_03 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_thigh_03.webp")
##############################

#image p_ao_sex_amazon_front_n_wings == Null(width=800, height=600)
image p_ao_sex_amazon_front_n_wings_xx = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_wings_[p_ao_n_wings].webp")
image p_ao_sex_amazon_front_n_wings_xxx = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_wings_[p_ao_n_wings].webp")

#image p_ao_sex_amazon_front_n_tail_xx = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_tail_[p_ao_n_tail].webp")


image p_ao_sex_amazon_front_n_wings_00 = Null(width=800, height=600)
image p_ao_sex_amazon_front_n_wings_01 = Null(width=800, height=600)
image p_ao_sex_amazon_front_n_wings_02 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_wings_02.webp")
image p_ao_sex_amazon_front_n_wings_03 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_wings_03.webp")
image p_ao_sex_amazon_front_n_wings_04 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_wings_04.webp")
image p_ao_sex_amazon_front_n_wings_05 = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_wings_05.webp")

image p_ao_sex_amazon_front_n_wings_TEST = "images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_front_n_wings_TEST.webp"


# WINGS AND TAIL
image p_ao_sex_amazon_front_n_feet_wings_image_01:
    contains:
        "p_ao_sex_amazon_front_n_wings_xx"
        p_ao_sex_amazon_front_n_wings_feet_01_pos

image p_ao_sex_amazon_front_n_feet_wings_image_02:
    contains:
        "p_ao_sex_amazon_front_n_wings_xx"
        p_ao_sex_amazon_front_n_wings_feet_02_pos

image p_ao_sex_amazon_front_n_feet_wings_image_03:
    contains:
        "p_ao_sex_amazon_front_n_wings_xx"
        p_ao_sex_amazon_front_n_wings_feet_03_pos

image p_ao_sex_amazon_front_n_feet_wings_image_04:
    contains:
        "p_ao_sex_amazon_front_n_wings_xx"
        p_ao_sex_amazon_front_n_wings_feet_04_pos

# ## TAIL
# image p_ao_sex_amazon_front_n_feet_tail_image_01:
#     contains:
#         "p_ao_sex_amazon_front_n_tail_xx"
#         p_ao_sex_amazon_front_n_wings_feet_01_pos

# image p_ao_sex_amazon_front_n_feet_tail_image_02:
#     contains:
#         "p_ao_sex_amazon_front_n_tail_xx"
#         p_ao_sex_amazon_front_n_wings_feet_02_pos

# image p_ao_sex_amazon_front_n_feet_tail_image_03:
#     contains:
#         "p_ao_sex_amazon_front_n_tail_xx"
#         p_ao_sex_amazon_front_n_wings_feet_03_pos

# image p_ao_sex_amazon_front_n_feet_tail_image_04:
#     contains:
#         "p_ao_sex_amazon_front_n_tail_xx"
#         p_ao_sex_amazon_front_n_wings_feet_04_pos


transform p_ao_sex_amazon_front_n_wings_feet_01_pos:
    truecenter
    ypos 0.04

transform p_ao_sex_amazon_front_n_wings_feet_02_pos:
    truecenter
    ypos 0.12

transform p_ao_sex_amazon_front_n_wings_feet_03_pos:
    truecenter
    ypos 0.26

transform p_ao_sex_amazon_front_n_wings_feet_04_pos:
    truecenter
    ypos 0.5


# image p_ao_sex_amazon_front_n_feet_wings_test_01 = ("p_ao_sex_amazon_front_n_wings_01")
#     "p_ao_sex_amazon_front_n_wings_01"
#     p_ao_sex_amazon_front_n_wings_feet_01_pos

######################################################################################################
######################################################################################################

image p_ao_sex_amazon_front_comp_01:

    contains:
        "bg_dark_HD"
        truecenter
        zoom 1.35

###
    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 0.0 ypos 0.75 #DownLeft

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 1.0 ypos 0.75 # DownRight

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 0.0 ypos -0.25 rotate 180 #UpLeft

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 1.0 ypos -0.25 rotate 180 #UpRight
###

    contains:
        "p_ao_sex_amazon_front_mc_bed"
        truecenter

    contains:
        "p_ao_sex_amazon_front_mc_legs"
        truecenter

    contains:
        "p_ao_sex_amazon_front_mc_body"
        truecenter

    contains:
        "p_ao_sex_amazon_front_n_feet_body_04"
        truecenter
# Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())

######################################################################################################
######################################################################################################

# Dick Hard = 06
transform p_ao_sex_amazon_front_dick_hard:
    #"gensex_oral_mc_dick_b_01_wet_00"
    transform_anchor True
    xalign 0.5 yalign 0.78 
    zoom 0.21 xpos 0.504 ypos 0.96 rotate 0

# Dick = 05
transform p_ao_sex_amazon_front_dick_05:
    #"gensex_oral_mc_dick_b_01_wet_00"
    transform_anchor True
    xalign 0.5 yalign 0.78 
    xzoom 0.2 yzoom 0.18 xpos 0.504 ypos 0.96 rotate 0

# Dick = 04
transform p_ao_sex_amazon_front_dick_04:
    #"gensex_oral_mc_dick_b_01_wet_00"
    transform_anchor True
    xalign 0.5 yalign 0.78 
    xzoom 0.19 yzoom 0.15 xpos 0.504 ypos 0.96 rotate 0

# Dick = 03
transform p_ao_sex_amazon_front_dick_03:
    #"gensex_oral_mc_dick_b_01_wet_00"
    transform_anchor True
    xalign 0.5 yalign 0.78 
    xzoom 0.18 yzoom 0.13 xpos 0.504 ypos 0.96 rotate 0

# Dick = 02
transform p_ao_sex_amazon_front_dick_02:
    #"gensex_oral_mc_dick_b_01_wet_00"
    transform_anchor True
    xalign 0.5 yalign 0.78 
    xzoom 0.17 yzoom 0.10 xpos 0.504 ypos 0.96 rotate 0

# Dick = 01
transform p_ao_sex_amazon_front_dick_01:
    #"gensex_oral_mc_dick_b_01_wet_00"
    transform_anchor True
    xalign 0.5 yalign 0.78 
    xzoom 0.17 yzoom 0.08 xpos 0.504 ypos 0.96 rotate 0

# Dick = 00
transform p_ao_sex_amazon_front_dick_00:
    #"gensex_oral_mc_dick_b_01_wet_00"
    transform_anchor True
    xalign 0.5 yalign 0.78 
    xzoom 0.16 yzoom 0.05 xpos 0.504 ypos 0.96 rotate 0



image p_ao_sex_amazon_front_n_feet_body_01_04:
    "p_ao_sex_amazon_front_n_feet_body_01"
    truecenter
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_body_02" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_body_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_body_04" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_body_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_body_02" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_body_01" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_amazon_front_n_feet_over_01_04:
    "p_ao_sex_amazon_front_n_feet_over_01"
    truecenter
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_over_02" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_over_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_over_04" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_over_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_over_02" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_over_01" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_amazon_front_n_feet_wings_01_04:
    "p_ao_sex_amazon_front_n_feet_wings_01"
    truecenter
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_wings_02" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_wings_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_wings_04" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_wings_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_wings_02" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_wings_01" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_amazon_front_n_feet_tail_01_04:
    "p_ao_sex_amazon_front_n_feet_tail_01"
    truecenter
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_tail_02" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_tail_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_tail_04" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_tail_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_tail_02" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_tail_01" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_amazon_front_n_feet_l_iris_01_04:
    "p_ao_sex_amazon_front_n_feet_l_iris_01"
    truecenter
    alpha ped_neus_whispers_sfx04
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_l_iris_02" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_l_iris_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_l_iris_04" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_l_iris_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_l_iris_02" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_l_iris_01" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_amazon_front_n_feet_iLight_01_04:
    "p_ao_sex_amazon_front_n_feet_iLight_01"
    truecenter
    additive 1.0
    alpha ped_neus_whispers_sfx04
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_iLight_02" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_iLight_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_iLight_04" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_iLight_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_iLight_02" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_iLight_01" with Dissolve(2.0/p_ao_n_vel)
        repeat

transform p_ao_sex_amazon_front_n_feet_iLight_truecenter:
    subpixel True
    truecenter
    additive 1.0
    alpha ped_neus_whispers_sfx04



######################################## 02_04

image p_ao_sex_amazon_front_n_feet_body_02_04:
    "p_ao_sex_amazon_front_n_feet_body_02"
    truecenter

    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_body_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_body_04" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_body_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_body_02" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_amazon_front_n_feet_over_02_04:
    "p_ao_sex_amazon_front_n_feet_over_02"
    truecenter

    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_over_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_over_04" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_over_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_over_02" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_amazon_front_n_feet_wings_02_04:
    "p_ao_sex_amazon_front_n_feet_wings_02" with Dissolve(2.0/p_ao_n_vel)
    truecenter
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_wings_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_wings_04" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_wings_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_wings_02" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_amazon_front_n_feet_tail_02_04:
    "p_ao_sex_amazon_front_n_feet_tail_02" with Dissolve(2.0/p_ao_n_vel)
    truecenter
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_tail_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_tail_04" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_tail_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_tail_02" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_amazon_front_n_feet_l_iris_02_04:
    "p_ao_sex_amazon_front_n_feet_l_iris_02" with Dissolve(2.0/p_ao_n_vel)
    truecenter
    alpha ped_neus_whispers_sfx04
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_l_iris_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_l_iris_04" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_l_iris_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_l_iris_02" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_amazon_front_n_feet_iLight_02_04:
    "p_ao_sex_amazon_front_n_feet_iLight_02" with Dissolve(2.0/p_ao_n_vel)
    truecenter
    additive 1.0
    alpha ped_neus_whispers_sfx04
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_iLight_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_iLight_04" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_iLight_03" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_iLight_02" with Dissolve(2.0/p_ao_n_vel)
        repeat


##### 03_04

image p_ao_sex_amazon_front_n_feet_l_iris_03_04:
    "p_ao_sex_amazon_front_n_feet_l_iris_03" with Dissolve(2.0/p_ao_n_vel)
    truecenter
    alpha ped_neus_whispers_sfx04
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_l_iris_04" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_l_iris_03" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_amazon_front_n_feet_iLight_03_04:
    "p_ao_sex_amazon_front_n_feet_iLight_03" with Dissolve(2.0/p_ao_n_vel)
    truecenter
    additive 1.0
    alpha ped_neus_whispers_sfx04
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_iLight_04" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_iLight_03" with Dissolve(2.0/p_ao_n_vel)
        repeat

image p_ao_sex_amazon_front_n_feet_body_03_04:
    "p_ao_sex_amazon_front_n_feet_body_03"
    truecenter

    block:
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_body_04" with Dissolve(2.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_sex_amazon_front_n_feet_body_03" with Dissolve(2.0/p_ao_n_vel)
        repeat

# image p_ao_sex_amazon_front_n_feet_body_01_02:
#     "p_ao_sex_amazon_front_n_feet_body_01"
#     truecenter

#     block:
#         pause 4.0/p_ao_n_vel
#         "p_ao_sex_amazon_front_n_feet_body_02" with Dissolve(2.0/p_ao_n_vel)
#         pause 4.0/p_ao_n_vel
#         "p_ao_sex_amazon_front_n_feet_body_01" with Dissolve(2.0/p_ao_n_vel)
#         repeat

# image p_ao_sex_amazon_front_n_feet_body_02_03:
#     "p_ao_sex_amazon_front_n_feet_body_02"
#     truecenter

#     block:
#         pause 4.0/p_ao_n_vel
#         "p_ao_sex_amazon_front_n_feet_body_02" with Dissolve(2.0/p_ao_n_vel)
#         pause 4.0/p_ao_n_vel
#         "p_ao_sex_amazon_front_n_feet_body_03" with Dissolve(2.0/p_ao_n_vel)
#         repeat


#####################
transform p_ao_sex_amazon_front_n_tongue_dick_gen:
    transform_anchor True
    xalign 0.5 yalign 0.86
    xpos 0.5 ypos 0.94

transform p_ao_sex_amazon_front_n_tongue_dick_00_trans:
    subpixel True
    p_ao_sex_amazon_front_n_tongue_dick_gen
    zoom 0.85
    block:
        easein 4.0/p_ao_n_vel ypos 0.94
        easeout 4.0/p_ao_n_vel ypos 0.95
        repeat

transform p_ao_sex_amazon_front_n_tongue_dick_01_trans:
    subpixel True
    p_ao_sex_amazon_front_n_tongue_dick_gen
    block:
        easein 4.0/p_ao_n_vel ypos 0.9
        easeout 4.0/p_ao_n_vel ypos 0.94
        repeat

transform p_ao_sex_amazon_front_n_tongue_dick_02_trans:
    subpixel True
    p_ao_sex_amazon_front_n_tongue_dick_gen
    block:
        easein 4.0/p_ao_n_vel ypos 0.88
        easeout 4.0/p_ao_n_vel ypos 0.94
        repeat

transform p_ao_sex_amazon_front_n_tongue_dick_03_trans:
    subpixel True
    p_ao_sex_amazon_front_n_tongue_dick_gen
    block:
        easein 4.0/p_ao_n_vel ypos 0.84
        easeout 4.0/p_ao_n_vel ypos 0.94
        repeat

transform p_ao_sex_amazon_front_n_tongue_dick_04_trans:
    subpixel True
    p_ao_sex_amazon_front_n_tongue_dick_gen
    block:
        easein 4.0/p_ao_n_vel ypos 0.83
        easeout 4.0/p_ao_n_vel ypos 0.94
        repeat

transform p_ao_sex_amazon_front_n_tongue_dick_05_trans:
    subpixel True
    p_ao_sex_amazon_front_n_tongue_dick_gen
    block:
        easein 4.0/p_ao_n_vel ypos 0.8
        easeout 4.0/p_ao_n_vel ypos 0.94
        repeat

transform p_ao_sex_amazon_front_n_tongue_dick_06_trans:
    subpixel True
    p_ao_sex_amazon_front_n_tongue_dick_gen
    block:
        easein 4.0/p_ao_n_vel ypos 0.77
        easeout 4.0/p_ao_n_vel ypos 0.94
        repeat
#####################

transform p_ao_sex_amazon_front_bgDark:
    truecenter
    zoom 2.5

transform p_ao_sex_amazon_front_bg800x600:
    truecenter
    zoom 4.0

image p_ao_sex_amazon_front_comp_02:

    contains:
        ConditionSwitch(
            p_ao_background == "pedrera", At("bg_ped_04", p_ao_sex_amazon_front_bg800x600),
            "True", At("bg_dark_HD",p_ao_sex_amazon_front_bgDark))

    # contains:
    #     "bg_dark_HD"
    #     truecenter
    #     #zoom 1.35
    #     zoom 2.5

###
    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 0.0 ypos 0.75 #DownLeft

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 1.0 ypos 0.75 # DownRight

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 0.0 ypos -0.25 rotate 180 #UpLeft

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        xpos 1.0 ypos -0.25 rotate 180 #UpRight
###

    contains:
        "p_ao_sex_amazon_front_mc_bed"
        truecenter

    ## Neus WINGS

    contains:
        ConditionSwitch(
            p_ao_n_wings_num > 4 and p_ao_action_Cond in ["teasing_feet_01_04", "fucking_feet_01_04"], At("p_ao_sex_amazon_front_n_feet_wings_01_04", truecenter),
            p_ao_n_wings_num > 4 and p_ao_action_Cond in ["teasing_feet_02_04", "fucking_feet_02_04"], At("p_ao_sex_amazon_front_n_feet_wings_02_04", truecenter),
            p_ao_n_wings_num > 4 and p_ao_action_Cond in ["teasing_feet_04", "fucking_feet_04"], At("p_ao_sex_amazon_front_n_wings_xx", p_ao_sex_amazon_front_n_wings_feet_04_pos),
            p_ao_n_wings_num > 4 and p_ao_action_Cond in ["teasing_feet_03", "fucking_feet_03"], At("p_ao_sex_amazon_front_n_wings_xx", p_ao_sex_amazon_front_n_wings_feet_03_pos),
            p_ao_n_wings_num > 4 and p_ao_action_Cond in ["teasing_feet_02", "fucking_feet_02"], At("p_ao_sex_amazon_front_n_wings_xx", p_ao_sex_amazon_front_n_wings_feet_02_pos),
            p_ao_n_wings_num > 4 and p_ao_action_Cond in ["teasing_feet_01", "fucking_feet_01"], At("p_ao_sex_amazon_front_n_wings_xx", p_ao_sex_amazon_front_n_wings_feet_01_pos),
            "True", Null())

    ## Neus TAIL

    contains:
        ConditionSwitch(
            p_ao_n_tail_num > 0 and p_ao_action_Cond in ["teasing_feet_01_04", "fucking_feet_01_04"], At("p_ao_sex_amazon_front_n_feet_tail_01_04", truecenter),
            p_ao_n_tail_num > 0 and p_ao_action_Cond in ["teasing_feet_02_04", "fucking_feet_02_04"], At("p_ao_sex_amazon_front_n_feet_tail_02_04", truecenter),
            p_ao_n_tail_num > 0 and p_ao_action_Cond in ["teasing_feet_04", "fucking_feet_04"], At("p_ao_sex_amazon_front_n_feet_tail_04", truecenter),
            p_ao_n_tail_num > 0 and p_ao_action_Cond in ["teasing_feet_03", "fucking_feet_03"], At("p_ao_sex_amazon_front_n_feet_tail_03", truecenter),
            p_ao_n_tail_num > 0 and p_ao_action_Cond in ["teasing_feet_02", "fucking_feet_02"], At("p_ao_sex_amazon_front_n_feet_tail_02", truecenter),
            p_ao_n_tail_num > 0 and p_ao_action_Cond in ["teasing_feet_01", "fucking_feet_01"], At("p_ao_sex_amazon_front_n_feet_tail_01", truecenter),
            "True", Null())

    contains:
        "p_ao_sex_amazon_front_mc_legs"
        truecenter

## NEUS Teasing your dick.
    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["fucking_feet_01_04", "teasing_feet_01_04"], At("p_ao_sex_amazon_front_n_feet_body_01_04", truecenter),
            p_ao_action_Cond in["fucking_feet_02_04", "teasing_feet_02_04"], At("p_ao_sex_amazon_front_n_feet_body_02_04", truecenter),
            p_ao_action_Cond in["fucking_feet_03_04", "teasing_feet_03_04"], At("p_ao_sex_amazon_front_n_feet_body_03_04", truecenter),
            p_ao_action_Cond in ["fucking_feet_04", "teasing_feet_04"], At("p_ao_sex_amazon_front_n_feet_body_04", truecenter),
            p_ao_action_Cond in ["fucking_feet_03", "teasing_feet_03"], At("p_ao_sex_amazon_front_n_feet_body_03", truecenter),
            p_ao_action_Cond in ["fucking_feet_02", "teasing_feet_02"], At("p_ao_sex_amazon_front_n_feet_body_02", truecenter),
            p_ao_action_Cond in ["teasing_feet_01"], At("p_ao_sex_amazon_front_n_feet_body_01", truecenter),
            "True", Null())

# Neus-Tongue

    contains:
        ConditionSwitch(
            p_ao_action_tongue_Cond in ["02", "02_00", "02_01", "02_02", "02_03", "02_04", "02_05", "02_06", ], At("p_ao_sex_amazon_front_n_tongue_l_02", truecenter),
            "True", Null())

## DICK
    
    contains:
        ConditionSwitch(
            p_ao_mc_dick_num == 6, At("gensex_oral_mc_dick_b_01_wet_00", p_ao_sex_amazon_front_dick_hard),
            p_ao_mc_dick_num == 5, At("gensex_oral_mc_dick_b_01_wet_00", p_ao_sex_amazon_front_dick_05),
            p_ao_mc_dick_num == 4, At("gensex_oral_mc_dick_b_01_wet_00", p_ao_sex_amazon_front_dick_04),
            p_ao_mc_dick_num == 3, At("gensex_oral_mc_dick_b_01_wet_00", p_ao_sex_amazon_front_dick_03),
            p_ao_mc_dick_num == 2, At("gensex_oral_mc_dick_b_01_wet_00", p_ao_sex_amazon_front_dick_02),
            p_ao_mc_dick_num == 1, At("gensex_oral_mc_dick_b_01_wet_00", p_ao_sex_amazon_front_dick_01),
            p_ao_mc_dick_num == 0, At("gensex_oral_mc_dick_b_01_wet_00", p_ao_sex_amazon_front_dick_00),
            "True", At("gensex_oral_mc_dick_b_01_wet_00", p_ao_sex_amazon_front_dick_hard))

# Neus_TongueMast
    
    contains:
        ConditionSwitch(
            p_ao_action_tongue_Cond == "02_06", At("p_ao_sex_amazon_front_n_tongue_dick_06", p_ao_sex_amazon_front_n_tongue_dick_06_trans),
            p_ao_action_tongue_Cond == "02_05", At("p_ao_sex_amazon_front_n_tongue_dick_05", p_ao_sex_amazon_front_n_tongue_dick_05_trans),
            p_ao_action_tongue_Cond == "02_04", At("p_ao_sex_amazon_front_n_tongue_dick_04", p_ao_sex_amazon_front_n_tongue_dick_04_trans),
            p_ao_action_tongue_Cond == "02_03", At("p_ao_sex_amazon_front_n_tongue_dick_03", p_ao_sex_amazon_front_n_tongue_dick_03_trans),
            p_ao_action_tongue_Cond == "02_02", At("p_ao_sex_amazon_front_n_tongue_dick_02", p_ao_sex_amazon_front_n_tongue_dick_02_trans),
            p_ao_action_tongue_Cond == "02_01", At("p_ao_sex_amazon_front_n_tongue_dick_01", p_ao_sex_amazon_front_n_tongue_dick_01_trans),
            p_ao_action_tongue_Cond == "02_00", At("p_ao_sex_amazon_front_n_tongue_dick_00", p_ao_sex_amazon_front_n_tongue_dick_00_trans),
            "True", Null())

    # contains:
    #     "p_ao_sex_amazon_front_n_tongue_dick_01"
    #     p_ao_sex_amazon_front_n_tongue_dick_01_trans

    # OVER VAGINAL:
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "fucking_feet_01_04", At("p_ao_sex_amazon_front_n_feet_over_01_04", truecenter),
            p_ao_action_Cond == "fucking_feet_02_04", At("p_ao_sex_amazon_front_n_feet_over_02_04", truecenter),
            p_ao_action_Cond == "fucking_feet_04", At("p_ao_sex_amazon_front_n_feet_over_04", truecenter),
            p_ao_action_Cond == "fucking_feet_03", At("p_ao_sex_amazon_front_n_feet_over_03", truecenter),
            p_ao_action_Cond == "fucking_feet_02", At("p_ao_sex_amazon_front_n_feet_over_02", truecenter),
            #p_ao_action_Cond == "fucking_feet_01", At("p_ao_sex_amazon_front_n_feet_body_01", truecenter),
            "True", Null())

    ## NEUS L_IRIS

    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["teasing_feet_01_04", "fucking_feet_01_04"], At("p_ao_sex_amazon_front_n_feet_l_iris_01_04", truecenter),
            p_ao_action_Cond in ["teasing_feet_02_04", "fucking_feet_02_04"], At("p_ao_sex_amazon_front_n_feet_l_iris_02_04", truecenter),
            p_ao_action_Cond in ["teasing_feet_03_04", "fucking_feet_03_04"], At("p_ao_sex_amazon_front_n_feet_l_iris_03_04", truecenter),
            p_ao_action_Cond in ["teasing_feet_04", "fucking_feet_04"], At("p_ao_sex_amazon_front_n_feet_l_iris_04", truecenter),
            p_ao_action_Cond in ["teasing_feet_03", "fucking_feet_03"], At("p_ao_sex_amazon_front_n_feet_l_iris_03", truecenter),
            p_ao_action_Cond in ["teasing_feet_02", "fucking_feet_02"], At("p_ao_sex_amazon_front_n_feet_l_iris_02", truecenter),
            p_ao_action_Cond in ["teasing_feet_01", "fucking_feet_01"], At("p_ao_sex_amazon_front_n_feet_l_iris_01", truecenter),
            "True", Null())

    ## NEUS iLight

    contains:
        ConditionSwitch(
            p_ao_action_Cond in ["teasing_feet_01_04", "fucking_feet_01_04"], At("p_ao_sex_amazon_front_n_feet_iLight_01_04", truecenter),
            p_ao_action_Cond in ["teasing_feet_02_04", "fucking_feet_02_04"], At("p_ao_sex_amazon_front_n_feet_iLight_02_04", truecenter),
            p_ao_action_Cond in ["teasing_feet_03_04", "fucking_feet_03_04"], At("p_ao_sex_amazon_front_n_feet_iLight_03_04", truecenter),
            p_ao_action_Cond in ["teasing_feet_04", "fucking_feet_04"], At("p_ao_sex_amazon_front_n_feet_iLight_04", p_ao_sex_amazon_front_n_feet_iLight_truecenter),
            p_ao_action_Cond in ["teasing_feet_03", "fucking_feet_03"], At("p_ao_sex_amazon_front_n_feet_iLight_03", p_ao_sex_amazon_front_n_feet_iLight_truecenter),
            p_ao_action_Cond in ["teasing_feet_02", "fucking_feet_02"], At("p_ao_sex_amazon_front_n_feet_iLight_02", p_ao_sex_amazon_front_n_feet_iLight_truecenter),
            p_ao_action_Cond in ["teasing_feet_01", "fucking_feet_01"], At("p_ao_sex_amazon_front_n_feet_iLight_01", p_ao_sex_amazon_front_n_feet_iLight_truecenter),
            "True", Null())

    contains:
        "p_ao_sex_amazon_front_mc_body"
        truecenter

    # contains:
    #     alpha 0.5
    #     ConditionSwitch(
    #         p_ao_n_wings in ["01", "02"], Null(),
    #         p_ao_action_Cond == "fucking_01_04", At("p_ao_sex_amazon_front_n_wings_xx", p_ao_sex_amazon_front_n_wings_feet_01_04_pos),
    #         p_ao_action_Cond == "fucking_02_04", At("p_ao_sex_amazon_front_n_wings_feet_02_04", truecenter),
    #         p_ao_action_Cond == "feet_04", At("p_ao_sex_amazon_front_n_wings_xx", p_ao_sex_amazon_front_n_wings_feet_04_pos),
    #         p_ao_action_Cond == "feet_03", At("p_ao_sex_amazon_front_n_wings_xx", p_ao_sex_amazon_front_n_wings_feet_03_pos),
    #         p_ao_action_Cond == "feet_02", At("p_ao_sex_amazon_front_n_wings_xx", p_ao_sex_amazon_front_n_wings_feet_02_pos),
    #         p_ao_action_Cond == "feet_01", At("p_ao_sex_amazon_front_n_wings_xx", p_ao_sex_amazon_front_n_wings_feet_01_pos),
    #         "True", Null())



    # contains:
    #     "p_ao_sex_amazon_front_n_wings_xx"
    #     truecenter
    #     alpha 0.75
    #     #ypos 0.5 # feet04
    #     #ypos 0.26 # feet03
    #     ypos 0.12 # feet 02

    # contains:
    #     "p_ao_sex_amazon_front_n_wings_TEST"
    #     truecenter
    #     alpha 0.5

    # Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())



    
######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################

######################################################################################################
######################################################################################################
##

image p_ao_sex_amazon_side_fg = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_side_fg.webp")

image p_ao_sex_amazon_side_mc = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_side_mc.webp")
image p_ao_sex_amazon_side_n_down = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_side_n_down.webp")
image p_ao_sex_amazon_side_n_up = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_side_n_up.webp")

image p_ao_sex_amazon_side_REFERENCE = "images/day05/pedrera/afterOrgasm/p_ao_sex_amazon_side_REFERENCE.webp"


transform p_ao_amazon_side_mcDick_normalHard:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.4 # Dick Position
    xzoom -1.0 zoom 0.5 xpos 0.72 ypos 1.15
    #rotate -90 # Up
    #rotate -125 # Fucked inside.
    #rotate -155 # Stretched
    rotate -140 # Rest
    block:
        easein 5.5/p_ao_n_vel rotate -139
        easeout 5.1/p_ao_n_vel rotate -141
        repeat

transform p_ao_amazon_side_mcTesticle_normal:
    subpixel True
    transform_anchor True
    xalign 0.38 yalign 0.18
    xzoom -1.0 zoom 0.5
    rotate -140 xpos 0.74 ypos 1.05

transform p_ao_amazon_side_mcTesticle_slappingBalls:
    subpixel True
    transform_anchor True
    xalign 0.38 yalign 0.18
    xzoom -1.0 zoom 0.5
    rotate -140 xpos 0.74 ypos 1.05 # Default Position
    ease_quad 0.1 rotate -150 xpos 0.72 ypos 1.06 yzoom 0.75 # Slapped.
    easeout_quad 1.0 xpos 0.74 ypos 1.05 yzoom 1.0 # Default Position


transform p_ao_amazon_side_n_sighing_breathingBalls:
    subpixel True
    transform_anchor True
    xalign 0.3 yalign 0.4
    zoom 1.0
    xpos 0.97 ypos 0.95 rotate -5
    parallel:
        ease 4.2/p_ao_n_vel rotate -10
        ease 4.3/p_ao_n_vel rotate -5
        repeat
    parallel:
        ease 6.5/p_ao_n_vel ypos 0.96
        ease 6.6/p_ao_n_vel ypos 0.9
        repeat
    parallel:
        ease 5.5/p_ao_n_vel xpos 0.95
        ease 5.1/p_ao_n_vel xpos 0.99
        repeat

transform p_ao_amazon_side_n_sighing_bitingBalls:
    subpixel True
    #"p_ao_ground_n_body_biting_comp"
    transform_anchor True
    xalign 0.3 yalign 0.4
    zoom 1.0
    xpos 0.95 ypos 0.94 rotate 5

transform p_ao_amazon_side_n_vapor_breathingBalls:
    truecenter
    xpos 0.95 ypos 0.98

transform p_ao_amazon_side_smack_slappingBalls:
    subpixel True
    truecenter
    additive 1.0
    zoom 0.5 xpos 0.9 ypos 1.0 rotate 10 alpha 0.0 # Beginning
    parallel:
        easein_quint 0.3 zoom 1.0 xpos 0.75 ypos 0.98 rotate -20 # Final
    parallel:
        easein_quad 0.1 alpha 1.0
        easein_quad 0.3 alpha 0.0

######################################################################################################
######################################################################################################
##

image p_ao_sex_amazon_side_comp_01:

    contains:
        "bg_dark_HD"
        truecenter
        zoom 1.35

## MC TESTICLE
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "slappingBalls", At("gensex_stan_mc_04_02_dick_testiclefront", p_ao_amazon_side_mcTesticle_slappingBalls),
            "True", At("gensex_stan_mc_04_02_dick_testiclefront", p_ao_amazon_side_mcTesticle_normal))

## MC DICK

    contains:
        ConditionSwitch(
            "True", At("gensex_stan_mc_04_01_dick_01", p_ao_amazon_side_mcDick_normalHard))

## Neus Breathing
    
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "breathingBalls", At("vaporbreathing_new", p_ao_amazon_side_n_vapor_breathingBalls),
            "True", Null())

## NEUS SIGHING

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "breathingBalls", At("p_ao_ground_n_body_sighing_comp", p_ao_amazon_side_n_sighing_breathingBalls),
            p_ao_action_Cond == "bitingBalls", At("p_ao_ground_n_body_biting_comp", p_ao_amazon_side_n_sighing_bitingBalls),
            "True", Null())


    # contains:
    #     "p_ao_ground_n_body_biting"
    #     p_ao_amazon_side_n_sighing_bitingBalls
    #     alpha 0.5


    # contains:
    #     "p_ao_ground_n_body_sighing_comp"
    #     p_ao_amazon_side_n_sighing_breathingBalls

## MC BODY
    contains:
        "p_ao_sex_amazon_side_mc"
        truecenter

## NEUS FUCKING BODY

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "nOverUp", At("p_ao_sex_amazon_side_n_up", truecenter),
            "True", Null())
    # contains:
    #     "p_ao_sex_amazon_side_n_up"
    #     truecenter


## SMACK
    
    contains:
        ConditionSwitch(
            p_ao_action_Cond == "slappingBalls", At("smackLateral_01", p_ao_amazon_side_smack_slappingBalls),
            "True", Null())
    # contains:
    #     "smackLateral_01"
    #     truecenter
    #     additive 1.0
    #     zoom 0.5 xpos 0.9 ypos 1.0 rotate 10 alpha 0.0 # Beginning
    #     parallel:
    #         easein_quint 0.3 zoom 1.0 xpos 0.75 ypos 0.98 rotate -20 # Final
    #     parallel:
    #         easein_quad 0.1 alpha 1.0
    #         easein_quad 0.3 alpha 0.0

    contains:
        "p_ao_sex_amazon_side_fg"
        truecenter

    # contains:
    #     "p_ao_sex_amazon_side_REFERENCE"
    #     truecenter
    #     alpha 0.4


# Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())



