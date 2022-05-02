default afternigh04_sexwithDidac_RemoveAll_dickInside = False

#########################################################
#########################################################
#########################################################

label Remove:

#########################################################

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.07.08") or (not current_pose.id == "pose_1" and config.version < "00.90.00"):

            call endupdatescript_sexbattle

#########################################################

    $ __suffix = []
    $ __prefix = "Remove."

#########################################################

    $ afternight04__prehfix_Remove = True
    $ afternight04__a_prehfix_Remove = True

    call afternigh04_sexwithDidac_RemoveAll_scene

    if afternight04_condom_broken == False:

        call afternigh04_sexwithDidac_RemoveAll_converstation

    jump expression __prefix + "call_screen"

    label .call_screen:
        call screen dummy_screen()

###############################################################################
##############################################################################
#############################################################################

label afternigh04_sexwithDidac_RemoveAll_scene:

    if afternight04_condom_broken == False:

        $ afternight04__Remove_Done += 1

        if (mc_body.store["dick"] == "" or mc_body.store["dick"] == "Pussy_dick_out"): 

            ##
            $ afternight04__Remove_Failed += 1
            ##

            $ afternigh04_sexwithDidac_RemoveAll_dickInside = False

        else: # DICK OVER or INSIDE her.

            ##
            $ afternight04__Remove_Success += 1
            ##

            $ afternigh04_sexwithDidac_RemoveAll_dickInside = True

        call afternigh04_sexwithDidac_RemoveAll_image

        return

###############################################################################
##############################################################################
#############################################################################
###############################################################################
##############################################################################
#############################################################################

label afternigh04_sexwithDidac_RemoveAll_image:

    if current_pose.id == "pose_1":

        #if pose01_right_boob.get_action("RBoob_Slap").times_done + pose01_right_boob.get_action("RBoob_Slap").times_failed == 0:
        if (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 0:  
            show afternight04_sexbattle_d_boobR wet_00_smash_00_a_static
        elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 1:
            show afternight04_sexbattle_d_boobR wet_00_smash_01_a_static
        elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 2:
            show afternight04_sexbattle_d_boobR wet_00_smash_02_a_static
        elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 3:
            show afternight04_sexbattle_d_boobR wet_00_smash_03_a_static
        elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 4:
            show afternight04_sexbattle_d_boobR wet_00_smash_04_a_static
        elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 5:
            show afternight04_sexbattle_d_boobR wet_00_smash_05_a_static
        elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) >= 6:
            show afternight04_sexbattle_d_boobR wet_00_smash_06_a_static

        if (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 0: 
            show afternight04_sexbattle_d_boobL wet_00_smash_00_a_static
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 1:
            show afternight04_sexbattle_d_boobL wet_00_smash_01_a_static
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 2:
            show afternight04_sexbattle_d_boobL wet_00_smash_02_a_static
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 3:
            show afternight04_sexbattle_d_boobL wet_00_smash_03_a_static
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 4:
            show afternight04_sexbattle_d_boobL wet_00_smash_04_a_static
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 5:
            show afternight04_sexbattle_d_boobL wet_00_smash_05_a_static
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) >= 6:
            show afternight04_sexbattle_d_boobL wet_00_smash_06_a_static

        show afternight04_sexbattle_mc_handL empty
        show afternight04_sexbattle_mc_handR empty

        show afternight04_sexbattle_mc_tongue_clitoris empty

        show afternight04_sexbattle_mc_tongue_pussy empty
        show afternight04_sexbattle_mc_tongue_anal empty

        show afternight04_sexbattle_mc_handR_penetrate_pussy empty
        show afternight04_sexbattle_mc_handR_penetrate_anal empty

        show afternight04_sexbattle_d_legs_over_anal empty:
            afternight04_sexbattle_empty_NOposition
        show afternight04_sexbattle_d_legs_top_anal empty:
            afternight04_sexbattle_d_pubicpart_pos

        show afternight04_sexbattle_d_legs_stomach_anal empty:
            afternight04_sexbattle_empty_NOposition
        show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
            afternight04_sexbattle_d_pubicpart_pos

        show afternight04_sexbattle_mc_dick_anal empty:
            afternight04_sexbattle_empty_NOposition


        if afternight04_condom_broken == False:

            show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
                afternight04_sexbattle_d_pubicpart_pos
            show afternight04_sexbattle_d_legs_over_pussy empty:
                afternight04_sexbattle_empty_NOposition
            show afternight04_sexbattle_d_legs_top_pussy empty:
                afternight04_sexbattle_d_pubicpart_pos

            show afternight04_sexbattle_mc_dick_pussy empty:
                afternight04_sexbattle_empty_NOposition

            show afternight04_sexbattle_d_legs_stomach_pussy empty:
                afternight04_sexbattle_empty_NOposition

            show afternight04_sexbattle_d_legs_base wet_00_a:
                xanchor 0.0 yanchor 0.0

            #call afternight04_sexbattle_pubic_emptiness

        else:

            call afternight04_condom_broken_scene

        with dissolve

