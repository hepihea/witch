
default ped_sex_blow_Cond = False

default Pedrera_char_Cond = "NeusClose"

default p_neus_orgasmHurry = False
default p_neus_orgasmHurry_promise = False


label Pedrera_char_lab:

    call p_ao_n_changes

    if Pedrera_char_Cond == "NeusFarRight":
        $ p_neuspos = "neus_exp_"

        show neus_arm_r sd:
            neus_body_atright_position
        show neus_body sd_default:
            neus_body_atright_position
        show neus_head:
            neus_body_atright_position
        show neus_arm_l sd:
            neus_body_atright_position

        show neus_exp_blush 01:
            neus_exp_atright_position
        show neus_exp_mouth sad_Talkingx03:
            neus_exp_atright_position
        show neus_exp_eyes 01:
            neus_exp_atright_position
        show neus_exp_iris front01:
            neus_exp_atright_position
        show neus_exp_tears empty:
            neus_exp_atright_position
        show neus_exp_eyebrows sadx01:
            neus_exp_atright_position
        show neus_exp_glasses:
            neus_exp_atright_position
        show neus_exp_hairfront:
            neus_exp_atright_position

    elif Pedrera_char_Cond == "NeusFarLeft":
        $ p_neuspos = "neus_exp_"

        show neus_arm_r sd:
            neus_body_atleft_position
        show neus_body sd_default:
            neus_body_atleft_position
        show neus_head:
            neus_body_atleft_position
        show neus_arm_l sd:
            neus_body_atleft_position

        show neus_exp_blush 01:
            neus_exp_atleft_position
        show neus_exp_mouth sad_Talkingx03:
            neus_exp_atleft_position
        show neus_exp_eyes 01:
            neus_exp_atleft_position
        show neus_exp_iris front01:
            neus_exp_atleft_position
        show neus_exp_tears empty:
            neus_exp_atleft_position
        show neus_exp_eyebrows sadx01:
            neus_exp_atleft_position
        show neus_exp_glasses:
            neus_exp_atleft_position
        show neus_exp_hairfront:
            neus_exp_atleft_position

    elif Pedrera_char_Cond == "NeusFarFarLeft":
        $ p_neuspos = "neus_exp_"

        show neus_arm_r sd:
            neus_body_atleft_far_position
        show neus_body sd_default:
            neus_body_atleft_far_position
        show neus_head:
            neus_body_atleft_far_position
        show neus_arm_l sd:
            neus_body_atleft_far_position

        show neus_exp_blush 01:
            neus_exp_atleft_far_position
        show neus_exp_mouth sad_Talkingx03:
            neus_exp_atleft_far_position
        show neus_exp_eyes 01:
            neus_exp_atleft_far_position
        show neus_exp_iris front01:
            neus_exp_atleft_far_position
        show neus_exp_tears empty:
            neus_exp_atleft_far_position
        show neus_exp_eyebrows sadx01:
            neus_exp_atleft_far_position
        show neus_exp_glasses:
            neus_exp_atleft_far_position
        show neus_exp_hairfront:
            neus_exp_atleft_far_position

    elif Pedrera_char_Cond == "NeusFarFarRight":
        $ p_neuspos = "neus_exp_"

        show neus_arm_r sd:
            neus_body_atright_far_position
        show neus_body sd_default:
            neus_body_atright_far_position
        show neus_head:
            neus_body_atright_far_position
        show neus_arm_l sd:
            neus_body_atright_far_position

        show neus_exp_blush 01:
            neus_exp_atright_far_position
        show neus_exp_mouth sad_Talkingx03:
            neus_exp_atright_far_position
        show neus_exp_eyes 01:
            neus_exp_atright_far_position
        show neus_exp_iris front01:
            neus_exp_atright_far_position
        show neus_exp_tears empty:
            neus_exp_atright_far_position
        show neus_exp_eyebrows sadx01:
            neus_exp_atright_far_position
        show neus_exp_glasses:
            neus_exp_atright_far_position
        show neus_exp_hairfront:
            neus_exp_atright_far_position

    elif Pedrera_char_Cond == "NeusNotSuper":
        $ p_neuspos = "n_closefromup_"

        scene bg dark_a

        show p_ao_ghost_standing_comp:
            truecenter

        if p_ao_started and not pdaytime == "06morning":
            show night05_Cemetery_smoke_b_comp:
                p_ao_smoke_default

        $ nteye = 8
        show n_closefromup_body sd:
            n_closefromup_03_position
        show n_closefromup_blush 02:
            n_closefromup_03_position
        show n_closefromup_eyes 08:
            n_closefromup_03_position
        show n_closefromup_iris front08:
            n_closefromup_03_position
        show n_closefromup_l_iris front08:
            n_closefromup_03_position
        show n_closefromup_eyebrows serious:
            n_closefromup_03_position
        show n_closefromup_tears 08_03:
            n_closefromup_03_position
        show n_closefromup_mouth sad_Silentx02:
            n_closefromup_03_position
        show n_closefromup_iLight empty:
            n_closefromup_03_position
            additive 1.0
        if n_withoutGlasses_story == False and n_withoutGlasses_Cond == False:
            show n_closefromup_glasses:
                n_closefromup_03_position
        show n_closefromup_hair_front:
            n_closefromup_03_position
        call n_closefromup_tears_tears

    elif Pedrera_char_Cond == "NeusClose":

        $ p_neuspos = "neus_exp_"

        scene bg 03
        show neus_arm_r sd:
            neus_body_atright_close_position
        show neus_body sd_default:
            neus_body_atright_close_position
        show neus_head:
            neus_body_atright_close_position
        show neus_arm_l sd:
            neus_body_atright_close_position
        show neus_exp_blush 01:
            neus_exp_atright_close_position
        show neus_exp_mouth sad_Silentx01:
            neus_exp_atright_close_position
        show neus_exp_eyes 08:
            neus_exp_atright_close_position
        show neus_exp_iris front08:
            neus_exp_atright_close_position
        show neus_exp_l_iris empty:
            neus_exp_atright_close_position
        show neus_exp_iLight empty:
            neus_exp_atright_close_position
        show neus_exp_tears 08_01:
            neus_exp_atright_close_position
        show neus_exp_eyebrows serious:
            neus_exp_atright_close_position
        show neus_exp_glasses:
            neus_exp_atright_close_position
        show neus_exp_hairfront:
            neus_exp_atright_close_position

    elif Pedrera_char_Cond == "NeusBitClose":

        $ p_neuspos = "neus_exp_"

        scene bg 03
        show neus_arm_r sd:
            neus_body_atright_bitClose_position
        show neus_body sd_default:
            neus_body_atright_bitClose_position
        show neus_head:
            neus_body_atright_bitClose_position
        show neus_arm_l sd:
            neus_body_atright_bitClose_position
        show neus_exp_blush 01:
            neus_exp_atright_bitClose_position
        show neus_exp_mouth sad_Silentx01:
            neus_exp_atright_bitClose_position
        show neus_exp_eyes 08:
            neus_exp_atright_bitClose_position
        show neus_exp_iris front08:
            neus_exp_atright_bitClose_position
        show neus_exp_l_iris empty:
            neus_exp_atright_bitClose_position
        show neus_exp_iLight empty:
            neus_exp_atright_bitClose_position
        show neus_exp_tears 08_01:
            neus_exp_atright_bitClose_position
        show neus_exp_eyebrows serious:
            neus_exp_atright_bitClose_position
        show neus_exp_glasses:
            neus_exp_atright_bitClose_position
        show neus_exp_hairfront:
            neus_exp_atright_bitClose_position

    elif Pedrera_char_Cond == "NeusClose_show":

        $ p_neuspos = "neus_exp_"

        show bg_03
        show neus_arm_r sd:
            neus_body_atright_close_position
        show neus_body sd_default:
            neus_body_atright_close_position
        show neus_head:
            neus_body_atright_close_position
        show neus_arm_l sd:
            neus_body_atright_close_position
        show neus_exp_blush 01:
            neus_exp_atright_close_position
        show neus_exp_mouth sad_Silentx01:
            neus_exp_atright_close_position
        show neus_exp_eyes 08:
            neus_exp_atright_close_position
        show neus_exp_iris front08:
            neus_exp_atright_close_position
        show neus_exp_l_iris empty:
            neus_exp_atright_close_position
        show neus_exp_iLight empty:
            neus_exp_atright_close_position
        show neus_exp_tears 08_01:
            neus_exp_atright_close_position
        show neus_exp_eyebrows serious:
            neus_exp_atright_close_position
        show neus_exp_glasses:
            neus_exp_atright_close_position
        show neus_exp_hairfront:
            neus_exp_atright_close_position

    elif Pedrera_char_Cond == "NeusSuperClose":
        $ p_neuspos = "n_closefromup_"

        if pdaytime == "06morning":
            scene morning04_bg bedroom_neus_a
        elif pdaytime == "05_night_Pedrera":
            scene bg ped_04
        else:
            scene bg dark_a

        show p_ao_ghost_standing_comp:
            truecenter

        if p_ao_started and not pdaytime == "06morning":
            show night05_Cemetery_smoke_b_comp:
                p_ao_smoke_default

        $ nteye = 8
        show n_closefromup_body sd:
            n_closefromup_05_position
        show n_closefromup_blush 02:
            n_closefromup_05_position
        show n_closefromup_eyes 08:
            n_closefromup_05_position
        show n_closefromup_iris front08:
            n_closefromup_05_position
        show n_closefromup_l_iris front08:
            n_closefromup_05_position
        show n_closefromup_eyebrows serious:
            n_closefromup_05_position
        show n_closefromup_tears 08_03:
            n_closefromup_05_position
        show n_closefromup_mouth sad_Silentx02:
            n_closefromup_05_position
        show n_closefromup_iLight empty:
            n_closefromup_05_position
            additive 1.0
        # show n_closefromup_bright empty:
        #     n_closefromup_05_position
        #     additive 1.0
        if n_withoutGlasses_story == False and n_withoutGlasses_Cond == False:
            show n_closefromup_glasses:
                n_closefromup_05_position
        show n_closefromup_hair_front:
            n_closefromup_05_position
        call n_closefromup_tears_tears

        show n_closefromup_handL empty:
            n_closefromup_05_position

        

    elif Pedrera_char_Cond == "NeusSuperSuperClose":
        $ p_neuspos = "n_closefromup_"

        scene bg dark_a

        if p_ao_started and not pdaytime == "06morning":
            show night05_Cemetery_smoke_b_comp:
                p_ao_smoke_default

        $ nteye = 8
        show n_closefromup_body sd:
            n_closefromup_1_position
        show n_closefromup_blush 02:
            n_closefromup_1_position
        show n_closefromup_eyes 08:
            n_closefromup_1_position
        show n_closefromup_iris front08:
            n_closefromup_1_position
        show n_closefromup_l_iris front08:
            n_closefromup_1_position
        show n_closefromup_eyebrows serious:
            n_closefromup_1_position
        show n_closefromup_tears 08_03:
            n_closefromup_1_position
        show n_closefromup_mouth sad_Silentx02:
            n_closefromup_1_position
        show n_closefromup_iLight empty:
            n_closefromup_1_position
            additive 1.0
        # show n_closefromup_bright empty:
        #     n_closefromup_1_position
        #     additive 1.0
        
        if n_withoutGlasses_story == False and n_withoutGlasses_Cond == False:
            show n_closefromup_glasses:
                n_closefromup_1_position
        show n_closefromup_hair_front:
            n_closefromup_1_position
        call n_closefromup_tears_tears

    elif Pedrera_char_Cond == "ALL":
        $ p_neuspos = "neus_exp_"

        $ p_deyespCond = False
        call p_deyesp_check

        #scene bg 01
        scene bg ped_02

        show m_bodynew naked_hips:
            mtxell_body_ontheleft_position

        show m_exp_blush 01:
            mtxell_exp_ontheleft_position
        show m_exp_mouth sad_Silentx02:
            mtxell_exp_ontheleft_position
        show m_exp_eyes 08:
            mtxell_exp_ontheleft_position
        show m_exp_piris front08:
            mtxell_exp_ontheleft_position
        show m_exp_eyebrows serious:
            mtxell_exp_ontheleft_position

        show m_exp_hair_front:
            mtxell_exp_ontheleft_position

        ###

        # show didacf_aprove_new:
        #     df_body_onthecenter

        show didacfbodycloth_whole new_naked:
            df_body_onthecenter

        show didacf_blush 01:
            df_exp_onthecenter
        show didacf_eyes 08:
            df_exp_onthecenter
        show didacf_pupils front08:
            df_exp_onthecenter
        show didacf_eyebrows serious:
            df_exp_onthecenter
        show didacfbodytop_hair new:
            df_body_onthecenter
        show didacf_mouth sad_Silentx03:
            df_exp_onthecenter
        show didacf_tears empty:
            df_exp_onthecenter

        ###

        show neus_arm_r sd:
            neus_body_atright_position
        show neus_body sd_default:
            neus_body_atright_position
        show neus_head:
            neus_body_atright_position
        show neus_arm_l sd:
            neus_body_atright_position
        show neus_exp_blush 01:
            neus_exp_atright_position
        show neus_exp_mouth sad_Silentx03:
            neus_exp_atright_position
        show neus_exp_eyes 08:
            neus_exp_atright_position
        show neus_exp_iris front08:
            neus_exp_atright_position
        show neus_exp_l_iris empty:
            neus_exp_atright_position
        show neus_exp_iLight empty:
            neus_exp_atright_position
        show neus_exp_tears 08_01:
            neus_exp_atright_position
        show neus_exp_eyebrows serious:
            neus_exp_atright_position
        show neus_exp_glasses:
            neus_exp_atright_position
        show neus_exp_hairfront:
            neus_exp_atright_position

    elif Pedrera_char_Cond == "NeusDidac_close":
        $ p_neuspos = "neus_exp_"

        $ p_deyespCond = False
        call p_deyesp_check

        if pdaytime == "06morning":
            scene morning04_bg bedroom_neus_a
        else:
            scene bg 01

        show didacfbodycloth_whole new_naked:
            df_body_ontheleftInverted_close

        show didacf_blush 01:
            df_exp_ontheleftInverted_close
        show didacf_eyes 08:
            df_exp_ontheleftInverted_close
        show didacf_pupils front08:
            df_exp_ontheleftInverted_close
        show didacf_eyebrows serious:
            df_exp_ontheleftInverted_close
        show didacfbodytop_hair new:
            df_body_ontheleftInverted_close
        show didacf_mouth sad_Silentx03:
            df_exp_ontheleftInverted_close
        show didacf_tears empty:
            df_exp_ontheleftInverted_close

        ###

        show neus_arm_r sd:
            neus_body_atright_close_position
        show neus_body sd_default:
            neus_body_atright_close_position
        show neus_head:
            neus_body_atright_close_position
        show neus_arm_l sd:
            neus_body_atright_close_position
        show neus_exp_blush 01:
            neus_exp_atright_close_position
        show neus_exp_mouth sad_Silentx03:
            neus_exp_atright_close_position
        show neus_exp_eyes 08:
            neus_exp_atright_close_position
        show neus_exp_iris front08:
            neus_exp_atright_close_position

        show neus_exp_l_iris empty:
            neus_exp_atright_close_position
        show neus_exp_iLight empty:
            additive 1.0
            neus_exp_atright_close_position

        show neus_exp_tears 08_01:
            neus_exp_atright_close_position
        show neus_exp_eyebrows serious:
            neus_exp_atright_close_position
        show neus_exp_glasses:
            neus_exp_atright_close_position
        show neus_exp_hairfront:
            neus_exp_atright_close_position

    elif Pedrera_char_Cond == "TxellNeus":

        $ p_neuspos = "neus_exp_"

        scene bg ped_02

        show m_bodynew naked_hips:
            mtxell_body_ontheleft_position

        show m_exp_blush 01:
            mtxell_exp_ontheleft_position
        show m_exp_mouth sad_Silentx02:
            mtxell_exp_ontheleft_position
        show m_exp_eyes 08:
            mtxell_exp_ontheleft_position
        show m_exp_piris front08:
            mtxell_exp_ontheleft_position
        show m_exp_eyebrows serious:
            mtxell_exp_ontheleft_position

        ##

        show m_exp_hair_front:
            mtxell_exp_ontheleft_position

        show neus_arm_r sd:
            neus_body_atright_position
        show neus_body sd_default:
            neus_body_atright_position
        show neus_head:
            neus_body_atright_position
        show neus_arm_l sd:
            neus_body_atright_position
        show neus_exp_blush 01:
            neus_exp_atright_position
        show neus_exp_mouth sad_Silentx03:
            neus_exp_atright_position
        show neus_exp_eyes 08:
            neus_exp_atright_position
        show neus_exp_iris front08:
            neus_exp_atright_position
        show neus_exp_l_iris empty:
            neus_exp_atright_position
        show neus_exp_iLight empty:
            neus_exp_atright_position
        show neus_exp_tears 08_01:
            neus_exp_atright_position
        show neus_exp_eyebrows serious:
            neus_exp_atright_position
        show neus_exp_glasses:
            neus_exp_atright_position
        show neus_exp_hairfront:
            neus_exp_atright_position

    elif Pedrera_char_Cond == "TxellDidac":

        $ p_deyespCond = False
        call p_deyesp_check

        scene bg ped_02

        show m_bodynew naked_hips:
            mtxell_body_ontheleft_position

        show m_exp_blush 01:
            mtxell_exp_ontheleft_position
        show m_exp_mouth sad_Silentx02:
            mtxell_exp_ontheleft_position
        show m_exp_eyes 08:
            mtxell_exp_ontheleft_position
        show m_exp_piris front08:
            mtxell_exp_ontheleft_position
        show m_exp_eyebrows serious:
            mtxell_exp_ontheleft_position

        show m_exp_hair_front:
            mtxell_exp_ontheleft_position

        ###

        # show didacf_aprove_new:
        #     df_body_onthecenter

        show didacfbodycloth_whole new_naked:
            df_body_onthecenter

        show didacf_blush 01:
            df_exp_onthecenter
        show didacf_eyes 08:
            df_exp_onthecenter
        show didacf_pupils front08:
            df_exp_onthecenter
        show didacf_eyebrows serious:
            df_exp_onthecenter
        show didacfbodytop_hair new:
            df_body_onthecenter
        show didacf_mouth sad_Silentx03:
            df_exp_onthecenter
        show didacf_tears empty:
            df_exp_onthecenter

    elif Pedrera_char_Cond == "TxellClose":

        scene bg ped_04

        show m_bodynew naked_hips:
            mtxell_body_ontheleft_zoom_0_4_pos

        show m_exp_blush 01:
            mtxell_exp_ontheleft_zoom_0_4_pos
        show m_exp_mouth happy_Silentx06:
            mtxell_exp_ontheleft_zoom_0_4_pos
        show m_exp_eyes 04:
            mtxell_exp_ontheleft_zoom_0_4_pos
        show m_exp_piris front04:
            mtxell_exp_ontheleft_zoom_0_4_pos
        show m_exp_eyebrows angryx01:
            mtxell_exp_ontheleft_zoom_0_4_pos

        show m_exp_hair_front:
            mtxell_exp_ontheleft_zoom_0_4_pos

    elif Pedrera_char_Cond == "TxellClose_b":

        scene bg ped_04

        show m_bodynew naked_down:
            mtxell_body_center_zoom_0_4_pos

        show m_exp_blush 01:
            mtxell_exp_center_zoom_0_4_pos
        show m_exp_mouth happy_Silentx06:
            mtxell_exp_center_zoom_0_4_pos
        show m_exp_eyes 04:
            mtxell_exp_center_zoom_0_4_pos
        show m_exp_piris front04:
            mtxell_exp_center_zoom_0_4_pos
        show m_exp_eyebrows angryx01:
            mtxell_exp_center_zoom_0_4_pos

        show m_exp_hair_front:
            mtxell_exp_center_zoom_0_4_pos

    elif Pedrera_char_Cond == "TxellClose_b_show":

        show bg_02

        show m_bodynew naked_down:
            mtxell_body_center_zoom_0_4_pos

        show m_exp_blush 01:
            mtxell_exp_center_zoom_0_4_pos
        show m_exp_mouth happy_Silentx06:
            mtxell_exp_center_zoom_0_4_pos
        show m_exp_eyes 04:
            mtxell_exp_center_zoom_0_4_pos
        show m_exp_piris front04:
            mtxell_exp_center_zoom_0_4_pos
        show m_exp_eyebrows angryx01:
            mtxell_exp_center_zoom_0_4_pos

        show m_exp_hair_front:
            mtxell_exp_center_zoom_0_4_pos

    elif Pedrera_char_Cond == "TxellSuperClose":

        #scene bg 02
        scene bg ped_04

        show m_bodynew naked_down:
            mtxell_body_center_zoom_1_0_pos

        show m_exp_blush 01:
            mtxell_exp_center_zoom_1_0_pos
        show m_exp_mouth happy_Silentx06:
            mtxell_exp_center_zoom_1_0_pos
        show m_exp_eyes 04:
            mtxell_exp_center_zoom_1_0_pos
        show m_exp_piris front04:
            mtxell_exp_center_zoom_1_0_pos
        show m_exp_eyebrows angryx01:
            mtxell_exp_center_zoom_1_0_pos

        show m_armL empty:
            mtxell_body_center_zoom_1_0_pos

        show m_exp_hair_front:
            mtxell_exp_center_zoom_1_0_pos

    elif Pedrera_char_Cond == "TxellSuperClose_show":

        show bg_02

        show m_bodynew naked_down:
            mtxell_body_center_zoom_1_0_pos

        show m_exp_blush 01:
            mtxell_exp_center_zoom_1_0_pos
        show m_exp_mouth happy_Silentx06:
            mtxell_exp_center_zoom_1_0_pos
        show m_exp_eyes 04:
            mtxell_exp_center_zoom_1_0_pos
        show m_exp_piris front04:
            mtxell_exp_center_zoom_1_0_pos
        show m_exp_eyebrows angryx01:
            mtxell_exp_center_zoom_1_0_pos

        show m_armL empty:
            mtxell_body_center_zoom_1_0_pos

        show m_exp_hair_front:
            mtxell_exp_center_zoom_1_0_pos

    elif Pedrera_char_Cond == "DidacClose":

        $ p_deyespCond = False
        call p_deyesp_check

        if pdaytime == "06morning":
            scene morning04_bg bedroom_neus_a
        else:
            scene bg 04

        if d_bodyType == "_slim":
            show didacfbodycloth_whole new_naked:
                df_body_onthecenter_close
        else:
            show didacfbodybelow_naked_drops 00:
                df_body_onthecenter_close
            show didacfhandr leg_naked:
                df_body_onthecenter_close
            show didacfbodytop_naked_drops 00:
                df_body_onthecenter_close
            show didacfhandl hip_naked:
                df_body_onthecenter_close

        show didacf_blush 01:
            df_exp_onthecenter_close
        show didacf_eyes 08:
            df_exp_onthecenter_close
        show didacf_pupils front08:
            df_exp_onthecenter_close
        show didacf_eyebrows serious:
            df_exp_onthecenter_close
        show didacfbodytop_hair:
            df_body_onthecenter_close
        show didacf_mouth sad_Silentx03:
            df_exp_onthecenter_close
        show didacf_tears empty:
            df_exp_onthecenter_close

    elif Pedrera_char_Cond == "DidacClose_show":

        $ p_deyespCond = False
        call p_deyesp_check

        if pdaytime == "06morning":
            show morning04_bg bedroom_neus_a
        else:
            show bg_04

        show didacfbodycloth_whole new_naked:
            df_body_onthecenter_close
        show didacf_blush 01:
            df_exp_onthecenter_close
        show didacf_eyes 08:
            df_exp_onthecenter_close
        show didacf_pupils front08:
            df_exp_onthecenter_close
        show didacf_eyebrows serious:
            df_exp_onthecenter_close
        show didacfbodytop_hair new:
            df_body_onthecenter_close
        show didacf_mouth sad_Silentx03:
            df_exp_onthecenter_close
        show didacf_tears empty:
            df_exp_onthecenter_close

    elif Pedrera_char_Cond == "DidacSuperClose":

        $ p_deyespCond = False
        call p_deyesp_check

        if pdaytime == "06morning":
            scene morning04_bg bedroom_neus_a
        else:
            scene bg 04

        show didacfbodycloth_whole new_naked:
            df_body_onthecenter_superClose
        show didacf_blush 01:
            df_exp_onthecenter_superClose
        show didacf_eyes 08:
            df_exp_onthecenter_superClose
        show didacf_pupils front08:
            df_exp_onthecenter_superClose
        show didacf_eyebrows serious:
            df_exp_onthecenter_superClose
        show didacfbodytop_hair new:
            df_body_onthecenter_superClose
        show didacf_mouth sad_Silentx03:
            df_exp_onthecenter_superClose
        show didacf_tears empty:
            df_exp_onthecenter_superClose

    elif Pedrera_char_Cond == "p_nobody":

        $ p_neuspos = ""

        hide bg_03
        hide neus_arm_r
        hide neus_body
        hide neus_head
        hide neus_arm_l
        hide neus_exp_blush
        hide neus_exp_mouth
        hide neus_exp_eyes
        hide neus_exp_iris
        hide neus_exp_l_iris
        hide neus_exp_iLight
        hide neus_exp_tears
        hide neus_exp_eyebrows
        hide neus_exp_glasses
        hide neus_exp_hairfront

        hide bg_02
        hide m_bodynew
        hide m_exp_blush
        hide m_exp_mouth
        hide m_exp_eyes
        hide m_exp_piris
        hide m_exp_eyebrows
        hide m_exp_hair_front

        hide bg_04
        hide didacfbodycloth_whole
        hide didacf_blush
        hide didacf_eyes
        hide didacf_pupils
        hide didacf_eyebrows
        hide didacfbodytop_hair
        hide didacf_mouth
        hide didacf_tears

    elif Pedrera_char_Cond == "NeusFar_show":

        $ p_neuspos = "neus_exp_"

        show bg_03
        show neus_arm_r sd:
            neus_body_atcenter_position
        show neus_body sd_default:
            neus_body_atcenter_position
        show neus_head:
            neus_body_atcenter_position
        show neus_arm_l sd:
            neus_body_atcenter_position
        show neus_exp_blush 01:
            neus_exp_atcenter_position
        show neus_exp_mouth sad_Talkingx03:
            neus_exp_atcenter_position
        show neus_exp_eyes 08:
            neus_exp_atcenter_position
        show neus_exp_iris front08:
            neus_exp_atcenter_position
        show neus_exp_l_iris empty:
            neus_exp_atcenter_position
        show neus_exp_iLight empty:
            neus_exp_atcenter_position
        show neus_exp_tears 08_01:
            neus_exp_atcenter_position
        show neus_exp_eyebrows serious:
            neus_exp_atcenter_position
        show neus_exp_glasses:
            neus_exp_atcenter_position
        show neus_exp_hairfront:
            neus_exp_atcenter_position

    elif Pedrera_char_Cond == "NeusFar":

        $ p_neuspos = "neus_exp_"

        scene bg 03
        show neus_arm_r sd:
            neus_body_atcenter_position
        show neus_body sd_default:
            neus_body_atcenter_position
        show neus_head:
            neus_body_atcenter_position
        show neus_arm_l sd:
            neus_body_atcenter_position
        show neus_exp_blush 01:
            neus_exp_atcenter_position
        show neus_exp_mouth sad_Talkingx03:
            neus_exp_atcenter_position
        show neus_exp_eyes 08:
            neus_exp_atcenter_position
        show neus_exp_iris front08:
            neus_exp_atcenter_position
        show neus_exp_l_iris empty:
            neus_exp_atcenter_position
        show neus_exp_iLight empty:
            neus_exp_atcenter_position
        show neus_exp_tears 08_01:
            neus_exp_atcenter_position
        show neus_exp_eyebrows serious:
            neus_exp_atcenter_position
        show neus_exp_glasses:
            neus_exp_atcenter_position
        show neus_exp_hairfront:
            neus_exp_atcenter_position

    elif Pedrera_char_Cond == "TxellDChin": # Drying her Chin after licking DIdac at bed.

        scene bg 02

        show m_bodynew naked_hips:
            mtxell_body_Dchin_pos

        show m_exp_blush 01:
            mtxell_exp_Dchin_pos
        show m_exp_mouth happy_Silentx06:
            mtxell_exp_Dchin_pos
        show m_exp_eyes 04:
            mtxell_exp_Dchin_pos
        show m_exp_piris front04:
            mtxell_exp_Dchin_pos
        show m_exp_eyebrows angryx01:
            mtxell_exp_Dchin_pos

        show m_exp_hair_front:
            mtxell_exp_Dchin_pos

    elif Pedrera_char_Cond == "NeusPain":

        $ p_neuspos = "neus_exp_"

        scene bg 03
        show neus_arm_r sd:
            neus_body_pain_position
        show neus_body sd_default:
            neus_body_pain_position
        show neus_head:
            neus_body_pain_position
        show neus_arm_l sd:
            neus_body_pain_position
        show neus_exp_blush 01:
            neus_exp_pain_position
        show neus_exp_mouth sad_Talkingx03:
            neus_exp_pain_position
        show neus_exp_eyes 08:
            neus_exp_pain_position
        show neus_exp_iris front08:
            neus_exp_pain_position
        show neus_exp_l_iris empty:
            neus_exp_pain_position
        show neus_exp_iLight empty:
            neus_exp_pain_position
        show neus_exp_tears 08_01:
            neus_exp_pain_position
        show neus_exp_eyebrows serious:
            neus_exp_pain_position
        show neus_exp_glasses:
            neus_exp_pain_position
        show neus_exp_hairfront:
            neus_exp_pain_position

    elif Pedrera_char_Cond == "DidacPain":

        $ p_deyespCond = False
        call p_deyesp_check

        scene bg 04
        show didacfbodycloth_whole new_naked:
            df_body_pain_close
        show didacf_blush 01:
            df_exp_pain_close
        show didacf_eyes 08:
            df_exp_pain_close
        show didacf_pupils front08:
            df_exp_pain_close
        show didacf_eyebrows serious:
            df_exp_pain_close
        show didacfbodytop_hair new:
            df_body_pain_close
        show didacf_mouth sad_Silentx03:
            df_exp_pain_close
        show didacf_tears empty:
            df_exp_pain_close

    elif Pedrera_char_Cond == "TxellPain":
        scene bg 02

        show m_bodynew naked_hips:
            mtxell_body_Dchin_pos

        show m_exp_blush 01:
            mtxell_exp_Dchin_pos
        show m_exp_mouth happy_Silentx06:
            mtxell_exp_Dchin_pos
        show m_exp_eyes 04:
            mtxell_exp_Dchin_pos
        show m_exp_piris front04:
            mtxell_exp_Dchin_pos
        show m_exp_eyebrows angryx01:
            mtxell_exp_Dchin_pos

        show m_exp_hair_front:
            mtxell_exp_Dchin_pos

    elif Pedrera_char_Cond == "NeusWall":
        $ p_neuspos = "neus_exp_"

        if pdaytime == "06morning":
            scene morning04_bg bedroom_neus_a
        else:
            scene night04_pedrera_baba02_background:
                truecenter
                zoom 1.0 xpos 0.5 ypos 1.0

        show neus_arm_r sd:
            neus_body_atcenter_closeVery_position
        show neus_body sd_default:
            neus_body_atcenter_closeVery_position
        show neus_head:
            neus_body_atcenter_closeVery_position
        show neus_arm_l sd:
            neus_body_atcenter_closeVery_position
        show neus_exp_blush 01:
            neus_exp_atcenter_closeVery_position
        show neus_exp_mouth sad_Silentx03:
            neus_exp_atcenter_closeVery_position
        show neus_exp_eyes 08:
            neus_exp_atcenter_closeVery_position
        show neus_exp_iris front08:
            neus_exp_atcenter_closeVery_position
        show neus_exp_l_iris empty:
            neus_exp_atcenter_closeVery_position
        show neus_exp_iLight empty:
            neus_exp_atcenter_closeVery_position
        show neus_exp_tears 08_01:
            neus_exp_atcenter_closeVery_position
        show neus_exp_eyebrows serious:
            neus_exp_atcenter_closeVery_position
        show neus_exp_glasses:
            neus_exp_atcenter_closeVery_position
        show neus_exp_hairfront:
            neus_exp_atcenter_closeVery_position

    elif Pedrera_char_Cond == "NeusBodySuperClose":

        $ p_neuspos = "neus_exp_"

        if pdaytime == "06morning":
            scene morning04_bg bedroom_neus_a
        else:
            scene black

        show neus_arm_r sd:
            neus_body_atcenter_closeSuper_position
        show neus_body sd_default:
            neus_body_atcenter_closeSuper_position
        show neus_head:
            neus_body_atcenter_closeSuper_position
        show neus_arm_l sd:
            neus_body_atcenter_closeSuper_position
        show neus_exp_blush 01:
            neus_exp_atcenter_closeSuper_position
        show neus_exp_mouth sad_Silentx03:
            neus_exp_atcenter_closeSuper_position
        show neus_exp_eyes 08:
            neus_exp_atcenter_closeSuper_position
        show neus_exp_iris front08:
            neus_exp_atcenter_closeSuper_position
        show neus_exp_l_iris empty:
            neus_exp_atcenter_closeSuper_position
        show neus_exp_iLight empty:
            neus_exp_atcenter_closeSuper_position
        show neus_exp_tears 08_01:
            neus_exp_atcenter_closeSuper_position
        show neus_exp_eyebrows serious:
            neus_exp_atcenter_closeSuper_position
        show neus_exp_glasses:
            neus_exp_atcenter_closeSuper_position
        show neus_exp_hairfront:
            neus_exp_atcenter_closeSuper_position

    else:

        "ERROR IMAGE"

    if Pedrera_char_Cond in ["NeusBodySuperClose", "NeusWall", "NeusPain", "NeusFar", "NeusFar_show", "TxellNeus", "NeusDidac_close", "ALL", "NeusSuperSuperClose", "NeusSuperClose", "NeusClose_show", "NeusClose", "NeusNotSuper"]:
        if n_dress == "naked":
            if p_neuspos == "neus_exp_":
                show neus_arm_l naked
                show neus_body naked
                show neus_arm_r naked

            elif p_neuspos == "n_closefromup_":
                show n_closefromup_body naked

    return

##########################################################################################
##########################################################################################
##########################################################################################
############################################################
##########################################################################################
##########################################################################################
##########################################################################################


image pedrera05_neus_complete_body sd_image:

    contains:
        "bg 03"
        truecenter
        zoom 1.5

    contains:
        "neus_arm_r sd"
        neus_body_atcenter_position
    contains:
        "neus_body sd_default"
        neus_body_atcenter_position
    contains:
        "neus_head"
        neus_body_atcenter_position
    contains:
        "neus_arm_l sd"
        neus_body_atcenter_position
    contains:
        "neus_exp_blush 03"
        neus_exp_atcenter_position
    contains:
        "neus_exp_mouth sadbiting_Silentx05"
        neus_exp_atcenter_position
    contains:
        "neus_exp_eyes 08"
        neus_exp_atcenter_position
    contains:
        "neus_exp_iris front08"
        neus_exp_atcenter_position
    contains:
        "neus_exp_tears 08_03"
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


