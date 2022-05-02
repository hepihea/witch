########################################################
## Gallery Class tweaks to support automatic thumbnails
########################################################

init -1 python:

    def gallery_thumbnail(self, image=None, crop=None):

        self.button_.thumbnail = image if image else None

        self.button_.thumbnail_crop = crop

    Gallery.thumbnail = gallery_thumbnail


    def gallery_thumbnail_info(self, button):

        thumbnail = "images/gallery/gThumbs/gThumb_locked.webp"
        crop = (100, 0, 600, 600)

        if button.images and button.images[0].displayables:

            thumbnail = button.images[0].displayables[0]

        if hasattr(button, "thumbnail") and button.thumbnail:

            thumbnail = button.thumbnail

            crop = button.thumbnail_crop

        return (thumbnail, crop)

    Gallery.thumbnail_info = gallery_thumbnail_info

#############################################
## gThumbS
############################################

image gThumb_locked = "images/gallery/gThumbs/gThumb_locked.webp"
image gThumb_wip = "images/gallery/gThumbs/gThumb_wip.webp"
image gThumb_color01 = "images/gallery/gThumbs/gThumb_color01.webp"

########################################################################################
########################################################################################
######################################################################################## # RAPE NEUS DAY 01

##rape_neus

image afternoon01_BathroomrapeB00_gallery:
    contains:
        "afternoon01_bg Bathroom_02"
    contains:
        "afternoon01_BathroomrapeB00"
        afternoon01_BathroomrapeB00_gallery_transform
    contains:
        "afternoon01_Bathroom rapeB02"
        afternoon01_BathroomrapeB00_gallery_transform
    contains:
        "afternoon01_Bathroom_rapeB_glasses"
        afternoon01_BathroomrapeB00_gallery_transform
        
transform afternoon01_BathroomrapeB00_gallery_transform:
    # zoom 1.0 xalign 0.5 yalign 0.0 #Top
    # block:
    #     ease_quad 20.0 zoom 1.0 xalign 0.5 yalign 1.0 #Bottom
    #     pause 10.0
    #     ease_quad 20.0 zoom 1.0 xalign 0.5 yalign 0.0 #Top
    #     repeat
    truecenter
    zoom 0.5
    

image afternoon01_Bathroom rapeA01_gallery:
    contains:
        "afternoon01_bg Bathroom_02 "
    contains:
        "afternoon01_Bathroom rapeA01"
        # zoom 1.0 xalign 0.0 yalign 0.0 #Top
        # block:
        #     easeout_quad 20.0 zoom 1.0 xalign 0.6 yalign 0.8 #Bottom
        #     easein_quad 20.0 zoom 0.6 xalign 0.5 yalign 0.2 #General Vision
        #     easeout_quad 20.0 zoom 1.0 xalign 0.0 yalign 0.0 #Top
        #     repeat
        truecenter
        zoom 0.5

image afternoon01_Bathroom rapeBbright_gallery:
    contains:
        "afternoon01_bg Bathroom"
    contains:
        "afternoon01_BathroomrapeB00"
        zoom 0.45 xpos 0.15
    contains:
        "afternoon01_Bathroom rapeB012col"
        zoom 0.45 xpos 0.15
    contains:
        "afternoon01_Bathroom_rapeB_glasses"
        zoom 0.45 xpos 0.15

image afternoon01_Bathroom rapeB01_gallery:
    contains:
        "afternoon01_bg Bathroom"
    contains:
        "afternoon01_BathroomrapeB00"
        zoom 0.45 xpos 0.15
    contains:
        "afternoon01_Bathroom rapeB01"
        zoom 0.45 xpos 0.15
    contains:
        "afternoon01_Bathroom_rapeB_glasses"
        zoom 0.45 xpos 0.15

image afternoon01_Bathroom rapeB02_gallery:
    contains:
        "afternoon01_bg Bathroom"
    contains:
        "afternoon01_BathroomrapeB00"
        zoom 0.45 xpos 0.15
    contains:
        "afternoon01_Bathroom rapeB02"
        zoom 0.45 xpos 0.15
    contains:
        "afternoon01_Bathroom_rapeB_glasses"
        zoom 0.45 xpos 0.15


image afternoon01_Bathroom rapeBite_gallery: #Neus Bite Hand
    contains:
        "afternoon01_Bathroom rapeBite"
    contains:
        "afternoon01_Bathroom_rapeBite_glasses"

image afternoon01_Bathroomm rapeBiteCock_gallery: #Neus Bite Dick
    contains:
        "afternoon01_Bathroomm rapeBiteCock"
    contains:
        "afternoon01_Bathroomm_rapeBiteCock_glasses"
        
image afternoon01_Bathroom_rapeSlap_gallery: #Neus being slapped
    contains:
        "afternoon01_Bathroom_rapeSlap"
    contains:
        "afternoon01_Bathroom_rapeSlap_glasses"
    contains:
        "afternoon01_Bathroom_rapeSlap_blood"
        
image afternoon01_Bathroom_Rape_Crying_neus_gcom: #Neus Crying
    contains:
        "afternoon01_bg Bathroom_cryingneus"
    contains:
        "afternoon01_Bathroom_Rape_Crying_neus_body 01"
    contains:
        "afternoon01_Bathroom_Rape_Crying_neus_glasses"
    contains:
        "afternoon01_Bathroom_Rape_Crying_neus_eyes down"
    # contains:
    #     "afternoon01_Bathroom_Rape_Crying_prot_hand"

image afternoon01_Bathroom_Rape_Crying_neus_arm_gcom: #Neus Crying
    contains:
        "afternoon01_bg Bathroom_cryingneus"
    contains:
        "afternoon01_Bathroom_Rape_Crying_neus_body arm"
    contains:
        "afternoon01_Bathroom_Rape_Crying_neus_glasses"
    contains:
        "afternoon01_Bathroom_Rape_Crying_neus_eyes up"
    contains:
        "afternoon01_Bathroom_Rape_Crying_prot_hand"

image afternoon01_Bathroom rapePunch_gallery:

    contains:
        "afternoon01_Bathroom rapePunch"
        truecenter
        zoom 0.5

image night01_atHome_DidacTired_gcom:
    contains:
        "night01_bg dinner"
    contains:
        "night01_dinner_didac_body"
    contains:
        "night01_dinner_didac_mouth sad_Silent"

########################################################################################
########################################################################################
######################################################################################## # DAY 02
##
## DIDAC AT BED

image didac_bed_gcom_01:
    contains:
        "didac_bed_bed over"
    contains:
        "didac_bed_d_body 01"
    contains:
        "didac_bed_d_blush 01"
    contains:
        "didac_bed_d_eyes 03"
    contains:
        "didac_bed_d_eyespup front03"
    contains:
        "didac_bed_d_eyebrows surprisex02"
    contains:
        "didac_bed_d_mouth sad_Silentx01"
    contains:
        "didac_bed_d_hair 01"