###############################################################################
##############################################################################
#############################################################################

    elif current_pose.id == "pose_2":
        
        ## LBOOB

        if (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 0:
            show afternight04_sexbattle_d_boobL wet_00_smash_00_b:
                afternight04_sexbattle_d_boobL_position_b
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 1:
            show afternight04_sexbattle_d_boobL wet_00_smash_01_b:
                afternight04_sexbattle_d_boobL_position_b
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 2:
            show afternight04_sexbattle_d_boobL wet_00_smash_02_b:
                afternight04_sexbattle_d_boobL_position_b
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 3:
            show afternight04_sexbattle_d_boobL wet_00_smash_03_b:
                afternight04_sexbattle_d_boobL_position_b
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 4:
            show afternight04_sexbattle_d_boobL wet_00_smash_04_b:
                afternight04_sexbattle_d_boobL_position_b
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 5:
            show afternight04_sexbattle_d_boobL wet_00_smash_05_b:
                afternight04_sexbattle_d_boobL_position_b
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) >= 6:
            show afternight04_sexbattle_d_boobL wet_00_smash_06_b:
                afternight04_sexbattle_d_boobL_position_b

        ## RBUTTOCK

        if (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 0:
            show afternight04_sexbattle_d_buttockR wet_00_smash_00_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 1:
            show afternight04_sexbattle_d_buttockR wet_00_smash_01_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 2:
            show afternight04_sexbattle_d_buttockR wet_00_smash_02_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 3:
            show afternight04_sexbattle_d_buttockR wet_00_smash_03_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 4:
            show afternight04_sexbattle_d_buttockR wet_00_smash_04_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 5:
            show afternight04_sexbattle_d_buttockR wet_00_smash_05_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) >= 6:
            show afternight04_sexbattle_d_buttockR wet_00_smash_06_b_static:
                afternight04_sexbattle_empty_NOposition

        # LBUTTOCK

        if (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 0:
            show afternight04_sexbattle_d_buttockL wet_00_smash_00_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 1:
            show afternight04_sexbattle_d_buttockL wet_00_smash_01_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 2:
            show afternight04_sexbattle_d_buttockL wet_00_smash_02_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 3:
            show afternight04_sexbattle_d_buttockL wet_00_smash_03_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 4:
            show afternight04_sexbattle_d_buttockL wet_00_smash_04_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 5:
            show afternight04_sexbattle_d_buttockL wet_00_smash_05_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) >= 6:
            show afternight04_sexbattle_d_buttockL wet_00_smash_06_b_static:
                afternight04_sexbattle_empty_NOposition

        # HANDS ACTIONS

        show afternight04_sexbattle_mc_handR  empty:
            afternight04_sexbattle_empty_position

        show afternight04_sexbattle_mc_handL empty:
            afternight04_sexbattle_empty_position

        # DICK TONGUE ACTIONS

        ##
        #show afternight04_sexbattle_mc_tongue_clitoris empty #Necessary?

        show afternight04_sexbattle_mc_tongue_pussy empty

        if afternight04_condom_broken == False:

            show afternight04_sexbattle_mc_dick_pussy empty

            #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

            # penetrate_pussy empty - penetrate_anal empty
            call afternight04_sexbattle_pubic_emptiness

            show afternight04_sexbattle_d_legs_over_pussy 002_wet_00_b

        else:

            call afternight04_condom_broken_scene

        with dissolve

