#images05




#############################################################################################################################
############################################################################################################################

        ## NEUS BODY

image neus_body naked = SaturateTint("images/general/characters/neus/neus_body_naked.webp")
image neus_body sd_default = SaturateTint("images/general/characters/neus/neus_body_sd_default.webp")
image neus_body ld_default = SaturateTint("images/general/characters/neus/neus_body_ld_default.webp")

image neus_body_full ld_boobs = SaturateTint("images/general/characters/neus/neus_body_full_ld_boobs.webp")
image neus_body_full ld_covered = SaturateTint("images/general/characters/neus/neus_body_full_ld_covered.webp")

image neus_body_full day02 = SaturateTint("images/general/characters/neus/neus_body_full_day02.webp")
image neus_body_full day03 = SaturateTint("images/general/characters/neus/neus_body_full_day03.webp")
image neus_body_full afterrape = SaturateTint("images/general/characters/neus/neus_body_full_afterrape.webp")
image neus_body_full_afterrape_hair = SaturateTint("images/general/characters/neus/neus_body_full_afterrape_hair.webp")



image neus_body_prove = SaturateTint("images/general/characters/neus/neus_body_prove.webp")

#image neus_body_prove_little = im.Scale("images/general/characters/neus/neus_body_prove.webp"), 692, 1458) # with Zoom 0.5 Looks PERFECT.

#############################################################################################################################
############################################################################################################################

        ## NEUS OTHERS

image neus_head = SaturateTint("images/general/characters/neus/neus_head.webp")


image neus_arms ld_coffeedrinking = SaturateTint("images/general/characters/neus/neus_arms_ld_coffeedrinking.webp")
image neus_arms ld_coffeeholding = SaturateTint("images/general/characters/neus/neus_arms_ld_coffeeholding.webp")
image neus_arms ld_condoms = SaturateTint("images/general/characters/neus/neus_arms_ld_condoms.webp")
image neus_arms ld_keys = SaturateTint("images/general/characters/neus/neus_arms_ld_keys.webp")
image neus_arms ld_keystry = SaturateTint("images/general/characters/neus/neus_arms_ld_keystry.webp")
image neus_arms ld_keysinsert = SaturateTint("images/general/characters/neus/neus_arms_ld_keysinsert.webp")
image neus_arms ld_purse_opened = SaturateTint("images/general/characters/neus/neus_arms_ld_purse_opened.webp")
image neus_arms ld_purse_closed = SaturateTint("images/general/characters/neus/neus_arms_ld_purse_closed.webp")
image neus_arms ld_rest = SaturateTint("images/general/characters/neus/neus_arms_ld_rest.webp")
image neus_arms empty = SaturateTint("images/general/empty.webp")


image neus_arm_l sd = SaturateTint("images/general/characters/neus/neus_arm_l_sd.webp")
image neus_arm_r sd = SaturateTint("images/general/characters/neus/neus_arm_r_sd.webp")

image neus_arm_l naked = SaturateTint("images/general/characters/neus/neus_arm_l_naked.webp")
image neus_arm_r naked = SaturateTint("images/general/characters/neus/neus_arm_r_naked.webp")

#############################################################################################################################
############################################################################################################################

        ## NEUS EXPRESSIONS

# hair

image neus_exp_hairfront = SaturateTint("images/general/characters/neus/neus_exp_hairfront.webp")

#image neus_exp_hairfront_little = im.Scale("images/general/characters/neus/neus_exp_hairfront.webp"), 390, 390) # with Zoom 0.5 Looks PERFECT.

#image neus_exp_hairfront_little_superdark = im.MatrixColor ("images/general/characters/neus/neus_exp_hairfront.webp"),
                                                                 #im.matrix.saturation(0.5) * im.matrix.tint(.22, .25, .45)) im.Scale(390,390)




image neus_exp_hairfront_prove = SaturateTint("images/general/characters/neus/neus_exp_hairfront_prove.webp")
image neus_exp_hairfront_PROVERealSize = SaturateTint("images/general/characters/neus/neus_exp_hairfront_PROVERealSize.webp")


#image neus_exp_hairfront_little = im.Scale("images/general/characters/neus/neus_exp_hairfront.webp", 390, 390) # with Zoom 0.5 Looks 


#image neus_exp_hairfront_little_superdark = im.MatrixColor(neus_exp_hairfront_little, im.matrix.saturation(0.5) * im.matrix.tint(.22, .25, .45)) # doesn´t work


#############################################################################################################################

########## THIS WORKS.

#image neus_exp_hairfront_little_superdark = im.Scale(
  #im.MatrixColor (
    #"images/general/characters/neus/neus_exp_hairfront.webp",
    #im.matrix.saturation(0.5) * im.matrix.tint(.22, .25, .45)
  #), 390, 390)

#############################################################################################################################
#init -10 python:

    #ef small_night_time_tint(img):
        #return Transform(
            #im.MatrixColor(
                #img,
                #m.matrix.saturation(0.5) * im.matrix.tint(.22, .25, .45)),
            #maxsize=(390,390))

    #config.displayable_prefix["small_night"] = small_night_time_tint


#label start:

    #show expression "small_night:images/bgs/bg_1.png" # prefix to set function : colon : image with path

#############################################################################################################################

# glasses

image neus_exp_glasses = SaturateTint("images/general/characters/neus/neus_exp_glasses.webp")

# blush

image neus_exp_blush empty = "images/general/empty.webp"
image neus_exp_blush 00 = "images/general/empty.webp"
image neus_exp_blush 01 = SaturateTint("images/general/characters/neus/neus_exp_blush_01.webp")
image neus_exp_blush 02 = SaturateTint("images/general/characters/neus/neus_exp_blush_02.webp")
image neus_exp_blush 03 = SaturateTint("images/general/characters/neus/neus_exp_blush_03.webp")
image neus_exp_blush 04 = SaturateTint("images/general/characters/neus/neus_exp_blush_04.webp")
image neus_exp_blush 05 = SaturateTint("images/general/characters/neus/neus_exp_blush_05.webp")
image neus_exp_blush 06 = SaturateTint("images/general/characters/neus/neus_exp_blush_06.webp")
image neus_exp_blush 07 = SaturateTint("images/general/characters/neus/neus_exp_blush_07.webp")
image neus_exp_blush 08 = SaturateTint("images/general/characters/neus/neus_exp_blush_08.webp")


# eyebrows

image neus_exp_eyebrows angryx01 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_angryx01.webp")
image neus_exp_eyebrows angryx02 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_angryx02.webp")
image neus_exp_eyebrows angryx03 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_angryx03.webp")
image neus_exp_eyebrows angryx04 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_angryx04.webp")
image neus_exp_eyebrows angryx05 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_angryx05.webp")

image neus_exp_eyebrows suspiciousx01 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_suspiciousx01.webp")
image neus_exp_eyebrows suspiciousx02 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_suspiciousx02.webp")
image neus_exp_eyebrows suspiciousx03 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_suspiciousx03.webp")

image neus_exp_eyebrows normal = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_normal.webp")

image neus_exp_eyebrows sadx01 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_sadx01.webp")
image neus_exp_eyebrows sadx02 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_sadx02.webp")
image neus_exp_eyebrows sadx03 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_sadx03.webp")
image neus_exp_eyebrows sadx04 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_sadx04.webp")
image neus_exp_eyebrows sadx05 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_sadx05.webp")
image neus_exp_eyebrows sadx06 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_sadx06.webp")
image neus_exp_eyebrows sadx07 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_sadx07.webp")

image neus_exp_eyebrows serious = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_serious.webp")

image neus_exp_eyebrows surprisex01 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_surprisex01.webp")
image neus_exp_eyebrows surprisex02 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_surprisex02.webp")
image neus_exp_eyebrows surprisex03 = SaturateTint("images/general/characters/neus/neus_exp_eyebrows_surprisex03.webp")

# eyes

image neus_exp_eyes 00 = SaturateTint("images/general/characters/neus/neus_exp_eyes_00[neyesp].webp")
image neus_exp_eyes 01 = SaturateTint("images/general/characters/neus/neus_exp_eyes_01[neyesp].webp")
image neus_exp_eyes 02 = SaturateTint("images/general/characters/neus/neus_exp_eyes_02[neyesp].webp")
image neus_exp_eyes 03 = SaturateTint("images/general/characters/neus/neus_exp_eyes_03[neyesp].webp")
image neus_exp_eyes 04 = SaturateTint("images/general/characters/neus/neus_exp_eyes_04[neyesp].webp")
image neus_exp_eyes 05 = SaturateTint("images/general/characters/neus/neus_exp_eyes_05[neyesp].webp")
image neus_exp_eyes 06 = SaturateTint("images/general/characters/neus/neus_exp_eyes_06[neyesp].webp")
image neus_exp_eyes 07 = SaturateTint("images/general/characters/neus/neus_exp_eyes_07[neyesp].webp")
image neus_exp_eyes 08 = SaturateTint("images/general/characters/neus/neus_exp_eyes_08[neyesp].webp")

#label prove:

    #neus_exp_eyes_00_fun()

    #return


# pupils

image neus_exp_iris empty = SaturateTint("images/general/empty.webp")

image neus_exp_iris down00 = SaturateTint("images/general/characters/neus/neus_exp_iris_down00.webp")
image neus_exp_iris down01 = SaturateTint("images/general/characters/neus/neus_exp_iris_down01.webp")
image neus_exp_iris down02 = SaturateTint("images/general/characters/neus/neus_exp_iris_down02.webp")
image neus_exp_iris down03 = SaturateTint("images/general/characters/neus/neus_exp_iris_down03.webp")
image neus_exp_iris down04 = SaturateTint("images/general/characters/neus/neus_exp_iris_down04.webp")
image neus_exp_iris down05 = SaturateTint("images/general/characters/neus/neus_exp_iris_down05.webp")

image neus_exp_iris front00 = SaturateTint("images/general/characters/neus/neus_exp_iris_front00.webp")
image neus_exp_iris front01 = SaturateTint("images/general/characters/neus/neus_exp_iris_front01.webp")
image neus_exp_iris front02 = SaturateTint("images/general/characters/neus/neus_exp_iris_front02.webp")
image neus_exp_iris front03 = SaturateTint("images/general/characters/neus/neus_exp_iris_front03.webp")
image neus_exp_iris front04 = SaturateTint("images/general/characters/neus/neus_exp_iris_front04.webp")
image neus_exp_iris front05 = SaturateTint("images/general/characters/neus/neus_exp_iris_front05.webp")
image neus_exp_iris front06 = SaturateTint("images/general/empty.webp")
image neus_exp_iris front07 = SaturateTint("images/general/empty.webp")
image neus_exp_iris front08 = SaturateTint("images/general/empty.webp")

image neus_exp_iris left00 = SaturateTint("images/general/characters/neus/neus_exp_iris_left00.webp")
image neus_exp_iris left01 = SaturateTint("images/general/characters/neus/neus_exp_iris_left01.webp")
image neus_exp_iris left02 = SaturateTint("images/general/characters/neus/neus_exp_iris_left02.webp")
image neus_exp_iris left03 = SaturateTint("images/general/characters/neus/neus_exp_iris_left03.webp")
image neus_exp_iris left04 = SaturateTint("images/general/characters/neus/neus_exp_iris_left04.webp")
image neus_exp_iris left05 = SaturateTint("images/general/characters/neus/neus_exp_iris_left05.webp")

image neus_exp_iris right00 = SaturateTint("images/general/characters/neus/neus_exp_iris_right00.webp")
image neus_exp_iris right01 = SaturateTint("images/general/characters/neus/neus_exp_iris_right01.webp")
image neus_exp_iris right02 = SaturateTint("images/general/characters/neus/neus_exp_iris_right02.webp")
image neus_exp_iris right03 = SaturateTint("images/general/characters/neus/neus_exp_iris_right03.webp")
image neus_exp_iris right04 = SaturateTint("images/general/characters/neus/neus_exp_iris_right04.webp")
image neus_exp_iris right05 = SaturateTint("images/general/characters/neus/neus_exp_iris_right05.webp")

## l_iris Violet Iris

image neus_exp_l_iris down00 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_down00.webp")
image neus_exp_l_iris down01 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_down01.webp")
image neus_exp_l_iris down02 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_down02.webp")
image neus_exp_l_iris down03 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_down03.webp")
image neus_exp_l_iris down04 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_down04.webp")
image neus_exp_l_iris down05 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_down05.webp")

image neus_exp_l_iris front00 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_front00.webp")
image neus_exp_l_iris front01 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_front01.webp")
image neus_exp_l_iris front02 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_front02.webp")
image neus_exp_l_iris front03 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_front03.webp")
image neus_exp_l_iris front04 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_front04.webp")
image neus_exp_l_iris front05 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_front05.webp")
image neus_exp_l_iris front06 = SaturateTint("images/general/empty.webp")
image neus_exp_l_iris front07 = SaturateTint("images/general/empty.webp")
image neus_exp_l_iris front08 = SaturateTint("images/general/empty.webp")
image neus_exp_l_iris empty = "images/general/empty.webp"

image neus_exp_l_iris left00 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_left00.webp")
image neus_exp_l_iris left01 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_left01.webp")
image neus_exp_l_iris left02 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_left02.webp")
image neus_exp_l_iris left03 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_left03.webp")
image neus_exp_l_iris left04 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_left04.webp")
image neus_exp_l_iris left05 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_left05.webp")

image neus_exp_l_iris right00 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_right00.webp")
image neus_exp_l_iris right01 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_right01.webp")
image neus_exp_l_iris right02 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_right02.webp")
image neus_exp_l_iris right03 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_right03.webp")
image neus_exp_l_iris right04 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_right04.webp")
image neus_exp_l_iris right05 = SaturateTint("images/general/characters/neus/neus_exp_l_iris_right05.webp")

## iLight IRIS LIGHT

image neus_exp_iLight empty = "images/general/empty.webp"

image neus_exp_iLight down00 = "images/general/characters/neus/neus_exp_iLight_down00.webp"
image neus_exp_iLight down01 = "images/general/characters/neus/neus_exp_iLight_down01.webp"
image neus_exp_iLight down02 = "images/general/characters/neus/neus_exp_iLight_down02.webp"
image neus_exp_iLight down03 = "images/general/characters/neus/neus_exp_iLight_down03.webp"
image neus_exp_iLight down04 = "images/general/characters/neus/neus_exp_iLight_down04.webp"
image neus_exp_iLight down05 = "images/general/characters/neus/neus_exp_iLight_down05.webp"