image pedrera05_neus_complete_body naked_image:

    contains:
        "bg 03"
        truecenter
        zoom 1.5

    contains:
        "neus_arm_r naked"
        neus_body_atcenter_position
    contains:
        "neus_body naked"
        neus_body_atcenter_position
    contains:
        "neus_head"
        neus_body_atcenter_position
    contains:
        "neus_arm_l naked"
        neus_body_atcenter_position
    contains:
        "neus_exp_blush 03"
        neus_exp_atcenter_position
    contains:
        "neus_exp_mouth sadbiting_Silentx05"
        neus_exp_atcenter_position
    contains:
        "neus_exp_eyes 08"
        neus_exp_atcenter_position
    contains:
        "neus_exp_iris front08"
        neus_exp_atcenter_position
    contains:
        "neus_exp_tears 08_03"
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

##########################################################################################
##########################################################################################
##########################################################################################
############################################################
##########################################################################################
##########################################################################################
##########################################################################################

image ped_pain_didac = SaturateTint("images/day05/pedrera/ped_pain_didac.webp")
image ped_pain_neus = SaturateTint("images/day05/pedrera/ped_pain_neus.webp")

image ped_motherOnTxell = SaturateTint("images/day05/pedrera/ped_motherOnTxell.webp")
image ped_motherOnTxell empty = SaturateTint("images/general/empty.webp")

image ped_motherOnTxell_TEST = "images/day05/pedrera/ped_motherOnTxell_TEST.webp"
image ped_motherOnTxell_eye closed = SaturateTint("images/day05/pedrera/ped_motherOnTxell_eye_closed.webp")
image ped_motherOnTxell_eye opened = SaturateTint("images/day05/pedrera/ped_motherOnTxell_eye_opened.webp")
image ped_motherOnTxell_eyebrow angryx01 = SaturateTint("images/day05/pedrera/ped_motherOnTxell_eyebrow_angryx01.webp")
image ped_motherOnTxell_eyebrow angryx03 = SaturateTint("images/day05/pedrera/ped_motherOnTxell_eyebrow_angryx03.webp")
image ped_motherOnTxell_eyebrow surprise = SaturateTint("images/day05/pedrera/ped_motherOnTxell_eyebrow_surprise.webp")
image ped_motherOnTxell_eyeShine = "images/day05/pedrera/ped_motherOnTxell_eyeShine.webp"
image ped_motherOnTxell_mouth happy_Talking = SaturateTint("images/day05/pedrera/ped_motherOnTxell_mouth_happy_Talking.webp")
image ped_motherOnTxell_mouth sad_Talking = SaturateTint("images/day05/pedrera/ped_motherOnTxell_mouth_sad_Talking.webp")

transform ped_motherOnTxell_expression_pos:
    truecenter
    xpos 0.028 ypos 0.75



image ped_motherOnTxell pain:
    contains:
        "ped_motherOnTxell"
        truecenter

    contains:
        "ped_motherOnTxell_mouth sad_Talking"
        ped_motherOnTxell_expression_pos

    contains:
        "ped_motherOnTxell_eye closed"
        ped_motherOnTxell_expression_pos

    contains:
        "ped_motherOnTxell_eyebrow angryx03"
        ped_motherOnTxell_expression_pos

image ped_motherOnTxell sad_Silent:
    contains:
        "ped_motherOnTxell"
        truecenter

    contains:
        "ped_motherOnTxell_eye opened"
        ped_motherOnTxell_expression_pos

    contains:
        "ped_motherOnTxell_eyebrow angryx01"
        ped_motherOnTxell_expression_pos

    contains:
        "ped_motherOnTxell_eyeShine"
        ped_motherOnTxell_expression_pos
        additive 1.0

image ped_motherOnTxell happy_Talking:

    contains:
        "ped_motherOnTxell"
        truecenter

    contains:
        "ped_motherOnTxell_mouth happy_Talking"
        ped_motherOnTxell_expression_pos

    contains:
        "ped_motherOnTxell_eye opened"
        ped_motherOnTxell_expression_pos

    contains:
        "ped_motherOnTxell_eyebrow angryx01"
        ped_motherOnTxell_expression_pos

    contains:
        "ped_motherOnTxell_eyeShine"
        ped_motherOnTxell_expression_pos
        additive 1.0


#########
########


## PEDRERA SEX DIDAC: ORAL

#beach_sex_blow_comp Talkative_mast



label pedrera_general_kiss:

    if p_active == "p_didac":

        scene bg 01

        show kiss_ n_d_01:
            truecenter
            xzoom -1.0
            zoom 1.5
            rotate 50

    elif p_active == "p_neus":

        show bg_01

        show kiss_ n_n_01:
            truecenter
            xzoom -1.0
            zoom 1.5
            rotate 50

    return

label p_deyesp_check:

    if p_deyespCond == True: # Is it has to be changed?

        if p_active == "p_didac" and p_deyesp == "_rim":
            $ deyesp = "_rim"
        else:
            $ deyesp = ""

    else:

        if p_deyesp == "_rim":
            $ deyesp = "_rim"
        else:
            $ deyesp = ""

    return

default ped_sex_general_oral_list = ["o01_01", "o02_01", "o03_01", "o04_01", "o01_02", "o02_02", "o03_02", "o04_02", "o01_03", "o02_03", "o03_03", "o04_03", "o01_04", "o02_04", "o03_04", "o04_04", "o01_05", "o02_05", "o03_05", "o04_05"]

default ped_sex_general_lick_list = ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"]

    # if ped_sex_general_action_Cond in ["o01_01", "o02_01", "o03_01", "o04_01", "ob01_01", "ob02_01", "ob03_01", "ob04_01", "o00l_01"]:
    #         $ ped_sex_num = 1
    #     elif ped_sex_general_action_Cond in ["o01_02", "o02_02", "o03_02", "o04_02", "ob01_02", "ob02_02", "ob03_02", "ob04_02", "o00l_02"]:
    #         $ ped_sex_num = 2
    #     elif ped_sex_general_action_Cond in ["o01_03", "o02_03", "o03_03", "o04_03", "ob01_03", "ob02_03", "ob03_03", "ob04_03", "o00l_03"]:
    #         $ ped_sex_num = 3
    #     elif ped_sex_general_action_Cond in ["o01_04", "o02_04", "o03_04", "o04_04", "ob01_04", "ob02_04", "ob03_04", "ob04_04", "o00l_04"]:
    #         $ ped_sex_num = 4
    #     elif ped_sex_general_action_Cond in ["o01_05", "o02_05", "o03_05", "o04_05", "ob01_05", "ob02_05", "ob03_05", "ob04_05", "o00l_05"]:
    #         $ ped_sex_num = 5

label pedrera_sex_p_general_talk:

    $ p_deyespCond = True
    call p_deyesp_check
    # if p_deyesp == "_rim":
    #     $ deyesp = "_rim"
    # else:
    #     $ deyesp = ""

    call ped_sex_oral_blow_Check

    #scene bg 01 # old
    ## Background

    if pdaytime == "06morning":
        scene morning04_bg bedroom_neus_a
    elif pdaytime == "05_night_Pedrera":
        scene bg ped_04
    else:
        scene bg dark_a


    if p_active == "p_neus" and p_prot.pos == "missioanry":
        $ p_neuspos = "gensex_missionary_n_head_exp_"

    if p_active == "p_neus" and p_prot.pos == "oral":
        $ p_neuspos = "gensex_oral_n_frontHead_exp_"

    if p_prot.pos in ["missionary", "doggy"]:

        if ped_sex_general_action_Cond in ["v01_01", "v02_01", "a01_01", "a02_01", "vt01_01", "at01_01"]:
            $ ped_sex_num = 1
        elif ped_sex_general_action_Cond in ["v01_02", "v02_02", "a01_02", "a02_02", "vt01_02", "at01_02"]:
            $ ped_sex_num = 2
        elif ped_sex_general_action_Cond in ["v01_03", "v02_03", "a01_03", "a02_03", "vt01_03", "at01_03"]:
            $ ped_sex_num = 3
        elif ped_sex_general_action_Cond in ["v01_04", "v02_04", "a01_04", "a02_04", "vt01_04", "at01_04"]:
            $ ped_sex_num = 4
        elif ped_sex_general_action_Cond in ["v01_05", "v02_05", "a01_05", "a02_05", "vt01_05", "at01_05"]:
            $ ped_sex_num = 5

    if p_prot.pos == "oral":

        if ped_sex_general_action_Cond in ["o01_01", "o02_01", "o03_01", "o04_01", "ob01_01", "ob02_01", "ob03_01", "ob04_01", "o00l_01"]:
            $ ped_sex_num = 1
        elif ped_sex_general_action_Cond in ["o01_02", "o02_02", "o03_02", "o04_02", "ob01_02", "ob02_02", "ob03_02", "ob04_02", "o00l_02"]:
            $ ped_sex_num = 2
        elif ped_sex_general_action_Cond in ["o01_03", "o02_03", "o03_03", "o04_03", "ob01_03", "ob02_03", "ob03_03", "ob04_03", "o00l_03"]:
            $ ped_sex_num = 3
        elif ped_sex_general_action_Cond in ["o01_04", "o02_04", "o03_04", "o04_04", "ob01_04", "ob02_04", "ob03_04", "ob04_04", "o00l_04"]:
            $ ped_sex_num = 4
        elif ped_sex_general_action_Cond in ["o01_05", "o02_05", "o03_05", "o04_05", "ob01_05", "ob02_05", "ob03_05", "ob04_05", "o00l_05"]:
            $ ped_sex_num = 5
        else:
            $ ped_sex_num = 1

        # if p_active == "p_neus":
        #     show p_ao_ghost_standing_comp:
        #         truecenter
        #         zoom 0.5


        #if p_didac.action == "titwank_done":
        if ped_sex_general_action_Cond in ["ob00_00", "ob00_00b", "ob00_00c", "ob00_00d", "ob01_01", "ob01_02", "ob01_03", "ob01_04", "ob01_05"]:

            if p_active == "p_didac":
                show pedrera_sex_didac_oral boobjob_general:
                    subpixel True
                    truecenter
                    zoom 0.8 xpos 0.6 ypos 1.1
            elif p_active == "p_txell":
                show pedrera_sex_txell_oral boobjob_general:
                    subpixel True
                    truecenter
                    zoom 0.8 xpos 0.6 ypos 1.1
            elif p_active == "p_neus":
                show pedrera_sex_neus_oral boobjob_general:
                    subpixel True
                    truecenter
                    zoom 0.8 xpos 0.6 ypos 1.1
            call pedrera_sex_didac_general_expressions

        else:

            if p_active == "p_didac":
                if ped_sex_general_action_Cond in ["o04_xx", "o04_01", "o04_02", "o04_03", "o04_04", "o04_05"]:
                    if ped_sex_general_zoom_Cond == "faceCentered":
                        show pedrera_sex_didac_oral blowjob_general:
                            subpixel True
                            truecenter
                            #zoom 0.8 xpos 0.5 ypos 1.1 # Talkative pos?
                            zoom 1.3 xpos 0.5 ypos 1.0 # KUp
                            block:
                                ease 4.0/ped_sex_num zoom 1.5 ypos 0.5  # Down Throat
                                ease 4.0/ped_sex_num zoom 1.3 ypos 1.0 # Center_Up
                                repeat
                
                    #elif ped_sex_general_zoom_Cond == "face":
                    else:
                        show pedrera_sex_didac_oral blowjob_general:
                            subpixel True
                            truecenter
                            zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                            block:
                                ease 4.0/ped_sex_num zoom 1.3 xpos 0.65 ypos 0.7 # Down Throat
                                ease 4.0/ped_sex_num zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                                repeat

                elif ped_sex_general_action_Cond in ["o03_xx", "o03_01", "o03_02", "o03_03", "o03_04", "o03_05"]:

                    #if ped_sex_general_zoom_Cond == "face":
                    show pedrera_sex_didac_oral blowjob_general:
                        subpixel True
                        truecenter
                        zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                        block:
                            ease 4.0/ped_sex_num zoom 0.95 xpos 0.65 ypos 0.8 # Down Throat
                            ease 4.0/ped_sex_num zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                            repeat

                elif ped_sex_general_action_Cond in ["o02_xx", "o02_01", "o02_02", "o02_03", "o02_04", "o02_05"]:

                    #if ped_sex_general_zoom_Cond == "face":
                    show pedrera_sex_didac_oral blowjob_general:
                        subpixel True
                        truecenter
                        zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                        block:
                            ease 4.0/ped_sex_num zoom 0.9 xpos 0.625 ypos 1.0 # Down Throat
                            ease 4.0/ped_sex_num zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                            repeat

                elif ped_sex_general_action_Cond in ["o01_xx", "o01_01", "o01_02", "o01_03", "o01_04", "o01_05"]:

                    #if ped_sex_general_zoom_Cond == "face":
                    show pedrera_sex_didac_oral blowjob_general:
                        subpixel True
                        truecenter
                        zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                        block:
                            ease 4.0/ped_sex_num zoom 0.8 xpos 0.6 ypos 1.05 # Down Throat
                            ease 4.0/ped_sex_num zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                            repeat
                else:
                    if ped_sex_general_zoom_Cond == "talk_close":

                        show pedrera_sex_didac_oral blowjob_general:
                            truecenter
                            zoom 1.4 xpos 0.5 ypos 1.756 # talk_close
                            #zoom 1.5 ypos 0.5  # Down Throat
                    else:
                        show pedrera_sex_didac_oral blowjob_general:
                            truecenter
                            zoom 0.8 xpos 0.6 ypos 1.1

            elif p_active == "p_txell":

                if ped_sex_general_action_Cond in ["o04_xx", "o04_01", "o04_02", "o04_03", "o04_04", "o04_05"]:

                    if ped_sex_general_zoom_Cond == "faceCentered":
                        show pedrera_sex_txell_oral blowjob_general:
                            subpixel True
                            truecenter
                            #zoom 0.8 xpos 0.5 ypos 1.1 # Talkative pos?
                            zoom 1.3 xpos 0.5 ypos 1.0 # KUp
                            block:
                                ease 4.0/ped_sex_num zoom 1.5 ypos 0.5  # Down Throat
                                ease 4.0/ped_sex_num zoom 1.3 ypos 1.0 # Center_Up
                                repeat
                
                    #elif ped_sex_general_zoom_Cond == "face":
                    else:
                        show pedrera_sex_txell_oral blowjob_general:
                            subpixel True
                            truecenter
                            zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                            block:
                                ease 4.0/ped_sex_num zoom 1.3 xpos 0.65 ypos 0.7 # Down Throat
                                ease 4.0/ped_sex_num zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                                repeat

                elif ped_sex_general_action_Cond in ["o03_xx", "o03_01", "o03_02", "o03_03", "o03_04", "o03_05"]:

                    #if ped_sex_general_zoom_Cond == "face":
                    show pedrera_sex_txell_oral blowjob_general:
                        subpixel True
                        truecenter
                        zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                        block:
                            ease 4.0/ped_sex_num zoom 0.95 xpos 0.65 ypos 0.8 # Down Throat
                            ease 4.0/ped_sex_num zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                            repeat

                elif ped_sex_general_action_Cond in ["o02_xx", "o02_01", "o02_02", "o02_03", "o02_04", "o02_05"]:

                    #if ped_sex_general_zoom_Cond == "face":
                    show pedrera_sex_txell_oral blowjob_general:
                        subpixel True
                        truecenter
                        zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                        block:
                            ease 4.0/ped_sex_num zoom 0.9 xpos 0.625 ypos 1.0 # Down Throat
                            ease 4.0/ped_sex_num zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                            repeat

                elif ped_sex_general_action_Cond in ["o01_xx", "o01_01", "o01_02", "o01_03", "o01_04", "o01_05"]:

                    #if ped_sex_general_zoom_Cond == "face":
                    show pedrera_sex_txell_oral blowjob_general:
                        subpixel True
                        truecenter
                        zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                        block:
                            ease 4.0/ped_sex_num zoom 0.8 xpos 0.6 ypos 1.05 # Down Throat
                            ease 4.0/ped_sex_num zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                            repeat
                else:

                    show pedrera_sex_txell_oral blowjob_general:
                        truecenter
                        zoom 0.8 xpos 0.6 ypos 1.1


            elif p_active == "p_neus":

                #show day05 # NOT FINISHED

                if ped_sex_general_action_Cond in ["o_xx", "o04_01", "o04_02", "o04_03", "o04_04", "o04_05"]:

                    if ped_sex_general_zoom_Cond == "faceCentered":
                        show pedrera_sex_neus_oral blowjob_general:
                            subpixel True
                            truecenter
                            zoom 0.8 xpos 0.5 ypos 1.1 # KUp
                            block:
                                ease 4.0/ped_sex_num zoom 1.4 ypos 0.6 # Down Throat
                                ease 4.0/ped_sex_num zoom 0.8 ypos 1.1 # KUp
                                repeat

                    elif ped_sex_general_zoom_Cond == "faceCenteredClose":
                        show pedrera_sex_neus_oral blowjob_general:
                            subpixel True
                            truecenter
                            zoom 1.3 xpos 0.5 ypos 1.25 # KUp
                            block:
                                ease 4.0/ped_sex_num zoom 1.7 ypos 0.6 #
                                ease 4.0/ped_sex_num zoom 1.3 ypos 1.25 # KUp
                                repeat

                    else:
                        show pedrera_sex_neus_oral blowjob_general:
                            subpixel True
                            truecenter
                            zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                            block:
                                ease 4.0/ped_sex_num zoom 1.3 xpos 0.65 ypos 0.7 # Down Throat
                                ease 4.0/ped_sex_num zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                                repeat

                elif ped_sex_general_action_Cond in ["o03_xx", "o03_01", "o03_02", "o03_03", "o03_04", "o03_05"]:

                    if ped_sex_general_zoom_Cond == "faceCentered":
                        show pedrera_sex_neus_oral blowjob_general:
                            subpixel True
                            truecenter
                            zoom 0.8 xpos 0.5 ypos 1.1 # KUp
                            block:
                                ease 4.0/ped_sex_num zoom 0.95 ypos 0.8 # Down Throat
                                ease 4.0/ped_sex_num zoom 0.8 ypos 1.1 # KUp
                                repeat

                    elif ped_sex_general_zoom_Cond == "faceCenteredClose":
                        show pedrera_sex_neus_oral blowjob_general:
                            subpixel True
                            truecenter
                            zoom 1.3 xpos 0.5 ypos 1.25 # KUp
                            block:
                                ease 4.0/ped_sex_num zoom 1.5 ypos 0.8 #
                                ease 4.0/ped_sex_num zoom 1.3 ypos 1.25 # KUp
                                repeat
                    else:
                        show pedrera_sex_neus_oral blowjob_general:
                            subpixel True
                            truecenter
                            zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                            block:
                                ease 4.0/ped_sex_num zoom 0.95 xpos 0.65 ypos 0.8 # Down Throat
                                ease 4.0/ped_sex_num zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                                repeat

                elif ped_sex_general_action_Cond in ["o02_xx", "o02_01", "o02_02", "o02_03", "o02_04", "o02_05"]:

                    if ped_sex_general_zoom_Cond == "faceCentered":
                        show pedrera_sex_neus_oral blowjob_general:
                            subpixel True
                            truecenter
                            zoom 0.8 xpos 0.5 ypos 1.1 # KUp
                            block:
                                ease 4.0/ped_sex_num zoom 0.9 ypos 1.0 # Down Throat
                                ease 4.0/ped_sex_num zoom 0.8 ypos 1.1 # KUp
                                repeat

                    elif ped_sex_general_zoom_Cond == "faceCenteredClose":
                        show pedrera_sex_neus_oral blowjob_general:
                            subpixel True
                            truecenter
                            zoom 1.3 xpos 0.5 ypos 1.25 # KUp
                            block:
                                ease 4.0/ped_sex_num zoom 1.4 ypos 1.0 #
                                ease 4.0/ped_sex_num zoom 1.3 ypos 1.25 # KUp
                                repeat
                    else:
                        show pedrera_sex_neus_oral blowjob_general:
                            subpixel True
                            truecenter
                            zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                            block:
                                ease 4.0/ped_sex_num zoom 0.9 xpos 0.625 ypos 1.0 # Down Throat
                                ease 4.0/ped_sex_num zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                                repeat

                elif ped_sex_general_action_Cond in ["o01_xx", "o01_01", "o01_02", "o01_03", "o01_04", "o01_05"]:

                    if ped_sex_general_zoom_Cond == "faceCentered":
                        show pedrera_sex_neus_oral blowjob_general:
                            subpixel True
                            truecenter
                            #zoom 0.8 xpos 0.5 ypos 1.1 # Talkative pos?
                            zoom 0.8 xpos 0.5 ypos 1.1 # KUp
                            block:
                                ease 4.0/ped_sex_num zoom 0.85 ypos 1.08 #
                                ease 4.0/ped_sex_num zoom 0.8 ypos 1.1 # KUp
                                repeat

                    elif ped_sex_general_zoom_Cond == "faceCenteredClose":
                        show pedrera_sex_neus_oral blowjob_general:
                            subpixel True
                            truecenter
                            zoom 1.3 xpos 0.5 ypos 1.25 # KUp
                            block:
                                ease 4.0/ped_sex_num zoom 1.35 ypos 1.2 #
                                ease 4.0/ped_sex_num zoom 1.3 ypos 1.25 # KUp
                                repeat

                    else:
                        show pedrera_sex_neus_oral blowjob_general:
                            subpixel True
                            truecenter
                            zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                            block:
                                ease 4.0/ped_sex_num zoom 0.8 xpos 0.6 ypos 1.05 #
                                ease 4.0/ped_sex_num zoom 0.8 xpos 0.6 ypos 1.1 # KUp
                                repeat
                            
                else:

                    show pedrera_sex_neus_oral blowjob_general:
                        truecenter
                        zoom 0.8 xpos 0.6 ypos 1.1

            call pedrera_sex_didac_general_expressions

        

    elif p_prot.pos == "missionary":

        if ped_sex_general_zoom_Cond == "face":

            if p_active == "p_didac":
                show gensex_missionary_d_comp 02:
                    truecenter
                    zoom 1.5
                    ypos 1.35

            elif p_active == "p_neus":
                #show day05 # NOT FINISHED

                show gensex_missionary_n_comp 01:
                    truecenter
                    zoom 1.5
                    ypos 1.2

        elif ped_sex_general_zoom_Cond == "crotch":

            if p_active == "p_didac":
                show gensex_missionary_d_comp 02:
                    truecenter
                    zoom 1.5
                    ypos -0.25

            elif p_active == "p_neus":
                show gensex_missionary_n_comp 01:
                    truecenter
                    zoom 1.5
                    ypos -0.25

        else:

            if p_active == "p_didac":
                show gensex_missionary_d_comp 02:
                    truecenter
                    zoom 0.5

            elif p_active == "p_neus":
                show gensex_missionary_n_comp 01:
                    truecenter
                    zoom 0.5

        call pedrera_sex_didac_general_expressions



    elif p_prot.pos == "doggy":

        if ped_sex_general_zoom_Cond == "face":

            if p_active == "p_didac":
                show gensex_doggy_d_comp 01:
                    truecenter
                    zoom 0.9
                    ypos 1.9
            elif p_active == "p_neus":
                show gensex_doggy_n_comp 01:
                    truecenter
                    zoom 0.9
                    xpos 0.6
                    ypos 1.58

        elif ped_sex_general_zoom_Cond == "butt":

            if p_active == "p_didac":
                show gensex_doggy_d_comp 01:
                    truecenter
                    zoom 0.4
                    ypos 0.2
            elif p_active == "p_neus":
                show gensex_doggy_n_comp 01:
                    truecenter
                    zoom 0.4
                    ypos 0.2

        elif ped_sex_general_zoom_Cond == "crotch":

            if p_active == "p_didac":
                show gensex_doggy_d_comp 01:
                    truecenter
                    zoom 0.5
                    ypos 0.1
            elif p_active == "p_neus":
                #show day05 # NOT FINISHED
                show gensex_doggy_n_comp 01:
                    truecenter
                    zoom 0.5
                    ypos 0.1

        elif ped_sex_general_zoom_Cond == "ass":

            if p_active == "p_didac":
                show gensex_doggy_d_comp 01:
                    truecenter
                    zoom 1.5
                    ypos -0.35
            elif p_active == "p_neus":
                #show day05 # NOT FINISHED
                show gensex_doggy_n_comp 01:
                    truecenter
                    zoom 1.5
                    ypos -0.35

        elif ped_sex_general_zoom_Cond == "test":

            if p_active == "p_didac":
                show gensex_doggy_d_comp 01:
                    truecenter
                    zoom 1.0
                    ypos 0.5
            elif p_active == "p_neus":
                #show day05 # NOT FINISHED
                show gensex_doggy_n_comp 01:
                    truecenter
                    zoom 1.0
                    ypos 0.5

        elif ped_sex_general_zoom_Cond == "centered":

            if p_active == "p_didac":
                show gensex_doggy_d_comp 01:
                    truecenter
                    zoom 0.2 # Full Image
            elif p_active == "p_neus":
                #show day05 # NOT FINISHED
                show gensex_doggy_n_comp 01:
                    truecenter
                    zoom 0.2 # Full Image

        else:

            if p_active == "p_didac":
                show gensex_doggy_d_comp 01:
                    truecenter
                    zoom 0.2 # Full Image
                    xpos 0.62 # To Right
            elif p_active == "p_neus":
                # show gensex_doggy_n_comp 01:
                #     truecenter
                #     zoom 0.2 # Full Image
                #     xpos 0.62 # To Right

                show gensex_doggy_n_comp 01:
                    truecenter
                    zoom 0.28
                    ypos 0.52
                    xpos 0.62 # To Right


    elif p_prot.pos == "69":

        # LEFT PART

        if ped_sex_general_action_b_Cond in ["69b_00_01", "69b_01_01", "69b_02_01", "69b_03_01", "69b_04_01"]:
            $ ped_sex_b_num = 1
        elif ped_sex_general_action_b_Cond in ["69b_00_02", "69b_01_02", "69b_02_02", "69b_03_02", "69b_04_02"]:
            $ ped_sex_b_num = 2
        elif ped_sex_general_action_b_Cond in ["69b_00_03", "69b_01_03", "69b_02_03", "69b_03_03", "69b_04_03"]:
            $ ped_sex_b_num = 3
        elif ped_sex_general_action_b_Cond in ["69b_00_04", "69b_01_04", "69b_02_04", "69b_03_04", "69b_04_04"]:
            $ ped_sex_b_num = 4
        elif ped_sex_general_action_b_Cond in ["69b_00_05", "69b_01_05", "69b_02_05", "69b_03_05", "69b_04_05"]:
            $ ped_sex_b_num = 5

        # RIGHT PART

        if ped_sex_general_action_Cond in ["69_00_01", "69_01_01", "69_02_01", "69_03_01"]:
            $ ped_sex_num = 1
        elif ped_sex_general_action_Cond in ["69_00_02", "69_01_02", "69_02_02", "69_03_02"]:
            $ ped_sex_num = 2
        elif ped_sex_general_action_Cond in ["69_00_03", "69_01_03", "69_02_03", "69_03_03"]:
            $ ped_sex_num = 3
        elif ped_sex_general_action_Cond in ["69_00_04", "69_01_04", "69_02_04", "69_03_04"]:
            $ ped_sex_num = 4
        elif ped_sex_general_action_Cond in ["69_00_05", "69_01_05", "69_02_05", "69_03_05"]:
            $ ped_sex_num = 5


        scene ped_sex_69_compe_01:
            truecenter
            zoom 0.5

        # LEFT PART after SCENE

        if ped_sex_general_expression_Cond == "talk":
            show gensex_69_L_d_mouth sadbiting_Silentx02:
                gensex_69_L_d_mouth_pos

    return


transform pedrera_sex_buttSmack_base_pos:
    subpixel True
    additive 1.0
    zoom 0.01 rotate 25
    parallel:
        easein 0.6 zoom 0.5
    parallel:
        ease 0.5 rotate 40
    parallel:
        ease 0.45 alpha 0.0

transform pedrera_sex_buttSmack_inverse_pos:
    subpixel True
    additive 1.0
    zoom 0.01 rotate -25
    parallel:
        easein 0.6 zoom 0.5
    parallel:
        ease 0.5 rotate -40
    parallel:
        ease 0.45 alpha 0.0


