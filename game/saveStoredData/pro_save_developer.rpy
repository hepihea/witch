
## Press "Alt + s" To execute.

init python:

    import pygame

    import renpy.compat.pickle as cPickle


    def create_pro_save_data_string():

        data = cPickle.dumps(_pro_save_store_data)

        try:

            fn = os.path.join( 
                renpy.config.gamedir, 
                #*_pro_save_file_format.format(_pro_save_label).split("/"))
                *store._pro_save_file_format.format( _pro_save_label).split("/"))

            with open(fn, "w") as f:

                f.write(data.replace("\n","·"))

        except Exception as e:

            renpy.notify(e)


        # Note from Remix:
        #     def __init__(self):
        #     type classes are okay, whereas
        #     def __init__(self, name, title):
        #     type classes are not.


        # Note:
        # Girl() would be okay if you coded it to allow no args...
        #     class Girl():

        #         def __init__(self, *args, enslavement=0, pleasure=0):
        #             """
        #             Main Girl Object.
        #             """

        #             self.name = args[0] if args else "default name"
        #             self.base_dir = args[1] if args else "default dir"

        # Anything extra can, if needed, be done in the label it jumps to

        # label jump_target_name:
        #     $ girl_1 = Girl(name="Minxy", base_dir="images/")
        #     ## or
        #     $ girl_1.name = "Minxy"
        #     ## ...

    def pro_save_get_store():

        _pro_save_saved_objects = (
            Pedrera_Body,
            PointLocker,
            #Girl,
        )

        _pro_save_ignore_vars = [
            "i", #"window_icon.ico"
            "basestring",
            "suppress_overlay",
            "nvl_list",
            "mouse_visible",
            "main_menu",
            "quick_menu",
            "save_name",
            "PY2",
            "protname",
            # "neusname",
            "is_save_allowed",
            "neus_glasses",
            "Tendolarsversion",
            "Platinumversion",
            "programming_check",
            "Steam_check",
            "PlatinumHelp",
            "Tendolarstext",
            "Platinumtext",
            "p_neg",
            "p_negx2",
            "p_pos",
            "walkthrough_patreon",
            "update_patreon_eng",
            "hir_ple",
            "hir_painass",
            "hn",
            "hh",
            "p_but",
            "hd",
            "hir_dilass",
            "dass_001_points_med",
            "p_diff",
            "hir_dom",
            "hir_hap",
            "hir_org",

            "gallery_sections_page",
            "gallery_image_objects",
            "gallery_sections",
            "lang",
            "startmenudisclaimer_ADULT",
            "startmenudisclaimer_ALPHA",
            "gallery_type",
            "gallery_image_thumbnail_rows",
            "gallery_image_sections",
            "gallery_image_sections_index",
            "startmenudisclaimer_PATREON",
            "gallery_image_sections_page",
            "startmenudisclaimer_DISCLAIMER",
            "gallery_sections_index",
            "all_voices",
            "gallery_viewport_size",
            "gallery_image_size",
            "gallery_zoom_settings",
        ]

        _pro_save_default_values = {
            #"Pedrera_char_Cond" : "NeusClose",
            #"hir_hap" : "{image=gui/icons/dungeon/dun_hap_hi.png}",
            "p_activeno" : "_d",
            "afternight04_condom_on" : True,
            #"hir_dom" : "{image=gui/icons/dungeon/dun_dom_hi.png}",
            "ped_sex_general_action_Cond" : "talk",
            "gensex_oral_others_front_left_Cond" : "",
            #"p_pos" : "{color=#6b4}Positive Points Message{/color}",
            "n_exp_Cond" : "empty",
            #"p_diff" : "Necesitas algo distinto para ver otro desenlace.",
            "ped_sex_general_69_cover" : "over",
            "ped_sex_general_expression_Cond" : "talk",
            "hir_heart" : "{image=gui/icons/heart_pos_hi.png}",
            "afternight05_Pedrera_Vegan_ColdBlood" : True,
            "ped_sex_general_oral_list" : ["o01_01","o02_01","o03_01","o04_01",
                "o01_02","o02_02","o03_02","o04_02","o01_03","o02_03","o03_03",
                "o04_03","o01_04","o02_04","o03_04","o04_04","o01_05","o02_05",
                "o03_05","o04_05"],
            #"nblushNumber" : "02", 
            #"Tendolarsversion" : True,
            "gensex_oral_d_blow_exp_eyes" : "06",
            #"p_negx2" : "{color=#e22}Negative Points Repetitive Message{/color}",
            "p_ao_assSmacked" : "right",
            "ped_doggy_v_a_at" : ["v01_01","v01_02","v01_03","v01_04","v01_05",
                "v02_01","v02_02","v02_03","v02_04","v02_05","a01_01","a01_02",
                "a01_03","a01_04","a01_05","a02_01","a02_02","a02_03","a02_04",
                "a02_05","at01_01","at01_02","at01_03","at01_04","at01_05"],
            "FuckH_act_focus_" : "nothing",
            "p_ao_dThrob_vel" : 1,
            "can_click" : True,
            "p_ao_n_horns" : "_cut01",
            "stra_number" : 500,
            #"protmaster" : "Maestro",
            "girl_difficulty" : {1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1,
            "default" : 0},
            #"pdaytime" : "01_afternoon",
            "ped_sex_num" : 1,
            "beach_sex_blow_expression_Cond" : "closed",
            "FuckH_pose_" : "onFeet",
            "ped_doggy_v_a_vt_at" : ["v01_01","v01_02","v01_03","v01_04",
                "v01_05","v02_01","v02_02","v02_03","v02_04","v02_05","a01_01",
                "a01_02","a01_03","a01_04","a01_05","a02_01","a02_02","a02_03",
                "a02_04","a02_05","vt01_01","vt01_02","vt01_03","vt01_04",
                "vt01_05","at01_01","at01_02","at01_03","at01_04","at01_05"],
            "ped_cs_kiss_eyes_Cond" : "right",
            "p_ao_whispers_n" : 5.0,
            "ntlong" : 1,
            "gensex_briding_bg_Cond" : "deepsea",
            "p_ao_sexPart" : "_v",
            "FuckH_act_body_" : "back",
            "hir_sti" : "{image=gui/icons/dungeon/dun_sti_hi.png}",
            "p_prot_69_blowjob_received" : ["blowjob_received","blowjobDeep_received"],
            "ped_1_10_dictionary" : {},
            "ped_1_5_dictionary" : {},
            "joan_names" : ["joan","juan","john","johan","johann","johannes",
                "xuan","jon","jan","johnny","jack","giovanni","gianni","gian",
                "giuvanni","jonas","jovan","hans","ivan","yann"],
            "pday_day" : 1,
            "night04_pedrera_blowjob_pov02_ghosts_001" : True,
            "gensex_oral_d_blow_exp_eyebrows" : "serious",
            "day06_neusAlone_sex" : "vaginal",
            "nblush" : 2,
            #"dass_001_points_med" : "20 <= pl.dp <= 23",
            "p_neuspos" : "n_closefromup_",
            "ped_sex_b_num" : 1,
            #"Tendolarstext" : "PREMIUM",
            "gallery_image_thumbnail_cols" : 4,
            #"neus_glasses" : True,
            #"hir_dilass" : "{image=gui/icons/dungeon/dun_dilanal_hi_01.png}",
            #"hd" : "{image=gui/icons/heart_d.png}",
            "p_activen" : "didac",
            "p_ao_n_vel" : 1,
            "dass_001_points_high" : "pl.dp >= 24",
            "p_ao_background" : "ground",
            "dundiff" : 50,
            "c_spaceNum" : 60,
            #"p_dictCloseOrgasm" : {},
            #"p_but" : "{color=#e224}Pero no m\xe1s de{/color}",
            "ped_cs_kiss_n_arm_Cond" : "down",
            "night04_pedrera_blowjob_pov_Conditional_026" : True,
            #"gensex_oral_d_blow_exp_blush" : "04",
            #"dadname" : "txell",
            #"hh" : "{image=gui/icons/heart_hi.png}",
            "saturation_tint_values" : {"superdark" : (0.5, 0.22, 0.25, 0.45),
            "verydark" : (0.6, 0.6, 0.6, 0.75),
            "reallydark" : (0.5, 0.42, 0.45, 0.5),
            "underwater" : (0.5, 0.4, 0.65, 0.8),
            "default" : (1.0, 1.0, 1.0, 1.0),
            "dark" : (0.7, 0.8, 0.8, 0.9),
            "green" : (0.7, 0.97, 1.0, 0.95),
            "afternoon" : (0.7, 0.97, 0.87, 0.7)},
            #"night04_pedrera_blowjob_pov_010_blush_Con_01" : True,
            "hm" : "{image=gui/icons/heart_m.png}",
            "ped_sex_general_lick_list" : ["o00l_01","o00l_02","o00l_03",
                "o00l_04","o00l_05"],
            #"s_ntlong" : "01",
            #"night04_pedrera_blowjob_pov_010_eyebrows_Con_serious" : True,
            "ped_sex_blow_MChand" : "off",
            "gensex_oral_d_mast_left" : "rest",
            "p_ao_n_hipsImg" : "_open", 
            #"update_patreon_eng" : "{a=https://www.patreon.com/jonnymelabo}update{/a}",
            #"p_ao_mc_dick_num" : 6,
            #"g_zoomNumber" : 0.2,
            "MShooter_Bracelet_var" : ["GOLD","SILVER","BRONZE","PLASTIC"],
            #"hir_org" : "{image=gui/icons/dungeon/dun_org_hi.png}", 
            #"programming_check" : True,
            "p_ao_ground" : "ground",
            "myFuckinAlpha" : 1.0,
            "is_save_allowed" : True,
            "p_ao_n_hipsTrans" : 0.5,
            #"hir_ple" : "{image=gui/icons/dungeon/dun_ple_hi.png}",
            #"hir_painass" : "{image=gui/icons/dungeon./dun_painanal_hi.png}",
            #"Platinumtext" : "PLATINUM",
            "beach_fuckr_erection_Cond" : "erect",
            #"ghost_sM" : 2.5,
            #"walkthrough_patreon" : "{a=https://www.patreon.com/posts/8830789}{size=32}gu\xeda{/size}{/a}",
            "ped_1_20_dictionary" : {},
            "ped_doggy_v_a" : ["v01_01","v01_02","v01_03","v01_04","v01_05",
                "v02_01","v02_02","v02_03","v02_04","v02_05","a01_01","a01_02",
                "a01_03","a01_04","a01_05","a02_01","a02_02","a02_03","a02_04",
                "a02_05"],
            "day06_ending_city" : "paris",
            "night04_pedrera_blowjob_pov_010_eyes_Con_camera03_03" : True,
            "dass_001_points_low" : "pl.dp <= 19",
            #"p_neus_blowjob_done_ACCEPTED" : True, 
            #"Platinumversion" : True,
            #"hn" : "{image=gui/icons/heart_n.png}",
            #"p_neg" : "{color=#e22}Negative Points Message{/color}", 
            #"i" : "window_icon.ico",
            "gensex_oral_d_mast_right" : "rest",
            "FuckH_orn_focus_" : "noone"
        }

        store_data = {}

        for k in store.__dict__:

            if k.startswith("_") or k in _pro_save_ignore_vars:

                continue

            od = getattr(store, k)

            if isinstance(od, (int, float, bool, basestring, unicode)) and not od:

                continue

            if k in _pro_save_default_values:

                if od == _pro_save_default_values[k]:

                    continue

            if isinstance(od, _pro_save_saved_objects):

                vdict = {
                    "class_name" : od.__class__.__name__
                }

                tmp_obj = globals()[od.__class__.__name__]()

                for vk in [
                        j for j in od.__dict__ 
                        if not hasattr(object, j) 
                        and not callable(od)]:

                    if getattr(od, vk) != getattr(tmp_obj, vk):

                        vdict[vk] = getattr(od, vk)

                store_data["{}.state".format(k)] = vdict

                del tmp_obj

            elif isinstance(od, (bool, basestring, unicode, int, float, tuple, set, list, dict)):

                store_data[k] = od

        return store_data


    _file_line_label_map = {}

    def get_label_for_location(location):
        """ 
        Return label name relevant for the filename and linenumber
        """ 
        global _file_line_label_map
        filename, linenumber = location
        if "tl" in filename:
            filename = "game/" + "/".join(filename.split("/")[3:])
        if not filename in _file_line_label_map:
            poss_labels = [k for k in renpy.get_all_labels() if k[0] != "_"]
            for k in poss_labels:
                fn = renpy.game.script.namemap[k].filename
                ln = renpy.game.script.namemap[k].linenumber
                if not fn in _file_line_label_map:
                    _file_line_label_map[fn] = []
                _file_line_label_map[fn].append( (ln, k) )
            for fn in _file_line_label_map:
                # sort reverse
                _file_line_label_map[fn].sort(key=lambda r:-r[0])
        if filename in _file_line_label_map:
            for lineno, label in _file_line_label_map[filename]:
                if lineno < linenumber:
                    return label
        return "{} : {}".format(filename, linenumber)


    def pro_save_get_label():

        return get_label_for_location(renpy.get_filename_line())


    def pro_save_launch():

        renpy.free_memory()
        store._pro_save_label = pro_save_get_label()
        store._pro_save_store_data = pro_save_get_store()

        return


