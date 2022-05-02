#images 04

# hit

image hit_01 = "images/effects/hit/hit_01.webp"
image hit_02 = "images/effects/hit/hit_02.webp"
image hit_03 = "images/effects/hit/hit_03.webp"
image hit_04 = "images/effects/hit/hit_04.webp"
image hit_05 = "images/effects/hit/hit_05.webp"
image hit_06 = "images/effects/hit/hit_06.webp"
image hit_07 = "images/effects/hit/hit_07.webp"
image hit_08 = "images/effects/hit/hit_08.webp"
image hit_09 = "images/effects/hit/hit_09.webp"
image hit_10 = "images/effects/hit/hit_10.webp"
image hit_11 = "images/effects/hit/hit_11.webp"
image hit_12 = "images/effects/hit/hit_12.webp"
image hit_13 = "images/effects/hit/hit_13.webp"
image hit_14 = "images/effects/hit/hit_14.webp"
image hit_15 = "images/effects/hit/hit_15.webp"
image hit_16 = "images/effects/hit/hit_16.webp"
image hit_17 = "images/effects/hit/hit_17.webp"
image hit_18 = "images/effects/hit/hit_18.webp"
image hit_19 = "images/effects/hit/hit_19.webp"
image hit_20 = "images/effects/hit/hit_20.webp"
image hit_21 = "images/effects/hit/hit_21.webp"
image hit_22 = "images/effects/hit/hit_22.webp"
image hit_23 = "images/effects/hit/hit_23.webp"
image hit_24 = "images/effects/hit/hit_24.webp"

image hit 01= "images/effects/hit/hit_01.webp"
image hit 02= "images/effects/hit/hit_02.webp"
image hit 03= "images/effects/hit/hit_03.webp"
image hit 04= "images/effects/hit/hit_04.webp"
image hit 05= "images/effects/hit/hit_05.webp"
image hit 06= "images/effects/hit/hit_06.webp"
image hit 07= "images/effects/hit/hit_07.webp"
image hit 08= "images/effects/hit/hit_08.webp"
image hit 09= "images/effects/hit/hit_09.webp"
image hit 10= "images/effects/hit/hit_10.webp"
image hit 11= "images/effects/hit/hit_11.webp"
image hit 12= "images/effects/hit/hit_12.webp"
image hit 13= "images/effects/hit/hit_13.webp"
image hit 14= "images/effects/hit/hit_14.webp"
image hit 15= "images/effects/hit/hit_15.webp"
image hit 16= "images/effects/hit/hit_16.webp"
image hit 17= "images/effects/hit/hit_17.webp"
image hit 18= "images/effects/hit/hit_18.webp"
image hit 19= "images/effects/hit/hit_19.webp"
image hit 20= "images/effects/hit/hit_20.webp"
image hit 21= "images/effects/hit/hit_21.webp"
image hit 22= "images/effects/hit/hit_22.webp"
image hit 23= "images/effects/hit/hit_23.webp"
image hit 24= "images/effects/hit/hit_24.webp"

## BEACH aftermorning 05

image beach_01 = "images/day05/aftermorning/beach_01.webp"

image beach_02 = "images/day05/aftermorning/beach_02.webp"
image beach_02_erection  = "images/day05/aftermorning/beach_02_erection.webp"

image beach_02_erection_blur = "images/day05/aftermorning/beach_02_erection_blur.webp"
image beach_02_others = "images/day05/aftermorning/beach_02_others.webp"
image beach_02_others_blur = "images/day05/aftermorning/beach_02_others_blur.webp"
image beach_02_police = "images/day05/aftermorning/beach_02_police.webp"
image beach_02_police_little = "images/day05/aftermorning/beach_02_police_little.webp"
image beach_02_police_mouth = "images/day05/aftermorning/beach_02_police_mouth.webp"

image beach_02_far03_mask = "images/day05/aftermorning/beach_02_far03_mask.webp"
image beach_02_far04_mask = "images/day05/aftermorning/beach_02_far04_mask.webp"



####################################
############################################
####################################


transform beach_02_police_base_pos_:
    transform_anchor True
    xalign 0.5 yalign 0.95

transform beach_02_police_pos_far00:
    beach_02_police_base_pos_
    zoom 2.0 xpos 0.35 ypos 6.8 # Closest Place

transform beach_02_police_pos_far01:
    beach_02_police_base_pos_
    zoom 1.0 xpos -0.12 ypos 3.5 # Done

transform beach_02_police_pos_far02:
    beach_02_police_base_pos_
    zoom 0.5 xpos -0.4 ypos 2.5

transform beach_02_police_pos_far03:
    beach_02_police_base_pos_
    zoom 0.2 xpos -0.81 ypos 1.78 # Done

transform beach_02_police_pos_far04:
    beach_02_police_base_pos_
    zoom 0.09 xpos -0.8 ypos 1.28 # Done

transform beach_02_police_pos_far05:
    beach_02_police_base_pos_
    #zoom 0.055 
    xpos -0.72 ypos 1.1 # Done
    zoom 0.55 # little

transform beach_02_police_pos_far06:
    beach_02_police_base_pos_
    #zoom 0.03 
    xpos -0.56 ypos 0.98 # Farthest Place 
    zoom 0.3 # little




image beach_02_erection_police_comp:

    # BACKGROUND

    contains:
        ConditionSwitch(
            beach_02_p_police_Cond == "far06_blur", At("beach_02_erection_blur", truecenter),
            "True", At("beach_02_erection", truecenter)
            )
    
    # POLICE

    contains:
        ConditionSwitch(
            beach_02_p_police_Cond == "far06", At("beach_02_police_little", beach_02_police_pos_far06),
            beach_02_p_police_Cond == "far05", At("beach_02_police_little", beach_02_police_pos_far05),
            beach_02_p_police_Cond == "far04", At("beach_02_police", beach_02_police_pos_far04),
            beach_02_p_police_Cond == "far03", At("beach_02_police", beach_02_police_pos_far03),
            beach_02_p_police_Cond == "far02", At("beach_02_police", beach_02_police_pos_far02),
            beach_02_p_police_Cond == "far01", At("beach_02_police", beach_02_police_pos_far01),
            beach_02_p_police_Cond == "far00", At("beach_02_police", beach_02_police_pos_far00),
            beach_02_p_police_Cond == "far00_mouth", At("beach_02_police", beach_02_police_pos_far00),
            "True", Null()
            )

    # POLICE mouth.

    contains:
        ConditionSwitch(
            beach_02_p_police_Cond == "far00_mouth", At("beach_02_police_mouth", beach_02_police_pos_far00),
            "True", Null()
            )

    # Mask over POLICE

    contains:
        ConditionSwitch(
            beach_02_p_police_Cond == "far04", At("beach_02_far04_mask", truecenter),
            beach_02_p_police_Cond == "far03", At("beach_02_far03_mask", truecenter),
            "True", Null()
            )

    # OTHERS LEGS

    contains:
        ConditionSwitch(
            beach_02_p_legs_blur_Cond == "True", At("beach_02_others_blur", truecenter),
            beach_02_p_legs_blur_Cond == "False", At("beach_02_others", truecenter),
            "True", Null()
            )



####################################
############################################
####################################


image beach_didac_kneel = "images/day05/aftermorning/beach_didac_kneel.webp"

## 03

image beach_03_sand 01 = "images/day05/aftermorning/beach_03_sand_01.webp"
image beach_03_sand 02 = "images/day05/aftermorning/beach_03_sand_02.webp"

image beach_03_splash = "images/day05/aftermorning/beach_03_splash.webp"
image beach_03_splash empty = "images/general/empty.webp"

image beach_03_things_didac a_01 = "images/day05/aftermorning/beach_03_things_didac_a_01.webp"
image beach_03_things_didac a_02 = "images/day05/aftermorning/beach_03_things_didac_a_02.webp"

image beach_03_things_didac b_01 = "images/day05/aftermorning/beach_03_things_didac_b_01.webp"
image beach_03_things_didac b_02 = "images/day05/aftermorning/beach_03_things_didac_b_02.webp"

image beach_03_things_mc 01 = "images/day05/aftermorning/beach_03_things_mc_01.webp"
image beach_03_things_mc 02 = "images/day05/aftermorning/beach_03_things_mc_02.webp"
image beach_03_things_mc empty = "images/general/empty.webp"

image beach_03_sea 01 = "images/day05/aftermorning/beach_03_sea_01.webp"
image beach_03_sea 02 = "images/day05/aftermorning/beach_03_sea_02.webp"

    ## 03 Didac

image beach_03_didac_whole_blurred = "images/day05/aftermorning/beach_03_didac_whole_blurred.webp"

image beach_03_didac_shadow = "images/day05/aftermorning/beach_03_didac_shadow.webp"
image beach_03_didac_shadow empty = "images/general/empty.webp"

image beach_03_didac_back_arms = "images/day05/aftermorning/beach_03_didac_back_arms.webp"
image beach_03_didac_back_arms empty = "images/general/empty.webp"

image beach_03_didac_down bikini = "images/day05/aftermorning/beach_03_didac_down_bikini.webp"
image beach_03_didac_down naked = "images/day05/aftermorning/beach_03_didac_down_naked.webp"
image beach_03_didac_down empty = "images/general/empty.webp"

image beach_03_didac_hair wet = "images/day05/aftermorning/beach_03_didac_hair_wet.webp"
image beach_03_didac_hair empty = "images/general/empty.webp"

image beach_03_didac_hairback = "images/day05/aftermorning/beach_03_didac_hairback.webp"
image beach_03_didac_hairback empty = "images/general/empty.webp"

image beach_03_didac_head down = "images/day05/aftermorning/beach_03_didac_head_down.webp"
image beach_03_didac_head front = "images/day05/aftermorning/beach_03_didac_head_front.webp"
image beach_03_didac_head front empty = "images/general/empty.webp"

image beach_03_didac_head_exp_eyebrows angry = "images/day05/aftermorning/beach_03_didac_head_exp_eyebrows_angry.webp"
image beach_03_didac_head_exp_eyebrows angryx02 = "images/day05/aftermorning/beach_03_didac_head_exp_eyebrows_angryx02.webp"
image beach_03_didac_head_exp_eyebrows surprise = "images/day05/aftermorning/beach_03_didac_head_exp_eyebrows_surprise.webp"
image beach_03_didac_head_exp_eyebrows suspicious = "images/day05/aftermorning/beach_03_didac_head_exp_eyebrows_suspicious.webp"
image beach_03_didac_head_exp_eyebrows empty = "images/general/empty.webp"

image beach_03_didac_head_exp_mouth happy_Silentx01 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_sad_Silentx01.webp"
image beach_03_didac_head_exp_mouth happy_Silentx02 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_happy_Silentx02.webp"
image beach_03_didac_head_exp_mouth happy_Silentx03 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_happy_Silentx03.webp"
image beach_03_didac_head_exp_mouth happy_Silentx04 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_happy_Silentx04.webp"
image beach_03_didac_head_exp_mouth happy_Silentx05 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_happy_Silentx05.webp"
image beach_03_didac_head_exp_mouth happy_Silentx06 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_happy_Silentx06.webp"

image beach_03_didac_head_exp_mouth sad_Silentx01 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_sad_Silentx01.webp"
image beach_03_didac_head_exp_mouth sad_Silentx02 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_sad_Silentx02.webp"
image beach_03_didac_head_exp_mouth sad_Silentx03 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_sad_Silentx03.webp"
image beach_03_didac_head_exp_mouth sad_Silentx04 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_sad_Silentx04.webp"

image beach_03_didac_head_exp_mouth happy_Talkingx01 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_happy_Talkingx01.webp"
image beach_03_didac_head_exp_mouth happy_Talkingx02 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_happy_Talkingx02.webp"
image beach_03_didac_head_exp_mouth happy_Talkingx03 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_happy_Talkingx03.webp"
image beach_03_didac_head_exp_mouth happy_Talkingx04 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_happy_Talkingx04.webp"

image beach_03_didac_head_exp_mouth sad_Talkingx01 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_sad_Talkingx01.webp"
image beach_03_didac_head_exp_mouth sad_Talkingx02 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_sad_Talkingx02.webp"
image beach_03_didac_head_exp_mouth sad_Talkingx03 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_sad_Talkingx03.webp"
image beach_03_didac_head_exp_mouth sad_Talkingx04 = "images/day05/aftermorning/beach_03_didac_head_exp_mouth_sad_Talkingx04.webp"

image beach_03_didac_head_exp_mouth empty = "images/general/empty.webp"


image beach_03_didac_top armsback_bikini = "images/day05/aftermorning/beach_03_didac_top_armsback_bikini.webp"
image beach_03_didac_top armsback_naked = "images/day05/aftermorning/beach_03_didac_top_armsback_naked.webp"
image beach_03_didac_top armsdown = "images/day05/aftermorning/beach_03_didac_top_armsdown.webp"
image beach_03_didac_top armsup = "images/day05/aftermorning/beach_03_didac_top_armsup.webp"

image beach_03_didac_top hips = "images/day05/aftermorning/beach_03_didac_top_hips.webp"
image beach_03_didac_top risinghand = "images/day05/aftermorning/beach_03_didac_top_risinghand.webp"

image beach_03_didac_top cold = "images/day05/aftermorning/beach_03_didac_top_cold.webp"
image beach_03_didac_top cold empty = "images/general/empty.webp"

transform beach_03_didac_pos:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.5
    zoom 0.5 xpos 0.494 ypos 0.525

##
##

    ## OUTSEXY

image beach_outsexy_bg_sky = "images/day05/aftermorning/beach_outsexy_bg_sky.webp"

#image beach_outsexy_bg = "images/day05/aftermorning/beach_outsexy_bg.webp" #
image beach_outsexy_bg_withbeach_ 12 = "images/day05/aftermorning/beach_outsexy_bg_withbeach_over_12.webp" # WITH BEACH

#image beach_outsexy_bg_withbeach_over 03 = "images/day05/aftermorning/beach_outsexy_bg_withbeach_over_03.webp"
#image beach_outsexy_bg_withbeach_over 04 = "images/day05/aftermorning/beach_outsexy_bg_withbeach_over_04.webp"
#image beach_outsexy_bg_withbeach_over 05 = "images/day05/aftermorning/beach_outsexy_bg_withbeach_over_05.webp"
#image beach_outsexy_bg_withbeach_over 06 = "images/day05/aftermorning/beach_outsexy_bg_withbeach_over_06.webp"
#image beach_outsexy_bg_withbeach_over 07 = "images/day05/aftermorning/beach_outsexy_bg_withbeach_over_07.webp"
#image beach_outsexy_bg_withbeach_over 08 = "images/day05/aftermorning/beach_outsexy_bg_withbeach_over_08.webp"
#image beach_outsexy_bg_withbeach_over 12 = "images/day05/aftermorning/beach_outsexy_bg_withbeach_over_12.webp"

image beach_outsexy_bg_blur = "images/day05/aftermorning/beach_outsexy_bg_blur.webp"

#image beach_outsexy_bg_sea = "images/day05/aftermorning/beach_outsexy_bg_sea.webp"
image beach_outsexy_bg_sea_ 12 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_12.webp" # ONLY WATER

image beach_outsexy_bg_sea_over 01 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_01.webp"
image beach_outsexy_bg_sea_over 02 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_02.webp"
image beach_outsexy_bg_sea_over 03 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_03.webp"
image beach_outsexy_bg_sea_over 04 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_04.webp"
image beach_outsexy_bg_sea_over 05 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_05.webp"
image beach_outsexy_bg_sea_over 06 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_06.webp"
image beach_outsexy_bg_sea_over 07 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_07.webp"
image beach_outsexy_bg_sea_over 08 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_08.webp"
image beach_outsexy_bg_sea_over 09 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_09.webp"
image beach_outsexy_bg_sea_over 10 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_10.webp"
image beach_outsexy_bg_sea_over 11 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_11.webp"
image beach_outsexy_bg_sea_over 12 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_12.webp"

image beach_outsexy_bg_sea_over_b 01 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_01.webp"
image beach_outsexy_bg_sea_over_b 02 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_02.webp"
image beach_outsexy_bg_sea_over_b 03 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_03.webp"
image beach_outsexy_bg_sea_over_b 04 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_04.webp"
image beach_outsexy_bg_sea_over_b 05 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_05.webp"
image beach_outsexy_bg_sea_over_b 06 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_06.webp"
image beach_outsexy_bg_sea_over_b 07 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_07.webp"
image beach_outsexy_bg_sea_over_b 08 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_08.webp"
image beach_outsexy_bg_sea_over_b 09 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_09.webp"
image beach_outsexy_bg_sea_over_b 10 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_10.webp"
image beach_outsexy_bg_sea_over_b 11 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_11.webp"
image beach_outsexy_bg_sea_over_b 12 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_12.webp"

image beach_outsexy_bg_sea_over_c 01 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_01.webp"
image beach_outsexy_bg_sea_over_c 02 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_02.webp"
image beach_outsexy_bg_sea_over_c 03 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_03.webp"
image beach_outsexy_bg_sea_over_c 04 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_04.webp"
image beach_outsexy_bg_sea_over_c 05 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_05.webp"
image beach_outsexy_bg_sea_over_c 06 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_06.webp"
image beach_outsexy_bg_sea_over_c 07 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_07.webp"
image beach_outsexy_bg_sea_over_c 08 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_08.webp"
image beach_outsexy_bg_sea_over_c 09 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_09.webp"
image beach_outsexy_bg_sea_over_c 10 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_10.webp"
image beach_outsexy_bg_sea_over_c 11 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_11.webp"
image beach_outsexy_bg_sea_over_c 12 = "images/day05/aftermorning/beach_outsexy_bg_sea_over_12.webp"

image beach_buoy yellow = "images/day05/aftermorning/beach_buoy_yellow.webp"

image beach_outsexy_didac = "images/day05/aftermorning/beach_outsexy_didac.webp"

image beach_outsexy_bg_sea_d_swimming 01 = "images/day05/aftermorning/beach_outsexy_bg_sea_d_swimming_01.webp"

image beach_outsexy_comp:

    contains:
        "beach_outsexy_bg_sky"
        transform_anchor True
        xalign 0.5 yalign 0.5 zoom 2.0


    contains:
        "beach_outsexy_bg_withbeach_ 12"
        transform_anchor True
        xalign 0.5 yalign 0.5 zoom 2.0

    contains:
        "beach_outsexy_didac"
        transform_anchor True
        xalign 0.5 yalign 0.5

    contains:

        "sunglow 01"
        transform_anchor True
        xalign 0.5 yalign 0.5
        additive 1.0
        zoom 4.0 xpos -1.0 ypos -3.0
        block:
            linear 0.0 rotate 0
            linear 250.0 rotate 360
            repeat

    contains:

        "sunglow 02"
        transform_anchor True
        xalign 0.5 yalign 0.5
        additive 1.0
        zoom 5.0 xpos -1.0 ypos -3.0
        block:
            linear 0.0 rotate 0
            linear 250.0 rotate -360
            repeat

###

image sunglow 01 = "images/effects/light/sunglow_01.webp"
image sunglow 02 = "images/effects/light/sunglow_02.webp"



##

## Beach_Sky

image beach_sky 01 = "images/day05/aftermorning/beach_sky_01.webp"

image beach_sky_01_didac_prove = "images/day05/aftermorning/beach_sky_01_didac_prove.webp"

image beach_sky_01_didac_body empty = "images/general/empty.webp"
image beach_sky_01_didac_body = "images/day05/aftermorning/beach_sky_01_didac_body.webp"

image beach_sky_01_didac_exp_eyebrows empty = "images/general/empty.webp"
image beach_sky_01_didac_exp_eyebrows angryx01 = "images/day05/aftermorning/beach_sky_01_didac_exp_eyebrows_angryx01.webp"
image beach_sky_01_didac_exp_eyebrows angryx02 = "images/day05/aftermorning/beach_sky_01_didac_exp_eyebrows_angryx02.webp"
image beach_sky_01_didac_exp_eyebrows angryx03 = "images/day05/aftermorning/beach_sky_01_didac_exp_eyebrows_angryx03.webp"
image beach_sky_01_didac_exp_eyebrows surprisex01 = "images/day05/aftermorning/beach_sky_01_didac_exp_eyebrows_surprisex01.webp"
image beach_sky_01_didac_exp_eyebrows normal = "images/day05/aftermorning/beach_sky_01_didac_exp_eyebrows_normal.webp"
image beach_sky_01_didac_exp_eyebrows serious = "images/day05/aftermorning/beach_sky_01_didac_exp_eyebrows_serious.webp"
image beach_sky_01_didac_exp_eyebrows suspiciousx01 = "images/day05/aftermorning/beach_sky_01_didac_exp_eyebrows_suspiciousx01.webp"
image beach_sky_01_didac_exp_eyebrows suspiciousx02 = "images/day05/aftermorning/beach_sky_01_didac_exp_eyebrows_suspiciousx02.webp"

