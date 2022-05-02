
## GALLERY

### init python:
init python:

    gallery_image_objects = []
    # Step 1. Create the gallery object.
    g = Gallery()

                             ############################
                            ##############################
                           ##                            ##
                           ##   Gallery Day 1, 2 and 3   ##
                           ##                            ##
                            ##############################
                             ############################

    # Step 2. Add buttons and images to the gallery.

    # A button that contains an image that automatically unlocks.

    # This button has multiple images assocated with it. We use unlock_image
    # so we don't have to call both .image and .unlock. We also apply a
    # transform to the first image.


    g.button("gal_day01")
    g.thumbnail("images/gallery/gThumbs/gThumb_b_01.webp")
    
    # 01 Hand Grab
    g.unlock_image("afternoon01_Grabbed")
    # 02 Shhh
    g.image("images/gallery/images/day01/02_shhh.webp")
    g.unlock("afternoon01_Toilet_Didac_body")
    # Neus Being Grabbed byt Tis.
    g.image("afternoon01_Bathroom rapeA01_gallery")
    g.unlock("afternoon01_Bathroom rapeA01")
    # 03 NeusBeing Grabbed
    g.image("images/gallery/images/day01/04_grabbing.webp")
    g.unlock("afternoon01_Bathroom_rapeB_bodies")
    # 03 NeusBeing Grabbed Eyes
    g.image("images/gallery/images/day01/05_grabbingEyes.webp")
    g.unlock("afternoon01_Bathroom_rapeB_bodies")
    # Bite Hand
    g.image("afternoon01_Bathroom rapeBite_gallery")
    g.condition("persistent.unlock_rape_neus_hand")
    # Bite Dick
    g.image("afternoon01_Bathroom rapeB02_gallery")
    g.unlock("afternoon01_BathroomrapeB00")
    #g.condition("persistent.unlock_rape_neus_dick")
    g.image("afternoon01_Bathroom rapeB01_gallery")
    g.unlock("afternoon01_BathroomrapeB00")
    g.image("afternoon01_Bathroom rapeBbright_gallery")
    g.unlock("afternoon01_BathroomrapeB00")

    g.image("afternoon01_Bathroomm rapeBiteCock_gallery")
    g.condition("persistent.unlock_rape_neus_dick")
    # Neus Being Slapped
    g.image("afternoon01_Bathroom_rapeSlap_gallery")
    g.unlock("afternoon01_Bathroom_rapeSlap")
    #g.condition("persistent.unlock_rape_neus_out")
    # Didac being Punched
    g.image("afternoon01_Bathroom rapePunch_gallery")
    g.unlock("afternoon01_Bathroom rapePunch")
    # Neus Crying on Ground
    g.image("afternoon01_Bathroom_Rape_Crying_neus_gcom")
    g.unlock("afternoon01_Bathroom_Rape_Crying_neus_body 01")
    
    g.image("afternoon01_Bathroom_Rape_Crying_neus_arm_gcom")
    g.unlock("afternoon01_Bathroom_Rape_Crying_neus_body arm")

    g.image("images/gallery/images/day01/06_NeusDamaged.webp")
    g.unlock("neus_body_full afterrape")

    g.image("images/gallery/images/day01/07_DidacMale.webp")
    g.unlock("D_damagedIndifferent_body")

    # At home:
    g.image("images/gallery/images/day01/08_TVkid.webp")
    g.unlock("bg tv_kid_comp")
    g.image("images/gallery/images/day01/09_TVTemple.webp")
    g.unlock("bg tv_sagradafamilia_comp")
    g.image ("night01_atHome_DidacTired_gcom")
    g.unlock("night01_dinner_didac_body")


################################
######## DAY 02

    g.button("gal_day02")
    g.thumbnail("images/gallery/gThumbs/gThumb_b_02.webp")
    g.image("day02schoolTxell_gcom")
    g.unlock("m_bodynew relax_02")
    g.image("day02schoolNeusAngry_gcom")
    g.unlock("neus_body_full day02")
    g.image("day02schoolNeusHappy_gcom")
    g.unlock("neus_body_full day02")
    g.image("afternoon02_beforeshower_didac_gcom")
    g.unlock("afternoon02_beforeshower_didac_body")
    g.image("afternoon02_bg_showering_back_gcom")
    g.unlock("afternoon02_bg showering_Back")
    g.transform(g_zoomTrans_0_5)
    g.image("afternoon02_bg showering_intimate")
    g.unlock("afternoon02_bg showering_intimate")
    g.transform(g_zoomTrans_0_35)
    g.image("afternoon02_bg showering_Silent")
    g.unlock("afternoon02_bg showering_Silent")
    g.transform(g_zoomTrans_0_75)
    g.image("d_showerin_compilation02")
    g.unlock("d_showerin_compilation02")
    g.image("d_showerin_compilation02_gcom")
    g.unlock("d_showerin_compilation02")