image neus_exp_iLight front00 = "images/general/characters/neus/neus_exp_iLight_front00.webp"
image neus_exp_iLight front01 = "images/general/characters/neus/neus_exp_iLight_front01.webp"
image neus_exp_iLight front02 = "images/general/characters/neus/neus_exp_iLight_front02.webp"
image neus_exp_iLight front03 = "images/general/characters/neus/neus_exp_iLight_front03.webp"
image neus_exp_iLight front04 = "images/general/characters/neus/neus_exp_iLight_front04.webp"
image neus_exp_iLight front05 = "images/general/characters/neus/neus_exp_iLight_front05.webp"
image neus_exp_iLight front06 = "images/general/empty.webp"
image neus_exp_iLight front07 = "images/general/empty.webp"
image neus_exp_iLight front08 = "images/general/empty.webp"

image neus_exp_iLight left00 = "images/general/characters/neus/neus_exp_iLight_left00.webp"
image neus_exp_iLight left01 = "images/general/characters/neus/neus_exp_iLight_left01.webp"
image neus_exp_iLight left02 = "images/general/characters/neus/neus_exp_iLight_left02.webp"
image neus_exp_iLight left03 = "images/general/characters/neus/neus_exp_iLight_left03.webp"
image neus_exp_iLight left04 = "images/general/characters/neus/neus_exp_iLight_left04.webp"
image neus_exp_iLight left05 = "images/general/characters/neus/neus_exp_iLight_left05.webp"

image neus_exp_iLight right00 = "images/general/characters/neus/neus_exp_iLight_right00.webp"
image neus_exp_iLight right01 = "images/general/characters/neus/neus_exp_iLight_right01.webp"
image neus_exp_iLight right02 = "images/general/characters/neus/neus_exp_iLight_right02.webp"
image neus_exp_iLight right03 = "images/general/characters/neus/neus_exp_iLight_right03.webp"
image neus_exp_iLight right04 = "images/general/characters/neus/neus_exp_iLight_right04.webp"
image neus_exp_iLight right05 = "images/general/characters/neus/neus_exp_iLight_right05.webp"


image neus_exp_iris down00_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_down00.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris down01_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_down01.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris down02_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_down02.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris down03_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_down03.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris down04_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_down04.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris down05_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_down05.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))

image neus_exp_iris front00_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_front00.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris front01_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_front01.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris front02_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_front02.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris front03_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_front03.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris front04_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_front04.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris front05_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_front05.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))

image neus_exp_iris left00_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_left00.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris left01_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_left01.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris left02_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_left02.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris left03_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_left03.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris left04_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_left04.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris left05_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_left05.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))

image neus_exp_iris right00_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_right00.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris right01_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_right01.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris right02_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_right02.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris right03_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_right03.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris right04_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_right04.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))
image neus_exp_iris right05_bright = im.MatrixColor("images/general/characters/neus/neus_exp_iris_right05.webp", im.matrix.saturation(0.0) * im.matrix.tint(1.2, 1.0, 2.0))

# tears

label neus_exp_tears_tears:

    if nteye in [0, "front00", "front00b", "down00", "down00b", "right00", "left00"]:
        show neus_exp_eyes 00
        if ntlong == 1:
            show neus_exp_tears 00_01
        elif ntlong == 2:
            show neus_exp_tears 00_02
        elif ntlong == 3:
            show neus_exp_tears 00_03
        elif ntlong == 4:
            show neus_exp_tears 00_04
        elif ntlong == 5:
            show neus_exp_tears 00_05
    elif nteye in [1, "front01", "front01b", "down01", "down01b", "right01", "left01"]:
        show neus_exp_eyes 01
        if ntlong == 1:
            show neus_exp_tears 01_01
        elif ntlong == 2:
            show neus_exp_tears 01_02
        elif ntlong == 3:
            show neus_exp_tears 01_03
        elif ntlong == 4:
            show neus_exp_tears 01_04
        elif ntlong == 5:
            show neus_exp_tears 01_05
    elif nteye in [2, "front02", "front02b", "down02", "down02b", "right02", "left02"]:
        show neus_exp_eyes 02
        if ntlong == 1:
            show neus_exp_tears 02_01
        elif ntlong == 2:
            show neus_exp_tears 02_02
        elif ntlong == 3:
            show neus_exp_tears 02_03
        elif ntlong == 4:
            show neus_exp_tears 02_04
        elif ntlong == 5:
            show neus_exp_tears 02_05

    elif nteye in [3, "front03", "front03b", "down03", "down03b", "right03", "left03"]:
        show neus_exp_eyes 03
        if ntlong == 1:
            show neus_exp_tears 03_01
        elif ntlong == 2:
            show neus_exp_tears 03_02
        elif ntlong == 3:
            show neus_exp_tears 03_03
        elif ntlong == 4:
            show neus_exp_tears 03_04
        elif ntlong == 5:
            show neus_exp_tears 03_05

    elif nteye in [4, "front04", "front04b", "down04", "down04b", "right04", "left04"]:
        show neus_exp_eyes 04
        if ntlong == 1:
            show neus_exp_tears 04_01
        elif ntlong == 2:
            show neus_exp_tears 04_02
        elif ntlong == 3:
            show neus_exp_tears 04_03
        elif ntlong == 4:
            show neus_exp_tears 04_04
        elif ntlong == 5:
            show neus_exp_tears 04_05
             
    elif nteye in [5, "front05", "front05b", "down05", "down05b", "right05", "left05"]:
        show neus_exp_eyes 05
        if ntlong == 1:
            show neus_exp_tears 05_01
        elif ntlong == 2:
            show neus_exp_tears 05_02
        elif ntlong == 3:
            show neus_exp_tears 05_03
        elif ntlong == 4:
            show neus_exp_tears 05_04
        elif ntlong == 5:
            show neus_exp_tears 05_05

    elif nteye in [6, "front06"]:
        show neus_exp_eyes 06
        if ntlong == 1:
            show neus_exp_tears 06_01
        elif ntlong == 2:
            show neus_exp_tears 06_02
        elif ntlong == 3:
            show neus_exp_tears 06_03
        elif ntlong == 4:
            show neus_exp_tears 06_04
        elif ntlong == 5:
            show neus_exp_tears 06_05

    elif nteye in [7, "front07"]:
        show neus_exp_eyes 07
        if ntlong == 1:
            show neus_exp_tears 07_01
        elif ntlong == 2:
            show neus_exp_tears 07_02
        elif ntlong == 3:
            show neus_exp_tears 07_03
        elif ntlong == 4:
            show neus_exp_tears 07_04
        elif ntlong == 5:
            show neus_exp_tears 07_05

    elif nteye in [8, "front08"]:
        show neus_exp_eyes 08
        if ntlong == 1:
            show neus_exp_tears 08_01
        elif ntlong == 2:
            show neus_exp_tears 08_02
        elif ntlong == 3:
            show neus_exp_tears 08_03
        elif ntlong == 4:
            show neus_exp_tears 08_04
        elif ntlong == 5:
            show neus_exp_tears 08_05
    else:
        show neus_exp_tears empty

    return

default dteye = 0
default dtlong = 0

label didac_exp_tears_tears:

    if dteye == 0:
        show didacf_eyes 00
        if dtlong == 1:
            show didacf_tears 00_01
        elif dtlong == 2:
            show didacf_tears 00_02
        elif dtlong == 3:
            show didacf_tears 00_03
        elif dtlong == 4:
            show didacf_tears 00_04
        elif dtlong == 5:
            show didacf_tears 00_05

    elif dteye == 1:
        show didacf_eyes 01
        if dtlong == 1:
            show didacf_tears 01_01
        elif dtlong == 2:
            show didacf_tears 01_02
        elif dtlong == 3:
            show didacf_tears 01_03
        elif dtlong == 4:
            show didacf_tears 01_04
        elif dtlong == 5:
            show didacf_tears 01_05

    elif dteye == 2:
        show didacf_eyes 02
        if dtlong == 1:
            show didacf_tears 02_01
        elif dtlong == 2:
            show didacf_tears 02_02
        elif dtlong == 3:
            show didacf_tears 02_03
        elif dtlong == 4:
            show didacf_tears 02_04
        elif dtlong == 5:
            show didacf_tears 02_05

    elif dteye == 3:
        show didacf_eyes 03
        if dtlong == 1:
            show didacf_tears 03_01
        elif dtlong == 2:
            show didacf_tears 03_02
        elif dtlong == 3:
            show didacf_tears 03_03
        elif dtlong == 4:
            show didacf_tears 03_04
        elif dtlong == 5:
            show didacf_tears 03_05

    elif dteye == 4:
        show didacf_eyes 04
        if dtlong == 1:
            show didacf_tears 04_01
        elif dtlong == 2:
            show didacf_tears 04_02
        elif dtlong == 3:
            show didacf_tears 04_03
        elif dtlong == 4:
            show didacf_tears 04_04
        elif dtlong == 5:
            show didacf_tears 04_05

    elif dteye == 5:
        show didacf_eyes 05
        if dtlong == 1:
            show didacf_tears 05_01
        elif dtlong == 2:
            show didacf_tears 05_02
        elif dtlong == 3:
            show didacf_tears 05_03
        elif dtlong == 4:
            show didacf_tears 05_04
        elif dtlong == 5:
            show didacf_tears 05_05

    elif dteye == 6:
        show didacf_eyes 06
        if dtlong == 1:
            show didacf_tears 06_01
        elif dtlong == 2:
            show didacf_tears 06_02
        elif dtlong == 3:
            show didacf_tears 06_03
        elif dtlong == 4:
            show didacf_tears 06_04
        elif dtlong == 5:
            show didacf_tears 06_05

    elif dteye == 7:
        show didacf_eyes 07
        if dtlong == 1:
            show didacf_tears 07_01
        elif dtlong == 2:
            show didacf_tears 07_02
        elif dtlong == 3:
            show didacf_tears 07_03
        elif dtlong == 4:
            show didacf_tears 07_04
        elif dtlong == 5:
            show didacf_tears 07_05

    elif dteye == 8:
        show didacf_eyes 08
        if dtlong == 1:
            show didacf_tears 08_01
        elif dtlong == 2:
            show didacf_tears 08_02
        elif dtlong == 3:
            show didacf_tears 08_03
        elif dtlong == 4:
            show didacf_tears 08_04
        elif dtlong == 5:
            show didacf_tears 08_05

    return



image neus_exp_tears auto = SaturateTint("images/general/characters/neus/neus_exp_tears_[nteye]_[ntlong].webp")

image neus_exp_tears empty = SaturateTint("images/general/empty.webp")

image neus_exp_tears 00_01 = SaturateTint("images/general/characters/neus/neus_exp_tears_00_01.webp")
image neus_exp_tears 00_02 = SaturateTint("images/general/characters/neus/neus_exp_tears_00_02.webp")
image neus_exp_tears 00_03 = SaturateTint("images/general/characters/neus/neus_exp_tears_00_03.webp")
image neus_exp_tears 00_04 = SaturateTint("images/general/characters/neus/neus_exp_tears_00_04.webp")
image neus_exp_tears 00_05 = SaturateTint("images/general/characters/neus/neus_exp_tears_00_05.webp")

image neus_exp_tears 01_01 = SaturateTint("images/general/characters/neus/neus_exp_tears_01_01.webp")
image neus_exp_tears 01_02 = SaturateTint("images/general/characters/neus/neus_exp_tears_01_02.webp")
image neus_exp_tears 01_03 = SaturateTint("images/general/characters/neus/neus_exp_tears_01_03.webp")
image neus_exp_tears 01_04 = SaturateTint("images/general/characters/neus/neus_exp_tears_01_04.webp")
image neus_exp_tears 01_05 = SaturateTint("images/general/characters/neus/neus_exp_tears_01_05.webp")

image neus_exp_tears 02_01 = SaturateTint("images/general/characters/neus/neus_exp_tears_02_01.webp")
image neus_exp_tears 02_02 = SaturateTint("images/general/characters/neus/neus_exp_tears_02_02.webp")
image neus_exp_tears 02_03 = SaturateTint("images/general/characters/neus/neus_exp_tears_02_03.webp")
image neus_exp_tears 02_04 = SaturateTint("images/general/characters/neus/neus_exp_tears_02_04.webp")
image neus_exp_tears 02_05 = SaturateTint("images/general/characters/neus/neus_exp_tears_02_05.webp")

image neus_exp_tears 03_01 = SaturateTint("images/general/characters/neus/neus_exp_tears_03_01.webp")
image neus_exp_tears 03_02 = SaturateTint("images/general/characters/neus/neus_exp_tears_03_02.webp")
image neus_exp_tears 03_03 = SaturateTint("images/general/characters/neus/neus_exp_tears_03_03.webp")
image neus_exp_tears 03_04 = SaturateTint("images/general/characters/neus/neus_exp_tears_03_04.webp")
image neus_exp_tears 03_05 = SaturateTint("images/general/characters/neus/neus_exp_tears_03_05.webp")

image neus_exp_tears 04_01 = SaturateTint("images/general/characters/neus/neus_exp_tears_04_01.webp")
image neus_exp_tears 04_02 = SaturateTint("images/general/characters/neus/neus_exp_tears_04_02.webp")
image neus_exp_tears 04_03 = SaturateTint("images/general/characters/neus/neus_exp_tears_04_03.webp")
image neus_exp_tears 04_04 = SaturateTint("images/general/characters/neus/neus_exp_tears_04_04.webp")
image neus_exp_tears 04_05 = SaturateTint("images/general/characters/neus/neus_exp_tears_04_05.webp")

image neus_exp_tears 05_01 = SaturateTint("images/general/characters/neus/neus_exp_tears_05_01.webp")
image neus_exp_tears 05_02 = SaturateTint("images/general/characters/neus/neus_exp_tears_05_02.webp")
image neus_exp_tears 05_03 = SaturateTint("images/general/characters/neus/neus_exp_tears_05_03.webp")
image neus_exp_tears 05_04 = SaturateTint("images/general/characters/neus/neus_exp_tears_05_04.webp")
image neus_exp_tears 05_05 = SaturateTint("images/general/characters/neus/neus_exp_tears_05_05.webp")


image neus_exp_tears 06_01 = SaturateTint("images/general/characters/neus/neus_exp_tears_06_01.webp")
image neus_exp_tears 06_02 = SaturateTint("images/general/characters/neus/neus_exp_tears_06_02.webp")
image neus_exp_tears 06_03 = SaturateTint("images/general/characters/neus/neus_exp_tears_06_03.webp")
image neus_exp_tears 06_04 = SaturateTint("images/general/characters/neus/neus_exp_tears_06_04.webp")
image neus_exp_tears 06_05 = SaturateTint("images/general/characters/neus/neus_exp_tears_06_05.webp")