image beach_sky_01_didac_exp_mouth empty = "images/general/empty.webp"
image beach_sky_01_didac_exp_mouth happy_Silentx01 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_happy_Silentx01.webp"
image beach_sky_01_didac_exp_mouth happy_Silentx02 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_happy_Silentx02.webp"
image beach_sky_01_didac_exp_mouth happy_Silentx03 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_happy_Silentx03.webp"
image beach_sky_01_didac_exp_mouth happy_Silentx04 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_happy_Silentx04.webp"
image beach_sky_01_didac_exp_mouth happy_Silentx05 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_happy_Silentx05.webp"

image beach_sky_01_didac_exp_mouth happy_Talkingx01 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_happy_Talkingx01.webp"
image beach_sky_01_didac_exp_mouth happy_Talkingx02 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_happy_Talkingx02.webp"
image beach_sky_01_didac_exp_mouth happy_Talkingx03 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_happy_Talkingx03.webp"
image beach_sky_01_didac_exp_mouth happy_Talkingx04 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_happy_Talkingx04.webp"
image beach_sky_01_didac_exp_mouth happy_Talkingx05 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_happy_Talkingx05.webp"

image beach_sky_01_didac_exp_mouth sad_Silentx01 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_sad_Silentx01.webp"
image beach_sky_01_didac_exp_mouth sad_Silentx02 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_sad_Silentx02.webp"
image beach_sky_01_didac_exp_mouth sad_Silentx03 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_sad_Silentx03.webp"
image beach_sky_01_didac_exp_mouth sad_Silentx04 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_sad_Silentx04.webp"
image beach_sky_01_didac_exp_mouth sad_Silentx05 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_sad_Silentx05.webp"
image beach_sky_01_didac_exp_mouth sad_Silentx06 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_sad_Silentx06.webp"
image beach_sky_01_didac_exp_mouth sad_Silentx07 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_sad_Silentx07.webp"

image beach_sky_01_didac_exp_mouth sad_Talkingx01 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_sad_Talkingx01.webp"
image beach_sky_01_didac_exp_mouth sad_Talkingx02 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_sad_Talkingx02.webp"
image beach_sky_01_didac_exp_mouth sad_Talkingx03 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_sad_Talkingx03.webp"
image beach_sky_01_didac_exp_mouth sad_Talkingx04 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_sad_Talkingx04.webp"
image beach_sky_01_didac_exp_mouth sad_Talkingx05 = "images/day05/aftermorning/beach_sky_01_didac_exp_mouth_sad_Talkingx05.webp"

image beach_sky_01_didac_hairfront empty = "images/general/empty.webp"
image beach_sky_01_didac_hairfront = "images/day05/aftermorning/beach_sky_01_didac_hairfront.webp"

    ##

transform beach_sky_01_didac_exp_pos:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.5
    zoom 0.5 xpos 0.333 ypos 0.461


################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
## BEACH BALL

image beach_ball_bg = "images/day05/aftermorning/beach_ball_bg.webp"
image beach_ball_bg on = "images/day05/aftermorning/beach_ball_bg_on.webp"

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

## massage_MC

    ## back

image beach_massage_mc_back_didac_arms = "images/day05/aftermorning/beach_massage_mc_back_didac_arms.webp"
image beach_massage_mc_back_didac_body = "images/day05/aftermorning/beach_massage_mc_back_didac_body.webp"
image beach_massage_mc_back_mc_body = "images/day05/aftermorning/beach_massage_mc_back_mc_body.webp"
image beach_massage_mc_back_mc_swimsuit = "images/day05/aftermorning/beach_massage_mc_back_mc_swimsuit.webp" # Part of Dick Hidden
#image beach_massage_mc_back_mc_towel = "images/day05/aftermorning/beach_massage_mc_back_mc_towel.webp"

    ## didacoveryou

image beach_massage_mc_didacoveryou 01 = "images/day05/aftermorning/beach_massage_mc_didacoveryou_01.webp"
image beach_massage_mc_didacoveryou 02 = "images/day05/aftermorning/beach_massage_mc_didacoveryou_02.webp"
image beach_massage_mc_didacoveryou 03 = "images/day05/aftermorning/beach_massage_mc_didacoveryou_03.webp"
image beach_massage_mc_didacoveryou 04 = "images/day05/aftermorning/beach_massage_mc_didacoveryou_04.webp"
image beach_massage_mc_didacoveryou 05 = "images/day05/aftermorning/beach_massage_mc_didacoveryou_05.webp"

    ## legs

image beach_massage_mc_legs 01 = "images/day05/aftermorning/beach_massage_mc_legs_01.webp"
image beach_massage_mc_legs 02 = "images/day05/aftermorning/beach_massage_mc_legs_02.webp"
image beach_massage_mc_legs 03 = "images/day05/aftermorning/beach_massage_mc_legs_03.webp"

    ## ass 01

image beach_massage_mc_ass 01_a = "images/day05/aftermorning/beach_massage_mc_ass_01_a.webp"
image beach_massage_mc_ass 01_b = "images/day05/aftermorning/beach_massage_mc_ass_01_b.webp"
image beach_massage_mc_ass 01_c = "images/day05/aftermorning/beach_massage_mc_ass_01_c.webp"

image light_05_beach:

    contains:
        "light 05"
        subpixel True
        truecenter
        zoom 1.0
        additive 1.0
        parallel:
            ease 5.3 zoom 0.6
            ease 6.6 zoom 1.2
            repeat
        parallel:
            ease 8.3 rotate -10
            ease 4.0 rotate 2
            repeat
        parallel:
            ease 4.6 alpha 0.7
            ease 3.0 alpha 1.0
            ease 4.7 alpha 0.6
            repeat


image beach_massage_mc_ass 01_comp:

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "beach_massage_mc_ass 01_a" with Dissolve (0.5)
        transform_anchor True
        xalign 0.5 yalign 0.5
        pause 1.0
        "beach_massage_mc_ass 01_b" with Dissolve (0.5)
        transform_anchor True
        xalign 0.5 yalign 0.5
        pause 1.0
        "beach_massage_mc_ass 01_c" with Dissolve (0.5)
        transform_anchor True
        xalign 0.5 yalign 0.5
        pause 1.0
        repeat

    # contains:
    #     "beach_massage_mc_ass 01_a"
    #     transform_anchor True
    #     xalign 0.5 yalign 0.5
    #     alpha 1.0
    #     block:
    #         linear 1.0 alpha 1.5
    #         linear 1.0 alpha 0.0
    #         linear 1.0 alpha 0.0
    #         repeat

    # contains:
    #     "beach_massage_mc_ass 01_b"
    #     transform_anchor True
    #     xalign 0.5 yalign 0.5
    #     alpha 0.0
    #     block:
    #         linear 1.0 alpha 0.0
    #         linear 1.0 alpha 1.5
    #         linear 1.0 alpha 0.0
    #         repeat

    # contains:
    #     "beach_massage_mc_ass 01_c"
    #     transform_anchor True
    #     xalign 0.5 yalign 0.5
    #     alpha 0.0
    #     block:
    #         linear 1.0 alpha 0.0
    #         linear 1.0 alpha 0.0
    #         linear 1.0 alpha 1.5
    #         repeat



    ## ass 02

image beach_massage_mc_ass_02_test = "images/day05/aftermorning/beach_massage_mc_ass_02_test.webp"
image beach_massage_mc_ass_02_mc = "images/day05/aftermorning/beach_massage_mc_ass_02_mc.webp"
image beach_massage_mc_ass_02_didacarm_a = "images/day05/aftermorning/beach_massage_mc_ass_02_didacarm_a.webp"
image beach_massage_mc_ass_02_didacarm_b = "images/day05/aftermorning/beach_massage_mc_ass_02_didacarm_b.webp"

image beach_massage_mc_ass_02_comp 01:

    contains:
        "beach_massage_mc_ass_02_test"
        transform_anchor True
        xalign 0.5 yalign 0.5

    contains:
        "beach_massage_mc_ass_02_mc"
        transform_anchor True
        xalign 0.5 yalign 0.5 alpha 1.0

    contains:
        "beach_massage_mc_ass_02_didacarm_b"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5 
        xpos 0.08 ypos 0.39 #Origin
        block:
            easein_quad 1.0 xpos 0.35 ypos 0.3 # Top Ass
            easeout_quad 1.0 xpos -0.03 ypos 0.5 # Base Buttock
            ease_quad 1.0 xpos -0.3 ypos 0.51 # Below Legs
            ease_quad 1.0 xpos -0.03 ypos 0.5 # Base Buttock
            repeat

    contains:
        "beach_massage_mc_ass_02_didacarm_a"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5 
        xpos 0.08 ypos 0.39 #Origin
        block:
            easein_quad 1.0 xpos 0.15 ypos 0.35 #Top Ass
            easeout_quad 1.0 xpos -0.2 ypos 0.6 ## Base Buttock
            ease_quad 1.0 xpos -0.8 ypos 0.8 # Below Ass, Legs
            ease_quad 1.0 xpos -0.2 ypos 0.6 ## Base Buttock
            repeat

image beach_massage_mc_ass_02_comp 02:

    contains:
        "beach_massage_mc_ass_02_test"
        transform_anchor True
        xalign 0.5 yalign 0.5

    contains:
        "beach_massage_mc_ass_02_mc"
        transform_anchor True
        xalign 0.5 yalign 0.5 alpha 1.0

    contains:
        "beach_massage_mc_ass_02_didacarm_b"
        transform_anchor True
        xalign 0.5 yalign 0.5 
        xpos 0.08 ypos 0.39 #Origin

    contains:
        "beach_massage_mc_ass_02_didacarm_a"
        transform_anchor True
        xalign 0.5 yalign 0.5 
        xpos 0.08 ypos 0.39 #Origin


    ## ass 03
image beach_massage_mc_ass_03_prove = "images/day05/aftermorning/beach_massage_mc_ass_03_prove.webp"
image beach_massage_mc_ass_03_bg = "images/day05/aftermorning/beach_massage_mc_ass_03_bg.webp"
image beach_massage_mc_ass_03_buttock = "images/day05/aftermorning/beach_massage_mc_ass_03_buttock.webp"
image beach_massage_mc_ass_03_buttock red = "images/day05/aftermorning/beach_massage_mc_ass_03_buttock_red.webp"
image beach_massage_mc_ass_03_arm = "images/day05/aftermorning/beach_massage_mc_ass_03_arm.webp"

image smack 00 = "images/effects/smack/smack_00.webp" # Size must be reduced 40%
image smack 00b = "images/effects/smack/smack_00b.webp"
image smack 01 = "images/effects/smack/smack_01.webp" # Size must be reduced 40%
image smack 02 = "images/effects/smack/smack_02.webp"

image smackLateral_01 = "images/effects/smack/smackLateral_01.webp"
image smackImpact_01 = "images/effects/smack/smackImpact_01.webp"


image beach_massage_mc_ass_03_comp 01:

    #contains:
        #"beach_massage_mc_ass_03_prove"
        #truecenter

    contains:
        "beach_massage_mc_ass_03_bg"
        truecenter
        alpha 1.0

    contains:
        "beach_massage_mc_ass_03_buttock"
        subpixel True
        truecenter
        xzoom 1.0 yzoom 1.0 xpos 0.93 ypos 0.79 # Origin
        block:
            easein_quad 1.0 xzoom 1.1 yzoom 0.9 xpos 0.9 ypos 0.82 # Stretched (Base)
            easeout_quad 1.0 xzoom 1.0 yzoom 1.0 xpos 0.93 ypos 0.79 # Origin
            easein_quad 1.0 xzoom 0.95 yzoom 1.05 xpos 0.95 ypos 0.77 # Squashed (Top)
            easeout_quad 1.0 xzoom 1.0 yzoom 1.0 xpos 0.93 ypos 0.79 # Origin
            repeat

    contains:
        "beach_massage_mc_ass_03_arm"
        subpixel True
        transform_anchor True
        xanchor 0.0 yanchor 0.5
        rotate 0 xpos -0.83 ypos 0.84  #Origin
        block:
            easein_quad 1.0 rotate 10 xpos -0.95 ypos 0.5 # Base Buttock
            easeout_quad 1.0 rotate 0 xpos -0.83 ypos 0.84  #Origin
            easein_quad 1.0 rotate -20 xpos -0.75 ypos 1.4 # Top Buttock
            easeout_quad 1.0 rotate 0 xpos -0.83 ypos 0.84  #Origin
            repeat


    contains:
        "smack 01"
        truecenter
        zoom 0.4 xpos 0.96 ypos 0.83 alpha 0.0


image beach_massage_mc_ass_03_comp 02:

    #contains:
        #"beach_massage_mc_ass_03_prove"
        #truecenter

    contains:
        "beach_massage_mc_ass_03_bg"
        truecenter
        alpha 1.0

    contains:
        "beach_massage_mc_ass_03_buttock"
        subpixel True
        truecenter
        xzoom 1.0 yzoom 1.0 xpos 0.93 ypos 0.79 # Origin
        ease_elastic 0.5 xzoom 0.85 yzoom 1.15 xpos 1.0 ypos 0.76 rotate 20 # Squashed Hard (Top)
        ease_quad 0.5 xzoom 1.1 yzoom 0.9 xpos 0.9 ypos 0.82 rotate -5 # Stretched (Base)
        ease_quad 0.5 xzoom 0.95 yzoom 1.05 xpos 0.95 ypos 0.77 rotate 5 # Squashed (Top)
        ease 0.5 xzoom 1.0 yzoom 1.0 xpos 0.93 ypos 0.79 rotate 0 # Origin

    contains:
        "beach_massage_mc_ass_03_buttock red"
        subpixel True
        truecenter
        xzoom 1.0 yzoom 1.0 xpos 0.93 ypos 0.79 rotate 0 # Origin
        alpha 0.0
        pause 2.0
        easein_quad 5.0 alpha 1.0

    contains:
        "smack 01"
        subpixel True
        truecenter
        additive 1.0
        parallel:
            zoom 0.1 xpos 0.9 ypos 0.85 # Small
            ease_expo 1.0 zoom 0.6 xpos 1.0 ypos 0.8 # Big
            easeout_quad 1.0 zoom 0.7
        parallel:
            alpha 0.0
            ease_expo 0.5 alpha 1.0
            easein_quad 0.75 alpha 0.0

        #zoom 0.4 xpos 0.96 ypos 0.83  # Original
        
        

image beach_massage_mc_ass_03_comp 03:

    contains:
        "beach_massage_mc_ass_03_bg"
        truecenter
        alpha 1.0

    contains:
        "beach_massage_mc_ass_03_buttock red"
        subpixel True
        truecenter
        xzoom 1.0 yzoom 1.0 xpos 0.93 ypos 0.79 # Origin
        block:
            easein_quad 1.0 xzoom 1.1 yzoom 0.9 xpos 0.9 ypos 0.82 # Stretched (Base)
            easeout_quad 1.0 xzoom 1.0 yzoom 1.0 xpos 0.93 ypos 0.79 # Origin
            easein_quad 1.0 xzoom 0.95 yzoom 1.05 xpos 0.95 ypos 0.77 # Squashed (Top)
            easeout_quad 1.0 xzoom 1.0 yzoom 1.0 xpos 0.93 ypos 0.79 # Origin
            repeat

    contains:
        "beach_massage_mc_ass_03_arm"
        subpixel True
        transform_anchor True
        xanchor 0.0 yanchor 0.5
        rotate 0 xpos -0.83 ypos 0.84  #Origin
        block:
            easein_quad 1.0 rotate 10 xpos -0.95 ypos 0.5 # Base Buttock
            easeout_quad 1.0 rotate 0 xpos -0.83 ypos 0.84  #Origin
            easein_quad 1.0 rotate -20 xpos -0.75 ypos 1.4 # Top Buttock
            easeout_quad 1.0 rotate 0 xpos -0.83 ypos 0.84  #Origin
            repeat


    contains:
        "smack 01"
        truecenter
        zoom 0.4 xpos 0.96 ypos 0.83 alpha 0.0

    ## ear 01

image beach_massage_mc_ear_01_head = "images/day05/aftermorning/beach_massage_mc_ear_01_head.webp"
image beach_massage_mc_ear_01_hand = "images/day05/aftermorning/beach_massage_mc_ear_01_hand.webp"

image beach_massage_mc_ear_01_comp:

    contains:
        "beach_massage_mc_ear_01_head"
        truecenter

    contains:
        "beach_massage_mc_ear_01_hand"
        subpixel True
        transform_anchor True
        truecenter
        xpos 0.0 ypos 1.0 # Beginning
        block:
            easein_quad 5.0 xpos 0.8 ypos 0.6 rotate 10 # End Right
            easeout_quad 4.0 xpos 0.0 ypos 1.0 rotate -10 # Beginning
            repeat

    ## arm

image beach_massage_mc_arm_01 = "images/day05/aftermorning/beach_massage_mc_arm_01.webp"

        
    ## mc_back

image beach_massage_mc_back_mc_bg 01 = "images/day05/aftermorning/beach_massage_mc_back_mc_bg_01.webp"

image beach_massage_mc_back_didac_arms = "images/day05/aftermorning/beach_massage_mc_back_didac_arms.webp"
image beach_massage_mc_back_didac_arm_left = "images/day05/aftermorning/beach_massage_mc_back_didac_arm_left.webp"
image beach_massage_mc_back_didac_arm_right = "images/day05/aftermorning/beach_massage_mc_back_didac_arm_right.webp"
image beach_massage_mc_back_didac_body = "images/day05/aftermorning/beach_massage_mc_back_didac_body.webp"

image beach_massage_mc_back_mc_comp 01:

    contains:
        "beach_massage_mc_back_mc_bg 01"
        truecenter

    contains:
        "beach_massage_mc_back_mc_body"
        truecenter

    contains:
        "beach_massage_mc_back_didac_arms"
        truecenter
        ypos 1.6
        alpha 0.0
        #block:
            #easein_quad 5.0 ypos 1.5
            #easeout_quad 5.0 ypos 1.7
            #repeat
    contains:
        "beach_massage_mc_back_didac_arm_right"
        subpixel True
        truecenter
        #xpos 0.71 ypos 0.66
        xpos 0.63 ypos 0.9 rotate 10 #Below
        block:
            easein_quad 5.0 xpos 0.71 ypos 0.6 rotate -35 #Top
            easeout_quad 5.0 xpos 0.63 ypos 0.9 rotate 10 #Below
            repeat

    contains:
        "beach_massage_mc_back_didac_arm_left"
        subpixel True
        truecenter
        #xpos 0.28 ypos 0.66
        xpos 0.35 ypos 0.9 rotate -10 #Below
        block:
            easein_quad 5.0 xpos 0.28 ypos 0.6 rotate 35  #Top
            easeout_quad 5.0 xpos 0.35 ypos 0.9 rotate -10 #Below
            repeat

    contains:
        "beach_massage_mc_back_mc_swimsuit"
        subpixel True
        truecenter
        block:
            easein_quad 5.0 ypos 0.49 yzoom 0.9
            easeout_quad 5.0 ypos 0.52 yzoom 1.0
            repeat

    contains:
        "beach_massage_mc_back_didac_body"
        subpixel True
        truecenter
        ypos 1.7
        block:
            easein_quad 5.0 ypos 1.71
            easeout_quad 5.0 ypos 1.69
            repeat

    ## didac_back

image beach_massage_didac_back_bg_01 = "images/day05/aftermorning/beach_massage_didac_back_bg_01.webp"
image beach_massage_didac_back_bg_cum = "images/day05/aftermorning/beach_massage_didac_back_bg_cum.webp"

image beach_massage_didac_front_bg_01 = "images/day05/aftermorning/beach_massage_didac_front_bg_01.webp"
image beach_massage_didac_front_bg_cum  = "images/day05/aftermorning/beach_massage_didac_front_bg_cum.webp"

image beach_massage_didac_back_d_body = "images/day05/aftermorning/beach_massage_didac_back_d_body.webp"

image beach_massage_didac_back_comp 01:

    contains:
        "beach_massage_didac_back_bg_01"
        truecenter

    contains:
        "beach_massage_didac_back_d_body"
        truecenter

image beach_massage_didac_back_comp cum:

    contains:
        "beach_massage_didac_back_bg_cum"
        truecenter

    contains:
        "beach_massage_didac_back_d_body"
        truecenter

## Just to not repeat the same Position all the time.

label beach_massage_didac_back_comp_label:

    scene beach_massage_didac_back_comp 01:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos -1.0 # Feet Image
        easein_quad 25.0 zoom 1.0 xpos 0.5 ypos 1.5 # Didac Semi-face
    show light_05_beach:
        truecenter
    with fade

    return

    ## didac_front