label pedrera_sex_didac_general_expressions:

    call p_neus_orgasmHurry_label

    if p_prot.pos == "oral":

        if p_active == "p_didac":

            show gensex_oral_d_frontHead_exp_mouth empty:
                pedrera_sex_didac_general_speaking_exp_pos

            if ped_sex_general_expression_Cond == "talk":
                show gensex_oral_d_frontHead_exp_blush 01:
                    pedrera_sex_didac_general_speaking_exp_pos
                    
            show gensex_oral_d_frontHead_exp_eyes empty:
                pedrera_sex_didac_general_speaking_exp_pos
            show gensex_oral_d_frontHead_exp_iris empty:
                pedrera_sex_didac_general_speaking_exp_pos
            show gensex_oral_d_frontHead_exp_mouth_b empty:
                pedrera_sex_didac_general_speaking_exp_pos
            show gensex_oral_d_frontHead_exp_eyebrows empty:
                pedrera_sex_didac_general_speaking_exp_pos

            if ped_sex_general_expression_Cond == "talk":
                show gensex_oral_d_frontHead_hair:
                    pedrera_sex_didac_general_speaking_exp_pos
            else:
                show gensex_oral_d_frontHead_hair empty:
                    pedrera_sex_didac_general_speaking_exp_pos

            if ped_sex_general_zoom_Cond == "talk_close":
                show gensex_oral_d_frontHead_exp_mouth empty:
                    pedrera_sex_didac_general_speaking_close_exp_pos
                show gensex_oral_d_frontHead_exp_blush 01:
                    pedrera_sex_didac_general_speaking_close_exp_pos

                show gensex_oral_d_frontHead_exp_eyes empty:
                    pedrera_sex_didac_general_speaking_close_exp_pos
                show gensex_oral_d_frontHead_exp_iris empty:
                    pedrera_sex_didac_general_speaking_close_exp_pos
                show gensex_oral_d_frontHead_exp_mouth_b empty:
                    pedrera_sex_didac_general_speaking_close_exp_pos
                show gensex_oral_d_frontHead_exp_eyebrows empty:
                    pedrera_sex_didac_general_speaking_close_exp_pos

                show gensex_oral_d_frontHead_hair:
                    pedrera_sex_didac_general_speaking_close_exp_pos


        elif p_active == "p_txell":

            show gensex_oral_m_frontHead_exp_mouth empty:
                pedrera_sex_didac_general_speaking_exp_pos

            if ped_sex_general_expression_Cond == "talk":
                show gensex_oral_m_frontHead_exp_blush 01:
                    pedrera_sex_didac_general_speaking_exp_pos
                    
            show gensex_oral_m_frontHead_exp_eyes empty:
                pedrera_sex_didac_general_speaking_exp_pos
            show gensex_oral_m_frontHead_exp_iris empty:
                pedrera_sex_didac_general_speaking_exp_pos
            show gensex_oral_m_frontHead_exp_mouth_b empty:
                pedrera_sex_didac_general_speaking_exp_pos
            show gensex_oral_m_frontHead_exp_eyebrows empty:
                pedrera_sex_didac_general_speaking_exp_pos

            if ped_sex_general_expression_Cond == "talk":
                show gensex_oral_m_frontHead_hair:
                    pedrera_sex_didac_general_speaking_exp_pos
            else:
                show gensex_oral_m_frontHead_hair empty:
                    pedrera_sex_didac_general_speaking_exp_pos

        elif p_active == "p_neus":

            if ped_sex_general_zoom_Cond == "faceCentered":

                show gensex_oral_n_frontHead_exp_mouth empty:
                    pedrera_sex_didac_general_speakingCentered_exp_pos

                if ped_sex_general_expression_Cond == "talk":
                    show gensex_oral_n_frontHead_exp_blush 01:
                        pedrera_sex_didac_general_speakingCentered_exp_pos
                        
                show gensex_oral_n_frontHead_exp_eyes empty:
                    pedrera_sex_didac_general_speakingCentered_exp_pos
                show gensex_oral_n_frontHead_exp_iris empty:
                    pedrera_sex_didac_general_speakingCentered_exp_pos
                show gensex_oral_n_frontHead_exp_l_iris empty:
                    pedrera_sex_didac_general_speakingCentered_exp_pos
                    alpha 1.0
                show gensex_oral_n_frontHead_exp_tears empty:
                    pedrera_sex_didac_general_speakingCentered_exp_pos
                show gensex_oral_n_frontHead_exp_iLight empty:
                    pedrera_sex_didac_general_speakingCentered_exp_pos
                    additive 1.0
                # show gensex_oral_n_frontHead_exp_mouth_b empty:
                #     pedrera_sex_didac_general_speakingCentered_exp_pos
                show gensex_oral_n_frontHead_exp_eyebrows empty:
                    pedrera_sex_didac_general_speakingCentered_exp_pos

                if ped_sex_general_expression_Cond == "talk":

                    if n_withoutGlasses_story == False and n_withoutGlasses_Cond == False:
                        show gensex_oral_n_frontHead_glasses:
                            pedrera_sex_didac_general_speakingCentered_exp_pos
                    else:
                        show gensex_oral_n_frontHead_glasses empty:
                            pedrera_sex_didac_general_speakingCentered_exp_pos


                if ped_sex_general_expression_Cond == "talk":
                    show gensex_oral_n_frontHead_hair:
                        pedrera_sex_didac_general_speakingCentered_exp_pos
                else:
                    show gensex_oral_n_frontHead_hair empty:
                        pedrera_sex_didac_general_speakingCentered_exp_pos


            else:

                show gensex_oral_n_frontHead_exp_mouth empty:
                    pedrera_sex_didac_general_speaking_exp_pos

                if ped_sex_general_expression_Cond == "talk":
                    show gensex_oral_n_frontHead_exp_blush 01:
                        pedrera_sex_didac_general_speaking_exp_pos
                        
                show gensex_oral_n_frontHead_exp_eyes empty:
                    pedrera_sex_didac_general_speaking_exp_pos
                show gensex_oral_n_frontHead_exp_iris empty:
                    pedrera_sex_didac_general_speaking_exp_pos
                show gensex_oral_n_frontHead_exp_l_iris empty:
                    pedrera_sex_didac_general_speaking_exp_pos
                    alpha 1.0
                show gensex_oral_n_frontHead_exp_tears empty:
                    pedrera_sex_didac_general_speaking_exp_pos
                show gensex_oral_n_frontHead_exp_iLight empty:
                    pedrera_sex_didac_general_speaking_exp_pos
                    additive 1.0
                # show gensex_oral_n_frontHead_exp_mouth_b empty:
                #     pedrera_sex_didac_general_speaking_exp_pos
                show gensex_oral_n_frontHead_exp_eyebrows empty:
                    pedrera_sex_didac_general_speaking_exp_pos

                # if n_withoutGlasses_story == False and n_withoutGlasses_Cond == False:
                #     show gensex_oral_n_frontHead_glasses:
                #         pedrera_sex_didac_general_speaking_exp_pos

                if ped_sex_general_expression_Cond == "talk":

                    if n_withoutGlasses_story == False and n_withoutGlasses_Cond == False:
                        show gensex_oral_n_frontHead_glasses:
                            pedrera_sex_didac_general_speaking_exp_pos
                    else:
                        show gensex_oral_n_frontHead_glasses empty:
                            pedrera_sex_didac_general_speaking_exp_pos

                if ped_sex_general_expression_Cond == "talk":
                    show gensex_oral_n_frontHead_hair:
                        pedrera_sex_didac_general_speaking_exp_pos
                else:
                    show gensex_oral_n_frontHead_hair empty:
                        pedrera_sex_didac_general_speaking_exp_pos

    elif p_prot.pos == "missionary":

        if ped_sex_general_zoom_Cond == "face":

            if p_active == "p_didac":

                if ped_sex_general_expression_Cond == "talk" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_blush 02:
                        ped_missionary02_d_exp_face_pos
                else:
                    show gensex_missionary_d_head_exp_blush empty:
                        ped_missionary02_d_exp_face_pos
                show gensex_missionary_d_head_exp_eyes empty:
                    ped_missionary02_d_exp_face_pos
                show gensex_missionary_d_head_exp_pupils empty:
                    ped_missionary02_d_exp_face_pos
                show gensex_missionary_d_head_exp_eyebrows empty:
                    ped_missionary02_d_exp_face_pos
                show gensex_missionary_d_head_exp_mouth empty:
                    ped_missionary02_d_exp_face_pos

                if ped_sex_general_expression_Cond == "talk" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_hairfront:
                        ped_missionary02_d_exp_face_pos
                else:
                    show gensex_missionary_d_head_hairfront empty:
                        ped_missionary02_d_exp_face_pos

            elif p_active == "p_neus":

                #pass # NOT FINISHED

                if ped_sex_general_expression_Cond == "talk":
                    show gensex_missionary_n_head_exp_blush 02:
                        ped_missionary02_n_exp_face_pos
                else:
                    show gensex_missionary_n_head_exp_blush empty:
                        ped_missionary02_n_exp_face_pos
                show gensex_missionary_n_head_exp_eyes empty:
                    ped_missionary02_n_exp_face_pos

                ## IRIS
                show gensex_missionary_n_head_exp_iris empty:
                    ped_missionary02_n_exp_face_pos
                # show expression "gensex_missionary_n_head_exp_iris " + n_exp_Cond:
                #     ped_missionary02_n_exp_face_pos

                ## IRIS VIOLET
                show gensex_missionary_n_head_exp_l_iris empty:
                    ped_missionary02_n_exp_face_pos
                    #alpha p_neus.closeOrgasm/50
                # show expression "gensex_missionary_n_head_exp_l_iris " + n_exp_Cond:
                #     ped_missionary02_n_exp_face_pos
                #     alpha p_neus.closeOrgasm/50

                ## TEARS
                show gensex_missionary_n_head_exp_tears empty:
                    ped_missionary02_n_exp_face_pos

                ## IRIS LIGHT
                show gensex_missionary_n_head_exp_iLight empty:
                    ped_missionary02_n_exp_face_pos
                    additive 1.0
                #     alpha p_neus.closeOrgasm/50
                # show expression "gensex_missionary_n_head_exp_iLight " + n_exp_Cond:
                #     ped_missionary02_n_exp_face_pos
                #     additive 1.0
                #     alpha p_neus.closeOrgasm/50

                show gensex_missionary_n_head_exp_eyebrows empty:
                    ped_missionary02_n_exp_face_pos
                show gensex_missionary_n_head_exp_mouth empty:
                    ped_missionary02_n_exp_face_pos

                if ped_sex_general_expression_Cond == "talk":
                    show gensex_missionary_n_head_glasses:
                        ped_missionary02_n_exp_face_pos
                    show gensex_missionary_n_head_hairfront:
                        ped_missionary02_n_exp_face_pos
                else:
                    show gensex_missionary_n_head_glasses:
                        ped_missionary02_n_exp_face_pos

                    show gensex_missionary_n_head_hairfront bullshit:
                        ped_missionary02_n_exp_face_pos

        elif ped_sex_general_zoom_Cond == "":

            if p_active == "p_didac":

                if ped_sex_general_expression_Cond == "talk" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_blush 02:
                        ped_missionary02_d_exp_zoom05_pos
                else:
                    show gensex_missionary_d_head_exp_blush empty:
                        ped_missionary02_d_exp_zoom05_pos
                show gensex_missionary_d_head_exp_eyes empty:
                    ped_missionary02_d_exp_zoom05_pos
                show gensex_missionary_d_head_exp_pupils empty:
                    ped_missionary02_d_exp_zoom05_pos
                show gensex_missionary_d_head_exp_eyebrows empty:
                    ped_missionary02_d_exp_zoom05_pos
                show gensex_missionary_d_head_exp_mouth empty:
                    ped_missionary02_d_exp_zoom05_pos
                if ped_sex_general_expression_Cond == "talk" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_hairfront:
                        ped_missionary02_d_exp_zoom05_pos
                else:
                    show gensex_missionary_d_head_hairfront empty:
                        ped_missionary02_d_exp_zoom05_pos

            elif p_active == "p_neus":

                #pass # NOT FINISHED

                if ped_sex_general_expression_Cond == "talk":
                    show gensex_missionary_n_head_exp_blush 02:
                        ped_missionary02_n_exp_zoom05_pos
                else:
                    show gensex_missionary_n_head_exp_blush empty:
                        ped_missionary02_n_exp_zoom05_pos
                show gensex_missionary_n_head_exp_eyes empty:
                    ped_missionary02_n_exp_zoom05_pos


                ## IRIS
                show gensex_missionary_n_head_exp_iris empty:
                    ped_missionary02_n_exp_zoom05_pos
                # show expression "gensex_missionary_n_head_exp_iris " + n_exp_Cond:
                #     ped_missionary02_n_exp_zoom05_pos

                ## IRIS VIOLET
                show gensex_missionary_n_head_exp_l_iris empty:
                    ped_missionary02_n_exp_zoom05_pos
                #     alpha p_neus.closeOrgasm/50
                # show expression "gensex_missionary_n_head_exp_l_iris " + n_exp_Cond:
                #     ped_missionary02_n_exp_zoom05_pos
                #     alpha p_neus.closeOrgasm/50

                ## TEARS
                show gensex_missionary_n_head_exp_tears empty:
                    ped_missionary02_n_exp_zoom05_pos
                ## IRIS LIGHT

                show gensex_missionary_n_head_exp_iLight empty:
                    ped_missionary02_n_exp_zoom05_pos
                    additive 1.0
                #     alpha p_neus.closeOrgasm/50
                # show expression "gensex_missionary_n_head_exp_iLight " + n_exp_Cond:
                #     ped_missionary02_n_exp_zoom05_pos
                #     additive 1.0
                #     alpha p_neus.closeOrgasm/50

                show gensex_missionary_n_head_exp_eyebrows empty:
                    ped_missionary02_n_exp_zoom05_pos
                show gensex_missionary_n_head_exp_mouth empty:
                    ped_missionary02_n_exp_zoom05_pos
                if ped_sex_general_expression_Cond == "talk":
                    show gensex_missionary_n_head_glasses:
                        ped_missionary02_n_exp_zoom05_pos
                    show gensex_missionary_n_head_hairfront:
                        ped_missionary02_n_exp_zoom05_pos
                else:
                    show gensex_missionary_n_head_glasses empty:
                        ped_missionary02_n_exp_zoom05_pos
                    show gensex_missionary_n_head_hairfront bullshit:
                        ped_missionary02_n_exp_zoom05_pos

    return

####################################################
####################################################
####################################################

####################################################
####################################################



# label n_exp_label:

#     ## EYES

#     #call p_neus_exp_eyes_string

#     ###

#     if nteye in ["front00", "right00", "left00", "up00", "down00"]:
#         show gensex_missionary_n_head_exp_eyes 00

#     elif nteye in ["front01", "right01", "left01", "up01", "down01"]:
#         show gensex_missionary_n_head_exp_eyes 01

#     elif nteye in ["front02", "right02", "left02", "up02", "down02"]:
#         show gensex_missionary_n_head_exp_eyes 02

#     elif nteye in ["front03", "right03", "left03", "up03", "down03"]:
#         show gensex_missionary_n_head_exp_eyes 03

#     elif nteye in ["front04", "right04", "left04", "up04", "down04"]:
#         show gensex_missionary_n_head_exp_eyes 04

#     elif nteye in ["front05", "right05", "left05", "up05", "down05"]:
#         show gensex_missionary_n_head_exp_eyes 05

#     elif nteye in ["front06", "right06", "left06", "up06", "down06"]:
#         show gensex_missionary_n_head_exp_eyes 06

#     elif nteye in ["front07", "right07", "left07", "up07", "down07"]:
#         show gensex_missionary_n_head_exp_eyes 07

#     elif nteye in ["front08", "right08", "left08", "up08", "down08"]:
#         show gensex_missionary_n_head_exp_eyes 08

#     ## TEARS

#     call n_exp_max

#     if nteye in ["front00", "right00", "left00", "up00", "down00"]:

#         if ntlong == 1:
#             show gensex_missionary_n_head_exp_tears 00_01
#         elif ntlong == 2:
#             show gensex_missionary_n_head_exp_tears 00_02
#         elif ntlong == 3:
#             show gensex_missionary_n_head_exp_tears 00_03
#         elif ntlong == 4:
#             show gensex_missionary_n_head_exp_tears 00_04
#         elif ntlong == 5:
#             show gensex_missionary_n_head_exp_tears 00_05

#     elif nteye in ["front01", "right01", "left01", "up01", "down01"]:
#         if ntlong == 1:
#             show gensex_missionary_n_head_exp_tears 01_01
#         elif ntlong == 2:
#             show gensex_missionary_n_head_exp_tears 01_02
#         elif ntlong == 3:
#             show gensex_missionary_n_head_exp_tears 01_03
#         elif ntlong == 4:
#             show gensex_missionary_n_head_exp_tears 01_04
#         elif ntlong == 5:
#             show gensex_missionary_n_head_exp_tears 01_05

#     elif nteye in ["front02", "right02", "left02", "up02", "down02"]:
#         if ntlong == 1:
#             show gensex_missionary_n_head_exp_tears 02_01
#         elif ntlong == 2:
#             show gensex_missionary_n_head_exp_tears 02_02
#         elif ntlong == 3:
#             show gensex_missionary_n_head_exp_tears 02_03
#         elif ntlong == 4:
#             show gensex_missionary_n_head_exp_tears 02_04
#         elif ntlong == 5:
#             show gensex_missionary_n_head_exp_tears 02_05

#     elif nteye in ["front03", "right03", "left03", "up03", "down03"]:
#         if ntlong == 1:
#             show gensex_missionary_n_head_exp_tears 03_01
#         elif ntlong == 2:
#             show gensex_missionary_n_head_exp_tears 03_02
#         elif ntlong == 3:
#             show gensex_missionary_n_head_exp_tears 03_03
#         elif ntlong == 4:
#             show gensex_missionary_n_head_exp_tears 03_04
#         elif ntlong == 5:
#             show gensex_missionary_n_head_exp_tears 03_05

#     elif nteye in ["front04", "right04", "left04", "up04", "down04"]:
#         if ntlong == 1:
#             show gensex_missionary_n_head_exp_tears 04_01
#         elif ntlong == 2:
#             show gensex_missionary_n_head_exp_tears 04_02
#         elif ntlong == 3:
#             show gensex_missionary_n_head_exp_tears 04_03
#         elif ntlong == 4:
#             show gensex_missionary_n_head_exp_tears 04_04
#         elif ntlong == 5:
#             show gensex_missionary_n_head_exp_tears 04_05

#     elif nteye in ["front05", "right05", "left05", "up05", "down05"]:
#         if ntlong == 1:
#             show gensex_missionary_n_head_exp_tears 05_01
#         elif ntlong == 2:
#             show gensex_missionary_n_head_exp_tears 05_02
#         elif ntlong == 3:
#             show gensex_missionary_n_head_exp_tears 05_03
#         elif ntlong == 4:
#             show gensex_missionary_n_head_exp_tears 05_04
#         elif ntlong == 5:
#             show gensex_missionary_n_head_exp_tears 05_05

#     elif nteye in ["front06", "right06", "left06", "up06", "down06"]:
#         if ntlong == 1:
#             show gensex_missionary_n_head_exp_tears 06_01
#         elif ntlong == 2:
#             show gensex_missionary_n_head_exp_tears 06_02
#         elif ntlong == 3:
#             show gensex_missionary_n_head_exp_tears 06_03
#         elif ntlong == 4:
#             show gensex_missionary_n_head_exp_tears 06_04
#         elif ntlong == 5:
#             show gensex_missionary_n_head_exp_tears 06_05

#     elif nteye in ["front07", "right07", "left07", "up07", "down07"]:
#         if ntlong == 1:
#             show gensex_missionary_n_head_exp_tears 07_01
#         elif ntlong == 2:
#             show gensex_missionary_n_head_exp_tears 07_02
#         elif ntlong == 3:
#             show gensex_missionary_n_head_exp_tears 07_03
#         elif ntlong == 4:
#             show gensex_missionary_n_head_exp_tears 07_04
#         elif ntlong == 5:
#             show gensex_missionary_n_head_exp_tears 07_05

#     elif nteye in ["front08", "right08", "left08", "up08", "down08"]:
#         if ntlong == 1:
#             show gensex_missionary_n_head_exp_tears 08_01
#         elif ntlong == 2:
#             show gensex_missionary_n_head_exp_tears 08_02
#         elif ntlong == 3:
#             show gensex_missionary_n_head_exp_tears 08_03
#         elif ntlong == 4:
#             show gensex_missionary_n_head_exp_tears 08_04
#         elif ntlong == 5:
#             show gensex_missionary_n_head_exp_tears 08_05
#     else:
#         show gensex_missionary_n_head_exp_tears empty

#     ## IRIS
#     show expression "gensex_missionary_n_head_exp_iris " + nteye

#     ## IRIS VIOLET
#     show expression "gensex_missionary_n_head_exp_l_iris " + nteye

#     ## IRIS LIGHT
#     show expression "gensex_missionary_n_head_exp_iLight " + nteye

#     #show gensex_missionary_n_head_exp_iris + [n_exp_Cond]

#     # show gensex_missionary_n_head_exp_tears 06_05
#     # show gensex_missionary_n_head_exp_iLight empty
#     # show gensex_missionary_n_head_exp_l_iris front06

#     return


####################################################
####################################################
####################################################

####################################################
####################################################


transform gensex_oral_mc_handmast_top_anim01:
    subpixel True
    truecenter
    ypos 0.6
    block:
        ease 0.5 ypos 0.15
        ease 0.5 ypos 0.6
        repeat


####################################################
####################################################
####################################################

####################################################
####################################################

## LEGS UP?

transform ped05_sex_oral_d_legs_down_action:
    truecenter
    ypos 0.3
transform ped05_sex_oral_n_legs_down_action:
    truecenter
    ypos 0.3

transform ped05_sex_oral_d_legs_up_00_00:
    truecenter
    ypos 0.0
transform ped05_sex_oral_n_legs_up_00_00:
    truecenter
    ypos -0.15

transform ped05_sex_oral_d_legs_up_00_00b:
    truecenter
    ypos 0.05

transform ped05_sex_oral_d_legs_up_04_00:
    truecenter
    ypos 0.5
transform ped05_sex_oral_n_legs_up_04_00:
    truecenter
    ypos 0.3


####################################################
## BLOWJOB 01_   BLOWING JUST THE TIP OF THE GLANS.

####################
####################
#################### BLOWJOB TIP GLANS (TOP)


transform ped05_sex_oral_d_frontHead_blow_over_o01_xx:
    subpixel True
    "gensex_oral_d_frontHead_exp_mouth_b_blow_over 03"
    truecenter
    ypos -0.4 # up
    parallel:
        ease 4.0/ped_sex_num ypos -0.34 # down
        ease 4.0/ped_sex_num ypos -0.4 # up
        repeat
    parallel:
        pause 2.0/ped_sex_num 
        "gensex_oral_d_frontHead_exp_mouth_b_blow_over 04" # with Dissolve(0.5)
        pause 4.0/ped_sex_num
        "gensex_oral_d_frontHead_exp_mouth_b_blow_over 03" # with Dissolve(0.5)
        pause 2.0/ped_sex_num
        repeat

image ped05_sex_oral_d_frontHead_blow_over_im_o01_xx:
    contains:
        "gensex_oral_d_frontHead_exp_mouth_b_blow_over 03"
        subpixel True
        truecenter
        ypos -0.4 # up
        parallel:
            ease 4.0/ped_sex_num ypos -0.34 # down
            ease 4.0/ped_sex_num ypos -0.4 # up
            repeat
        parallel:
            pause 2.0/ped_sex_num 
            "gensex_oral_d_frontHead_exp_mouth_b_blow_over 04" with Dissolve(0.5/ped_sex_num)
            pause 4.0/ped_sex_num
            "gensex_oral_d_frontHead_exp_mouth_b_blow_over 03" with Dissolve(0.5/ped_sex_num)
            pause 2.0/ped_sex_num
            repeat

#################### BLOWJOB TIP GLANS (BELOW)

transform ped05_sex_oral_d_frontHead_blow_below_o01_xx:
    subpixel True
    "gensex_oral_d_frontHead_exp_mouth_b_blow_below 03"
    truecenter
    ypos -0.4 # up
    parallel:
        ease 4.0/ped_sex_num ypos -0.34 # down
        ease 4.0/ped_sex_num ypos -0.4 # up
        repeat
    parallel:
        pause 2.0/ped_sex_num 
        "gensex_oral_d_frontHead_exp_mouth_b_blow_below 04" # with Dissolve(0.5)
        pause 4.0/ped_sex_num 
        "gensex_oral_d_frontHead_exp_mouth_b_blow_below 03" # with Dissolve(0.5)
        pause 2.0/ped_sex_num
        repeat

image ped05_sex_oral_d_frontHead_blow_below_im_o01_xx:
    contains:
        "gensex_oral_d_frontHead_exp_mouth_b_blow_below 03"
        subpixel True
        truecenter
        ypos -0.4 # up
        parallel:
            ease 4.0/ped_sex_num ypos -0.34 # down
            ease 4.0/ped_sex_num ypos -0.4 # up
            repeat
        parallel:
            pause 2.0/ped_sex_num 
            "gensex_oral_d_frontHead_exp_mouth_b_blow_below 04" with Dissolve(0.5/ped_sex_num)
            pause 4.0/ped_sex_num 
            "gensex_oral_d_frontHead_exp_mouth_b_blow_below 03" with Dissolve(0.5/ped_sex_num)
            pause 2.0/ped_sex_num
            repeat

####################################################

####################################################
## BLOWJOB 02_   BLOWING WHOLE GLANS.


transform ped05_sex_oral_d_frontHead_blow_over_o02_xx:
    subpixel True
    "gensex_oral_d_frontHead_exp_mouth_b_blow_over 04"
    truecenter
    ypos -0.4 # up
    parallel:
        # ease 4.0/ped_sex_num ypos -0.1 # down
        # ease 4.0/ped_sex_num ypos -0.32 # up

        ease 4.0/ped_sex_num ypos -0.1 # down
        ease 4.0/ped_sex_num ypos -0.36 # up
        repeat
    parallel:
        pause 0.5/ped_sex_num
        "gensex_oral_d_frontHead_exp_mouth_b_blow_over 05" # with Dissolve(0.5)
        pause 6.5/ped_sex_num
        "gensex_oral_d_frontHead_exp_mouth_b_blow_over 04" # with Dissolve(0.5)
        pause 1.0/ped_sex_num
        repeat

image ped05_sex_oral_d_frontHead_blow_over_im_o02_xx:
    contains:
        "gensex_oral_d_frontHead_exp_mouth_b_blow_over 04"
        subpixel True
        truecenter
        ypos -0.4 # up
        parallel:
            ease 4.0/ped_sex_num ypos -0.1 # down
            ease 4.0/ped_sex_num ypos -0.36 # up
            repeat
        parallel:
            pause 0.5/ped_sex_num
            "gensex_oral_d_frontHead_exp_mouth_b_blow_over 05" with Dissolve(0.5/ped_sex_num)
            pause 6.5/ped_sex_num
            "gensex_oral_d_frontHead_exp_mouth_b_blow_over 04" with Dissolve(0.5/ped_sex_num)
            pause 1.0/ped_sex_num
            repeat

#################### BLOWJOB 02 WHOLE GLANS (BELOW)

transform ped05_sex_oral_d_frontHead_blow_below_o02_xx:
    subpixel True
    "gensex_oral_d_frontHead_exp_mouth_b_blow_below 04"
    truecenter
    ypos -0.4 # up
    parallel:
        ease 4.0/ped_sex_num ypos -0.1 # down
        ease 4.0/ped_sex_num ypos -0.36 # up
        repeat
    parallel:
        pause 0.5/ped_sex_num 
        "gensex_oral_d_frontHead_exp_mouth_b_blow_below 05" # with Dissolve(0.5)
        pause 6.5/ped_sex_num 
        "gensex_oral_d_frontHead_exp_mouth_b_blow_below 04" # with Dissolve(0.5)
        pause 1.0/ped_sex_num
        repeat

image ped05_sex_oral_d_frontHead_blow_below_im_o02_xx:
    contains:
        
        "gensex_oral_d_frontHead_exp_mouth_b_blow_below 04"
        subpixel True
        truecenter
        ypos -0.4 # up
        parallel:
            ease 4.0/ped_sex_num ypos -0.1 # down
            ease 4.0/ped_sex_num ypos -0.36 # up
            repeat
        parallel:
            pause 0.5/ped_sex_num 
            "gensex_oral_d_frontHead_exp_mouth_b_blow_below 05" with Dissolve(0.5/ped_sex_num)
            pause 6.5/ped_sex_num 
            "gensex_oral_d_frontHead_exp_mouth_b_blow_below 04" with Dissolve(0.5/ped_sex_num)
            pause 1.0/ped_sex_num
            repeat

####################################################

####################################################
## BLOWJOB 03_   BLOWING HALF (OVER)

transform ped05_sex_oral_d_frontHead_blow_over_o03_xx:
    subpixel True
    "gensex_oral_d_frontHead_exp_mouth_b_blow_over 04"
    truecenter
    ypos -0.4 # up
    parallel:
        ease 4.0/ped_sex_num ypos 0.1 # down
        ease 4.0/ped_sex_num ypos -0.36 # up
        repeat
    parallel:
        pause 0.4/ped_sex_num
        "gensex_oral_d_frontHead_exp_mouth_b_blow_over 05" # with Dissolve(0.5)
        pause 6.6/ped_sex_num
        "gensex_oral_d_frontHead_exp_mouth_b_blow_over 04" # with Dissolve(0.5)
        pause 1.0/ped_sex_num
        repeat

image ped05_sex_oral_d_frontHead_blow_over_im_o03_xx:
    contains:
        "gensex_oral_d_frontHead_exp_mouth_b_blow_over 04"
        subpixel True
        truecenter
        ypos -0.4 # up
        parallel:
            ease 4.0/ped_sex_num ypos 0.1 # down
            ease 4.0/ped_sex_num ypos -0.36 # up
            repeat
        parallel:
            pause 0.4/ped_sex_num
            "gensex_oral_d_frontHead_exp_mouth_b_blow_over 05" with Dissolve(0.5/ped_sex_num)
            pause 6.6/ped_sex_num
            "gensex_oral_d_frontHead_exp_mouth_b_blow_over 04" with Dissolve(0.5/ped_sex_num)
            pause 1.0/ped_sex_num
            repeat

####################################################
# BELOW 03
transform ped05_sex_oral_d_frontHead_blow_below_o03_xx:
    subpixel True 
    "gensex_oral_d_frontHead_exp_mouth_b_blow_below 04"
    truecenter
    ypos -0.4 # up
    parallel:
        ease 4.0/ped_sex_num ypos 0.1 # down
        ease 4.0/ped_sex_num ypos -0.36 # up
        repeat
    parallel:
        pause 0.4/ped_sex_num 
        "gensex_oral_d_frontHead_exp_mouth_b_blow_below 05" # with Dissolve(0.5)
        pause 6.6/ped_sex_num 
        "gensex_oral_d_frontHead_exp_mouth_b_blow_below 04" # with Dissolve(0.5)
        pause 1.0/ped_sex_num
        repeat
image ped05_sex_oral_d_frontHead_blow_below_im_o03_xx:
    contains:
        
        "gensex_oral_d_frontHead_exp_mouth_b_blow_below 04"
        subpixel True 
        truecenter
        ypos -0.4 # up
        parallel:
            ease 4.0/ped_sex_num ypos 0.1 # down
            ease 4.0/ped_sex_num ypos -0.36 # up
            repeat
        parallel:
            pause 0.4/ped_sex_num 
            "gensex_oral_d_frontHead_exp_mouth_b_blow_below 05" with Dissolve(0.5/ped_sex_num)
            pause 6.6/ped_sex_num 
            "gensex_oral_d_frontHead_exp_mouth_b_blow_below 04" with Dissolve(0.5/ped_sex_num)
            pause 1.0/ped_sex_num
            repeat

####################################################

####################################################
## BLOWJOB 04_   DEEPTHROAT. (OVER)

transform ped05_sex_oral_d_frontHead_blow_over_o04_xx:
    subpixel True
    "gensex_oral_d_frontHead_exp_mouth_b_blow_over 04"
    truecenter
    ypos -0.4 # up
    parallel:
        ease 4.0/ped_sex_num ypos 0.4 # down (?)
        ease 4.0/ped_sex_num ypos -0.36 # up
        repeat
    parallel:
        pause 0.4/ped_sex_num
        "gensex_oral_d_frontHead_exp_mouth_b_blow_over 05" # with Dissolve(0.5)
        pause 6.6/ped_sex_num
        "gensex_oral_d_frontHead_exp_mouth_b_blow_over 04" # with Dissolve(0.5)
        pause 1.0/ped_sex_num
        repeat

image ped05_sex_oral_d_frontHead_blow_over_im_o04_xx:
    contains:
        "gensex_oral_d_frontHead_exp_mouth_b_blow_over 04"
        subpixel True
        truecenter
        ypos -0.4 # up
        parallel:
            ease 4.0/ped_sex_num ypos 0.4 # down (?)
            ease 4.0/ped_sex_num ypos -0.36 # up
            repeat
        parallel:
            pause 0.4/ped_sex_num
            "gensex_oral_d_frontHead_exp_mouth_b_blow_over 05" with Dissolve(0.5/ped_sex_num)
            pause 6.6/ped_sex_num
            "gensex_oral_d_frontHead_exp_mouth_b_blow_over 04" with Dissolve(0.5/ped_sex_num)
            pause 1.0/ped_sex_num
            repeat
#########################
# BELOW 04
transform ped05_sex_oral_d_frontHead_blow_below_o04_xx:
    subpixel True
    "gensex_oral_d_frontHead_exp_mouth_b_blow_below 04"
    truecenter
    ypos -0.4 # up
    parallel:
        ease 4.0/ped_sex_num ypos 0.4 # down
        ease 4.0/ped_sex_num ypos -0.36 # up
        repeat
    parallel:
        pause 0.4/ped_sex_num 
        "gensex_oral_d_frontHead_exp_mouth_b_blow_below 05" # with Dissolve(0.5)
        pause 6.6/ped_sex_num 
        "gensex_oral_d_frontHead_exp_mouth_b_blow_below 04" # with Dissolve(0.5)
        pause 1.0/ped_sex_num
        repeat

image ped05_sex_oral_d_frontHead_blow_below_im_o04_xx:
    contains:
        "gensex_oral_d_frontHead_exp_mouth_b_blow_below 04"
        subpixel True
        truecenter
        ypos -0.4 # up
        parallel:
            ease 4.0/ped_sex_num ypos 0.4 # down
            ease 4.0/ped_sex_num ypos -0.36 # up
            repeat
        parallel:
            pause 0.4/ped_sex_num 
            "gensex_oral_d_frontHead_exp_mouth_b_blow_below 05" with Dissolve(0.5/p_ao_n_vel)
            pause 6.6/ped_sex_num 
            "gensex_oral_d_frontHead_exp_mouth_b_blow_below 04" with Dissolve(0.5/p_ao_n_vel)
            pause 1.0/ped_sex_num
            repeat

####################################################

####################################################
## BLOWJOB 00l_   LICKING?

transform ped05_sex_oral_d_frontHead_o00l_xx:
    subpixel True
    truecenter
    ypos -0.4 # up
    block:
        ease 4.0/ped_sex_num  ypos 0.1 # down
        ease 4.0/ped_sex_num  ypos -0.4 # up
        repeat

####
#### What the fuck is this shit?

transform ped05_sex_oral_d_body_o00l_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2
    # ypos -0.1
    ypos -0.2 # up
    block:
        ease 4.0/ped_sex_num  ypos 0.0 # down
        ease 4.0/ped_sex_num  ypos -0.2 # up
        repeat

####
####

transform ped05_sex_oral_d_hand_o00l_xx:
    subpixel True
    truecenter
    ypos 0.6
    block:
        ease 2.0/ped_sex_num  ypos 0.5 # half
        ease 2.0/ped_sex_num  ypos 0.6 # down
        repeat

####################################################

####################################################
## BLOWJOB 01_   BLOWING JUST THE TIP OF THE GLANS.

transform ped05_sex_oral_d_frontHead_o01_xx:
    subpixel True
    truecenter
    ypos -0.4 # up
    parallel:
        ease 4.0/ped_sex_num  ypos -0.34 # down
        ease 4.0/ped_sex_num  ypos -0.4 # up
        repeat

####
####

transform ped05_sex_oral_d_body_o01_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2
    # ypos -0.1
    ypos -0.2 # up
    parallel:
        ease 4.0/ped_sex_num  ypos -0.1 # down
        ease 4.0/ped_sex_num  ypos -0.2 # up
        repeat

####
####

transform ped05_sex_oral_d_hairback_o01_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2
    # ypos -0.1
    ypos -0.2 # up
    parallel:
        ease 4.0/ped_sex_num  ypos -0.05 # down
        ease 4.0/ped_sex_num  ypos -0.15 # up
        repeat

####################################################

####################################################
## BLOWJOB 02_   BLOWING THE WHOLE GLANS.

transform ped05_sex_oral_d_frontHead_o02_xx:
    subpixel True
    truecenter
    ypos -0.4 # up
    parallel:
        ease 4.0/ped_sex_num  ypos -0.1 # down
        ease 4.0/ped_sex_num  ypos -0.36 # up
        repeat

####
####

transform ped05_sex_oral_d_body_o02_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2
    ypos -0.2 # up
    parallel:
        ease 4.0/ped_sex_num  ypos -0.1 # down
        ease 4.0/ped_sex_num  ypos -0.2 # up
        repeat


####
####

transform ped05_sex_oral_d_hairback_o02_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2
    ypos -0.2 # up
    parallel:
        ease 4.0/ped_sex_num  ypos -0.05 # down
        ease 4.0/ped_sex_num  ypos -0.15 # up
        repeat

####
####

# Are they the same? # NOT FINISHED
transform ped05_sex_oral_d_hand_o01_xx:
    subpixel True 
    truecenter
    ypos 0.6
    block:
        ease 4.0/ped_sex_num  ypos 0.55 # half
        ease 4.0/ped_sex_num  ypos 0.6 # down
        repeat

transform ped05_sex_oral_d_hand_o02_xx:
    subpixel True
    truecenter
    ypos 0.6
    block:
        ease 4.0/ped_sex_num  ypos 0.5 # half
        ease 4.0/ped_sex_num  ypos 0.6 # down
        repeat

####################################################

####################################################
## HALF DICK 03_  HALF DICK

transform ped05_sex_oral_d_frontHead_o03_xx:
    subpixel True
    truecenter
    ypos -0.4 # up
    parallel:
        ease 4.0/ped_sex_num  ypos 0.1 # down
        ease 4.0/ped_sex_num  ypos -0.36 # up
        repeat

####
####

transform ped05_sex_oral_d_body_o03_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2
    ypos -0.2 # up
    parallel:
        ease 4.0/ped_sex_num  ypos 0.1 # down
        ease 4.0/ped_sex_num  ypos -0.2 # up
        repeat

####
####

transform ped05_sex_oral_d_hairback_o03_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2
    # ypos -0.1
    ypos -0.2 # up
    parallel:
        ease 4.0/ped_sex_num ypos 0.05 # down
        ease 4.0/ped_sex_num ypos -0.15 # up
        repeat

####
####

transform ped05_sex_oral_d_hand_o03_xx:
    subpixel True
    truecenter
    ypos 0.5
    block:
        ease 4.0/ped_sex_num  ypos 0.65 # down
        ease 4.0/ped_sex_num  ypos 0.5 # half
        repeat


####################################################
## DEEPTHROAT 04_ (NOT DONE IN THE BEACH SCENE.)


transform ped05_sex_oral_d_frontHead_o04_xx:
    subpixel True
    truecenter
    ypos -0.4 # up
    parallel:
        ease 4.0/ped_sex_num  ypos 0.4 # down
        ease 4.0/ped_sex_num  ypos -0.36 # up
        repeat

####
####

transform ped05_sex_oral_d_body_o04_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2
    ypos -0.2 # up
    parallel:
        ease 4.0/ped_sex_num  ypos 0.25 # down
        ease 4.0/ped_sex_num  ypos -0.2 # up
        repeat

####
####

transform ped05_sex_oral_d_hairback_o04_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2
    ypos -0.2 # up
    parallel:
        ease 4.0/ped_sex_num  ypos 0.30 # down
        ease 4.0/ped_sex_num  ypos -0.15 # up
        repeat

####################################################
####################################################
####################################################

####################################################
#################################################### DICK TEASING

transform ped05_sex_oral_d_dick_o00_xx:
    subpixel True
    truecenter
    ypos 0.6
    parallel:
        ease 4.0/ped_sex_num  ypos 0.5
        ease 4.8/ped_sex_num  ypos 0.6
        repeat
    parallel:
        ease 4.2/ped_sex_num  rotate 2
        ease 4.8/ped_sex_num  rotate -2
        repeat

###
###