image didac_bed_gcom_02:
    contains:
        "didac_bed_bed over"
    contains:
        "didac_bed_d_body 02"
    contains:
        "didac_bed_d_blush 02"
    contains:
        "didac_bed_d_eyes 03"
    contains:
        "didac_bed_d_eyespup front03"
    contains:
        "didac_bed_d_eyebrows suspiciousx02"
    contains:
        "didac_bed_d_mouth sad_Silentx02"
    contains:
        "didac_bed_d_hair 02"

image didac_bed_gcom_03:
    contains:
        "didac_bed_bed over_sweaty"
    contains:
        "didac_bed_d_body 03"
    contains:
        "didac_bed_d_blush 03"
    contains:
        "didac_bed_d_eyes 07"
    contains:
        "didac_bed_d_eyebrows angryx04"
    contains:
        "didac_bed_d_mouth sad_Silentx04"
    contains:
        "didac_bed_d_hair 03"

image didac_bed_gcom_04:
    contains:
        "didac_bed_bed over_sweaty"
    contains:
        "didac_bed_d_body 04"
    contains:
        "didac_bed_d_blush 04"
    contains:
        "didac_bed_d_eyes 06"
    contains:
        "didac_bed_d_eyebrows sadx01"
    contains:
        "didac_bed_d_mouth sad_Silentx02"
    contains:
        "didac_bed_d_hair 04"

image didac_bed_gcom_05:
    contains:
        "didac_bed_bed over_sweaty"
    contains:
        "didac_bed_d_body 04"
    contains:
        "didac_bed_d_blush 04"
    contains:
        "didac_bed_d_eyes 06"
    contains:
        "didac_bed_d_eyebrows angryx02"
    contains:
        "didac_bed_d_mouth sad_Talkingx04"
    contains:
        "didac_bed_d_hair 04"
    contains:
        "didac_bed_headtowel dry"
    contains:
        "didac_bed_d_blanket 01"

image didac_bed_gcom_06:
    contains:
        "didac_bed_bed over_sweaty"
    contains:
        "didac_bed_d_body 04"
    contains:
        "didac_bed_d_blush 01"
    contains:
        "didac_bed_d_eyes 06"
    contains:
        "didac_bed_d_eyebrows normal"
    contains:
        "didac_bed_d_mouth sad_Silentx05"
    contains:
        "didac_bed_d_hair 04"
    contains:
        "didac_bed_headtowel wet"
    contains:
        "didac_bed_d_blanket 02"
    contains:
        "didac_bed_MC_handonfront"

image didac_bed_gcom_07:
    contains:
        "didac_bed_bed empty_cleansweaty"

image didac_bed_gcom_08:
    contains:
        "didac_bed_bed empty_clean"



## 
## DIDAC AT DOOR.

image afternoon02_beforeshower_didac_gcom:
    contains:
        "afternoon02_beforeshower_didac_body"
    contains:
        "afternoon02_beforeshower_blush 03"
    contains:
        "afternoon02_beforeshower_eyes front01"
    contains:
        "afternoon02_beforeshower_eyebrows sad"
    contains:
        "afternoon02_beforeshower_mouth sad_Silent"
    contains:
        "afternoon02_beforeshower_didac_hair"

image afternoon02_bg_showering_back_gcom:
    contains:
        "afternoon02_bg_showering_back"
    contains:
        "afternoon02_bg_showering_back_hand"

image d_showerin_gcom:

    contains:
        "d_showerin_bg"
        truecenter
    contains:
        "d_showerin_body"
        truecenter
    contains:
        "d_showerin_doors"
        truecenter

## 
## HOSPITAL

image afternoon02_bg_hospital_corridor_gcom:

    contains:
        truecenter
        "afternoon02_bg HospitalCorridor"
    contains:
        truecenter
        xpos 0.25
        "afternoon_nurse Pointing"

## PEDRERA NEUS

image night03_n_pedrera_hall_gcom_01:

    contains:
        "night03_bg street_pedrera_hall01"

    contains:
        "night03_n_pedrera_hall_back_body 01"
        truecenter

## CIUTADELLA

image bg_an04_park_entrance_far_gcom_01:

    contains:
        "bg an04_park_entrance_far_background_02"

    contains:
        "an04_park_entrance_far_foreground 01"

image bg_an04_park_entrance_far_gcom_02:

    contains:
        "bg an04_park_entrance_far_background_01"

    contains:
        "an04_park_entrance_far_foreground 02"

image bg_an04_entranceciutadella_fence_gcom_01:

    contains:
        "bg an04_entranceciutadella_fence_02"

    contains:
        "an04_entranceciutadella_foreground 01"

image bg_an04_entranceciutadella_fence_gcom_02:

    contains:
        "bg an04_entranceciutadella_fence_01"

    contains:
        "an04_entranceciutadella_foreground 02"
        ease 1 xpos -2.0

#### PARK path

image bg_an04_park_path_01_gcom:

    contains:
        "bg an04_park_path01_blur"
        truecenter
    contains:
        "bg_an04_park_path01_bush a"
        truecenter
        zoom 1.0 xpos 0.0 ypos 0.5

image bg_an04_park_path_02_gcom:

    contains:
        "bg an04_park_path01"
        truecenter
    contains:
        "bg_an04_park_path01_bush b"
        truecenter
        zoom 1.0 xpos 0.0 ypos 0.5
        ease 5.0 zoom 1.5 xpos 0.2 ypos 0.5 alpha 0.5
########


# Park bank very far:

image bg_an04_park_bank_veryfar_01_gcom:
    contains:
        "bg an04_park_bank_veryfar_background_02"
        zoom 0.5
    contains:
        "an04_park_bank_veryfar_foreground 02"
        zoom 0.5
    contains:
        "an04_park_bank_veryfar_plants 01"
        xanchor 0.0 yanchor -0.25 zoom 0.5


image bg_an04_park_bank_veryfar_02_gcom:
    contains:
        "bg an04_park_bank_veryfar_background_01"
        zoom 0.5
    contains:
        "an04_park_bank_veryfar_foreground 01"
        zoom 0.5
    contains:
        "an04_park_bank_veryfar_plants 02"
        xanchor 0.0 yanchor -0.25 zoom 0.5


image bg_an04_park_bank_far_01_gcom:
    contains:
        "bg an04_park_bank_far_background_composition 01"
        xanchor 0.0 yanchor 0.3 zoom 0.5

# label das:

#     scene bg an04_park_bank_far_background_composition 01:
#         xanchor 0.0 yanchor 0.3 zoom 0.5

# # bank bg
#     show an04_park_bank_bg_bank 01:
#         xanchor -1.135 yanchor -0.75 zoom 0.4

#     show an04_park_bank_bg_bank_cum empty:
#         xanchor -1.135 yanchor -0.75 zoom 0.4

# # smoke
#     show cigarette_smoke_pimp_anim 01: #PIMP
#         xanchor -2.0 yanchor -1.4 zoom 0.2 alpha 0.5

#     show cigarette_smoke_pot_anim 01: #POTHEAD
#         xanchor -2.745 yanchor -1.4 zoom 0.2 alpha 0.5

#     show cigarette_smoke_sqt_anim 01: #SQUITTER
#         xanchor -3.8 yanchor -1.78 zoom 0.2 alpha 0.5

# # pimp