image beach_massage_didac_front_d_body = "images/day05/aftermorning/beach_massage_didac_front_d_body.webp"
# image beach_massage_didac_front_d_bodyPROVE = "images/day05/aftermorning/beach_massage_didac_front_d_bodyPROVE.webp"
# image beach_massage_didac_front_d_body_PROVE = "images/day05/aftermorning/beach_massage_didac_front_d_body_PROVE.webp"

# ARM RIGHT


image beach_massage_didac_front_d_armR rest = "images/day05/aftermorning/beach_massage_didac_front_d_armR_rest.webp"
image beach_massage_didac_front_d_armR empty = "images/general/empty.webp"

image beach_massage_didac_front_d_armR_mouth = "images/day05/aftermorning/beach_massage_didac_front_d_armR_mouth.webp"
image beach_massage_didac_front_d_armR_mouth empty = "images/general/empty.webp"

## Expressions:
# HairFront
# 
image beach_massage_didac_front_d_hair_front = "images/day05/aftermorning/beach_massage_didac_front_d_hair_front.webp"

# Eyebrows

image beach_massage_didac_front_d_exp_eyebrows normal = "images/day05/aftermorning/beach_massage_didac_front_d_exp_eyebrows_normal.webp"
image beach_massage_didac_front_d_exp_eyebrows surprisex01 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_eyebrows_surprisex01.webp"
image beach_massage_didac_front_d_exp_eyebrows serious = "images/day05/aftermorning/beach_massage_didac_front_d_exp_eyebrows_serious.webp"
image beach_massage_didac_front_d_exp_eyebrows angryx01 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_eyebrows_angryx01.webp"
image beach_massage_didac_front_d_exp_eyebrows angryx02 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_eyebrows_angryx02.webp"
image beach_massage_didac_front_d_exp_eyebrows angryx03 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_eyebrows_angryx03.webp"
image beach_massage_didac_front_d_exp_eyebrows angryx04 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_eyebrows_angryx04.webp"

image beach_massage_didac_front_d_exp_eyebrows sadx01 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_eyebrows_sadx01.webp"
image beach_massage_didac_front_d_exp_eyebrows sadx02 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_eyebrows_sadx02.webp"
image beach_massage_didac_front_d_exp_eyebrows sadx03 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_eyebrows_sadx03.webp"

image beach_massage_didac_front_d_exp_eyebrows suspiciousx01 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_eyebrows_suspiciousx01.webp"
image beach_massage_didac_front_d_exp_eyebrows suspiciousx02 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_eyebrows_suspiciousx02.webp"

# Tears

image beach_massage_didac_front_d_exp_tears empty = "images/general/empty.webp"
image beach_massage_didac_front_d_exp_tears 04_01 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_tears_04_01.webp"
image beach_massage_didac_front_d_exp_tears 04_02 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_tears_04_01.webp"
image beach_massage_didac_front_d_exp_tears 04_03 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_tears_04_01.webp"

# Pupils

image beach_massage_didac_front_d_exp_pupils front04 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_pupils_front04.webp"
image beach_massage_didac_front_d_exp_pupils right04 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_pupils_right04.webp"
image beach_massage_didac_front_d_exp_pupils left04 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_pupils_left04.webp"
image beach_massage_didac_front_d_exp_pupils up04 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_pupils_up04.webp"
image beach_massage_didac_front_d_exp_pupils down04 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_pupils_down04.webp"

image beach_massage_didac_front_d_exp_pupils front06 = "images/general/empty.webp"

# Eyes

image beach_massage_didac_front_d_exp_eyes 04 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_eyes_04.webp"
image beach_massage_didac_front_d_exp_eyes 06 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_eyes_06.webp"

# Mouth

image beach_massage_didac_front_d_exp_mouth happybiting_Silentx01 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_happybiting_Silentx01.webp"
image beach_massage_didac_front_d_exp_mouth happybiting_Silentx02 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_happybiting_Silentx02.webp"
image beach_massage_didac_front_d_exp_mouth happybiting_Silentx03 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_happybiting_Silentx03.webp"
image beach_massage_didac_front_d_exp_mouth happybiting_Silentx04 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_happybiting_Silentx04.webp"
#image beach_massage_didac_front_d_exp_mouth happybiting_Silentx05 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_happybiting_Silentx05.webp" # There isn't?

image beach_massage_didac_front_d_exp_mouth happy_Silentx01 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_happy_Silentx01.webp"
image beach_massage_didac_front_d_exp_mouth happy_Silentx02 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_happy_Silentx02.webp"
image beach_massage_didac_front_d_exp_mouth happy_Silentx03 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_happy_Silentx03.webp"
image beach_massage_didac_front_d_exp_mouth happy_Silentx04 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_happy_Silentx04.webp"
image beach_massage_didac_front_d_exp_mouth happy_Silentx05 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_happy_Silentx05.webp"

image beach_massage_didac_front_d_exp_mouth sadbiting_Silentx01 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_sad_Silentx01.webp"
image beach_massage_didac_front_d_exp_mouth sadbiting_Silentx02 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_sadbiting_Silentx02.webp"
image beach_massage_didac_front_d_exp_mouth sadbiting_Silentx03 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_sadbiting_Silentx03.webp"
image beach_massage_didac_front_d_exp_mouth sadbiting_Silentx04 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_sadbiting_Silentx04.webp"
image beach_massage_didac_front_d_exp_mouth sadbiting_Silentx05 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_sadbiting_Silentx05.webp"

image beach_massage_didac_front_d_exp_mouth sad_Silentx01 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_sad_Silentx01.webp"
image beach_massage_didac_front_d_exp_mouth sad_Silentx02 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_sad_Silentx02.webp"
image beach_massage_didac_front_d_exp_mouth sad_Silentx03 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_sad_Silentx03.webp"
image beach_massage_didac_front_d_exp_mouth sad_Silentx04 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_sad_Silentx04.webp"
image beach_massage_didac_front_d_exp_mouth sad_Silentx05 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_sad_Silentx05.webp"

image beach_massage_didac_front_d_exp_mouth happy_Talkingx01 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_happy_Talkingx01.webp"
image beach_massage_didac_front_d_exp_mouth happy_Talkingx02 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_happy_Talkingx02.webp"
image beach_massage_didac_front_d_exp_mouth happy_Talkingx03 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_happy_Talkingx03.webp"
image beach_massage_didac_front_d_exp_mouth happy_Talkingx04 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_happy_Talkingx04.webp"

image beach_massage_didac_front_d_exp_mouth sad_Talkingx01 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_sad_Talkingx01.webp"
image beach_massage_didac_front_d_exp_mouth sad_Talkingx02 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_sad_Talkingx02.webp"
image beach_massage_didac_front_d_exp_mouth sad_Talkingx03 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_sad_Talkingx03.webp"
image beach_massage_didac_front_d_exp_mouth sad_Talkingx04 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_mouth_sad_Talkingx04.webp"

# Blush

image beach_massage_didac_front_d_exp_blush 00 = "images/general/empty.webp"
image beach_massage_didac_front_d_exp_blush 01 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_blush_01.webp"
image beach_massage_didac_front_d_exp_blush 02 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_blush_02.webp"
image beach_massage_didac_front_d_exp_blush 03 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_blush_03.webp"
image beach_massage_didac_front_d_exp_blush 04 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_blush_04.webp"
image beach_massage_didac_front_d_exp_blush 05 = "images/day05/aftermorning/beach_massage_didac_front_d_exp_blush_05.webp"

########
##

## Just to not repeat the same Position all the time.

label beach_massage_didac_front_comp_label:

    scene beach_massage_didac_front_comp 01:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos -1.0 # Feet Image
        easein_quad 25.0 zoom 1.0 xpos 0.5 ypos 1.55 # Didac Semi-face
    show light_05_beach:
        truecenter
    with fade

    return

##
##

transform beach_massage_didac_front_exptalk_pos:
    truecenter
    xpos 0.49 ypos 0.298 alpha 1.0

image beach_massage_didac_front_comp 01:

    

    contains:
        "beach_massage_didac_front_bg_01"
        truecenter

    contains:
        "beach_massage_didac_front_d_armR rest"
        transform_anchor True
        xalign 0.6 yalign 0.12
        xpos 0.295 ypos -0.7

    contains:
        "beach_massage_didac_front_d_body"
        truecenter

    contains:
        "beach_massage_didac_front_d_exp_blush 02"
        truecenter
        xpos 0.49 ypos -1.1 

    contains:
        "beach_massage_didac_front_d_exp_mouth happy_Silentx03"
        truecenter
        xpos 0.49 ypos -1.1 

    contains:
        "beach_massage_didac_front_d_exp_eyes 04"
        truecenter
        xpos 0.49 ypos -1.1

    contains:
        "beach_massage_didac_front_d_exp_pupils front04"
        truecenter
        xpos 0.49 ypos -1.1

    contains:
        "beach_massage_didac_front_d_exp_eyebrows surprisex01"
        truecenter
        xpos 0.49 ypos -1.1

    contains:
        "beach_massage_didac_front_d_hair_front"
        truecenter
        xpos 0.49 ypos -1.1


################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
    ## DIDAC BACK MASSAGE images:
        ##################################################################################
# ARMS
image beach_massage_didac_back_arms_bg = "images/day05/aftermorning/beach_massage_didac_back_arms_bg.webp"
image beach_massage_didac_back_arms_bgPROVE = "images/day05/aftermorning/beach_massage_didac_back_arms_bgPROVE.webp"

image beach_massage_didac_back_arms_mchand_L 01 = "images/day05/aftermorning/beach_massage_didac_back_arms_mchand_L_01.webp"
image beach_massage_didac_back_arms_mchand_R 01 = "images/day05/aftermorning/beach_massage_didac_back_arms_mchand_R_01.webp"

image beach_massage_didac_back_arms_mchand_L 02 = "images/day05/aftermorning/beach_massage_didac_back_arms_mchand_L_02.webp"
image beach_massage_didac_back_arms_mchand_R 02 = "images/day05/aftermorning/beach_massage_didac_back_arms_mchand_R_02.webp"

image beach_massage_didac_back_arms_mchand_L 03 = "images/day05/aftermorning/beach_massage_didac_back_arms_mchand_L_03.webp"
image beach_massage_didac_back_arms_mchand_R 03 = "images/day05/aftermorning/beach_massage_didac_back_arms_mchand_R_03.webp"

image beach_massage_didac_back_arms_comp 01:

    #truecenter

    contains:
        "beach_massage_didac_back_arms_bg"
        truecenter

    contains:
        "beach_massage_didac_back_arms_mchand_R 01"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5 alpha 1.0
        rotate 0 xpos 0.535 ypos 0.805
        parallel:
            easein_quad 1.0 alpha 1.1
            pause 5.0
            easein_quad 1.0 alpha 0.0
            pause 5.0
            pause 1.0
            pause 5.0
            repeat

        parallel:
            easein_quad 2.0 rotate 5
            easeout_quad 2.0 rotate -5
            repeat


    contains:
        "beach_massage_didac_back_arms_mchand_L 01"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5 alpha 1.0
        xpos 1.035 ypos 0.7
        parallel:
            easein_quad 1.0 alpha 1.1
            pause 5.0
            easein_quad 1.0 alpha 0.0
            pause 5.0
            pause 1.0
            pause 5.0
            repeat

        parallel:
            easein_quad 2.0 rotate -1
            easeout_quad 2.0 rotate -6
            repeat

    contains:
        "beach_massage_didac_back_arms_mchand_R 02"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5 alpha 0.0
        rotate 0 xpos 0.21 ypos 0.865
        parallel:
            pause 1.0
            pause 5.0
            easein_quad 1.0 alpha 1.1
            pause 5.0
            easein_quad 1.0 alpha 0.0
            pause 5.0
            repeat

        parallel:
            easein_quad 2.0 rotate 5
            easeout_quad 2.0 rotate -5
            repeat

    contains:
        "beach_massage_didac_back_arms_mchand_L 02"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5 alpha 0.0
        xpos 0.785 ypos 0.77
        parallel:
            pause 1.0
            pause 5.0
            easein_quad 1.0 alpha 1.1
            pause 5.0
            easein_quad 1.0 alpha 0.0
            pause 5.0
            repeat

        parallel:
            easein_quad 2.0 rotate 2
            easeout_quad 2.0 rotate -6
            repeat

    contains:
        "beach_massage_didac_back_arms_mchand_R 03"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5 alpha 0.0
        rotate 0 xpos -0.26 ypos 0.95
        parallel:
            easein_quad 1.0 alpha 0.0
            pause 5.0
            pause 1.0
            pause 5.0
            easein_quad 1.0 alpha 1.1
            pause 5.0
            repeat

        parallel:
            easein_quad 2.0 rotate 5
            easeout_quad 2.0 rotate -5
            repeat

    contains:
        "beach_massage_didac_back_arms_mchand_L 03"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5 alpha 0.0
        xpos -0.12 ypos 0.97
        parallel:
            easein_quad 1.0 alpha 0.0
            pause 5.0
            pause 1.0
            pause 5.0
            easein_quad 1.0 alpha 1.1
            pause 5.0
            repeat

        parallel:
            easein_quad 2.0 rotate 5
            easeout_quad 2.0 rotate -5
            repeat



# ASS
    #finger
image beach_massage_didac_back_ass_finger 01 = "images/day05/aftermorning/beach_massage_didac_back_ass_finger_01.webp"
image beach_massage_didac_back_ass_finger 02 = "images/day05/aftermorning/beach_massage_didac_back_ass_finger_02.webp"
image beach_massage_didac_back_ass_finger 03 = "images/day05/aftermorning/beach_massage_didac_back_ass_finger_03.webp"

    #massage
image beach_massage_didac_back_ass_massage 00 = "images/day05/aftermorning/beach_massage_didac_back_ass_massage_00.webp"
image beach_massage_didac_back_ass_massage 01 = "images/day05/aftermorning/beach_massage_didac_back_ass_massage_01.webp"
image beach_massage_didac_back_ass_massage 02 = "images/day05/aftermorning/beach_massage_didac_back_ass_massage_02.webp"
image beach_massage_didac_back_ass_massage 03 = "images/day05/aftermorning/beach_massage_didac_back_ass_massage_03.webp"
image beach_massage_didac_back_ass_massage 04 = "images/day05/aftermorning/beach_massage_didac_back_ass_massage_04.webp"
image beach_massage_didac_back_ass_massage 05 = "images/day05/aftermorning/beach_massage_didac_back_ass_massage_05.webp"
image beach_massage_didac_back_ass_massage 06 = "images/day05/aftermorning/beach_massage_didac_back_ass_massage_06.webp"
image beach_massage_didac_back_ass_massage 07 = "images/day05/aftermorning/beach_massage_didac_back_ass_massage_07.webp"
image beach_massage_didac_back_ass_massage 08 = "images/day05/aftermorning/beach_massage_didac_back_ass_massage_08.webp"


image beach_massage_didac_back_ass_finger_comp 01:

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "beach_massage_didac_back_ass_finger 01"
        subpixel True
        truecenter
        alpha 1.05
        pause 0.5
        easeout_quint 0.5 alpha 0.0

    contains:
        "beach_massage_didac_back_ass_finger 02"
        subpixel True
        truecenter
        alpha 0.0
        pause 0.5
        easein_quad 0.5 alpha 1.05

    contains:
        "beach_massage_didac_back_ass_finger 03"
        subpixel True
        truecenter
        alpha 0.0
        block:
            easeout_quad 0.5 alpha 0.0
            easein_quad 0.5 alpha 1.05
            repeat

image beach_massage_didac_back_ass_finger_comp 02:

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "beach_massage_didac_back_ass_finger 01"
        subpixel True
        truecenter
        alpha 1.05
        pause 0.25
        easeout_quint 0.25 alpha 0.0

    contains:
        "beach_massage_didac_back_ass_finger 02"
        subpixel True
        truecenter
        alpha 0.0
        pause 0.25
        easein_quad 0.25 alpha 1.05

    contains:
        "beach_massage_didac_back_ass_finger 03"
        subpixel True
        truecenter
        alpha 0.0
        block:
            easeout_quad 0.25 alpha 0.0
            easein_quad 0.25 alpha 1.05
            repeat

image beach_massage_didac_back_ass_massage_comp 01:

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "beach_massage_didac_back_ass_massage 00"
        subpixel True
        truecenter
        alpha 1.05
        block:
            easein_quad 0.5 alpha 1.05
            easeout_quint 0.25 alpha 0.0
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            easeout_quint 0.25 alpha 0.0
            repeat

    contains:
        "beach_massage_didac_back_ass_massage 01"
        subpixel True
        truecenter
        alpha 0.0
        block:
            easeout_quint 0.5 alpha 0.0
            easein_quad 0.25 alpha 1.05
            easeout_quint 0.25 alpha 0.0
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            repeat

    contains:
        "beach_massage_didac_back_ass_massage 02"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.5
            easeout_quint 0.25 alpha 0.0
            easein_quad 0.25 alpha 1.05
            easeout_quint 0.25 alpha 0.0
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            repeat

    contains:
        "beach_massage_didac_back_ass_massage 03"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.5
            pause 0.25
            easeout_quint 0.25 alpha 0.0
            easein_quad 0.25 alpha 1.05
            easeout_quint 0.25 alpha 0.0
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            repeat

    contains:
        "beach_massage_didac_back_ass_massage 04"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.5
            pause 0.25
            pause 0.25
            easeout_quint 0.25 alpha 0.0
            easein_quad 0.25 alpha 1.05
            easeout_quint 0.25 alpha 0.0
            pause 0.25
            pause 0.25
            pause 0.25
            repeat

    contains:
        "beach_massage_didac_back_ass_massage 05"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.5
            pause 0.25
            pause 0.25
            pause 0.25
            easeout_quint 0.25 alpha 0.0
            easein_quad 0.25 alpha 1.05
            easeout_quint 0.25 alpha 0.0
            pause 0.25
            pause 0.25
            repeat

    contains:
        "beach_massage_didac_back_ass_massage 06"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.5
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            easeout_quint 0.25 alpha 0.0
            easein_quad 0.25 alpha 1.05
            easeout_quint 0.25 alpha 0.0
            pause 0.25
            repeat

    contains:
        "beach_massage_didac_back_ass_massage 07"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.5
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            easeout_quint 0.25 alpha 0.0
            easein_quad 0.25 alpha 1.05
            easeout_quint 0.25 alpha 0.0
            repeat

    contains:
        "beach_massage_didac_back_ass_massage 08"
        subpixel True
        truecenter
        alpha 0.0
        block:
            easeout_quint 0.5 alpha 0.0
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            easeout_quint 0.25 alpha 0.0
            easein_quad 0.25 alpha 1.05
            repeat

image beach_massage_didac_back_ass_massage_comp 02:

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "beach_massage_didac_back_ass_massage 00"
        subpixel True
        truecenter
        alpha 1.05
        block:
            easein_quad 0.2 alpha 1.05
            easeout_quint 0.1 alpha 0.0
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            easeout_quint 0.1 alpha 0.0
            repeat

    contains:
        "beach_massage_didac_back_ass_massage 01"
        subpixel True
        truecenter
        alpha 0.0
        block:
            easeout_quint 0.2 alpha 0.0
            easein_quad 0.1 alpha 1.05
            easeout_quint 0.1 alpha 0.0
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            repeat

    contains:
        "beach_massage_didac_back_ass_massage 02"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.2
            easeout_quint 0.1 alpha 0.0
            easein_quad 0.1 alpha 1.05
            easeout_quint 0.1 alpha 0.0
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            repeat

    contains:
        "beach_massage_didac_back_ass_massage 03"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.2
            pause 0.1
            easeout_quint 0.1 alpha 0.0
            easein_quad 0.1 alpha 1.05
            easeout_quint 0.1 alpha 0.0
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            repeat

    contains:
        "beach_massage_didac_back_ass_massage 04"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.2
            pause 0.1
            pause 0.1
            easeout_quint 0.1 alpha 0.0
            easein_quad 0.1 alpha 1.05
            easeout_quint 0.1 alpha 0.0
            pause 0.1
            pause 0.1
            pause 0.1
            repeat

    contains:
        "beach_massage_didac_back_ass_massage 05"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.2
            pause 0.1
            pause 0.1
            pause 0.1
            easeout_quint 0.1 alpha 0.0
            easein_quad 0.1 alpha 1.05
            easeout_quint 0.1 alpha 0.0
            pause 0.1
            pause 0.1
            repeat

    contains:
        "beach_massage_didac_back_ass_massage 06"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.2
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            easeout_quint 0.1 alpha 0.0
            easein_quad 0.1 alpha 1.05
            easeout_quint 0.1 alpha 0.0
            pause 0.1
            repeat

    contains:
        "beach_massage_didac_back_ass_massage 07"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.2
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            easeout_quint 0.1 alpha 0.0
            easein_quad 0.1 alpha 1.05
            easeout_quint 0.1 alpha 0.0
            repeat

    contains:
        "beach_massage_didac_back_ass_massage 08"
        subpixel True
        truecenter
        alpha 0.0
        block:
            easeout_quint 0.2 alpha 0.0
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            easeout_quint 0.1 alpha 0.0
            easein_quad 0.1 alpha 1.05
            repeat