################################
######## DAY 03

#####
    g.button("gal_day03")
    g.thumbnail("images/gallery/gThumbs/gThumb_b_03_a.webp")
    g.image("day03schoolTxell_gcom")
    g.unlock("m_bodynew relax_03")
    g.unlock_image("morning02_Txell_Kiss")
    g.transform(g_zoomTrans_0_7)
    g.image("day03schoolNeusHappy_gcom")
    g.unlock("neus_body_full day03")
    g.image("N_Against_grabbed_tensed_shadow_gcom")
    g.unlock("N_Against_P_Arm")
    g.image("N_Against_grabbedHarder_tensed_shadow_gcom")
    g.unlock("N_Against_P_Arm")
    g.image("N_Against_free_tensed_shadow_gcom")
    g.unlock("N_Against_P_Arm notTensed")
    g.image("N_Against_tensed_gcom")
    g.unlock("N_Against_N_body tensed")
    g.image("N_Against_relaxed_gcom")
    g.unlock("N_Against_N_body relaxed")

#####
    g.button("gal_day03NightBar")
    g.thumbnail("images/gallery/gThumbs/gThumb_b_03_b.webp")
    g.image("night03_bar_general_gcom")
    g.unlock("night03_bg bar_general")
    g.image("night03_bar_barra_01_gcom")
    g.unlock("night03_bg bar_barra")
    g.image("night03_bar_barra_NeusAngry_gcom")
    g.unlock("night03_bar_barra_n_eyebrows angryx04")
    g.image("night03_bar_barra_BarmanAngry_gcom")
    g.unlock("night03_bg bar_barra")
    g.image("night03_bar_barra_BarmanAngryAlone_gcom")
    g.unlock("night03_bg bar_barra")
    g.image("night03_bar_backstage_01_gcom")
    g.unlock("night03_bg bar_backstage")
    g.image("night03_bar_backstage_drinking_gcom")
    g.unlock("night03_bar_drinking_glass empty_alot")
    g.image("night03_bar_backstage_drunk_gcom")
    g.unlock("night03_bar_drinking_glass empty_alot")

#####
    g.button("gal_day03NightPedrera")
    g.thumbnail("images/gallery/gThumbs/gThumb_b_03_c.webp")
    g.image("night03_pedreraFar_gcom")
    g.unlock("night03_bg street_pedrera_far")
    g.image("night03_pedreraClose_Empty_gcom")
    g.unlock("night03_bg street_pedrera_close")
    g.image("night03_pedreraClose_bagLooking_gcom")
    g.unlock("neus_arms ld_purse_opened")
    g.image("night03_pedreraClose_bagCondoms_gcom")
    g.unlock("neus_arms ld_condoms")
    g.image("night03_pedreraDoor_testingKeys_gcom")
    g.unlock("neus_arms ld_keystry")
    g.image("night03_pedreraDoor_watchingKeys_gcom")
    g.unlock("neus_arms ld_keys")
    g.image("night03_pedreraDoor_keysIn_gcom")
    g.unlock("neus_arms ld_keysinsert")
    g.image("night03_pedreraDoor_doorOpen_gcom")
    g.unlock("night03_bg street_pedrera_door_opened")
    g.unlock_image("night03_pedrera_neusground")
    g.transform(g_zoomTrans_1)
    g.image("night03_pedreraEntranceDark_gcom")
    g.unlock("night03_bg street_pedrera_entrance")
    g.image("night03_pedreraElevator_gcom")
    g.unlock("night03_bg street_pedrera_elevator")