image neus_exp_tears 07_01 = SaturateTint("images/general/characters/neus/neus_exp_tears_07_01.webp")
image neus_exp_tears 07_02 = SaturateTint("images/general/characters/neus/neus_exp_tears_07_02.webp")
image neus_exp_tears 07_03 = SaturateTint("images/general/characters/neus/neus_exp_tears_07_03.webp")
image neus_exp_tears 07_04 = SaturateTint("images/general/characters/neus/neus_exp_tears_07_04.webp")
image neus_exp_tears 07_05 = SaturateTint("images/general/characters/neus/neus_exp_tears_07_05.webp")

image neus_exp_tears 08_01 = SaturateTint("images/general/characters/neus/neus_exp_tears_08_01.webp")
image neus_exp_tears 08_02 = SaturateTint("images/general/characters/neus/neus_exp_tears_08_02.webp")
image neus_exp_tears 08_03 = SaturateTint("images/general/characters/neus/neus_exp_tears_08_03.webp")
image neus_exp_tears 08_04 = SaturateTint("images/general/characters/neus/neus_exp_tears_08_04.webp")
image neus_exp_tears 08_05 = SaturateTint("images/general/characters/neus/neus_exp_tears_08_05.webp")

# mouth

image neus_exp_mouth happy_Silentx01 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Silentx01.webp")
image neus_exp_mouth happy_Silentx02 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Silentx02.webp")
image neus_exp_mouth happy_Silentx03 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Silentx03.webp")
image neus_exp_mouth happy_Silentx04 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Silentx04.webp")
image neus_exp_mouth happy_Silentx05 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Silentx05.webp")
image neus_exp_mouth happy_Silentx06 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Silentx06.webp")
image neus_exp_mouth happy_Silentx07 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Silentx07.webp")
image neus_exp_mouth happy_Silentx08 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Silentx08.webp")
image neus_exp_mouth happy_Silentx09 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Silentx09.webp")
image neus_exp_mouth happy_Silentx10 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Silentx10.webp")

image neus_exp_mouth happy_Talkingx01 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Talkingx01.webp")
image neus_exp_mouth happy_Talkingx02 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Talkingx02.webp")
image neus_exp_mouth happy_Talkingx03 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Talkingx03.webp")
image neus_exp_mouth happy_Talkingx04 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Talkingx04.webp")
image neus_exp_mouth happy_Talkingx05 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Talkingx05.webp")
image neus_exp_mouth happy_Talkingx06 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Talkingx06.webp")
image neus_exp_mouth happy_Talkingx07 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Talkingx07.webp")
image neus_exp_mouth happy_Talkingx08 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Talkingx08.webp")
image neus_exp_mouth happy_Talkingx09 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Talkingx09.webp")
image neus_exp_mouth happy_Talkingx10 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happy_Talkingx10.webp")

image neus_exp_mouth happybiting_Silentx01 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happybiting_Silentx01.webp")
image neus_exp_mouth happybiting_Silentx02 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happybiting_Silentx02.webp")
image neus_exp_mouth happybiting_Silentx03 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happybiting_Silentx03.webp")
image neus_exp_mouth happybiting_Silentx04 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happybiting_Silentx04.webp")
image neus_exp_mouth happybiting_Silentx05 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happybiting_Silentx05.webp")
image neus_exp_mouth happybiting_Silentx06 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happybiting_Silentx06.webp")
image neus_exp_mouth happybiting_Silentx07 = SaturateTint("images/general/characters/neus/neus_exp_mouth_happybiting_Silentx07.webp")

image neus_exp_mouth sad_Silentx01 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Silentx01.webp")
image neus_exp_mouth sad_Silentx02 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Silentx02.webp")
image neus_exp_mouth sad_Silentx03 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Silentx03.webp")
image neus_exp_mouth sad_Silentx04 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Silentx04.webp")
image neus_exp_mouth sad_Silentx05 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Silentx05.webp")
image neus_exp_mouth sad_Silentx06 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Silentx06.webp")
image neus_exp_mouth sad_Silentx07 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Silentx07.webp")
image neus_exp_mouth sad_Silentx08 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Silentx08.webp")
image neus_exp_mouth sad_Silentx09 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Silentx09.webp")
image neus_exp_mouth sad_Silentx10 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Silentx10.webp")
image neus_exp_mouth sad_Silentx11 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Silentx11.webp")

image neus_exp_mouth sad_Talkingx01 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Talkingx01.webp")
image neus_exp_mouth sad_Talkingx02 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Talkingx02.webp")
image neus_exp_mouth sad_Talkingx03 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Talkingx03.webp")
image neus_exp_mouth sad_Talkingx04 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Talkingx04.webp")
image neus_exp_mouth sad_Talkingx05 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Talkingx05.webp")
image neus_exp_mouth sad_Talkingx06 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Talkingx06.webp")
image neus_exp_mouth sad_Talkingx07 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Talkingx07.webp")
image neus_exp_mouth sad_Talkingx08 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Talkingx08.webp")
image neus_exp_mouth sad_Talkingx09 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Talkingx09.webp")
image neus_exp_mouth sad_Talkingx10 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Talkingx10.webp")
image neus_exp_mouth sad_Talkingx11 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Talkingx11.webp")

image neus_exp_mouth sad_Talkingx001 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Talkingx001.webp")
image neus_exp_mouth sad_Talkingx002 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Talkingx002.webp")
image neus_exp_mouth sad_Talkingx003 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Talkingx003.webp")
image neus_exp_mouth sad_Talkingx004 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Talkingx004.webp")
image neus_exp_mouth sad_Talkingx005 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sad_Talkingx005.webp")

image neus_exp_mouth sadbiting_Silentx01 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sadbiting_Silentx01.webp")
image neus_exp_mouth sadbiting_Silentx02 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sadbiting_Silentx02.webp")
image neus_exp_mouth sadbiting_Silentx03 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sadbiting_Silentx03.webp")
image neus_exp_mouth sadbiting_Silentx04 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sadbiting_Silentx04.webp")
image neus_exp_mouth sadbiting_Silentx05 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sadbiting_Silentx05.webp")
image neus_exp_mouth sadbiting_Silentx06 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sadbiting_Silentx06.webp")
image neus_exp_mouth sadbiting_Silentx07 = SaturateTint("images/general/characters/neus/neus_exp_mouth_sadbiting_Silentx07.webp")

#############################################################################################################################
############################################################################################################################
###########################################################################################################################

    ## NEUS POSITIONS

transform neus_center_body:
    transform_anchor True
    xalign 0.5 yalign 0.265 # Eyes line
    zoom 1.0 xpos 0.5 ypos 0.5

transform neus_center_exp:
    transform_anchor True
    xalign 0.5 yalign 0.5 # Eyes line
    zoom 1.0 xpos 0.5 ypos 0.5

####

transform neus_body_atright_position:
    transform_anchor True
    xalign 0.5 yalign 0.265 # Eyes line
    zoom 0.243 xpos 0.8215 ypos 0.35
    #zoom 0.243 xpos 0.824 ypos 0.35

transform neus_exp_atright_position:
    transform_anchor True
    xalign 0.5 yalign 0.5 # Eyes line 
    zoom 0.243 xpos 0.824 ypos 0.35

### # LEFT

transform neus_body_atleft_position:
    transform_anchor True
    xalign 0.5 yalign 0.265 # Eyes line
    xzoom -1.0
    zoom 0.243 xpos 0.2 ypos 0.35

transform neus_exp_atleft_position:
    transform_anchor True
    xzoom -1.0
    xalign 0.5 yalign 0.5 # Eyes line 
    zoom 0.243 xpos 0.2 ypos 0.35

### # LEFT FAR

transform neus_body_atleft_far_position:
    transform_anchor True
    xalign 0.5 yalign 0.265 # Eyes line
    xzoom -1.0
    zoom 0.2 xpos 0.2 ypos 0.435

transform neus_exp_atleft_far_position:
    transform_anchor True
    xzoom -1.0
    xalign 0.5 yalign 0.5 # Eyes line 
    zoom 0.2 xpos 0.2 ypos 0.435


### # Right FAR

transform neus_body_atright_far_position:
    transform_anchor True
    xalign 0.5 yalign 0.265 # Eyes line
    #xzoom -1.0
    zoom 0.2 xpos 0.8 ypos 0.435

transform neus_exp_atright_far_position:
    transform_anchor True
    #xzoom -1.0
    xalign 0.5 yalign 0.5 # Eyes line 
    zoom 0.2 xpos 0.8 ypos 0.435

##

transform neus_body_atright_close_position:
    transform_anchor True
    xalign 0.5 yalign 0.265 # Eyes line
    zoom 0.5 xpos 0.7 ypos 0.35

transform neus_exp_atright_close_position:
    transform_anchor True
    xalign 0.5 yalign 0.5 # Eyes line 
    zoom 0.5 xpos 0.7 ypos 0.35

##

transform neus_body_atright_bitClose_position:
    transform_anchor True
    xalign 0.5 yalign 0.265 # Eyes line
    zoom 0.4 xpos 0.7 ypos 0.35

transform neus_exp_atright_bitClose_position:
    transform_anchor True
    xalign 0.5 yalign 0.5 # Eyes line 
    zoom 0.4 xpos 0.7 ypos 0.35


##

transform neus_body_atcenter_position:
    transform_anchor True
    xalign 0.5 yalign 0.265 # Eyes line
    zoom 0.243 xpos 0.5 ypos 0.35

transform neus_exp_atcenter_position:
    transform_anchor True
    xalign 0.5 yalign 0.5 # Eyes line 
    zoom 0.243 xpos 0.5 ypos 0.35

##

transform neus_body_atcenter_close_position:
    transform_anchor True
    xalign 0.5 yalign 0.265 # Eyes line
    zoom 0.5 xpos 0.5 ypos 0.35

transform neus_exp_atcenter_close_position:
    transform_anchor True
    xalign 0.5 yalign 0.5 # Eyes line 
    zoom 0.5 xpos 0.5 ypos 0.35

##

transform neus_body_atcenter_closeVery_position:
    transform_anchor True
    xalign 0.5 yalign 0.265 # Eyes line
    zoom 0.75 xpos 0.5 ypos 0.35

transform neus_exp_atcenter_closeVery_position:
    transform_anchor True
    xalign 0.5 yalign 0.5 # Eyes line 
    zoom 0.75 xpos 0.5 ypos 0.35

##

transform neus_body_atcenter_closeSuper_position:
    transform_anchor True
    xalign 0.5 yalign 0.265 # Eyes line
    zoom 1.0 xpos 0.5 ypos 0.3

transform neus_exp_atcenter_closeSuper_position:
    transform_anchor True
    xalign 0.5 yalign 0.5 # Eyes line 
    zoom 1.0 xpos 0.5 ypos 0.3

## PAIN

transform neus_body_pain_position:
    transform_anchor True
    xalign 0.5 yalign 0.265 # Eyes line
    zoom 2.5 xpos 0.5 ypos -0.5

transform neus_exp_pain_position:
    transform_anchor True
    xalign 0.5 yalign 0.5 # Eyes line 
    zoom 2.5 xpos 0.5 ypos -0.5

#show neus_body_prove:  ## BODY at right
  #transform_anchor True
    ##xalign 0.5 yalign 0.265 # Eyes line
    #zoom 0.243 xpos 0.8215 ypos 0.35 alpha 0.75

#show neus_exp_hairfront: ## EXPRESSION at right
    #transform_anchor True
    #xalign 0.5 yalign 0.5 # Eyes line
    #zoom 0.243 xpos 0.823 ypos 0.35 alpha 0.75

#############################################################################################################################
############################################################################################################################
###########################################################################################################################


image night04_pedrera_Ngrabhand_night05 = SaturateTint("images/day04/night04/night04_pedrera_Ngrabhand_night05.webp")
image night04_pedrera_Ngrabhand_hold_night05 = SaturateTint("images/day04/night04/night04_pedrera_Ngrabhand_hold_night05.webp")

image night04_pedrera_Ngrabhand_night05_park = SaturateTint("images/day04/night04/night04_pedrera_Ngrabhand_night05.webp") #Aren´t them the same?!
image night04_pedrera_Ngrabhand_hold_night05_park = SaturateTint("images/day04/night04/night04_pedrera_Ngrabhand_hold_night05.webp")

#image night04_pedrera_Ngrabhand_night05_park = im.MatrixColor (
    #"images/day04/night04/night04_pedrera_Ngrabhand_night05.webp",
    #im.matrix.saturation(0.5) * im.matrix.tint(.62, .65, .75)
  #)

#image night04_pedrera_Ngrabhand_hold_night05_park = im.MatrixColor (
    #"images/day04/night04/night04_pedrera_Ngrabhand_hold_night05.webp",
    #im.matrix.saturation(0.5) * im.matrix.tint(.62, .65, .75)
  #)

#############################################################################################################################

## Station
image bg night05_bg_station_ticket = "images/day05/night/night05_bg_station_ticket.webp"
image bg night05_bg_station_previous = "images/day05/night/night05_bg_station_previous.webp"
image bg night05_bg_station_train = "images/day05/night/night05_bg_station_train.webp"
image bg night05_bg_station_sign = "images/day05/night/night05_bg_station_sign.webp"
image bg night05_bg_station_tranvia = "images/day05/night/night05_bg_station_tranvia.webp"
image bg night05_bg_station_funicular = "images/day05/night/night05_bg_station_funicular.webp"
image bg night05_bg_station_funicular_out = "images/day05/night/night05_bg_station_funicular_out.webp"

image bg night05_bg_policestation = "images/day05/night/night05_bg_policestation.webp"

image bg night05_bg_cups_01 = "images/day05/night/night05_bg_cups_01.webp"


image bg night05_bg_castle_flag = "images/day05/night/night05_bg_castle_flag.webp"
image bg night05_bg_castle_queue = "images/day05/night/night05_bg_castle_queue.webp"
image bg night05_bg_castle_siege = "images/day05/night/night05_bg_castle_siege.webp"
image bg_night05_bg_castle_siege = "images/day05/night/night05_bg_castle_siege.webp"
image bg night05_bg_castle_queue_out = "images/day05/night/night05_bg_castle_queue_out.webp"