##########################

# FEET

image beach_massage_didac_back_feet_bg = "images/day05/aftermorning/beach_massage_didac_back_feet_bg.webp"

# LEGS

image beach_massage_didac_back_legs_bg = "images/day05/aftermorning/beach_massage_didac_back_legs_bg.webp"

image beach_massage_didac_back_legs_bgPROVE = "images/day05/aftermorning/beach_massage_didac_back_legs_bgPROVE.webp"

image beach_massage_didac_back_legs_mchand_L 01 = "images/day05/aftermorning/beach_massage_didac_back_legs_mchand_L_01.webp"
image beach_massage_didac_back_legs_mchand_L 02 = "images/day05/aftermorning/beach_massage_didac_back_legs_mchand_L_02.webp"
image beach_massage_didac_back_legs_mchand_L 03 = "images/day05/aftermorning/beach_massage_didac_back_legs_mchand_L_03.webp"
image beach_massage_didac_back_legs_mchand_L 04 = "images/day05/aftermorning/beach_massage_didac_back_legs_mchand_L_04.webp"

image beach_massage_didac_back_legs_mchand_R 01 = "images/day05/aftermorning/beach_massage_didac_back_legs_mchand_R_01.webp"
image beach_massage_didac_back_legs_mchand_R 02 = "images/day05/aftermorning/beach_massage_didac_back_legs_mchand_R_02.webp"
image beach_massage_didac_back_legs_mchand_R 03 = "images/day05/aftermorning/beach_massage_didac_back_legs_mchand_R_03.webp"
image beach_massage_didac_back_legs_mchand_R 04 = "images/day05/aftermorning/beach_massage_didac_back_legs_mchand_R_04.webp"

image beach_massage_didac_back_legs_Comp 01:

    contains:
        "beach_massage_didac_back_legs_bg"
        truecenter

    contains:
        "beach_massage_didac_back_legs_mchand_L 01"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.7 ypos 0.318 rotate 0
        alpha 1.0
        parallel:
            easein_quad 1.0 alpha 1.0
            pause 10.0
            easein_quad 1.0 alpha -0.1
            pause 6.0
            pause 1.0
            pause 6.0
            pause 1.0
            pause 6.0
        parallel:
            easein_quad 2.0 rotate -5
            easeout_quad 2.0 rotate 5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_R 01"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.29 ypos 0.625 rotate 0
        alpha 1.0
        parallel:
            easein_quad 1.0 alpha 1.0
            pause 10.0
            easein_quad 1.0 alpha -0.1
            pause 6.0
            pause 1.0
            pause 6.0
            pause 1.0
            pause 6.0
        parallel:
            easein_quad 2.0 rotate 5
            easeout_quad 2.0 rotate -5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_L 02"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 1.025 ypos 0.19 rotate 0
        alpha 0.0
        parallel:
            pause 1.0
            pause 10.0
            easein_quad 1.0 alpha 1.0
            pause 6.0
            easein_quad 1.0 alpha -0.1
            pause 6.0
            pause 1.0
            pause 6.0
        parallel:
            easein_quad 2.0 rotate -5
            easeout_quad 2.0 rotate 5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_R 02"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.537 ypos 0.435 rotate 0
        alpha 0.0
        parallel:
            pause 1.0
            pause 10.0
            easein_quad 1.0 alpha 1.0
            pause 6.0
            easein_quad 1.0 alpha -0.1
            pause 6.0
            pause 1.0
            pause 6.0
        parallel:
            easein_quad 2.0 rotate 5
            easeout_quad 2.0 rotate -5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_L 03"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.9 ypos 0.225 rotate 0
        alpha 0.0
        parallel:
            pause 1.0
            pause 10.0
            pause 1.0
            pause 6.0
            easein_quad 1.0 alpha 1.0
            pause 6.0
            easein_quad 1.0 alpha -0.1
            pause 6.0
        parallel:
            easein_quad 2.0 rotate -5
            easeout_quad 2.0 rotate 5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_R 03"
        subpixel True
        transform_anchor True
        xalign 0.9 yalign 0.55
        xpos 0.87 ypos 0.36 rotate 0
        alpha 0.0
        parallel:
            pause 1.0
            pause 10.0
            pause 1.0
            pause 6.0
            easein_quad 1.0 alpha 1.0
            pause 6.0
            easein_quad 1.0 alpha -0.1
            pause 6.0
        parallel:
            easein_quad 2.0 rotate 5
            easeout_quad 2.0 rotate -5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_L 04"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 1.24 ypos 0.07 rotate 0
        alpha 0.0
        parallel:
            easein_quad 1.0 alpha -0.1
            pause 10.0
            pause 1.0
            pause 6.0
            pause 1.0
            pause 6.0
            easein_quad 1.0 alpha 1.0
            pause 6.0
        parallel:
            easein_quad 2.0 rotate -5
            easeout_quad 2.0 rotate 5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_R 04"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.875 ypos 0.35 rotate 0
        alpha 0.0
        parallel:
            easein_quad 1.0 alpha -0.1
            pause 10.0
            pause 1.0
            pause 6.0
            pause 1.0
            pause 6.0
            easein_quad 1.0 alpha 1.0
            pause 6.0
        parallel:
            easein_quad 2.0 rotate 5
            easeout_quad 2.0 rotate -5
            repeat

image beach_massage_didac_back_legs_Comp 02: # Only Up.

    contains:
        "beach_massage_didac_back_legs_bg"
        truecenter

    contains:
        "beach_massage_didac_back_legs_mchand_L 01"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.7 ypos 0.318 rotate 0
        alpha 1.0
        parallel:
            easein_quad 1.0 alpha 1.0
            pause 1.5
            easein_quad 0.5 alpha -0.1
            pause 1.5
            pause 0.5
            pause 1.5
            pause 0.5
            pause 1.5
            repeat
        parallel:
            easein_quad 1.0 rotate -5
            easeout_quad 1.0 rotate 5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_R 01"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.29 ypos 0.625 rotate 0
        alpha 1.0
        parallel:
            easein_quad 1.0 alpha 1.0
            pause 1.5
            easein_quad 0.5 alpha -0.1
            pause 1.5
            pause 0.5
            pause 1.5
            pause 0.5
            pause 1.5
            repeat
        parallel:
            easein_quad 1.0 rotate 5
            easeout_quad 1.0 rotate -5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_L 02"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 1.025 ypos 0.19 rotate 0
        alpha 0.0
        parallel:
            pause 1.0
            pause 1.5
            easein_quad 0.5 alpha 1.0
            pause 1.5
            easein_quad 0.5 alpha -0.1
            pause 1.5
            pause 0.5
            pause 1.5
            repeat
        parallel:
            easein_quad 1.0 rotate -5
            easeout_quad 1.0 rotate 5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_R 02"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.537 ypos 0.435 rotate 0
        alpha 0.0
        parallel:
            pause 1.0
            pause 1.5
            easein_quad 0.5 alpha 1.0
            pause 1.5
            easein_quad 0.5 alpha -0.1
            pause 1.5
            pause 0.5
            pause 1.5
            repeat
        parallel:
            easein_quad 1.0 rotate 5
            easeout_quad 1.0 rotate -5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_L 03"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.9 ypos 0.225 rotate 0
        alpha 0.0
        parallel:
            pause 1.0
            pause 1.5
            pause 0.5
            pause 1.5
            easein_quad 0.5 alpha 1.0
            pause 1.5
            easein_quad 0.5 alpha -0.1
            pause 1.5
            repeat
        parallel:
            easein_quad 1.0 rotate -5
            easeout_quad 1.0 rotate 5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_R 03"
        subpixel True
        transform_anchor True
        xalign 0.9 yalign 0.55
        xpos 0.87 ypos 0.36 rotate 0
        alpha 0.0
        parallel:
            pause 1.0
            pause 1.5
            pause 0.5
            pause 1.5
            easein_quad 0.5 alpha 1.0
            pause 1.5
            easein_quad 0.5 alpha -0.1
            pause 1.5
            repeat
        parallel:
            easein_quad 1.0 rotate 5
            easeout_quad 1.0 rotate -5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_L 04"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 1.24 ypos 0.07 rotate 0
        alpha 0.0
        parallel:
            easein_quad 1.0 alpha -0.1
            pause 1.5
            pause 0.5
            pause 1.5
            pause 0.5
            pause 1.5
            easein_quad 0.5 alpha 1.0
            pause 1.5
            repeat
        parallel:
            easein_quad 1.0 rotate -5
            easeout_quad 1.0 rotate 5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_R 04"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.875 ypos 0.35 rotate 0
        alpha 0.0
        parallel:
            easein_quad 1.0 alpha -0.1
            pause 1.5
            pause 0.5
            pause 1.5
            pause 0.5
            pause 1.5
            easein_quad 0.5 alpha 1.0
            pause 1.5
            repeat
        parallel:
            easein_quad 1.0 rotate 5
            easeout_quad 1.0 rotate -5
            repeat

image beach_massage_didac_back_legs_Comp 03: # Up-Down

    contains:
        "beach_massage_didac_back_legs_bg"
        truecenter

    contains:
        "beach_massage_didac_back_legs_mchand_L 01"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.7 ypos 0.318 rotate 0
        alpha 1.0
        parallel:
            easein_quad 0.5 alpha 1.0
            pause 1.5
            easein_quad 0.5 alpha -0.1 # 02
            pause 1.5
            pause 0.5 # 03
            pause 1.5
            pause 0.5 # 04
            pause 1.5
            pause 0.5 # 03
            pause 1.5
            pause 0.5 # 02
            pause 1.5
            repeat
        parallel:
            easein_quad 1.0 rotate -5
            easeout_quad 1.0 rotate 5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_R 01"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.29 ypos 0.625 rotate 0
        alpha 1.0
        parallel:
            easein_quad 0.5 alpha 1.0
            pause 1.5
            easein_quad 0.5 alpha -0.1 # 02
            pause 1.5
            pause 0.5 # 03
            pause 1.5
            pause 0.5 # 04
            pause 1.5
            pause 0.5 # 03
            pause 1.5
            pause 0.5 # 02
            pause 1.5
            repeat
        parallel:
            easein_quad 1.0 rotate 5
            easeout_quad 1.0 rotate -5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_L 02"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 1.025 ypos 0.19 rotate 0
        alpha 0.0
        parallel:
            easein_quad 0.5 alpha -0.1
            pause 1.5
            easein_quad 0.5 alpha 1.0
            pause 1.5
            easein_quad 0.5 alpha -0.1
            pause 1.5
            pause 0.5
            pause 1.5
            pause 0.5
            pause 1.5
            easein_quad 0.5 alpha 1.0
            pause 1.5
            repeat
        parallel:
            easein_quad 1.0 rotate -5
            easeout_quad 1.0 rotate 5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_R 02"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.537 ypos 0.435 rotate 0
        alpha 0.0
        parallel:
            easein_quad 0.5 alpha -0.1
            pause 1.5
            easein_quad 0.5 alpha 1.0
            pause 1.5
            easein_quad 0.5 alpha -0.1
            pause 1.5
            pause 0.5
            pause 1.5
            pause 0.5
            pause 1.5
            easein_quad 0.5 alpha 1.0
            pause 1.5
            repeat
        parallel:
            easein_quad 1.0 rotate 5
            easeout_quad 1.0 rotate -5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_L 03"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.9 ypos 0.225 rotate 0
        alpha 0.0
        parallel:
            pause 0.5
            pause 1.5
            pause 0.5
            pause 1.5
            easein_quad 0.5 alpha 1.0
            pause 1.5
            easein_quad 0.5 alpha -0.1
            pause 1.5
            easein_quad 0.5 alpha 1.0
            pause 1.5
            easein_quad 0.5 alpha -0.1 # 02
            pause 1.5
            repeat
        parallel:
            easein_quad 1.0 rotate -5
            easeout_quad 1.0 rotate 5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_R 03"
        subpixel True
        transform_anchor True
        xalign 0.9 yalign 0.55
        xpos 0.87 ypos 0.36 rotate 0
        alpha 0.0
        parallel:
            pause 0.5
            pause 1.5
            pause 0.5
            pause 1.5
            easein_quad 0.5 alpha 1.0
            pause 1.5
            easein_quad 0.5 alpha -0.1
            pause 1.5
            easein_quad 0.5 alpha 1.0
            pause 1.5
            easein_quad 0.5 alpha -0.1 # 02
            pause 1.5
            repeat
        parallel:
            easein_quad 1.0 rotate 5
            easeout_quad 1.0 rotate -5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_L 04"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 1.24 ypos 0.07 rotate 0
        alpha 0.0
        parallel:
            pause 0.5
            pause 1.5
            pause 0.5
            pause 1.5
            pause 0.5
            pause 1.5
            easein_quad 0.5 alpha 1.0
            pause 1.5
            easeout_quad 0.5 alpha -0.1 # 03
            pause 1.5
            pause 0.5 # 02
            pause 1.5
            repeat
        parallel:
            easein_quad 1.0 rotate -5
            easeout_quad 1.0 rotate 5
            repeat

    contains:
        "beach_massage_didac_back_legs_mchand_R 04"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.875 ypos 0.35 rotate 0
        alpha 0.0
        parallel:
            pause 0.5
            pause 1.5
            pause 0.5
            pause 1.5
            pause 0.5
            pause 1.5
            easein_quad 0.5 alpha 1.0
            pause 1.5
            easeout_quad 0.5 alpha -0.1 # 03
            pause 1.5
            pause 0.5 # 02
            pause 1.5
            repeat
        parallel:
            easein_quad 1.0 rotate 5
            easeout_quad 1.0 rotate -5
            repeat

# NECK
    # armpit

image beach_massage_didac_back_neck_armpit_bg = "images/day05/aftermorning/beach_massage_didac_back_neck_armpit_bg.webp"
image beach_massage_didac_back_neck_armpit_bgPROVE = "images/day05/aftermorning/beach_massage_didac_back_neck_armpit_bgPROVE.webp"
image beach_massage_didac_back_neck_armpit_mchand_L 01 = "images/day05/aftermorning/beach_massage_didac_back_neck_armpit_mchand_L_01.webp"
image beach_massage_didac_back_neck_armpit_mchand_R 01 = "images/day05/aftermorning/beach_massage_didac_back_neck_armpit_mchand_R_01.webp"

image beach_massage_didac_back_neck_armpit_comp 01:

    contains:
        "beach_massage_didac_back_neck_armpit_bg"
        truecenter

    contains:
        "beach_massage_didac_back_neck_armpit_mchand_R 01"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.01 ypos 0.325 rotate 0
        block:
            easein_quad 3.0 rotate 5
            easeout_quad 3.0 rotate -5
            repeat

    contains:
        "beach_massage_didac_back_neck_armpit_mchand_L 01"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 1.172 ypos 0.255 rotate 0
        block:
            easein_quad 3.0 rotate -5
            easeout_quad 3.0 rotate 5
            repeat

    # ear

image beach_massage_didac_back_neck_ear_bg = "images/day05/aftermorning/beach_massage_didac_back_neck_ear_bg.webp"
image beach_massage_didac_back_neck_ear_bgPROVE = "images/day05/aftermorning/beach_massage_didac_back_neck_ear_bgPROVE.webp"
image beach_massage_didac_back_neck_ear_mchand = "images/day05/aftermorning/beach_massage_didac_back_neck_ear_mchand.webp"

image beach_massage_didac_back_neck_ear_comp 01:

    contains:

        "beach_massage_didac_back_neck_ear_bg"
        truecenter

    contains:

        "beach_massage_didac_back_neck_ear_mchand"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.19 ypos 1.02 rotate 0 # Original pose
        block:
            easein_quad 10.0 xpos 0.0 ypos 1.5 rotate -10 # Beginning
            easeout_quad 5.0 xpos 1.0 ypos 0.8 rotate 10 # All hand
            easein_quad 10.0 xpos 1.1 ypos 1.3 rotate -20 # Pulgar around the ear
            repeat

    # neck

image beach_massage_didac_back_neck_neck 01 = "images/day05/aftermorning/beach_massage_didac_back_neck_neck_01.webp"
image beach_massage_didac_back_neck_neck 02 = "images/day05/aftermorning/beach_massage_didac_back_neck_neck_02.webp"
image beach_massage_didac_back_neck_neck 03 = "images/day05/aftermorning/beach_massage_didac_back_neck_neck_03.webp"
image beach_massage_didac_back_neck_neck 04 = "images/day05/aftermorning/beach_massage_didac_back_neck_neck_04.webp"
image beach_massage_didac_back_neck_neck 05 = "images/day05/aftermorning/beach_massage_didac_back_neck_neck_05.webp"

image beach_massage_didac_back_neck_neck_comp 01:

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "beach_massage_didac_back_neck_neck 01" with Dissolve (0.15)
        truecenter
        pause 0.3
        "beach_massage_didac_back_neck_neck 02" with Dissolve (0.15)
        pause 0.3
        "beach_massage_didac_back_neck_neck 03" with Dissolve (0.15)
        pause 0.3
        "beach_massage_didac_back_neck_neck 04" with Dissolve (0.15)
        pause 0.3
        "beach_massage_didac_back_neck_neck 05" with Dissolve (0.15)
        pause 0.3
        repeat


    # contains:
    #     "beach_massage_didac_back_neck_neck 01"
    #     truecenter
    #     alpha 0.1
    #     block:
    #         easein_quad 0.5 alpha 1.1
    #         easeout_quad 0.3 alpha 0.0
    #         pause 0.3
    #         pause 0.3
    #         pause 0.3
    #         repeat
    # contains:
    #     "beach_massage_didac_back_neck_neck 02"
    #     truecenter
    #     alpha 0.0
    #     block:
    #         pause 0.5
    #         easein_quad 0.3 alpha 1.1
    #         easeout_quad 0.3 alpha 0.0
    #         pause 0.3
    #         pause 0.3
    #         repeat
    # contains:
    #     "beach_massage_didac_back_neck_neck 03"
    #     truecenter
    #     alpha 0.0
    #     block:
    #         pause 0.5
    #         pause 0.3
    #         easein_quad 0.3 alpha 1.1
    #         easeout_quad 0.3 alpha 0.0
    #         pause 0.3
    #         repeat
    # contains:
    #     "beach_massage_didac_back_neck_neck 04"
    #     truecenter
    #     alpha 0.0
    #     block:
    #         pause 0.5
    #         pause 0.3
    #         pause 0.3
    #         easein_quad 0.3 alpha 1.1
    #         easeout_quad 0.3 alpha 0.0
    #         repeat
            
    # contains:
    #     "beach_massage_didac_back_neck_neck 05"
    #     truecenter
    #     alpha 0.0
    #     block:
    #         easeout_quad 0.5 alpha 0.0
    #         pause 0.3
    #         pause 0.3
    #         pause 0.3
    #         easein_quad 0.3 alpha 1.1
    #         repeat
            
            

    # shoulder

image beach_massage_didac_back_neck_shoulder_bg = "images/day05/aftermorning/beach_massage_didac_back_neck_shoulder_bg.webp"

# PUSSY
    # fingering

image beach_massage_didac_back_pussy_fingering 01 = "images/day05/aftermorning/beach_massage_didac_back_pussy_fingering_01.webp"
image beach_massage_didac_back_pussy_fingering 02 = "images/day05/aftermorning/beach_massage_didac_back_pussy_fingering_02.webp"
image beach_massage_didac_back_pussy_fingering 03 = "images/day05/aftermorning/beach_massage_didac_back_pussy_fingering_03.webp"
image beach_massage_didac_back_pussy_fingering 04 = "images/day05/aftermorning/beach_massage_didac_back_pussy_fingering_04.webp"
image beach_massage_didac_back_pussy_fingering 05 = "images/day05/aftermorning/beach_massage_didac_back_pussy_fingering_05.webp"
image beach_massage_didac_back_pussy_fingering 06 = "images/day05/aftermorning/beach_massage_didac_back_pussy_fingering_06.webp"

image beach_massage_didac_back_pussy_fingering cum = "images/day05/aftermorning/beach_massage_didac_back_pussy_fingering_cum.webp"
image beach_massage_didac_back_pussy_fingering_squirt = "images/day05/aftermorning/beach_massage_didac_back_pussy_fingering_squirt.webp"
image beach_massage_didac_back_pussy_fingering_squirtcam = "images/day05/aftermorning/beach_massage_didac_back_pussy_fingering_squirtcam.webp"