#####
    g.button("gal_day03NightPedHall")
    g.thumbnail("images/gallery/gThumbs/gThumb_b_03_d.webp")
    g.image("night03_pedreraHall_back_gcom")
    g.unlock("night03_n_pedrera_hall_back_head 01")
    g.image("night03_pedreraHall_down_gcom")
    g.unlock("night03_n_pedrera_hall_back_head 03")
    g.image("night03_pedreraHall_downDark_gcom")
    g.unlock("night03_n_pedrera_hall_back_head 02")
    g.image("night03_pedreraHall_upDark_gcom")
    g.unlock("night03_n_pedrera_hall_back_head 04")
    g.image("night03_pedreraHall_titsShowing_gcom")
    g.unlock("neus_body_full ld_boobs")
    g.image("night03_pedreraHall_titsCovered_gcom")
    g.unlock("neus_body_full ld_covered")
    g.image("night03_pedreraHall_titsCoveredClose_gcom")
    g.unlock("n_closefromup_prothand")
    g.image("night03_pedreraHall_kissing_before_gcom")
    g.unlock("n_closefromup_prothand")
    g.image("night03_pedreraHall_kissing_beforeHand_gcom")
    g.unlock("n_closefromup_prothand")
    # g.image("night03_n_pedrera_hall_fondlebreast_comp 01")
    # g.transform(g_zoomTrans_0_8)
    # g.image("night03_n_pedrera_hall_fondlebreast_comp 02")
    # g.transform(g_zoomTrans_0_8)
    g.image("images/gallery/images/day03/night03_pedHall_nTits.webp")
    g.unlock("night03_n_pedrera_hall_fondlebreast_comp 01")
    g.image("images/gallery/images/day03/night03_pedHall_nTitsGrab.webp")
    g.unlock("night03_n_pedrera_hall_fondlebreast_comp 02")
    g.unlock_image("night03_n_pedrera_hall_fondlebreast_comp 03")
    g.transform(g_zoomTrans_0_8)

    g.image("night03_pedreraHall_kissing_vomitMoment_gcom")
    g.unlock("night03_n_pedrera_puking_body")
    g.image("night03_pedreraHall_wc_surprise_gcom")
    g.unlock("night03_n_pedrera_puking_eyebrows surprise")
    g.image("night03_pedreraHall_wc_sad_gcom")
    g.unlock("night03_n_pedrera_puking_eyebrows sad")

#####
    g.button("gal_day03NightAfter_Didac")
    g.thumbnail("images/gallery/gThumbs/gThumb_b_03_e.webp")
    g.image("night03_atHome_DidacNaked_surprise_gcom")
    g.unlock("didacfhandr towel")
    g.image("night03_atHome_DidacNaked_angry_gcom")
    g.unlock("didacfhandr towel")
    g.image("night03_atHome_DidacNaked_lookingDown_gcom")
    g.unlock("didacfhandr towel")

    g.image("night03_atHome_DidacBedResting_gcom")
    g.unlock("afternight03_didac_bedroom_onbed_body")
    g.image("night03_atHome_DidacBedTalking_gcom")
    g.unlock("afternight03_didac_bedroom_onbed_body")
    g.image("night03_atHome_DidacBedSilent_gcom")
    g.unlock("afternight03_didac_bedroom_onbed_body")
    g.image("night03_atHome_DidacStand_Smile_gcom")
    g.unlock("afternight03_didac_bedroom_onbed_body")

    
    # g.button("gal_pedrera_Neus")
    # g.image("night03_n_pedrera_hall_gcom_01")

    gallery_image_objects.append(g)
    g = Gallery()
    # Even if a Gallery is empty, we still create it


                             #################
                            ###################
                           ##                 ##
                           ##  Gallery Day 4  ##
                           ##                 ##
                            ###################
                             #################


    g.button("am04_ftr_rape_but") # After Morning 04 -- Fitting Room -- Sticking your Dick on Didac, or masturbating with her cheecks.
    g.image("am04_ftr_rape_01")
    g.unlock("aftermorning04_fittingrass 04wet")
    g.image("am04_ftr_rape_02")
    g.unlock("aftermorning04_fittingrass bg_02")
    g.image("am04_ftr_rape_03")
    g.unlock("aftermorning04_fittingrass bg_02")
    g.image("am04_ftr_rape_04")
    g.unlock("aftermorning04_fittingrass bg_02")
    g.image("am04_ftr_rape_05")
    g.unlock("aftermorning04_fittingrass bg_02")
    g.image("am04_ftr_rape_06")
    g.unlock("aftermorning04_fittingrass bg_02")
    g.image("am04_ftr_rape_07")
    g.unlock("aftermorning04_fittingrass bg_02")
    g.image("am04_ftr_rape_08")
    g.unlock("aftermorning04_fittingrass_mcbody_down_naked 03")
    g.image("am04_ftr_rape_09")
    g.unlock("aftermorning04_fittingrass_mcbody_down_naked 03")
    g.image("am04_ftr_rape_10")
    g.unlock("aftermorning04_fittingrass_mcbody_down_naked 03")
    g.image("am04_ftr_rape_11")
    g.unlock("aftermorning04_fittingrass_mcbody_down_naked 03")
    g.image("am04_ftr_rape_12")
    g.unlock("aftermorning04_fittingrass_mcbody_down_naked 03")
    g.image("am04_ftr_rape_13")
    g.unlock("aftermorning04_fittingrass_mcbody_down_naked 03")
    g.image("am04_ftr_rape_14")
    g.unlock("aftermorning04_fittingrass_dbody_cum 02")
    g.image("am04_ftr_rape_15")
    g.unlock("aftermorning04_fittingrass_dbody_cum 02")


    g.button("gal_neusBlowjob")
    g.image("night04_pedrera_blowjob 001")
    g.transform(g_zoomTrans_0_5)
    g.unlock("night04_pedrera_blowjob 007")
    g.image("night04_pedrera_blowjob 002")
    g.transform(g_zoomTrans_0_5)
    g.unlock("night04_pedrera_blowjob 007")
    g.image("night04_pedrera_blowjob 003")
    g.transform(g_zoomTrans_0_5)
    g.unlock("night04_pedrera_blowjob 007")
    #g.image("night04_pedrera_blowjob_gcom_05")
    g.image("night04_pedrera_blowjob 005")
    g.transform(g_zoomTrans_0_5)
    g.unlock("night04_pedrera_blowjob 007")
    g.image("night04_pedrera_blowjob 007")
    g.transform(g_zoomTrans_0_5)
    g.unlock("night04_pedrera_blowjob 007")
    g.image("night04_pedrera_blowjob_pov 024")
    g.transform(g_zoomTrans_0_5)
    g.unlock("night04_pedrera_blowjob 007")
    g.image("night04_pedrera_blowjob_pov 010")
    g.transform(g_zoomTrans_0_5)
    g.unlock("night04_pedrera_blowjob 007")

    gallery_image_objects.append(g)
    g = Gallery()


                             #################
                            ###################
                           ##                 ##
                           ##  Gallery Day 5a  ##
                           ##                 ##
                            ###################
                             #################



    gallery_image_objects.append(g)
    g = Gallery()


                             #################
                            ###################
                           ##                 ##
                           ##  Gallery Day 5b  ##
                           ##                 ##
                            ###################
                             #################