image bg night05_bg_castle_siege_comp_01:

    contains:
        "bg night05_bg_castle_siege"
        truecenter

    contains:
        "m_body guard"
        mtxell_body_onleftpark_comp_position

    contains:
        "m_arm_r guard_hip"
        mtxell_body_onleftpark_comp_position

    contains:
        "m_exp_mouth serious_Silentx01"
        mtxell_exp_onleftpark_comp_position

    contains:
        "m_exp_over hat"
        mtxell_exp_onleftpark_comp_position

image bg night05_bg_castle_siege_comp_02:

    contains:
        "bg night05_bg_castle_siege"
        truecenter

    contains:
        "m_body guard"
        mtxell_body_onleftpark_comp_position

    contains:
        "m_arm_r guard_pointing"
        mtxell_body_onleftpark_comp_position

    contains:
        "m_exp_mouth serious_Silentx01"
        mtxell_exp_onleftpark_comp_position

    contains:
        "m_exp_over hat"
        mtxell_exp_onleftpark_comp_position

# Funicular

#image bg night05_bg_tranvia_seat = "images/day05/night/night05_bg_tranvia_seat.webp"
image bg night05_bg_tranvia_door = "images/day05/night/night05_bg_tranvia_door.webp"

# Park
image night05_bg_tibidabo_park_00 = "images/day05/night/night05_bg_tibidabo_park_00.webp"
image bg night05_bg_tibidabo_park_00 = "images/day05/night/night05_bg_tibidabo_park_00.webp"
#image bg night05_bg_tibidabo_park_01 = "images/day05/night/night05_bg_tibidabo_park_01.webp"
#image bg night05_bg_tibidabo_park_02 = "images/day05/night/night05_bg_tibidabo_park_02.webp"
#image bg_night05_bg_tibidabo_park_03 = "images/day05/night/night05_bg_tibidabo_park_03.webp"

image bg night05_bg_tibidabo_park_acuatic = "images/day05/night/night05_bg_tibidabo_park_acuatic.webp"
image bg night05_bg_tibidabo_park_ticketpass = "images/day05/night/night05_bg_tibidabo_park_ticketpass.webp"
image bg night05_bg_tibidabo_park_around01 = "images/day05/night/night05_bg_tibidabo_park_around01.webp"
image bg night05_bg_tibidabo_park_coaster_entrance = "images/day05/night/night05_bg_tibidabo_park_coaster_entrance.webp"
image bg night05_bg_tibidabo_park_coaster_entrance_02 = "images/day05/night/night05_bg_tibidabo_park_coaster_entrance_02.webp"
image bg night05_bg_tibidabo_park_shooter_surroundings = "images/day05/night/night05_bg_tibidabo_park_shooter_surroundings.webp"
image bg night05_bg_tibidabo_park_coaster_riding = "images/day05/night/night05_bg_tibidabo_park_coaster_riding.webp"

image bg night05_bg_tibidabo_park_shooter_barra = "images/day05/night/night05_bg_tibidabo_park_shooter_barra.webp"

image bg night05_bg_tibidabo_dinner_bg = "images/day05/night/night05_bg_tibidabo_dinner_bg.webp"
image night05_bg_tibidabo_dinner_table = "images/day05/night/night05_bg_tibidabo_dinner_table.webp"

image night05_bg_park_food orange = SaturateTint("images/day05/night/night05_bg_park_food_orange.webp")
image night05_bg_park_food salchichon = SaturateTint("images/day05/night/night05_bg_park_food_salchichon.webp")
image night05_bg_park_food pizza = SaturateTint("images/day05/night/night05_bg_park_food_pizza.webp")
image night05_bg_park_food dildo = SaturateTint("images/day05/night/night05_bg_park_food_dildo.webp")

#############################################################################################################################
############################################################################################################################
###########################################################################################################################

##### Neus Sit Body Short Dress.

#image n_s_bg_sd_test = "images/general/sit/neus/dressshort/n_s_bg_sd_test03.webp"
##
image bg n_s_bg_sd_01 = "images/general/sit/neus/dressshort/n_s_bg_sd_01.webp" # Background

image bg n_s_bg_sd_park_01 = SaturateTint("images/general/sit/neus/dressshort/n_s_bg_sd_park_01.webp")

image n_s_bg_table_01 = "images/general/sit/neus/dressshort/n_s_bg_table_01.webp"

image n_s_b_sd_leg_l down_closed = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_leg_l_down_closed.webp")
image n_s_b_sd_leg_l up_closed = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_leg_l_up_closed.webp")
image n_s_b_sd_leg_l up_open_skirt_over = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_leg_l_up_open_skirt_over.webp")
image n_s_b_sd_leg_l up_open_skirt_off = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_leg_l_up_open_skirt_off.webp")
image n_s_b_sd_leg_l up_open_skirt_up = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_leg_l_up_open_skirt_up.webp")
image n_s_b_sd_toy dildo = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_toy_dildo.webp")
image n_s_b_sd_leg_l empty = "images/general/empty.webp" 
image n_s_b_sd_leg_r down_closed = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_leg_r_down_closed.webp")
image n_s_b_sd_leg_r empty = "images/general/empty.webp"

image n_s_b_sd_hair_front = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_hair_front.webp")
image n_s_b_sd_face = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_face.webp")
image n_s_b_sd_body = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_body.webp")

image n_s_b_sd_arm_l bank_bitfinger = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_arm_l_bank_bitfinger.webp")
image n_s_b_sd_arm_l bank_rest = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_arm_l_bank_rest.webp")
image n_s_b_sd_arm_l_b bank_rest = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_arm_l_bank_rest.webp")
image n_s_b_sd_arm_l table_fist = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_arm_l_table_fist.webp")
image n_s_b_sd_arm_l table_rest = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_arm_l_table_rest.webp")
image n_s_b_sd_arm_l table_tensed = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_arm_l_table_tensed.webp")
image n_s_b_sd_arm_l empty = "images/general/empty.webp"
image n_s_b_sd_arm_l_b empty = "images/general/empty.webp"

image n_s_b_sd_arm_r bank_rest = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_arm_r_bank_rest.webp")
image n_s_b_sd_arm_r_b bank_rest = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_arm_r_bank_rest.webp")
image n_s_b_sd_arm_r bank_skirthold = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_arm_r_bank_skirthold.webp")
image n_s_b_sd_arm_r bank_onleg_rest = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_arm_r_bank_onleg_rest.webp")
image n_s_b_sd_arm_r bank_onleg_tensed = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_arm_r_bank_onleg_tensed.webp")
image n_s_b_sd_arm_r table_fist = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_arm_r_table_fist.webp")
image n_s_b_sd_arm_r table_rest = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_arm_r_table_rest.webp")
image n_s_b_sd_arm_r table_tensed = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_arm_r_table_tensed.webp")
image n_s_b_sd_arm_r empty = "images/general/empty.webp"
image n_s_b_sd_arm_r_b empty = "images/general/empty.webp"


image n_s_b_sd_hair_back = SaturateTint("images/general/sit/neus/dressshort/n_s_b_sd_hair_back.webp")

#############################################################################################################################
############################################################################################################################
###########################################################################################################################

    ## DARK


#image n_s_b_sd_body_superdark = im.MatrixColor("images/general/sit/neus/dressshort/n_s_b_sd_body.webp",
                            #im.matrix.saturation(0.5) * im.matrix.tint(.22, .25, .45))

#image n_s_b_sd_body_dark = im.MatrixColor("images/general/sit/neus/dressshort/n_s_b_sd_body.webp",
                            #im.matrix.saturation(0.7) * im.matrix.tint(.8, .8, .9))

#############################################################################################################################
############################################################################################################################
###########################################################################################################################

## 
## { Neus Sit Short Dress POSITIONS }
##

transform n_s_b_sd_funicular_position:
    transform_anchor True
    xalign 0.5 yalign 0.2145 # Eyes line NeusShortDress
    zoom 0.2 xpos 0.6 ypos 0.205

transform n_s_exp_sd_funicular_position:
    transform_anchor True
    xalign 0.5 yalign 0.5
    zoom 0.2 xpos 0.6 ypos 0.205

## 
##

transform n_s_b_sd_funicular_close_position:
    transform_anchor True
    xalign 0.5 yalign 0.2145 # Eyes line NeusShortDress
    zoom 0.5 xpos 0.6 ypos 0.4

transform n_s_exp_sd_funicular_close_position:
    transform_anchor True
    xalign 0.5 yalign 0.5
    zoom 0.5 xpos 0.6 ypos 0.4

## 
##

transform n_s_b_sd_cup_close_position:
    transform_anchor True
    xalign 0.5 yalign 0.2145 # Eyes line NeusShortDress
    zoom 0.4 xpos 0.6 ypos 0.4

transform n_s_exp_sd_cup_close_position:
    transform_anchor True
    xalign 0.5 yalign 0.5
    zoom 0.4 xpos 0.6 ypos 0.4


##
transform n_s_b_sd_table_position:
    transform_anchor True
    xalign 0.5 yalign 0.2145 # Eyes line NeusShortDress
    zoom 0.24 xpos 0.6 ypos 0.24

transform n_s_exp_sd_table_position:
    transform_anchor True
    xalign 0.5 yalign 0.5
    zoom 0.24 xpos 0.6 ypos 0.24

#############################################################################################################################
############################################################################################################################

image n_s_b_sd_funicular_comp 01:

    contains:
        "bg n_s_bg_sd_01"
        truecenter
        zoom 0.5

    contains:
        "n_s_b_sd_hair_back"
        truecenter
        n_s_b_sd_funicular_position

    contains:
        "n_s_b_sd_body"
        truecenter
        n_s_b_sd_funicular_position

    contains:
        "n_s_b_sd_face"
        truecenter
        n_s_b_sd_funicular_position

    ## Expressions

    contains:
        "n_s_exp_blush 04"
        truecenter
        n_s_exp_sd_funicular_position
    contains:
        "n_s_exp_mouth happybiting_Silentx07"
        truecenter
        n_s_exp_sd_funicular_position
    contains:
        "n_s_exp_eyes 05"
        truecenter
        n_s_exp_sd_funicular_position
    contains:
        "n_s_exp_iris front05"
        truecenter
        n_s_exp_sd_funicular_position
    contains:
        "n_s_exp_eyebrows suspiciousx04"
        truecenter
        n_s_exp_sd_funicular_position
    contains:
        "n_s_exp_glasses"
        truecenter
        n_s_exp_sd_funicular_position

    contains:
        "n_s_b_sd_arm_l bank_rest"
        truecenter
        n_s_b_sd_funicular_position
    contains:
        "n_s_b_sd_hair_front"
        truecenter
        n_s_b_sd_funicular_position
    contains:
        "n_s_b_sd_leg_l up_open_skirt_off"
        truecenter
        n_s_b_sd_funicular_position
    contains:
        "n_s_b_sd_leg_r empty"
        truecenter
        n_s_b_sd_funicular_position
    contains:
        "n_s_b_sd_arm_r bank_skirthold"
        truecenter
        n_s_b_sd_funicular_position


#############################################################################################################################
############################################################################################################################

image n_s_b_sd_funicular_comp 02:

    contains:
        "bg n_s_bg_sd_01"
        truecenter
        zoom 0.5

    contains:
        "n_s_b_sd_hair_back"
        truecenter
        n_s_b_sd_funicular_position

    contains:
        "n_s_b_sd_body"
        truecenter
        n_s_b_sd_funicular_position

    contains:
        "n_s_b_sd_face"
        truecenter
        n_s_b_sd_funicular_position

    ## Expressions

    contains:
        "n_s_exp_blush 04"
        truecenter
        n_s_exp_sd_funicular_position
    contains:
        "n_s_exp_mouth happybiting_Silentx07"
        truecenter
        n_s_exp_sd_funicular_position
    contains:
        "n_s_exp_eyes 05"
        truecenter
        n_s_exp_sd_funicular_position
    contains:
        "n_s_exp_iris front05"
        truecenter
        n_s_exp_sd_funicular_position
    contains:
        "n_s_exp_eyebrows suspiciousx04"
        truecenter
        n_s_exp_sd_funicular_position
    contains:
        "n_s_exp_glasses"
        truecenter
        n_s_exp_sd_funicular_position

    contains:
        "n_s_b_sd_arm_l bank_rest"
        truecenter
        n_s_b_sd_funicular_position
    contains:
        "n_s_b_sd_hair_front"
        truecenter
        n_s_b_sd_funicular_position
    contains:
        "n_s_b_sd_leg_l up_open_skirt_up"
        truecenter
        n_s_b_sd_funicular_position
    contains:
        "n_s_b_sd_leg_r empty"
        truecenter
        n_s_b_sd_funicular_position
    contains:
        "n_s_b_sd_arm_l bank_bitfinger"
        truecenter
        n_s_b_sd_funicular_position
    contains:
        "n_s_b_sd_arm_r bank_onleg_tensed"
        truecenter
        n_s_b_sd_funicular_position

#############################################################################################################################
############################################################################################################################

image n_s_b_sd_park_undertable_comp 01:

    contains:
        "bg n_s_bg_sd_park_01"
        truecenter
        zoom 0.5

    contains:
        "n_s_b_sd_hair_back"
        truecenter
        n_s_b_sd_funicular_position

    contains:
        "n_s_b_sd_body"
        truecenter
        n_s_b_sd_funicular_position

    contains:
        "n_s_b_sd_face"
        truecenter
        n_s_b_sd_funicular_position

    ## Expressions

    contains:
        "n_s_exp_blush 04"
        truecenter
        n_s_exp_sd_funicular_position
    contains:
        "n_s_exp_mouth happybiting_Silentx07"
        truecenter
        n_s_exp_sd_funicular_position
    contains:
        "n_s_exp_eyes 05"
        truecenter
        n_s_exp_sd_funicular_position
    contains:
        "n_s_exp_iris front05"
        truecenter
        n_s_exp_sd_funicular_position
    contains:
        "n_s_exp_eyebrows suspiciousx04"
        truecenter
        n_s_exp_sd_funicular_position
    contains:
        "n_s_exp_glasses"
        truecenter
        n_s_exp_sd_funicular_position

    contains:
        "n_s_b_sd_arm_l bank_rest"
        truecenter
        n_s_b_sd_funicular_position
    contains:
        "n_s_b_sd_hair_front"
        truecenter
        n_s_b_sd_funicular_position
    contains:
        "n_s_b_sd_leg_l up_open_skirt_off"
        truecenter
        n_s_b_sd_funicular_position
    contains:
        "n_s_b_sd_leg_r empty"
        truecenter
        n_s_b_sd_funicular_position
    contains:
        "n_s_b_sd_arm_l bank_bitfinger"
        truecenter
        n_s_b_sd_funicular_position
    contains:
        "n_s_b_sd_arm_r bank_skirthold"
        truecenter
        n_s_b_sd_funicular_position
    contains:
        "n_s_b_sd_toy dildo"
        truecenter
        n_s_b_sd_funicular_position

    contains:
        "n_s_bg_table_01"
        truecenter
        zoom 0.5