image beach_massage_didac_back_pussy_fingering_comp 01:

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "beach_massage_didac_back_pussy_fingering 01"
        subpixel True
        truecenter
        alpha 1.0
        block:
            easein_quad 0.5 alpha 1.1
            easeout_circ 0.2 alpha 0.0
            pause 0.2
            pause 0.2
            pause 0.2
            pause 0.2
            pause 0.2
            pause 0.2
            pause 0.2
            pause 0.2
            repeat

    contains:
        "beach_massage_didac_back_pussy_fingering 02"
        subpixel True
        truecenter
        alpha 0.0
        block:
            easeout_circ 0.5 alpha 0.0
            easein_quad 0.2 alpha 1.1
            easeout_circ 0.2 alpha 0.0
            pause 0.2
            pause 0.2
            pause 0.2
            pause 0.2
            pause 0.2
            pause 0.2
            easein_quad 0.2 alpha 1.1
            repeat
            

    contains:
        "beach_massage_didac_back_pussy_fingering 03"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.5
            pause 0.2
            easein_quad 0.2 alpha 1.1
            easeout_circ 0.2 alpha 0.0
            pause 0.2
            pause 0.2
            pause 0.2
            pause 0.2
            easein_quad 0.2 alpha 1.1
            easeout_circ 0.2 alpha 0.0
            repeat
            

    contains:
        "beach_massage_didac_back_pussy_fingering 04"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.5
            pause 0.2
            pause 0.2
            easein_quad 0.2 alpha 1.1
            easeout_circ 0.2 alpha 0.0
            pause 0.2
            pause 0.2
            easein_quad 0.2 alpha 1.1
            easeout_circ 0.2 alpha 0.0
            pause 0.2
            repeat


    contains:
        "beach_massage_didac_back_pussy_fingering 05"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.5
            pause 0.2
            pause 0.2
            pause 0.2
            easein_quad 0.2 alpha 1.1
            easeout_circ 0.2 alpha 0.0
            easein_quad 0.2 alpha 1.1
            easeout_circ 0.2 alpha 0.0
            pause 0.2
            pause 0.2
            repeat


    contains:
        "beach_massage_didac_back_pussy_fingering 06"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.5
            pause 0.2
            pause 0.2
            pause 0.2   
            pause 0.2  
            easein_quad 0.2 alpha 1.1
            easeout_circ 0.2 alpha 0.0
            pause 0.2
            pause 0.2
            pause 0.2
            repeat

image beach_massage_didac_back_pussy_fingering_comp 02:

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "beach_massage_didac_back_pussy_fingering 01"
        subpixel True
        truecenter
        alpha 1.0
        block:
            easein_quad 0.15 alpha 1.1
            easeout_circ 0.05 alpha 0.0
            pause 0.05
            pause 0.05
            pause 0.05
            pause 0.05
            pause 0.05
            pause 0.05
            pause 0.05
            pause 0.05
            repeat

    contains:
        "beach_massage_didac_back_pussy_fingering 02"
        subpixel True
        truecenter
        alpha 0.0
        block:
            easeout_circ 0.15 alpha 0.0
            easein_quad 0.05 alpha 1.1
            easeout_circ 0.05 alpha 0.0
            pause 0.05
            pause 0.05
            pause 0.05
            pause 0.05
            pause 0.05
            pause 0.05
            easein_quad 0.05 alpha 1.1
            repeat
            

    contains:
        "beach_massage_didac_back_pussy_fingering 03"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.15
            pause 0.05
            easein_quad 0.05 alpha 1.1
            easeout_circ 0.05 alpha 0.0
            pause 0.05
            pause 0.05
            pause 0.05
            pause 0.05
            easein_quad 0.05 alpha 1.1
            easeout_circ 0.05 alpha 0.0
            repeat
            

    contains:
        "beach_massage_didac_back_pussy_fingering 04"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.15
            pause 0.05
            pause 0.05
            easein_quad 0.05 alpha 1.1
            easeout_circ 0.05 alpha 0.0
            pause 0.05
            pause 0.05
            easein_quad 0.05 alpha 1.1
            easeout_circ 0.05 alpha 0.0
            pause 0.05
            repeat


    contains:
        "beach_massage_didac_back_pussy_fingering 05"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.15
            pause 0.05
            pause 0.05
            pause 0.05
            easein_quad 0.05 alpha 1.1
            easeout_circ 0.05 alpha 0.0
            easein_quad 0.05 alpha 1.1
            easeout_circ 0.05 alpha 0.0
            pause 0.05
            pause 0.05
            repeat


    contains:
        "beach_massage_didac_back_pussy_fingering 06"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.15
            pause 0.05
            pause 0.05
            pause 0.05   
            pause 0.05  
            easein_quad 0.05 alpha 1.1
            easeout_circ 0.05 alpha 0.0
            pause 0.05
            pause 0.05
            pause 0.05
            repeat                

    # over

image beach_massage_didac_back_pussy_over 00a = "images/day05/aftermorning/beach_massage_didac_back_pussy_over_00a.webp"
image beach_massage_didac_back_pussy_over 00a_cum = "images/day05/aftermorning/beach_massage_didac_back_pussy_over_00a_cum.webp"
image beach_massage_didac_back_pussy_over 00b = "images/day05/aftermorning/beach_massage_didac_back_pussy_over_00b.webp"
image beach_massage_didac_back_pussy_over 00b_cum = "images/day05/aftermorning/beach_massage_didac_back_pussy_over_00b_cum.webp"
image beach_massage_didac_back_pussy_over 00c = "images/day05/aftermorning/beach_massage_didac_back_pussy_over_00c.webp"
image beach_massage_didac_back_pussy_over 00c_cum = "images/day05/aftermorning/beach_massage_didac_back_pussy_over_00c_cum.webp"
image beach_massage_didac_back_pussy_over 01 = "images/day05/aftermorning/beach_massage_didac_back_pussy_over_01.webp"
image beach_massage_didac_back_pussy_over 02 = "images/day05/aftermorning/beach_massage_didac_back_pussy_over_02.webp"
image beach_massage_didac_back_pussy_over 03 = "images/day05/aftermorning/beach_massage_didac_back_pussy_over_03.webp"
image beach_massage_didac_back_pussy_over 04 = "images/day05/aftermorning/beach_massage_didac_back_pussy_over_04.webp"
image beach_massage_didac_back_pussy_over 05 = "images/day05/aftermorning/beach_massage_didac_back_pussy_over_05.webp"
image beach_massage_didac_back_pussy_over 06 = "images/day05/aftermorning/beach_massage_didac_back_pussy_over_06.webp"
image beach_massage_didac_back_pussy_over 07 = "images/day05/aftermorning/beach_massage_didac_back_pussy_over_07.webp"
image beach_massage_didac_back_pussy_over 08 = "images/day05/aftermorning/beach_massage_didac_back_pussy_over_08.webp"


image beach_massage_didac_back_pussy_over_comp 01:

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "beach_massage_didac_back_pussy_over 01"
        subpixel True
        truecenter
        alpha 1.0
        block:
            easein_quad 0.5 alpha 1.1
            easeout_circ 0.25 alpha 0.0
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            easeout_circ 0.25 alpha 0.0
            repeat

    contains:
        "beach_massage_didac_back_pussy_over 02"
        subpixel True
        truecenter
        alpha 0.0
        block:
            easeout_circ 0.5 alpha 0.0
            easein_quad 0.25 alpha 1.1
            easeout_circ 0.25 alpha 0.0
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            repeat
            

    contains:
        "beach_massage_didac_back_pussy_over 03"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.5
            easeout_circ 0.25 alpha 0.0
            easein_quad 0.25 alpha 1.1
            easeout_circ 0.25 alpha 0.0
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            repeat
            

    contains:
        "beach_massage_didac_back_pussy_over 04"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.5
            pause 0.25
            easeout_circ 0.25 alpha 0.0
            easein_quad 0.25 alpha 1.1
            easeout_circ 0.25 alpha 0.0
            pause 0.25
            pause 0.25
            pause 0.25
            repeat
            

    contains:
        "beach_massage_didac_back_pussy_over 05"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.5
            pause 0.25
            pause 0.25
            easeout_circ 0.25 alpha 0.0
            easein_quad 0.25 alpha 1.1
            easeout_circ 0.25 alpha 0.0
            pause 0.25
            pause 0.25
            repeat
            

    contains:
        "beach_massage_didac_back_pussy_over 06"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.5
            pause 0.25
            pause 0.25
            pause 0.25
            easeout_circ 0.25 alpha 0.0
            easein_quad 0.25 alpha 1.1
            easeout_circ 0.25 alpha 0.0
            pause 0.25
            repeat
            

    contains:
        "beach_massage_didac_back_pussy_over 07"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.5
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            easeout_circ 0.25 alpha 0.0
            easein_quad 0.25 alpha 1.1
            easeout_circ 0.25 alpha 0.0
            repeat
            

    contains:
        "beach_massage_didac_back_pussy_over 08"
        subpixel True
        truecenter
        alpha 0.0
        block:
            easeout_circ 0.5 alpha 0.0
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            pause 0.25
            easeout_circ 0.25 alpha 0.0
            easein_quad 0.25 alpha 1.1
            repeat
            
image beach_massage_didac_back_pussy_over_comp 02:

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "beach_massage_didac_back_pussy_over 01"
        subpixel True
        truecenter
        alpha 1.0
        block:
            easein_quad 0.2 alpha 1.1
            easeout_circ 0.1 alpha 0.0
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            easeout_circ 0.1 alpha 0.0
            repeat

    contains:
        "beach_massage_didac_back_pussy_over 02"
        subpixel True
        truecenter
        alpha 0.0
        block:
            easeout_circ 0.2 alpha 0.0
            easein_quad 0.1 alpha 1.1
            easeout_circ 0.1 alpha 0.0
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            repeat
            

    contains:
        "beach_massage_didac_back_pussy_over 03"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.2
            easeout_circ 0.1 alpha 0.0
            easein_quad 0.1 alpha 1.1
            easeout_circ 0.1 alpha 0.0
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            repeat
            

    contains:
        "beach_massage_didac_back_pussy_over 04"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.2
            pause 0.1
            easeout_circ 0.1 alpha 0.0
            easein_quad 0.1 alpha 1.1
            easeout_circ 0.1 alpha 0.0
            pause 0.1
            pause 0.1
            pause 0.1
            repeat
            

    contains:
        "beach_massage_didac_back_pussy_over 05"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.2
            pause 0.1
            pause 0.1
            easeout_circ 0.1 alpha 0.0
            easein_quad 0.1 alpha 1.1
            easeout_circ 0.1 alpha 0.0
            pause 0.1
            pause 0.1
            repeat
            

    contains:
        "beach_massage_didac_back_pussy_over 06"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.2
            pause 0.1
            pause 0.1
            pause 0.1
            easeout_circ 0.1 alpha 0.0
            easein_quad 0.1 alpha 1.1
            easeout_circ 0.1 alpha 0.0
            pause 0.1
            repeat
            

    contains:
        "beach_massage_didac_back_pussy_over 07"
        subpixel True
        truecenter
        alpha 0.0
        block:
            pause 0.2
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            easeout_circ 0.1 alpha 0.0
            easein_quad 0.1 alpha 1.1
            easeout_circ 0.1 alpha 0.0
            repeat
            

    contains:
        "beach_massage_didac_back_pussy_over 08"
        subpixel True
        truecenter
        alpha 0.0
        block:
            easeout_circ 0.2 alpha 0.0
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            pause 0.1
            easeout_circ 0.1 alpha 0.0
            easein_quad 0.1 alpha 1.1
            repeat

# BACK

image beach_massage_didac_back_back 01 = "images/day05/aftermorning/beach_massage_didac_back_back_01.webp"
image beach_massage_didac_back_back 02 = "images/day05/aftermorning/beach_massage_didac_back_back_02.webp"
image beach_massage_didac_back_back 03 = "images/day05/aftermorning/beach_massage_didac_back_back_03.webp"
image beach_massage_didac_back_back 04 = "images/day05/aftermorning/beach_massage_didac_back_back_04.webp"
image beach_massage_didac_back_back 05 = "images/day05/aftermorning/beach_massage_didac_back_back_05.webp"
image beach_massage_didac_back_back 06 = "images/day05/aftermorning/beach_massage_didac_back_back_06.webp"

image beach_massage_didac_back_back_comp 01: # Once Up

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "beach_massage_didac_back_back 01" with Dissolve (1.0)
        truecenter
        pause 3.5
        "beach_massage_didac_back_back 02" with Dissolve (1.0)
        pause 1.2
        "beach_massage_didac_back_back 03" with Dissolve (1.0)
        pause 1.2
        "beach_massage_didac_back_back 04" with Dissolve (1.0)
        pause 1.2
        "beach_massage_didac_back_back 05" with Dissolve (1.0)
        pause 1.2
        "beach_massage_didac_back_back 06" with Dissolve (1.0)
        pause 1.2


image beach_massage_didac_back_back_comp 02: # Repeat Up.

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "beach_massage_didac_back_back 01" with Dissolve (1.0)
        truecenter
        pause 0.75
        "beach_massage_didac_back_back 02" with Dissolve (0.25)
        pause 0.5
        "beach_massage_didac_back_back 03" with Dissolve (0.25)
        pause 0.5
        "beach_massage_didac_back_back 04" with Dissolve (0.25)
        pause 0.5
        "beach_massage_didac_back_back 05" with Dissolve (0.5)
        pause 0.5
        "beach_massage_didac_back_back 06" with Dissolve (0.5)
        pause 0.5
        repeat

image beach_massage_didac_back_back_comp 03: # Repeat Up-Down.

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "beach_massage_didac_back_back 01" with Dissolve (0.25)
        truecenter
        pause 0.5
        "beach_massage_didac_back_back 02" with Dissolve (0.25)
        pause 0.5
        "beach_massage_didac_back_back 03" with Dissolve (0.25)
        pause 0.5
        "beach_massage_didac_back_back 04" with Dissolve (0.25)
        pause 0.5
        "beach_massage_didac_back_back 05" with Dissolve (0.25)
        pause 0.5
        "beach_massage_didac_back_back 06" with Dissolve (0.25)
        pause 0.5
        "beach_massage_didac_back_back 05" with Dissolve (0.25)
        pause 0.5
        "beach_massage_didac_back_back 04" with Dissolve (0.25)
        pause 0.5
        "beach_massage_didac_back_back 03" with Dissolve (0.25)
        pause 0.5
        "beach_massage_didac_back_back 02" with Dissolve (0.25)
        pause 0.5
        repeat

    ## DIDAC FRONT MASSAGE images:
        ##################################################################################

# ABS

image beach_massage_didac_front_abs_bg = "images/day05/aftermorning/beach_massage_didac_front_abs_bg.webp"

image beach_massage_didac_front_abs_bgPROVE = "images/day05/aftermorning/beach_massage_didac_front_abs_bgPROVE.webp"
image beach_massage_didac_front_abs_hand_L 01 = "images/day05/aftermorning/beach_massage_didac_front_abs_hand_L_01.webp"
image beach_massage_didac_front_abs_hand_L 02 = "images/day05/aftermorning/beach_massage_didac_front_abs_hand_L_02.webp"
image beach_massage_didac_front_abs_hand_L 03 = "images/day05/aftermorning/beach_massage_didac_front_abs_hand_L_03.webp"
image beach_massage_didac_front_abs_hand_R 01 = "images/day05/aftermorning/beach_massage_didac_front_abs_hand_R_01.webp"
image beach_massage_didac_front_abs_hand_R 02 = "images/day05/aftermorning/beach_massage_didac_front_abs_hand_R_02.webp"
image beach_massage_didac_front_abs_hand_R 03 = "images/day05/aftermorning/beach_massage_didac_front_abs_hand_R_03.webp"

image beach_massage_didac_front_abs_comp 01:

    contains:
        "beach_massage_didac_front_abs_bg"
        truecenter

    contains:
        "beach_massage_didac_front_abs_hand_L 01"
        subpixel True
        transform_anchor True
        xalign 0.25 yalign 0.55# rotate from thumb
        xpos 0.51 ypos 0.205
        alpha 1.0
        parallel:
            easein_quad 0.5 alpha 1.1
            pause 6.0
            easein_quad 0.5 alpha 0.0
            pause 6.0
            pause 0.5
            pause 6.0
            repeat

        parallel:
            easein_quad 5.0 rotate 4
            easeout_quad 5.0 rotate -5
            repeat


    contains:
        "beach_massage_didac_front_abs_hand_R 01"
        subpixel True
        transform_anchor True
        xalign 0.7 yalign 0.85 # rotate from FINGERS
        xpos 0.4 ypos 0.22
        alpha 1.0
        parallel:
            easein_quad 0.5 alpha 1.0
            pause 6.0
            easein_quad 0.5 alpha 0.0
            pause 6.0
            pause 0.5
            pause 6.0
            repeat
        parallel:
            easein_quad 5.0 rotate 5
            easeout_quad 5.0 rotate -4
            repeat

    contains:
        "beach_massage_didac_front_abs_hand_L 02"
        subpixel True
        transform_anchor True
        xalign 0.45 yalign 0.95 # rotate from fingers
        xpos 0.685 ypos 0.56
        alpha 0.0
        parallel:
            pause 0.5
            pause 6.0
            easein_quad 0.5 alpha 1.0
            pause 6.0
            easein_quad 0.5 alpha 0.0
            pause 6.0
            repeat
        parallel:
            easein_quad 5.0 rotate 3
            easeout_quad 5.0 rotate -2
            repeat

    contains:
        "beach_massage_didac_front_abs_hand_R 02"
        subpixel True
        transform_anchor True
        xalign 0.73 yalign 0.87 # rotate from FINGERS
        xpos 0.56 ypos 0.42
        alpha 0.0
        parallel:
            pause 0.5
            pause 6.0
            easein_quad 0.5 alpha 1.0
            pause 6.0
            easein_quad 0.5 alpha 0.0
            pause 6.0
            repeat
        parallel:
            easein_quad 5.0 rotate 2
            easeout_quad 5.0 rotate -3
            repeat

    contains:
        "beach_massage_didac_front_abs_hand_L 03"
        subpixel True
        transform_anchor True
        xalign 0.2 yalign 0.5 # rotate from thumb
        xpos 0.57 ypos 0.04
        alpha 0.0
        parallel:
            easein_quad 0.5 alpha 0.0
            pause 6.0
            pause 0.5
            pause 6.0
            easein_quad 0.5 alpha 1.0
            pause 6.0
            repeat
        parallel:
            easein_quad 5.0 rotate 5
            easeout_quad 5.0 rotate -5
            repeat

    contains:
        "beach_massage_didac_front_abs_hand_R 03"
        subpixel True
        transform_anchor True
        xalign 0.7 yalign 0.5  # rotate from FINGERS
        xpos 0.475 ypos 0.025
        alpha 0.0
        parallel:
            easein_quad 0.5 alpha 0.0
            pause 6.0
            pause 0.5
            pause 6.0
            easein_quad 0.5 alpha 1.0
            pause 6.0
            repeat
        parallel:
            easein_quad 5.0 rotate 5
            easeout_quad 5.0 rotate -5
            repeat




# ARMS

image beach_massage_didac_front_arms_bg = "images/day05/aftermorning/beach_massage_didac_front_arms_bg.webp"

# BOOBS

image beach_massage_didac_front_boobs 01 = "images/day05/aftermorning/beach_massage_didac_front_boobs_01.webp"
image beach_massage_didac_front_boobs 02 = "images/day05/aftermorning/beach_massage_didac_front_boobs_02.webp"
image beach_massage_didac_front_boobs 03 = "images/day05/aftermorning/beach_massage_didac_front_boobs_03.webp"
image beach_massage_didac_front_boobs 04 = "images/day05/aftermorning/beach_massage_didac_front_boobs_04.webp"
image beach_massage_didac_front_boobs 05 = "images/day05/aftermorning/beach_massage_didac_front_boobs_05.webp"
image beach_massage_didac_front_boobs 06 = "images/day05/aftermorning/beach_massage_didac_front_boobs_06.webp"
image beach_massage_didac_front_boobs 07 = "images/day05/aftermorning/beach_massage_didac_front_boobs_07.webp"
image beach_massage_didac_front_boobs 08 = "images/day05/aftermorning/beach_massage_didac_front_boobs_08.webp"

image beach_massage_didac_front_boobs_comp 01:

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "beach_massage_didac_front_boobs 01" with Dissolve (0.3)
        truecenter
        pause 0.5
        "beach_massage_didac_front_boobs 02" with Dissolve (0.3)
        pause 0.5
        "beach_massage_didac_front_boobs 03" with Dissolve (0.3)
        pause 0.5
        "beach_massage_didac_front_boobs 04" with Dissolve (0.3)
        pause 0.5
        "beach_massage_didac_front_boobs 05" with Dissolve (0.3)
        pause 0.5
        "beach_massage_didac_front_boobs 06" with Dissolve (0.3)
        pause 0.5
        "beach_massage_didac_front_boobs 07" with Dissolve (0.3)
        pause 0.5
        "beach_massage_didac_front_boobs 08" with Dissolve (0.3)
        pause 0.5
        repeat