default _pro_save_label = ""
default _pro_save_store_data = {}


style pro_save_outer_frame:
    background Frame(
        Text("\u25C9", font="DejaVuSans.ttf", size=42, color="#FFF"), 
        18, 18)

style pro_save_inner_frame:
    background Frame(
        Text("\u25C9", font="DejaVuSans.ttf", size=40, color="#111"), 
        18, 18)



screen pro_save_create():

    modal True

    frame:
        area (0.05, 0.05, 0.9, 0.9)
        style "pro_save_outer_frame"
        padding (4, 4)

        frame:
            area (0, 0, 1.0, 1.0)
            style "pro_save_inner_frame"
            padding (20, 20)

            vbox:
                spacing 4
                hbox:
                    spacing 20
                    textbutton "Create Data File":
                        action Function(create_pro_save_data_string)
                    textbutton "Close Window":
                        action Hide("pro_save_create")
                    # textbutton "Copy Defaults":
                    #     action Function(
                    #                     pygame.scrap.put,
                    #                     pygame.SCRAP_TEXT, 
                    #                     str(_pro_save_store_data).encode("utf-8"))

                hbox:
                    spacing 12

                    text "Label Name"

                    input:
                        value VariableInputValue("_pro_save_label")
                        default _pro_save_label

                viewport:
                    area (0,0, 1.0, 0.75)
                    scrollbars "vertical"
                    draggable True
                    mousewheel True
                    vbox:
                        for k,v in _pro_save_store_data.items():
                            hbox:
                                spacing 4
                                textbutton "[k!q]":
                                    action Function(
                                        pygame.scrap.put,
                                        pygame.SCRAP_TEXT, 
                                        k.encode("utf-8"))
                                text "   [v!q]" size 16  



init python:

    if config.developer == True:

        config.underlay.append(
            renpy.Keymap( 
                alt_K_s = [Function(pro_save_launch), Show("pro_save_create")]
            )
        )