###############################################################################
##############################################################################
#############################################################################

    elif current_pose.id == "pose_3":

        ## LBOOB

        if (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 0:
            show afternight04_sexbattle_d_boobL wet_00_smash_00_b:
                afternight04_sexbattle_d_boobL_position_b
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 1:
            show afternight04_sexbattle_d_boobL wet_00_smash_01_b:
                afternight04_sexbattle_d_boobL_position_b
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 2:
            show afternight04_sexbattle_d_boobL wet_00_smash_02_b:
                afternight04_sexbattle_d_boobL_position_b
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 3:
            show afternight04_sexbattle_d_boobL wet_00_smash_03_b:
                afternight04_sexbattle_d_boobL_position_b
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 4:
            show afternight04_sexbattle_d_boobL wet_00_smash_04_b:
                afternight04_sexbattle_d_boobL_position_b
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 5:
            show afternight04_sexbattle_d_boobL wet_00_smash_05_b:
                afternight04_sexbattle_d_boobL_position_b
        elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) >= 6:
            show afternight04_sexbattle_d_boobL wet_00_smash_06_b:
                afternight04_sexbattle_d_boobL_position_b

        ## RBUTTOCK

        if (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 0:
            show afternight04_sexbattle_d_buttockR wet_00_smash_00_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 1:
            show afternight04_sexbattle_d_buttockR wet_00_smash_01_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 2:
            show afternight04_sexbattle_d_buttockR wet_00_smash_02_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 3:
            show afternight04_sexbattle_d_buttockR wet_00_smash_03_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 4:
            show afternight04_sexbattle_d_buttockR wet_00_smash_04_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 5:
            show afternight04_sexbattle_d_buttockR wet_00_smash_05_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) >= 6:
            show afternight04_sexbattle_d_buttockR wet_00_smash_06_b_static:
                afternight04_sexbattle_empty_NOposition

        # LBUTTOCK

        if (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 0:
            show afternight04_sexbattle_d_buttockL wet_00_smash_00_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 1:
            show afternight04_sexbattle_d_buttockL wet_00_smash_01_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 2:
            show afternight04_sexbattle_d_buttockL wet_00_smash_02_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 3:
            show afternight04_sexbattle_d_buttockL wet_00_smash_03_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 4:
            show afternight04_sexbattle_d_buttockL wet_00_smash_04_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 5:
            show afternight04_sexbattle_d_buttockL wet_00_smash_05_b_static:
                afternight04_sexbattle_empty_NOposition
        elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) >= 6:
            show afternight04_sexbattle_d_buttockL wet_00_smash_06_b_static:
                afternight04_sexbattle_empty_NOposition

        # HANDS ACTIONS

        show afternight04_sexbattle_mc_handR  empty:
            afternight04_sexbattle_empty_position

        show afternight04_sexbattle_mc_handL empty:
            afternight04_sexbattle_empty_position

        # DICK TONGUE ACTIONS

        ##
        #show afternight04_sexbattle_mc_tongue_clitoris empty #Necessary?

        show afternight04_sexbattle_mc_tongue_pussy empty

        if afternight04_condom_broken == False:

            show afternight04_sexbattle_mc_dick_pussy empty
            show afternight04_sexbattle_mc_dick_pussy empty

            #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

            # penetrate_pussy empty - penetrate_anal empty
            call afternight04_sexbattle_pubic_emptiness

            show afternight04_sexbattle_d_legs_over_pussy 002_wet_00_b

        else:

            call afternight04_condom_broken_scene

        with dissolve

##############################################################
#############################################################

    $ mc_body.store["right_hand"] = ""
    $ mc_body.store["left_hand"] = ""
    $ mc_body.store["tongue"] = ""

    if afternight04_condom_broken == False:

        $ mc_body.store["dick"] = ""