#     show an04_park_bank_pimp_01_body:
#         xanchor -4.475 yanchor -1.155 zoom 0.4
#     show an04_park_bank_pimp_01_arm_L bottle:
#         xanchor -4.475 yanchor -1.155 zoom 0.4
#     show an04_park_bank_pimp_01_head right:
#         xanchor -4.475 yanchor -1.155 zoom 0.4

# # pothead

#     show an04_park_bank_pothead_01_body:
#         xanchor -5.455 yanchor -1.16 zoom 0.4
#     show an04_park_bank_pothead_01_head right:
#         xanchor -5.455 yanchor -1.16 zoom 0.4

# # squitter
#     show an04_park_bank_squitter_01_legs_shadow:
#         xanchor -3.382 yanchor -1.455 zoom 0.4
#     show an04_park_bank_squitter_01_body Drinking:
#         xanchor -3.382 yanchor -1.455 zoom 0.4
#     show an04_park_bank_squitter_01_legs:
#         xanchor -3.382 yanchor -1.455 zoom 0.4


# # didac
#     show an04_park_bank_didac_01_head right:
#         xanchor -1.5085 yanchor -0.76 zoom 0.4
#     show an04_park_bank_didac_01_body gabardine:
#         xanchor -1.5085 yanchor -0.76 zoom 0.4

#     show an04_park_bank_far_bush 02 zorder 99:
#         xanchor 0.0 yanchor 0.0 zoom 0.5
#     with Dissolve (2.0)


########################################
########################################################
########################################

image night04_pedrera_blowjob_gcom_01:

    contains:
        "bg dark_a"
    contains:
        "night04_pedrera_blowjob 001"

image night04_pedrera_blowjob_gcom_02:

    contains:
        "bg dark_a"
    contains:
        "night04_pedrera_blowjob 002"

image night04_pedrera_blowjob_gcom_03:

    contains:
        "bg dark_a"
    contains:
        "night04_pedrera_blowjob 003"

image night04_pedrera_blowjob_gcom_05:

    contains:
        "bg dark_a"
    contains:
        "night04_pedrera_blowjob 005"

image night04_pedrera_blowjob_gcom_07:

    contains:
        "bg dark_a"
    contains:
        "night04_pedrera_blowjob 007"


## DAY 02

image day02schoolTxell_gcom:

    contains:
        "morning02_bg schoolwall"
    contains:
        "m_bodynew relax_02"
        mtxell_body_ontheright_position
    contains:
        "m_exp_blush 02"
        mtxell_exp_ontheright_position
    contains:
        "m_exp_blush 02"
        mtxell_exp_ontheright_position
    contains:
        "m_exp_mouth happy_Silentx05"
        mtxell_exp_ontheright_position
    contains:
        "m_exp_eyes 03"
        mtxell_exp_ontheright_position
    contains:
        "m_exp_piris front03_red"
        mtxell_exp_ontheright_position
    contains:
        "m_exp_eyebrows normal"
        mtxell_exp_ontheright_position
    contains:
        "m_exp_hair_front"
        mtxell_exp_ontheright_position

image day03schoolTxell_gcom:

    contains:
        "morning02_bg schoolwall"
    contains:
        "m_bodynew relax_03"
        mtxell_body_ontheright_position
    contains:
        "m_exp_blush 02"
        mtxell_exp_ontheright_position
    contains:
        "m_exp_blush 02"
        mtxell_exp_ontheright_position
    contains:
        "m_exp_mouth happy_Silentx05"
        mtxell_exp_ontheright_position
    contains:
        "m_exp_eyes 03"
        mtxell_exp_ontheright_position
    contains:
        "m_exp_piris front03_red"
        mtxell_exp_ontheright_position
    contains:
        "m_exp_eyebrows normal"
        mtxell_exp_ontheright_position
    contains:
        "m_exp_hair_front"
        mtxell_exp_ontheright_position

image day02schoolNeusAngry_gcom:

    contains:
        "morning02_bg schoolwall"
    contains:
        "neus_body_full day02"
        neus_body_atright_position
    contains:
        "neus_head"
        neus_body_atright_position
    contains:
        "neus_exp_blush 01"
        neus_exp_atright_position
    contains:
        "neus_exp_eyebrows angryx02"
        neus_exp_atright_position
    contains:
        "neus_exp_eyes 04"
        neus_exp_atright_position
    contains:
        "neus_exp_iris left04"
        neus_exp_atright_position
    contains:
        "neus_exp_mouth sad_Silentx05"
        neus_exp_atright_position
    contains:
        "neus_exp_tears empty"
        neus_exp_atright_position
    contains:
        "neus_exp_glasses"
        neus_exp_atright_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atright_position

image day02schoolNeusHappy_gcom:

    contains:
        "morning02_bg schoolwall"
    contains:
        "neus_body_full day02"
        neus_body_atright_position
    contains:
        "neus_head"
        neus_body_atright_position
    contains:
        "neus_exp_blush 01"
        neus_exp_atright_position
    contains:
        "neus_exp_eyebrows sadx02"
        neus_exp_atright_position
    contains:
        "neus_exp_eyes 04"
        neus_exp_atright_position
    contains:
        "neus_exp_iris front04"
        neus_exp_atright_position
    contains:
        "neus_exp_mouth happy_Silentx05"
        neus_exp_atright_position
    contains:
        "neus_exp_tears empty"
        neus_exp_atright_position
    contains:
        "neus_exp_glasses"
        neus_exp_atright_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atright_position

image day03schoolNeusHappy_gcom:

    contains:
        "morning02_bg schoolwall"
    contains:
        "neus_body_full day03"
        neus_body_atright_position
    contains:
        "neus_head"
        neus_body_atright_position
    contains:
        "neus_exp_blush 01"
        neus_exp_atright_position
    contains:
        "neus_exp_eyebrows sadx02"
        neus_exp_atright_position
    contains:
        "neus_exp_eyes 04"
        neus_exp_atright_position
    contains:
        "neus_exp_iris front04"
        neus_exp_atright_position
    contains:
        "neus_exp_mouth happy_Silentx05"
        neus_exp_atright_position
    contains:
        "neus_exp_tears empty"
        neus_exp_atright_position
    contains:
        "neus_exp_glasses"
        neus_exp_atright_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atright_position

#d_showerin_compilation02

image d_showerin_compilation02_gcom:

    contains:
        "d_showerin_bg"
        d_showerin_base_pos

    contains:
        "d_showerin_body"
        d_showerin_base_pos

    contains:
        "d_showerin_blush 02"
        d_showerin_expressions_pos

    contains:
        "d_showerin_mouth sad_Silent"
        d_showerin_expressions_pos

    contains:
        "d_showerin_eyes 03"
        d_showerin_expressions_pos

    contains:
        "d_showerin_pupils right03"
        d_showerin_expressions_pos

    contains:
        "d_showerin_eyebrows sad"
        d_showerin_expressions_pos

    contains:
        "d_showerin_hair"
        d_showerin_expressions_pos

    # contains:
    #     "afternoon02_bg_showering_water"
    #     afternoon02_bg_showering_water_move

    # contains:
    #     "night05_Cemetery_smoke_comp"

    #contains:
        #"fog_01"
        ##additive 1.0
        #afternoon02_bg_showering_smoke_move

    contains:
        "d_showerin_doors"
        d_showerin_base_pos