#############################################################################################################################
############################################################################################################################


image bg night05_bg_wheel_far = "images/day05/night/night05_bg_wheel_far.webp"
image bg night05_bg_wheel_queue = "images/day05/night/night05_bg_wheel_queue.webp"
image bg night05_bg_wheel_seat = "images/day05/night/night05_bg_wheel_seat.webp"
image night05_bg_wheel_seat_cabin = "images/day05/night/night05_bg_wheel_seat_cabin.webp"
image night05_bg_wheel_seat_structure = "images/day05/night/night05_bg_wheel_seat_structure.webp"
image night05_bg_wheel_seat_structure_lights = "images/day05/night/night05_bg_wheel_seat_structure_lights.webp"
image bg night05_bg_wheel_city = "images/day05/night/night05_bg_wheel_city.webp"

##################################################################################################################

image fireworks_yellow_a 01 = "images/effects/fireworks/yellow_a/01.webp"

image fireworks_yellow_a_01 = "images/effects/fireworks/yellow_a/01.webp"
image fireworks_yellow_a_02 = "images/effects/fireworks/yellow_a/02.webp"
image fireworks_yellow_a_03 = "images/effects/fireworks/yellow_a/03.webp"
image fireworks_yellow_a_04 = "images/effects/fireworks/yellow_a/04.webp"
image fireworks_yellow_a_05 = "images/effects/fireworks/yellow_a/05.webp"
image fireworks_yellow_a_06 = "images/effects/fireworks/yellow_a/06.webp"
image fireworks_yellow_a_07 = "images/effects/fireworks/yellow_a/07.webp"
image fireworks_yellow_a_08 = "images/effects/fireworks/yellow_a/08.webp"
image fireworks_yellow_a_09 = "images/effects/fireworks/yellow_a/09.webp"
image fireworks_yellow_a_10 = "images/effects/fireworks/yellow_a/10.webp"
image fireworks_yellow_a_11 = "images/effects/fireworks/yellow_a/11.webp"
image fireworks_yellow_a_12 = "images/effects/fireworks/yellow_a/12.webp"
image fireworks_yellow_a_13 = "images/effects/fireworks/yellow_a/13.webp"
image fireworks_yellow_a_14 = "images/effects/fireworks/yellow_a/14.webp"
image fireworks_yellow_a_15 = "images/effects/fireworks/yellow_a/15.webp"
image fireworks_yellow_a_16 = "images/effects/fireworks/yellow_a/16.webp"
image fireworks_yellow_a_17 = "images/effects/fireworks/yellow_a/17.webp"
image fireworks_yellow_a_18 = "images/effects/fireworks/yellow_a/18.webp"
image fireworks_yellow_a_19 = "images/effects/fireworks/yellow_a/19.webp"
image fireworks_yellow_a_20 = "images/effects/fireworks/yellow_a/20.webp"
image fireworks_yellow_a_21 = "images/effects/fireworks/yellow_a/21.webp"
image fireworks_yellow_a_22 = "images/effects/fireworks/yellow_a/22.webp"
image fireworks_yellow_a_23 = "images/effects/fireworks/yellow_a/23.webp"
image fireworks_yellow_a_24 = "images/effects/fireworks/yellow_a/24.webp"
image fireworks_yellow_a_25 = "images/effects/fireworks/yellow_a/25.webp"
image fireworks_yellow_a_26 = "images/effects/fireworks/yellow_a/26.webp"
image fireworks_yellow_a_27 = "images/effects/fireworks/yellow_a/27.webp"
image fireworks_yellow_a_28 = "images/effects/fireworks/yellow_a/28.webp"
image fireworks_yellow_a_29 = "images/effects/fireworks/yellow_a/29.webp"
image fireworks_yellow_a_30 = "images/effects/fireworks/yellow_a/30.webp"
image fireworks_yellow_a_31 = "images/effects/fireworks/yellow_a/31.webp"
image fireworks_yellow_a_32 = "images/effects/fireworks/yellow_a/32.webp"
image fireworks_yellow_a_33 = "images/effects/fireworks/yellow_a/33.webp"
image fireworks_yellow_a_34 = "images/effects/fireworks/yellow_a/34.webp"
image fireworks_yellow_a_35 = "images/effects/fireworks/yellow_a/35.webp"
image fireworks_yellow_a_36 = "images/effects/fireworks/yellow_a/36.webp"
image fireworks_yellow_a_37 = "images/effects/fireworks/yellow_a/37.webp"
image fireworks_yellow_a_38 = "images/effects/fireworks/yellow_a/38.webp"
image fireworks_yellow_a_39 = "images/effects/fireworks/yellow_a/39.webp"
image fireworks_yellow_a_40 = "images/effects/fireworks/yellow_a/40.webp"
image fireworks_yellow_a_41 = "images/effects/fireworks/yellow_a/41.webp"
image fireworks_yellow_a_42 = "images/effects/fireworks/yellow_a/42.webp"
image fireworks_yellow_a_43 = "images/effects/fireworks/yellow_a/43.webp"
image fireworks_yellow_a_44 = "images/effects/fireworks/yellow_a/44.webp"
image fireworks_yellow_a_45 = "images/effects/fireworks/yellow_a/45.webp"
image fireworks_yellow_a_46 = "images/effects/fireworks/yellow_a/46.webp"

image fireworks_yellow_a_comp:

    contains:
        "fireworks_yellow_a_01"
        truecenter
        0.1
        "fireworks_yellow_a_02"
        truecenter
        0.1
        "fireworks_yellow_a_03"
        truecenter
        0.1
        "fireworks_yellow_a_04"
        truecenter
        0.1
        "fireworks_yellow_a_05"
        truecenter
        0.1
        "fireworks_yellow_a_06"
        truecenter
        0.1
        "fireworks_yellow_a_07"
        truecenter
        0.1
        "fireworks_yellow_a_08"
        truecenter
        0.1
        "fireworks_yellow_a_09"
        truecenter
        0.1
        "fireworks_yellow_a_10"
        truecenter
        0.1
        "fireworks_yellow_a_11"
        truecenter
        0.1
        "fireworks_yellow_a_12"
        truecenter
        0.1
        "fireworks_yellow_a_13"
        truecenter
        0.1
        "fireworks_yellow_a_14"
        truecenter
        0.1
        "fireworks_yellow_a_15"
        truecenter
        0.1
        "fireworks_yellow_a_16"
        truecenter
        0.1
        "fireworks_yellow_a_17"
        truecenter
        0.1
        "fireworks_yellow_a_18"
        truecenter
        0.1
        "fireworks_yellow_a_19"
        truecenter
        0.1
        "fireworks_yellow_a_20"
        truecenter
        0.1
        "fireworks_yellow_a_21"
        truecenter
        0.1
        "fireworks_yellow_a_22"
        truecenter
        0.1
        "fireworks_yellow_a_23"
        truecenter
        0.1
        "fireworks_yellow_a_24"
        truecenter
        0.1
        "fireworks_yellow_a_25"
        truecenter
        0.1
        "fireworks_yellow_a_26"
        truecenter
        0.1
        "fireworks_yellow_a_27"
        truecenter
        0.1
        "fireworks_yellow_a_28"
        truecenter
        0.1
        "fireworks_yellow_a_29"
        truecenter
        0.1
        "fireworks_yellow_a_30"
        truecenter
        0.1
        "fireworks_yellow_a_31"
        truecenter
        0.1
        "fireworks_yellow_a_32"
        truecenter
        0.1
        "fireworks_yellow_a_33"
        truecenter
        0.1
        "fireworks_yellow_a_34"
        truecenter
        0.1
        "fireworks_yellow_a_35"
        truecenter
        0.1
        "fireworks_yellow_a_36"
        truecenter
        0.1
        "fireworks_yellow_a_37"
        truecenter
        0.1
        "fireworks_yellow_a_38"
        truecenter
        0.1
        "fireworks_yellow_a_39"
        truecenter
        0.1
        "fireworks_yellow_a_40"
        truecenter
        0.1
        "fireworks_yellow_a_41"
        truecenter
        0.1
        "fireworks_yellow_a_42"
        truecenter
        0.1
        "fireworks_yellow_a_43"
        truecenter
        0.1
        "fireworks_yellow_a_44"
        truecenter
        0.1
        "fireworks_yellow_a_45"
        truecenter
        0.1
        "fireworks_yellow_a_46"
        truecenter
        0.1

        "black"
        pause 4.2
        repeat

    contains:
        "sunglow 02" # 4.6 seconds
        subpixel True
        truecenter
        alpha 0.0
        zoom 0.5
        easeout_quad 1.0 alpha 1.0
        easeout_quad 3.6 alpha 0.0
        #pause 4.2
        #repeat





##################################################################################################################

image fireworks_yellow_b 01 = "images/effects/fireworks/yellow_b/01.webp"

image fireworks_yellow_b_01 = "images/effects/fireworks/yellow_b/01.webp"
image fireworks_yellow_b_02 = "images/effects/fireworks/yellow_b/02.webp"
image fireworks_yellow_b_03 = "images/effects/fireworks/yellow_b/03.webp"
image fireworks_yellow_b_04 = "images/effects/fireworks/yellow_b/04.webp"
image fireworks_yellow_b_05 = "images/effects/fireworks/yellow_b/05.webp"
image fireworks_yellow_b_06 = "images/effects/fireworks/yellow_b/06.webp"
image fireworks_yellow_b_07 = "images/effects/fireworks/yellow_b/07.webp"
image fireworks_yellow_b_08 = "images/effects/fireworks/yellow_b/08.webp"
image fireworks_yellow_b_09 = "images/effects/fireworks/yellow_b/09.webp"
image fireworks_yellow_b_10 = "images/effects/fireworks/yellow_b/10.webp"
image fireworks_yellow_b_11 = "images/effects/fireworks/yellow_b/11.webp"
image fireworks_yellow_b_12 = "images/effects/fireworks/yellow_b/12.webp"
image fireworks_yellow_b_13 = "images/effects/fireworks/yellow_b/13.webp"
image fireworks_yellow_b_14 = "images/effects/fireworks/yellow_b/14.webp"
image fireworks_yellow_b_15 = "images/effects/fireworks/yellow_b/15.webp"
image fireworks_yellow_b_16 = "images/effects/fireworks/yellow_b/16.webp"
image fireworks_yellow_b_17 = "images/effects/fireworks/yellow_b/17.webp"
image fireworks_yellow_b_18 = "images/effects/fireworks/yellow_b/18.webp"
image fireworks_yellow_b_19 = "images/effects/fireworks/yellow_b/19.webp"
image fireworks_yellow_b_20 = "images/effects/fireworks/yellow_b/20.webp"
image fireworks_yellow_b_21 = "images/effects/fireworks/yellow_b/21.webp"
image fireworks_yellow_b_22 = "images/effects/fireworks/yellow_b/22.webp"
image fireworks_yellow_b_23 = "images/effects/fireworks/yellow_b/23.webp"
image fireworks_yellow_b_24 = "images/effects/fireworks/yellow_b/24.webp"
image fireworks_yellow_b_25 = "images/effects/fireworks/yellow_b/25.webp"
image fireworks_yellow_b_26 = "images/effects/fireworks/yellow_b/26.webp"
image fireworks_yellow_b_27 = "images/effects/fireworks/yellow_b/27.webp"
image fireworks_yellow_b_28 = "images/effects/fireworks/yellow_b/28.webp"
image fireworks_yellow_b_29 = "images/effects/fireworks/yellow_b/29.webp"
image fireworks_yellow_b_30 = "images/effects/fireworks/yellow_b/30.webp"
image fireworks_yellow_b_31 = "images/effects/fireworks/yellow_b/31.webp"
image fireworks_yellow_b_32 = "images/effects/fireworks/yellow_b/32.webp"
image fireworks_yellow_b_33 = "images/effects/fireworks/yellow_b/33.webp"
image fireworks_yellow_b_34 = "images/effects/fireworks/yellow_b/34.webp"
image fireworks_yellow_b_35 = "images/effects/fireworks/yellow_b/35.webp"
image fireworks_yellow_b_36 = "images/effects/fireworks/yellow_b/36.webp"
image fireworks_yellow_b_37 = "images/effects/fireworks/yellow_b/37.webp"
image fireworks_yellow_b_38 = "images/effects/fireworks/yellow_b/38.webp"
image fireworks_yellow_b_39 = "images/effects/fireworks/yellow_b/39.webp"
image fireworks_yellow_b_40 = "images/effects/fireworks/yellow_b/40.webp"
image fireworks_yellow_b_41 = "images/effects/fireworks/yellow_b/41.webp"

image fireworks_yellow_b_comp:

    pause 3.0

    contains:
        "black"
        0.1
        "fireworks_yellow_b_01"
        truecenter
        0.1
        "fireworks_yellow_b_02"
        truecenter
        0.1
        "fireworks_yellow_b_03"
        truecenter
        0.1
        "fireworks_yellow_b_04"
        truecenter
        0.1
        "fireworks_yellow_b_05"
        truecenter
        0.1
        "fireworks_yellow_b_06"
        truecenter
        0.1
        "fireworks_yellow_b_07"
        truecenter
        0.1
        "fireworks_yellow_b_08"
        truecenter
        0.1
        "fireworks_yellow_b_09"
        truecenter
        0.1
        "fireworks_yellow_b_10"
        truecenter
        0.1
        "fireworks_yellow_b_11"
        truecenter
        0.1
        "fireworks_yellow_b_12"
        truecenter
        0.1
        "fireworks_yellow_b_13"
        truecenter
        0.1
        "fireworks_yellow_b_14"
        truecenter
        0.1
        "fireworks_yellow_b_15"
        truecenter
        0.1
        "fireworks_yellow_b_16"
        truecenter
        0.1
        "fireworks_yellow_b_17"
        truecenter
        0.1
        "fireworks_yellow_b_18"
        truecenter
        0.1
        "fireworks_yellow_b_19"
        truecenter
        0.1
        "fireworks_yellow_b_20"
        truecenter
        0.1
        "fireworks_yellow_b_21"
        truecenter
        0.1
        "fireworks_yellow_b_22"
        truecenter
        0.1
        "fireworks_yellow_b_23"
        truecenter
        0.1
        "fireworks_yellow_b_24"
        truecenter
        0.1
        "fireworks_yellow_b_25"
        truecenter
        0.1
        "fireworks_yellow_b_26"
        truecenter
        0.1
        "fireworks_yellow_b_27"
        truecenter
        0.1
        "fireworks_yellow_b_28"
        truecenter
        0.1
        "fireworks_yellow_b_29"
        truecenter
        0.1
        "fireworks_yellow_b_30"
        truecenter
        0.1
        "fireworks_yellow_b_31"
        truecenter
        0.1
        "fireworks_yellow_b_32"
        truecenter
        0.1
        "fireworks_yellow_b_33"
        truecenter
        0.1
        "fireworks_yellow_b_34"
        truecenter
        0.1
        "fireworks_yellow_b_35"
        truecenter
        0.1
        "fireworks_yellow_b_36"
        truecenter
        0.1
        "fireworks_yellow_b_37"
        truecenter
        0.1
        "fireworks_yellow_b_38"
        truecenter
        0.1
        "fireworks_yellow_b_39"
        truecenter
        0.1
        "fireworks_yellow_b_40"
        truecenter
        0.1
        "fireworks_yellow_b_41"
        truecenter
        0.1

        "black"
        pause 3.3
        repeat