######
    gallery_image_objects.append(g)
    g = Gallery()


                             #################
                            ###################
                           ##                 ##
                           ##  Epilogue       ##
                           ##                 ##
                            ###################
                             #################
    # g.button("rape_neus")
    # g.thumbnail("gThumb_rape_neus")
    # g.image("afternoon01_BathroomrapeB00_gallery")
    # g.transform(g_zoomTrans_0_2)
    # g.condition("persistent.unlock_rape_neus_hand")

######
    gallery_image_objects.append(g)
    g = Gallery()


                          #########
                         ############
                       ##           ##
                       ##  Others   ## # Repetitive ones
                       ##           ##
                        #############
                         ###########

    g.button("gal_didac_bed")
    g.image("didac_bed_gcom_01")
    g.unlock("didac_bed_d_body 01")
    g.image("didac_bed_gcom_02")
    g.unlock("didac_bed_d_body 02")
    g.image("didac_bed_gcom_03")
    g.unlock("didac_bed_d_body 03")
    g.image("didac_bed_gcom_04")
    g.unlock("didac_bed_d_body 04")
    g.image("didac_bed_gcom_05")
    g.unlock("didac_bed_d_body 04")
    g.image("didac_bed_gcom_06")
    g.unlock("didac_bed_d_body 04")
    g.image("didac_bed_gcom_07")
    g.unlock("didac_bed_bed empty_cleansweaty")
    g.image("didac_bed_gcom_08")
    g.unlock("didac_bed_bed emptyClean")

    g.button("gal_kissesNeus")
    g.image("general_handkissNeus_gcom")
    g.unlock("handkiss_n_hand 01")
    g.transform(g_zoomTrans_1)
    g.unlock_image("kiss_ n_n_01")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ n_n_02")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ n_n_03")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ n_n_04")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ n_n_05")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_n_01")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_n_02")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_n_03")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_n_04")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_n_05")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_n_06")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_n_07")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_n_08")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_n_09")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_n_10")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_n_11")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_n_12")
    g.transform(g_zoomTrans_0_2)
    
    g.button("gal_kissesDidac")
    g.unlock_image("kiss_ n_d_01")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ n_d_02")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ n_d_03")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ n_d_04")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ n_d_05")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_d_01")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_d_02")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_d_03")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_d_04")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_d_05")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_d_06")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_d_07")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_d_08")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_d_09")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_d_10")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_d_11")
    g.transform(g_zoomTrans_0_2)
    g.unlock_image("kiss_ f_d_12")
    g.transform(g_zoomTrans_0_2)