## You grabbing Neus against the WALL.

image N_Against_grabbed_tensed_shadow_gcom:
    contains:
        "N_Against_bg"
    contains:
        "N_Against_N_body tensed_shadow"
    contains:
        "N_Against_N_blush 01"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_eyes 01"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_pupils front_01"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_eyebrows surprise"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_glasses"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_mouth sad_Talking"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_hair_front"
        N_Against_N_expressions_position
    contains:
        "N_Against_P_Arm"
    contains:
        "N_Against_P_Body"

image N_Against_grabbedHarder_tensed_shadow_gcom:
    contains:
        "N_Against_bg"
    contains:
        "N_Against_N_body tensed_shadow"
    contains:
        "N_Against_N_blush 03"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_eyes 01"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_pupils front_01"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_eyebrows surprise"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_glasses"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_mouth sadbitingx03_Silent"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_hair_front"
        N_Against_N_expressions_position
    contains:
        "N_Against_P_Arm"
    contains:
        "N_Against_P_Body"

image N_Against_free_tensed_shadow_gcom:
    contains:
        "N_Against_bg"
    contains:
        "N_Against_N_body tensed_shadow"
    contains:
        "N_Against_N_blush 01"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_eyes 03"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_pupils front_03"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_eyebrows angry"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_glasses"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_mouth happyx02_Silent"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_hair_front"
        N_Against_N_expressions_position
    contains:
        "N_Against_P_Arm notTensed"
    contains:
        "N_Against_P_Body"



image N_Against_tensed_gcom:
    contains:
        "N_Against_bg"
    contains:
        "N_Against_N_body tensed"
    contains:
        "N_Against_N_blush 01"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_eyes 03"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_pupils front_03"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_eyebrows angry"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_glasses"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_mouth happyx03_Silent"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_hair_front"
        N_Against_N_expressions_position

image N_Against_relaxed_gcom:
    contains:
        "N_Against_bg"
    contains:
        "N_Against_N_body relaxed"
    contains:
        "N_Against_N_blush 01"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_eyes 03"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_pupils front_03"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_eyebrows surprise"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_glasses"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_mouth happyx02_Silent"
        N_Against_N_expressions_position
    contains:
        "N_Against_N_hair_front"
        N_Against_N_expressions_position


# day03 Neus Bar:

image night03_bar_general_gcom:

    contains:
        "night03_bg bar_general"
    contains:
        "neus_body ld_default"
        neus_body_atright_position
    contains:
        "neus_head"
        neus_body_atright_position
    contains:
        "neus_arms ld_rest"
        neus_body_atright_position
    contains:
        "neus_exp_blush 01"
        neus_exp_atright_position
    contains:
        "neus_exp_mouth happy_Silentx04"
        neus_exp_atright_position
    contains:
        "neus_exp_eyes 02"
        neus_exp_atright_position
    contains:
        "neus_exp_iris front02"
        neus_exp_atright_position
    contains:
        "neus_exp_eyebrows normal"
        neus_exp_atright_position
    contains:
        "neus_exp_glasses"
        neus_exp_atright_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atright_position

image night03_bar_barra_01_gcom:
    contains:
        "night03_bg bar_barra"
    # contains:
    #     "night03_bar_barra_copas empty"
    #     night03_bar_barra_copas_expressions_pos
    contains:
        "night03_bar_barra_barman_body"
    contains:
        "night03_bar_barra_barman_eyes angry"
        night03_bar_barra_barman_expressions_pos
    contains:
        "night03_bar_barra_barman_pupils angry_front"
        night03_bar_barra_barman_expressions_pos
    contains:
        "night03_bar_barra_barman_mouth sad_Silent"
        night03_bar_barra_barman_expressions_pos
    contains:
        "night03_bar_barra_n_body_ld"
    contains:
        "night03_bar_barra_n_eyes 01"
        night03_bar_barra_n_expressions_pos
    contains:
        "night03_bar_barra_n_pupils front01"
        night03_bar_barra_n_expressions_pos
    contains:
        "night03_bar_barra_n_eyebrows surprisex02"
        night03_bar_barra_n_expressions_pos
    contains:
        "night03_bar_barra_n_glasses"
        night03_bar_barra_n_expressions_pos
    contains:
        "night03_bar_barra_n_mouth happy_Silentx03"
        night03_bar_barra_n_expressions_pos
    contains:
        "night03_bar_barra_n_hair_front"
        night03_bar_barra_n_expressions_pos

image night03_bar_barra_NeusAngry_gcom: # She's angry with you
    contains:
        "night03_bg bar_barra"
    # contains:
    #     "night03_bar_barra_copas empty"
    #     night03_bar_barra_copas_expressions_pos
    contains:
        "night03_bar_barra_barman_body"
    contains:
        "night03_bar_barra_barman_eyes surprise"
        night03_bar_barra_barman_expressions_pos
    contains:
        "night03_bar_barra_barman_pupils surprise_left"
        night03_bar_barra_barman_expressions_pos
    contains:
        "night03_bar_barra_barman_mouth happy_Silent"
        night03_bar_barra_barman_expressions_pos
    contains:
        "night03_bar_barra_n_body_ld"
    contains:
        "night03_bar_barra_n_eyes 01"
        night03_bar_barra_n_expressions_pos
    contains:
        "night03_bar_barra_n_pupils front01"
        night03_bar_barra_n_expressions_pos
    contains:
        "night03_bar_barra_n_eyebrows angryx04"
        night03_bar_barra_n_expressions_pos
    contains:
        "night03_bar_barra_n_glasses"
        night03_bar_barra_n_expressions_pos
    contains:
        "night03_bar_barra_n_mouth sad_Silentx03"
        night03_bar_barra_n_expressions_pos
    contains:
        "night03_bar_barra_n_hair_front"
        night03_bar_barra_n_expressions_pos

image night03_bar_barra_BarmanAngry_gcom: # She's angry with you
    contains:
        "night03_bg bar_barra"
    contains:
        "night03_bar_barra_copas copas"
        night03_bar_barra_copas_expressions_pos
    contains:
        "night03_bar_barra_barman_body"
    contains:
        "night03_bar_barra_barman_eyes angry"
        night03_bar_barra_barman_expressions_pos
    contains:
        "night03_bar_barra_barman_pupils angry_front"
        night03_bar_barra_barman_expressions_pos
    contains:
        "night03_bar_barra_barman_mouth sad_Silent"
        night03_bar_barra_barman_expressions_pos
    contains:
        "night03_bar_barra_n_body_ld"
    contains:
        "night03_bar_barra_n_eyes 01"
        night03_bar_barra_n_expressions_pos
    contains:
        "night03_bar_barra_n_pupils right01"
        night03_bar_barra_n_expressions_pos
    contains:
        "night03_bar_barra_n_eyebrows angryx03"
        night03_bar_barra_n_expressions_pos
    contains:
        "night03_bar_barra_n_glasses"
        night03_bar_barra_n_expressions_pos
    contains:
        "night03_bar_barra_n_mouth sad_Silentx03"
        night03_bar_barra_n_expressions_pos
    contains:
        "night03_bar_barra_n_hair_front"
        night03_bar_barra_n_expressions_pos