##################################################################################################################

image fireworks_red_a 01 = "images/effects/fireworks/red_a/01.webp"

image fireworks_red_a_01 = "images/effects/fireworks/red_a/01.webp"
image fireworks_red_a_02 = "images/effects/fireworks/red_a/02.webp"
image fireworks_red_a_03 = "images/effects/fireworks/red_a/03.webp"
image fireworks_red_a_04 = "images/effects/fireworks/red_a/04.webp"
image fireworks_red_a_05 = "images/effects/fireworks/red_a/05.webp"
image fireworks_red_a_06 = "images/effects/fireworks/red_a/06.webp"
image fireworks_red_a_07 = "images/effects/fireworks/red_a/07.webp"
image fireworks_red_a_08 = "images/effects/fireworks/red_a/08.webp"
image fireworks_red_a_09 = "images/effects/fireworks/red_a/09.webp"
image fireworks_red_a_10 = "images/effects/fireworks/red_a/10.webp"
image fireworks_red_a_11 = "images/effects/fireworks/red_a/11.webp"
image fireworks_red_a_12 = "images/effects/fireworks/red_a/12.webp"
image fireworks_red_a_13 = "images/effects/fireworks/red_a/13.webp"
image fireworks_red_a_14 = "images/effects/fireworks/red_a/14.webp"
image fireworks_red_a_15 = "images/effects/fireworks/red_a/15.webp"
image fireworks_red_a_16 = "images/effects/fireworks/red_a/16.webp"
image fireworks_red_a_17 = "images/effects/fireworks/red_a/17.webp"
image fireworks_red_a_18 = "images/effects/fireworks/red_a/18.webp"
image fireworks_red_a_19 = "images/effects/fireworks/red_a/19.webp"
image fireworks_red_a_20 = "images/effects/fireworks/red_a/20.webp"
image fireworks_red_a_21 = "images/effects/fireworks/red_a/21.webp"
image fireworks_red_a_22 = "images/effects/fireworks/red_a/22.webp"
image fireworks_red_a_23 = "images/effects/fireworks/red_a/23.webp"
image fireworks_red_a_24 = "images/effects/fireworks/red_a/24.webp"
image fireworks_red_a_25 = "images/effects/fireworks/red_a/25.webp"
image fireworks_red_a_26 = "images/effects/fireworks/red_a/26.webp"
image fireworks_red_a_27 = "images/effects/fireworks/red_a/27.webp"
image fireworks_red_a_28 = "images/effects/fireworks/red_a/28.webp"
image fireworks_red_a_29 = "images/effects/fireworks/red_a/29.webp"
image fireworks_red_a_30 = "images/effects/fireworks/red_a/30.webp"
image fireworks_red_a_31 = "images/effects/fireworks/red_a/31.webp"
image fireworks_red_a_32 = "images/effects/fireworks/red_a/32.webp"
image fireworks_red_a_33 = "images/effects/fireworks/red_a/33.webp"
image fireworks_red_a_34 = "images/effects/fireworks/red_a/34.webp"
image fireworks_red_a_35 = "images/effects/fireworks/red_a/35.webp"
image fireworks_red_a_36 = "images/effects/fireworks/red_a/36.webp"
image fireworks_red_a_37 = "images/effects/fireworks/red_a/37.webp"
image fireworks_red_a_38 = "images/effects/fireworks/red_a/38.webp"
image fireworks_red_a_39 = "images/effects/fireworks/red_a/39.webp"
image fireworks_red_a_40 = "images/effects/fireworks/red_a/40.webp"
image fireworks_red_a_41 = "images/effects/fireworks/red_a/41.webp"
image fireworks_red_a_42 = "images/effects/fireworks/red_a/42.webp"
image fireworks_red_a_43 = "images/effects/fireworks/red_a/43.webp"
image fireworks_red_a_44 = "images/effects/fireworks/red_a/44.webp"
image fireworks_red_a_45 = "images/effects/fireworks/red_a/45.webp"
image fireworks_red_a_46 = "images/effects/fireworks/red_a/46.webp"
image fireworks_red_a_47 = "images/effects/fireworks/red_a/47.webp"
image fireworks_red_a_48 = "images/effects/fireworks/red_a/48.webp"
image fireworks_red_a_49 = "images/effects/fireworks/red_a/49.webp"
image fireworks_red_a_50 = "images/effects/fireworks/red_a/50.webp"
image fireworks_red_a_51 = "images/effects/fireworks/red_a/51.webp"
image fireworks_red_a_52 = "images/effects/fireworks/red_a/52.webp"
image fireworks_red_a_53 = "images/effects/fireworks/red_a/53.webp"
image fireworks_red_a_54 = "images/effects/fireworks/red_a/54.webp"
image fireworks_red_a_55 = "images/effects/fireworks/red_a/55.webp"
image fireworks_red_a_56 = "images/effects/fireworks/red_a/56.webp"
image fireworks_red_a_57 = "images/effects/fireworks/red_a/57.webp"
image fireworks_red_a_58 = "images/effects/fireworks/red_a/58.webp"
image fireworks_red_a_59 = "images/effects/fireworks/red_a/59.webp"
image fireworks_red_a_60 = "images/effects/fireworks/red_a/60.webp"
image fireworks_red_a_61 = "images/effects/fireworks/red_a/61.webp"
image fireworks_red_a_62 = "images/effects/fireworks/red_a/62.webp"
image fireworks_red_a_63 = "images/effects/fireworks/red_a/63.webp"
image fireworks_red_a_64 = "images/effects/fireworks/red_a/64.webp"
image fireworks_red_a_65 = "images/effects/fireworks/red_a/65.webp"
image fireworks_red_a_66 = "images/effects/fireworks/red_a/66.webp"
image fireworks_red_a_67 = "images/effects/fireworks/red_a/67.webp"
image fireworks_red_a_68 = "images/effects/fireworks/red_a/68.webp"
image fireworks_red_a_69 = "images/effects/fireworks/red_a/69.webp"
image fireworks_red_a_70 = "images/effects/fireworks/red_a/70.webp"
image fireworks_red_a_71 = "images/effects/fireworks/red_a/71.webp"
image fireworks_red_a_72 = "images/effects/fireworks/red_a/72.webp"
image fireworks_red_a_73 = "images/effects/fireworks/red_a/73.webp"
image fireworks_red_a_74 = "images/effects/fireworks/red_a/74.webp"
image fireworks_red_a_75 = "images/effects/fireworks/red_a/75.webp"
image fireworks_red_a_76 = "images/effects/fireworks/red_a/76.webp"
image fireworks_red_a_77 = "images/effects/fireworks/red_a/77.webp"
image fireworks_red_a_78 = "images/effects/fireworks/red_a/78.webp"
image fireworks_red_a_79 = "images/effects/fireworks/red_a/79.webp"

image fireworks_red_a_comp:

    pause 9.0

    contains:
        "black"
        0.1
        "fireworks_red_a_01"
        truecenter
        0.1
        "fireworks_red_a_02"
        truecenter
        0.1
        "fireworks_red_a_03"
        truecenter
        0.1
        "fireworks_red_a_04"
        truecenter
        0.1
        "fireworks_red_a_05"
        truecenter
        0.1
        "fireworks_red_a_06"
        truecenter
        0.1
        "fireworks_red_a_07"
        truecenter
        0.1
        "fireworks_red_a_08"
        truecenter
        0.1
        "fireworks_red_a_09"
        truecenter
        0.1
        "fireworks_red_a_10"
        truecenter
        0.1
        "fireworks_red_a_11"
        truecenter
        0.1
        "fireworks_red_a_12"
        truecenter
        0.1
        "fireworks_red_a_13"
        truecenter
        0.1
        "fireworks_red_a_14"
        truecenter
        0.1
        "fireworks_red_a_15"
        truecenter
        0.1
        "fireworks_red_a_16"
        truecenter
        0.1
        "fireworks_red_a_17"
        truecenter
        0.1
        "fireworks_red_a_18"
        truecenter
        0.1
        "fireworks_red_a_19"
        truecenter
        0.1
        "fireworks_red_a_20"
        truecenter
        0.1
        "fireworks_red_a_21"
        truecenter
        0.1
        "fireworks_red_a_22"
        truecenter
        0.1
        "fireworks_red_a_23"
        truecenter
        0.1
        "fireworks_red_a_24"
        truecenter
        0.1
        "fireworks_red_a_25"
        truecenter
        0.1
        "fireworks_red_a_26"
        truecenter
        0.1
        "fireworks_red_a_27"
        truecenter
        0.1
        "fireworks_red_a_28"
        truecenter
        0.1
        "fireworks_red_a_29"
        truecenter
        0.1
        "fireworks_red_a_30"
        truecenter
        0.1
        "fireworks_red_a_31"
        truecenter
        0.1
        "fireworks_red_a_32"
        truecenter
        0.1
        "fireworks_red_a_33"
        truecenter
        0.1
        "fireworks_red_a_34"
        truecenter
        0.1
        "fireworks_red_a_35"
        truecenter
        0.1
        "fireworks_red_a_36"
        truecenter
        0.1
        "fireworks_red_a_37"
        truecenter
        0.1
        "fireworks_red_a_38"
        truecenter
        0.1
        "fireworks_red_a_39"
        truecenter
        0.1
        "fireworks_red_a_40"
        truecenter
        0.1
        "fireworks_red_a_41"
        truecenter
        0.1
        "fireworks_red_a_42"
        truecenter
        0.1
        "fireworks_red_a_43"
        truecenter
        0.1
        "fireworks_red_a_44"
        truecenter
        0.1
        "fireworks_red_a_45"
        truecenter
        0.1
        "fireworks_red_a_46"
        truecenter
        0.1
        "fireworks_red_a_47"
        truecenter
        0.1
        "fireworks_red_a_48"
        truecenter
        0.1
        "fireworks_red_a_49"
        truecenter
        0.1
        "fireworks_red_a_50"
        truecenter
        0.1
        "fireworks_red_a_51"
        truecenter
        0.1
        "fireworks_red_a_52"
        truecenter
        0.1
        "fireworks_red_a_53"
        truecenter
        0.1
        "fireworks_red_a_54"
        truecenter
        0.1
        "fireworks_red_a_55"
        truecenter
        0.1
        "fireworks_red_a_56"
        truecenter
        0.1
        "fireworks_red_a_57"
        truecenter
        0.1
        "fireworks_red_a_58"
        truecenter
        0.1
        "fireworks_red_a_59"
        truecenter
        0.1
        "fireworks_red_a_60"
        truecenter
        0.1
        "fireworks_red_a_61"
        truecenter
        0.1
        "fireworks_red_a_62"
        truecenter
        0.1
        "fireworks_red_a_63"
        truecenter
        0.1
        "fireworks_red_a_64"
        truecenter
        0.1
        "fireworks_red_a_65"
        truecenter
        0.1
        "fireworks_red_a_66"
        truecenter
        0.1
        "fireworks_red_a_67"
        truecenter
        0.1
        "fireworks_red_a_68"
        truecenter
        0.1
        "fireworks_red_a_69"
        truecenter
        0.1
        "fireworks_red_a_70"
        truecenter
        0.1
        "fireworks_red_a_71"
        truecenter
        0.1
        "fireworks_red_a_72"
        truecenter
        0.1
        "fireworks_red_a_73"
        truecenter
        0.1
        "fireworks_red_a_74"
        truecenter
        0.1
        "fireworks_red_a_75"
        truecenter
        0.1
        "fireworks_red_a_76"
        truecenter
        0.1
        "fireworks_red_a_77"
        truecenter
        0.1
        "fireworks_red_a_78"
        truecenter
        0.1
        "fireworks_red_a_79"
        truecenter
        0.1

        "black"
        pause 2.3
        repeat


##################################################################################################################

image fireworks_colors_a 01 = "images/effects/fireworks/colors_a/01.webp"