######
    gallery_image_objects.append(g)
    g = Gallery()

                          ######################
                         ########################
                        ##                      ##
                        ##      Backgrounds      ##
                        ##                      ##
                         ########################
                          ######################

    

        ## BACKGROUNDS

    g.button("gal_bg_day01_02")
    g.unlock_image("afternoon01_bg Bathroom")
    g.transform(g_zoomTrans_0_75)
    g.unlock_image("afternoon01_bg Toilet")
    g.transform(g_zoomTrans_0_75)
    g.unlock_image("afternoon01_bg Toilet_02")
    g.transform(g_zoomTrans_0_75)
    g.unlock_image("afternoon01_bg Toilet_Close")
    g.transform(g_zoomTrans_0_75)
    g.unlock_image("night01_bg espaguetti")
    g.transform(g_zoomTrans_0_6)
    g.unlock_image("night01_bg dinner")
    g.transform(g_zoomTrans_0_6)
    g.unlock_image("bg tv_kid_comp")
    g.transform(g_zoomTrans_0_1)
    g.unlock_image("bg tv_sagradafamilia_comp")
    g.transform(g_zoomTrans_0_1)

    ##

    # Barcelona City

    g.button("gal_bg_barcelonacity")
    g.unlock_image("aftermorning04_bg cataloniapark") # 01
    g.transform(g_zoomTrans_1)
    g.unlock_image("night03_bg street_rambla_colon") # 02
    g.transform(g_zoomTrans_0_6)
    g.unlock_image("bg an04_corteingles_composition 03") # 03
    g.transform(g_zoomTrans_0_1)

    g.image("bg an04_palaumusica")
    g.unlock("bg an04_palaumusica_composition")
    g.transform(g_zoomTrans_0_1)

    g.unlock_image("bg an04_arctriumf_composition 04") # 04
    g.transform(g_zoomTrans_0_1)
    g.unlock_image("bg an04_placasantagustivell_composition 04") # 05
    g.transform(g_zoomTrans_0_1)
    g.image("aftermorning04_bg fr_aftercum_park") # 06
    g.unlock("aftermorning04_fr_aftercum_park_scene")
    g.transform(g_zoomTrans_0_5)
    g.image("bg an04_street_01")# 07
    g.unlock("bg an04_street_01_composition003")
    g.transform(g_zoomTrans_0_1)
    g.image("bg an04_street02")
    g.unlock("bg an04_street02_composition 03") # 08
    g.transform(g_zoomTrans_0_1)
    g.image("bg an04_vialayetana") # 09
    g.unlock("bg an04_vialayetana_composition")
    g.transform(g_zoomTrans_0_1)
    g.unlock_image("aftermorning04_bg gothicquarter_01") # 10
    g.transform(g_zoomTrans_0_8)
    g.unlock_image("aftermorning04_bg gothicquarter_02") # 11
    g.transform(g_zoomTrans_0_8)
    g.unlock_image("aftermorning04_bg gothicquarter_03") # 12
    g.transform(g_zoomTrans_0_8)

    ##

    # Parc Ciutadella

    g.button("gal_bg_park")

    g.image("bg an04_flat_outside") # 01
    g.transform(g_zoomTrans_0_2)
    g.image("bg an04_flat_stairs") # 02
    g.transform(g_zoomTrans_0_2)
    g.image("bg an04_flat_gate_front") # 03
    g.transform(g_zoomTrans_0_1)
    
    g.image("bg_an04_park_entrance_far_gcom_01") # 04
    g.unlock("bg an04_park_entrance_far_background_compisition 01")
    g.transform(g_zoomTrans_0_5)
    g.image("bg_an04_park_entrance_far_gcom_02") # 05
    g.unlock("bg an04_park_entrance_far_background_compisition 02")
    g.transform(g_zoomTrans_0_5)
    g.image("bg_an04_entranceciutadella_fence_gcom_01") # 06
    g.unlock("bg an04_entranceciutadella_composition 01")
    g.transform(g_zoomTrans_0_5)
    g.image("bg_an04_entranceciutadella_fence_gcom_02") # 07
    g.unlock("bg an04_entranceciutadella_composition 02")
    g.transform(g_zoomTrans_0_5)
    g.image("bg_an04_park_path_01_gcom") # 08
    g.image("bg_an04_park_path_02_gcom") # 09
    #g.unlock("bg an04_park_path01_composition 01")
    #g.transform(g_zoomTrans_0_5)
    g.unlock_image("bg an04_park_fountain") # 10
    g.transform(g_zoomTrans_0_1)

    g.image("bg_an04_park_bank_veryfar_01_gcom") # 11
    g.unlock("bg an04_park_bank_veryfar_composition 01")

    g.image("bg_an04_park_bank_veryfar_02_gcom") # 12
    g.unlock("bg an04_park_bank_veryfar_composition 02")


    g.image("bg_an04_park_bank_far_01_gcom") # 13
    g.transform(g_zoomTrans_0_1)

    g.image("bg an04_park_bank_far_background_01") # 14
    #g.unlock("bg an04_park_bank_far_background_composition 01")
    g.transform(g_zoomTrans_0_1)

    g.unlock_image("bg an04_park_bank_far_closer_background_01") # 15
    g.transform(g_zoomTrans_0_1)
    

    ##

    ## Bar

    g.button("gal_bg_bar")
    g.unlock_image("night03_bg bar_general")
    g.transform(g_zoomTrans_0_75)
    g.unlock_image("night03_bg bar_barra")
    g.transform(g_zoomTrans_0_75)
    g.unlock_image("night03_bg bar_backstage")
    g.transform(g_zoomTrans_0_5)
    
    ##

    g.button("gal_bg_pedrera")
    g.unlock_image("night03_bg street_pedrera_far")
    g.transform(g_zoomTrans_0_55)
    g.unlock_image("night03_bg street_pedrera_close")
    g.transform(g_zoomTrans_0_55)
    g.unlock_image("night03_bg street_pedrera_door")
    g.transform(g_zoomTrans_0_55)
    g.unlock_image("night03_bg street_pedrera_door_opened")
    g.transform(g_zoomTrans_0_55)
    g.unlock_image("night03_bg street_pedrera_entrance")
    g.transform(g_zoomTrans_0_55)
    g.unlock_image("night03_bg_street_pedrera_entrance_lightson")
    g.transform(g_zoomTrans_1)
    g.unlock_image("night03_bg street_pedrera_elevator_day")
    g.transform(g_zoomTrans_0_55)
    g.unlock_image("night03_bg street_pedrera_elevator")
    g.transform(g_zoomTrans_0_55)
    g.unlock_image("night03_bg street_pedrera_corridorclosed")
    g.transform(g_zoomTrans_0_55)
    g.unlock_image("night03_bg street_pedrera_corridoropen")
    g.transform(g_zoomTrans_0_55)
    g.unlock_image("night03_bg street_pedrera_flatdoor_open")
    g.transform(g_zoomTrans_0_55)
    g.unlock_image("night03_bg street_pedrera_flatdoor_closed")
    g.transform(g_zoomTrans_0_55)
    g.unlock_image("night03_bg street_pedrera_hall01")
    g.transform(g_zoomTrans_0_55)
    g.unlock_image("night03_bg street_pedrera_hall02")
    g.transform(g_zoomTrans_0_55)
    g.unlock_image("night03_bg street_pedrera_hall03")
    g.transform(g_zoomTrans_0_55)
    g.unlock_image("night03_n_pedrera_puking_bg")
    g.transform(g_zoomTrans_1)

    ##

    g.button("gal_bg_beds")
    g.image("beds_morning_lightOff_blindUp_DmessyMCmessy")
    g.image("beds_midday_lightOff_blindUp_DmessyMCmessy")
    g.image("beds_morning_lightOff_blindDown_DmessyMCmessy")
    g.image("beds_midday_lightOff_blindDown_DmessyMCmessy")
    g.image("beds_afternoon_lightOn_blindUp_DmessyMCmessy")
    g.image("beds_afternoon_lightOff_blindDown_DmessyMCmessy")
    g.image("beds_night_lightOn_blindDown_DmessyMCmessy")
    g.image("beds_night_lightOn_blindUp_DmessyMCmessy")
    g.image("beds_night_lightOff_blindUp_DmessyMCmessy")
    g.image("beds_night_lightOff_blindDown_DmessyMCmessy")