##############################################################
#############################################################
    
    # Previous RHand Action

    if current_pose.id == "pose_1":

        $ afternight04__a_prehfix_RArm_Grab = False
        $ afternight04__a_prehfix_LBoob_Grab = False
        $ afternight04__a_prehfix_LBoob_Slap = False
        $ afternight04__a_prehfix_LButtock_Massage = False
        $ afternight04__a_prehfix_LButtock_Slap = False
        $ afternight04__a_prehfix_LLeg_Massage = False
        $ afternight04__a_prehfix_LNipple_Pinch = False

    else:

        $ afternight04__a_prehfix_RBoob_Grab = False
        $ afternight04__a_prehfix_RBoob_Slap = False
        $ afternight04__a_prehfix_RButtock_Massage = False
        $ afternight04__a_prehfix_RButtock_Slap = False
        $ afternight04__a_prehfix_RLeg_Massage = False
        $ afternight04__a_prehfix_RNipple_Pinch = False

    $ afternight04__a_prehfix_Pussy_Fingers = False
    $ afternight04__a_prehfix_Anal_Fingers = False

    $ afternight04__a_prehfix_MMouth_Fingers = False
    $ afternight04__a_prehfix_MClitoris_Massage = False

    # Previous Tongue Action

    $ afternight04__a_prehfix_MClitoris_Tongue = False
    $ afternight04__a_prehfix_MMouth_Tongue = False
    $ afternight04__a_prehfix_Pussy_Tongue = False
    $ afternight04__a_prehfix_Anal_Tongue = False  # Rim Job
    $ afternight04__a_prehfix_RNipple_Lick = False  # Rim Job

    ## Remove

    $ afternight04__a_prehfix_Remove = False


##############################################################
#############################################################

    return

###############################################################################
##############################################################################
#############################################################################
###############################################################################
##############################################################################
#############################################################################