image fireworks_colors_a_01 = "images/effects/fireworks/colors_a/01.webp"
image fireworks_colors_a_02 = "images/effects/fireworks/colors_a/02.webp"
image fireworks_colors_a_03 = "images/effects/fireworks/colors_a/03.webp"
image fireworks_colors_a_04 = "images/effects/fireworks/colors_a/04.webp"
image fireworks_colors_a_05 = "images/effects/fireworks/colors_a/05.webp"
image fireworks_colors_a_06 = "images/effects/fireworks/colors_a/06.webp"
image fireworks_colors_a_07 = "images/effects/fireworks/colors_a/07.webp"
image fireworks_colors_a_08 = "images/effects/fireworks/colors_a/08.webp"
image fireworks_colors_a_09 = "images/effects/fireworks/colors_a/09.webp"
image fireworks_colors_a_10 = "images/effects/fireworks/colors_a/10.webp"
image fireworks_colors_a_11 = "images/effects/fireworks/colors_a/11.webp"
image fireworks_colors_a_12 = "images/effects/fireworks/colors_a/12.webp"
image fireworks_colors_a_13 = "images/effects/fireworks/colors_a/13.webp"
image fireworks_colors_a_14 = "images/effects/fireworks/colors_a/14.webp"
image fireworks_colors_a_15 = "images/effects/fireworks/colors_a/15.webp"
image fireworks_colors_a_16 = "images/effects/fireworks/colors_a/16.webp"
image fireworks_colors_a_17 = "images/effects/fireworks/colors_a/17.webp"
image fireworks_colors_a_18 = "images/effects/fireworks/colors_a/18.webp"
image fireworks_colors_a_19 = "images/effects/fireworks/colors_a/19.webp"
image fireworks_colors_a_20 = "images/effects/fireworks/colors_a/20.webp"
image fireworks_colors_a_21 = "images/effects/fireworks/colors_a/21.webp"
image fireworks_colors_a_22 = "images/effects/fireworks/colors_a/22.webp"
image fireworks_colors_a_23 = "images/effects/fireworks/colors_a/23.webp"
image fireworks_colors_a_24 = "images/effects/fireworks/colors_a/24.webp"
image fireworks_colors_a_25 = "images/effects/fireworks/colors_a/25.webp"
image fireworks_colors_a_26 = "images/effects/fireworks/colors_a/26.webp"
image fireworks_colors_a_27 = "images/effects/fireworks/colors_a/27.webp"
image fireworks_colors_a_28 = "images/effects/fireworks/colors_a/28.webp"
image fireworks_colors_a_29 = "images/effects/fireworks/colors_a/29.webp"
image fireworks_colors_a_30 = "images/effects/fireworks/colors_a/30.webp"
image fireworks_colors_a_31 = "images/effects/fireworks/colors_a/31.webp"
image fireworks_colors_a_32 = "images/effects/fireworks/colors_a/32.webp"
image fireworks_colors_a_33 = "images/effects/fireworks/colors_a/33.webp"
image fireworks_colors_a_34 = "images/effects/fireworks/colors_a/34.webp"
image fireworks_colors_a_35 = "images/effects/fireworks/colors_a/35.webp"
image fireworks_colors_a_36 = "images/effects/fireworks/colors_a/36.webp"
image fireworks_colors_a_37 = "images/effects/fireworks/colors_a/37.webp"
image fireworks_colors_a_38 = "images/effects/fireworks/colors_a/38.webp"
image fireworks_colors_a_39 = "images/effects/fireworks/colors_a/39.webp"
image fireworks_colors_a_40 = "images/effects/fireworks/colors_a/40.webp"
image fireworks_colors_a_41 = "images/effects/fireworks/colors_a/41.webp"
image fireworks_colors_a_42 = "images/effects/fireworks/colors_a/42.webp"
image fireworks_colors_a_43 = "images/effects/fireworks/colors_a/43.webp"
image fireworks_colors_a_44 = "images/effects/fireworks/colors_a/44.webp"
image fireworks_colors_a_45 = "images/effects/fireworks/colors_a/45.webp"
image fireworks_colors_a_46 = "images/effects/fireworks/colors_a/46.webp"
image fireworks_colors_a_47 = "images/effects/fireworks/colors_a/47.webp"
image fireworks_colors_a_48 = "images/effects/fireworks/colors_a/48.webp"
image fireworks_colors_a_49 = "images/effects/fireworks/colors_a/49.webp"
image fireworks_colors_a_50 = "images/effects/fireworks/colors_a/50.webp"

image fireworks_colors_a_comp:

    pause 7.0

    contains:
        "black"
        0.1
        "fireworks_colors_a_01"
        truecenter
        0.1
        "fireworks_colors_a_02"
        truecenter
        0.1
        "fireworks_colors_a_03"
        truecenter
        0.1
        "fireworks_colors_a_04"
        truecenter
        0.1
        "fireworks_colors_a_05"
        truecenter
        0.1
        "fireworks_colors_a_06"
        truecenter
        0.1
        "fireworks_colors_a_07"
        truecenter
        0.1
        "fireworks_colors_a_08"
        truecenter
        0.1
        "fireworks_colors_a_09"
        truecenter
        0.1
        "fireworks_colors_a_10"
        truecenter
        0.1
        "fireworks_colors_a_11"
        truecenter
        0.1
        "fireworks_colors_a_12"
        truecenter
        0.1
        "fireworks_colors_a_13"
        truecenter
        0.1
        "fireworks_colors_a_14"
        truecenter
        0.1
        "fireworks_colors_a_15"
        truecenter
        0.1
        "fireworks_colors_a_16"
        truecenter
        0.1
        "fireworks_colors_a_17"
        truecenter
        0.1
        "fireworks_colors_a_18"
        truecenter
        0.1
        "fireworks_colors_a_19"
        truecenter
        0.1
        "fireworks_colors_a_20"
        truecenter
        0.1
        "fireworks_colors_a_21"
        truecenter
        0.1
        "fireworks_colors_a_22"
        truecenter
        0.1
        "fireworks_colors_a_23"
        truecenter
        0.1
        "fireworks_colors_a_24"
        truecenter
        0.1
        "fireworks_colors_a_25"
        truecenter
        0.1
        "fireworks_colors_a_26"
        truecenter
        0.1
        "fireworks_colors_a_27"
        truecenter
        0.1
        "fireworks_colors_a_28"
        truecenter
        0.1
        "fireworks_colors_a_29"
        truecenter
        0.1
        "fireworks_colors_a_30"
        truecenter
        0.1
        "fireworks_colors_a_31"
        truecenter
        0.1
        "fireworks_colors_a_32"
        truecenter
        0.1
        "fireworks_colors_a_33"
        truecenter
        0.1
        "fireworks_colors_a_34"
        truecenter
        0.1
        "fireworks_colors_a_35"
        truecenter
        0.1
        "fireworks_colors_a_36"
        truecenter
        0.1
        "fireworks_colors_a_37"
        truecenter
        0.1
        "fireworks_colors_a_38"
        truecenter
        0.1
        "fireworks_colors_a_39"
        truecenter
        0.1
        "fireworks_colors_a_40"
        truecenter
        0.1
        "fireworks_colors_a_41"
        truecenter
        0.1
        "fireworks_colors_a_42"
        truecenter
        0.1
        "fireworks_colors_a_43"
        truecenter
        0.1
        "fireworks_colors_a_44"
        truecenter
        0.1
        "fireworks_colors_a_45"
        truecenter
        0.1
        "fireworks_colors_a_46"
        truecenter
        0.1
        "fireworks_colors_a_47"
        truecenter
        0.1
        "fireworks_colors_a_48"
        truecenter
        0.1
        "fireworks_colors_a_49"
        truecenter
        0.1
        "fireworks_colors_a_50"
        truecenter
        0.1
        "black"
        pause 3.6
        repeat


##################################################################################################################
image fireworks_colors_b 01 = "images/effects/fireworks/colors_b/01.webp"

image fireworks_colors_b_01 = "images/effects/fireworks/colors_b/01.webp"
image fireworks_colors_b_02 = "images/effects/fireworks/colors_b/02.webp"
image fireworks_colors_b_03 = "images/effects/fireworks/colors_b/03.webp"
image fireworks_colors_b_04 = "images/effects/fireworks/colors_b/04.webp"
image fireworks_colors_b_05 = "images/effects/fireworks/colors_b/05.webp"
image fireworks_colors_b_06 = "images/effects/fireworks/colors_b/06.webp"
image fireworks_colors_b_07 = "images/effects/fireworks/colors_b/07.webp"
image fireworks_colors_b_08 = "images/effects/fireworks/colors_b/08.webp"
image fireworks_colors_b_09 = "images/effects/fireworks/colors_b/09.webp"
image fireworks_colors_b_10 = "images/effects/fireworks/colors_b/10.webp"
image fireworks_colors_b_11 = "images/effects/fireworks/colors_b/11.webp"
image fireworks_colors_b_12 = "images/effects/fireworks/colors_b/12.webp"
image fireworks_colors_b_13 = "images/effects/fireworks/colors_b/13.webp"
image fireworks_colors_b_14 = "images/effects/fireworks/colors_b/14.webp"
image fireworks_colors_b_15 = "images/effects/fireworks/colors_b/15.webp"
image fireworks_colors_b_16 = "images/effects/fireworks/colors_b/16.webp"
image fireworks_colors_b_17 = "images/effects/fireworks/colors_b/17.webp"
image fireworks_colors_b_18 = "images/effects/fireworks/colors_b/18.webp"
image fireworks_colors_b_19 = "images/effects/fireworks/colors_b/19.webp"
image fireworks_colors_b_20 = "images/effects/fireworks/colors_b/20.webp"
image fireworks_colors_b_21 = "images/effects/fireworks/colors_b/21.webp"
image fireworks_colors_b_22 = "images/effects/fireworks/colors_b/22.webp"
image fireworks_colors_b_23 = "images/effects/fireworks/colors_b/23.webp"
image fireworks_colors_b_24 = "images/effects/fireworks/colors_b/24.webp"
image fireworks_colors_b_25 = "images/effects/fireworks/colors_b/25.webp"
image fireworks_colors_b_26 = "images/effects/fireworks/colors_b/26.webp"
image fireworks_colors_b_27 = "images/effects/fireworks/colors_b/27.webp"
image fireworks_colors_b_28 = "images/effects/fireworks/colors_b/28.webp"
image fireworks_colors_b_29 = "images/effects/fireworks/colors_b/29.webp"
image fireworks_colors_b_30 = "images/effects/fireworks/colors_b/30.webp"
image fireworks_colors_b_31 = "images/effects/fireworks/colors_b/31.webp"
image fireworks_colors_b_32 = "images/effects/fireworks/colors_b/32.webp"
image fireworks_colors_b_33 = "images/effects/fireworks/colors_b/33.webp"
image fireworks_colors_b_34 = "images/effects/fireworks/colors_b/34.webp"
image fireworks_colors_b_35 = "images/effects/fireworks/colors_b/35.webp"
image fireworks_colors_b_36 = "images/effects/fireworks/colors_b/36.webp"
image fireworks_colors_b_37 = "images/effects/fireworks/colors_b/37.webp"
image fireworks_colors_b_38 = "images/effects/fireworks/colors_b/38.webp"
image fireworks_colors_b_39 = "images/effects/fireworks/colors_b/39.webp"
image fireworks_colors_b_40 = "images/effects/fireworks/colors_b/40.webp"
image fireworks_colors_b_41 = "images/effects/fireworks/colors_b/41.webp"
image fireworks_colors_b_42 = "images/effects/fireworks/colors_b/42.webp"
image fireworks_colors_b_43 = "images/effects/fireworks/colors_b/43.webp"
image fireworks_colors_b_44 = "images/effects/fireworks/colors_b/44.webp"
image fireworks_colors_b_45 = "images/effects/fireworks/colors_b/45.webp"
image fireworks_colors_b_46 = "images/effects/fireworks/colors_b/46.webp"
image fireworks_colors_b_47 = "images/effects/fireworks/colors_b/47.webp"
image fireworks_colors_b_48 = "images/effects/fireworks/colors_b/48.webp"
image fireworks_colors_b_49 = "images/effects/fireworks/colors_b/49.webp"
image fireworks_colors_b_50 = "images/effects/fireworks/colors_b/50.webp"
image fireworks_colors_b_51 = "images/effects/fireworks/colors_b/51.webp"
image fireworks_colors_b_52 = "images/effects/fireworks/colors_b/52.webp"
image fireworks_colors_b_53 = "images/effects/fireworks/colors_b/53.webp"
image fireworks_colors_b_54 = "images/effects/fireworks/colors_b/54.webp"
image fireworks_colors_b_55 = "images/effects/fireworks/colors_b/55.webp"
image fireworks_colors_b_56 = "images/effects/fireworks/colors_b/56.webp"
image fireworks_colors_b_57 = "images/effects/fireworks/colors_b/57.webp"
image fireworks_colors_b_58 = "images/effects/fireworks/colors_b/58.webp"
image fireworks_colors_b_59 = "images/effects/fireworks/colors_b/59.webp"
image fireworks_colors_b_60 = "images/effects/fireworks/colors_b/60.webp"
image fireworks_colors_b_61 = "images/effects/fireworks/colors_b/61.webp"
image fireworks_colors_b_62 = "images/effects/fireworks/colors_b/62.webp"
image fireworks_colors_b_63 = "images/effects/fireworks/colors_b/63.webp"
image fireworks_colors_b_64 = "images/effects/fireworks/colors_b/64.webp"
image fireworks_colors_b_65 = "images/effects/fireworks/colors_b/65.webp"
image fireworks_colors_b_66 = "images/effects/fireworks/colors_b/66.webp"
image fireworks_colors_b_67 = "images/effects/fireworks/colors_b/67.webp"
image fireworks_colors_b_68 = "images/effects/fireworks/colors_b/68.webp"
image fireworks_colors_b_69 = "images/effects/fireworks/colors_b/69.webp"
image fireworks_colors_b_70 = "images/effects/fireworks/colors_b/70.webp"
image fireworks_colors_b_71 = "images/effects/fireworks/colors_b/71.webp"
image fireworks_colors_b_72 = "images/effects/fireworks/colors_b/72.webp"
image fireworks_colors_b_73 = "images/effects/fireworks/colors_b/73.webp"
image fireworks_colors_b_74 = "images/effects/fireworks/colors_b/74.webp"
image fireworks_colors_b_75 = "images/effects/fireworks/colors_b/75.webp"
image fireworks_colors_b_76 = "images/effects/fireworks/colors_b/76.webp"
image fireworks_colors_b_77 = "images/effects/fireworks/colors_b/77.webp"
image fireworks_colors_b_78 = "images/effects/fireworks/colors_b/78.webp"
image fireworks_colors_b_79 = "images/effects/fireworks/colors_b/79.webp"
image fireworks_colors_b_80 = "images/effects/fireworks/colors_b/80.webp"
image fireworks_colors_b_81 = "images/effects/fireworks/colors_b/81.webp"
image fireworks_colors_b_82 = "images/effects/fireworks/colors_b/82.webp"
image fireworks_colors_b_83 = "images/effects/fireworks/colors_b/83.webp"
image fireworks_colors_b_84 = "images/effects/fireworks/colors_b/84.webp"
image fireworks_colors_b_85 = "images/effects/fireworks/colors_b/85.webp"
image fireworks_colors_b_86 = "images/effects/fireworks/colors_b/86.webp"
image fireworks_colors_b_87 = "images/effects/fireworks/colors_b/87.webp"
image fireworks_colors_b_88 = "images/effects/fireworks/colors_b/88.webp"
image fireworks_colors_b_89 = "images/effects/fireworks/colors_b/89.webp"
image fireworks_colors_b_90 = "images/effects/fireworks/colors_b/90.webp"
image fireworks_colors_b_91 = "images/effects/fireworks/colors_b/91.webp"
image fireworks_colors_b_92 = "images/effects/fireworks/colors_b/92.webp"
image fireworks_colors_b_93 = "images/effects/fireworks/colors_b/93.webp"
image fireworks_colors_b_94 = "images/effects/fireworks/colors_b/94.webp"
image fireworks_colors_b_95 = "images/effects/fireworks/colors_b/95.webp"
image fireworks_colors_b_96 = "images/effects/fireworks/colors_b/96.webp"
image fireworks_colors_b_97 = "images/effects/fireworks/colors_b/97.webp"
image fireworks_colors_b_98 = "images/effects/fireworks/colors_b/98.webp"
image fireworks_colors_b_99 = "images/effects/fireworks/colors_b/99.webp"
image fireworks_colors_b_100 = "images/effects/fireworks/colors_b/100.webp"
image fireworks_colors_b_101 = "images/effects/fireworks/colors_b/101.webp"
image fireworks_colors_b_102 = "images/effects/fireworks/colors_b/102.webp"