image beach_massage_didac_front_boobs_comp 02:

    contains:
        "black"
        truecenter
        zoom 2.0

    contains:
        "beach_massage_didac_front_boobs 01" with Dissolve (0.1)
        truecenter
        pause 0.15
        "beach_massage_didac_front_boobs 02" with Dissolve (0.1)
        pause 0.15
        "beach_massage_didac_front_boobs 03" with Dissolve (0.1)
        pause 0.15
        "beach_massage_didac_front_boobs 04" with Dissolve (0.1)
        pause 0.15
        "beach_massage_didac_front_boobs 05" with Dissolve (0.1)
        pause 0.15
        "beach_massage_didac_front_boobs 06" with Dissolve (0.1)
        pause 0.15
        "beach_massage_didac_front_boobs 07" with Dissolve (0.1)
        pause 0.15
        "beach_massage_didac_front_boobs 08" with Dissolve (0.1)
        pause 0.15
        repeat

# LEGS

image beach_massage_didac_front_legs_bg = "images/day05/aftermorning/beach_massage_didac_front_legs_bg.webp"

image beach_massage_didac_front_legs_bgPROVE = "images/day05/aftermorning/beach_massage_didac_front_legs_bgPROVE.webp"

image beach_massage_didac_front_legs_hand_L 01 = "images/day05/aftermorning/beach_massage_didac_front_legs_hand_L_01.webp"
image beach_massage_didac_front_legs_hand_L 02 = "images/day05/aftermorning/beach_massage_didac_front_legs_hand_L_02.webp"
image beach_massage_didac_front_legs_hand_L 03 = "images/day05/aftermorning/beach_massage_didac_front_legs_hand_L_03.webp"

image beach_massage_didac_front_legs_hand_R 01 = "images/day05/aftermorning/beach_massage_didac_front_legs_hand_R_01.webp"
image beach_massage_didac_front_legs_hand_R 02 = "images/day05/aftermorning/beach_massage_didac_front_legs_hand_R_02.webp"
image beach_massage_didac_front_legs_hand_R 03 = "images/day05/aftermorning/beach_massage_didac_front_legs_hand_R_03.webp"

transform beach_massage_didac_front_legs_rotation:
    subpixel True
    easein_quad 2.0 rotate 5
    easeout_quad 2.0 rotate -5
    repeat


image beach_massage_didac_front_legs_comp 01:

    contains:
        "beach_massage_didac_front_legs_bg"
        truecenter

    contains:
        "beach_massage_didac_front_legs_hand_L 01"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.635 ypos 0.26
        alpha 1.0

        parallel:
            easein_quad 0.5 alpha 1.0 # 01
            pause 5.0
            easein_quad 0.5 alpha 0.0 # 02
            pause 5.0
            pause 0.5 # 03
            pause 5.0
            repeat
        parallel:
            beach_massage_didac_front_legs_rotation

    contains:
        "beach_massage_didac_front_legs_hand_R 01"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.335 ypos 0.645
        alpha 0.0

        parallel:
            easein_quad 0.5 alpha 1.0 # 01
            pause 5.0
            easein_quad 0.5 alpha 0.0 # 02
            pause 5.0
            pause 0.5 # 03
            pause 5.0
            repeat
        parallel:
            beach_massage_didac_front_legs_rotation

    contains:
        "beach_massage_didac_front_legs_hand_L 02"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 1.135 ypos 0.26
        alpha 0.0

        parallel:
            pause 0.5
            pause 5.0
            easein_quad 0.5 alpha 1.0 # 02
            pause 5.0
            easein_quad 0.5 alpha 0.0 # 03
            pause 5.0
            repeat
        parallel:
            easein_quad 2.0 rotate -1
            easeout_quad 2.0 rotate 1
            repeat

    contains:
        "beach_massage_didac_front_legs_hand_R 02"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.772 ypos 0.31
        alpha 0.0

        parallel:
            pause 0.5
            pause 5.0
            easein_quad 0.5 alpha 1.0 # 02
            pause 5.0
            easein_quad 0.5 alpha 0.0 # 03
            pause 5.0
            repeat
        parallel:
            beach_massage_didac_front_legs_rotation

    contains:
        "beach_massage_didac_front_legs_hand_L 03"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 1.12 ypos 0.225
        alpha 0.0

        parallel:
            easein_quad 0.5 alpha 0.0 # 01
            pause 5.0
            pause 0.5
            pause 5.0
            easein_quad 0.5 alpha 1.0 # 03
            pause 5.0
            repeat
        parallel:
            beach_massage_didac_front_legs_rotation

    contains:
        "beach_massage_didac_front_legs_hand_R 03"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.785 ypos 0.11
        alpha 0.0

        parallel:
            easein_quad 0.5 alpha 0.0 # 01
            pause 5.0
            pause 0.5
            pause 5.0
            easein_quad 0.5 alpha 1.0 # 03
            pause 5.0
            repeat
        parallel:
            beach_massage_didac_front_legs_rotation

image beach_massage_didac_front_legs_comp 02:

    contains:
        "beach_massage_didac_front_legs_bg"
        truecenter

    contains:
        "beach_massage_didac_front_legs_hand_L 01"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.635 ypos 0.26
        alpha 1.0

        parallel:
            easein_quad 0.5 alpha 1.0 # 01
            pause 5.0
            easein_quad 0.5 alpha 0.0 # 02
            pause 5.0
            pause 0.5 # 03
            pause 5.0
            pause 0.5 # 02
            pause 5.0
            repeat
        parallel:
            beach_massage_didac_front_legs_rotation

    contains:
        "beach_massage_didac_front_legs_hand_R 01"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.335 ypos 0.645
        alpha 0.0

        parallel:
            easein_quad 0.5 alpha 1.0 # 01
            pause 5.0
            easein_quad 0.5 alpha 0.0 # 02
            pause 5.0
            pause 0.5 # 03
            pause 5.0
            pause 0.5 # 02
            pause 5.0
            repeat
        parallel:
            beach_massage_didac_front_legs_rotation

    contains:
        "beach_massage_didac_front_legs_hand_L 02"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 1.135 ypos 0.26
        alpha 0.0

        parallel:
            easein_quad 0.5 alpha 0.0 # 01
            pause 5.0
            easein_quad 0.5 alpha 1.0 # 02
            pause 5.0
            easein_quad 0.5 alpha 0.0 # 03
            pause 5.0
            easein_quad 0.5 alpha 1.0 # 02
            pause 5.0
            repeat
        parallel:
            easein_quad 2.0 rotate -1
            easeout_quad 2.0 rotate 1
            repeat

    contains:
        "beach_massage_didac_front_legs_hand_R 02"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.772 ypos 0.31
        alpha 0.0

        parallel:
            easein_quad 0.5 alpha 0.0 # 01
            pause 5.0
            easein_quad 0.5 alpha 1.0 # 02
            pause 5.0
            easein_quad 0.5 alpha 0.0 # 03
            pause 5.0
            easein_quad 0.5 alpha 1.0 # 02
            pause 5.0
            repeat
        parallel:
            beach_massage_didac_front_legs_rotation

    contains:
        "beach_massage_didac_front_legs_hand_L 03"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 1.12 ypos 0.225
        alpha 0.0

        parallel:
            pause 0.5 # 01
            pause 5.0
            pause 0.5 # 02
            pause 5.0
            easein_quad 0.5 alpha 1.0 # 03
            pause 5.0
            easein_quad 0.5 alpha 0.0 # 02
            pause 5.0
            repeat
        parallel:
            beach_massage_didac_front_legs_rotation

    contains:
        "beach_massage_didac_front_legs_hand_R 03"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos 0.785 ypos 0.11
        alpha 0.0

        parallel:
            pause 0.5 # 01
            pause 5.0
            pause 0.5 # 02
            pause 5.0
            easein_quad 0.5 alpha 1.0 # 03
            pause 5.0
            easein_quad 0.5 alpha 0.0 # 02
            pause 5.0
            repeat
        parallel:
            beach_massage_didac_front_legs_rotation

# NECK
    # ear

image beach_massage_didac_front_neck_ear_bg = "images/day05/aftermorning/beach_massage_didac_front_neck_ear_bg.webp"

    # massage

image beach_massage_didac_front_neck_massage 01 = "images/day05/aftermorning/beach_massage_didac_front_neck_massage_01.webp"
image beach_massage_didac_front_neck_massage 02 = "images/day05/aftermorning/beach_massage_didac_front_neck_massage_02.webp"
image beach_massage_didac_front_neck_massage 03 = "images/day05/aftermorning/beach_massage_didac_front_neck_massage_03.webp"
image beach_massage_didac_front_neck_massage 04 = "images/day05/aftermorning/beach_massage_didac_front_neck_massage_04.webp"

image beach_massage_didac_front_neck_massage_comp 01:

    contains:
        "beach_massage_didac_front_neck_massage 01" with Dissolve (0.3)
        truecenter
        pause 0.75
        "beach_massage_didac_front_neck_massage 02" with Dissolve (0.3)
        pause 0.75
        "beach_massage_didac_front_neck_massage 03" with Dissolve (0.3)
        pause 0.75
        "beach_massage_didac_front_neck_massage 04" with Dissolve (0.3)
        pause 0.75
        repeat

image beach_massage_didac_front_neck_massage_comp 02:

    contains:
        "beach_massage_didac_front_neck_massage 01" with Dissolve (0.2)
        truecenter
        pause 0.4
        "beach_massage_didac_front_neck_massage 02" with Dissolve (0.2)
        pause 0.4
        "beach_massage_didac_front_neck_massage 03" with Dissolve (0.2)
        pause 0.4
        "beach_massage_didac_front_neck_massage 04" with Dissolve (0.2)
        pause 0.4
        repeat


    # strangle
image beach_massage_didac_front_neck_strangle 01 = "images/day05/aftermorning/beach_massage_didac_front_neck_strangle_01.webp"

image beach_massage_didac_front_neck_chocking 01 = "images/day05/aftermorning/beach_massage_didac_front_neck_chocking_01.webp"

image beach_sky_crowd 01 = "images/day05/aftermorning/beach_sky_crowd_01.webp"


# PUSSY (front)

image beach_massage_didac_front_pussy_bgPROVE = "images/day05/aftermorning/beach_massage_didac_front_pussy_bgPROVE.webp"

image beach_massage_didac_front_pussy_bg = "images/day05/aftermorning/beach_massage_didac_front_pussy_bg.webp"

image beach_massage_didac_front_pussy_blegs 01 = "images/day05/aftermorning/beach_massage_didac_front_pussy_blegs_01.webp"
image beach_massage_didac_front_pussy_blegs 02 = "images/day05/aftermorning/beach_massage_didac_front_pussy_blegs_02.webp"

image beach_massage_didac_front_pussy_blegs_mccum 02 = "images/day05/aftermorning/beach_massage_didac_front_pussy_blegs_mccum_02.webp"

image beach_massage_didac_front_pussy_cum 01 = "images/day05/aftermorning/beach_massage_didac_front_pussy_cum_01.webp"

image beach_massage_didac_front_pussy_body 01 = "images/day05/aftermorning/beach_massage_didac_front_pussy_body_01.webp"
image beach_massage_didac_front_pussy_body 02 = "images/day05/aftermorning/beach_massage_didac_front_pussy_body_02.webp"

image beach_massage_didac_front_pussy_body_mccum 02 = "images/day05/aftermorning/beach_massage_didac_front_pussy_body_mccum_02.webp"

image beach_massage_didac_front_pussy_hand_R 01 = "images/day05/aftermorning/beach_massage_didac_front_pussy_hand_R_01.webp"
image beach_massage_didac_front_pussy_hand_R 02 = "images/day05/aftermorning/beach_massage_didac_front_pussy_hand_R_02.webp"
image beach_massage_didac_front_pussy_hand_R 03 = "images/day05/aftermorning/beach_massage_didac_front_pussy_hand_R_03.webp"

image beach_massage_didac_front_pussy_hand_L 01 = "images/day05/aftermorning/beach_massage_didac_front_pussy_hand_L_01.webp"



image beach_massage_didac_front_pussy_comp 00a: # when she has her legs closed

    contains:
        "beach_massage_didac_front_pussy_bg"
        truecenter
# body

    contains:
        "beach_massage_didac_front_pussy_body 01"
        truecenter

# legs
    contains:
        "beach_massage_didac_front_pussy_blegs 01"
        truecenter

image beach_massage_didac_front_pussy_comp 00b: # when she has her legs open

    contains:
        "beach_massage_didac_front_pussy_bg"
        truecenter
# body

    contains:
        "beach_massage_didac_front_pussy_body 02"
        truecenter

# legs
    contains:
        "beach_massage_didac_front_pussy_blegs 02"
        truecenter

image beach_massage_didac_front_pussy_comp 02: # when fingers are alredy in position instead of comming from outside.

    contains:
        "beach_massage_didac_front_pussy_bg"
        truecenter
# body

    contains:
        "beach_massage_didac_front_pussy_body 01"
        truecenter
        alpha 1.0

    contains:
        "beach_massage_didac_front_pussy_body 02"
        truecenter
        alpha 0.0

# legs
    contains:
        "beach_massage_didac_front_pussy_blegs 01"
        truecenter
        alpha 1.0

    contains:
        "beach_massage_didac_front_pussy_blegs 02"
        truecenter
        alpha 0.0

# hand L
    contains:
        "beach_massage_didac_front_pussy_hand_L 01"
        subpixel True
        transform_anchor True
        xalign 0.48 yalign 0.82 alpha 1.0
        xpos 0.785 ypos 0.49
        block:
            parallel:
                easein_quad 2.4 xpos 0.8
                easeout_quad 2.3 xpos 0.75
                repeat

            parallel:
                easein_quad 1.9 ypos 0.55 #0.45
                easeout_quad 2.1 ypos 0.6 #0.52
                repeat

            parallel:
                easein_quad 3.8 rotate 20
                easeout_quad 3.3 rotate -20
                repeat

            #xpos 0.8 ypos 0.45 rotate 20 #TopRight
            #xpos 0.75 ypos 0.52 rotate -40 #DownLeft


# hand R

    contains:
        "beach_massage_didac_front_pussy_hand_R 01"
        subpixel True
        transform_anchor True
        xalign 0.63 yalign 0.88 alpha 1.0
        xpos 0.822 ypos 0.825 # Origin
        block:
            parallel:
                easein_quad 2.2 xpos 0.74
                easeout_quad 2.3 xpos 0.78
                repeat
            parallel:
                easein_quad 3.2 ypos 0.52
                easeout_quad 3.4 ypos 0.85
                repeat
            parallel:
                easein_quad 2.55 rotate -30
                easeout_quad 2.53 rotate 30
                repeat

            #xpos 0.74 ypos 0.52 rotate -30 # Top
            #xpos 0.78 ypos 0.85 rotate 30 # Down


    contains:
        "beach_massage_didac_front_pussy_hand_R 02"
        transform_anchor True
        xalign 0.5 yalign 0.5 alpha 0.0
        xpos 0.785 ypos 0.705

    contains:
        "beach_massage_didac_front_pussy_hand_R 03"
        transform_anchor True
        xalign 0.5 yalign 0.5 alpha 0.0
        xpos 0.785 ypos 0.75


image beach_massage_didac_front_pussy_comp 03:

    contains:
        "beach_massage_didac_front_pussy_bg"
        truecenter
# body

    contains:
        "beach_massage_didac_front_pussy_body 01"
        subpixel True
        truecenter
        block:
            easein_quad 1.9 ypos 0.495
            easeout_quad 2.1 ypos 0.51
            repeat

# legs
    contains:
        "beach_massage_didac_front_pussy_blegs 01"
        subpixel True
        truecenter
        block:
            easein_quad 1.9 ypos 0.48
            easeout_quad 2.1 ypos 0.55
            repeat

# hand L
    contains:
        "beach_massage_didac_front_pussy_hand_L 01"
        subpixel True
        transform_anchor True
        xalign 0.48 yalign 0.82 alpha 1.0
        xpos 0.785 ypos 0.49
        block:
            parallel:
                easein_quad 2.4 xpos 0.8
                easeout_quad 2.3 xpos 0.75
                repeat

            parallel:
                easein_quad 1.9 ypos 0.55 #0.45
                easeout_quad 2.1 ypos 0.6 #0.52
                repeat

            parallel:
                easein_quad 3.8 rotate 20
                easeout_quad 3.3 rotate -20
                repeat

# hand R

    contains:
        "beach_massage_didac_front_pussy_hand_R 02"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5 alpha 1.0
        xpos 0.785 ypos 0.705
        block:
            parallel:
                easein_quad 2.4 xpos 0.82
                easeout_quad 2.3 xpos 0.75
                repeat

            parallel:
                easein_quad 1.9 ypos 0.65
                easeout_quad 2.1 ypos 0.75
                repeat

            parallel:
                easein_quad 2.2 rotate -20
                easeout_quad 2.3 rotate 20
                repeat
            #xpos 0.82 ypos 0.6 rotate -30 #TopRight
            #xpos 0.75 ypos 0.75 rotate 30 # LowLeft

image beach_massage_didac_front_pussy_comp 04:

    contains:
        "beach_massage_didac_front_pussy_bg"
        truecenter
# body

    contains:
        "beach_massage_didac_front_pussy_body 01"
        subpixel True
        truecenter
        block:
            parallel:
                easein_quad 1.8 ypos 0.49
                easeout_quad 2.0 ypos 0.52
                repeat

            parallel:
                easein_quad 2.2 xpos 0.495
                easeout_quad 2.4 xpos 0.51
                repeat

            parallel:
                easein_quad 1.9 rotate -1
                easeout_quad 2.0 rotate 1
                repeat


# legs
    contains:
        "beach_massage_didac_front_pussy_blegs 01"
        subpixel True
        truecenter
        block:
            parallel:
                easein_quad 1.8 ypos 0.47
                easeout_quad 2.0 ypos 0.58
                repeat
            parallel:
                easein_quad 2.2 xpos 0.52
                easeout_quad 2.4 xpos 0.51
                repeat
            parallel:
                easein_quad 1.9 rotate -3
                easeout_quad 2.0 rotate 3
                repeat

# hand L
    contains:
        "beach_massage_didac_front_pussy_hand_L 01"
        subpixel True
        transform_anchor True
        xalign 0.48 yalign 0.82 alpha 1.0
        xpos 0.785 ypos 0.49
        block:
            parallel:
                easein_quad 2.4 xpos 0.8
                easeout_quad 2.3 xpos 0.75
                repeat

            parallel:
                easein_quad 1.9 ypos 0.55 #0.45
                easeout_quad 2.1 ypos 0.6 #0.52
                repeat

            parallel:
                easein_quad 3.8 rotate 20
                easeout_quad 3.3 rotate -20
                repeat

# hand R

    contains:
        "beach_massage_didac_front_pussy_hand_R 03"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5 alpha 1.0
        xpos 0.785 ypos 0.75
        block:
            parallel:
                easein_quad 2.4 xpos 0.8
                easeout_quad 2.3 xpos 0.75
                repeat

            parallel:
                easein_quad 1.9 ypos 0.7
                easeout_quad 2.1 ypos 0.8
                repeat

            parallel:
                easein_quad 2.2 rotate -20
                easeout_quad 2.3 rotate 20
                repeat
            #xpos 0.8 ypos 0.7 rotate -20
            #xpos 0.75 ypos 0.8 rotate 20

image beach_massage_didac_front_pussy_comp 05: # Faster

    contains:
        "beach_massage_didac_front_pussy_bg"
        truecenter
# body

    contains:
        "beach_massage_didac_front_pussy_body 01"
        subpixel True
        truecenter
        block:
            parallel:
                easein_quad 1.2 ypos 0.49
                easeout_quad 2.0 ypos 0.52
                repeat

            parallel:
                easein_quad 1.2 xpos 0.495
                easeout_quad 1.4 xpos 0.51
                repeat

            parallel:
                easein_quad 1.1 rotate -1
                easeout_quad 1.0 rotate 1
                repeat


# legs
    contains:
        "beach_massage_didac_front_pussy_blegs 01"
        subpixel True
        truecenter
        block:
            parallel:
                easein_quad 0.8 ypos 0.47
                easeout_quad 1.0 ypos 0.58
                repeat
            parallel:
                easein_quad 1.2 xpos 0.52
                easeout_quad 1.4 xpos 0.51
                repeat
            parallel:
                easein_quad 0.9 rotate -3
                easeout_quad 1.0 rotate 3
                repeat