label afternigh04_sexwithDidac_RemoveAll_converstation:

    #if current_girl.total_try == 1:
    if afternight04__Remove_Success + afternight04__Remove_Failed == 1:

        if afternigh04_sexwithDidac_RemoveAll_dickInside == False:

            $ current_girl.pleasure -= 1

            $ debug ("POLLA FUERA 01")

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils front00_a
                show afternight04_sexbattle_d_eyebrows surprisex02_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Tanta puñetita con la lengua y las manos..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                with dissolve

            d "¡¿Para qué?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡¿Para quitarlo todo ahora?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¿A qué juegas [protname]?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "¿Por qué te quejas tanto?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils right01_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Lo que quiero es follar y que te dejes de mariconadas."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            pt "Está claro que no oye lo que dice..."

        else:

            $ debug ("POLLA DENTRO")

            $ current_girl.pleasure -= 2

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡¿Por qué diablos quitas la polla de ahí?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx01_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Sé lo que me hago..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡Pues a ver si se nota!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            pt "La madre que lo..."

    elif afternight04__Remove_Success + afternight04__Remove_Failed == 2:

        if afternigh04_sexwithDidac_RemoveAll_dickInside == False:
            
            $ current_girl.enslavement -= 1
            $ current_girl.pleasure -= 2

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "Tanta tontería con la lengua y las manos,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                with dissolve

            d "para luego volver a empezar de nuevo..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve
            
            d "Fóllame de una vez y déjate de tonterías."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve
        else:

            $ current_girl.enslavement -= 1
            $ current_girl.pleasure -= 4

            #if current_pose.id == "pose_1":

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡¿Otra vez quitas la polla?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            p "Dídac..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡No me vengas con la gilipollez de que sabes lo que te haces!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡Fóllame y déjate de hostias!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "..."


    elif afternight04__Remove_Success + afternight04__Remove_Failed == 3:

        if afternigh04_sexwithDidac_RemoveAll_dickInside == False:

            $ current_girl.enslavement -= 1
            $ current_girl.pleasure -= 4

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡¿Otra vez con lo mismo?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "Deja de quejarte tanto."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx02_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            p "Luego te me quejarás de que me he corrido muy pronto."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils right01_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils right02_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡Si lo que quiero es que me metas la polla!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡No que me manosees!."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            p "..."

            pt "EL muy idiota no se da cuenta lo estrecho que tiene el coño..."

            pt "Si hago lo que dice terminaré antes que él y entonces se cabreará."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "¿Estás esperando a que se me pase el arroz?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¿o qué?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx08_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            pt "¡¿Por qué demonios me preocupo por este imbécil?!"

        else:

            $ current_girl.enslavement -= 1
            $ current_girl.pleasure -= 6

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡¿OTRA VEZ SACÁNDOLA?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡¿Qué es lo que no entiendes de...?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡FÓ-"

            extend "LLA-"

            extend "ME!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx08_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            p "Dídac..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "¡¿No entiendes que la aparto para evitar correrme antes de tiempo?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡No me seas {i}pichafloja{/i}!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡y compórtate!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡Aguanta un poco!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡Coño!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx08_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            pt "Me encantaría ver lo que aguantaba él..."

            pt "Hipócrita de mierda..."

    elif afternight04__Remove_Success + afternight04__Remove_Failed == 4:

        if afternigh04_sexwithDidac_RemoveAll_dickInside == False:

            $ current_girl.enslavement -= 1
            $ current_girl.pleasure -= 4

        else:

            $ current_girl.enslavement -= 1
            $ current_girl.pleasure -= 6

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows angryx04_a
            with dissolve

        d "¿Piensas pasarte toda la noche igual...?"

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sad_Silentx05_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows angryx04_a
            with dissolve

    elif afternight04__Remove_Success + afternight04__Remove_Failed == 5:

        if afternigh04_sexwithDidac_RemoveAll_dickInside == False:

            $ current_girl.enslavement -= 1
            $ current_girl.pleasure -= 4

        else:

            $ current_girl.enslavement -= 1
            $ current_girl.pleasure -= 6

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sad_Talkingx004_a
            show afternight04_sexbattle_d_eyes 02_a
            show afternight04_sexbattle_d_pupils front02_a
            show afternight04_sexbattle_d_eyebrows angryx04_a
            with dissolve

        d "¡¿Otra vez?!"

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sad_Talkingx06_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils front03_a
            show afternight04_sexbattle_d_eyebrows angryx04_a
            with dissolve

        d "¡¿A qué coño estás jugando?!"

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sad_Silentx06_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows angryx04_a
            with dissolve

    elif afternight04__Remove_Success + afternight04__Remove_Failed >= 6:

        if afternigh04_sexwithDidac_RemoveAll_dickInside == False:

            #$ debug ("POLLA FUERA 02")

            $ current_girl.enslavement -= 1
            $ current_girl.pleasure -= 6

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if randomnum_1to5 == 1:

                d "¡Me sacas las manos pero no me follas!"

            elif randomnum_1to5 == 2:

                d "¡Decídete de una vez!"

            elif randomnum_1to5 == 3:

                d "¡¿Y ahora vuelves a sacar las manos?!"

            elif randomnum_1to5 == 4:

                d "¡¿Piensas pasarte toda la noche igual?!"

            elif randomnum_1to5 == 5:

                d "¡¿Se puede saber a qué estás jugando?!"

            ##

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            pt "Mierda..."

            ##


        else:

            $ debug ("POLLA DENTRO")

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if randomnum_1to5 == 1:

                $ current_girl.enslavement -= 1
                $ current_girl.pleasure -= 8

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡No me quites la polla de ahí coño!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                pt "Mierda..."

            elif randomnum_1to5 == 2:

                $ current_girl.enslavement -= 1
                $ current_girl.pleasure -= 8

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡Que no quites la polla he dicho!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                pt "Maldita sea..."

            elif randomnum_1to5 == 3:

                $ current_girl.enslavement -= 1
                $ current_girl.pleasure -= 5

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿Otra vez sacándola?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "¡Luego no te quejes si me corro demasiado pronto!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡No me seas {i}bocachancla{/i}!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Comportate como un hombre y aguanta!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡Joder!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                pt "Como se nota ahora que no es él quien tiene polla..."

            elif randomnum_1to5 == 4:

                $ current_girl.enslavement -= 1
                $ current_girl.pleasure -= 5

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡Que manía con sacar la polla!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "¡¿Quieres que me corra antes que tú?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "No me hagas esperar mucho."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "¡¿Eres consciente que lo estoy haciendo por hacerte un favor?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡Calla y fóllame!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                pt "Puto Dídac..."

            elif randomnum_1to5 == 5:

                $ current_girl.enslavement -= 1
                $ current_girl.pleasure -= 5

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx10_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿Por qué demonios la sacas otra vez?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "¡Por que te estoy haciendo un favor y hago lo que me da la gana!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "Sino te gusta,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "me voy."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "¡¿Queda claro?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "Sino me gusta como lo haces,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "voy a violarte."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "..."

                pt "Dan ganas de enviarle a la mierda..."

    ###########################
    ##########################

    ### RAPE OR NOT?

    $ afternight04_SheRapingYou = False

    call afternight04_RapeOrNot

    ###########################
    ##########################

    return