image fireworks_colors_b_comp:

    pause 5.0

    contains:
        "black"
        0.1
        "fireworks_colors_b_01"
        truecenter
        0.1
        "fireworks_colors_b_02"
        truecenter
        0.1
        "fireworks_colors_b_03"
        truecenter
        0.1
        "fireworks_colors_b_04"
        truecenter
        0.1
        "fireworks_colors_b_05"
        truecenter
        0.1
        "fireworks_colors_b_06"
        truecenter
        0.1
        "fireworks_colors_b_07"
        truecenter
        0.1
        "fireworks_colors_b_08"
        truecenter
        0.1
        "fireworks_colors_b_09"
        truecenter
        0.1
        "fireworks_colors_b_10"
        truecenter
        0.1
        "fireworks_colors_b_11"
        truecenter
        0.1
        "fireworks_colors_b_12"
        truecenter
        0.1
        "fireworks_colors_b_13"
        truecenter
        0.1
        "fireworks_colors_b_14"
        truecenter
        0.1
        "fireworks_colors_b_15"
        truecenter
        0.1
        "fireworks_colors_b_16"
        truecenter
        0.1
        "fireworks_colors_b_17"
        truecenter
        0.1
        "fireworks_colors_b_18"
        truecenter
        0.1
        "fireworks_colors_b_19"
        truecenter
        0.1
        "fireworks_colors_b_20"
        truecenter
        0.1
        "fireworks_colors_b_21"
        truecenter
        0.1
        "fireworks_colors_b_22"
        truecenter
        0.1
        "fireworks_colors_b_23"
        truecenter
        0.1
        "fireworks_colors_b_24"
        truecenter
        0.1
        "fireworks_colors_b_25"
        truecenter
        0.1
        "fireworks_colors_b_26"
        truecenter
        0.1
        "fireworks_colors_b_27"
        truecenter
        0.1
        "fireworks_colors_b_28"
        truecenter
        0.1
        "fireworks_colors_b_29"
        truecenter
        0.1
        "fireworks_colors_b_30"
        truecenter
        0.1
        "fireworks_colors_b_31"
        truecenter
        0.1
        "fireworks_colors_b_32"
        truecenter
        0.1
        "fireworks_colors_b_33"
        truecenter
        0.1
        "fireworks_colors_b_34"
        truecenter
        0.1
        "fireworks_colors_b_35"
        truecenter
        0.1
        "fireworks_colors_b_36"
        truecenter
        0.1
        "fireworks_colors_b_37"
        truecenter
        0.1
        "fireworks_colors_b_38"
        truecenter
        0.1
        "fireworks_colors_b_39"
        truecenter
        0.1
        "fireworks_colors_b_40"
        truecenter
        0.1
        "fireworks_colors_b_41"
        truecenter
        0.1
        "fireworks_colors_b_42"
        truecenter
        0.1
        "fireworks_colors_b_43"
        truecenter
        0.1
        "fireworks_colors_b_44"
        truecenter
        0.1
        "fireworks_colors_b_45"
        truecenter
        0.1
        "fireworks_colors_b_46"
        truecenter
        0.1
        "fireworks_colors_b_47"
        truecenter
        0.1
        "fireworks_colors_b_48"
        truecenter
        0.1
        "fireworks_colors_b_49"
        truecenter
        0.1
        "fireworks_colors_b_50"
        truecenter
        0.1
        "fireworks_colors_b_51"
        truecenter
        0.1
        "fireworks_colors_b_52"
        truecenter
        0.1
        "fireworks_colors_b_53"
        truecenter
        0.1
        "fireworks_colors_b_54"
        truecenter
        0.1
        "fireworks_colors_b_55"
        truecenter
        0.1
        "fireworks_colors_b_56"
        truecenter
        0.1
        "fireworks_colors_b_57"
        truecenter
        0.1
        "fireworks_colors_b_58"
        truecenter
        0.1
        "fireworks_colors_b_59"
        truecenter
        0.1
        "fireworks_colors_b_60"
        truecenter
        0.1
        "fireworks_colors_b_61"
        truecenter
        0.1
        "fireworks_colors_b_62"
        truecenter
        0.1
        "fireworks_colors_b_63"
        truecenter
        0.1
        "fireworks_colors_b_64"
        truecenter
        0.1
        "fireworks_colors_b_65"
        truecenter
        0.1
        "fireworks_colors_b_66"
        truecenter
        0.1
        "fireworks_colors_b_67"
        truecenter
        0.1
        "fireworks_colors_b_68"
        truecenter
        0.1
        "fireworks_colors_b_69"
        truecenter
        0.1
        "fireworks_colors_b_70"
        truecenter
        0.1
        "fireworks_colors_b_71"
        truecenter
        0.1
        "fireworks_colors_b_72"
        truecenter
        0.1
        "fireworks_colors_b_73"
        truecenter
        0.1
        "fireworks_colors_b_74"
        truecenter
        0.1
        "fireworks_colors_b_75"
        truecenter
        0.1
        "fireworks_colors_b_76"
        truecenter
        0.1
        "fireworks_colors_b_77"
        truecenter
        0.1
        "fireworks_colors_b_78"
        truecenter
        0.1
        "fireworks_colors_b_79"
        truecenter
        0.1
        "fireworks_colors_b_80"
        truecenter
        0.1
        "fireworks_colors_b_81"
        truecenter
        0.1
        "fireworks_colors_b_82"
        truecenter
        0.1
        "fireworks_colors_b_83"
        truecenter
        0.1
        "fireworks_colors_b_84"
        truecenter
        0.1
        "fireworks_colors_b_85"
        truecenter
        0.1
        "fireworks_colors_b_86"
        truecenter
        0.1
        "fireworks_colors_b_87"
        truecenter
        0.1
        "fireworks_colors_b_88"
        truecenter
        0.1
        "fireworks_colors_b_89"
        truecenter
        0.1
        "fireworks_colors_b_90"
        truecenter
        0.1
        "fireworks_colors_b_91"
        truecenter
        0.1
        "fireworks_colors_b_92"
        truecenter
        0.1
        "fireworks_colors_b_93"
        truecenter
        0.1
        "fireworks_colors_b_94"
        truecenter
        0.1
        "fireworks_colors_b_95"
        truecenter
        0.1
        "fireworks_colors_b_96"
        truecenter
        0.1
        "fireworks_colors_b_97"
        truecenter
        0.1
        "fireworks_colors_b_98"
        truecenter
        0.1
        "fireworks_colors_b_99"
        truecenter
        0.1
        "fireworks_colors_b_100"
        truecenter
        0.1
        "fireworks_colors_b_101"
        truecenter
        0.1
        "fireworks_colors_b_102"
        truecenter
        0.1

        "black"
        pause 3.6
        repeat

##################################################################################################################
###############################################################################################
############################################################################

image night05_bg_wheel_city_fireworks:

    contains:
        "bg night05_bg_wheel_city"
        truecenter

    contains:
        "fireworks_yellow_a_comp"
        truecenter
        alpha 1.0
        additive 1.0
        zoom 1.5 ypos -0.2

    contains:
        "fireworks_red_a_comp"
        truecenter
        alpha 1.0
        additive 1.0
        zoom 2.0 xpos 0.2 ypos 0.0

    contains:
        "fireworks_yellow_b_comp"
        transform_anchor True
        xalign 0.5 yalign 0.42
        alpha 1.0
        additive 1.0
        zoom 1.5 xpos 0.8 ypos -0.5
    contains:
        "fireworks_colors_b_comp"
        truecenter
        alpha 1.0
        additive 1.0
        zoom 2.5 xpos -0.1 ypos -0.1

    contains:
        "fireworks_colors_a_comp"
        truecenter
        rotate -5
        alpha 1.0
        additive 1.0
        zoom 2.0 xpos 1.0 ypos 0.2



image night05_bg_wheel_seat_structure_comp:

    contains:
        "night05_bg_wheel_seat_structure"
        truecenter

    contains:
        "night05_bg_wheel_seat_structure_lights"
        subpixel True
        truecenter
        additive 1.0
        block:
            easein_quad 5.0 alpha 0.0
            easein_quad 5.0 alpha 1.0
            easein_quad 1.0 alpha 0.0
            easein_quad 1.0 alpha 1.0
            easein_quad 0.5 alpha 0.0
            easein_quad 0.5 alpha 1.0
            easein_quad 0.5 alpha 0.0
            easein_quad 0.5 alpha 1.0
            easein_quad 0.5 alpha 0.0
            easein_quad 0.5 alpha 1.0
            easein_quad 0.5 alpha 0.0
            easein_quad 0.5 alpha 1.0
            repeat

image night05_bg_wheel_seat_structure_comp02:

    contains:
        "night05_bg_wheel_seat_structure"
        truecenter

    contains:
        "night05_bg_wheel_seat_structure_lights"
        subpixel True
        truecenter
        additive 1.0
        block:
            easein_quad 5.0 alpha 0.0
            easein_quad 5.0 alpha 1.0
            easein_quad 1.0 alpha 0.0
            easein_quad 1.0 alpha 1.0
            easein_quad 0.5 alpha 0.0
            easein_quad 0.5 alpha 1.0
            easein_quad 0.5 alpha 0.0
            easein_quad 0.5 alpha 1.0
            easein_quad 0.5 alpha 0.0
            easein_quad 0.5 alpha 1.0
            easein_quad 0.5 alpha 0.0
            easein_quad 0.5 alpha 1.0
            repeat


#############################################################################################################################
############################################################################################################################

## CODE BY REMIX (From Discord)

label saturation_ting_values_check:

    $ saturation_tint_values = {
        # name : ( saturation, red, green, blue )
        "default" : (1.0, 1.0, 1.0, 1.0), # <--- values used if key not found
        "dark" : (0.7, 0.8, 0.8, 0.9), # dark
        "verydark" : (0.6, 0.6, 0.6, 0.75), #Testing
        "reallydark" : (0.5, 0.42, 0.45, 0.5),
        "superdark" : (0.5, 0.22, 0.25, 0.45), # superdark
        "green" : (0.7, 0.97, 1.0, 0.95), # restaurant
        "afternoon"  : (0.7, 0.97, 0.87, 0.7),
        "underwater"  : (0.5, 0.4, 0.65, 0.8), #underwater
        "candle"  : (0.7, 0.99, 0.9, 0.75),
        "reddish"  : (0.6, 0.99, 0.5, 0.5),
        "veryDarkBlue"  : (0.6, 0.3, 0.4, 0.6),
        "darkBlue"  : (0.7, 0.4, 0.6, 0.9)
        ## add more if wanted
    }

    return

default saturation_tint_values = {
    # name : ( saturation, red, green, blue )
    "default" : (1.0, 1.0, 1.0, 1.0), # <--- values used if key not found
    "dark" : (0.7, 0.8, 0.8, 0.9), # dark
    "verydark" : (0.6, 0.6, 0.6, 0.75), #Testing
    "reallydark" : (0.5, 0.42, 0.45, 0.5),
    "superdark" : (0.5, 0.22, 0.25, 0.45), # superdark
    "green" : (0.7, 0.97, 1.0, 0.95), # restaurant
    "afternoon"  : (0.7, 0.97, 0.87, 0.7),
    "underwater"  : (0.5, 0.4, 0.65, 0.8), #underwater
    "candle"  : (0.7, 0.99, 0.9, 0.75),
    "reddish"  : (0.6, 0.99, 0.5, 0.5),
    "veryDarkBlue"  : (0.6, 0.3, 0.4, 0.6),
    "darkBlue"  : (0.7, 0.4, 0.6, 0.9)
    ## add more if wanted
}
default saturation_tint_level = None



init python:

    class SaturateTint(renpy.display.layout.DynamicDisplayable):
        """
        A dynamic image that applies a saturation and tint

        @args:
            image: file path and name using Ren'Py [] interpolation
                   for any varriable parts
        """

        def __init__(self, *args, **kwargs):

            self.file_name = args[0]

            self.monitor_vars = [
                "saturation_tint_level"
            ]

            interpolated_var = "" 
            for k in self.file_name:
                if k == "[":
                    interpolated_var = "-" 
                    continue
                if interpolated_var:
                    if k == "]":
                        self.monitor_vars.append( interpolated_var[1:] )
                        interpolated_var = ""
                        continue
                    interpolated_var += k

            self.monitor_values = self.get_monitored_values()

            self.cache = None

            kwargs.update( {
                '_predict_function' : self.predict_images } )

            super(SaturateTint, self).__init__( self.get_tinted_image, 
                                                *args, 
                                                **kwargs )

        def get_monitored_values(self):
            return [ globals().get(k, 'default') for k in self.monitor_vars ]

        def get_tinted_image(self, st, at, *args, **kwargs):
            """
            Return image to use for this time
            """
            current_values = self.get_monitored_values()

            if not self.cache or current_values != self.monitor_values:

                #print("Generating New with Matrix as: {} vs {}".format(
                    #current_values, self.monitor_values))

                self.monitor_values = current_values

                s,r,g,b = saturation_tint_values.get(
                    saturation_tint_level, saturation_tint_values['default'] )

                if (s,r,g,b) == (1.0, 1.0, 1.0, 1.0):

                    self.cache = renpy.substitute(self.file_name)

                else:

                    self.cache = im.MatrixColor(
                        renpy.substitute(self.file_name),
                        im.matrix.saturation(s) * im.matrix.tint(r,g,b))

            return self.cache, 0.0


        def predict_images(self):

            return [ renpy.substitute(self.file_name) ]

#default kaori_pose = "kaori"
#image n2y = SaturateTint("images/kaori/[kaori_pose].webp")