transform ped05_sex_oral_d_dick_o00_00: # Stop Dick
    truecenter
    ypos 0.8

transform ped05_sex_oral_d_dick_ob00_00: # Stop Dick on Boobjob
    truecenter
    ypos 0.8


transform ped05_sex_oral_d_dick_o_soft: # Soft
    truecenter
    ypos 0.8
    xzoom 0.6 yzoom 0.4

transform ped05_sex_oral_d_frontHead_o00_00:
    truecenter
    ypos -0.59

transform ped05_sex_oral_d_frontHead_ob00_00:
    truecenter
    ypos -0.59



####################################################
####################################################
####################################################

####################################################
#################################################### ## BOOBJOB f (originally 01)

transform ped05_sex_oral_d_frontHead_ob01_xx:
    subpixel True
    truecenter
    #ypos -0.59
    ypos -0.4
    block:
        ease 4.0/ped_sex_num  ypos -0.6
        ease 4.0/ped_sex_num  ypos -0.4
        repeat

    ##

transform ped05_sex_oral_d_body_o00_00:
    transform_anchor True
    xalign 0.5 yalign 0.2
    ypos -0.55

# transform ped05_sex_oral_m_body_o00_00:
#     transform_anchor True
#     xalign 0.5 yalign 0.1
#     ypos -0.5

    ## BLOWJOB



    ## BOOBJOB

transform ped05_sex_oral_d_body_ob01_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.2
    #ypos -0.55
    ypos -0.45
    block:
        ease 4.0/ped_sex_num  ypos -0.6
        ease 4.0/ped_sex_num  ypos -0.45
        repeat

    ##

# transform ped05_sex_oral_d_dick_ob00_00:
#     truecenter
#     ypos 0.8

transform ped05_sex_oral_d_dick_ob01_xx:
    subpixel True # Not sure if this is gonna work in his particular case.
    truecenter
    ypos 0.8
    block:
        pause 3.0/ped_sex_num 
        "gensex_oral_mc_dick_02_wet_00" # with Dissolve(0.6)
        pause 0.8/ped_sex_num 
        "gensex_oral_mc_dick_03_wet_00" # with Dissolve(0.4)
        pause 0.8/ped_sex_num 
        "gensex_oral_mc_dick_02_wet_00" # with Dissolve(0.4)
        pause 1.2/ped_sex_num 
        "gensex_oral_mc_dick_01_wet_00" # with Dissolve(0.6)
        pause 2.2/ped_sex_num 
        repeat

    ## BOOBJOB _04 (originally 02)

#transform gensex_oral_d_frontHead_pos_Boobjob_02:

transform ped05_sex_oral_d_frontHead_ob01_xx:
    subpixel True # Is this ok?!

    truecenter
    #ypos -0.59
    ypos -0.25
    block:
        ease 4.0/ped_sex_num  ypos -0.65
        ease 4.0/ped_sex_num  ypos -0.25
        repeat

# transform ped05_sex_oral_d_frontHead_ob01_04:

#     truecenter
#     #ypos -0.59
#     ypos -0.25
#     block:
#         ease 0.5 ypos -0.65
#         ease 0.5 ypos -0.25
#         repeat

transform ped05_sex_oral_d_body_ob01_xx:
    subpixel True # Not sure about this one Neither # NOT FINISHED

    transform_anchor True
    xalign 0.5 yalign 0.2
    #ypos -0.55
    ypos -0.3
    block:
        ease 4.0/ped_sex_num  ypos -0.65
        ease 4.0/ped_sex_num  ypos -0.3
        repeat

# transform ped05_sex_oral_d_body_ob01_04:

#     transform_anchor True
#     xalign 0.5 yalign 0.2
#     #ypos -0.55
#     ypos -0.3
#     block:
#         ease 0.5 ypos -0.65
#         ease 0.5 ypos -0.3
#         repeat

    ## LEGS BLOWJOB

transform ped05_sex_oral_d_legs_o00_00:
    truecenter
    ypos 0.0

transform ped05_sex_oral_d_legs_ob00_00:
    truecenter
    ypos 0.45



####################################################
####################################################
####################################################

####################################################
####################################################

image pedrera_sex_didac_oral blowjob_general: # BLOWJOB  DIDAC

 ###Ground
    contains:
        #if p_ao_started #This is After ORGASM! and not pdaytime == "06morning":
        ConditionSwitch(
            # ped_sex_general_action_Cond in ["talk", "o00_00", "o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("gensex_oral_bg_ground_noShadow", p_ao_oral_ground_trans),
            p_bg == "bed_mcRoom", At("bg_ped_04", p_ao_oral_ground_trans),
            "True", At("gensex_oral_bg_ground_noShadow", p_ao_oral_ground_zoom_052trans))

## BED (bgOverLayer)
    contains:
        ConditionSwitch(
            p_bg == "bed_mcRoom", At("gensex_oral_bg_grounddownMiddle_bed_light", p_ao_oral_ground_zoom_052trans),
            "True", Null())

##~D LEGS
    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["o00_00"], At("gensex_oral_d_legs up", ped05_sex_oral_d_legs_up_00_00),
            ped_sex_general_action_Cond in ["talk", "o00_00", "o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("gensex_oral_d_legs up", ped05_sex_oral_d_legs_up_00_00b),

            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04"], At("gensex_oral_d_legs down", ped05_sex_oral_d_legs_up_04_00),

            ped_sex_blow_Cond == True, At("gensex_oral_d_legs down", ped05_sex_oral_d_legs_up_04_00),

            "True", At("gensex_oral_d_legs down", ped05_sex_oral_d_legs_down_action)
            )

    # contains:
    #     "gensex_oral_d_legs down"
    #     truecenter
    #     ypos 0.0

# D BODY
    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("gensex_oral_d_down_body", ped05_sex_oral_d_body_o04_xx),
            
            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_d_down_body", ped05_sex_oral_d_body_o03_xx),
            
            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_d_down_body", ped05_sex_oral_d_body_o02_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_d_down_body", ped05_sex_oral_d_body_o01_xx),

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_d_down_body", ped05_sex_oral_d_body_o00l_xx),

            ped_sex_general_action_Cond in ["o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("gensex_oral_d_down_body", ped05_sex_oral_d_body_o00_00),
            "True", At("gensex_oral_d_down_body", ped05_sex_oral_d_body_o00_00)
            )

# D HAIR OVER DOWN
    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("gensex_oral_d_hairOver_down", ped05_sex_oral_d_frontHead_o04_xx),
            
            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_d_hairOver_down", ped05_sex_oral_d_frontHead_o03_xx),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_d_hairOver_down", ped05_sex_oral_d_frontHead_o02_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_d_hairOver_down", ped05_sex_oral_d_frontHead_o01_xx),

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_d_hairOver_down", ped05_sex_oral_d_frontHead_o00l_xx),

            ped_sex_general_action_Cond in ["o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("gensex_oral_d_hairOver_down", ped05_sex_oral_d_frontHead_o00_00),


            "True", At("gensex_oral_d_hairOver_down", ped05_sex_oral_d_frontHead_o00_00)
            )

# D FACE Lick?
    contains:
        ConditionSwitch(
            ped_sex_blow_Cond == True, Null(),

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_d_frontHead_face", ped05_sex_oral_d_frontHead_o00l_xx),

            "True", At("gensex_oral_d_frontHead_face", ped05_sex_oral_d_frontHead_o00_00)
            )

# # # D JAW BELOW (for BlowJob)

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("ped05_sex_oral_d_frontHead_blow_below_im_o04_xx", truecenter),

            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("ped05_sex_oral_d_frontHead_blow_below_im_o03_xx", truecenter),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("ped05_sex_oral_d_frontHead_blow_below_im_o02_xx", truecenter),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("ped05_sex_oral_d_frontHead_blow_below_im_o01_xx", truecenter),

            "True", Null()
            )

# D HAND BOTTOM

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_d_down_hand_mast_bot_slim", ped05_sex_oral_d_hand_o03_xx),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_d_down_hand_mast_bot_slim", ped05_sex_oral_d_hand_o02_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_d_down_hand_mast_bot_slim", ped05_sex_oral_d_hand_o01_xx),

            "True", Null()
            )

# MC DICK FOR SUCKING.
    
    contains:
        ConditionSwitch(
            ped_sex_blow_Cond == True, At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_d_dick_o00_00),
            "True", Null()
            )

# D HAND TOP

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_d_down_hand_mast_top", ped05_sex_oral_d_hand_o03_xx),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_d_down_hand_mast_top", ped05_sex_oral_d_hand_o02_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_d_down_hand_mast_top", ped05_sex_oral_d_hand_o01_xx),

            "True", Null()
            )

# FrontHead BLOW OVER

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("ped05_sex_oral_d_frontHead_blow_over_im_o04_xx", truecenter),
            
            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("ped05_sex_oral_d_frontHead_blow_over_im_o03_xx", truecenter),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("ped05_sex_oral_d_frontHead_blow_over_im_o02_xx", truecenter),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("ped05_sex_oral_d_frontHead_blow_over_im_o01_xx", truecenter),

            "True", Null()
            )

    # EXPRESSIONS

    contains:
        ConditionSwitch(
            ped_sex_general_expression_Cond == "talk", Null(),

            ped_sex_general_action_Cond in ["o00_00", "o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o00_00),

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02","o00l_03","o00l_04","o00l_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o00l_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o01_xx),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o02_xx),

            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o03_xx),

            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o04_xx),

            "True", Null()
            )

        # FRONT HAIR

    contains:
        ConditionSwitch(

            ped_sex_general_expression_Cond == "talk", Null(),

            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("gensex_oral_d_frontHead_hair", ped05_sex_oral_d_frontHead_o04_xx),

            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_d_frontHead_hair", ped05_sex_oral_d_frontHead_o03_xx),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_d_frontHead_hair", ped05_sex_oral_d_frontHead_o02_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_d_frontHead_hair", ped05_sex_oral_d_frontHead_o01_xx),

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_d_frontHead_hair", ped05_sex_oral_d_frontHead_o00l_xx),

            "True", At("gensex_oral_d_frontHead_hair", ped05_sex_oral_d_frontHead_o00_00)
            )

# D HAND BOTTOM_B

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_d_down_hand_mast_bot_slim", ped05_sex_oral_d_hand_o02_xx),

            "True", Null()
            )

# MC_Dick_B

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_d_dick_o00_xx),

            ped_sex_blow_Cond == True, Null(),

            "True", At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_d_dick_o00_00)
            )

# D HAND TOP_B

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_d_down_hand_mast_top", ped05_sex_oral_d_hand_o02_xx),

            "True", Null()
            )

    contains:
        ConditionSwitch(
            p_prot.action == "masturbate", At("gensex_oral_mc_handmast_top", gensex_oral_mc_handmast_top_anim01),
            "True", Null()
            )

## MC_BODY

    contains:
        "gensex_oral_mc_body_02"
        truecenter
        ypos 0.65

## MC_Chest
        
    contains:
        "gensex_oral_mc_chest"
        truecenter
        ypos 0.65

## MC HAND

    contains:
        ConditionSwitch(

            ped_sex_blow_MChand == "on" and ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_mc_handonherhead", ped05_sex_oral_mc_handOverHead_o02_xx),
            
            ped_sex_blow_MChand == "on" and ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_mc_handonherhead", ped05_sex_oral_mc_handOverHead_o03_xx),
            
            ped_sex_blow_MChand == "on" and ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("gensex_oral_mc_handonherhead", ped05_sex_oral_mc_handOverHead_o04_xx),

            "True", Null()
            )

    # contains:
    #     "gensex_oral_mc_handonherhead"
    #     ped05_sex_oral_mc_handOverHead_o04_04



####################################################
####################################################
####################################################

####################################################
#################################################### MERITXELL

image pedrera_sex_txell_oral blowjob_general: # BLOWJOB 

 ###Ground
    contains:
        #if p_ao_started #This is After ORGASM! and not pdaytime == "06morning":
        ConditionSwitch(
            # ped_sex_general_action_Cond in ["talk", "o00_00", "o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("gensex_oral_bg_ground_noShadow", p_ao_oral_ground_trans),
            "True", At("gensex_oral_bg_ground_noShadow", p_ao_oral_ground_zoom_052trans))

# M LEGS
    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["talk", "o00_00", "o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("gensex_oral_m_legs up", ped05_sex_oral_d_legs_up_00_00),

            ped_sex_blow_Cond == True, At("gensex_oral_m_legs down", ped05_sex_oral_d_legs_up_04_00),

            "True", At("gensex_oral_m_legs down", ped05_sex_oral_d_legs_down_action)
            )

# M BODY
    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("gensex_oral_m_down_body", ped05_sex_oral_d_body_o04_xx),
            
            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_m_down_body", ped05_sex_oral_d_body_o03_xx),
            
            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_m_down_body", ped05_sex_oral_d_body_o02_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_m_down_body", ped05_sex_oral_d_body_o01_xx),

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_m_down_body", ped05_sex_oral_d_body_o00l_xx),

            ped_sex_general_action_Cond in ["o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("gensex_oral_m_down_body", ped05_sex_oral_d_body_o00_00),
            "True", At("gensex_oral_m_down_body", ped05_sex_oral_d_body_o00_00)
            )

# M HAIR OVER DOWN
    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("gensex_oral_m_frontHead_hairBack", ped05_sex_oral_d_frontHead_o04_xx),
            
            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_m_frontHead_hairBack", ped05_sex_oral_d_frontHead_o03_xx),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_m_frontHead_hairBack", ped05_sex_oral_d_frontHead_o02_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_m_frontHead_hairBack", ped05_sex_oral_d_frontHead_o01_xx),

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_m_frontHead_hairBack", ped05_sex_oral_d_frontHead_o00l_xx),

            ped_sex_general_action_Cond in ["o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("gensex_oral_m_frontHead_hairBack", ped05_sex_oral_d_frontHead_o00_00),


            "True", At("gensex_oral_m_frontHead_hairBack", ped05_sex_oral_d_frontHead_o00_00)
            )

# M FACE Lick?
    contains:
        ConditionSwitch(
            ped_sex_blow_Cond == True, Null(),

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_m_frontHead_face", ped05_sex_oral_d_frontHead_o00l_xx),

            "True", At("gensex_oral_m_frontHead_face", ped05_sex_oral_d_frontHead_o00_00)
            )

# # # M JAW BELOW (for BlowJob)

    # contains:
    #     ConditionSwitch(
    #         ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("gensex_oral_m_frontHead_exp_mouth_b_blow_below 04", ped05_sex_oral_d_frontHead_blow_below_o04_xx),

    #         ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_m_frontHead_exp_mouth_b_blow_below 04", ped05_sex_oral_d_frontHead_blow_below_o03_xx),

    #         ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_m_frontHead_exp_mouth_b_blow_below 04", ped05_sex_oral_d_frontHead_blow_below_o02_xx),

    #         ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_m_frontHead_exp_mouth_b_blow_below 04", ped05_sex_oral_d_frontHead_blow_below_o01_xx),

    #         "True", Null()
    #         )

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("ped05_sex_oral_d_frontHead_blow_below_im_o04_xx", truecenter),

            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("ped05_sex_oral_d_frontHead_blow_below_im_o03_xx", truecenter),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("ped05_sex_oral_d_frontHead_blow_below_im_o02_xx", truecenter),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("ped05_sex_oral_d_frontHead_blow_below_im_o01_xx", truecenter),

            "True", Null()
            )

# M HAND BOTTOM

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_m_down_hand_mast_bot", ped05_sex_oral_d_hand_o03_xx),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_m_down_hand_mast_bot", ped05_sex_oral_d_hand_o02_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_m_down_hand_mast_bot", ped05_sex_oral_d_hand_o01_xx),

            "True", Null()
            )

# MC DICK FOR SUCKING.
    
    contains:
        ConditionSwitch(
            ped_sex_blow_Cond == True, At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_d_dick_o00_00),
            "True", Null()
            )

# M HAND TOP

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_m_down_hand_mast_top", ped05_sex_oral_d_hand_o03_xx),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_m_down_hand_mast_top", ped05_sex_oral_d_hand_o02_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_m_down_hand_mast_top", ped05_sex_oral_d_hand_o01_xx),

            "True", Null()
            )

# FrontHead BLOW OVER

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("ped05_sex_oral_d_frontHead_blow_over_im_o04_xx", truecenter),
            
            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("ped05_sex_oral_d_frontHead_blow_over_im_o03_xx", truecenter),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("ped05_sex_oral_d_frontHead_blow_over_im_o02_xx", truecenter),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("ped05_sex_oral_d_frontHead_blow_over_im_o01_xx", truecenter),

            "True", Null()
            )

    # EXPRESSIONS

    contains:
        ConditionSwitch(
            ped_sex_general_expression_Cond == "talk", Null(),

            ped_sex_general_action_Cond in ["o00_00", "o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o00_00),

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02","o00l_03","o00l_04","o00l_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o00l_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o01_xx),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o02_xx),

            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o03_xx),

            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o04_xx),

            "True", Null()
            )

        # FRONT HAIR

    contains:
        ConditionSwitch(

            ped_sex_general_expression_Cond == "talk", Null(),

            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("gensex_oral_m_frontHead_hair", ped05_sex_oral_d_frontHead_o04_xx),

            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_m_frontHead_hair", ped05_sex_oral_d_frontHead_o03_xx),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_m_frontHead_hair", ped05_sex_oral_d_frontHead_o02_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_m_frontHead_hair", ped05_sex_oral_d_frontHead_o01_xx),

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_m_frontHead_hair", ped05_sex_oral_d_frontHead_o00l_xx),

            "True", At("gensex_oral_m_frontHead_hair", ped05_sex_oral_d_frontHead_o00_00)
            )

# M HAND BOTTOM_B

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_m_down_hand_mast_bot", ped05_sex_oral_d_hand_o02_xx),

            "True", Null()
            )

# MC_Dick_B

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_d_dick_o00_xx),

            ped_sex_blow_Cond == True, Null(),

            "True", At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_d_dick_o00_00)
            )

# D HAND TOP_B

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_m_down_hand_mast_top", ped05_sex_oral_d_hand_o02_xx),

            "True", Null()
            )

    contains:
        ConditionSwitch(
            p_prot.action == "masturbate", At("gensex_oral_mc_handmast_top", gensex_oral_mc_handmast_top_anim01),
            "True", Null()
            )

## MC_BODY

    contains:
        "gensex_oral_mc_body_02"
        truecenter
        ypos 0.65

## MC_Chest
        
    contains:
        "gensex_oral_mc_chest"
        truecenter
        ypos 0.65

## MC HAND

    contains:
        ConditionSwitch(

            ped_sex_blow_MChand == "on" and ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_mc_handonherhead", ped05_sex_oral_mc_handOverHead_o02_xx),
            
            ped_sex_blow_MChand == "on" and ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_mc_handonherhead", ped05_sex_oral_mc_handOverHead_o03_xx),
            
            ped_sex_blow_MChand == "on" and ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("gensex_oral_mc_handonherhead", ped05_sex_oral_mc_handOverHead_o04_xx),

            "True", Null()
            )

    # contains:
    #     "gensex_oral_mc_handonherhead"
    #     ped05_sex_oral_mc_handOverHead_o04_04

####################################################
####################################################
####################################################

####################################################
####################################################


####################################################
####################################################
####################################################

####################################################
#################################################### NEUS BLOWJOB

# image pedrera_sex_neus_oral blowjob_general: # BLOWJOB
    
#     contains:
#         "day05"
#         truecenter
#         zoom 2.0

transform p_ao_oral_ground_trans:
    truecenter
    #Image 800x600
    #zoom 0.8 xpos 0.6 ypos 1.1 # this is blowjob is moved.
    zoom 2.0
    xpos 0.38 ypos -0.25 # Good Center! # 0= Down / 3=Up


transform p_ao_oral_ground_zoom_052trans:
    truecenter
    #####zoom 0.8 xpos 0.6 ypos 1.1 # this is blowjob is moved.
    #zoom 0.52
    #xpos 0.38 ypos -0.25 # Good Center! # 0= Down / 3=Up
    zoom 0.63 xpos 0.5 ypos -0.25


transform p_ao_oral_ghostsPos:
    truecenter
    zoom 1.8 ypos 0.15

image pedrera_sex_neus_oral blowjob_general: # BLOWJOB
    
 ###Ground
    contains:
        #if p_ao_started #This is After ORGASM! and not pdaytime == "06morning":
        ConditionSwitch(
            p_ao_background == "pedrera", At("bg_ped_04", p_ao_oral_ground_trans),
            # ped_sex_general_action_Cond in ["talk", "o00_00", "o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("gensex_oral_bg_ground_noShadow", p_ao_oral_ground_zoom_052trans),
            "True", At("gensex_oral_bg_ground_noShadow", p_ao_oral_ground_zoom_052trans))


# Ghosts # If there's ground, ghosts are not necessary.

    contains:
        ConditionSwitch(
            p_ao_background == "pedrera", Null(),
            p_ao_background == "ground", Null(),
            "True", At("p_ao_ghost_standing_comp", p_ao_oral_ghostsPos))
    # contains:
    #     "p_ao_ghost_standing_comp"
    #     truecenter
    #     zoom 1.8 ypos 0.15

# M LEGS
    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["talk", "o00_00", "o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("gensex_oral_n_legs up", ped05_sex_oral_n_legs_up_00_00),

            ped_sex_blow_Cond == True, At("gensex_oral_n_legs down", ped05_sex_oral_n_legs_up_04_00),

            "True", At("gensex_oral_n_legs down", ped05_sex_oral_n_legs_down_action)
            )

# N HAIR BEHIND?
    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("gensex_oral_n_boobJob_body_hair", ped05_sex_oral_d_body_o04_xx),
            
            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_n_boobJob_body_hair", ped05_sex_oral_d_body_o03_xx),
            
            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_n_boobJob_body_hair", ped05_sex_oral_d_body_o02_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_n_boobJob_body_hair", ped05_sex_oral_d_body_o01_xx),

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_n_boobJob_body_hair", ped05_sex_oral_d_body_o00l_xx),

            ped_sex_general_action_Cond in ["o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("gensex_oral_n_boobJob_body_hair", ped05_sex_oral_d_body_o00_00),
            "True", At("gensex_oral_n_boobJob_body_hair", ped05_sex_oral_d_body_o00_00)
            )

# N BODY
    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("gensex_oral_n_down_body", ped05_sex_oral_d_body_o04_xx),
            
            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_n_down_body", ped05_sex_oral_d_body_o03_xx),
            
            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_n_down_body", ped05_sex_oral_d_body_o02_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_n_down_body", ped05_sex_oral_d_body_o01_xx),

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_n_down_body", ped05_sex_oral_d_body_o00l_xx),

            ped_sex_general_action_Cond in ["o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("gensex_oral_n_down_body", ped05_sex_oral_d_body_o00_00),
            "True", At("gensex_oral_n_down_body", ped05_sex_oral_d_body_o00_00)
            )

# N HAIR over Shoulders.
    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("gensex_oral_n_frontHead_hair_back_ground", ped05_sex_oral_d_frontHead_o04_xx),
            
            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_n_frontHead_hair_back_ground", ped05_sex_oral_d_frontHead_o03_xx),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_n_frontHead_hair_back_ground", ped05_sex_oral_d_frontHead_o02_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_n_frontHead_hair_back_ground", ped05_sex_oral_d_frontHead_o01_xx),

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_n_frontHead_hair_back_ground", ped05_sex_oral_d_frontHead_o00l_xx),

            ped_sex_general_action_Cond in ["o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("gensex_oral_n_frontHead_hair_back_ground", ped05_sex_oral_d_frontHead_o00_00),


            "True", At("gensex_oral_n_frontHead_hair_back_ground", ped05_sex_oral_d_frontHead_o00_00)
            )

# N EARS
    contains:
        ConditionSwitch(
            ped_sex_blow_Cond == True, Null(),

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_n_frontHead_ears down", ped05_sex_oral_d_frontHead_o00l_xx),

            "True", At("gensex_oral_n_frontHead_ears down", ped05_sex_oral_d_frontHead_o00_00)
            )

# N FACE Lick?
    contains:
        ConditionSwitch(
            ped_sex_blow_Cond == True, Null(),

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_n_frontHead_face", ped05_sex_oral_d_frontHead_o00l_xx),

            "True", At("gensex_oral_n_frontHead_face", ped05_sex_oral_d_frontHead_o00_00)
            )

# # # M JAW BELOW (for BlowJob)

    # contains:
    #     ConditionSwitch(
    #         ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("gensex_oral_n_frontHead_exp_mouth_b_blow_below 05", ped05_sex_oral_d_frontHead_blow_below_o04_xx),

    #         ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_n_frontHead_exp_mouth_b_blow_below 03", ped05_sex_oral_d_frontHead_blow_below_o03_xx),

    #         ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_n_frontHead_exp_mouth_b_blow_below 02", ped05_sex_oral_d_frontHead_blow_below_o02_xx),

    #         ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_n_frontHead_exp_mouth_b_blow_below 01", ped05_sex_oral_d_frontHead_blow_below_o01_xx),

    #         "True", Null()
    #         )

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("ped05_sex_oral_d_frontHead_blow_below_im_o04_xx", truecenter),

            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("ped05_sex_oral_d_frontHead_blow_below_im_o03_xx", truecenter),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("ped05_sex_oral_d_frontHead_blow_below_im_o02_xx", truecenter),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("ped05_sex_oral_d_frontHead_blow_below_im_o01_xx", truecenter),

            "True", Null()
            )

# M HAND BOTTOM

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_n_down_hand_mast_bot", ped05_sex_oral_d_hand_o03_xx),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_n_down_hand_mast_bot", ped05_sex_oral_d_hand_o02_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_n_down_hand_mast_bot", ped05_sex_oral_d_hand_o01_xx),

            "True", Null()
            )

# MC DICK FOR SUCKING.
    
    contains:
        ConditionSwitch(
            ped_sex_blow_Cond == True, At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_d_dick_o00_00),
            "True", Null()
            )

# M HAND TOP

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_n_down_hand_mast_top", ped05_sex_oral_d_hand_o03_xx),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_n_down_hand_mast_top", ped05_sex_oral_d_hand_o02_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_n_down_hand_mast_top", ped05_sex_oral_d_hand_o01_xx),

            "True", Null()
            )

# FrontHead BLOW OVER

    # contains:
    #     ConditionSwitch(

    #         ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("gensex_oral_n_frontHead_exp_mouth_b_blow_over 05", ped05_sex_oral_d_frontHead_blow_over_o04_xx),
            
    #         ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_n_frontHead_exp_mouth_b_blow_over 03", ped05_sex_oral_d_frontHead_blow_over_o03_xx),

    #         ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_n_frontHead_exp_mouth_b_blow_over 02", ped05_sex_oral_d_frontHead_blow_over_o02_xx),

    #         ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_n_frontHead_exp_mouth_b_blow_over 01", ped05_sex_oral_d_frontHead_blow_over_o01_xx),

    #         "True", Null()
    #         )
    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("ped05_sex_oral_d_frontHead_blow_over_im_o04_xx", truecenter),
            
            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("ped05_sex_oral_d_frontHead_blow_over_im_o03_xx", truecenter),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("ped05_sex_oral_d_frontHead_blow_over_im_o02_xx", truecenter),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("ped05_sex_oral_d_frontHead_blow_over_im_o01_xx", truecenter),

            "True", Null()
            )

    # EXPRESSIONS

    contains:
        ConditionSwitch(
            ped_sex_general_expression_Cond == "talk", Null(),

            ped_sex_general_action_Cond in ["o00_00", "o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o00_00),

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02","o00l_03","o00l_04","o00l_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o00l_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o01_xx),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o02_xx),

            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o03_xx),

            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_o04_xx),

            "True", Null()
            )

# GLASSES

    contains:
        ConditionSwitch(

            ped_sex_general_expression_Cond == "talk", Null(),

            n_withoutGlasses_story == False and n_withoutGlasses_Cond == False and ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("gensex_oral_n_frontHead_glasses", ped05_sex_oral_d_frontHead_o04_xx),

            n_withoutGlasses_story == False and n_withoutGlasses_Cond == False and ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_n_frontHead_glasses", ped05_sex_oral_d_frontHead_o03_xx),

            n_withoutGlasses_story == False and n_withoutGlasses_Cond == False and ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_n_frontHead_glasses", ped05_sex_oral_d_frontHead_o02_xx),

            n_withoutGlasses_story == False and n_withoutGlasses_Cond == False and ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_n_frontHead_glasses", ped05_sex_oral_d_frontHead_o01_xx),

            n_withoutGlasses_story == False and n_withoutGlasses_Cond == False and ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_n_frontHead_glasses", ped05_sex_oral_d_frontHead_o00l_xx),

            n_withoutGlasses_story == False and n_withoutGlasses_Cond == False, At("gensex_oral_n_frontHead_glasses",ped05_sex_oral_d_frontHead_o00_00),
            "True", Null()

            #"True", At("gensex_oral_n_frontHead_glasses", ped05_sex_oral_d_frontHead_o00_00)
            )

        # FRONT HAIR

    contains:
        ConditionSwitch(

            ped_sex_general_expression_Cond == "talk", Null(),

            ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("gensex_oral_n_frontHead_hair", ped05_sex_oral_d_frontHead_o04_xx),

            ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_n_frontHead_hair", ped05_sex_oral_d_frontHead_o03_xx),

            ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_n_frontHead_hair", ped05_sex_oral_d_frontHead_o02_xx),

            ped_sex_general_action_Cond in ["o01_01", "o01_02", "o01_03", "o01_04", "o01_05"], At("gensex_oral_n_frontHead_hair", ped05_sex_oral_d_frontHead_o01_xx),

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_n_frontHead_hair", ped05_sex_oral_d_frontHead_o00l_xx),

            "True", At("gensex_oral_n_frontHead_hair", ped05_sex_oral_d_frontHead_o00_00)
            )

# M HAND BOTTOM_B

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_n_down_hand_mast_bot", ped05_sex_oral_d_hand_o02_xx),

            "True", Null()
            )

# MC_Dick_B

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["o00_01", "o00_02", "o00_03", "o00_04", "o00_05"], At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_d_dick_o00_xx),

            ped_sex_blow_Cond == True, Null(),

            "True", At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_d_dick_o00_00)
            )

# D HAND TOP_B

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["o00l_01", "o00l_02", "o00l_03", "o00l_04", "o00l_05"], At("gensex_oral_n_down_hand_mast_top", ped05_sex_oral_d_hand_o02_xx),

            "True", Null()
            )

    contains:
        ConditionSwitch(
            p_prot.action == "masturbate", At("gensex_oral_mc_handmast_top", gensex_oral_mc_handmast_top_anim01),
            "True", Null()
            )

## MC_BODY

    contains:
        "gensex_oral_mc_body_02"
        truecenter
        ypos 0.65

## MC_Chest
        
    contains:
        "gensex_oral_mc_chest"
        truecenter
        ypos 0.65

## MC HAND

    contains:
        ConditionSwitch(

            ped_sex_blow_MChand == "on" and ped_sex_general_action_Cond in ["o02_01", "o02_02", "o02_03", "o02_04", "o02_05"], At("gensex_oral_mc_handonherhead", ped05_sex_oral_mc_handOverHead_o02_xx),
            
            ped_sex_blow_MChand == "on" and ped_sex_general_action_Cond in ["o03_01", "o03_02", "o03_03", "o03_04", "o03_05"], At("gensex_oral_mc_handonherhead", ped05_sex_oral_mc_handOverHead_o03_xx),
            
            ped_sex_blow_MChand == "on" and ped_sex_general_action_Cond in ["o04_01", "o04_02", "o04_03", "o04_04", "o04_05"], At("gensex_oral_mc_handonherhead", ped05_sex_oral_mc_handOverHead_o04_xx),

            "True", Null()
            )

    # contains:
    #     "gensex_oral_mc_handonherhead"
    #     ped05_sex_oral_mc_handOverHead_o04_04

# Smoke
    contains:
        ConditionSwitch(
            p_ao_started == True, At("night05_Cemetery_smoke_b_comp", p_ao_nride_smoke_pos),
            "True", Null())

####################################################
####################################################
####################################################

####################################################
####################################################

# beach_sex_blow_comp Boobjob_01
image pedrera_sex_didac_oral boobjob_general: # DÍDAC

## GROUND

 ###Ground
    contains:
        #if p_ao_started #This is After ORGASM! and not pdaytime == "06morning":
        ConditionSwitch(
            pdaytime == "05_night_Pedrera", At("bg 01", p_ao_oral_ground_trans),
            "True", Null())

## DIDAC
    
    contains:
        "gensex_oral_d_legs down"
        truecenter
        ypos 0.5

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["ob00_00b", "ob00_00"], At("gensex_oral_d_hairBack_down", ped05_sex_oral_d_body_o00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_d_hairBack_down", ped05_sex_oral_d_body_ob01_xx),

            "True", Null()
            )

    ## BODY_BACK

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["ob00_00b", "ob00_00"], At("gensex_oral_d_boobJob_body_back", ped05_sex_oral_d_body_o00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_d_boobJob_body_back", ped05_sex_oral_d_body_ob01_xx),

            "True", Null()
            )
    
    ## HAIR OVER

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["ob00_00b", "ob00_00"], At("gensex_oral_d_hairOver_down", ped05_sex_oral_d_frontHead_ob00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_d_hairOver_down", ped05_sex_oral_d_frontHead_ob01_xx),

            "True", Null()
            )

    ## FRONT HEAD FACE

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["ob00_00b", "ob00_00"], At("gensex_oral_d_frontHead_face", ped05_sex_oral_d_frontHead_ob00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_d_frontHead_face", ped05_sex_oral_d_frontHead_ob01_xx),

            "True", Null()
            )

    # Didac Chest (TO TALK) NOT DOING BoobJob

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond == "ob00_00", At("gensex_oral_d_boobJob_body_front a", ped05_sex_oral_d_body_o00_00),
            "True", Null()
            )

## D EXPRESSIONS

    contains:
        ConditionSwitch(
            ped_sex_general_expression_Cond == "talk", Null(),

            ped_sex_general_action_Cond in ["ob00_00b", "ob00_00"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_ob00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_ob01_xx),

            "True", Null()
            )

## HAIR FRONTHEAD

    contains:
        ConditionSwitch(
            ped_sex_general_expression_Cond == "talk", Null(),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_d_frontHead_hair", ped05_sex_oral_d_frontHead_ob01_xx),

            "True", At("gensex_oral_d_frontHead_hair", ped05_sex_oral_d_frontHead_ob00_00)
            )

## MC_Dick

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["ob00_00", "ob00_00b"], At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_d_dick_ob00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_d_dick_ob01_xx),
            "True", Null()
            )

## BOOBS  OVER DICK!

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond == "ob00_00b", At("gensex_oral_d_boobJob_body_front b", ped05_sex_oral_d_body_o00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_d_boobJob_body_front b", ped05_sex_oral_d_body_ob01_xx),
            "True", Null()
            )