#####
    gallery_image_objects.append(g)
    g = Gallery()


                          ######################
                         ########################
                        ##                      ##
                        ##  Gallery Game Overs  ##
                        ##                      ##
                         ########################
                          ######################

# Final alternativo 01
    g.button("gal_GO_hospital")
    g.thumbnail("images/gallery/gThumbs/gThumb_b_go_01.webp")
    g.unlock_image("afternoon02_bg HospitalWaitingRoom")
    g.transform(g_zoomTrans_0_75)
    g.image("afternoon02_bg_hospital_corridor_gcom")
    g.transform(g_zoomTrans_1_2)
    g.unlock("afternoon02_bg HospitalCorridor")
    g.unlock_image("afternoon02_bg EmergencyRoom")
    g.transform(g_zoomTrans_0_15)

    ## persistent.gameOver_hospita = True  # day02

# Final Alternativo 02
    g.button("gal_GO_DidacForced") # Day 04 Morning Didac Park.
    g.thumbnail("images/gallery/gThumbs/gThumb_b_go_02.webp")

    g.image("images/gallery/images/gameOvers/go_02__a.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02__b.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02__c.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02__d.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02__e.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02__f.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02__g.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02__h.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02__i.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02__j.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02__k.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02__l.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02__m.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02__n.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02__o.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_cumOut")
    g.image("images/gallery/images/gameOvers/go_02__p.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_cumOut")
    g.image("images/gallery/images/gameOvers/go_02__q.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_cumOut")
    g.image("images/gallery/images/gameOvers/go_02__r.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_cumIn")
    g.image("images/gallery/images/gameOvers/go_02__s.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_cumIn")

    g.unlock_image("aftermorning04_fr_rape_bite")
    g.image("images/gallery/images/gameOvers/go_02_a.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02_b.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02_c.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02_d.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")
    g.image("images/gallery/images/gameOvers/go_02_e.webp")
    g.condition("persistent.gameOver_aftmor04_fr_rape_general")

    g.image("images/gallery/images/gameOvers/go_02_f.webp")
    g.unlock("aftermorning04_fr_rape_after_face front")
    g.image("images/gallery/images/gameOvers/go_02_g.webp")
    g.unlock("aftermorning04_fr_rape_after_face front")
    g.image("images/gallery/images/gameOvers/go_02_h.webp")
    g.unlock("aftermorning04_fr_aftercum_park_d_body female")
    g.image("images/gallery/images/gameOvers/go_02_i.webp")
    g.unlock("aftermorning04_fr_aftercum_park_d_body female")
    g.image("images/gallery/images/gameOvers/go_02_j.webp")
    g.unlock("aftermorning04_fr_aftercum_park_d_body male")
    g.image("images/gallery/images/gameOvers/go_02_k.webp")
    g.unlock("aftermorning04_fr_aftercum_park_d_body male")

