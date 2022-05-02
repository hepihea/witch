

image stra_handL empty = "images/general/empty.webp"
image stra_handL rest = SaturateTint("images/day05/pedrera/strangle/stra_handL_rest.webp")
image stra_handL stra = SaturateTint("images/day05/pedrera/strangle/stra_handL_stra.webp")

image stra_handR empty = "images/general/empty.webp"
image stra_handR rest = SaturateTint("images/day05/pedrera/strangle/stra_handR_rest.webp")
image stra_handR stra = SaturateTint("images/day05/pedrera/strangle/stra_handR_stra.webp")

image stra_neus_reference = "images/day05/pedrera/strangle/stra_neus_reference.webp"

transform stra_neus_exp_pos:
    truecenter
    zoom 0.62
    ypos 0.11
    #alpha 0.5

######################################################################
######################################################################
####################
######################################################################
######################################################################

default key_space_ = False
default key_mouse_ = False
default key_boh_ = False
default stra_number = 500
default str_adviceDad = 0
default str_talkNeus = 0

#default pl_np = 200

default dad_talks = 0

screen stra_neus():
    zorder -2
    $ str_vapor = (stra_number - 500) / 500.0

    if renpy.variant("pc"):
        key "keydown_K_SPACE" action SetVariable("key_space_", True)
        key "keyup_K_SPACE" action SetVariable("key_space_", False)
        key "mousedown_1" action SetVariable("key_mouse_", True)
        key "mouseup_1" action SetVariable("key_mouse_", False)
    else:
        key "mousedown_1" action SetVariable("key_mouse_", True)
        key "mouseup_1" action SetVariable("key_mouse_", False)


    if (renpy.variant("pc") and key_space_ and key_mouse_) or (not renpy.variant("pc") and key_mouse_):
        add "stra_handR stra"
        add "stra_handL stra"
        if stra_number > 995:
            add "n_closefromup_mouth sad_Talkingx02" xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 ypos 0.11 zoom 0.62 at scrappdissolve
        elif stra_number > 900:
            add "n_closefromup_mouth sad_Silentx16" xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 ypos 0.11 zoom 0.62 at scrappdissolve
        elif stra_number > 700:
            add "n_closefromup_mouth sad_Silentx15" xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 ypos 0.11 zoom 0.62 at scrappdissolve
        elif stra_number > 550:
            add "n_closefromup_mouth sad_Silentx13" xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 ypos 0.11 zoom 0.62 at scrappdissolve
        else:
            add "n_closefromup_mouth sad_Silentx12" xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 ypos 0.11 zoom 0.62 at scrappdissolve

    elif key_space_:
        add "stra_handR rest"
        add "stra_handL stra"
        add "n_closefromup_mouth sad_Silentx09" xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 ypos 0.11 zoom 0.62 at scrappdissolve

    elif key_mouse_:
        add "stra_handR stra"
        add "stra_handL rest"
        add "n_closefromup_mouth sad_Silentx10" xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 ypos 0.11 zoom 0.62 at scrappdissolve

    else:
        add "stra_handL rest"
        add "stra_handR rest"
        if stra_number > 900:
            add "n_closefromup_mouth sad_Talkingx08" xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 ypos 0.11 zoom 0.62 at scrappdissolve
        elif stra_number > 700:
            add "n_closefromup_mouth sad_Talkingx05" xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 ypos 0.11 zoom 0.62 at scrappdissolve
        elif stra_number > 550:
            add "n_closefromup_mouth sad_Talkingx03" xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 ypos 0.11 zoom 0.62 at scrappdissolve
        else:
            add "n_closefromup_mouth sadbiting_Silentx03" xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 ypos 0.11 zoom 0.62 at scrappdissolve

        # if stra_number > 550:
        #     add "breath_new_toRightFast" alpha str_vapor xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 ypos 0.28 zoom 1.0  at scrappdissolve

        if stra_number > 950:
            add "breath_new_toRightFast" xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 ypos 0.28 zoom 1.0 alpha 1.0 at scrappdissolve
        elif stra_number > 850:
            add "breath_new_toRightFast" xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 ypos 0.28 zoom 1.0 alpha 0.8 at scrappdissolve
        elif stra_number > 750:
            add "breath_new_toRightFast" xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 ypos 0.28 zoom 1.0 alpha 0.6 at scrappdissolve
        elif stra_number > 650:
            add "breath_new_toRightFast" xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 ypos 0.28 zoom 1.0 alpha 0.4 at scrappdissolve
        elif stra_number > 550:
            add "breath_new_toRightFast" xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 ypos 0.28 zoom 1.0 alpha 0.2 at scrappdissolve

    # vbox:
    #     text "[stra_number]"
    #     if key_space_ and key_mouse_:
    #         text "AMBOOOOOSSSSS!!!!"
    #     elif key_space_:
    #         text "ESPACIOOOO!!!!!"

    #     elif key_mouse_:
    #         text "RATOOOOONNNNN!!!!!"
    #     else:
    #         text "Ninguno"
            

    timer 0.1 repeat True:

        if (stra_number > 0) and (stra_number < 1000):

            if (renpy.variant("pc") and key_space_ and key_mouse_) or (not renpy.variant("pc") and key_mouse_):
            #if key_space_ and key_mouse_:
                action SetVariable("stra_number", stra_number + 4)
            elif not (key_space_ or key_mouse_):
                action SetVariable("stra_number", stra_number - 1)
            else:
                action NullAction()
            #if stra_number == 500:
                #action SetVariable("str_adviceDad", str_adviceDad - 2)
            ##
            if stra_number == 450 and str_adviceDad == 0:
                action SetVariable("stra_number", stra_number - 1), SetVariable("str_adviceDad", str_adviceDad + 1), Return()
            elif stra_number == 250 and str_adviceDad == 1:
                action SetVariable("stra_number", stra_number - 1), SetVariable("str_adviceDad", str_adviceDad + 1), Return()
            elif stra_number == 100 and str_adviceDad == 2:
                action SetVariable("stra_number", stra_number - 1), SetVariable("str_adviceDad", str_adviceDad + 1), Return()
            elif stra_number == 10 and str_adviceDad == 3:
                action SetVariable("stra_number", stra_number - 1), SetVariable("str_adviceDad", str_adviceDad + 1), Return()

            ##

            if stra_number == 400 and str_talkNeus == 0:
                action SetVariable("stra_number", stra_number - 1), SetVariable("str_talkNeus", str_talkNeus + 1), Return()
            elif stra_number == 370 and str_talkNeus == 1:
                action SetVariable("stra_number", stra_number - 1), SetVariable("str_talkNeus", str_talkNeus + 1), Return()
            elif stra_number == 320 and str_talkNeus == 2:
                action SetVariable("stra_number", stra_number - 1), SetVariable("str_talkNeus", str_talkNeus + 1), Return()
            elif stra_number == 150 and str_talkNeus == 3:
                action SetVariable("stra_number", stra_number - 1), SetVariable("str_talkNeus", str_talkNeus + 1), Return()
            elif stra_number == 50 and str_talkNeus == 4:
                action SetVariable("stra_number", stra_number - 1), SetVariable("str_talkNeus", str_talkNeus + 1), Return()

        else:
            action Return()

screen stra_neus_transpa():
    zorder -1
    $ str_transpa = (stra_number - 500) / 500.0
    if str_transpa > 0:
        #add "#f00" alpha str_transpa
        add "border_bloddy01" alpha str_transpa xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 zoom 0.5
        add "border_bloddy02" alpha str_transpa xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 zoom 0.5
        add "border_darkness_reddish" alpha str_transpa xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 zoom 0.5

    if str_transpa < 0:
        add "#000" alpha -str_transpa
        add "morning04_bedroom_DMast_blinkeye" alpha -str_transpa


######################################################################
######################################################################
####################
######################################################################
######################################################################

######################################################################
######################################################################
####################
######################################################################
######################################################################