##

    contains:
        "gensex_oral_mc_body_02"
        truecenter
        ypos 0.65

## MC_Chest
        
    contains:
        "gensex_oral_mc_chest"
        truecenter
        ypos 0.65

####################################################
####################################################
####################################################


####################################################
####################################################
####################################################

####################################################
####################################################


# beach_sex_blow_comp Boobjob_01
image pedrera_sex_txell_oral boobjob_general: # MERITXELL BOOBJOB


## Txell

    ## TXELL LEGS
    
    contains:
        "gensex_oral_m_legs down"
        truecenter
        ypos 0.5

    ## BODY_BACK

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["ob00_00b", "ob00_00"], At("gensex_oral_m_boobJob_body_back", ped05_sex_oral_d_body_o00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_m_boobJob_body_back", ped05_sex_oral_d_body_ob01_xx),

            "True", Null()
            )

    ## FRONT HEAD FACE

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["ob00_00b", "ob00_00"], At("gensex_oral_m_frontHead_face", ped05_sex_oral_d_frontHead_ob00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_m_frontHead_face", ped05_sex_oral_d_frontHead_ob01_xx),

            "True", Null()
            )

    # Didac Chest (TO TALK) NOT DOING BoobJob

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond == "ob00_00", At("gensex_oral_m_boobJob_body_front a", ped05_sex_oral_d_body_o00_00),
            "True", Null()
            )

## D EXPRESSIONS

    contains:
        ConditionSwitch(
            ped_sex_general_expression_Cond == "talk", Null(),

            ped_sex_general_action_Cond in ["ob00_00b", "ob00_00"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_ob00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_ob01_xx),

            "True", Null()
            )

## HAIR FRONTHEAD

    contains:
        ConditionSwitch(
            ped_sex_general_expression_Cond == "talk", Null(),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_m_frontHead_hair", ped05_sex_oral_d_frontHead_ob01_xx),

            "True", At("gensex_oral_m_frontHead_hair", ped05_sex_oral_d_frontHead_ob00_00)
            )

## MC_Dick

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["ob00_00", "ob00_00b"], At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_d_dick_ob00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_d_dick_ob01_xx),
            "True", Null()
            )

## BOOBS  OVER DICK!

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond == "ob00_00b", At("gensex_oral_m_boobJob_body_front b", ped05_sex_oral_d_body_o00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_m_boobJob_body_front b", ped05_sex_oral_d_body_ob01_xx),
            "True", Null()
            )
##

    contains:
        "gensex_oral_mc_body_02"
        truecenter
        ypos 0.65

## MC_Chest
        
    contains:
        "gensex_oral_mc_chest"
        truecenter
        ypos 0.65

####################################################
####################################################
####################################################

####################################################
####################################################
####################################################

####################################################
####################################################
####################################################

####################################################
####################################################

# image pedrera_sex_neus_oral boobjob_general:

#     contains:
#         "day05"
#         truecenter
#         zoom 2.0

# beach_sex_blow_comp Boobjob_01

### ob00_00 = small boobs
### ob00_00b = small boobs trying
### ob00_00c = Big boobs
### ob00_00d = Big boobs Over dick Stop

image pedrera_sex_neus_oral boobjob_general: # Neus

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 1.8 ypos 0.15

## NEUS
    
    contains:
        "gensex_oral_n_legs down"
        truecenter
        ypos 0.5

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["ob00_00", "ob00_00b", "ob00_00c", "ob00_00d"], At("gensex_oral_n_boobJob_body_hair", ped05_sex_oral_d_body_o00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_n_boobJob_body_hair", ped05_sex_oral_d_body_ob01_xx),

            "True", Null()
            )

    ## BODY_BACK

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["ob00_00"], At("gensex_oral_n_boobJob_body_back_a", ped05_sex_oral_d_body_o00_00),
            ped_sex_general_action_Cond in ["ob00_00b"], At("gensex_oral_n_boobJob_body_back_c", ped05_sex_oral_d_body_o00_00),
            ped_sex_general_action_Cond in ["ob00_00c"], At("gensex_oral_n_boobJob_body_back_b", ped05_sex_oral_d_body_o00_00),
            ped_sex_general_action_Cond in ["ob00_00d"], At("gensex_oral_n_boobJob_body_back", ped05_sex_oral_d_body_o00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_n_boobJob_body_back", ped05_sex_oral_d_body_ob01_xx),

            "True", Null()
            )
    
    # HAIR OVER

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["ob00_00", "ob00_00b", "ob00_00c", "ob00_00d"], At("gensex_oral_n_frontHead_hair_back_ground", ped05_sex_oral_d_frontHead_ob00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_n_frontHead_hair_back_ground", ped05_sex_oral_d_frontHead_ob01_xx),

            "True", Null()
            )

    ## NEUS EARS

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["ob00_00", "ob00_00b", "ob00_00c", "ob00_00d"], At("gensex_oral_n_frontHead_ears ground", ped05_sex_oral_d_frontHead_ob00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_n_frontHead_ears ground", ped05_sex_oral_d_frontHead_ob01_xx),

            "True", Null()
            )

    ## FRONT HEAD FACE

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["ob00_00", "ob00_00b", "ob00_00c", "ob00_00d"], At("gensex_oral_n_frontHead_face", ped05_sex_oral_d_frontHead_ob00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_n_frontHead_face", ped05_sex_oral_d_frontHead_ob01_xx),

            "True", Null()
            )

    # Neus Chest (TO TALK) NOT DOING BoobJob

    # contains:
    #     ConditionSwitch(
    #         ped_sex_general_action_Cond == "ob00_00", At("gensex_oral_n_boobJob_body_front a", ped05_sex_oral_d_body_o00_00),
    #         "True", Null()
    #         )

## N EXPRESSIONS

    contains:
        ConditionSwitch(
            ped_sex_general_expression_Cond == "talk", Null(),

            ped_sex_general_action_Cond in ["ob00_00", "ob00_00b", "ob00_00c", "ob00_00d"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_ob00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("ped_sex_oral_expression_img", ped05_sex_oral_d_frontHead_ob01_xx),

            "True", Null()
            )

## HAIR FRONTHEAD

    contains:
        ConditionSwitch(
            ped_sex_general_expression_Cond == "talk", Null(),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_n_frontHead_hair", ped05_sex_oral_d_frontHead_ob01_xx),

            "True", At("gensex_oral_n_frontHead_hair", ped05_sex_oral_d_frontHead_ob00_00)
            )

## MC_Dick

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ["ob00_00", "ob00_00b", "ob00_00c", "ob00_00d"], At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_d_dick_ob00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_mc_dick_01_wet_00", ped05_sex_oral_d_dick_ob01_xx),
            "True", Null()
            )

## BOOBS  OVER DICK!

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond == "ob00_00d", At("gensex_oral_n_boobJob_body_front_c_big", ped05_sex_oral_d_body_o00_00),

            ped_sex_general_action_Cond in ["ob01_01", "ob01_02", "ob01_03","ob01_04", "ob01_05"], At("gensex_oral_n_boobJob_body_front_c_big", ped05_sex_oral_d_body_ob01_xx),
            "True", Null()
            )
##

    contains:
        "gensex_oral_mc_body_02"
        truecenter
        ypos 0.65

## MC_Chest
        
    contains:
        "gensex_oral_mc_chest"
        truecenter
        ypos 0.65


####################################################
####################################################
####################################################

####################################################
####################################################
####################################################

####################################################
####################################################
####################################################

####################################################
####################################################


####################################################
## 02 WHOLE GLANS

transform ped05_sex_oral_mc_handOverHead_o02_xx:
    subpixel True
    truecenter
    xpos 0.5 
    ypos -0.58 # Top Head
    block:
        ease 4.0/ped_sex_num  ypos -0.32 # Below
        ease 4.0/ped_sex_num  ypos -0.58 # Top Head
        repeat

####################################################
## 03 HALF DICK

transform ped05_sex_oral_mc_handOverHead_o03_xx:
    subpixel True
    truecenter
    xpos 0.5
    ypos -0.58 # Top Head
    block:
        ease 4.0/ped_sex_num  ypos -0.15 # Below Deepthroat
        ease 4.0/ped_sex_num  ypos -0.58 # Top Head
        repeat

####################################################
## 04 DEEPTHROAT

transform ped05_sex_oral_mc_handOverHead_o04_xx:
    subpixel True
    truecenter
    xpos 0.5
    ypos -0.58 # Top Head
    block:
        ease 4.0/ped_sex_num  ypos 0.10 # Below Deepthroat
        ease 4.0/ped_sex_num  ypos -0.58 # Top Head
        repeat


####################################################
####################################################
####################################################
####################################################
####################################################
####################################################
####################################################
####################################################
####################################################
####################################################
####################################################
####################################################

## MISSIONARY

#image pedrera_sex_missionary_didac_REFERENCE = "images/day05/pedrera/sex/missionary/pedrera_sex_missionary_didac_REFERENCE.webp"

#image morning05_missionary02_REFERENCE = "images/day05/morning/morning05_missionary02_REFERENCE.webp"
image gensex_missionary02_d_slim_bg = SaturateTint("images/general/sex/missionary/didac/gensex_missionary02_d_slim_bg.webp")

image gensex_missionary02_d_slim_boobs = SaturateTint("images/general/sex/missionary/didac/gensex_missionary02_d_slim_boobs.webp")
image gensex_missionary02_d_slim_below_vaginal_closed = SaturateTint("images/general/sex/missionary/didac/gensex_missionary02_d_slim_below_vaginal_closed.webp")
image gensex_missionary02_d_slim_body = SaturateTint("images/general/sex/missionary/didac/gensex_missionary02_d_slim_body.webp")
image gensex_missionary02_d_slim_cover = SaturateTint("images/general/sex/missionary/didac/gensex_missionary02_d_slim_cover.webp")
image gensex_missionary02_d_slim_legs_vaginal = SaturateTint("images/general/sex/missionary/didac/gensex_missionary02_d_slim_legs_vaginal.webp")
image gensex_missionary02_d_slim_legs_anal = SaturateTint("images/general/sex/missionary/didac/gensex_missionary02_d_slim_legs_anal.webp")
image gensex_missionary02_d_slim_over_vaginal_fucked = SaturateTint("images/general/sex/missionary/didac/gensex_missionary02_d_slim_over_vaginal_fucked.webp")
image gensex_missionary02_d_slim_over_vaginal_licked = SaturateTint("images/general/sex/missionary/didac/gensex_missionary02_d_slim_over_vaginal_licked.webp")
image gensex_missionary02_d_slim_over_anal_fucked = SaturateTint("images/general/sex/missionary/didac/gensex_missionary02_d_slim_over_anal_fucked.webp")

image gensex_missionary02_didac_txell_bottom = SaturateTint("images/general/sex/missionary/didac/gensex_missionary02_didac_txell_bottom.webp")
image gensex_missionary02_didac_txell_top = SaturateTint("images/general/sex/missionary/didac/gensex_missionary02_didac_txell_top.webp")

############################################################################################################
############################################################################################################

    ## DICK

transform ped05_sex_missionary_dick_00:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.92
    #zoom 0.9 ypos 1.0 ## All In
    zoom 1.1 ypos 2.0 ## All Out

transform ped05_sex_missionary_dick_v00_00:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.92
    #zoom 0.9 ypos 1.0 ## All In
    zoom 1.1 ypos 2.0 ## All Out

###

transform ped05_sex_missionary_dick_v00_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.92
    #zoom 0.9 ypos 1.0 ## All In
    zoom 1.1 ypos 2.0 ## All Out
    block:
        ease 4.0/ped_sex_num  ypos 1.9
        ease 4.0/ped_sex_num  ypos 2.0
        repeat


transform ped05_sex_missionary_dick_v01_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.92
    zoom 1.0 ypos 1.65 ## On the tip
    block:
        ease 4.0/ped_sex_num  zoom 0.95 ypos 1.25 # Half in
        ease 4.0/ped_sex_num  zoom 1.0 ypos 1.65 ## On the tip
        repeat

    # Deep

transform ped05_sex_missionary_dick_v02_xx:
    subpixel True
    transform_anchor True 
    xalign 0.5 yalign 0.92
    zoom 1.0 ypos 1.65 ## On the tip
    block:
        ease 4.0/ped_sex_num  zoom 0.9 ypos 1.0 ## All In
        ease 4.0/ped_sex_num  zoom 1.0 ypos 1.65 ## On the tip
        repeat

    ## ANAL

transform ped05_sex_missionary_dick_a00_00:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.92
    zoom 1.1 ypos 2.0 ## All Out

transform ped05_sex_missionary_dick_a00_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.92
    zoom 1.1 ypos 2.0 ## All Out
    block:
        easein 4.0/ped_sex_num  zoom 1.08 ypos 1.95 ## Anal Tease
        easeout 4.0/ped_sex_num  zoom 1.1 ypos 2.0 ## All Out
        repeat

    ## ANAL 01 HALF

transform ped05_sex_missionary_dick_a01_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.92
    zoom 1.05 ypos 1.9 ## Anal Beginnning
    block:
        ease 4.0/ped_sex_num  zoom 0.95 ypos 1.55 ## Anal HALF
        ease 4.0/ped_sex_num  zoom 1.05 ypos 1.9 ## Anal Beginnning
        repeat

###

transform ped05_sex_missionary_dick_a02_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.92
    zoom 1.05 ypos 1.9 ## Anal Beginnning
    block:
        ease 4.0/ped_sex_num  zoom 0.95 ypos 1.2 ## Anal Full
        ease 4.0/ped_sex_num  zoom 1.05 ypos 1.9 ## Anal Beginnning
        repeat


    # CUM Vaginal

transform ped05_sex_missionary_dick_vcum01:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.92
    zoom 1.0 ypos 1.65 ## On the tip
    parallel:
        ease_bounce 4.0 zoom 0.95 ypos 1.25 # Half in
    parallel:
        ease_bounce 1.0 xzoom 0.98
        ease_bounce 1.0 xzoom 1.02
        ease_bounce 1.0 xzoom 0.99
        ease_bounce 1.0 xzoom 1.0
        repeat
    parallel:
        easein_bounce 0.9 yzoom 0.99
        easeout_bounce 1.1 yzoom 1.01
        easein_bounce 1.1 yzoom 0.98
        easeout_bounce 0.9 yzoom 1.0
        repeat

transform ped05_sex_missionary_dick_vcum02:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.92
    zoom 1.0 ypos 1.65 ## On the tip
    parallel:
        ease_bounce 4.0 zoom 0.95 ypos 1.0 ## All In
    parallel:
        ease_bounce 1.0 xzoom 0.98
        ease_bounce 1.0 xzoom 1.02
        ease_bounce 1.0 xzoom 0.99
        ease_bounce 1.0 xzoom 1.0
        repeat
    parallel:
        easein_bounce 0.9 yzoom 0.99
        easeout_bounce 1.1 yzoom 1.01
        easein_bounce 1.1 yzoom 0.98
        easeout_bounce 0.9 yzoom 1.0
        repeat


transform ped05_sex_missionary_dick_acum01:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.92
    zoom 1.05 ypos 1.9 ## Anal Beginnning
    parallel:
        ease_bounce 4.0 zoom 0.95 ypos 1.55 ## Anal HALF
    parallel:
        ease_bounce 1.0 xzoom 0.98
        ease_bounce 1.0 xzoom 1.02
        ease_bounce 1.0 xzoom 0.99
        ease_bounce 1.0 xzoom 1.0
        repeat
    parallel:
        easein_bounce 0.9 yzoom 0.99
        easeout_bounce 1.1 yzoom 1.01
        easein_bounce 1.1 yzoom 0.98
        easeout_bounce 0.9 yzoom 1.0
        repeat

transform ped05_sex_missionary_dick_acum02:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.92
    zoom 1.05 ypos 1.9 ## Anal Beginnning
    parallel:
        ease_bounce 4.0 zoom 0.95 ypos 1.2 ## Anal Full
    parallel:
        ease_bounce 1.0 xzoom 0.98
        ease_bounce 1.0 xzoom 1.02
        ease_bounce 1.0 xzoom 0.99
        ease_bounce 1.0 xzoom 1.0
        repeat
    parallel:
        easein_bounce 0.9 yzoom 0.99
        easeout_bounce 1.1 yzoom 1.01
        easein_bounce 1.1 yzoom 0.98
        easeout_bounce 0.9 yzoom 1.0
        repeat

##########  ## PUSSY OVER

transform ped05_sex_missionary_vaginalOver_v01_xx:
    subpixel True
    truecenter
    xzoom 0.8 yzoom 0.7 ypos 0.92 # On the tip
    block:
        easein_quad 4.0/ped_sex_num  xzoom 1.0 yzoom 1.1 ypos 0.85 # Half Dick Inside
        easeout_quad 4.0/ped_sex_num  xzoom 0.8 yzoom 0.65 ypos 0.92 # On the tip
        repeat

    # Deep

transform ped05_sex_missionary_vaginalOver_v02_xx:
    subpixel True
    truecenter
    xzoom 0.8 yzoom 0.7 ypos 0.92 # On the tip
    block:
        ease 4.0/ped_sex_num  xzoom 1.1 yzoom 1.1 ypos 0.85 # Half Dick Inside
        ease 4.0/ped_sex_num  xzoom 0.8 yzoom 0.65 ypos 0.92 # On the tip
        repeat

##

transform ped05_sex_missionary_vaginalOver_vcum01:
    subpixel True
    truecenter
    xzoom 0.8 yzoom 0.7 ypos 0.92 # On the tip
    block:
        ease_bounce 4.0 xzoom 1.0 yzoom 1.1 ypos 0.85 # Half Dick Inside

transform ped05_sex_missionary_vaginalOver_vcum02:
    subpixel True
    truecenter
    xzoom 0.8 yzoom 0.7 ypos 0.92 # On the tip
    block:
        ease_bounce 4.0 xzoom 1.1 yzoom 1.1 ypos 0.85 # Half Dick Inside

## ANAL OVER

transform ped05_sex_missionary_analOver_a01_xx:
    subpixel True
    truecenter
    xzoom 0.75 yzoom 0.4 ypos 1.12 # Anal On the tip
    block:
        easein 4.0/ped_sex_num  xzoom 1.0 yzoom  0.9 ypos 1.08 # Anal HALF
        ease 4.0/ped_sex_num  xzoom 0.75 yzoom 0.4 ypos 1.12 # Anal On the tip
        repeat

###

transform ped05_sex_missionary_analOver_a02_xx:
    subpixel True
    truecenter
    xzoom 0.75 yzoom 0.4 ypos 1.13 # Anal On the tip
    block:
        easein 4.0/ped_sex_num  xzoom 1.1 yzoom  0.9 ypos 1.03 # Anal DEEP
        ease 4.0/ped_sex_num  xzoom 0.75 yzoom 0.4 ypos 1.15 # Anal On the tip
        repeat

transform ped05_sex_missionary_analOver_acum01:
    subpixel True
    truecenter
    xzoom 0.75 yzoom 0.4 ypos 1.13 # Anal On the tip
    ease_bounce 4.0 xzoom 1.0 yzoom  0.9 ypos 1.04 # Anal HALF
    parallel:
        ease_bounce 1.0 xzoom 1.0
        ease_bounce 1.0 xzoom 1.02
        ease_bounce 1.0 xzoom 1.0
        ease_bounce 1.0 xzoom 1.01
        repeat
    parallel:
        easein_bounce 0.9 yzoom 1.0
        easeout_bounce 1.1 yzoom 1.01
        easein_bounce 1.1 yzoom 1.0
        easeout_bounce 0.9 yzoom 1.01
        repeat

transform ped05_sex_missionary_analOver_acum02:
    subpixel True
    truecenter
    xzoom 0.75 yzoom 0.4 ypos 1.13 # Anal On the tip
    ease_bounce 4.0 xzoom 1.1 yzoom  0.9 ypos 1.02 # Anal DEEP
    parallel:
        ease_bounce 1.0 xzoom 1.0
        ease_bounce 1.0 xzoom 1.02
        ease_bounce 1.0 xzoom 1.0
        ease_bounce 1.0 xzoom 1.01
        repeat
    parallel:
        easein_bounce 0.9 yzoom 1.0
        easeout_bounce 1.1 yzoom 1.01
        easein_bounce 1.1 yzoom 1.0
        easeout_bounce 0.9 yzoom 1.01
        repeat


    ## VAGINAL TONGUE

transform ped05_sex_missionary_vaginalOver_vt01_xx:
    subpixel True
    truecenter
    xzoom 0.42 yzoom 0.4 ypos 0.92 # Tip-Beginning Licking
    #xzoom 0.47 yzoom 0.5 ypos 0.9 # Mostly Tongue inside.
    #xzoom 0.5 yzoom 0.6 ypos 0.9 #All Tongue inside
    block:
        ease 4.0/ped_sex_num  xzoom 0.47 yzoom 0.5 ypos 0.9 # Mostly Tongue inside.
        ease 4.0/ped_sex_num  xzoom 0.42 yzoom 0.4 ypos 0.92 # Tip-Beginning Licking
        repeat

###

transform ped05_sex_missionary_vaginalOver_vt02_xx:
    subpixel True
    truecenter
    xzoom 0.42 yzoom 0.4 ypos 0.92 # Tip-Beginning Licking
    block:
        ease 4.0/ped_sex_num  xzoom 0.47 yzoom 0.6 ypos 0.9 #All Tongue inside
        ease 4.0/ped_sex_num  xzoom 0.42 yzoom 0.4 ypos 0.92 # Tip-Beginning Licking
        repeat

    ##

##########  ## BOOBS MOVING with Missionary Sex

transform ped05_sex_missionary_boobs_v00_00:
    truecenter
    ypos 0.19

##

transform ped05_sex_missionary_boobs_v01_xx:
    subpixel True
    truecenter
    ypos 0.19
    block:
        ease 4.0/ped_sex_num  xzoom 0.995 yzoom 1.004 ypos 0.188
        ease 4.0/ped_sex_num  xzoom 1.0 yzoom 1.0 ypos 0.19
        repeat

    # Deep

transform ped05_sex_missionary_boobs_v02_xx:
    subpixel True
    truecenter
    ypos 0.19
    block:
        ease 4.0/ped_sex_num  xzoom 0.995 yzoom 1.004 ypos 0.188
        ease 4.0/ped_sex_num  xzoom 1.0 yzoom 1.0 ypos 0.19
        repeat

    # CUM

transform ped05_sex_missionary_boobs_vcum01:
    subpixel True
    truecenter
    ypos 0.19
    block:
        ease 2.0 xzoom 0.995 yzoom 1.004 ypos 0.188
        ease 2.0 xzoom 1.0 yzoom 1.0 ypos 0.19

##########  ## LEGS

transform ped05_sex_missionary_legs_v01_xx:
    subpixel True
    truecenter
    ypos 0.5
    block:
        ease 4.0/ped_sex_num  ypos 0.48
        ease 4.0/ped_sex_num  ypos 0.5
        repeat

    # Deep

transform ped05_sex_missionary_legs_v02_xx:
    subpixel True
    truecenter
    ypos 0.5
    block:
        ease 4.0/ped_sex_num  ypos 0.45
        ease 4.0/ped_sex_num  ypos 0.52
        repeat

    # CUM

transform ped05_sex_missionary_legs_vcum01:
    subpixel True
    truecenter
    ypos 0.5
    ease_bounce 4.0 ypos 0.43 # Half Dick Inside

##########  ## BODY

transform ped05_sex_missionary_body_v01_xx:
    subpixel True
    truecenter
    block:
        ease 4.0/ped_sex_num  ypos 0.4995
        ease 4.0/ped_sex_num  ypos 0.5005
        repeat

    # Deep

transform ped05_sex_missionary_body_v02_xx:
    subpixel True
    truecenter
    block:
        ease 4.0/ped_sex_num  ypos 0.4995
        ease 4.0/ped_sex_num  ypos 0.5005
        repeat

    # CUM

transform ped05_sex_missionary_body_vcum01:
    subpixel True
    truecenter
    block:
        ease 2.0 ypos 0.4995
        ease 2.0 ypos 0.5005


##########  ## TONGUE

# transform ped05_sex_missionary_at00: # THERE'S NO ANAL TONGUE IN MISSIONARY POSITION.
#     transform_anchor True
#     xalign 0.5 yalign 0.72
#     ypos 1.255  # Tip-Out of Pussy
#     block:
#         easein 4.0 rotate 5
#         easein 4.0 rotate -5
#         repeat

transform ped05_sex_missionary_vt00_00:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.72
    ypos 1.255  # Tip-Out of Pussy
    parallel:
        easeout 8.0 ypos 1.1 # Tip-At Clitoris
        easein 8.0 ypos 1.23 # Tip-At below part
        repeat
    parallel:
        easein 8.5 rotate 5
        easein 8.5 rotate -5
        repeat
##

transform ped05_sex_missionary_vt00_xx:
    subpixel True ## 00? That's only the pose, not the velocity.
    transform_anchor True
    xalign 0.5 yalign 0.72
    ypos 1.255  # Tip-Out of Pussy
    parallel:
        easeout 4.0/ped_sex_num  ypos 1.1 # Tip-At Clitoris
        easein 4.0/ped_sex_num  ypos 1.23 # Tip-At below part
        repeat
    parallel:
        easein 3.5/ped_sex_num  rotate 5
        easein 3.5/ped_sex_num  rotate -5
        repeat

    # TONGUE IN

transform ped05_sex_missionary_vt01_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.72
    ypos 1.08 # Tip-Beginning Licking
    #ypos 0.95 # All Tongue inside.
    block:
        easeout 4.0/ped_sex_num  ypos 1.0 # Mostly Tongue inside.
        easein 4.0 ypos 1.08 # Tip-Beginning Licking
        repeat
    parallel:
        easein 2.5/ped_sex_num  rotate 5
        easein 2.5/ped_sex_num  rotate -5
        repeat

##

transform ped05_sex_missionary_vt02_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.72
    ypos 1.08 # Tip-Beginning Licking
    parallel:
        easeout 4.0/ped_sex_num  ypos 0.95 # All Tongue inside.
        easein 4.0/ped_sex_num  ypos 1.08 # Tip-Beginning Licking
        repeat
    parallel:
        ease 2.5 rotate 1
        ease 2.5 rotate -1
        repeat

############################################################################################################
############################################################################################################


image gensex_missionary_d_comp 02:

    # contains:
    #     "morning05_missionary02_REFERENCE"
    #     truecenter

        # BG-BED

    contains:
        "gensex_missionary02_d_slim_bg"
        truecenter

        ## DIDAC BODY

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05", "a01_01", "a01_02", "a01_03", "a01_04", "a01_05"], At("gensex_missionary02_d_slim_body", ped05_sex_missionary_body_v01_xx),

            ped_sex_general_action_Cond in ["v02_01", "v02_02", "v02_03", "v02_04", "v02_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05"], At("gensex_missionary02_d_slim_body", ped05_sex_missionary_body_v02_xx),
            
            "True", At("gensex_missionary02_d_slim_body", truecenter)
            )

    # contains:
    #     "gensex_missionary02_d_slim_body"
    #     truecenter

        ## BELOW LEGS (ASS-VAGINA)

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["vcum01", "vcum02", "acum01", "acum02"], At("gensex_missionary02_d_slim_below_vaginal_closed", ped05_sex_missionary_legs_vcum01),

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05", "a01_01", "a01_02", "a01_03", "a01_04", "a01_05"], At("gensex_missionary02_d_slim_below_vaginal_closed", ped05_sex_missionary_legs_v01_xx),

            ped_sex_general_action_Cond in ["v02_01", "v02_02", "v02_03", "v02_04", "v02_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05"], At("gensex_missionary02_d_slim_below_vaginal_closed", ped05_sex_missionary_legs_v02_xx),

            "True", At("gensex_missionary02_d_slim_below_vaginal_closed", truecenter)
            )
    
    # contains:
    #     "gensex_missionary02_d_slim_below_vaginal_closed"
    #     truecenter

    #     ## TXELL BOTTOM

    contains:
        ConditionSwitch(
            p_didac.action == "cunnilingus_done_p_txell", At("gensex_missionary02_didac_txell_bottom", truecenter),
            "True", Null()
            )

        # TONGUE

    contains:
        ConditionSwitch(
            #ped_sex_general_action_Cond == "vt00", At("gensex_missionary_mc_tongue_01", ped05_sex_missionary_vt00),



            ped_sex_general_action_Cond == "vt00_00", At("gensex_missionary_mc_tongue_01", ped05_sex_missionary_vt00_00),

            ped_sex_general_action_Cond in ["vt00_01", "vt00_02", "vt00_03", "vt00_04", "vt00_05"], At("gensex_missionary_mc_tongue_01", ped05_sex_missionary_vt00_xx),

            ped_sex_general_action_Cond in ["vt01_01", "vt01_02", "vt01_03", "vt01_04", "vt01_05"], At("gensex_missionary_mc_tongue_01", ped05_sex_missionary_vt01_xx),

            ped_sex_general_action_Cond in ["vt02_01", "vt02_02", "vt02_03", "vt02_04", "vt02_05"], At("gensex_missionary_mc_tongue_01", ped05_sex_missionary_vt02_xx),

            "True", Null()

            )
    
        # DICK

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["00"], At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_00),

            ped_sex_general_action_Cond == "vcum01", At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_vcum01),
            ped_sex_general_action_Cond == "vcum02", At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_vcum02),

            ped_sex_general_action_Cond == "acum01", At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_acum01),
            ped_sex_general_action_Cond == "acum02", At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_acum02),

            ped_sex_general_action_Cond == "v00_00", At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_v00_00),

            ped_sex_general_action_Cond in ["v00_01", "v00_02", "v00_03", "v00_04", "v00_05"], At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_v00_xx),

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05"], At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_v01_xx),
            
            ped_sex_general_action_Cond in ["v02_01", "v02_02", "v02_03", "v02_04", "v02_05"], At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_v02_xx),

            ped_sex_general_action_Cond == "a00_00", At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_a00_00),

            ped_sex_general_action_Cond in ["a00_01", "a00_02", "a00_03", "a00_04", "a00_05"], At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_a00_xx),

            ped_sex_general_action_Cond in ["a01_01", "a01_02", "a01_03", "a01_04", "a01_05"], At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_a01_xx),
            
            ped_sex_general_action_Cond in ["a02_01", "a02_02", "a02_03", "a02_04", "a02_05"], At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_a02_xx),

            #### ped_sex_general_action_Cond in ["vt00", "vt01_01", "vt01_02", "vt01_03", "vt01_04", "vt01_05", "vt02", "vt02_02", "vt02_03", "vt02_04", "vt02_05","vt03", "vt03_02", "vt03_03", "vt03_04", "vt03_05"], Null(),
            "True", Null()
            )

        ## STOMACH COVER

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05", "a01_01", "a01_02", "a01_03", "a01_04", "a01_05"], At("gensex_missionary02_d_slim_cover", ped05_sex_missionary_body_v01_xx),

            ped_sex_general_action_Cond in ["v02_01", "v02_02", "v02_03", "v02_04", "v02_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05"], At("gensex_missionary02_d_slim_cover", ped05_sex_missionary_body_v02_xx),

            "True", At("gensex_missionary02_d_slim_cover", truecenter)
            )

        ## ANAL OVER

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond == "acum01", At("gensex_missionary02_d_slim_over_anal_fucked", ped05_sex_missionary_analOver_acum01),
            ped_sex_general_action_Cond == "acum02", At("gensex_missionary02_d_slim_over_anal_fucked", ped05_sex_missionary_analOver_acum02),

            ped_sex_general_action_Cond in ["a01_01", "a01_02", "a01_03", "a01_04", "a01_05",], At("gensex_missionary02_d_slim_over_anal_fucked", ped05_sex_missionary_analOver_a01_xx),

            ped_sex_general_action_Cond in ["a02_01", "a02_02", "a02_03", "a02_04", "a02_05",], At("gensex_missionary02_d_slim_over_anal_fucked", ped05_sex_missionary_analOver_a02_xx),

            "True", Null()
            )
    
        ## LEGS VAGINAL-ANAL

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["vcum01", "vcum02"], At("gensex_missionary02_d_slim_legs_vaginal", ped05_sex_missionary_legs_vcum01),

            ped_sex_general_action_Cond in ["acum01", "acum02"], At("gensex_missionary02_d_slim_legs_anal", ped05_sex_missionary_legs_vcum01),

            ped_sex_general_action_Cond in ["v01_01", "v01_02","v01_03","v01_04","v01_05"], At("gensex_missionary02_d_slim_legs_vaginal", ped05_sex_missionary_legs_v01_xx),

            ped_sex_general_action_Cond in ["v02_01", "v02_02","v02_03","v02_04","v02_05"], At("gensex_missionary02_d_slim_legs_vaginal", ped05_sex_missionary_legs_v02_xx),

            ped_sex_general_action_Cond in ["a01_01", "a01_02","a01_03","a01_04","a01_05"], At("gensex_missionary02_d_slim_legs_anal", ped05_sex_missionary_legs_v01_xx),
            
            ped_sex_general_action_Cond in ["a02_01", "a02_02","a02_03","a02_04","a02_05"], At("gensex_missionary02_d_slim_legs_anal", ped05_sex_missionary_legs_v02_xx),

            "True", At("gensex_missionary02_d_slim_legs_vaginal", truecenter)
            )

        ## PUSSY OVER

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond == "vcum01", At("gensex_missionary02_d_slim_over_vaginal_fucked", ped05_sex_missionary_vaginalOver_vcum01),
            ped_sex_general_action_Cond == "vcum02", At("gensex_missionary02_d_slim_over_vaginal_fucked", ped05_sex_missionary_vaginalOver_vcum02),

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05"], At("gensex_missionary02_d_slim_over_vaginal_fucked", ped05_sex_missionary_vaginalOver_v01_xx),

            ped_sex_general_action_Cond in ["v02_01", "v02_02", "v02_03", "v02_04", "v02_05"], At("gensex_missionary02_d_slim_over_vaginal_fucked", ped05_sex_missionary_vaginalOver_v02_xx),

            ped_sex_general_action_Cond in ["vt01_01", "vt01_02", "vt01_03", "vt01_04", "vt01_05"], At("gensex_missionary02_d_slim_over_vaginal_licked", ped05_sex_missionary_vaginalOver_vt01_xx),

            ped_sex_general_action_Cond in ["vt02_01", "vt02_02", "vt02_03", "vt02_04", "vt02_05"], At("gensex_missionary02_d_slim_over_vaginal_licked", ped05_sex_missionary_vaginalOver_vt02_xx),

            "True", Null()
            )

        ## BOOBS

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05", "a01_01", "a01_02", "a01_03", "a01_04", "a01_05"], At("gensex_missionary02_d_slim_boobs", ped05_sex_missionary_boobs_v01_xx),

            ped_sex_general_action_Cond in ["v02_01", "v02_02", "v02_03", "v02_04", "v02_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05"], At("gensex_missionary02_d_slim_boobs", ped05_sex_missionary_boobs_v02_xx),

            "True", At("gensex_missionary02_d_slim_boobs", ped05_sex_missionary_boobs_v00_00)
            )

    ## FACE
    
    contains:
        "gensex_missionary_d_head_face"
        ped_missionary02_d_exp_comp_pos