# Final Alternativo 03 # day04 You don't have enough points and you didn't hear her conversation during Dinner.
    
    g.button("gal_GO_NotInterested")
    g.thumbnail("images/gallery/gThumbs/gThumb_b_go_03.webp")

    g.image("images/gallery/images/gameOvers/go_03_a.webp")
    g.condition("persistent.gameOver_night04_Neus_Kiss_Idontlikeyou_SorryforyourTime")
    g.image("images/gallery/images/gameOvers/go_03_b.webp")
    g.condition("persistent.gameOver_night04_Neus_Kiss_Idontlikeyou_SorryforyourTime")
    g.image("images/gallery/images/gameOvers/go_03_c.webp")
    g.condition("persistent.gameOver_night04_Neus_Kiss_Idontlikeyou_SorryforyourTime")
    g.image("night03_bg street_pedrera_close")
    g.transform(g_zoomTrans_0_55)

# Final Alternativo 04
    g.button("gal_GO_NotLove") # Day 04 Night you tell Neus you don't love her.
    g.thumbnail("images/gallery/gThumbs/gThumb_b_go_04.webp")

    g.image("images/gallery/images/gameOvers/go_04_a.webp")
    g.condition("persistent.night04_Neus_NotFeelTheSame")
    g.image("night03_bg street_pedrera_close")
    g.condition("persistent.night04_Neus_NotFeelTheSame")
    g.transform(g_zoomTrans_0_55)

# Final Alternativo 05 # Day 04 Night -- You laugh on her.
    g.button("gal_GO_LaughOnNeus")
    g.thumbnail("images/gallery/gThumbs/gThumb_b_go_05.webp")

    g.image("images/gallery/images/gameOvers/go_05_a.webp")
    g.condition("persistent.night04_Neus_After_AreYouHappier_02")
    g.image("images/gallery/images/gameOvers/go_05_b.webp")
    g.condition("persistent.night04_Neus_After_AreYouHappier_02")
    g.image("images/gallery/images/gameOvers/go_05_c.webp")
    g.condition("persistent.night04_Neus_After_AreYouHappier_02")
    g.image("images/gallery/images/gameOvers/go_05_d.webp")
    g.condition("persistent.night04_Neus_After_AreYouHappier_02")