# hand L
    contains:
        "beach_massage_didac_front_pussy_hand_L 01"
        subpixel True
        transform_anchor True
        xalign 0.48 yalign 0.82 alpha 1.0
        xpos 0.785 ypos 0.49
        block:
            parallel:
                easein_quad 1.0 xpos 0.8
                easeout_quad 0.9 xpos 0.75
                repeat

            parallel:
                easein_quad 0.7 ypos 0.55 #0.45
                easeout_quad 0.9 ypos 0.6 #0.52
                repeat

            parallel:
                easein_quad 1.8 rotate 20
                easeout_quad 1.3 rotate -20
                repeat

# hand R

    contains:
        "beach_massage_didac_front_pussy_hand_R 03"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5 alpha 1.0
        xpos 0.785 ypos 0.75
        block:
            parallel:
                easein_quad 1.4 xpos 0.8
                easeout_quad 1.3 xpos 0.75
                repeat

            parallel:
                easein_quad 0.9 ypos 0.7
                easeout_quad 1.1 ypos 0.8
                repeat

            parallel:
                easein_quad 1.2 rotate -20
                easeout_quad 1.3 rotate 20
                repeat
            #xpos 0.8 ypos 0.7 rotate -20
            #xpos 0.75 ypos 0.8 rotate 20

image beach_massage_didac_front_pussy_comp 06: # She´s Convulsing.

    contains:
        "beach_massage_didac_front_pussy_bg"
        truecenter
# body

    contains:
        "beach_massage_didac_front_pussy_body 01"
        subpixel True
        truecenter
        block:
            parallel:
                easein_quad 0.5 ypos 0.48
                easeout_quad 0.3 ypos 0.53
                repeat

            parallel:
                easein_quad 0.6 xpos 0.49
                easeout_quad 0.4 xpos 0.52
                repeat

            parallel:
                easein_quad 0.4 rotate -2
                easeout_quad 0.3 rotate 3
                repeat


# legs
    contains:
        "beach_massage_didac_front_pussy_blegs 01"
        subpixel True
        truecenter
        block:
            parallel:
                easein_quad 0.1 ypos 0.45
                easeout_quad 0.05 ypos 0.55
                easein_quad 0.1 ypos 0.45
                easeout_quad 0.08 ypos 0.55
                easein_quad 0.12 ypos 0.45
                easeout_quad 0.04 ypos 0.55
                easein_quad 0.13 ypos 0.45
                easeout_quad 0.07 ypos 0.55
                easein_quad 0.16 ypos 0.45
                easeout_quad 0.05 ypos 0.55
                #
                easein_quad 0.3 ypos 0.45
                easeout_quad 0.1 ypos 0.55
                easein_quad 0.2 ypos 0.45
                #
                repeat
            parallel:
                easein_quad 0.6 xpos 0.52
                easeout_quad 0.7 xpos 0.51
                repeat
            parallel:
                easein_quad 0.7 rotate -3
                easeout_quad 0.4 rotate 3
                repeat

# hand L
    contains:
        "beach_massage_didac_front_pussy_hand_L 01"
        subpixel True
        transform_anchor True
        xalign 0.48 yalign 0.82 alpha 1.0
        xpos 0.785 ypos 0.49
        block:
            parallel:
                easein_quad 1.0 xpos 0.8
                easeout_quad 0.9 xpos 0.75
                repeat

            parallel:
                easein_quad 0.7 ypos 0.55 #0.45
                easeout_quad 0.9 ypos 0.6 #0.52
                repeat

            parallel:
                easein_quad 1.8 rotate 20
                easeout_quad 1.3 rotate -20
                repeat

# hand R

    contains:
        "beach_massage_didac_front_pussy_hand_R 03"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5 alpha 1.0
        xpos 0.785 ypos 0.75
        block:
            parallel:
                easein_quad 0.41 xpos 0.8
                easeout_quad 0.33 xpos 0.75
                repeat

            parallel:
                easein_quad 0.22 ypos 0.6
                easeout_quad 0.11 ypos 0.9
                repeat

            parallel:
                easein_quad 0.61 rotate -20
                easeout_quad 0.42 rotate 20
                repeat
            #xpos 0.8 ypos 0.7 rotate -20
            #xpos 0.75 ypos 0.8 rotate 20
            #

image beach_massage_didac_front_pussy_comp 07: # After Cum

    contains:
        "beach_massage_didac_front_pussy_bg"
        truecenter
# body

    contains:
        "beach_massage_didac_front_pussy_body 02"
        subpixel True
        truecenter
        block:
            parallel:
                easein_quad 0.5 ypos 0.48
                easeout_quad 0.3 ypos 0.53
                repeat

            parallel:
                easein_quad 0.6 xpos 0.49
                easeout_quad 0.4 xpos 0.52
                repeat

            parallel:
                easein_quad 0.4 rotate -2
                easeout_quad 0.3 rotate 3
                repeat


# legs
    contains:
        "beach_massage_didac_front_pussy_blegs 02"
        subpixel True
        truecenter
        block:
            parallel:
                easein_quad 0.1 ypos 0.45
                easeout_quad 0.05 ypos 0.55
                easein_quad 0.1 ypos 0.45
                easeout_quad 0.08 ypos 0.55
                easein_quad 0.12 ypos 0.45
                easeout_quad 0.04 ypos 0.55
                easein_quad 0.13 ypos 0.45
                easeout_quad 0.07 ypos 0.55
                easein_quad 0.16 ypos 0.45
                easeout_quad 0.05 ypos 0.55
                #
                easein_quad 0.3 ypos 0.45
                easeout_quad 0.1 ypos 0.55
                easein_quad 0.2 ypos 0.45
                #
                repeat
            parallel:
                easein_quad 0.6 xpos 0.52
                easeout_quad 0.7 xpos 0.51
                repeat
            parallel:
                easein_quad 0.7 rotate -3
                easeout_quad 0.4 rotate 3
                repeat

    contains:
        "red"
        truecenter
        zoom 5.0 alpha 0.0

# Didac Cumshot

    contains:
        "beach_massage_didac_front_pussy_cum 01"
        subpixel True
        transform_anchor True
        xalign 0.95 yalign 0.5 alpha 1.0
        xpos 0.8 ypos 0.45
        xzoom 0.001 yzoom 0.01 rotate 40 #Origin
        linear 0.3 xzoom 1.0 yzoom 0.5 rotate 20 # Normal
        linear 0.4 xzoom 1.5 yzoom 1.5 rotate -20 alpha 0.0 # disappear
        pause 0.1
        
        xzoom 0.001 yzoom 0.01 rotate 45 alpha 1.0 #Origin
        linear 0.2 xzoom 1.2 yzoom 0.4 rotate 25 # Normal
        linear 0.3 xzoom 1.5 yzoom 1.5 rotate -26 alpha 0.0 # disappear
        pause 0.5

        xzoom 0.001 yzoom 0.01 rotate 42 alpha 1.0 #Origin
        linear 0.3 xzoom 1.1 yzoom 0.6 rotate 18 # Normal
        linear 0.4 xzoom 1.5 yzoom 1.5 rotate -30 alpha 0.0 # disappear

# hand L
    contains:
        "beach_massage_didac_front_pussy_hand_L 01"
        subpixel True
        transform_anchor True
        xalign 0.48 yalign 0.82 alpha 1.0
        xpos 0.785 ypos 0.49
        block:
            parallel:
                easein_quad 1.0 xpos 0.8
                easeout_quad 0.9 xpos 0.75
                repeat

            parallel:
                easein_quad 0.7 ypos 0.5 #0.35
                easeout_quad 0.9 ypos 0.43 #0.22
                repeat

            parallel:
                easein_quad 1.8 rotate 20
                easeout_quad 1.3 rotate -20
                repeat

# hand R

    contains:
        "beach_massage_didac_front_pussy_hand_R 03"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5 alpha 0.0
        xpos 0.785 ypos 0.75
        block:
            parallel:
                easein_quad 1.4 xpos 0.8
                easeout_quad 1.3 xpos 0.75
                repeat

            parallel:
                easein_quad 1.05 ypos 0.5
                easeout_quad 1.1 ypos 0.6
                repeat

            parallel:
                easein_quad 1.6 rotate -20
                easeout_quad 1.4 rotate 20
                repeat
            #xpos 0.8 ypos 0.7 rotate -20
            #xpos 0.75 ypos 0.8 rotate 20
            #
            #

########################################################################


transform beach_massage_didac_front_pussy_body_move_08:
    subpixel True
    truecenter
    parallel:
        easein_quad 0.5 ypos 0.48
        easeout_quad 0.3 ypos 0.53
        repeat

    parallel:
        easein_quad 0.6 xpos 0.49
        easeout_quad 0.4 xpos 0.52
        repeat

    parallel:
        easein_quad 0.4 rotate -2
        easeout_quad 0.3 rotate 3
        repeat


transform beach_massage_didac_front_pussy_legs_move_08:
    subpixel True
    truecenter
    parallel:
        easein_quad 0.1 ypos 0.45
        easeout_quad 0.05 ypos 0.55
        easein_quad 0.1 ypos 0.45
        easeout_quad 0.08 ypos 0.55
        easein_quad 0.12 ypos 0.45
        easeout_quad 0.04 ypos 0.55
        easein_quad 0.13 ypos 0.45
        easeout_quad 0.07 ypos 0.55
        easein_quad 0.16 ypos 0.45
        easeout_quad 0.05 ypos 0.55
        #
        easein_quad 0.3 ypos 0.45
        easeout_quad 0.1 ypos 0.55
        easein_quad 0.2 ypos 0.45
        #
        repeat
    parallel:
        easein_quad 0.6 xpos 0.52
        easeout_quad 0.7 xpos 0.51
        repeat
    parallel:
        easein_quad 0.7 rotate -3
        easeout_quad 0.4 rotate 3
        repeat

transform beach_massage_didac_front_pussy_hand_L_08:
    subpixel True
    transform_anchor True
    xalign 0.48 yalign 0.82 alpha 1.0
    xpos 0.785 ypos 0.49
    block:
        parallel:
            easein_quad 1.0 xpos 0.8
            easeout_quad 0.9 xpos 0.75
            repeat

        parallel:
            easein_quad 0.7 ypos 0.5 #0.45
            easeout_quad 0.9 ypos 0.6 #0.52
            repeat

        parallel:
            easein_quad 1.8 rotate 20
            easeout_quad 1.3 rotate -20
            repeat

image beach_massage_didac_front_pussy_comp 08: # Taking Off Hands

    contains:
        "beach_massage_didac_front_pussy_bg"
        truecenter
# body

    contains:
        "beach_massage_didac_front_pussy_body 02"
        truecenter
        beach_massage_didac_front_pussy_body_move_08

    contains:
        ConditionSwitch(aftermorning05_SunScreenMassage_FrontParts_Complete_Cond == False, At("beach_massage_didac_front_pussy_body_mccum 02", beach_massage_didac_front_pussy_body_move_08),
                            "True", Null())
    #contains:
        #"beach_massage_didac_front_pussy_body_mccum 02"
        #truecenter
        #beach_massage_didac_front_pussy_body_move_08

# legs

    contains:
        "beach_massage_didac_front_pussy_blegs 02"
        truecenter
        beach_massage_didac_front_pussy_legs_move_08

    contains:
        ConditionSwitch(aftermorning05_SunScreenMassage_FrontParts_Complete_Cond == False, At("beach_massage_didac_front_pussy_blegs_mccum 02", beach_massage_didac_front_pussy_legs_move_08),
                            "True", Null())
    #contains:
        #"beach_massage_didac_front_pussy_blegs_mccum_ 02"
        #truecenter
        #beach_massage_didac_front_pussy_legs_move_08

    

# hand L
    contains:
        ConditionSwitch(aftermorning05_SunScreenMassage_FrontParts_Complete_Cond, At("beach_massage_didac_front_pussy_hand_L 01", beach_massage_didac_front_pussy_hand_L_08),
                            "True", Null())


###############################

transform beach_massage_didac_front_pussy_body_move_09:
    subpixel True
    truecenter
    parallel:
        easein_quad 1.5 ypos 0.48
        easeout_quad 1.3 ypos 0.53
        repeat

    parallel:
        easein_quad 1.6 xpos 0.49
        easeout_quad 1.4 xpos 0.52
        repeat

    parallel:
        easein_quad 1.4 rotate -2
        easeout_quad 1.3 rotate 3
        repeat

transform beach_massage_didac_front_pussy_legs_move_09:
    subpixel True
    truecenter
    parallel:
        easein_quad 0.8 ypos 0.45
        easeout_quad 0.09 ypos 0.55
        easein_quad 0.1 ypos 0.45
        easeout_quad 0.08 ypos 0.55
        easein_quad 0.15 ypos 0.45
        easeout_quad 0.14 ypos 0.55
        easein_quad 0.23 ypos 0.45
        easeout_quad 0.17 ypos 0.55
        easein_quad 0.26 ypos 0.45
        easeout_quad 0.15 ypos 0.55
        #
        easein_quad 2.3 ypos 0.45
        easeout_quad 3.1 ypos 0.55
        easein_quad 4.2 ypos 0.45
        #
        repeat
    parallel:
        easein_quad 1.6 xpos 0.52
        easeout_quad 1.7 xpos 0.51
        repeat
    parallel:
        easein_quad 1.7 rotate -3
        easeout_quad 1.4 rotate 3
        repeat

transform  beach_massage_didac_front_pussy_hand_L_09:
    subpixel True
    transform_anchor True
    xalign 0.48 yalign 0.82 alpha 1.0
    xpos 0.785 ypos 0.49
    block:
        parallel:
            easein_quad 2.0 xpos 0.8
            easeout_quad 1.9 xpos 0.75
            repeat

        parallel:
            easein_quad 1.7 ypos 0.5 # 0.45
            easeout_quad 1.9 ypos 0.6 # 0.52
            repeat

        parallel:
            easein_quad 2.8 rotate 20
            easeout_quad 2.3 rotate -20
            repeat

image beach_massage_didac_front_pussy_comp 09: # Relaxing

    contains:
        "beach_massage_didac_front_pussy_bg"
        truecenter


# body

    contains:
        "beach_massage_didac_front_pussy_body 02"
        truecenter
        beach_massage_didac_front_pussy_body_move_09

# body CUM

    contains:
        ConditionSwitch(aftermorning05_SunScreenMassage_FrontParts_Complete_Cond == False, At("beach_massage_didac_front_pussy_body_mccum 02", beach_massage_didac_front_pussy_body_move_09),
                            "True", Null())

# legs
    contains:
        "beach_massage_didac_front_pussy_blegs 02"
        truecenter
        beach_massage_didac_front_pussy_legs_move_09

# legs CUM

    contains:
        ConditionSwitch(aftermorning05_SunScreenMassage_FrontParts_Complete_Cond == False, At("beach_massage_didac_front_pussy_blegs_mccum 02", beach_massage_didac_front_pussy_legs_move_09),
                            "True", Null())

# hand L
    contains:
        ConditionSwitch(aftermorning05_SunScreenMassage_FrontParts_Complete_Cond, At("beach_massage_didac_front_pussy_hand_L 01", beach_massage_didac_front_pussy_hand_L_09),
                            "True", Null())

# hand R

##
## ##################################################################################
##################################################################################
##################################################################################
##


# Didac Masturbating MC Dick.

image beach_massage_mc_front_masturbation_PROVE = "images/day05/aftermorning/beach_massage_mc_front_masturbation_PROVE.webp"
image beach_massage_mc_front_masturbation_MC_body = "images/day05/aftermorning/beach_massage_mc_front_masturbation_MC_body.webp"
image beach_massage_mc_front_masturbation_d_arm_over = "images/day05/aftermorning/beach_massage_mc_front_masturbation_d_arm_over.webp"
image beach_massage_mc_front_masturbation_d_arm_below = "images/day05/aftermorning/beach_massage_mc_front_masturbation_d_arm_below.webp"

image beach_massage_mc_front_masturbation_mc_dick 01 = "images/day05/aftermorning/beach_massage_mc_front_masturbation_mc_dick_01.webp"
image beach_massage_mc_front_masturbation_mc_dick 02 = "images/day05/aftermorning/beach_massage_mc_front_masturbation_mc_dick_02.webp"
image beach_massage_mc_front_masturbation_mc_dick 03 = "images/day05/aftermorning/beach_massage_mc_front_masturbation_mc_dick_03.webp"

image beach_massage_mc_front_masturbation_mc_dick 01_wet01 = "images/day05/aftermorning/beach_massage_mc_front_masturbation_mc_dick_01_wet01.webp"
image beach_massage_mc_front_masturbation_mc_dick 01_wet02 = "images/day05/aftermorning/beach_massage_mc_front_masturbation_mc_dick_01_wet02.webp"
image beach_massage_mc_front_masturbation_mc_dick 01_wet03 = "images/day05/aftermorning/beach_massage_mc_front_masturbation_mc_dick_01_wet03.webp"
image beach_massage_mc_front_masturbation_mc_dick 01_wet03b = "images/day05/aftermorning/beach_massage_mc_front_masturbation_mc_dick_01_wet03b.webp"

image beach_massage_mc_front_masturbation_mc_cumshot 01 = "images/day05/aftermorning/beach_massage_mc_front_masturbation_mc_cumshot_01.webp"
image beach_massage_mc_front_masturbation_mc_cumshot 02 = "images/day05/aftermorning/beach_massage_mc_front_masturbation_mc_cumshot_02.webp"
image beach_massage_mc_front_masturbation_mc_cumshot 03 = "images/day05/aftermorning/beach_massage_mc_front_masturbation_mc_cumshot_03.webp"

transform beach_massage_mc_front_masturbation_d_arm_move_01:
    subpixel True
    transform_anchor True
    #xalign 0.85 yalign 0.85 #rotation Elbow
    #xpos 1.9 ypos 1.88 rotate 0 # origin
    #xpos 1.85 ypos 1.7 rotate -15 # down
    #xpos 1.75 ypos 1.8 rotate 15 # up
    xalign 0.25 yalign 0.2 # rotation Hand
    #xpos 0.48 ypos 0.4 rotate 0 #origin
    xpos 0.75 ypos 0.0 rotate 10 # up
    block:
        easein_quad 2.0 xpos 0.19 ypos 0.85 rotate -10 # down
        easeout_quad 2.0 xpos 0.75 ypos 0.0 rotate 10 # up
        repeat

transform beach_massage_mc_front_masturbation_d_arm_move_03:
    subpixel True #Masturbation Fast
    transform_anchor True
    xalign 0.25 yalign 0.2 # rotation Hand
    xpos 0.75 ypos 0.0 rotate 10 # up
    block:
        easein_quad 0.1 xpos 0.19 ypos 0.85 rotate -10 # down
        easeout_quad 0.1 xpos 0.75 ypos 0.0 rotate 10 # up
        repeat

transform beach_massage_mc_front_masturbation_d_arm_move_04:
    subpixel True #Cumming Hand
    transform_anchor True
    xalign 0.25 yalign 0.2 # rotation Hand
    xpos 0.7 ypos -0.2 rotate 10 # up
    block:
        easein_quad 2.0 xpos 0.19 ypos 0.85 rotate -10 # down
        easeout_quad 2.0 xpos 0.7 ypos -0.2 rotate 10 # up
        repeat

####

transform beach_massage_mc_front_masturbation_mc_dick_move_01:
    subpixel True
    easein_quad 2.0 xpos 0.06 ypos 1.23 yzoom 1.05 xzoom 0.95 rotate -60 # down
    easeout_quad 2.0 xpos 0.06 ypos 1.23 yzoom 0.95 xzoom 1.05 rotate -50 # up
    repeat

transform beach_massage_mc_front_masturbation_mc_dick_move_03:
    subpixel True # Masturbation Fast
    easein_quad 0.1 xpos 0.06 ypos 1.23 yzoom 1.05 xzoom 0.95 rotate -60 # down
    easeout_quad 0.1 xpos 0.06 ypos 1.23 yzoom 0.95 xzoom 1.05 rotate -50 # up
    repeat

transform beach_massage_mc_front_masturbation_mc_dick_move_02:
    subpixel True # Throbbing Cock
    parallel:
        easein_quad 3.0 xpos 0.06 ypos 1.23 rotate -57 # down
        easeout_quad 4.0 xpos 0.06 ypos 1.23 rotate -53 # up
        repeat
    parallel:
        easein_quad 0.5 yzoom 1.01 xzoom 1.0 # down
        easeout_quad 0.7 yzoom 0.99 xzoom 1.0 # up
        easein_quad 0.2 yzoom 1.01 xzoom 1.0 # down
        easeout_quad 0.5 yzoom 0.99 xzoom 1.0 # up
        repeat