image night03_bar_barra_BarmanAngryAlone_gcom: # She's angry with you
    contains:
        "night03_bg bar_barra"
    contains:
        "night03_bar_barra_barman_body"
    contains:
        "night03_bar_barra_barman_eyes angry"
        night03_bar_barra_barman_expressions_pos
    contains:
        "night03_bar_barra_barman_pupils angry_front"
        night03_bar_barra_barman_expressions_pos
    contains:
        "night03_bar_barra_barman_mouth sad_Silent"
        night03_bar_barra_barman_expressions_pos

# 03night neus Sitting

image night03_bar_backstage_01_gcom:
    contains:
        "night03_bg bar_backstage"
    contains:
        "n_s_b_ld_body"
        night03_bar_drinking_body_pos
    contains:
        "n_s_b_ld_hair_pigtails"
        night03_bar_drinking_body_pos
    contains:
        "n_s_exp_blush 02"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_eyes 02"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_iris front02"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_tears empty"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_eyebrows normal"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_glasses"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_mouth happy_Silentx04"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_b_ld_hairfront"
        night03_bar_drinking_body_pos
    contains:
        "n_s_b_ld_arm rest"
        night03_bar_drinking_body_pos
    contains:
        "night03_bar_drinking_coaster"
        zoom 0.5
    contains:
        "night03_bar_drinking_glass full"
        zoom 0.5
    contains:
        "night03_bar_drinking_straw"
        zoom 0.5

image night03_bar_backstage_drinking_gcom:
    contains:
        "night03_bg bar_backstage"
    contains:
        "n_s_b_ld_body"
        night03_bar_drinking_body_pos
    contains:
        "n_s_b_ld_hair_pigtails"
        night03_bar_drinking_body_pos
    contains:
        "n_s_exp_blush 02"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_eyes 04"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_iris down04"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_tears empty"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_eyebrows surprisex02"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_glasses"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_mouth happy_Silentx04"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_b_ld_hairfront"
        night03_bar_drinking_body_pos
    contains:
        "n_s_b_ld_arm glass"
        night03_bar_drinking_body_pos
    contains:
        "night03_bar_drinking_coaster"
        zoom 0.5
    contains:
        "night03_bar_drinking_glass empty"
        zoom 0.5
    contains:
        "night03_bar_drinking_straw"
        zoom 0.5

image night03_bar_backstage_drunk_gcom:
    contains:
        "night03_bg bar_backstage"
    contains:
        "n_s_b_ld_body"
        night03_bar_drinking_body_pos
    contains:
        "n_s_b_ld_hair_pigtails"
        night03_bar_drinking_body_pos
    contains:
        "n_s_exp_blush 05"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_eyes 04"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_iris front04"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_tears empty"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_eyebrows normal"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_glasses"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_exp_mouth happy_Silentx02"
        night03_bar_drinking_expressions_pos
    contains:
        "n_s_b_ld_hairfront"
        night03_bar_drinking_body_pos
    contains:
        "n_s_b_ld_arm rest"
        night03_bar_drinking_body_pos
    contains:
        "night03_bar_drinking_coaster"
        zoom 0.5
    contains:
        "night03_bar_drinking_glass empty_alot"
        zoom 0.5


image night03_pedreraFar_gcom:
    contains:
        "night03_bg street_pedrera_far"
    contains:
        "neus_body ld_default"
        neus_body_atright_position
    contains:
        "neus_head"
        neus_body_atright_position
    contains:
        "neus_arms ld_rest"
        neus_body_atright_position
    contains:
        "neus_exp_blush 05"
        neus_exp_atright_position
    contains:
        "neus_exp_mouth happy_Silentx03"
        neus_exp_atright_position
    contains:
        "neus_exp_eyes 03"
        neus_exp_atright_position
    contains:
        "neus_exp_iris front03"
        neus_exp_atright_position
    contains:
        "neus_exp_eyebrows normal"
        neus_exp_atright_position
    contains:
        "neus_exp_glasses"
        neus_exp_atright_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atright_position

image night03_pedreraClose_Empty_gcom:
    contains:
        "night03_bg street_pedrera_close"
    contains:
        "neus_body ld_default"
        neus_body_atright_position
    contains:
        "neus_head"
        neus_body_atright_position
    contains:
        "neus_arms ld_rest"
        neus_body_atright_position
    contains:
        "neus_exp_blush 05"
        neus_exp_atright_position
    contains:
        "neus_exp_mouth happy_Silentx04"
        neus_exp_atright_position
    contains:
        "neus_exp_eyes 04"
        neus_exp_atright_position
    contains:
        "neus_exp_iris left04"
        neus_exp_atright_position
    contains:
        "neus_exp_eyebrows normal"
        neus_exp_atright_position
    contains:
        "neus_exp_glasses"
        neus_exp_atright_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atright_position


image night03_pedreraClose_bagLooking_gcom:
    contains:
        "night03_bg street_pedrera_close"
    contains:
        "neus_body ld_default"
        neus_body_atright_position
    contains:
        "neus_head"
        neus_body_atright_position
    contains:
        "neus_arms ld_purse_opened"
        neus_body_atright_position
    contains:
        "neus_exp_blush 05"
        neus_exp_atright_position
    contains:
        "neus_exp_mouth happy_Silentx04"
        neus_exp_atright_position
    contains:
        "neus_exp_eyes 03"
        neus_exp_atright_position
    contains:
        "neus_exp_iris down03"
        neus_exp_atright_position
    contains:
        "neus_exp_eyebrows normal"
        neus_exp_atright_position
    contains:
        "neus_exp_glasses"
        neus_exp_atright_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atright_position

image night03_pedreraClose_bagCondoms_gcom:
    contains:
        "night03_bg street_pedrera_close"
    contains:
        "neus_body ld_default"
        neus_body_atright_position
    contains:
        "neus_head"
        neus_body_atright_position
    contains:
        "neus_arms ld_condoms"
        neus_body_atright_position
    contains:
        "neus_exp_blush 05"
        neus_exp_atright_position
    contains:
        "neus_exp_mouth happy_Silentx06"
        neus_exp_atright_position
    contains:
        "neus_exp_eyes 04"
        neus_exp_atright_position
    contains:
        "neus_exp_iris front04"
        neus_exp_atright_position
    contains:
        "neus_exp_eyebrows surprisex01"
        neus_exp_atright_position
    contains:
        "neus_exp_glasses"
        neus_exp_atright_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atright_position

image night03_pedreraClose_bagKeys_gcom:
    contains:
        "night03_bg street_pedrera_close"
    contains:
        "neus_body ld_default"
        neus_body_atright_position
    contains:
        "neus_head"
        neus_body_atright_position
    contains:
        "neus_arms ld_keys"
        neus_body_atright_position
    contains:
        "neus_exp_blush 05"
        neus_exp_atright_position
    contains:
        "neus_exp_mouth happy_Silentx04"
        neus_exp_atright_position
    contains:
        "neus_exp_eyes 04"
        neus_exp_atright_position
    contains:
        "neus_exp_iris left04"
        neus_exp_atright_position
    contains:
        "neus_exp_eyebrows surprisex01"
        neus_exp_atright_position
    contains:
        "neus_exp_glasses"
        neus_exp_atright_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atright_position