# Final Alternativo 06 # Day 04 Night -- You're killed by your mother after raping Neus...

    g.button("gal_GO_KilledByNana")
    g.thumbnail("images/gallery/gThumbs/gThumb_b_go_06.webp")
    g.condition("persistent.night04_Neus_Rape_Yes")

    g.image("images/gallery/images/gameOvers/go_06_a.webp")
    g.image("images/gallery/images/gameOvers/go_06_b.webp")
    g.image("images/gallery/images/gameOvers/go_06_c.webp")
    g.image("images/gallery/images/gameOvers/go_06_d.webp")
    g.image("images/gallery/images/gameOvers/go_06_e.webp")
    g.image("images/gallery/images/gameOvers/go_06_f.webp")
    g.image("images/gallery/images/gameOvers/go_06_g.webp")
    g.image("images/gallery/images/gameOvers/go_06_h.webp")
    g.image("images/gallery/images/gameOvers/go_06_i.webp")
    g.image("images/gallery/images/gameOvers/go_06_j.webp")
    g.image("images/gallery/images/gameOvers/go_06_k.webp")
    g.image("images/gallery/images/gameOvers/go_06_l.webp")
    g.image("images/gallery/images/gameOvers/go_06_m.webp")
    g.image("images/gallery/images/gameOvers/go_06_n.webp")
    g.image("images/gallery/images/gameOvers/go_06_o.webp")
    g.image("images/gallery/images/gameOvers/go_06_p.webp")
    g.image("images/gallery/images/gameOvers/go_06_q.webp")
    g.image("images/gallery/images/gameOvers/go_06_r.webp")
    g.image("images/gallery/images/gameOvers/go_06_s.webp")
    g.image("images/gallery/images/gameOvers/go_06_t.webp")
    g.image("images/gallery/images/gameOvers/go_06_u.webp")
    g.image("images/gallery/images/gameOvers/go_06_v.webp")
    g.image("images/gallery/images/gameOvers/go_06_w.webp")
    g.image("images/gallery/images/gameOvers/go_06_x.webp")
    g.image("images/gallery/images/gameOvers/go_06_y.webp")

# Final alternativo 07 - 3 different -- Neus Noria Angry-Sad -- A) Didac Pregnant B) Didac Not Pregnat C) No idea...
    
    g.button("gal_GO_LastDateNoriaNotWell")
    g.thumbnail("images/gallery/gThumbs/gThumb_b_go_07.webp")

    g.image("images/gallery/images/gameOvers/go_07_a.webp")
    g.image("images/gallery/images/gameOvers/go_07_b.webp")
    g.image("images/gallery/images/gameOvers/go_07_c.webp")
    g.image("images/gallery/images/gameOvers/go_07_d.webp")
    g.image("images/gallery/images/gameOvers/go_07_e.webp")
    g.unlock_image("bg night05_bg_policestation")
    g.transform(g_zoomTrans_0_1)
    g.image("go_07_m")
    g.unlock("bg night05_bg_policestation")
    g.image("images/gallery/images/gameOvers/go_07_f.webp")
    g.unlock("go_07_e")
    g.image("images/gallery/images/gameOvers/go_07_g.webp")
    g.unlock("go_07_j")
    g.image("images/gallery/images/gameOvers/go_07_h.webp")
    g.unlock("go_07_j")
    g.image("images/gallery/images/gameOvers/go_07_i.webp")
    g.unlock("go_07_j")
    g.image("images/gallery/images/gameOvers/go_07_j.webp")
    g.unlock("go_07_j")
    g.image("images/gallery/images/gameOvers/go_07_k.webp")
    g.unlock("go_07_j")
    g.image("images/gallery/images/gameOvers/go_07_l.webp")
    g.unlock("go_07_j")

## Final alternativo 08


## FIN DEL JUEGO z001 z002 z003




################### Don't Erase
    gallery_image_objects.append(g)
    del g

# Game Over 07 # NeusNoriSad--Didac Not Pregnant
image go_07_e = "images/gallery/images/gameOvers/go_07_e.webp"

# Game Over 07 # NeusNoriSad--Didac Pregnant
image go_07_j ="images/gallery/images/gameOvers/go_07_j.webp"

## if night05_NeusLastDate_Noria_Angry_ToldYouDidacFate == True: #Neus Phoned you. ?? Which ending is this?
# FINAL ALTERNATIVO 07a