transform beach_massage_mc_front_masturbation_mc_dick_move_04:
    subpixel True # Throbbing Cock
    parallel:
        easein_quad 2.0 xpos 0.06 ypos 1.23 rotate -56 # down
        easeout_quad 2.0 xpos 0.06 ypos 1.23 rotate -54 # up
        repeat
    parallel:
        easein_quad 0.1 yzoom 1.02 xzoom 1.0 # down
        easeout_quad 0.2 yzoom 0.98 xzoom 1.0 # up
        easein_quad 0.4 yzoom 1.03 xzoom 1.0 # down
        easeout_quad 0.5 yzoom 0.97 xzoom 1.0 # up
        repeat

image beach_massage_mc_front_masturbation_comp 01:

    contains :
        "beach_outsexy_bg_blur"
        truecenter
        zoom 1.5

    contains:
        "beach_massage_mc_front_masturbation_MC_body"
        truecenter
        alpha 1.0

    contains:
        "beach_massage_mc_front_masturbation_PROVE"
        truecenter
        alpha 0.0

    contains:
        "beach_massage_mc_front_masturbation_d_arm_below"
        beach_massage_mc_front_masturbation_d_arm_move_01

    contains:
        "beach_massage_mc_front_masturbation_mc_dick 01"
        transform_anchor True
        xalign 0.22 yalign 0.5 zoom 0.4
        #xpos 0.06 ypos 1.23 rotate -55 #Origin
        xpos 0.06 ypos 1.23 rotate -50 # up
        alpha 1.0
        parallel:
            beach_massage_mc_front_masturbation_mc_dick_move_01
        parallel:
            alpha 1.0

    contains:
        "beach_massage_mc_front_masturbation_mc_dick 02"
        subpixel True
        transform_anchor True
        xalign 0.22 yalign 0.5 zoom 0.4
        #xpos 0.06 ypos 1.23 rotate -55 #Origin
        xpos 0.06 ypos 1.23 rotate -50 # up
        alpha 0.0
        parallel:
            beach_massage_mc_front_masturbation_mc_dick_move_01
        parallel:
            easein_quad 0.5 alpha 1.0
            easeout_quad 0.5 alpha 0.0
            pause 0.5
            pause 0.5
            pause 0.5
            pause 0.5
            easein_quad 0.5 alpha 1.0
            easeout_quad 0.5 alpha 0.0
            repeat

    contains:
        "beach_massage_mc_front_masturbation_mc_dick 03"
        subpixel True
        transform_anchor True
        xalign 0.22 yalign 0.5 zoom 0.4
        #xpos 0.06 ypos 1.23 rotate -55 #Origin
        xpos 0.06 ypos 1.23 rotate -50 # up
        alpha 0.0
        parallel:
            beach_massage_mc_front_masturbation_mc_dick_move_01
        parallel:
            easeout_quad 0.5 alpha 0.0 # Up (Going Down)
            pause 0.5
            pause 0.5
            pause 0.5 #Down
            pause 0.5 # Down (Going Up)
            pause 0.5
            pause 0.5
            easein_quad 0.5 alpha 1.0 #Up
            repeat

    contains:
        "beach_massage_mc_front_masturbation_d_arm_over"
        beach_massage_mc_front_masturbation_d_arm_move_01


image beach_massage_mc_front_masturbation_comp 02: #Polla palpitando

    contains :
        "beach_outsexy_bg_blur"
        truecenter
        zoom 1.5

    contains:
        "beach_massage_mc_front_masturbation_MC_body"
        truecenter
        alpha 1.0

    contains:
        "beach_massage_mc_front_masturbation_PROVE"
        truecenter
        alpha 0.0


    contains:
        "beach_massage_mc_front_masturbation_mc_dick 01"
        transform_anchor True
        xalign 0.22 yalign 0.5 zoom 0.4
        #xpos 0.06 ypos 1.23 rotate -55 #Origin
        xpos 0.06 ypos 1.23 rotate -50 # up
        alpha 1.0
        block:
            beach_massage_mc_front_masturbation_mc_dick_move_02

image beach_massage_mc_front_masturbation_comp 03:

    contains :
        "beach_outsexy_bg_blur"
        truecenter
        zoom 1.5

    contains:
        "beach_massage_mc_front_masturbation_MC_body"
        truecenter
        alpha 1.0

    contains:
        "beach_massage_mc_front_masturbation_PROVE"
        truecenter
        alpha 0.0

    contains:
        "beach_massage_mc_front_masturbation_d_arm_below"
        beach_massage_mc_front_masturbation_d_arm_move_03

    contains:
        "beach_massage_mc_front_masturbation_mc_dick 01"
        transform_anchor True
        xalign 0.22 yalign 0.5 zoom 0.4
        #xpos 0.06 ypos 1.23 rotate -55 #Origin
        xpos 0.06 ypos 1.23 rotate -50 # up
        alpha 1.0
        parallel:
            beach_massage_mc_front_masturbation_mc_dick_move_03
        parallel:
            alpha 1.0

    contains:
        "beach_massage_mc_front_masturbation_mc_dick 02"
        subpixel True
        transform_anchor True
        xalign 0.22 yalign 0.5 zoom 0.4
        #xpos 0.06 ypos 1.23 rotate -55 #Origin
        xpos 0.06 ypos 1.23 rotate -50 # up
        alpha 0.0
        parallel:
            beach_massage_mc_front_masturbation_mc_dick_move_03
        parallel:
            easein_quad 0.025 alpha 1.0
            easeout_quad 0.025 alpha 0.0
            pause 0.025
            pause 0.025
            pause 0.025
            pause 0.025
            easein_quad 0.025 alpha 1.0
            easeout_quad 0.025 alpha 0.0
            repeat

    contains:
        "beach_massage_mc_front_masturbation_mc_dick 03"
        subpixel True
        transform_anchor True
        xalign 0.22 yalign 0.5 zoom 0.4
        #xpos 0.06 ypos 1.23 rotate -55 #Origin
        xpos 0.06 ypos 1.23 rotate -50 # up
        alpha 0.0
        parallel:
            beach_massage_mc_front_masturbation_mc_dick_move_03
        parallel:
            easeout_quad 0.025 alpha 0.0 # Up (Going Down)
            pause 0.025
            pause 0.025
            pause 0.025 #Down
            pause 0.025 # Down (Going Up)
            pause 0.025
            pause 0.025
            easein_quad 0.025 alpha 1.0 #Up
            repeat

    contains:
        "beach_massage_mc_front_masturbation_d_arm_over"
        beach_massage_mc_front_masturbation_d_arm_move_03

image beach_massage_mc_front_masturbation_comp 04: #Cumshot

    contains :
        "beach_outsexy_bg_blur"
        truecenter
        zoom 1.5

    contains:
        "beach_massage_mc_front_masturbation_MC_body"
        truecenter
        alpha 1.0

    contains:
        "beach_massage_mc_front_masturbation_PROVE"
        truecenter
        alpha 0.0

    contains:
        "beach_massage_mc_front_masturbation_mc_cumshot 01"
        transform_anchor True
        xalign 0.07 yalign 0.5
        alpha 0.0
        pause 2.0
        block:
            xpos 0.25 ypos 1.0 rotate -60 xzoom 0.01 yzoom 0.1 alpha 1.0 #Origin
            linear 0.5 xpos 0.85 ypos -0.3 rotate -55 xzoom 0.5 yzoom 0.3 #Spurt
            linear 0.5 xpos 1.5 ypos -0.9 rotate -20 xzoom 1.0 yzoom 1.8 alpha 0.0 #Falling
            pause 0.5
            repeat 3

    contains:
        "beach_massage_mc_front_masturbation_mc_cumshot 02"
        transform_anchor True
        xalign 0.07 yalign 0.5
        alpha 0.0
        pause 2.0
        block:
            pause 0.3
            xpos 0.25 ypos 1.0 rotate -60 xzoom 0.01 yzoom 0.1 alpha 1.0 #Origin
            linear 0.5 xpos 0.85 ypos -0.3 rotate -55 xzoom 0.5 yzoom 0.3 #Spurt
            linear 0.5 xpos 1.5 ypos -0.9 rotate -20 xzoom 1.0 yzoom 1.8 alpha 0.0 #Falling
            pause 0.125
            repeat 2

    contains:
        "beach_massage_mc_front_masturbation_mc_cumshot 03"
        transform_anchor True
        xalign 0.07 yalign 0.5
        alpha 0.0
        pause 2.0
        block:
            pause 0.5
            xpos 0.25 ypos 1.0 rotate -60 xzoom 0.01 yzoom 0.1 alpha 1.0 #Origin
            linear 0.5 xpos 0.85 ypos -0.3 rotate -55 xzoom 0.5 yzoom 0.3 #Spurt
            linear 0.5 xpos 1.5 ypos -0.9 rotate -20 xzoom 1.0 yzoom 1.8 alpha 0.0 #Falling
            pause 0.854
            repeat 3

    contains:
        "beach_massage_mc_front_masturbation_d_arm_below"
        beach_massage_mc_front_masturbation_d_arm_move_04

    contains:
        "beach_massage_mc_front_masturbation_mc_dick 01"
        transform_anchor True
        xalign 0.22 yalign 0.5 zoom 0.4
        #xpos 0.06 ypos 1.23 rotate -55 #Origin
        xpos 0.06 ypos 1.23 rotate -50 # up
        alpha 1.0
        parallel:
            beach_massage_mc_front_masturbation_mc_dick_move_04
        parallel:
            alpha 1.0

    contains:
        "beach_massage_mc_front_masturbation_mc_dick 02"
        subpixel True
        transform_anchor True
        xalign 0.22 yalign 0.5 zoom 0.4
        #xpos 0.06 ypos 1.23 rotate -55 #Origin
        xpos 0.06 ypos 1.23 rotate -50 # up
        alpha 0.0
        parallel:
            beach_massage_mc_front_masturbation_mc_dick_move_04
        parallel:
            easein_quad 0.5 alpha 1.0
            easeout_quad 0.5 alpha 0.0
            pause 0.5
            pause 0.5
            pause 0.5
            pause 0.5
            easein_quad 0.5 alpha 1.0
            easeout_quad 0.5 alpha 0.0
            repeat

    contains:
        "beach_massage_mc_front_masturbation_mc_dick 03"
        subpixel True
        transform_anchor True
        xalign 0.22 yalign 0.5 zoom 0.4
        #xpos 0.06 ypos 1.23 rotate -55 #Origin
        xpos 0.06 ypos 1.23 rotate -50 # up
        alpha 0.0
        parallel:
            beach_massage_mc_front_masturbation_mc_dick_move_04
        parallel:
            easeout_quad 0.5 alpha 0.0 # Up (Going Down)
            pause 0.5
            pause 0.5
            pause 0.5 #Down
            pause 0.5 # Down (Going Up)
            pause 0.5
            pause 0.5
            easein_quad 0.5 alpha 1.0 #Up
            repeat

    contains:
        "beach_massage_mc_front_masturbation_d_arm_over"
        beach_massage_mc_front_masturbation_d_arm_move_04

    contains:
        "red"
        truecenter
        zoom 5.0 alpha 0.0

############################################################################
###########################################################################
##########################################################################
#########################################################################


image beach_deepsea_mc_hand = "images/day05/aftermorning/beach_deepsea_mc_hand.webp"

image beach_deepsea_ball = "images/day05/aftermorning/beach_deepsea_ball.webp"
image beach_deepsea_ball_splash = "images/day05/aftermorning/beach_deepsea_ball_splash.webp"

image beach_deepsea_didac_afterorgasm 01 = "images/day05/aftermorning/beach_deepsea_didac_afterorgasm_01.webp"
image beach_deepsea_didac_afterorgasm 02 = "images/day05/aftermorning/beach_deepsea_didac_afterorgasm_02.webp"


## KID

image beach_deepsea_kid_swimming = "images/day05/aftermorning/beach_deepsea_kid_swimming.webp"

#image beach_deepsea_kid_TEST = "images/day05/aftermorning/beach_deepsea_kid_TEST.webp"
image beach_deepsea_kid_body = "images/day05/aftermorning/beach_deepsea_kid_body.webp"
image beach_deepsea_kid_hairFront = "images/day05/aftermorning/beach_deepsea_kid_hairFront.webp"
image beach_deepsea_kid_hand = "images/day05/aftermorning/beach_deepsea_kid_hand.webp"

    ## Kid Expressions

image beach_deepsea_kid_exp_glasses = "images/day05/aftermorning/beach_deepsea_kid_exp_glasses.webp"

image beach_deepsea_kid_exp_eyebrows angry = "images/day05/aftermorning/beach_deepsea_kid_exp_eyebrows_angry.webp"
image beach_deepsea_kid_exp_eyebrows surprise = "images/day05/aftermorning/beach_deepsea_kid_exp_eyebrows_surprise.webp"

image beach_deepsea_kid_exp_mouth happy_Talking = "images/day05/aftermorning/beach_deepsea_kid_exp_mouth_happy_Talking.webp"
image beach_deepsea_kid_exp_mouth sad_Silent = "images/day05/aftermorning/beach_deepsea_kid_exp_mouth_sad_Silent.webp"
image beach_deepsea_kid_exp_mouth sad_Talking = "images/day05/aftermorning/beach_deepsea_kid_exp_mouth_sad_Talking.webp"


image beach_deepsea_ball_comp 01:

    contains:
        "beach_outsexy_bg_sky"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.3 ypos 0.3

    contains:
        "beach_outsexy_bg_sea_ 12"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000

    # contains:
    #     "beach_deepsea_kid_body"
    #     truecenter
    #     zoom 0.5
    #     ypos 0.55

    contains:
        "beach_deepsea_ball"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5 # Don´t touch
        zoom 0.31
        xpos 1.2 ypos 0.4 #Arriving
        parallel:
            linear 0.2 xpos 0.8  ypos 0.6 # Beginning
            easein_quad 3.0 xpos 0.4 ypos 0.5 # Final pose.
            parallel:
                ease 2.3 xpos 0.405
                ease 1.4 xpos 0.395
                repeat
            parallel:
                ease 2.1 ypos 0.505
                ease 1.6 ypos 0.495
                repeat
            
        parallel:
            linear 0.2 rotate -360
            linear 0.0 rotate 0
            easein_quad 3.0 rotate -360
            linear 0.0 rotate 0
            parallel:
                ease 1.7 rotate 1
                ease 2.2 rotate -1
                repeat

    contains:
        "beach_deepsea_ball_splash"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.8 # Don´t touch
        zoom 0.31
        xpos 0.8  ypos 0.73 zoom 0.0 # Beginning
        pause 0.0
        parallel:
            easein_quad 3.0 xpos 0.4 ypos 0.73 # Final pose.
        parallel:
            easein_quad 0.75 alpha 1.0
            easein_quad 0.75 alpha 0.0
        parallel:
            easein_quad 2.0 zoom 1.0

    contains:
        "beach_outsexy_bg_sea_over 02"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000

image beach_deepsea_ball_comp 02:

    contains:
        "beach_outsexy_bg_sky"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.3 ypos 0.3

    contains:
        "beach_outsexy_bg_sea_ 12"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000

    #contains:
        #"beach_deepsea_kid_body"
        #truecenter
        #zoom 0.5
        #ypos 0.55

    contains:
        "beach_deepsea_ball"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5 # Don´t touch
        zoom 0.31
        xpos 0.4 ypos 0.5 # Final pose.
        parallel:
            ease 2.3 xpos 0.405
            ease 1.4 xpos 0.395
            repeat
        parallel:
            ease 2.1 ypos 0.505
            ease 1.6 ypos 0.495
            repeat
        parallel:
            ease 1.7 rotate 1
            ease 2.2 rotate -1
            repeat
           
    contains:
        "beach_outsexy_bg_sea_over 02"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000


image beach_deepsea_ball_comp 03:

    contains:
        "beach_outsexy_bg_sky"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.3 ypos 0.3

    contains:
        "beach_outsexy_bg_sea_ 12"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000

    #contains:
        #"beach_deepsea_kid_body"
        #truecenter
        #zoom 0.5
        #ypos 0.55

    contains:
        "beach_deepsea_ball"
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5 # Don´t touch
        zoom 0.31
        xpos 0.4 ypos 0.5 # Final pose.
        parallel:
            ease 2.3 xpos 0.405
            ease 1.4 xpos 0.395
            repeat
        parallel:
            ease 2.1 ypos 0.505
            ease 1.6 ypos 0.495
            repeat
        parallel:
            ease 1.7 rotate 1
            ease 2.2 rotate -1
            repeat
           
    contains:
        "beach_outsexy_bg_sea_over 02"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000


#####

#####

image beach_deepsea_kidswimming_comp 01:

    contains:
        "beach_outsexy_bg_sky"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.3 ypos 0.3

    contains:
        "beach_outsexy_bg_sea_ 12"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000

    contains:
        "beach_deepsea_kid_swimming"
        truecenter
        zoom 0.05 alpha 1.0
        ypos 0.311

    contains:
        "beach_outsexy_bg_sea_over 11"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000

image beach_deepsea_kidswimming_comp 02:

    contains:
        "beach_outsexy_bg_sky"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.3 ypos 0.3

    contains:
        "beach_outsexy_bg_sea_ 12"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000

    contains:
        "beach_deepsea_kid_swimming"
        subpixel True
        truecenter
        zoom 0.1
        ypos 0.348
        block:
            easein_quad 1.0 rotate 3
            easeout_quad 2.0 rotate -3
            repeat

    contains:
        "beach_outsexy_bg_sea_over 08"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000

image beach_deepsea_kidswimming_comp 03:

    contains:
        "beach_outsexy_bg_sky"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.3 ypos 0.3

    contains:
        "beach_outsexy_bg_sea_ 12"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000

    contains:
        "beach_deepsea_kid_swimming"
        truecenter
        zoom 0.4
        ypos 0.465

    contains:
        "beach_outsexy_bg_sea_over 05"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000

image beach_deepsea_kidswimming_comp 04:

    contains:
        "beach_outsexy_bg_sky"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.3 ypos 0.3

    contains:
        "beach_outsexy_bg_sea_ 12"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000

    contains:
        "beach_deepsea_kid_swimming"
        truecenter
        zoom 1.0
        ypos 0.72

    contains:
        "beach_outsexy_bg_sea_over 02"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000


transform beach_deepsea_kid_exp_pos:
    subpixel True
    truecenter
    zoom 0.5
    xpos 0.5875 ypos 0.343


image beach_deepsea_kidwithball_comp 01:

    contains:
        "beach_outsexy_bg_sky"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.3 ypos 0.3

    contains:
        "beach_outsexy_bg_sea_ 12"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000

    contains:
        "beach_deepsea_kid_body"
        truecenter
        zoom 0.5
        ypos 0.55

    contains:
        "beach_deepsea_kid_exp_eyebrows surprise"
        beach_deepsea_kid_exp_pos

    contains:
        "beach_deepsea_kid_exp_mouth sad_Silent"
        beach_deepsea_kid_exp_pos

    contains:
        "beach_deepsea_kid_exp_glasses"
        beach_deepsea_kid_exp_pos

    contains:
        "beach_deepsea_kid_hairFront"
        truecenter
        zoom 0.5
        ypos 0.55

    contains:
        "beach_outsexy_bg_sea_over 02"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000

image beach_deepsea_kidwithball_comp 02: # he has the ball being far away.

    contains:
        "beach_outsexy_bg_sky"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.3 ypos 0.3

    contains:
        "beach_outsexy_bg_sea_ 12"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000

    contains:
        "beach_deepsea_kid_hand"
        beach_deepsea_kidwithball_body_pos
        beach_deepsea_kidwithball_pos02

    contains:
        "beach_deepsea_kid_body"
        beach_deepsea_kidwithball_body_pos
        beach_deepsea_kidwithball_pos02

    contains:
        "beach_deepsea_kid_exp_eyebrows surprise"
        truecenter
        beach_deepsea_kidwithball_pos02

    contains:
        "beach_deepsea_kid_exp_mouth happy_Talking"
        truecenter
        beach_deepsea_kidwithball_pos02

    contains:
        "beach_deepsea_kid_exp_glasses"
        truecenter
        beach_deepsea_kidwithball_pos02

    contains:
        "beach_deepsea_kid_hairFront"
        beach_deepsea_kidwithball_body_pos
        beach_deepsea_kidwithball_pos02

    contains:
        "beach_outsexy_bg_sea_over 07"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000

transform beach_deepsea_kidwithball_body_pos:
    transform_anchor True
    xalign 0.632 yalign 0.26

transform beach_deepsea_kidwithball_pos02:
    subpixel True
    zoom 0.092 xpos 0.5 ypos 0.3


####

image beach_buoy_alone_comp 01:

    contains:
        "beach_outsexy_bg_sky"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.3 ypos 0.3

    contains:
        "beach_outsexy_bg_sea_ 12"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000

    contains:
        "beach_buoy yellow"
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 1.0 xpos 0.25 ypos 0.58

    contains:
        "beach_outsexy_bg_sea_over_b 03"
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.5 ypos 0.3 # ypos 0.3 #It´s the original 2667x2000