# At Door:

image night03_pedreraDoor_testingKeys_gcom:
    contains:
        "night03_bg street_pedrera_door"
    contains:
        "neus_body ld_default"
        neus_body_atright_position
    contains:
        "neus_head"
        neus_body_atright_position
    contains:
        "neus_arms ld_keystry"
        neus_body_atright_position
    contains:
        "neus_exp_blush 05"
        neus_exp_atright_position
    contains:
        "neus_exp_mouth sad_Silentx03"
        neus_exp_atright_position
    contains:
        "neus_exp_eyes 04"
        neus_exp_atright_position
    contains:
        "neus_exp_iris left04"
        neus_exp_atright_position
    contains:
        "neus_exp_eyebrows angryx01"
        neus_exp_atright_position
    contains:
        "neus_exp_glasses"
        neus_exp_atright_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atright_position

image night03_pedreraDoor_watchingKeys_gcom:
    contains:
        "night03_bg street_pedrera_door"
    contains:
        "neus_body ld_default"
        neus_body_atright_position
    contains:
        "neus_head"
        neus_body_atright_position
    contains:
        "neus_arms ld_keys"
        neus_body_atright_position
    contains:
        "neus_exp_blush 05"
        neus_exp_atright_position
    contains:
        "neus_exp_mouth sad_Silentx03"
        neus_exp_atright_position
    contains:
        "neus_exp_eyes 04"
        neus_exp_atright_position
    contains:
        "neus_exp_iris down04"
        neus_exp_atright_position
    contains:
        "neus_exp_eyebrows angryx01"
        neus_exp_atright_position
    contains:
        "neus_exp_glasses"
        neus_exp_atright_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atright_position

image night03_pedreraDoor_keysIn_gcom:
    contains:
        "night03_bg street_pedrera_door"
    contains:
        "neus_body ld_default"
        neus_body_atright_position
    contains:
        "neus_head"
        neus_body_atright_position
    contains:
        "neus_arms ld_keysinsert"
        neus_body_atright_position
    contains:
        "neus_exp_blush 05"
        neus_exp_atright_position
    contains:
        "neus_exp_mouth happy_Silentx04"
        neus_exp_atright_position
    contains:
        "neus_exp_eyes 01"
        neus_exp_atright_position
    contains:
        "neus_exp_iris left01"
        neus_exp_atright_position
    contains:
        "neus_exp_eyebrows surprisex01"
        neus_exp_atright_position
    contains:
        "neus_exp_glasses"
        neus_exp_atright_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atright_position

image night03_pedreraDoor_doorOpen_gcom:
    contains:
        "night03_bg street_pedrera_door_opened"
    contains:
        "neus_body ld_default"
        neus_body_atright_position
    contains:
        "neus_head"
        neus_body_atright_position
    contains:
        "neus_arms ld_keys"
        neus_body_atright_position
    contains:
        "neus_exp_blush 05"
        neus_exp_atright_position
    contains:
        "neus_exp_mouth happy_Silentx05"
        neus_exp_atright_position
    contains:
        "neus_exp_eyes 04"
        neus_exp_atright_position
    contains:
        "neus_exp_iris front04"
        neus_exp_atright_position
    contains:
        "neus_exp_eyebrows surprisex01"
        neus_exp_atright_position
    contains:
        "neus_exp_glasses"
        neus_exp_atright_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atright_position

image night03_pedreraEntranceDark_gcom:
    contains:
        "night03_bg street_pedrera_entrance"
    contains:
        "neus_body ld_default"
        neus_body_atright_position
    contains:
        "neus_head"
        neus_body_atright_position
    contains:
        "neus_arms ld_rest"
        neus_body_atright_position
    contains:
        "neus_exp_blush 05"
        neus_exp_atright_position
    contains:
        "neus_exp_mouth happy_Silentx05"
        neus_exp_atright_position
    contains:
        "neus_exp_eyes 04"
        neus_exp_atright_position
    contains:
        "neus_exp_iris front04"
        neus_exp_atright_position
    contains:
        "neus_exp_eyebrows normal"
        neus_exp_atright_position
    contains:
        "neus_exp_glasses"
        neus_exp_atright_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atright_position

image night03_pedreraElevator_gcom:
    contains:
        "night03_bg street_pedrera_elevator"
    contains:
        "neus_body ld_default"
        neus_body_atright_position
    contains:
        "neus_head"
        neus_body_atright_position
    contains:
        "neus_arms ld_rest"
        neus_body_atright_position
    contains:
        "neus_exp_blush 05"
        neus_exp_atright_position
    contains:
        "neus_exp_mouth happy_Silentx04"
        neus_exp_atright_position
    contains:
        "neus_exp_eyes 03"
        neus_exp_atright_position
    contains:
        "neus_exp_iris left03"
        neus_exp_atright_position
    contains:
        "neus_exp_eyebrows surprisex01"
        neus_exp_atright_position
    contains:
        "neus_exp_glasses"
        neus_exp_atright_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atright_position

### In apartament

image night03_pedreraHall_back_gcom:
    contains:
        "night03_bg street_pedrera_hall01"
    contains:
        "night03_n_pedrera_hall_back_body 01"
        xpos 0.4
    contains:
        "night03_n_pedrera_hall_back_head 01"
        xpos 0.4

image night03_pedreraHall_down_gcom:
    contains:
        "night03_bg street_pedrera_hall01"
    contains:
        "night03_n_pedrera_hall_back_body 01"
        xpos 0.4
    contains:
        "night03_n_pedrera_hall_back_head 03"
        xpos 0.4

image night03_pedreraHall_downDark_gcom:
    contains:
        "night03_bg street_pedrera_hall02"
    contains:
        "night03_n_pedrera_hall_back_body 02"
        xpos 0.4
    contains:
        "night03_n_pedrera_hall_back_head 04"
        xpos 0.4

image night03_pedreraHall_upDark_gcom:
    contains:
        "night03_bg street_pedrera_hall02"
    contains:
        "night03_n_pedrera_hall_back_body 02"
        xpos 0.4
    contains:
        "night03_n_pedrera_hall_back_head 02"
        xpos 0.4

image night03_pedreraHall_titsShowing_gcom:
    contains:
        "night03_bg street_pedrera_hall03"
    contains:
        "neus_body_full ld_boobs"
        neus_body_atcenter_position
    contains:
        "neus_head"
        neus_body_atcenter_position
    contains:
        "neus_arms empty"
        neus_body_atcenter_position
    contains:
        "neus_exp_blush 05"
        neus_exp_atcenter_position
    contains:
        "neus_exp_mouth sad_Silentx03"
        neus_exp_atcenter_position
    contains:
        "neus_exp_eyes 04"
        neus_exp_atcenter_position
    contains:
        "neus_exp_iris left04"
        neus_exp_atcenter_position
    contains:
        "neus_exp_eyebrows sadx01"
        neus_exp_atcenter_position
    contains:
        "neus_exp_glasses"
        neus_exp_atcenter_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atcenter_position