####################

        ## EXPRESSIONS

    contains:
        ConditionSwitch(
                ped_sex_general_expression_Cond != "talk", At("gensex_missionary_d_head_exp_blush 03", ped_missionary02_d_exp_comp_pos),
                "True", Null()
                )

    ## EYES

    contains:
        ConditionSwitch(
                ped_sex_general_expression_Cond == "closed", At("gensex_missionary_d_head_exp_eyes 08", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "indifferent", At("gensex_missionary_d_head_exp_eyes 08", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "lust", At("gensex_missionary_d_head_exp_eyes 04", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "angry", At("gensex_missionary_d_head_exp_eyes 06", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "angryFront", At("gensex_missionary_d_head_exp_eyes 05", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond in ["surpriseLeft", "surpriseRight"], At("gensex_missionary_d_head_exp_eyes 01", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "surpriseDown", At("gensex_missionary_d_head_exp_eyes 01", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "talk", Null(),
                "True", Null()
                )

    ## PIRIS

    contains:
        ConditionSwitch(
                ped_sex_general_expression_Cond == "closed", At("gensex_missionary_d_head_exp_pupils empty", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "indifferent", At("gensex_missionary_d_head_exp_pupils empty", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "lust", At("gensex_missionary_d_head_exp_pupils front04", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "angry", At("gensex_missionary_d_head_exp_pupils empty", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "angryFront", At("gensex_missionary_d_head_exp_pupils front05", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "surpriseLeft", At("gensex_missionary_d_head_exp_pupils left01", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "surpriseRight", At("gensex_missionary_d_head_exp_pupils right01", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "surpriseDown", At("gensex_missionary_d_head_exp_pupils down01", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "talk", Null(),
                "True", Null()
                )

    ## EYEBROWS

    contains:
        ConditionSwitch(
                ped_sex_general_expression_Cond == "closed", At("gensex_missionary_d_head_exp_eyebrows sadx07", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "indifferent", At("gensex_missionary_d_head_exp_eyebrows surprisex01", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "lust", At("gensex_missionary_d_head_exp_eyebrows suspiciousx03", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "angry", At("gensex_missionary_d_head_exp_eyebrows angryx07", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "angryFront", At("gensex_missionary_d_head_exp_eyebrows angryx07", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond in ["surpriseLeft", "surpriseRight"], At("gensex_missionary_d_head_exp_eyebrows surprisex02", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "surpriseDown", At("gensex_missionary_d_head_exp_eyebrows surprisex02", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "talk", Null(),
                "True", Null()
                )

    ## MOUTH

    contains:
        ConditionSwitch(
                ped_sex_general_expression_Cond == "closed", At("gensex_missionary_d_head_exp_mouth sadbiting_Silentx06", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "indifferent", At("gensex_missionary_d_head_exp_mouth sad_Silentx03", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "lust", At("gensex_missionary_d_head_exp_mouth happybiting_Silentx07", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "angry", At("gensex_missionary_d_head_exp_mouth sadbiting_Silentx06", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "angryFront", At("gensex_missionary_d_head_exp_mouth sadbiting_Silentx06", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond in ["surpriseLeft", "surpriseRight"], At("gensex_missionary_d_head_exp_mouth sadbiting_Silentx06", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "surpriseDown", At("gensex_missionary_d_head_exp_mouth sadbiting_Silentx06", ped_missionary02_d_exp_comp_pos),
                ped_sex_general_expression_Cond == "talk", Null(),

                "True", Null()
                )

    # ## GLASSES

    # contains:
    #     ConditionSwitch(
    #         p_activeno == "_n" and n_withoutGlasses_story == False and n_withoutGlasses_Cond == False, At("gensex_oral_n_frontHead_glasses", ped_missionary02_d_exp_comp_pos),
    #         "True", Null()
    #         )

# if ped_sex_general_expression_Cond == "talk":

#     if n_withoutGlasses_story == False and n_withoutGlasses_Cond == False:
#         show gensex_oral_n_frontHead_glasses:
#             pedrera_sex_didac_general_speaking_exp_pos
#     else:
#         show gensex_oral_n_frontHead_glasses empty:
#             pedrera_sex_didac_general_speaking_exp_pos

    ## HAIR FRONT

    contains:
        ConditionSwitch(ped_sex_general_expression_Cond == "talk", Null(),
                "True", At("gensex_missionary_d_head_hairfront", ped_missionary02_d_exp_comp_pos)
                )

####################

    #     ## TXELL TOP

    contains:
        ConditionSwitch(
                p_didac.action == "cunnilingus_done_p_txell", At("gensex_missionary02_didac_txell_top", truecenter),
                "True", Null()
                )


############################################################################################################
############################################################################################################
##########################################################################################
##########################################################################################
############################################################################################################
############################################################################################################

############################################################################################################
############################################################################################################ NEUS MISSIONARY


## NEUS MISSIONARY

image gensex_missionary_n_comp 01:

    # contains:
    #     "gensex_missionary_n_PROVE"
    #     truecenter

        ##BG-BED

    contains:
        "gensex_missionary_n_bg"
        truecenter

            ## NEUS BACK HAIR

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05", "a01_01", "a01_02", "a01_03", "a01_04", "a01_05"], At("gensex_missionary_n_hairBack", ped05_sex_missionary_body_v01_xx),

            ped_sex_general_action_Cond in ["v02_01", "v02_02", "v02_03", "v02_04", "v02_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05"], At("gensex_missionary_n_hairBack", ped05_sex_missionary_body_v02_xx),
            
            "True", At("gensex_missionary_n_hairBack", truecenter)
            )

        ## NEUS BODY

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05", "a01_01", "a01_02", "a01_03", "a01_04", "a01_05"], At("gensex_missionary_n_body", ped05_sex_missionary_body_v01_xx),

            ped_sex_general_action_Cond in ["v02_01", "v02_02", "v02_03", "v02_04", "v02_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05"], At("gensex_missionary_n_body", ped05_sex_missionary_body_v02_xx),
            
            "True", At("gensex_missionary_n_body", truecenter)
            )


## BELOW LEGS (ASS-VAGINA)

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["vcum01", "vcum02", "acum01", "acum02"], At("gensex_missionary_n_below_vaginal_closed", ped05_sex_missionary_legs_vcum01),

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05", "a01_01", "a01_02", "a01_03", "a01_04", "a01_05"], At("gensex_missionary_n_below_vaginal_closed", ped05_sex_missionary_legs_v01_xx),

            ped_sex_general_action_Cond in ["v02_01", "v02_02", "v02_03", "v02_04", "v02_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05"], At("gensex_missionary_n_below_vaginal_closed", ped05_sex_missionary_legs_v02_xx),

            "True", At("gensex_missionary_n_below_vaginal_closed", truecenter)
            )
    

# TONGUE

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond == "vt00_00", At("gensex_missionary_mc_tongue_01", ped05_sex_missionary_vt00_00),

            ped_sex_general_action_Cond in ["vt00_01", "vt00_02", "vt00_03", "vt00_04", "vt00_05"], At("gensex_missionary_mc_tongue_01", ped05_sex_missionary_vt00_xx),

            ped_sex_general_action_Cond in ["vt01_01", "vt01_02", "vt01_03", "vt01_04", "vt01_05"], At("gensex_missionary_mc_tongue_01", ped05_sex_missionary_vt01_xx),

            ped_sex_general_action_Cond in ["vt02_01", "vt02_02", "vt02_03", "vt02_04", "vt02_05"], At("gensex_missionary_mc_tongue_01", ped05_sex_missionary_vt02_xx),

            "True", Null()

            )
    
# DICK

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["00"], At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_00),

            ped_sex_general_action_Cond == "vcum01", At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_vcum01),
            ped_sex_general_action_Cond == "vcum02", At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_vcum02),

            ped_sex_general_action_Cond == "acum01", At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_acum01),
            ped_sex_general_action_Cond == "acum02", At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_acum02),

            ped_sex_general_action_Cond == "v00_00", At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_v00_00),

            ped_sex_general_action_Cond in ["v00_01", "v00_02", "v00_03", "v00_04", "v00_05"], At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_v00_xx),

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05"], At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_v01_xx),
            
            ped_sex_general_action_Cond in ["v02_01", "v02_02", "v02_03", "v02_04", "v02_05"], At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_v02_xx),

            ped_sex_general_action_Cond == "a00_00", At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_a00_00),

            ped_sex_general_action_Cond in ["a00_01", "a00_02", "a00_03", "a00_04", "a00_05"], At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_a00_xx),

            ped_sex_general_action_Cond in ["a01_01", "a01_02", "a01_03", "a01_04", "a01_05"], At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_a01_xx),
            
            ped_sex_general_action_Cond in ["a02_01", "a02_02", "a02_03", "a02_04", "a02_05"], At("gensex_missionary_mc_dick", ped05_sex_missionary_dick_a02_xx),
            "True", Null()
            )

## STOMACH COVER

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05", "a01_01", "a01_02", "a01_03", "a01_04", "a01_05"], At("gensex_missionary_n_cover", ped05_sex_missionary_body_v01_xx),

            ped_sex_general_action_Cond in ["v02_01", "v02_02", "v02_03", "v02_04", "v02_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05"], At("gensex_missionary_n_cover", ped05_sex_missionary_body_v02_xx),

            "True", At("gensex_missionary_n_cover", truecenter)
            )

## ANAL OVER

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond == "acum01", At("gensex_missionary_n_over_anal_fucked", ped05_sex_missionary_analOver_acum01),
            ped_sex_general_action_Cond == "acum02", At("gensex_missionary_n_over_anal_fucked", ped05_sex_missionary_analOver_acum02),

            ped_sex_general_action_Cond in ["a01_01", "a01_02", "a01_03", "a01_04", "a01_05",], At("gensex_missionary_n_over_anal_fucked", ped05_sex_missionary_analOver_a01_xx),

            ped_sex_general_action_Cond in ["a02_01", "a02_02", "a02_03", "a02_04", "a02_05",], At("gensex_missionary_n_over_anal_fucked", ped05_sex_missionary_analOver_a02_xx),

            "True", Null()
            )
    
## LEGS VAGINAL-ANAL

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["vcum01", "vcum02"], At("gensex_missionary_n_legs_vaginal", ped05_sex_missionary_legs_vcum01),

            ped_sex_general_action_Cond in ["acum01", "acum02"], At("gensex_missionary_n_legs_anal", ped05_sex_missionary_legs_vcum01),

            ped_sex_general_action_Cond in ["v01_01", "v01_02","v01_03","v01_04","v01_05"], At("gensex_missionary_n_legs_vaginal", ped05_sex_missionary_legs_v01_xx),

            ped_sex_general_action_Cond in ["v02_01", "v02_02","v02_03","v02_04","v02_05"], At("gensex_missionary_n_legs_vaginal", ped05_sex_missionary_legs_v02_xx),

            ped_sex_general_action_Cond in ["a01_01", "a01_02","a01_03","a01_04","a01_05"], At("gensex_missionary_n_legs_anal", ped05_sex_missionary_legs_v01_xx),
            
            ped_sex_general_action_Cond in ["a02_01", "a02_02","a02_03","a02_04","a02_05"], At("gensex_missionary_n_legs_anal", ped05_sex_missionary_legs_v02_xx),

            "True", At("gensex_missionary_n_legs_vaginal", truecenter)
            )

## PUSSY OVER

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond == "vcum01", At("gensex_missionary_n_over_vaginal_fucked", ped05_sex_missionary_vaginalOver_vcum01),
            ped_sex_general_action_Cond == "vcum02", At("gensex_missionary_n_over_vaginal_fucked", ped05_sex_missionary_vaginalOver_vcum02),

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05"], At("gensex_missionary_n_over_vaginal_fucked", ped05_sex_missionary_vaginalOver_v01_xx),

            ped_sex_general_action_Cond in ["v02_01", "v02_02", "v02_03", "v02_04", "v02_05"], At("gensex_missionary_n_over_vaginal_fucked", ped05_sex_missionary_vaginalOver_v02_xx),

            ped_sex_general_action_Cond in ["vt01_01", "vt01_02", "vt01_03", "vt01_04", "vt01_05"], At("gensex_missionary_n_over_vaginal_licked", ped05_sex_missionary_vaginalOver_vt01_xx),

            ped_sex_general_action_Cond in ["vt02_01", "vt02_02", "vt02_03", "vt02_04", "vt02_05"], At("gensex_missionary_n_over_vaginal_licked", ped05_sex_missionary_vaginalOver_vt02_xx),

            "True", Null()
            )

#     #     ## BOOBS

#     # contains:
#     #     ConditionSwitch(

#     #         ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05", "a01_01", "a01_02", "a01_03", "a01_04", "a01_05"], At("gensex_missionary02_n_boobs", ped05_sex_missionary_boobs_v01_xx),

#     #         ped_sex_general_action_Cond in ["v02_01", "v02_02", "v02_03", "v02_04", "v02_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05"], At("gensex_missionary02_n_boobs", ped05_sex_missionary_boobs_v02_xx),

#     #         "True", At("gensex_missionary02_n_boobs", ped05_sex_missionary_boobs_v00_00)
#     #         )


# ## TEST IMAGE FOR EXPRESSIONS POSITION
#     contains:
#         "gensex_missionary_n_PROVE"
#         truecenter


## FACE
    
    contains:
        "gensex_missionary_n_head_face"
        ped_missionary_n_exp_comp_pos


####################

        ## EXPRESSIONS MISSIONARY

    contains:
        ConditionSwitch(

                ped_sex_general_expression_Cond != "talk" and nblushNumber < 1, At("gensex_missionary_n_head_exp_blush 01", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond != "talk" and nblushNumber > 8, At("gensex_missionary_n_head_exp_blush 08", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond != "talk", At("gensex_missionary_n_head_exp_blush " + nblushNumber, ped_missionary_n_exp_comp_pos),
                "True", Null()
                )

    ## EYES

    contains:
        ConditionSwitch(
                ped_sex_general_expression_Cond == "closed", At("gensex_missionary_n_head_exp_eyes 08", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "indifferent", At("gensex_missionary_n_head_exp_eyes 08", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "lust", At("gensex_missionary_n_head_exp_eyes 04", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "angry", At("gensex_missionary_n_head_exp_eyes 06", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "angryFront", At("gensex_missionary_n_head_exp_eyes 05", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond in ["surpriseLeft", "surpriseRight"], At("gensex_missionary_n_head_exp_eyes 01", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "surpriseDown", At("gensex_missionary_n_head_exp_eyes 01", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "talk", Null(),
                "True", Null()
                )

    ## PIRIS

    contains:
        ConditionSwitch(
                ped_sex_general_expression_Cond == "closed", At("gensex_missionary_n_head_exp_iris empty", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "indifferent", At("gensex_missionary_n_head_exp_iris empty", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "lust", At("gensex_missionary_n_head_exp_iris front04", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "angry", At("gensex_missionary_n_head_exp_iris empty", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "angryFront", At("gensex_missionary_n_head_exp_iris front05", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "surpriseLeft", At("gensex_missionary_n_head_exp_iris left01", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "surpriseRight", At("gensex_missionary_n_head_exp_iris right01", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "surpriseDown", At("gensex_missionary_n_head_exp_iris down01", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "talk", Null(),
                "True", Null()
                )

    contains:
        ConditionSwitch(
                ntlong == 0, Null(),
                ped_sex_general_expression_Cond == "closed", At("gensex_missionary_n_head_exp_tears 08_" + s_ntlong, ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "indifferent", At("gensex_missionary_n_head_exp_tears 08_" + s_ntlong, ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "lust", At("gensex_missionary_n_head_exp_tears 04_" + s_ntlong, ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "angry", At("gensex_missionary_n_head_exp_tears 06_" + s_ntlong, ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "angryFront", At("gensex_missionary_n_head_exp_tears 05_" + s_ntlong, ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond in ["surpriseLeft", "surpriseRight"], At("gensex_missionary_n_head_exp_tears 01_" + s_ntlong, ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "surpriseDown", At("gensex_missionary_n_head_exp_tears 01_" + s_ntlong, ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "talk", Null(),
                "True", Null()
                )


    ## EYEBROWS

    contains:
        ConditionSwitch(
                ped_sex_general_expression_Cond == "closed", At("gensex_missionary_n_head_exp_eyebrows sadx05", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "indifferent", At("gensex_missionary_n_head_exp_eyebrows surprisex01", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "lust", At("gensex_missionary_n_head_exp_eyebrows suspiciousx03", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "angry", At("gensex_missionary_n_head_exp_eyebrows angryx07", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "angryFront", At("gensex_missionary_n_head_exp_eyebrows angryx07", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond in ["surpriseLeft", "surpriseRight"], At("gensex_missionary_n_head_exp_eyebrows surprisex02", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "surpriseDown", At("gensex_missionary_n_head_exp_eyebrows surprisex02", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "talk", Null(),
                "True", Null()
                )

    ## MOUTH

    contains:
        ConditionSwitch(
                ped_sex_general_expression_Cond == "closed", At("gensex_missionary_n_head_exp_mouth sadbiting_Silentx06", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "indifferent", At("gensex_missionary_n_head_exp_mouth sad_Silentx03", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "lust", At("gensex_missionary_n_head_exp_mouth happybiting_Silentx07", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "angry", At("gensex_missionary_n_head_exp_mouth sadbiting_Silentx06", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "angryFront", At("gensex_missionary_n_head_exp_mouth sadbiting_Silentx06", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond in ["surpriseLeft", "surpriseRight"], At("gensex_missionary_n_head_exp_mouth sadbiting_Silentx06", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "surpriseDown", At("gensex_missionary_n_head_exp_mouth sadbiting_Silentx06", ped_missionary_n_exp_comp_pos),
                ped_sex_general_expression_Cond == "talk", Null(),

                "True", Null()
                )

    ## GLASSES

    # contains:
    #     "gensex_missionary_n_head_glasses"
    #     ped_missionary_n_exp_comp_pos

    contains:
        ConditionSwitch(
            ped_sex_general_expression_Cond != "talk" and p_activeno == "_n" and n_withoutGlasses_story == False and n_withoutGlasses_Cond == False, At("gensex_missionary_n_head_glasses", ped_missionary_n_exp_comp_pos),
            "True", Null()
        )


    ## HAIR FRONT

    contains:
        ConditionSwitch(ped_sex_general_expression_Cond == "talk", Null(),
                "True", At("gensex_missionary_n_head_hairfront", ped_missionary_n_exp_comp_pos)
                )


############################################################################################################
############################################################################################################
##########################################################################################
##########################################################################################
############################################################################################################
############################################################################################################

############################################################################################################
############################################################################################################
##########################################################################################
##########################################################################################
############################################################################################################
############################################################################################################

transform ped_missionary02_d_exp_comp_pos:
    truecenter
    #zoom 1.0
    zoom 0.4
    ypos -0.155
    #alpha 0.0

transform ped_missionary_n_exp_comp_pos:
    truecenter
    zoom 0.4
    #ypos -0.055
    ypos -0.05
    #alpha 0.75

###

transform ped_missionary02_d_exp_zoom05_pos:
    truecenter
    #zoom 0.5
    zoom 0.2
    ypos 0.175
    #alpha 0.75

transform ped_missionary02_n_exp_zoom05_pos:
    truecenter
    zoom 0.2
    ypos 0.224
    #alpha 0.75
##

transform ped_missionary02_d_exp_face_pos:
    truecenter
    #zoom 1.5
    zoom 0.6
    ypos 0.372

transform ped_missionary02_n_exp_face_pos:
    truecenter
    zoom 0.6
    ypos 0.372



###

## ORAL blowjob POSITION


transform pedrera_sex_didac_general_speaking_close_exp_pos:
    truecenter
    zoom 1.4
    #zoom 0.32
    xpos 0.5 ypos 0.229 

transform pedrera_sex_didac_general_speaking_exp_pos:
    truecenter
    zoom 0.8
    #zoom 0.32
    ypos 0.229 xpos 0.6
    #alpha 0.75

transform pedrera_sex_didac_general_speakingCentered_exp_pos:
    truecenter
    zoom 0.8
    #zoom 0.32
    ypos 0.229 xpos 0.5
    #alpha 0.75

###


############################################################################################################
############################################################################################################
##########################################################################################
##########################################################################################
############################################################################################################
############################################################################################################

############################################################################################################
############################################################################################################
##########################################################################################
##########################################################################################
############################################################################################################
############################################################################################################ DIDAC

## DOGGY DIDAC

# image gensex_doggy_d_REFERENCE = "images/general/sex/doggy/didac/gensex_doggy_d_REFERENCE.webp"
# image gensex_doggy_d_REFERENCE02 = "images/general/sex/doggy/didac/gensex_doggy_d_REFERENCE02.webp"

image gensex_doggy_d_bg = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_bg.webp")

image gensex_doggy_d_body = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_body.webp")

image gensex_doggy_d_but_L = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_but_L_[p_d_butS_L].webp")
image gensex_doggy_d_but_R = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_but_R_[p_d_butS_R].webp")

image gensex_doggy_d_dabove_anal_closed = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_dabove_anal_closed.webp")
image gensex_doggy_d_dabove_anal_penetrated = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_dabove_anal_penetrated.webp")
image gensex_doggy_d_dabove_vaginal_penetrated = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_dabove_vaginal_penetrated.webp")
image gensex_doggy_d_dbelow_vaginal_closed = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_dbelow_vaginal_closed.webp")

image gensex_doggy_d_hands = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_hands.webp")
image gensex_doggy_d_head = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_head.webp")
image gensex_doggy_d_legs = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_legs.webp")

############################################################################################################
############################################################################################################

image gensex_doggy_d_squirt 01 = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_squirt_01.webp")
image gensex_doggy_d_squirt 02 = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_squirt_02.webp")
image gensex_doggy_d_squirt 03 = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_squirt_03.webp")
image gensex_doggy_d_squirt 04 = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_squirt_04.webp")

image gensex_doggy_d_squirt_bed 01 = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_squirt_bed_01.webp")
image gensex_doggy_d_squirt_bed 02 = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_squirt_bed_02.webp")
image gensex_doggy_d_squirt_bed 03 = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_squirt_bed_03.webp")
image gensex_doggy_d_squirt_bed 04 = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_squirt_bed_04.webp")
image gensex_doggy_d_squirt_bed 05 = SaturateTint("images/general/sex/doggy/didac/gensex_doggy_d_squirt_bed_05.webp")


############################################################################################################
############################################################################################################
##########################################################################################
##########################################################################################
############################################################################################################
############################################################################################################ NEUS

## DOGGY NEUS

image gensex_doggy_n_REFERENCE = "images/general/sex/doggy/neus/gensex_doggy_n_REFERENCE.webp"

image gensex_doggy_n_bg = SaturateTint("images/general/sex/doggy/neus/gensex_doggy_n_bg.webp")

image gensex_doggy_n_body = SaturateTint("images/general/sex/doggy/neus/gensex_doggy_n_body.webp")

image gensex_doggy_n_but_L = SaturateTint("images/general/sex/doggy/neus/gensex_doggy_n_but_L_[p_n_butS_L].webp")
image gensex_doggy_n_but_R = SaturateTint("images/general/sex/doggy/neus/gensex_doggy_n_but_R_[p_n_butS_R].webp")

image gensex_doggy_n_dabove_anal_closed = SaturateTint("images/general/sex/doggy/neus/gensex_doggy_n_dabove_anal_closed.webp")
image gensex_doggy_n_dabove_anal_penetrated = SaturateTint("images/general/sex/doggy/neus/gensex_doggy_n_dabove_anal_penetrated.webp")
image gensex_doggy_n_dabove_vaginal_penetrated = SaturateTint("images/general/sex/doggy/neus/gensex_doggy_n_dabove_vaginal_penetrated.webp")
image gensex_doggy_n_dbelow_vaginal_closed = SaturateTint("images/general/sex/doggy/neus/gensex_doggy_n_dbelow_vaginal_closed.webp")


image gensex_doggy_n_hands = SaturateTint("images/general/sex/doggy/neus/gensex_doggy_n_hands.webp")
image gensex_doggy_n_head = SaturateTint("images/general/sex/doggy/neus/gensex_doggy_n_head.webp")
image gensex_doggy_n_legs = SaturateTint("images/general/sex/doggy/neus/gensex_doggy_n_legs.webp")
image gensex_doggy_n_hairground = SaturateTint("images/general/sex/doggy/neus/gensex_doggy_n_hairground.webp")


############################################################################################################
############################################################################################################
##########################################################################################
##########################################################################################
############################################################################################################

#### TRANSFORMS

## HANDS

transform gensex_doggy_d_hands_trans_00_00:
    truecenter

    # V01

transform gensex_doggy_d_hands_trans_v01_xx:
    subpixel True
    truecenter
    block:
        ease 4.0/ped_sex_num  ypos 0.49
        ease 4.0/ped_sex_num  ypos 0.5
        repeat

## HEAD

transform gensex_doggy_d_head_trans_00_00:
    truecenter

    ## V01

transform gensex_doggy_d_head_trans_v01_xx:
    subpixel True
    truecenter
    block:
        ease 4.0/ped_sex_num  ypos 0.502
        ease 4.0/ped_sex_num  ypos 0.5
        repeat

transform gensex_doggy_n_head_trans_v01_xx:
    subpixel True
    truecenter
    block:
        pause 2.0/ped_sex_num
        ease 2.0/ped_sex_num  ypos 0.5
        ease 4.0/ped_sex_num  ypos 0.502
        repeat


## LEGS

transform gensex_doggy_d_legs_trans_00_00:
    truecenter

    # V01

transform gensex_doggy_d_legs_trans_v01_xx:
    subpixel True
    truecenter
    block:
        pause 2.0/ped_sex_num 
        easeout 2.0/ped_sex_num  ypos 0.495 # R_Half Dick
        easein 4.0/ped_sex_num  ypos 0.5 # R_Original
        repeat

transform gensex_doggy_d_legs_trans_vdcum01:
    subpixel True
    truecenter
    parallel:
        easein_quad 0.5 ypos 0.49
        easeout 0.5 ypos 0.49 # R_Half Dick
        easein 1.0 ypos 0.5 # R_Original
        repeat
    parallel:
        easeout_quad 0.5 xpos 0.505
        easein_quad 0.5 xpos 0.5
        ease 0.5 xpos 0.495
        ease 0.5 xpos 0.5
        repeat

## BODY

transform gensex_doggy_d_body_trans_00_00:
    subpixel True
    truecenter
    zoom 2.0

    # V01

transform gensex_doggy_d_body_trans_v01_xx:
    subpixel True
    truecenter
    zoom 2.0
    block:
        pause 2.0/ped_sex_num 
        easeout 2.0/ped_sex_num  ypos 0.495 # R_Half Dick
        easein 4.0/ped_sex_num  ypos 0.5 # R_Original
        repeat

transform gensex_doggy_n_body_trans_v01_xx:
    subpixel True
    truecenter
    zoom 2.0
    block:
        pause 2.0/ped_sex_num 
        easeout 2.0/ped_sex_num  ypos 0.49 # R_Half Dick
        easein 4.0/ped_sex_num  ypos 0.5 # R_Original
        repeat

## BUT_L

transform gensex_doggy_d_but_L_trans_00_00:
    transform_anchor True
    xalign 0.6 yalign 0.5 
    xpos 0.32 ypos 0.86 xzoom 1.0 yzoom 1.0 # L_Original

transform gensex_doggy_n_but_L_trans_00_00:
    transform_anchor True
    xalign 0.6 yalign 0.5 
    xpos 0.32 ypos 0.86 xzoom 1.0 yzoom 1.0 # L_Original

    # transform_anchor True
    # xalign 0.65 yalign 0.5
    # rotate 0.0
    # block:
    #     rotate 0.0
    #     ease 10.0 rotate 360
    #     repeat

    #xpos 0.32 ypos 0.86 xzoom 1.0 yzoom 1.0 

    # V01

transform gensex_doggy_d_but_L_trans_v01_xx:
    subpixel True
    transform_anchor True
    xalign 0.6 yalign 0.5 
    xpos 0.32 ypos 0.86 xzoom 1.0 yzoom 1.0 # L_Original
    block:
        pause 2.0/ped_sex_num 
        easeout 2.0/ped_sex_num  ypos 0.855 xzoom 1.01 yzoom 0.99 # R_Half Dick
        easein 4.0/ped_sex_num  ypos 0.86 xzoom 1.0 yzoom 1.0 # R_Original
        repeat

transform gensex_doggy_n_but_L_trans_v01_xx:
    subpixel True
    transform_anchor True
    xalign 0.6 yalign 0.5 
    xpos 0.32 ypos 0.86 xzoom 1.0 yzoom 1.0 # L_Original
    block:
        pause 2.0/ped_sex_num 
        easeout 2.0/ped_sex_num  ypos 0.855 xzoom 1.01 yzoom 0.99 # R_Half Dick
        easein 4.0/ped_sex_num  ypos 0.86 xzoom 1.0 yzoom 1.0 # R_Original
        repeat

transform gensex_doggy_d_but_L_trans_vdcum01:
    subpixel True
    transform_anchor True
    xalign 0.6 yalign 0.5 
    xpos 0.32 ypos 0.86 xzoom 1.0 yzoom 1.0 # L_Original
    parallel:
        ease_quad 0.25 xzoom 1.0 yzoom 1.0 # R_Original
        easeout_quad 0.25 xzoom 1.01 yzoom 0.995 # R_Half Dick
        easein_quad 0.25 xzoom 0.995 yzoom 1.005 # 
        ease_quad 0.25 xzoom 1.01 yzoom 0.995 #
        repeat
    parallel:
        easeout_quad 0.35 ypos 0.855
        easein_quad 0.35 ypos 0.86
        easeout_cubic 0.35 ypos 0.853
        ease_quad 0.35 ypos 0.862
        repeat
    parallel:
        ease_quad 0.5 xpos 0.319
        easein_quad 0.5 xpos 0.325
        ease_quad 0.5 xpos 0.315
        easeout_quad 0.5 xpos 0.321
        repeat


transform gensex_doggy_n_but_L_trans_vdcum01:
    subpixel True
    transform_anchor True
    xalign 0.6 yalign 0.5 
    xpos 0.32 ypos 0.86 xzoom 1.0 yzoom 1.0 # L_Original
    parallel:
        ease_quad 0.25 xzoom 1.0 yzoom 1.0 # R_Original
        easeout_quad 0.25 xzoom 1.01 yzoom 0.995 # R_Half Dick
        easein_quad 0.25 xzoom 0.995 yzoom 1.005 # 
        ease_quad 0.25 xzoom 1.01 yzoom 0.995 #
        repeat
    parallel:
        easeout_quad 0.35 ypos 0.855
        easein_quad 0.35 ypos 0.86
        easeout_cubic 0.35 ypos 0.853
        ease_quad 0.35 ypos 0.862
        repeat
    parallel:
        ease_quad 0.5 xpos 0.319
        easein_quad 0.5 xpos 0.325
        ease_quad 0.5 xpos 0.315
        easeout_quad 0.5 xpos 0.321
        repeat



## BUT_R

transform gensex_doggy_d_but_R_trans_00_00:
    transform_anchor True
    xalign 0.4 yalign 0.5
    xpos 0.68 ypos 0.86 xzoom 1.0 yzoom 1.0 # R_Original

transform gensex_doggy_n_but_R_trans_00_00:
    transform_anchor True
    xalign 0.4 yalign 0.5
    xpos 0.68 ypos 0.86 xzoom 1.0 yzoom 1.0 # R_Original


    # V01

transform gensex_doggy_d_but_R_trans_v01_xx:
    subpixel True
    transform_anchor True
    xalign 0.4 yalign 0.5
    xpos 0.68 ypos 0.86 xzoom 1.0 yzoom 1.0 # R_Original
    block:
        pause 2.0/ped_sex_num 
        easeout 2.0/ped_sex_num  ypos 0.855 xzoom 1.01 yzoom 0.99 # R_Half Dick
        easein 4.0/ped_sex_num  ypos 0.86 xzoom 1.0 yzoom 1.0 # R_Original
        repeat

transform gensex_doggy_n_but_R_trans_v01_xx:
    subpixel True
    transform_anchor True
    xalign 0.4 yalign 0.5
    xpos 0.68 ypos 0.86 xzoom 1.0 yzoom 1.0 # R_Original
    block:
        pause 2.0/ped_sex_num 
        easeout 2.0/ped_sex_num  ypos 0.855 xzoom 1.01 yzoom 0.99 # R_Half Dick
        easein 4.0/ped_sex_num  ypos 0.86 xzoom 1.0 yzoom 1.0 # R_Original
        repeat


transform gensex_doggy_d_but_R_trans_vdcum01:
    subpixel True
    transform_anchor True
    xalign 0.4 yalign 0.5
    xpos 0.68 ypos 0.86 xzoom 1.0 yzoom 1.0 # R_Original
    parallel:
        ease_quad 0.25 xzoom 1.0 yzoom 1.0 # R_Original
        easeout_quad 0.25 xzoom 1.01 yzoom 0.995 # R_Half Dick
        easein_quad 0.25 xzoom 0.995 yzoom 1.005 # 
        ease_quad 0.25 xzoom 1.01 yzoom 0.995 #
        repeat
    parallel:
        easein_quad 0.35 ypos 0.86
        easeout_quad 0.35 ypos 0.855
        ease_quad 0.35 ypos 0.862
        easeout_cubic 0.35 ypos 0.853
        repeat
    parallel:
        easein_quad 0.5 xpos 0.685
        ease_quad 0.5 xpos 0.678
        easeout_quad 0.5 xpos 0.682
        ease_quad 0.5 xpos 0.675
        repeat

transform gensex_doggy_n_but_R_trans_vdcum01:
    subpixel True
    transform_anchor True
    xalign 0.4 yalign 0.5
    xpos 0.68 ypos 0.86 xzoom 1.0 yzoom 1.0 # R_Original
    parallel:
        ease_quad 0.25 xzoom 1.0 yzoom 1.0 # R_Original
        easeout_quad 0.25 xzoom 1.01 yzoom 0.995 # R_Half Dick
        easein_quad 0.25 xzoom 0.995 yzoom 1.005 # 
        ease_quad 0.25 xzoom 1.01 yzoom 0.995 #
        repeat
    parallel:
        easein_quad 0.35 ypos 0.86
        easeout_quad 0.35 ypos 0.855
        ease_quad 0.35 ypos 0.862
        easeout_cubic 0.35 ypos 0.853
        repeat
    parallel:
        easein_quad 0.5 xpos 0.685
        ease_quad 0.5 xpos 0.678
        easeout_quad 0.5 xpos 0.682
        ease_quad 0.5 xpos 0.675
        repeat


## VAGINAL

transform gensex_doggy_d_dbelow_vaginal_closed_trans_00_00:
    truecenter
    xpos 0.5 ypos 0.93

    ## V01 NOT PENETRATED

transform gensex_doggy_d_dbelow_vaginal_closed_trans_v01_xx:
    subpixel True
    truecenter
    xpos 0.5 ypos 0.93
    block:
        easein 4.0/ped_sex_num  ypos 0.9
        easeout 4.0/ped_sex_num  ypos 0.93
        repeat

transform gensex_doggy_d_dbelow_vaginal_closed_trans_dcum:
    subpixel True
    truecenter
    xpos 0.5 ypos 0.93
    parallel:
        easein_bounce 2.0 ypos 0.9
        easeout_bounce 2.0 ypos 0.93
        repeat
    parallel:
        easein_bounce 2.1 xpos 0.505
        ease 1.8 xpos 0.499
        repeat
    parallel:
        ease_bounce 1.0 xzoom 1.05
        ease_bounce 1.0 xzoom 0.95
    parallel:
        ease_bounce 1.5 yzoom 1.05
        ease_bounce 0.5 yzoom 0.95

    ## V01 PENETRATED

transform gensex_doggy_d_dabove_vaginal_penetrated_trans_v01_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.7
    # ypos 1.17 xzoom 1.0 yzoom 1.0 # Vaginal Low
    # ypos 1.14 xzoom 1.0 yzoom 1.05 # Half Dick Inside
    ypos 1.22 xzoom 0.7 yzoom 0.8 # Beginning Pussy
    parallel:
        easein_quart 4.0/ped_sex_num  xzoom 1.0 yzoom 1.05 # Half Dick Inside
        easeout_expo 4.0/ped_sex_num  xzoom 0.8 yzoom 0.8 # Beginning Pussy
        repeat
    parallel:
        ease 4.0/ped_sex_num  ypos 1.14 # Half Dick Inside
        ease 4.0/ped_sex_num  ypos 1.22 # Beginning Pussy
        repeat

##
transform gensex_doggy_d_dabove_vaginal_penetrated_trans_vcum01:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.7
    # ypos 1.17 xzoom 1.0 yzoom 1.0 # Vaginal Low
    # ypos 1.14 xzoom 1.0 yzoom 1.05 # Half Dick Inside
    ypos 1.22 xzoom 0.7 yzoom 0.8 # Beginning Pussy
    easein_quart 2.0 xzoom 1.0 yzoom 1.05 ypos 1.14 # Half Dick Inside
    block:
        ease 0.5 xzoom 1.05 yzoom 1.0
        ease 0.5 xzoom 1.0 yzoom 1.05
        repeat

## ANAL

transform gensex_doggy_d_dabove_anal_closed_trans_00_00:
    truecenter
    xpos 0.5 ypos 0.93


    ## AT01 PENETRATED

transform gensex_doggy_d_dabove_anal_penetrated_trans_at01_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.7
    ypos 1.12 xzoom 0.75 yzoom 0.75 # Anal Beginning
    block:
        easein_quad 4.0/ped_sex_num  ypos 1.08 xzoom 1.0 yzoom 1.05 # Anal Half
        ease_quad 4.0/ped_sex_num  ypos 1.12 xzoom 0.75 yzoom 0.75 # Anal Beginning
        repeat

    # A01

transform gensex_doggy_d_dabove_anal_penetrated_trans_a01_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.7
    ypos 1.12 xzoom 0.75 yzoom 0.75 # Anal Beginning
    block:
        ease_quad 4.0/ped_sex_num  ypos 1.08 xzoom 1.0 yzoom 1.05 # Anal Half
        ease_quad 4.0/ped_sex_num  ypos 1.12 xzoom 0.75 yzoom 0.75 # Anal Beginning
        repeat

    ##

transform gensex_doggy_d_dabove_anal_penetrated_trans_acum01:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.7
    ypos 1.12 xzoom 0.75 yzoom 0.75 # Anal Beginning
    ease_quad 2.0 ypos 1.08 xzoom 1.0 yzoom 1.05 # Anal Half
    block:
        ease 0.5 xzoom 1.05 yzoom 1.0
        ease 0.5 xzoom 1.0 yzoom 1.05
        repeat

## DICK

transform pedrera_sex_doggy_mc_dick_trans_00_00:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.78 zoom 0.8
    ypos 2.8

    # V00_00

transform pedrera_sex_doggy_mc_dick_trans_v00_00:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.78 zoom 0.8
    ypos 2.72 # Teasing Beginning

# V00_xx

transform pedrera_sex_doggy_mc_dick_trans_v00_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.78 zoom 0.8
    ypos 2.72 # Teasing Beginning
    parallel:
        ease_quad 4.0/ped_sex_num  ypos 2.58 # Vaginal Teasing Ending
        ease_quad 4.0/ped_sex_num  ypos 2.72 # Vaginal Teasing Beginning
        repeat
    parallel:
        ease 6.0/ped_sex_num  rotate 1
        ease 6.0/ped_sex_num  rotate -1
        repeat

    # A00

transform pedrera_sex_doggy_mc_dick_trans_a00_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.78 zoom 0.8
    ypos 2.58 # Anal Teasing Beginnig
    parallel:
        ease_quad 4.0/ped_sex_num  ypos 2.48 # Anal Teasing Ending
        ease_quad 4.0/ped_sex_num  ypos 2.58 # Anal Teasing Beginnig
        repeat
    parallel:
        ease 6.0/ped_sex_num  rotate 1
        ease 6.0/ped_sex_num  rotate -1
        repeat

    # V01

transform pedrera_sex_doggy_mc_dick_trans_v01_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.78 zoom 0.8
    # ypos 1.3 # Full Dick inside.
    # ypos 1.8 # Half Dick
    ypos 2.66 # Beginning Pussy.
    block:
        ease_quad 4.0/ped_sex_num  ypos 1.8 # Half Dick
        ease_quad 4.0/ped_sex_num  ypos 2.66 # Beginning Pussy.
        repeat


transform pedrera_sex_doggy_mc_dick_trans_vdcum01:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.78 zoom 0.8
    ypos 2.66 # Beginning Pussy.
    block:
        easein_quad 2.0 ypos 1.8 # Half Dick
        easeout_cubic 2.0 ypos 2.0 #
        repeat

transform pedrera_sex_doggy_mc_dick_trans_vcum01:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.78 zoom 0.8
    ypos 2.66 # Beginning Pussy.
    parallel:
        easein_quad 2.0 ypos 1.8 # Half Dick
        easeout_cubic 2.0 ypos 2.0 #
        repeat
    parallel:
        ease_bounce 1.0 xzoom 1.1
        easeout_cubic 0.5 xzoom 0.95
        easein_quad 0.5 xzoom 1.05
        easeout_elastic 1.0 xzoom 0.9
        easein_quad 0.5 xzoom 1.0
        repeat 4

transform pedrera_sex_doggy_mc_dick_trans_vdcum02:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.78 zoom 0.8
    ypos 2.66 # Beginning Pussy.
    block:
        easein_quad 2.0 ypos 1.3 # Full Dick inside.
        easeout_cubic 2.0 ypos 2.0 #
        repeat

transform pedrera_sex_doggy_mc_dick_trans_vcum02:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.78 zoom 0.8
    ypos 2.66 # Beginning Pussy.
    parallel:
        easein_quad 2.0 ypos 1.3 # Full Dick inside.
        easeout_cubic 2.0 ypos 1.4 #
        repeat
    parallel:
        ease_bounce 1.0 xzoom 1.1
        easeout_cubic 0.5 xzoom 0.95
        easein_quad 0.5 xzoom 1.05
        easeout_elastic 1.0 xzoom 0.9
        easein_quad 0.5 xzoom 1.0
        repeat 4


    # V02

transform pedrera_sex_doggy_mc_dick_trans_v02_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.78 zoom 0.8
    # ypos 1.3 # Full Dick inside.
    # ypos 1.8 # Half Dick
    ypos 2.66 # Beginning Pussy.
    block:
        ease_quad 4.0/ped_sex_num  ypos 1.3 # Full Dick inside.
        ease_quad 4.0/ped_sex_num  ypos 2.66 # Beginning Pussy.
        repeat

    # A01

transform pedrera_sex_doggy_mc_dick_trans_a01_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.78 zoom 0.8
    # ypos 1.25 # Anal Full
    ypos 2.57 # Anal Beginning.
    block:
        ease_quad 4.0/ped_sex_num  ypos 2.0 # Anal Half
        ease_quad 4.0/ped_sex_num  ypos 2.57 # Anal Beginning.
        repeat

    # A02

transform pedrera_sex_doggy_mc_dick_trans_a02_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.78 zoom 0.8
    ypos 2.57 # Anal Beginning.
    block:
        ease_quad 4.0/ped_sex_num  ypos 1.25 # Anal Full
        ease_quad 4.0/ped_sex_num  ypos 2.57 # Anal Beginning.
        repeat

        ##

transform pedrera_sex_doggy_mc_dick_trans_adcum01:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.78 zoom 0.8
    ypos 2.57 # Anal Beginning.
    block:
        easein_quad 2.0 ypos 2.0 # Anal Half
        easeout_cubic 2.0 ypos 2.2 #
        repeat

transform pedrera_sex_doggy_mc_dick_trans_acum01:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.78 zoom 0.8
    ypos 2.57 # Anal Beginning.
    parallel:
        ease_bounce 2.0 ypos 1.8 # Anal Half
        repeat
    parallel:
        ease_bounce 1.0 xzoom 1.1
        easeout_cubic 0.5 xzoom 0.95
        easein_quad 0.5 xzoom 1.05
        easeout_elastic 1.0 xzoom 0.9
        easein_quad 0.5 xzoom 1.0
        repeat 4

transform pedrera_sex_doggy_mc_dick_trans_adcum02:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.78 zoom 0.8
    ypos 2.57 # Anal Beginning.
    block:
        easein_quad 2.0 ypos 1.25 # Anal Full
        easeout_cubic 2.0 ypos 2.0 #
        repeat

transform pedrera_sex_doggy_mc_dick_trans_acum02:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.78 zoom 0.8
    ypos 2.57 # Anal Beginning.
    parallel:
        ease_bounce 2.0 ypos 1.25 # Anal Full
        repeat
    parallel:
        ease_bounce 1.0 xzoom 1.1
        easeout_cubic 0.5 xzoom 0.95
        easein_quad 0.5 xzoom 1.05
        easeout_elastic 1.0 xzoom 0.9
        easein_quad 0.5 xzoom 1.0
        repeat 4

## TONGUE

transform pedrera_sex_doggy_mc_tongue_trans_00_00:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.72
    zoom 1.9
    ypos 1.4 # Anal Tongue Beginning

    ## ANAL TONGUE 00 (Teasing)

transform pedrera_sex_doggy_mc_tongue_trans_at00_00:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.72
    zoom 1.9
    ypos 1.45 # Anal Tongue Beginning
    parallel:
        ease 4.0 ypos 1.4 # Anal Tongue ALL in
        ease 4.0 ypos 1.45 # Anal Tongue Beginning
        repeat
    parallel:
        ease 4.5 rotate 1
        ease 4.5 rotate -1
        repeat
    parallel:
        ease 4.8 xzoom 0.99 yzoom 1.01
        ease 4.8 xzoom 1.01 yzoom 0.99
        repeat

transform pedrera_sex_doggy_mc_tongue_trans_at00_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.72
    zoom 1.9
    ypos 1.45 # Anal Tongue Beginning
    parallel:
        ease 2.0/ped_sex_num  ypos 1.4 # Anal Tongue ALL in
        ease 2.0/ped_sex_num  ypos 1.45 # Anal Tongue Beginning
        repeat
    parallel:
        ease 2.5/ped_sex_num  rotate 1
        ease 2.5/ped_sex_num  rotate -1
        repeat
    parallel:
        ease 1.8/ped_sex_num  xzoom 0.99 yzoom 1.01
        ease 1.8/ped_sex_num  xzoom 1.01 yzoom 0.99
        repeat

# transform pedrera_sex_doggy_mc_tongue_trans_at00_01:
#     transform_anchor True
#     xalign 0.5 yalign 0.72
#     zoom 1.9
#     ypos 1.45 # Anal Tongue Beginning
#     parallel:
#         ease 2.0 ypos 1.4 # Anal Tongue ALL in
#         ease 2.0 ypos 1.45 # Anal Tongue Beginning
#         repeat
#     parallel:
#         ease 2.5 rotate 1
#         ease 2.5 rotate -1
#         repeat
#     parallel:
#         ease 1.8 xzoom 0.99 yzoom 1.01
#         ease 1.8 xzoom 1.01 yzoom 0.99
#         repeat

# transform pedrera_sex_doggy_mc_tongue_trans_at00_02:
#     transform_anchor True
#     xalign 0.5 yalign 0.72
#     zoom 1.9
#     ypos 1.4 # Anal Tongue Beginning

# transform pedrera_sex_doggy_mc_tongue_trans_at00_03:
#     transform_anchor True
#     xalign 0.5 yalign 0.72
#     zoom 1.9
#     ypos 1.4 # Anal Tongue Beginning

# transform pedrera_sex_doggy_mc_tongue_trans_at00_04:
#     transform_anchor True
#     xalign 0.5 yalign 0.72
#     zoom 1.9
#     ypos 1.4 # Anal Tongue Beginning

# transform pedrera_sex_doggy_mc_tongue_trans_at00_05:
#     transform_anchor True
#     xalign 0.5 yalign 0.72
#     zoom 1.9
#     ypos 1.4 # Anal Tongue Beginning

    ## ANAL TONGUE 01 (ANNILINGUS)

transform pedrera_sex_doggy_mc_tongue_trans_at01_xx:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.72
    zoom 1.9
    ypos 1.4 # Anal Tongue Beginning
    parallel:
        ease 4.0/ped_sex_num  ypos 1.2 # Anal
        ease 4.0/ped_sex_num  ypos 1.4 # Anal Tongue Beginning
        repeat
    parallel:
        ease 3.5/ped_sex_num  rotate 2
        ease 3.5/ped_sex_num  rotate -2
        repeat
    parallel:
        ease 2.8/ped_sex_num  xzoom 0.9 yzoom 1.1
        ease 2.8/ped_sex_num  xzoom 1.1 yzoom 0.9
        repeat
###
###

transform gensex_doggy_d_squirt_bed_trans:
    transform_anchor True
    xalign 0.5 yalign 0.1
    xpos 0.5 ypos 1.22

transform gensex_doggy_d_squirt_trans:
    subpixel True
    transform_anchor True
    xalign 0.5 yalign 0.1
    xpos 0.5 ypos 1.22
    zoom 0.0
    parallel:
        easein_quad 0.5 alpha 1.0
        easeout_quad 1.0 alpha 0.0
        pause 2.0
        repeat 2
    parallel:
        easein_quad 0.5 zoom 0.9
        easeout_quad 1.5 zoom 1.1
        zoom 0.0
        pause 1.5
        repeat 2

##
##

transform gensex_doggy_d_vaporbreathing_01:
    subpixel True
    truecenter
    zoom 2.0
    xpos 0.25 ypos -1.0
    alpha 0.25

transform gensex_doggy_d_vaporbreathing_02:
    subpixel True
    truecenter
    zoom 2.0
    xpos 0.25 ypos -1.0
    alpha 0.5

transform gensex_doggy_d_vaporbreathing_03:
    subpixel True
    truecenter
    zoom 2.0
    xpos 0.25 ypos -1.0
    alpha 0.75

transform gensex_doggy_d_vaporbreathing_04:
    subpixel True
    truecenter
    zoom 2.0
    xpos 0.25 ypos -1.0
    alpha 1.0

# Neus

transform gensex_doggy_n_vaporbreathing_01:
    subpixel True
    truecenter
    zoom 2.0
    xpos 0.25 ypos -0.5
    alpha 0.25

transform gensex_doggy_n_vaporbreathing_02:
    subpixel True
    truecenter
    zoom 2.0
    xpos 0.25 ypos -0.5
    alpha 0.5

transform gensex_doggy_n_vaporbreathing_03:
    subpixel True
    truecenter
    zoom 2.0
    xpos 0.25 ypos -0.5
    alpha 0.75

transform gensex_doggy_n_vaporbreathing_04:
    subpixel True
    truecenter
    zoom 2.0
    xpos 0.25 ypos -0.5
    alpha 1.0

define ped_doggy_v_a = ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05", "v02_01", "v02_02", "v02_03", "v02_04", "v02_05", "a01_01", "a01_02", "a01_03", "a01_04", "a01_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05"]
define ped_doggy_v_a_vt_at = ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05", "v02_01", "v02_02", "v02_03", "v02_04", "v02_05", "a01_01", "a01_02", "a01_03", "a01_04", "a01_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05", "vt01_01", "vt01_02", "vt01_03", "vt01_04", "vt01_05", "at01_01", "at01_02", "at01_03", "at01_04", "at01_05"]
define ped_doggy_v_a_at = ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05", "v02_01", "v02_02", "v02_03", "v02_04", "v02_05", "a01_01", "a01_02", "a01_03", "a01_04", "a01_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05", "at01_01", "at01_02", "at01_03", "at01_04", "at01_05"]

image gensex_doggy_d_comp 01:

    # contains:
    #     "gensex_doggy_d_REFERENCE02"
    #     truecenter

## BG
        
    contains:
        "gensex_doggy_d_bg"
        truecenter
        zoom 2.0

## DIDAC SQUIRT on BED

    contains:
        ConditionSwitch(
            p_didac.orgasm == 1, At("gensex_doggy_d_squirt_bed 01", gensex_doggy_d_squirt_bed_trans),
            p_didac.orgasm == 2, At("gensex_doggy_d_squirt_bed 02", gensex_doggy_d_squirt_bed_trans),
            p_didac.orgasm == 3, At("gensex_doggy_d_squirt_bed 03", gensex_doggy_d_squirt_bed_trans),
            p_didac.orgasm >= 4, At("gensex_doggy_d_squirt_bed 04", gensex_doggy_d_squirt_bed_trans),
            "True", Null()
            )

## DIDAC SQUIRT
    
    contains:
        ConditionSwitch(
            ped_sex_general_action_b_Cond == "sdcum01", At("gensex_doggy_d_squirt 01", gensex_doggy_d_squirt_trans),
            ped_sex_general_action_b_Cond == "sdcum02", At("gensex_doggy_d_squirt 02", gensex_doggy_d_squirt_trans),
            ped_sex_general_action_b_Cond == "sdcum03", At("gensex_doggy_d_squirt 03", gensex_doggy_d_squirt_trans),
            ped_sex_general_action_b_Cond == "sdcum04", At("gensex_doggy_d_squirt 04", gensex_doggy_d_squirt_trans),
            "True", Null()
            )

## HANDS

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ped_doggy_v_a, At("gensex_doggy_d_hands", gensex_doggy_d_hands_trans_v01_xx),

            "True", At("gensex_doggy_d_hands", gensex_doggy_d_hands_trans_00_00)
            )


## DIDAC VAPOR

    contains:
        ConditionSwitch(
            p_didac.orgasm >= 4 and p_didac.closeOrgasmTotal > 135 or
            p_didac.orgasm == 3 and p_didac.closeOrgasmTotal > 115 or
            p_didac.orgasm == 2 and p_didac.closeOrgasmTotal > 90 or
            p_didac.orgasm == 1 and p_didac.closeOrgasmTotal > 65 or
            p_didac.orgasm == 0 and p_didac.closeOrgasmTotal > 40
            , At("vaporbreathing_new", gensex_doggy_d_vaporbreathing_04),
            p_didac.orgasm >= 4 and p_didac.closeOrgasmTotal > 100 or
            p_didac.orgasm == 3 and p_didac.closeOrgasmTotal > 85 or
            p_didac.orgasm == 2 and p_didac.closeOrgasmTotal > 75 or
            p_didac.orgasm == 1 and p_didac.closeOrgasmTotal > 50 or
            p_didac.orgasm == 0 and p_didac.closeOrgasmTotal > 30
            , At("vaporbreathing_new", gensex_doggy_d_vaporbreathing_03),
            p_didac.orgasm >= 4 and p_didac.closeOrgasmTotal > 75 or
            p_didac.orgasm == 3 and p_didac.closeOrgasmTotal > 60 or
            p_didac.orgasm == 2 and p_didac.closeOrgasmTotal > 45 or
            p_didac.orgasm == 1 and p_didac.closeOrgasmTotal > 35 or
            p_didac.orgasm == 0 and p_didac.closeOrgasmTotal > 20
            , At("vaporbreathing_new", gensex_doggy_d_vaporbreathing_02),
            p_didac.orgasm >= 4 and p_didac.closeOrgasmTotal > 50 or
            p_didac.orgasm == 3 and p_didac.closeOrgasmTotal > 40 or
            p_didac.orgasm == 2 and p_didac.closeOrgasmTotal > 35 or
            p_didac.orgasm == 1 and p_didac.closeOrgasmTotal > 25 or
            p_didac.orgasm == 0 and p_didac.closeOrgasmTotal > 10
            , At("vaporbreathing_new", gensex_doggy_d_vaporbreathing_01),
            "True", Null()
            )


## HEAD

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ped_doggy_v_a, At("gensex_doggy_d_head", gensex_doggy_d_head_trans_v01_xx),

            "True", At("gensex_doggy_d_head", gensex_doggy_d_head_trans_00_00)
            )


## LEGS

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["vcum01", "vcum02", "acum01", "acum02", "vdcum01", "vdcum02", "adcum01", "adcum02"], At("gensex_doggy_d_legs", gensex_doggy_d_legs_trans_vdcum01),

            ped_sex_general_action_b_Cond in ["sdcum01", "sdcum02", "sdcum03", "sdcum04"], At("gensex_doggy_d_legs", gensex_doggy_d_legs_trans_vdcum01),

            ped_sex_general_action_Cond in ped_doggy_v_a, At("gensex_doggy_d_legs", gensex_doggy_d_legs_trans_v01_xx),

            "True", At("gensex_doggy_d_legs", gensex_doggy_d_legs_trans_00_00)
            )

## VAGINAL DOWN

    contains:
        ConditionSwitch(

        ped_sex_general_action_b_Cond in ["sdcum01", "sdcum02", "sdcum03", "sdcum04"], At("gensex_doggy_d_dbelow_vaginal_closed", gensex_doggy_d_dbelow_vaginal_closed_trans_dcum),

        ped_sex_general_action_Cond in ped_doggy_v_a_vt_at, At("gensex_doggy_d_dbelow_vaginal_closed", gensex_doggy_d_dbelow_vaginal_closed_trans_v01_xx),

            "True", At("gensex_doggy_d_dbelow_vaginal_closed", gensex_doggy_d_dbelow_vaginal_closed_trans_00_00)
            )

## ANAL DOWN

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["a01_01", "a01_02", "a01_03", "a01_04", "a01_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05" "at01_01", "at01_02", "at01_03", "at01_04", "at01_05", "v01_01", "vt01_01", "v01_02", "vt01_02", "v01_03", "vt01_03", "v01_04", "v01_05", "vt01_04", "vt01_05"], Null(),

            ped_sex_general_action_b_Cond in ["sdcum01", "sdcum02", "sdcum03", "sdcum04"], Null(),


            "True", At("gensex_doggy_d_dabove_anal_closed", gensex_doggy_d_dabove_anal_closed_trans_00_00)
            )

## DICK

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["vcum01"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_vcum01),
            ped_sex_general_action_Cond in ["vcum02"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_vcum02),

            ped_sex_general_action_Cond in ["vdcum01"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_vdcum01),
            ped_sex_general_action_Cond in ["vdcum02"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_vdcum02),


            ped_sex_general_action_Cond in ["acum01"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_acum01),
            ped_sex_general_action_Cond in ["acum02"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_acum02),

            ped_sex_general_action_Cond in ["adcum01"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_adcum01),
            ped_sex_general_action_Cond in ["adcum02"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_adcum02),




            ped_sex_general_action_Cond == "v00_00", At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_v00_00),

            ped_sex_general_action_Cond in ["v00_01", "v00_02", "v00_03", "v00_04", "v00_05"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_v00_xx),

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_v01_xx),

            ped_sex_general_action_Cond in ["v02_01", "v02_02", "v02_03", "v02_04", "v02_05"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_v02_xx),

            ped_sex_general_action_Cond in ["a00_01", "a00_02", "a00_03", "a00_04", "a00_05"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_a00_xx),

            ped_sex_general_action_Cond in ["a01_01", "a01_02", "a01_03", "a01_04", "a01_05"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_a01_xx),

            ped_sex_general_action_Cond in ["a02_01", "a02_02", "a02_03", "a02_04", "a02_05"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_a02_xx),

            "True", Null()
            )

## TONGUE PENETRATING

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["at01_01", "at01_02", "at01_03", "at01_04", "at01_05"], At("gensex_missionary_mc_tongue_01", pedrera_sex_doggy_mc_tongue_trans_at01_xx),

            "True", Null()
            )

## VAGINAL PENETRATED

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["vcum01", "vdcum01"], At("gensex_doggy_d_dabove_vaginal_penetrated", gensex_doggy_d_dabove_vaginal_penetrated_trans_vcum01),
            ped_sex_general_action_Cond in ["vcum02", "vdcum02"], At("gensex_doggy_d_dabove_vaginal_penetrated", gensex_doggy_d_dabove_vaginal_penetrated_trans_vcum01),

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05", "v02_01", "v02_02", "v02_03", "v02_04", "v02_05"], At("gensex_doggy_d_dabove_vaginal_penetrated", gensex_doggy_d_dabove_vaginal_penetrated_trans_v01_xx),


            "True", Null()
            )

## ANAL CLOSED OVER

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05", "vt01_01", "vt01_02", "vt01_03", "vt01_04", "vt01_05"], At("gensex_doggy_d_dabove_anal_closed", gensex_doggy_d_dbelow_vaginal_closed_trans_v01_xx),

            ped_sex_general_action_b_Cond in ["sdcum01", "sdcum02", "sdcum03", "sdcum04"], At("gensex_doggy_d_dabove_anal_closed", gensex_doggy_d_dbelow_vaginal_closed_trans_dcum),

            ped_sex_general_action_Cond in ["v00_01", "v00", "a00", "v00_02", "a00_02", "v00_03", "a00_03", "v00_04", "a00_04","v00_05", "a00_05","a01_01", "a01_02", "a01_03", "a01_04", "a01_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05", "at01_01", "at01_02", "at01_03", "at01_04", "at01_05"], Null(),

            "True", At("gensex_doggy_d_dabove_anal_closed", gensex_doggy_d_dabove_anal_closed_trans_00_00)
            )

## TONGUE LICKING ASS

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond == "at00_00", At("gensex_missionary_mc_tongue_01", pedrera_sex_doggy_mc_tongue_trans_at00_00),

            ped_sex_general_action_Cond in ["at00_01", "at00_02", "at00_03", "at00_04", "at00_05"], At("gensex_missionary_mc_tongue_01", pedrera_sex_doggy_mc_tongue_trans_at00_xx),

            "True", Null()
            )

## ANAL PENETRATED

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["acum01", "adcum01"], At("gensex_doggy_d_dabove_anal_penetrated", gensex_doggy_d_dabove_anal_penetrated_trans_acum01),
            ped_sex_general_action_Cond in ["acum02", "adcum02"], At("gensex_doggy_d_dabove_anal_penetrated", gensex_doggy_d_dabove_anal_penetrated_trans_acum01),

            ped_sex_general_action_Cond in ["a01_01", "a01_02", "a01_03", "a01_04", "a01_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05"], At("gensex_doggy_d_dabove_anal_penetrated", gensex_doggy_d_dabove_anal_penetrated_trans_a01_xx),

            ped_sex_general_action_Cond in ["at01_01", "at01_02", "at01_03", "at01_04", "at01_05",], At("gensex_doggy_d_dabove_anal_penetrated", gensex_doggy_d_dabove_anal_penetrated_trans_at01_xx),

            "True", Null()
            )

## BODY

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ped_doggy_v_a, At("gensex_doggy_d_body", gensex_doggy_d_body_trans_v01_xx),

            "True", At("gensex_doggy_d_body", gensex_doggy_d_body_trans_00_00)
            )

## BUTT LEFT

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["vcum01", "vcum02", "acum01", "acum02", "vdcum01", "vdcum02", "adcum01", "adcum02"], At("gensex_doggy_d_but_L", gensex_doggy_d_but_L_trans_vdcum01),

            ped_sex_general_action_b_Cond in ["sdcum01", "sdcum02", "sdcum03", "sdcum04"], At("gensex_doggy_d_but_L", gensex_doggy_d_but_L_trans_vdcum01),

        # PainBut 0

            ped_sex_general_action_Cond in ped_doggy_v_a_at, At("gensex_doggy_d_but_L", gensex_doggy_d_but_L_trans_v01_xx),


            "True", At("gensex_doggy_d_but_L", gensex_doggy_d_but_L_trans_00_00)
            )
 

## BUTT RIGHT
    
    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["vcum01", "vcum02", "acum01", "acum02", "vdcum01", "vdcum02", "adcum01", "adcum02"], At("gensex_doggy_d_but_R", gensex_doggy_d_but_R_trans_vdcum01),

            ped_sex_general_action_b_Cond in ["sdcum01", "sdcum02", "sdcum03", "sdcum04"], At("gensex_doggy_d_but_R", gensex_doggy_d_but_R_trans_vdcum01),

        # painBut 0

            ped_sex_general_action_Cond in ped_doggy_v_a_at, At("gensex_doggy_d_but_R", gensex_doggy_d_but_R_trans_v01_xx),

            "True", At("gensex_doggy_d_but_R", gensex_doggy_d_but_R_trans_00_00)
            )


############################################################################################################
############################################################################################################
##########################################################################################
##########################################################################################
############################################################################################################
############################################################################################################

image gensex_doggy_n_comp 01:

## BG
        
    contains:
        "gensex_doggy_n_bg"
        truecenter
        zoom 2.0

## Hair over bed

    contains:
        "gensex_doggy_n_hairground"
        truecenter

## NEUS SQUIRT
    
    contains:
        ConditionSwitch(
            ped_sex_general_action_b_Cond == "sdcum01", At("gensex_doggy_d_squirt 01", gensex_doggy_d_squirt_trans),
            ped_sex_general_action_b_Cond == "sdcum02", At("gensex_doggy_d_squirt 02", gensex_doggy_d_squirt_trans),
            ped_sex_general_action_b_Cond == "sdcum03", At("gensex_doggy_d_squirt 03", gensex_doggy_d_squirt_trans),
            ped_sex_general_action_b_Cond == "sdcum04", At("gensex_doggy_d_squirt 04", gensex_doggy_d_squirt_trans),
            "True", Null()
            )

## HANDS

    contains:
        "gensex_doggy_n_hands"
        truecenter

## NEUS VAPOR

    contains:
        ConditionSwitch(
            p_neus.orgasm >= 4 and p_neus.closeOrgasmTotal > 135 or
            p_neus.orgasm == 3 and p_neus.closeOrgasmTotal > 115 or
            p_neus.orgasm == 2 and p_neus.closeOrgasmTotal > 90 or
            p_neus.orgasm == 1 and p_neus.closeOrgasmTotal > 65 or
            p_neus.orgasm == 0 and p_neus.closeOrgasmTotal > 40
            , At("vaporbreathing_new", gensex_doggy_n_vaporbreathing_04),
            p_neus.orgasm >= 4 and p_neus.closeOrgasmTotal > 100 or
            p_neus.orgasm == 3 and p_neus.closeOrgasmTotal > 85 or
            p_neus.orgasm == 2 and p_neus.closeOrgasmTotal > 75 or
            p_neus.orgasm == 1 and p_neus.closeOrgasmTotal > 50 or
            p_neus.orgasm == 0 and p_neus.closeOrgasmTotal > 30
            , At("vaporbreathing_new", gensex_doggy_n_vaporbreathing_03),
            p_neus.orgasm >= 4 and p_neus.closeOrgasmTotal > 75 or
            p_neus.orgasm == 3 and p_neus.closeOrgasmTotal > 60 or
            p_neus.orgasm == 2 and p_neus.closeOrgasmTotal > 45 or
            p_neus.orgasm == 1 and p_neus.closeOrgasmTotal > 35 or
            p_neus.orgasm == 0 and p_neus.closeOrgasmTotal > 20
            , At("vaporbreathing_new", gensex_doggy_n_vaporbreathing_02),
            p_neus.orgasm >= 4 and p_neus.closeOrgasmTotal > 50 or
            p_neus.orgasm == 3 and p_neus.closeOrgasmTotal > 40 or
            p_neus.orgasm == 2 and p_neus.closeOrgasmTotal > 35 or
            p_neus.orgasm == 1 and p_neus.closeOrgasmTotal > 25 or
            p_neus.orgasm == 0 and p_neus.closeOrgasmTotal > 10
            , At("vaporbreathing_new", gensex_doggy_n_vaporbreathing_01),
            "True", Null()
            )


## HEAD

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond in ped_doggy_v_a, At("gensex_doggy_n_head", gensex_doggy_n_head_trans_v01_xx),

            "True", At("gensex_doggy_n_head", gensex_doggy_d_head_trans_00_00)
            )


## LEGS

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["vcum01", "vcum02", "acum01", "acum02", "vdcum01", "vdcum02", "adcum01", "adcum02"], At("gensex_doggy_d_legs", gensex_doggy_d_legs_trans_vdcum01),

            ped_sex_general_action_b_Cond in ["sdcum01", "sdcum02", "sdcum03", "sdcum04"], At("gensex_doggy_n_legs", gensex_doggy_d_legs_trans_vdcum01),

            ped_sex_general_action_Cond in ped_doggy_v_a, At("gensex_doggy_n_legs", gensex_doggy_d_legs_trans_v01_xx),

            "True", At("gensex_doggy_n_legs", gensex_doggy_d_legs_trans_00_00)
            )

## VAGINAL DOWN

    contains:
        ConditionSwitch(

        ped_sex_general_action_b_Cond in ["sdcum01", "sdcum02", "sdcum03", "sdcum04"], At("gensex_doggy_d_dbelow_vaginal_closed", gensex_doggy_d_dbelow_vaginal_closed_trans_dcum),

        ped_sex_general_action_Cond in ped_doggy_v_a_vt_at, At("gensex_doggy_n_dbelow_vaginal_closed", gensex_doggy_d_dbelow_vaginal_closed_trans_v01_xx),

            "True", At("gensex_doggy_n_dbelow_vaginal_closed", gensex_doggy_d_dbelow_vaginal_closed_trans_00_00)
            )

## ANAL DOWN

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["a01_01", "a01_02", "a01_03", "a01_04", "a01_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05" "at01_01", "at01_02", "at01_03", "at01_04", "at01_05", "v01_01", "vt01_01", "v01_02", "vt01_02", "v01_03", "vt01_03", "v01_04", "v01_05", "vt01_04", "vt01_05"], Null(),

            ped_sex_general_action_b_Cond in ["sdcum01", "sdcum02", "sdcum03", "sdcum04"], Null(),


            "True", At("gensex_doggy_n_dabove_anal_closed", gensex_doggy_d_dabove_anal_closed_trans_00_00)
            )

## DICK

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["vcum01"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_vcum01),
            ped_sex_general_action_Cond in ["vcum02"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_vcum02),

            ped_sex_general_action_Cond in ["vdcum01"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_vdcum01),
            ped_sex_general_action_Cond in ["vdcum02"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_vdcum02),


            ped_sex_general_action_Cond in ["acum01"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_acum01),
            ped_sex_general_action_Cond in ["acum02"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_acum02),

            ped_sex_general_action_Cond in ["adcum01"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_adcum01),
            ped_sex_general_action_Cond in ["adcum02"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_adcum02),




            ped_sex_general_action_Cond == "v00_00", At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_v00_00),

            ped_sex_general_action_Cond in ["v00_01", "v00_02", "v00_03", "v00_04", "v00_05"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_v00_xx),

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_v01_xx),

            ped_sex_general_action_Cond in ["v02_01", "v02_02", "v02_03", "v02_04", "v02_05"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_v02_xx),

            ped_sex_general_action_Cond in ["a00_01", "a00_02", "a00_03", "a00_04", "a00_05"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_a00_xx),

            ped_sex_general_action_Cond in ["a01_01", "a01_02", "a01_03", "a01_04", "a01_05"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_a01_xx),

            ped_sex_general_action_Cond in ["a02_01", "a02_02", "a02_03", "a02_04", "a02_05"], At("gensex_oral_mc_dick_b_01_wet_00", pedrera_sex_doggy_mc_dick_trans_a02_xx),

            "True", Null()
            )

## TONGUE PENETRATING

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["at01_01", "at01_02", "at01_03", "at01_04", "at01_05"], At("gensex_missionary_mc_tongue_01", pedrera_sex_doggy_mc_tongue_trans_at01_xx),

            "True", Null()
            )

## VAGINAL PENETRATED

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["vcum01", "vdcum01"], At("gensex_doggy_n_dabove_vaginal_penetrated", gensex_doggy_d_dabove_vaginal_penetrated_trans_vcum01),
            ped_sex_general_action_Cond in ["vcum02", "vdcum02"], At("gensex_doggy_n_dabove_vaginal_penetrated", gensex_doggy_d_dabove_vaginal_penetrated_trans_vcum01),

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05", "v02_01", "v02_02", "v02_03", "v02_04", "v02_05"], At("gensex_doggy_n_dabove_vaginal_penetrated", gensex_doggy_d_dabove_vaginal_penetrated_trans_v01_xx),


            "True", Null()
            )

## ANAL CLOSED OVER

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["v01_01", "v01_02", "v01_03", "v01_04", "v01_05", "vt01_01", "vt01_02", "vt01_03", "vt01_04", "vt01_05"], At("gensex_doggy_n_dabove_anal_closed", gensex_doggy_d_dbelow_vaginal_closed_trans_v01_xx),

            ped_sex_general_action_b_Cond in ["sdcum01", "sdcum02", "sdcum03", "sdcum04"], At("gensex_doggy_n_dabove_anal_closed", gensex_doggy_d_dbelow_vaginal_closed_trans_dcum),

            ped_sex_general_action_Cond in ["v00_01", "v00", "a00", "v00_02", "a00_02", "v00_03", "a00_03", "v00_04", "a00_04","v00_05", "a00_05","a01_01", "a01_02", "a01_03", "a01_04", "a01_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05", "at01_01", "at01_02", "at01_03", "at01_04", "at01_05"], Null(),

            "True", At("gensex_doggy_n_dabove_anal_closed", gensex_doggy_d_dabove_anal_closed_trans_00_00)
            )

## TONGUE LICKING ASS

    contains:
        ConditionSwitch(
            ped_sex_general_action_Cond == "at00_00", At("gensex_missionary_mc_tongue_01", pedrera_sex_doggy_mc_tongue_trans_at00_00),

            ped_sex_general_action_Cond in ["at00_01", "at00_02", "at00_03", "at00_04", "at00_05"], At("gensex_missionary_mc_tongue_01", pedrera_sex_doggy_mc_tongue_trans_at00_xx),

            "True", Null()
            )

## ANAL PENETRATED

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["acum01", "adcum01"], At("gensex_doggy_n_dabove_anal_penetrated", gensex_doggy_d_dabove_anal_penetrated_trans_acum01),
            ped_sex_general_action_Cond in ["acum02", "adcum02"], At("gensex_doggy_n_dabove_anal_penetrated", gensex_doggy_d_dabove_anal_penetrated_trans_acum01),

            ped_sex_general_action_Cond in ["a01_01", "a01_02", "a01_03", "a01_04", "a01_05", "a02_01", "a02_02", "a02_03", "a02_04", "a02_05"], At("gensex_doggy_n_dabove_anal_penetrated", gensex_doggy_d_dabove_anal_penetrated_trans_a01_xx),

            ped_sex_general_action_Cond in ["at01_01", "at01_02", "at01_03", "at01_04", "at01_05",], At("gensex_doggy_n_dabove_anal_penetrated", gensex_doggy_d_dabove_anal_penetrated_trans_at01_xx),

            "True", Null()
            )

## BODY

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ped_doggy_v_a, At("gensex_doggy_n_body", gensex_doggy_n_body_trans_v01_xx),

            "True", At("gensex_doggy_n_body", gensex_doggy_d_body_trans_00_00)
            )

## BUTT LEFT

    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["vcum01", "vcum02", "acum01", "acum02", "vdcum01", "vdcum02", "adcum01", "adcum02"], At("gensex_doggy_n_but_L", gensex_doggy_n_but_L_trans_vdcum01),

            ped_sex_general_action_b_Cond in ["sdcum01", "sdcum02", "sdcum03", "sdcum04"], At("gensex_doggy_n_but_L", gensex_doggy_n_but_L_trans_vdcum01),

        # PainBut 0

            ped_sex_general_action_Cond in ped_doggy_v_a_at, At("gensex_doggy_n_but_L", gensex_doggy_n_but_L_trans_v01_xx),


            "True", At("gensex_doggy_n_but_L", gensex_doggy_n_but_L_trans_00_00)
            )
 

## BUTT RIGHT
    
    contains:
        ConditionSwitch(

            ped_sex_general_action_Cond in ["vcum01", "vcum02", "acum01", "acum02", "vdcum01", "vdcum02", "adcum01", "adcum02"], At("gensex_doggy_n_but_R", gensex_doggy_n_but_R_trans_vdcum01),

            ped_sex_general_action_b_Cond in ["sdcum01", "sdcum02", "sdcum03", "sdcum04"], At("gensex_doggy_n_but_R", gensex_doggy_n_but_R_trans_vdcum01),

        # painBut 0

            ped_sex_general_action_Cond in ped_doggy_v_a_at, At("gensex_doggy_n_but_R", gensex_doggy_n_but_R_trans_v01_xx),

            "True", At("gensex_doggy_n_but_R", gensex_doggy_n_but_R_trans_00_00)
            )


############################################################################################################
############################################################################################################
##########################################################################################
##########################################################################################
############################################################################################################
############################################################################################################
## 69

#image pedrera_sex_69_didac_REFERENCE = "images/day05/pedrera/sex/69/pedrera_sex_69_didac_REFERENCE.webp"


####################################################
####################################################
####################################################
####################################################
####################################################
####################################################
####################################################
####################################################
####################################################
####################################################
####################################################
####################################################


image ped_hugneus_REFERENCE = SaturateTint("images/day05/pedrera/ped_hugneus_REFERENCE.webp")

image ped_hugneus_mc_arms = SaturateTint("images/day05/pedrera/ped_hugneus_mc_arms.webp")
image ped_hugneus_mc_body = SaturateTint("images/day05/pedrera/ped_hugneus_mc_body.webp")
image ped_hugneus_neus = SaturateTint("images/day05/pedrera/ped_hugneus_neus.webp")

image ped_hugneus_comp 01:

    contains:
        "bg dark_a_blurry_02"
        truecenter
        zoom 4.0

    # contains:
    #     "ped_hugneus_REFERENCE"
    #     subpixel True
    #     truecenter
    #     alpha 0.0

    contains:
        "gensex_stan_mc_fit_03_body naked"
        truecenter
        zoom 1.5 xpos 0.4 ypos 1.7
        #alpha 0.5

    contains:
        "gensex_stan_mc_15_arm"
        transform_anchor True
        #alpha 0.5
        xalign 0.31 yalign 0.123 # Hombro de los cojones. #########################
        zoom 1.5
        xpos 1.45 ypos -0.41

    # contains:
    #     "gensex_stan_mc_fit_14_mc_shirtover_up"
    #     truecenter
    #     zoom 1.5
    #     xpos 1.63 ypos 2.0 rotate 10

    contains:
        "ped_hugneus_neus"
        truecenter
        zoom 0.5
        
image ped_hugneus_comp 02:

    contains:
        "bg dark_a_blurry_02"
        truecenter
        zoom 4.0

    contains:
        "ped_hugneus_mc_body"
        truecenter
        zoom 0.5


    contains:
        "ped_hugneus_neus"
        truecenter
        zoom 0.5

    contains:
        "ped_hugneus_mc_arms"
        truecenter
        zoom 0.5


#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################

#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################

transform ped_eyes_iLight_trans:
    subpixel True
    truecenter
    alpha ped_neus_whispers_sfx04
    additive 1.0

transform ped_eyes_l_iris_trans:
    subpixel True
    truecenter
    alpha ped_neus_whispers_sfx03

image ped_sex_oral_expression_img:

    ## EXPRESSIONS ORAL

    contains:
        ConditionSwitch(
            p_active == "p_neus", At("gensex_oral_n_frontHead_ears down", truecenter),
            "True", Null()
            )

##JAW # Neus JAWS
    contains:
        ConditionSwitch(
            p_active == "p_neus" and ped_sex_blow_Cond == True, Null(),
            p_active == "p_neus" and ped_sex_general_expressionJaw_Cond in ["blow_below_05_happy"], At("gensex_oral_n_frontHead_exp_mouth_b blow_below_05_happy", truecenter),
            p_active == "p_neus" and ped_sex_general_expressionJaw_Cond in ["blow_below_bite"], At("gensex_oral_n_frontHead_exp_mouth_b blow_below_bite", truecenter),
            p_active == "p_neus" and ped_sex_general_expressionJaw_Cond in ["blow_below_05"], At("gensex_oral_n_frontHead_exp_mouth_b blow_below_05", truecenter),
            p_active == "p_neus" and ped_sex_general_expressionJaw_Cond in ["blow_below_04"], At("gensex_oral_n_frontHead_exp_mouth_b blow_below_04", truecenter),
            p_active == "p_neus" and ped_sex_general_expressionJaw_Cond in ["blow_below_03"], At("gensex_oral_n_frontHead_exp_mouth_b blow_below_03", truecenter),
            p_active == "p_neus" and ped_sex_general_expressionJaw_Cond in ["blow_below_02"], At("gensex_oral_n_frontHead_exp_mouth_b blow_below_02", truecenter),
            p_active == "p_neus" and ped_sex_general_expressionJaw_Cond in ["blow_below_01"], At("gensex_oral_n_frontHead_exp_mouth_b blow_below_01", truecenter),
            p_active == "p_neus" and ped_sex_general_expressionJaw_Cond in ["blow_below_03b"], At("gensex_oral_n_frontHead_exp_mouth_b blow_below_03b", truecenter),
            p_active == "p_neus", At("gensex_oral_n_frontHead_face", truecenter),
            "True", Null() # If it's not Neus it must be empty.
            )

    contains: # nblush = int // nblushNumber = string
        ConditionSwitch(
            p_active == "p_neus" and nblush < 1, At("gensex_oral_n_frontHead_exp_blush 01", truecenter),
            p_active == "p_neus" and nblush > 8, At("gensex_oral_n_frontHead_exp_blush 08", truecenter),
            p_active == "p_neus", At("gensex_oral_n_frontHead_exp_blush " + nblushNumber, truecenter),
            "True", At("gensex_oral_d_frontHead_exp_blush 03", truecenter))

## EYES

    contains:
        ConditionSwitch(
                ped_sex_general_expression_Cond == "closed", At("gensex_oral[p_activeno]_frontHead_exp_eyes 08", truecenter),
                ped_sex_general_expression_Cond == "indifferent", At("gensex_oral[p_activeno]_frontHead_exp_eyes 08", truecenter),
                ped_sex_general_expression_Cond in ["angry", "angryLick"], At("gensex_oral[p_activeno]_frontHead_exp_eyes 08", truecenter),
                ped_sex_general_expression_Cond == "disgust", At("gensex_oral[p_activeno]_frontHead_exp_eyes 06", truecenter),
                ped_sex_general_expression_Cond == "veryAngry", At("gensex_oral[p_activeno]_frontHead_exp_eyes 08", truecenter),
                ped_sex_general_expression_Cond == "lust", At("gensex_oral[p_activeno]_frontHead_exp_eyes 04", truecenter),
                ped_sex_general_expression_Cond == "lustSmile", At("gensex_oral[p_activeno]_frontHead_exp_eyes 05", truecenter),
                ped_sex_general_expression_Cond == "lustToYou", At("gensex_oral[p_activeno]_frontHead_exp_eyes 05", truecenter),
                ped_sex_general_expression_Cond == "lustAngry", At("gensex_oral[p_activeno]_frontHead_exp_eyes 05", truecenter),
                ped_sex_general_expression_Cond in ["surpriseLeft", "surpriseRight"], At("gensex_oral[p_activeno]_frontHead_exp_eyes 01", truecenter),
                ped_sex_general_expression_Cond == "surpriseDown", At("gensex_oral[p_activeno]_frontHead_exp_eyes 01", truecenter),
                ped_sex_general_expression_Cond == "angryFront", At("gensex_oral[p_activeno]_frontHead_exp_eyes 05", truecenter),
                ped_sex_general_expression_Cond == "angryRight", At("gensex_oral[p_activeno]_frontHead_exp_eyes 05", truecenter),
                ped_sex_general_expression_Cond == "tongueWrap", At("gensex_oral[p_activeno]_frontHead_exp_eyes 05", truecenter),
                "True", Null())

## IRIS
    contains:
        ConditionSwitch(
                ped_sex_general_expression_Cond == "closed", At("gensex_oral[p_activeno]_frontHead_exp_iris empty", truecenter),
                ped_sex_general_expression_Cond == "indifferent", At("gensex_oral[p_activeno]_frontHead_exp_iris empty", truecenter),
                ped_sex_general_expression_Cond in ["angry", "disgust", "angryLick"], At("gensex_oral[p_activeno]_frontHead_exp_iris empty", truecenter),
                ped_sex_general_expression_Cond == "veryAngry", At("gensex_oral[p_activeno]_frontHead_exp_iris empty", truecenter),
                ped_sex_general_expression_Cond == "lust", At("gensex_oral[p_activeno]_frontHead_exp_iris front04", truecenter),
                ped_sex_general_expression_Cond == "lustSmile", At("gensex_oral[p_activeno]_frontHead_exp_iris front05", truecenter),
                ped_sex_general_expression_Cond == "lustToYou", At("gensex_oral[p_activeno]_frontHead_exp_iris front05", truecenter),
                ped_sex_general_expression_Cond == "lustAngry", At("gensex_oral[p_activeno]_frontHead_exp_iris front05", truecenter),
                ped_sex_general_expression_Cond == "surpriseLeft", At("gensex_oral[p_activeno]_frontHead_exp_iris left01", truecenter),
                ped_sex_general_expression_Cond == "surpriseRight", At("gensex_oral[p_activeno]_frontHead_exp_iris right01", truecenter),
                ped_sex_general_expression_Cond == "surpriseDown", At("gensex_oral[p_activeno]_frontHead_exp_iris down01", truecenter),
                ped_sex_general_expression_Cond == "angryFront", At("gensex_oral[p_activeno]_frontHead_exp_iris front05", truecenter),
                ped_sex_general_expression_Cond == "angryRight", At("gensex_oral[p_activeno]_frontHead_exp_iris right05", truecenter),
                ped_sex_general_expression_Cond == "tongueWrap", At("gensex_oral[p_activeno]_frontHead_exp_iris front05", truecenter),
                "True", Null())

## IRIS VIOLET
    contains:
        ConditionSwitch(
                p_active == "p_neus" and ped_sex_general_expression_Cond == "closed", At("gensex_oral[p_activeno]_frontHead_exp_l_iris empty", ped_eyes_l_iris_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "indifferent", At("gensex_oral[p_activeno]_frontHead_exp_l_iris empty", ped_eyes_l_iris_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond in ["angry", "disgust", "angryLick"], At("gensex_oral[p_activeno]_frontHead_exp_l_iris empty", ped_eyes_l_iris_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "veryAngry", At("gensex_oral[p_activeno]_frontHead_exp_l_iris empty", ped_eyes_l_iris_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "lust", At("gensex_oral[p_activeno]_frontHead_exp_l_iris front04", ped_eyes_l_iris_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "lustSmile", At("gensex_oral[p_activeno]_frontHead_exp_l_iris front05", ped_eyes_l_iris_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "lustToYou", At("gensex_oral[p_activeno]_frontHead_exp_l_iris front05", ped_eyes_l_iris_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "lustAngry", At("gensex_oral[p_activeno]_frontHead_exp_l_iris front05", ped_eyes_l_iris_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "surpriseLeft", At("gensex_oral[p_activeno]_frontHead_exp_l_iris left01", ped_eyes_l_iris_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "surpriseRight", At("gensex_oral[p_activeno]_frontHead_exp_l_iris right01", ped_eyes_l_iris_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "surpriseDown", At("gensex_oral[p_activeno]_frontHead_exp_l_iris down01", ped_eyes_l_iris_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "angryFront", At("gensex_oral[p_activeno]_frontHead_exp_l_iris front05", ped_eyes_l_iris_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "angryRight", At("gensex_oral[p_activeno]_frontHead_exp_l_iris right05", ped_eyes_l_iris_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "tongueWrap", At("gensex_oral[p_activeno]_frontHead_exp_l_iris front05", ped_eyes_l_iris_trans),
                "True", Null())

## LIGHT IRIS
    contains:
        ConditionSwitch(
                p_active == "p_neus" and ped_sex_general_expression_Cond == "closed", At("gensex_oral[p_activeno]_frontHead_exp_iLight empty", ped_eyes_iLight_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "indifferent", At("gensex_oral[p_activeno]_frontHead_exp_iLight empty", ped_eyes_iLight_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond in ["angry", "disgust", "angryLick"], At("gensex_oral[p_activeno]_frontHead_exp_iLight empty", ped_eyes_iLight_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "veryAngry", At("gensex_oral[p_activeno]_frontHead_exp_iLight empty", ped_eyes_iLight_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "lust", At("gensex_oral[p_activeno]_frontHead_exp_iLight front04", ped_eyes_iLight_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "lustSmile", At("gensex_oral[p_activeno]_frontHead_exp_iLight front05", ped_eyes_iLight_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "lustToYou", At("gensex_oral[p_activeno]_frontHead_exp_iLight front05", ped_eyes_iLight_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "lustAngry", At("gensex_oral[p_activeno]_frontHead_exp_iLight front05", ped_eyes_iLight_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "surpriseLeft", At("gensex_oral[p_activeno]_frontHead_exp_iLight left01", ped_eyes_iLight_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "surpriseRight", At("gensex_oral[p_activeno]_frontHead_exp_iLight right01", ped_eyes_iLight_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "surpriseDown", At("gensex_oral[p_activeno]_frontHead_exp_iLight down01", ped_eyes_iLight_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "angryFront", At("gensex_oral[p_activeno]_frontHead_exp_iLight front05", ped_eyes_iLight_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "angryRight", At("gensex_oral[p_activeno]_frontHead_exp_iLight right05", ped_eyes_iLight_trans),
                p_active == "p_neus" and ped_sex_general_expression_Cond == "tongueWrap", At("gensex_oral[p_activeno]_frontHead_exp_iLight right05", ped_eyes_iLight_trans),
                "True", Null())

## TEARS

    contains:
        ConditionSwitch(

                ntlong == 0, Null(),
            # 00
                p_active  == "p_neus" and nteye in [0, "front00", "right00", "left00", "up00", "down00"], At("gensex_oral_n_frontHead_exp_tears 00_0[ntlong]", truecenter),
            #01
                p_active  == "p_neus" and nteye in [1, "front01", "right01", "left01", "up01", "down01"], At("gensex_oral_n_frontHead_exp_tears 01_0[ntlong]", truecenter),
            #02
                p_active  == "p_neus" and nteye in [2, "front02", "right02", "left02", "up02", "down02"], At("gensex_oral_n_frontHead_exp_tears 02_0[ntlong]", truecenter),
            #03
                p_active  == "p_neus" and nteye in [3, "front03", "right03", "left03", "up03", "down03"], At("gensex_oral_n_frontHead_exp_tears 03_0[ntlong]", truecenter),
            #04
                p_active  == "p_neus" and nteye in [4, "front04", "right04", "left04", "up04", "down04"], At("gensex_oral_n_frontHead_exp_tears 04_0[ntlong]", truecenter),
            #05
                p_active  == "p_neus" and nteye in [5, "front05", "right05", "left05", "up05", "down05"], At("gensex_oral_n_frontHead_exp_tears 05_0[ntlong]", truecenter),
            #06
                p_active  == "p_neus" and nteye in [6, "front06"], At("gensex_oral_n_frontHead_exp_tears 06_0[ntlong]", truecenter),
            #07

                p_active  == "p_neus" and nteye in [7, "front07"], At("gensex_oral_n_frontHead_exp_tears 07_0[ntlong]", truecenter),
            #08

                p_active  == "p_neus" and nteye in [8, "front08"], At("gensex_oral_n_frontHead_exp_tears 08_0[ntlong]", truecenter),

                "True", Null())

                #"True", At("gensex_oral_n_frontHead_exp_tears empty", truecenter))

## EYEBROWS
    contains:
        ConditionSwitch(
                ped_sex_general_expression_Cond == "closed", At("gensex_oral[p_activeno]_frontHead_exp_eyebrows sadx02", truecenter),
                ped_sex_general_expression_Cond == "indifferent", At("gensex_oral[p_activeno]_frontHead_exp_eyebrows surprisex01", truecenter),
                ped_sex_general_expression_Cond in ["angry", "disgust", "angryLick"], At("gensex_oral[p_activeno]_frontHead_exp_eyebrows angryx03", truecenter),
                ped_sex_general_expression_Cond == "veryAngry", At("gensex_oral[p_activeno]_frontHead_exp_eyebrows angryx06", truecenter),
                ped_sex_general_expression_Cond == "lust", At("gensex_oral[p_activeno]_frontHead_exp_eyebrows suspiciousx02", truecenter),
                ped_sex_general_expression_Cond == "lustSmile", At("gensex_oral[p_activeno]_frontHead_exp_eyebrows suspiciousx02", truecenter),
                ped_sex_general_expression_Cond == "lustToYou", At("gensex_oral[p_activeno]_frontHead_exp_eyebrows sadx05", truecenter),
                ped_sex_general_expression_Cond == "lustAngry", At("gensex_oral[p_activeno]_frontHead_exp_eyebrows suspiciousx02", truecenter),
                ped_sex_general_expression_Cond in ["surpriseLeft", "surpriseRight"], At("gensex_oral[p_activeno]_frontHead_exp_eyebrows surprisex01", truecenter),
                ped_sex_general_expression_Cond == "surpriseDown", At("gensex_oral[p_activeno]_frontHead_exp_eyebrows surprisex01", truecenter),
                ped_sex_general_expression_Cond == "angryFront", At("gensex_oral[p_activeno]_frontHead_exp_eyebrows angryx04", truecenter),
                ped_sex_general_expression_Cond == "angryRight", At("gensex_oral[p_activeno]_frontHead_exp_eyebrows angryx04", truecenter),
                ped_sex_general_expression_Cond == "tongueWrap", At("gensex_oral[p_activeno]_frontHead_exp_eyebrows suspiciousx02", truecenter),
                "True", Null())

## MOUTH
    contains:
        ConditionSwitch(

                ped_sex_general_expressionJaw_Cond in ["blow_below_05_happy", "blow_below_bite", "blow_below_05", "blow_below_04", "blow_below_03", "blow_below_02", "blow_below_01", "blow_below_03b"], Null(),

                ped_sex_general_expression_Cond == "tongueWrap" and ped_sex_blow_Cond == False, At("gensex_oral[p_activeno]_frontHead_exp_mouth happy_TalkingxExtra", truecenter),

                ped_sex_general_expression_Cond == "closed" and ped_sex_blow_Cond == False, At("gensex_oral[p_activeno]_frontHead_exp_mouth sad_licking_b", truecenter),
                ped_sex_general_expression_Cond == "indifferent" and ped_sex_blow_Cond == False, At("gensex_oral[p_activeno]_frontHead_exp_mouth sad_Silentx03", truecenter),
                ped_sex_general_expression_Cond in ["angry", "disgust"] and ped_sex_blow_Cond == False, At("gensex_oral[p_activeno]_frontHead_exp_mouth sad_Silentx04", truecenter),

                ped_sex_general_expression_Cond == "angryLick" and ped_sex_blow_Cond == False, At("gensex_oral[p_activeno]_frontHead_exp_mouth sad_Talkingx03", truecenter),

                ped_sex_general_expression_Cond == "veryAngry" and ped_sex_blow_Cond == False, At("gensex_oral[p_activeno]_frontHead_exp_mouth sad_Silentx06", truecenter),
                ped_sex_general_expression_Cond == "lust" and ped_sex_blow_Cond == False, At("gensex_oral[p_activeno]_frontHead_exp_mouth sad_licking_b", truecenter),
                ped_sex_general_expression_Cond == "lustSmile" and ped_sex_blow_Cond == False, At("gensex_oral[p_activeno]_frontHead_exp_mouth happybiting_Silentx06", truecenter),
                ped_sex_general_expression_Cond == "lustToYou" and ped_sex_blow_Cond == False, At("gensex_oral[p_activeno]_frontHead_exp_mouth happy_Silentx09", truecenter),
                ped_sex_general_expression_Cond == "lustAngry" and ped_sex_blow_Cond == False, At("gensex_oral[p_activeno]_frontHead_exp_mouth sadbiting_Silentx06", truecenter),
                ped_sex_general_expression_Cond in ["surpriseLeft", "surpriseRight"] and ped_sex_blow_Cond == False, At("gensex_oral[p_activeno]_frontHead_exp_mouth sad_Silentx03", truecenter),
                ped_sex_general_expression_Cond == "surpriseDown" and ped_sex_blow_Cond == False, At("gensex_oral[p_activeno]_frontHead_exp_mouth sad_Silentx03", truecenter),
                ped_sex_general_expression_Cond == "angryFront" and ped_sex_blow_Cond == False, At("gensex_oral[p_activeno]_frontHead_exp_mouth sad_Silentx09", truecenter),
                ped_sex_general_expression_Cond == "angryRight" and ped_sex_blow_Cond == False, At("gensex_oral[p_activeno]_frontHead_exp_mouth sad_Silentx09", truecenter),

                "True", Null())

## GLASSES

    contains:
        ConditionSwitch(
            p_activeno == "_n" and n_withoutGlasses_story == False and n_withoutGlasses_Cond == False, At("gensex_oral_n_frontHead_glasses", truecenter),
            "True", Null()
        )



label ped_sex_oral_blow_Check:

    if ped_sex_general_expression_Cond == "closed":
        $ nteye = "front08"
    elif ped_sex_general_expression_Cond == "indifferent":
        $ nteye = "front08"
    elif ped_sex_general_expression_Cond in ["angry", "angryLick"]:
        $ nteye = "front08"
    elif ped_sex_general_expression_Cond == "disgust":
        $ nteye = "front06"
    elif ped_sex_general_expression_Cond == "veryAngry":
        $ nteye = "front08"
    elif ped_sex_general_expression_Cond == "lust":
        $ nteye = "front04"
    elif ped_sex_general_expression_Cond == "lustSmile":
        $ nteye = "front05"
    elif ped_sex_general_expression_Cond == "lustToYou":
        $ nteye = "front05"
    elif ped_sex_general_expression_Cond == "lustAngry":
        $ nteye = "front05"
    elif ped_sex_general_expression_Cond == ["surpriseLeft", "surpriseRight"]:
        $ nteye = "front01"
    elif ped_sex_general_expression_Cond == "surpriseDown":
        $ nteye = "down01"
    elif ped_sex_general_expression_Cond == "angryFront":
        $ nteye = "front05"
    elif ped_sex_general_expression_Cond == "angryRight":
        $ nteye = "right05"

    if ped_sex_general_action_Cond in ped_sex_general_oral_list:
        $ ped_sex_blow_Cond = True
        $ ped_sex_general_expressionJaw_Cond = ""
    elif ped_sex_general_action_Cond in ped_sex_general_lick_list:
        progcheck "She's licking your dick."
        $ ped_sex_blow_Cond = False
    else:
        $ ped_sex_blow_Cond = False

    # if ped_sex_general_action_Cond in ["o01_01", "o01_02",  "o01_03",  "o01_04",  "o01_05", "o02_01", "o02_02",  "o02_03",  "o02_04",  "o02_05", "o03_01", "o03_02",  "o03_03",  "o03_04",  "o03_05", "o04_01", "o04_02",  "o04_03",  "o04_04",  "o04_05", "o05_01", "o05_02",  "o05_03",  "o05_04",  "o05_05"]:

    #     $ ped_sex_blow_Cond = True

    # else:

    #     $ ped_sex_blow_Cond = False

    return


image ped_sex_missionary_expression_img:

    contains:
        ConditionSwitch(
            p_active == "p_neus", At("gensex_missionary_n_head_exp_blush " + nblushNumber, truecenter),
            "True", At("gensex_missionary_d_head_exp_blush 03", truecenter)
            )


################################################################################
################################################################################
########################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
########################################
##


label gensex_oral_c_frontHead_exp_label:

    if df_blush <= 0:
        $ df_blush = 0
        show gensex_oral_d_frontHead_exp_blush empty

    elif df_blush == 1:
        show gensex_oral_d_frontHead_exp_blush 01
    elif df_blush == 2:
        show gensex_oral_d_frontHead_exp_blush 02
    elif df_blush == 3:
        show gensex_oral_d_frontHead_exp_blush 03
    elif df_blush == 4:
        show gensex_oral_d_frontHead_exp_blush 04
    elif df_blush == 5:
        show gensex_oral_d_frontHead_exp_blush 05
    elif df_blush == 6:
        show gensex_oral_d_frontHead_exp_blush 06

    elif df_blush > 7:
        $ df_blush = 7
        show gensex_oral_d_frontHead_exp_blush 07

######
    
    if df_eye in ["front00", "right00", "left00", "down00", "up00"]:
        show gensex_oral_d_frontHead_exp_eyes 00

        if df_eye == "front00":
            show gensex_oral_d_frontHead_exp_iris front00
        elif df_eye == "right00":
            show gensex_oral_d_frontHead_exp_iris right00
        elif df_eye == "left00":
            show gensex_oral_d_frontHead_exp_iris left00
        elif df_eye == "down00":
            show gensex_oral_d_frontHead_exp_iris down00
        elif df_eye == "up00":
            show gensex_oral_d_frontHead_exp_iris up00

    elif df_eye in ["front01", "right01", "left01", "down01", "up01"]:
        show gensex_oral_d_frontHead_exp_eyes 01

        if df_eye == "front01":
            show gensex_oral_d_frontHead_exp_iris front01
        elif df_eye == "right01":
            show gensex_oral_d_frontHead_exp_iris right01
        elif df_eye == "left01":
            show gensex_oral_d_frontHead_exp_iris left01
        elif df_eye == "down01":
            show gensex_oral_d_frontHead_exp_iris down01
        elif df_eye == "up01":
            show gensex_oral_d_frontHead_exp_iris up01

    elif df_eye in ["front02", "right02", "left02", "down02", "up02"]:
        show gensex_oral_d_frontHead_exp_eyes 02

        if df_eye == "front02":
            show gensex_oral_d_frontHead_exp_iris front02
        elif df_eye == "right02":
            show gensex_oral_d_frontHead_exp_iris right02
        elif df_eye == "left02":
            show gensex_oral_d_frontHead_exp_iris left02
        elif df_eye == "down02":
            show gensex_oral_d_frontHead_exp_iris down02
        elif df_eye == "up02":
            show gensex_oral_d_frontHead_exp_iris up02

    elif df_eye in ["front03", "right03", "left03", "down03", "up03"]:
        show gensex_oral_d_frontHead_exp_eyes 03

        if df_eye == "front03":
            show gensex_oral_d_frontHead_exp_iris front03
        elif df_eye == "right03":
            show gensex_oral_d_frontHead_exp_iris right03
        elif df_eye == "left03":
            show gensex_oral_d_frontHead_exp_iris left03
        elif df_eye == "down03":
            show gensex_oral_d_frontHead_exp_iris down03
        elif df_eye == "up03":
            show gensex_oral_d_frontHead_exp_iris up03

    elif df_eye in ["front04", "right04", "left04", "down04", "up04"]:
        show gensex_oral_d_frontHead_exp_eyes 04

        if df_eye == "front04":
            show gensex_oral_d_frontHead_exp_iris front04
        elif df_eye == "right04":
            show gensex_oral_d_frontHead_exp_iris right04
        elif df_eye == "left04":
            show gensex_oral_d_frontHead_exp_iris left04
        elif df_eye == "down04":
            show gensex_oral_d_frontHead_exp_iris down04
        elif df_eye == "up04":
            show gensex_oral_d_frontHead_exp_iris up04

    elif df_eye in ["front05", "right05", "left05", "down05", "up05"]:
        show gensex_oral_d_frontHead_exp_eyes 05

        if df_eye == "front05":
            show gensex_oral_d_frontHead_exp_iris front05
        elif df_eye == "right05":
            show gensex_oral_d_frontHead_exp_iris right05
        elif df_eye == "left05":
            show gensex_oral_d_frontHead_exp_iris left05
        elif df_eye == "down05":
            show gensex_oral_d_frontHead_exp_iris down05
        elif df_eye == "up05":
            show gensex_oral_d_frontHead_exp_iris up05

    elif df_eye in ["front06", "front07", "front08", "empty"]:
        show gensex_oral_d_frontHead_exp_iris empty

    if df_eye == "front06":
        show gensex_oral_d_frontHead_exp_eyes 06
    elif df_eye == "front07":
        show gensex_oral_d_frontHead_exp_eyes 07
    elif df_eye == "front08":
        show gensex_oral_d_frontHead_exp_eyes 08


    return