image night03_pedreraHall_titsCovered_gcom:
    contains:
        "night03_bg street_pedrera_hall03"
    contains:
        "neus_body_full ld_covered"
        neus_body_atcenter_position
    contains:
        "neus_head"
        neus_body_atcenter_position
    contains:
        "neus_arms empty"
        neus_body_atcenter_position
    contains:
        "neus_exp_blush 05"
        neus_exp_atcenter_position
    contains:
        "neus_exp_mouth sad_Silentx03"
        neus_exp_atcenter_position
    contains:
        "neus_exp_eyes 04"
        neus_exp_atcenter_position
    contains:
        "neus_exp_iris left04"
        neus_exp_atcenter_position
    contains:
        "neus_exp_tears 04_02"
        neus_exp_atcenter_position
    contains:
        "neus_exp_eyebrows sadx02"
        neus_exp_atcenter_position
    contains:
        "neus_exp_glasses"
        neus_exp_atcenter_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atcenter_position


image night03_pedreraHall_titsCoveredClose_gcom:
    contains:
        "night03_bg street_pedrera_hall03"
    contains:
        "neus_body_full ld_covered"
        neus_body_atcenter_position
    contains:
        "neus_head"
        neus_body_atcenter_position
    contains:
        "neus_arms empty"
        neus_body_atcenter_position
    contains:
        "neus_exp_blush 05"
        neus_exp_atcenter_position
    contains:
        "neus_exp_mouth sad_Silentx02"
        neus_exp_atcenter_position
    contains:
        "neus_exp_eyes 01"
        neus_exp_atcenter_position
    contains:
        "neus_exp_iris front01"
        neus_exp_atcenter_position
    contains:
        "neus_exp_tears 01_05"
        neus_exp_atcenter_position
    contains:
        "neus_exp_eyebrows sadx01"
        neus_exp_atcenter_position
    contains:
        "neus_exp_glasses"
        neus_exp_atcenter_position
    contains:
        "neus_exp_hairfront"
        neus_exp_atcenter_position

# Kissing moment.

image night03_pedreraHall_kissing_before_gcom:
    contains:
        "bg dark_a"
    contains:
        "n_closefromup_body ld"
        truecenter
        zoom 0.5
    contains:
        "n_closefromup_blush 05"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_blush 05"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_eyes 02"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_iris front02"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_mouth sad_Talkingx04"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_eyebrows surprisex01"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_tears 01_05"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_glasses"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_prothand empty"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_hair_front"
        truecenter
        zoom 0.5

image night03_pedreraHall_kissing_beforeHand_gcom:
    contains:
        "bg dark_a"
    contains:
        "n_closefromup_body ld"
        truecenter
        zoom 0.5
    contains:
        "n_closefromup_blush 05"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_blush 05"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_eyes 01"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_iris right01"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_mouth sad_Talkingx04"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_eyebrows surprisex01"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_tears 01_05"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_glasses"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_prothand"
        zoom 0.5 xalign 0.5 yalign 0.5
    contains:
        "n_closefromup_hair_front"
        truecenter
        zoom 0.5

image general_handkissNeus_gcom:
    contains:
        "kissn_n_bg"
    contains:
        "handkiss_n_hand 01"
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
    contains:
        "handkiss_mclips"
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5

## Grabbing Tits



# Vomit Moment

image night03_pedreraHall_kissing_vomitMoment_gcom:

    contains:
        "bg dark_a"
    contains:
        "n_closefromup_body ld"
        kissn_n_surprise
    contains:
        "n_closefromup_blush 06"
        kissn_n_surprise
    contains:
        "n_closefromup_eyes 00"
        kissn_n_surprise
    contains:
        "n_closefromup_iris front00"
        kissn_n_surprise
    contains:
        "n_closefromup_eyebrows sadx05"
        kissn_n_surprise
    contains:
        "n_closefromup_tears 00_00"
    contains:
        "n_closefromup_mouth extra_tongueOut"
        kissn_n_surprise
    contains:
        "n_closefromup_glasses"
        kissn_n_surprise
    contains:
        "n_closefromup_hair_front"
        kissn_n_surprise
    # contains:
    #     "n_closefromup_prothand empty"
    #     kissn_n_surprise
    # contains:
    #     "n_closefromup_prothandchin empty"
    #     kissn_n_surprise

image night03_pedreraHall_wc_vomiting_gcom:
    contains:
        "night03_n_pedrera_puking_bg"
    contains:
        "night03_n_pedrera_puking_body"
    contains:
        "night03_n_pedrera_puking_eyes 06"
    contains:
        "night03_n_pedrera_puking_pupils empty"
    contains:
        "night03_n_pedrera_puking_eyebrows angry"
    contains:
        "night03_n_pedrera_puking_glasses"
    contains:
        "night03_n_pedrera_puking_door open"

image night03_pedreraHall_wc_surprise_gcom:
    contains:
        "night03_n_pedrera_puking_bg"
    contains:
        "night03_n_pedrera_puking_body"
    contains:
        "night03_n_pedrera_puking_eyes 01"
    contains:
        "night03_n_pedrera_puking_pupils front"
    contains:
        "night03_n_pedrera_puking_eyebrows surprise"
    contains:
        "night03_n_pedrera_puking_glasses"
    contains:
        "night03_n_pedrera_puking_door open"


image night03_pedreraHall_wc_sad_gcom:
    contains:
        "night03_n_pedrera_puking_bg"
    contains:
        "night03_n_pedrera_puking_body"
    contains:
        "night03_n_pedrera_puking_eyes 01"
    contains:
        "night03_n_pedrera_puking_pupils down"
    contains:
        "night03_n_pedrera_puking_eyebrows sad"
    contains:
        "night03_n_pedrera_puking_glasses"
    contains:
        "night03_n_pedrera_puking_door open"


######################################### Night 03 At Home
# Finding Didac Naked after Shower

image night03_atHome_DidacNaked_surprise_gcom:
    contains:
        "afternight03_bg hallway_dooropen"
    contains:
        "didacfbodybelow naked"
        dfbody_center_little
    contains:
        "didacfbodybelow_naked_drops 01"
        dfbody_center_little
    contains:
        "didacfbodytop naked"
        dfbody_center_little
    contains:
        "didacfbodytop_naked_drops 01"
        dfbody_center_little
    contains:
        "didacfhandl hip_naked"
        dfbody_center_little
    contains:
        "didacfhandl_hip_naked_drops 01"
        dfbody_center_little
    contains:
        "didacf_blush 01"
        dexpressions_center_little
    contains:
        "didacf_eyes 00"
        dexpressions_center_little
    contains:
        "didacf_pupils front00"
        dexpressions_center_little
    contains:
        "didacf_eyebrows surprisex01"
        dexpressions_center_little
    contains:
        "didacfbodytop_hair wet_01"
        dfbody_center
    contains:
        "didacfhandr towel"
        dfbody_center_little
    contains:
        "didacf_mouth sad_Silentx03"
        dexpressions_center_little

image night03_atHome_DidacNaked_angry_gcom:
    contains:
        "afternight03_bg hallway_dooropen"
    contains:
        "didacfbodybelow naked"
        dfbody_center_little
    contains:
        "didacfbodybelow_naked_drops 01"
        dfbody_center_little
    contains:
        "didacfbodytop naked"
        dfbody_center_little
    contains:
        "didacfbodytop_naked_drops 01"
        dfbody_center_little
    contains:
        "didacfhandl hip_naked"
        dfbody_center_little
    contains:
        "didacfhandl_hip_naked_drops 01"
        dfbody_center_little
    contains:
        "didacf_blush 03"
        dexpressions_center_little
    contains:
        "didacf_eyes 03"
        dexpressions_center_little
    contains:
        "didacf_pupils front03"
        dexpressions_center_little
    contains:
        "didacf_eyebrows angryx03"
        dexpressions_center_little
    contains:
        "didacfbodytop_hair wet_01"
        dfbody_center
    contains:
        "didacfhandr towel"
        dfbody_center_little
    contains:
        "didacf_mouth sad_Talkingx09"
        dexpressions_center_little

image night03_atHome_DidacNaked_lookingDown_gcom:
    contains:
        "afternight03_bg hallway_dooropen"
    contains:
        "didacfbodybelow naked"
        dfbody_center_little
    contains:
        "didacfbodybelow_naked_drops 01"
        dfbody_center_little
    contains:
        "didacfbodytop naked"
        dfbody_center_little
    contains:
        "didacfbodytop_naked_drops 01"
        dfbody_center_little
    contains:
        "didacfhandl hip_naked"
        dfbody_center_little
    contains:
        "didacfhandl_hip_naked_drops 01"
        dfbody_center_little
    contains:
        "didacf_blush 04"
        dexpressions_center_little
    contains:
        "didacf_eyes 05"
        dexpressions_center_little
    contains:
        "didacf_pupils down05"
        dexpressions_center_little
    contains:
        "didacf_eyebrows sadx01"
        dexpressions_center_little
    contains:
        "didacfbodytop_hair wet_01"
        dfbody_center
    contains:
        "didacfhandr towel"
        dfbody_center_little
    contains:
        "didacf_mouth sadbiting_Silentx05"
        dexpressions_center_little

image night03_atHome_DidacBedResting_gcom:
    contains:
        "beds_night_lightOff_blindUp_DemptyMCempty"
    contains:
        "beds_D03b_night_lightOff_blindUp"

image night03_atHome_DidacBedTalking_gcom:
    contains:
        "afternight03_didac_bedroom_onbed_body"
    contains:
        "afternight03_didac_bedroom_onbed_eyebrows surprise"
    contains:
        "afternight03_didac_bedroom_onbed_eyes front02"
    contains:
        "afternight03_didac_bedroom_onbed_pupils front02"
    contains:
        "afternight03_didac_bedroom_onbed_mouth sad_Talking"
    contains:
        "afternight03_didac_bedroom_onbed_hair"
    contains:
        "light 01_moon"
        xanchor 0.25 yanchor 0.3 rotate -60 zoom 0.5 additive 1.0
        parallel:
            ease 10.0 rotate -62
            ease 10.0 rotate -58
            repeat
        parallel:
            ease 30.0 zoom 1.0
            ease 30.0 zoom 0.6
            repeat

image night03_atHome_DidacBedSilent_gcom:
    contains:
        "afternight03_didac_bedroom_onbed_body"
    contains:
        "afternight03_didac_bedroom_onbed_eyebrows angry"
    contains:
        "afternight03_didac_bedroom_onbed_eyes front02"
    contains:
        "afternight03_didac_bedroom_onbed_pupils front02"
    contains:
        "afternight03_didac_bedroom_onbed_mouth sad_Silent"
    contains:
        "afternight03_didac_bedroom_onbed_hair"
    contains:
        "light 01_moon"
        xanchor 0.25 yanchor 0.3 rotate -60 zoom 0.5 additive 1.0
        parallel:
            ease 10.0 rotate -62
            ease 10.0 rotate -58
            repeat
        parallel:
            ease 30.0 zoom 1.0
            ease 30.0 zoom 0.6
            repeat

image night03_atHome_DidacStand_Smile_gcom:
    contains:
        "beds_night_lightOff_blindUp_DemptyMCempty_blur02"
    contains:
        "didacfbodybelow naked"
        dfbody_center_little
    # contains:
    #     "didacfbodybelow_naked_drops 00"
    #     dfbody_center_little
    contains:
        "didacfbodytop naked"
        dfbody_center_little
    contains:
        "didacfbodytop_naked_drops 00"
        dfbody_center_little
    contains:
        "didacfhandl hip_naked"
        dfbody_center_little
    # contains:
    #     "didacfhandl_hip_naked_drops 00"
    #     dfbody_center_little
    contains:
        "didacf_blush 03"
        dexpressions_center_little
    contains:
        "didacf_eyes 04"
        dexpressions_center_little
    contains:
        "didacf_pupils down04"
        dexpressions_center_little
    contains:
        "didacf_eyebrows surprisex01"
        dexpressions_center_little
    contains:
        "didacfbodytop_hair"
        dfbody_center_little
    contains:
        "didacfhandr leg_naked"
        dfbody_center_little
    contains:
        "didacf_mouth happy_Silentx02"
        dexpressions_center_little



        

#############################################
##SCENES
############################################

#############################################        
##MUSIC
############################################


#############################################
##TRANSFORMATIONS
############################################

transform slowpan:
    xalign 0.5
    yalign 0.5
    zoom 1.0
    block:
        easein_quad 2.0 zoom 1.2
        easein_quad 2.0 zoom 1.0
        repeat

default g_zoomNumber = 0.2

transform g_zoomTrans_var:
    truecenter
    zoom g_zoomNumber


transform g_zoomTrans_1_2:
    truecenter
    zoom 1.2

transform g_zoomTrans_1_1:
    truecenter
    zoom 1.1

transform g_zoomTrans_1:
    truecenter
    zoom 1.0

transform g_zoomTrans_0_9:
    truecenter
    zoom 0.9

transform g_zoomTrans_0_8:
    truecenter
    zoom 0.8

transform g_zoomTrans_0_75:
    truecenter
    zoom 0.75

transform g_zoomTrans_0_7:
    truecenter
    zoom 0.7

transform g_zoomTrans_0_6:
    truecenter
    zoom 0.6

transform g_zoomTrans_0_55:
    truecenter
    zoom 0.55

transform g_zoomTrans_0_5:
    truecenter
    zoom 0.5

transform g_zoomTrans_0_4:
    truecenter
    zoom 0.4

transform g_zoomTrans_0_35:
    truecenter
    zoom 0.35

transform g_zoomTrans_0_3:
    truecenter
    zoom 0.3

transform g_zoomTrans_0_2:
    truecenter
    zoom 0.2

transform g_zoomTrans_0_15:
    truecenter
    zoom 0.15

transform g_zoomTrans_0_1:
    truecenter
    zoom 0.1

