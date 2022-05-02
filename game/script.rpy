
#Tutorial Lemma Forum Several sound effects same time.
init -1 python hide:
    
    renpy.music.register_channel("sfx1", "sfx")
    renpy.music.register_channel("sfx2", "sfx")
    renpy.music.register_channel("sfx3", "sfx")
    renpy.music.register_channel("sfx4", "sfx")
    renpy.music.register_channel("sfx5", "sfx")
    renpy.music.register_channel("sfx6", "sfx")

## Prove Of hotkeys

define centered = Character("BLOCK", what_style="centered_text", window_style="centered_window")

init python:
     config.overlay_screens.append("my_scr")

screen my_scr:
    if PlatinumHelp == True:
        key "K_F5" action QuickSave()
        key "K_F6" action QuickLoad()
        key "c" action If(renpy.get_screen("cheat_system"), true=Hide("cheat_system"), false=Show("cheat_system"))
        
    key "i" action If(renpy.get_screen("history"), true=Hide("history"), false=Show("history"))
    #key "i" action ShowMenu("history")
    key "m" action Preference("all mute", "toggle")

##This disable the rollback if it´s "False".
#$ config.rollback_enabled = True

## Define Default Dissolve
        
define dissolve = Dissolve(.18)

define dissolve_05s = Dissolve(0.5)

define dissolve_1s = Dissolve(1.0)

define fade_long305s = Fade(1.0, 0.5, 2.0)
define fade_long1s = Fade(0.5, 0.5, 1.0)
define fade_short = Fade(0.2, 0.2, 0.3)


define flash_short = Fade(0.2, 0.2, 0.3, color = "#fff")
define flash_long1s = Fade(0.5, 0.5, 1.0, color="#fff")
define flash_long305s = Fade(1.0, 0.5, 2.0, color="#fff")

transform screendissolve:
    on show:
        alpha 0.0
        easein_quad 0.5 alpha 1.0
    on hide:
        alpha 1.0
        easein_quad 0.5 alpha 0.0

transform scrappdissolve:
    alpha 0.0
    linear 1.0 alpha 1.0

# Example:
#screen loquesea():
    #frame at screendissolve:


        ## Position of the renpy.notify.

style points_jonny:
    size 40

        ###

init python:
    def hidePoints_color():

        if Tendolarsversion == True: #True=10$Patrons .
            return "#fa0"
        elif Platinumversion == True: # True =1$, 3$ nad 5$.
            return "#9ab"
        else:
            return "#757"

init python:
    def hideDPoints_color():

        if Tendolarsversion == True: #True=10$Patrons .
            return "#fa0"
        elif Platinumversion == True: # True =1$, 3$ nad 5$.
            return "#9ab"
        else:
            return "#757"

screen Points():

    #if (PlatinumHelp) == True:

    zorder 100

    default hidePoints = "<"

    #if PlatinumHelp == False:
        #$ hidePoints = ">"
    
    if PlatinumHelp == True:
        key "p" action ToggleScreenVariable('hidePoints', True, False)
        #key "p" action ToggleScreenVariable('hidePoints', "<", ">")


        hbox:
            xalign 0.0
            yalign 0.0

            if hidePoints == "<":
                frame:
                    background  "#000a"
                    # hbox:
                    #     text "{image=gui/icons/heart_n.png}{size=15}{color=#969}: [pl.np]{/size}{/color}"
                    #     text "{image=gui/icons/heart_d.png}{size=15}{color=#c63}: [pl.dp]{/size}{/color}"
                    #     text "{image=gui/icons/heart_m.png}{size=15}{color=#a93}: [pl.mp]{/size}{/color}" #Hide Meritxell top left.
                    hbox:
                        text "{image=heartSmallN}"
                        text "{size=5} {/size}"
                        text "{color=#969}{size=15}[pl.np]{/size}{/color}"
                        text "{size=15} {/size}"
                        text "{image=heartSmallD}"
                        text "{size=5} {/size}"
                        text "{color=#c63}{size=15}[pl.dp]{/size}{/color}"
                        text "{size=15} {/size}"
                        text "{image=heartSmallM}"
                        text "{size=5} {/size}"
                        text "{color=#a93}{size=15}[pl.mp]{/size}{/color}" #Hide Meritxell top left.
            textbutton _(hidePoints) text_color hidePoints_color():
                action ToggleScreenVariable('hidePoints', "<", ">")

    #style.default.outlines = [(2, "#000a", 1, 1)] #I try to make semi-transparent the P


##################

define hh = "{image=gui/icons/heart_hi.png}" #Hiromi Heart

#define dun_hap_hi = "{image=gui/icons/dungeon/dun_hap_hi.png}" #Hiromi Happiness
#define dun_ang_hi = "{image=gui/icons/dungeon/dun_ang_hi.png}" #Hiromi Angryness
#define dun_dom_hi = "{image=gui/icons/dungeon/dun_dom_hi.png}" #Hiromi Domination
#define dun_org_hi = "{image=gui/icons/dungeon/dun_org_hi.png}" #Hiromi Orgasm
#define dun_ple_hi = "{image=gui/icons/dungeon/dun_ple_hi.png}" #Hiromi Pleasure

##################

#image dun_dilass_hi_general = "gui/icons/dungeon/dun_dilanal_hi_01.png"

#image dun_dilass_hi_general02 = (

    #if pLockerC.hi_dilass < 10: "gui/icons/dungeon/dun_dilanal_hi_01.png"
    #elif pLockerC.hi_dilass < 20: "gui/icons/dungeon/dun_dilanal_hi_02.png"

    #)

#init python:
    #def adjust_score(delta):
         ##global pLockerC.hi_dilass
         #global dun_dilass_hi_number
         #pLockerC.hi_dilass += delta

         #if pLockerC.hi_dilass < 10:
               #dun_dilass_hi_number = 0
         #elif pLockerC.hi_dilass < 20:
               #dun_dilass_hi_number = 1
         #else:
               #dun_dilass_hi_number = 2

#init python:
    #def dun_dilass_hi_number():

        #if pLockerC.hi_dilass in range (0, 15):
            #return "01"
        #elif pLockerC.hi_dilass in range (16, 25):
            #return "02"
        #else:
            #return "03"

####

style dungeon_bars:
    right_bar "gui/slider/horizontal_idle_bar_dungeon.png"
    left_bar "gui/slider/horizontal_hover_bar_dungeon.png"
    #thumb "gui/slider/horizontal_hover_thumb.png"
    #thumb_offset 15
    xysize (30, 10)
    xalign 0.5
    yalign 0.5

style dungeon_bars_neg:
    right_bar "gui/slider/horizontal_idle_bar_dungeon.png"
    left_bar "gui/slider/horizontal_hover_bar_neg_dungeon.png"
    #thumb "gui/slider/horizontal_hover_thumb.png"
    #thumb_offset 15
    xysize (30, 10)
    xalign 0.5
    yalign 0.5

define dundiff = 50

style dungeon_tooltip:
    ypos 1.0
    color "#fff"
    size 15
    font "fonts/chinrg__.ttf"
    #xmaximum 1000
    layout "nobreak"
    hover_background  "#000a"

style dungeon_tooltip_time:
    ypos 1.0
    color "#fff"
    size 15
    font "fonts/chinrg__.ttf"
    #xmaximum 1000
    layout "nobreak"
    hover_background  "#000a"
    #xanchor -3.0
    xpos -4.0

screen PointsDungeon():

    #default tt = Tooltip("No button selected.")

    if PlatinumHelp == True:

        zorder 99

        default hideDPoints = "<"
        
        #if Tendolarsversion == True:
        key "p" action ToggleScreenVariable('hideDPoints', True, False)
        
        #if Tendolarsversion == True:
        hbox:
            xalign 0.0
            yalign 0.05

            if hideDPoints == "<":
                frame:
                    background  "#000a"
                    hbox:

                        # PLEASURE

                        imagebutton:
                            if pLockerC.mc_ple < (0 + dundiff):
                                idle 'gui/icons/dungeon/dun_ple_neg_mc.png'
                            else:
                                idle 'gui/icons/dungeon/dun_ple_pos_mc.png'
                            hover "gui/icons/dungeon/dun_ple_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Tu placer: {}".format(pLockerC.mc_ple - dundiff), style="dungeon_tooltip")

                        if pLockerC.mc_ple < (0 + dundiff):
                            bar:
                                style "dungeon_bars_neg"
                                right_bar "gui/slider/horizontal_idle_bar_dungeon_ple.png"
                                value pLockerC.mc_ple
                                range 150
                        else:
                            bar:
                                style "dungeon_bars"
                                value pLockerC.mc_ple
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_ple.png"
                                right_bar "gui/slider/horizontal_idle_bar_dungeon_ple.png"
                                range 150
                        text "{size=15} {/size}"

                        # DILASS

                        imagebutton:
                            if pLockerC.mc_dilass < (0 + dundiff):
                                idle 'gui/icons/dungeon/dun_dilanal_mc_01.png'
                            else:
                                if pLockerC.mc_dilass < 60:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_02.png'
                                elif pLockerC.mc_dilass < 70:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_03.png'
                                elif pLockerC.mc_dilass < 80:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_04.png'
                                elif pLockerC.mc_dilass < 90:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_05.png'
                                elif pLockerC.mc_dilass < 100:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_06.png'
                                elif pLockerC.mc_dilass < 110:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_07.png'
                                elif pLockerC.mc_dilass < 120:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_08.png'
                                elif pLockerC.mc_dilass < 135:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_09.png'
                                else:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_10.png'

                            hover "gui/icons/dungeon/dun_dilanal_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Tu dilatación anal: {}".format(pLockerC.hi_dilass - dundiff), style="dungeon_tooltip")

                        if pLockerC.mc_dilass < (0 + dundiff):
                            bar:
                                style "dungeon_bars_neg"
                                value pLockerC.mc_dilass
                                range 150
                        else:
                            bar:
                                style "dungeon_bars"
                                value pLockerC.mc_dilass
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_dilanal.png"
                                range 150
                        text "{size=15} {/size}"

                        # DILTHROAT

                        imagebutton:
                            if pLockerC.mc_dilthroat < (0 + dundiff):
                                idle 'gui/icons/dungeon/dun_dilthroat_neg_mc.png'
                            else:
                                idle 'gui/icons/dungeon/dun_dilthroat_pos_mc.png'
                            hover "gui/icons/dungeon/dun_dilthroat_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Tu \"gag reflex\": {}".format(pLockerC.mc_dilthroat - dundiff), style="dungeon_tooltip")

                        if pLockerC.mc_dilthroat < (0 + dundiff):
                            bar:
                                style "dungeon_bars_neg"
                                value pLockerC.mc_dilthroat
                                range 150
                        else:
                            bar:
                                style "dungeon_bars"
                                value pLockerC.mc_dilthroat
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_dilthroat.png"
                                range 150
                        text "{size=15} {/size}"

                        # PAINASS

                        imagebutton:
                            if pLockerC.mc_painass < (0 + dundiff):
                                idle 'gui/icons/dungeon./dun_painanal_neg_mc.png'
                            else:
                                idle 'gui/icons/dungeon./dun_painanal_pos_mc.png'
                            hover "gui/icons/dungeon./dun_painanal_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Dolor en tu agujero anal: {}".format(pLockerC.mc_painass - dundiff), style="dungeon_tooltip")

                        if pLockerC.mc_painass < (0 + dundiff):
                            bar:
                                style "dungeon_bars_neg"
                                value pLockerC.mc_painass
                                range 150
                        else:
                            bar:
                                style "dungeon_bars"
                                value pLockerC.mc_painass
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_painanal.png"
                                range 150
                        text "{size=15} {/size}"

                        # STIMULATION

                        imagebutton:
                            idle 'gui/icons/dungeon/dun_sti_pos_mc.png'
                            hover "gui/icons/dungeon/dun_sti_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Proximidad al orgasmo: {}".format(pLockerC.mc_sti), style="dungeon_tooltip")
                        bar:
                            style "dungeon_bars"
                            value pLockerC.mc_sti
                            right_bar "gui/slider/horizontal_idle_bar_dungeon_empty.png"
                            left_bar "gui/slider/horizontal_hover_bar_dungeon_sti.png"
                            range 150

                        text "{size=15} {/size}"

                        # ORGASM

                        imagebutton:
                            idle 'gui/icons/dungeon/dun_org_pos_mc.png'
                            hover "gui/icons/dungeon/dun_org_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Orgasmos: {}".format(pLockerC.mc_org), style="dungeon_tooltip")

                        text "{size=15}{size=15}{color=#966} [pLockerC.mc_org]{/color}{/size}"

                        

        hbox:
            xalign 0.0
            yalign 0.0

            if hideDPoints == "<":
                frame:
                    background  "#000a"
                    hbox:

                        # DOMINATION

                        imagebutton:
                            if pLockerC.hi_dom < (0 + dundiff):
                                idle 'gui/icons/dungeon/dun_dom_neg_hi.png'
                            else:
                                idle 'gui/icons/dungeon/dun_dom_pos_hi.png'
                            hover "gui/icons/dungeon/dun_dom_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Dominación: {}".format(pLockerC.hi_dom - dundiff), style="dungeon_tooltip")

                        #text "{size=10} {/size}"

                        if pLockerC.hi_dom < (0 + dundiff):
                            bar:
                                style "dungeon_bars_neg"
                                value pLockerC.hi_dom
                                range 150
                        else:
                            bar:
                                style "dungeon_bars"
                                value pLockerC.hi_dom
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_dom.png"
                                range 150
                        text "{size=15} {/size}"
                        
                        # PLEASURE
                        imagebutton:
                            if pLockerC.hi_ple < (0 + dundiff):
                                idle 'gui/icons/dungeon/dun_ple_neg_hi.png'
                            else:
                                idle 'gui/icons/dungeon/dun_ple_pos_hi.png'
                            hover "gui/icons/dungeon/dun_ple_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Dolor/Placer: {}".format(pLockerC.hi_ple - dundiff), style="dungeon_tooltip")

                        if pLockerC.hi_ple < (0 + dundiff):
                            bar:
                                style "dungeon_bars_neg"
                                right_bar "gui/slider/horizontal_idle_bar_dungeon_ple.png"
                                value pLockerC.hi_ple
                                range 150
                        else:
                            bar:
                                style "dungeon_bars"
                                value pLockerC.hi_ple
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_ple.png"
                                right_bar "gui/slider/horizontal_idle_bar_dungeon_ple.png"
                                range 150
                        text "{size=15} {/size}"
                        
                        # HAPPINESS

                        imagebutton:
                            if pLockerC.hi_hap < (0 + dundiff):
                                idle 'gui/icons/dungeon/dun_hap_neg_hi.png'
                            else:
                                idle 'gui/icons/dungeon/dun_hap_pos_hi.png'
                            hover "gui/icons/dungeon/dun_hap_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Enfado/Felicidad: {}".format(pLockerC.hi_hap - dundiff), style="dungeon_tooltip")

                        if pLockerC.hi_hap < (0 + dundiff):
                            bar:
                                style "dungeon_bars_neg"
                                value pLockerC.hi_hap
                                range 150
                        else:
                            bar:
                                style "dungeon_bars"
                                value pLockerC.hi_hap
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_hap.png"
                                range 150
                        text "{size=15} {/size}"
                        
                        
                        # LOVE

                        imagebutton:
                            if pLockerC.hi_love < (0 + dundiff):
                                idle 'gui/icons/heart_neg_hi.png'
                            else:
                                idle 'gui/icons/heart_hi.png'
                            hover "gui/icons/heart_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Adoración: {}".format(pLockerC.hi_love - dundiff), style="dungeon_tooltip")


                        if pLockerC.hi_love < (0 + dundiff):
                            bar:
                                style "dungeon_bars_neg"
                                value pLockerC.hi_love
                                range 150
                        else:
                            bar:
                                style "dungeon_bars"
                                value pLockerC.hi_love
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_love.png"
                                range 150
                        text "{size=15} {/size}"

                        # new DILATATION ASSHOLE

                        imagebutton:
                            if pLockerC.hi_dilass < (0 + dundiff):
                                idle 'gui/icons/dungeon/dun_dilanal_hi_01.png'
                            else:
                                if pLockerC.hi_dilass < 60:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_02.png'
                                elif pLockerC.hi_dilass < 70:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_03.png'
                                elif pLockerC.hi_dilass < 80:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_04.png'
                                elif pLockerC.hi_dilass < 90:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_05.png'
                                elif pLockerC.hi_dilass < 100:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_06.png'
                                elif pLockerC.hi_dilass < 110:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_07.png'
                                elif pLockerC.hi_dilass < 120:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_08.png'
                                elif pLockerC.hi_dilass < 135:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_09.png'
                                else:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_10.png'

                            hover "gui/icons/dungeon/dun_dilanal_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Dilatación Anal: {}".format(pLockerC.hi_dilass - dundiff), style="dungeon_tooltip")

                        if pLockerC.hi_dilass < (0 + dundiff):
                            bar:
                                style "dungeon_bars_neg"
                                value pLockerC.hi_dilass
                                range 150
                        else:

                            bar:
                                style "dungeon_bars"
                                value pLockerC.hi_dilass
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_dilanal.png"
                                range 150
                        text "{size=15} {/size}"

                        # DILATATION THROAT

                        imagebutton:
                            if pLockerC.hi_dilthroat < (0 + dundiff):
                                idle 'gui/icons/dungeon/dun_dilthroat_neg_hi.png'
                            else:
                                idle 'gui/icons/dungeon/dun_dilthroat_pos_hi.png'
                            hover "gui/icons/dungeon/dun_dilthroat_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Gag Reflex: {}".format(pLockerC.hi_dilthroat - dundiff), style="dungeon_tooltip")

                        if pLockerC.hi_dilthroat < (0 + dundiff):
                            bar:
                                style "dungeon_bars_neg"
                                value pLockerC.hi_dilthroat
                                range 150
                        else:
                            bar:
                                style "dungeon_bars"
                                value pLockerC.hi_dilthroat
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_dilthroat.png"
                                range 150
                        text "{size=15} {/size}"

                        
                        # PAIN ASSHOLE

                        imagebutton:
                            if pLockerC.hi_painass < (0 + dundiff):
                                idle 'gui/icons/dungeon./dun_painanal_neg_hi.png'
                            else:
                                idle 'gui/icons/dungeon./dun_painanal_pos_hi.png'
                            hover "gui/icons/dungeon./dun_painanal_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Dolor anal: {}".format(pLockerC.hi_painass - dundiff), style="dungeon_tooltip")

                        if pLockerC.hi_painass < (0 + dundiff):
                            bar:
                                style "dungeon_bars_neg"
                                value pLockerC.hi_painass
                                range 150
                        else:
                            bar:
                                style "dungeon_bars"
                                value pLockerC.hi_painass
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_painanal.png"
                                range 150
                        text "{size=15} {/size}"

                        
                        # new STIMULATION to orgasm.

                        imagebutton:
                            if pLockerC.hi_sti < (0):
                                idle 'gui/icons/dungeon/dun_sti_pos_hi.png'
                            else:
                                idle 'gui/icons/dungeon/dun_sti_pos_hi.png'
                            hover "gui/icons/dungeon/dun_sti_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Proximidad al orgasmo: {}".format(pLockerC.hi_sti), style="dungeon_tooltip")
                        bar:
                            style "dungeon_bars"
                            value pLockerC.hi_sti
                            left_bar "gui/slider/horizontal_hover_bar_dungeon_sti.png"
                            right_bar "gui/slider/horizontal_idle_bar_dungeon_empty.png"
                            range 150

                        text "{size=15} {/size}"

                        ## ORGASMS

                        imagebutton:
                            idle 'gui/icons/dungeon/dun_org_pos_hi.png'
                            hover "gui/icons/dungeon/dun_org_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Orgasmos: {}".format(pLockerC.hi_org), style="dungeon_tooltip")

                        text "{size=15}{size=15}{color=#966} [pLockerC.hi_org]{/color}{/size}"

            textbutton (_(hideDPoints)) text_color hideDPoints_color():
                action ToggleScreenVariable('hideDPoints', "<", ">")

            # textbutton _(hidePoints) text_color hidePoints_color():
            #     action ToggleScreenVariable('hidePoints', "<", ">")


        hbox:
            xalign 1.0
            yalign 0.0

            #if hide == "<":
            frame:
                background  "#000a"
                hbox:

                    # TIME

                    #imagebutton:
                        #idle 'gui/icons/dungeon/clock_base.png'
                        #hover "gui/icons/dungeon/clock_right.png" 
                        #action NullAction() align (.5, .5)
                        #hover_foreground Text("Time: {}".format(pLockerC.hi_time), style="dungeon_tooltip")

                    #text "{size=15}{size=15}{color=#966} [pLockerC.hi_org]{/color}{/size}"
                #vbox align .5, .5:
                    fixed fit_first True:
                        #add "gui/icons/dungeon/clock_base.png"
                        imagebutton:
                            idle 'gui/icons/dungeon/clock_base.png'
                            hover "gui/icons/dungeon/clock_right.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Time passed: {} minutes".format(int(pLockerC.hi_time / 3)), style="dungeon_tooltip_time")
                        if pLockerC.hi_time <=180:
                            add AlphaBlend(Transform("gui/icons/dungeon/clock_mask.png", align = (.5, .5), rotate=pLockerC.hi_time), "gui/icons/dungeon/clock_right.png" , Solid("#0000"), alpha=True)
                        else:
                            add AlphaBlend(Transform("gui/icons/dungeon/clock_mask.png", align = (.5, .5), rotate=pLockerC.hi_time), "gui/icons/dungeon/clock_full.png" , Solid("#0000"), alpha=True)
                            add "gui/icons/dungeon/clock_right.png"
                            
                    #bar value ScreenVariableValue("pLockerC.hi_time", 360) xsize 100

#define dun_time_angle =  int(pLockerC.hi_time / 3)
      
#python:
    #def dun_time_angle():
        #return 10 * 5 # Degrees / 30 = Hours in half day. \\ Degrees / 6 = Minutes in an hour. \\ Degrees / 3 = Minutes in 2 hours (120 minutes)

transform _notify_transform:
    # These control the position.
    yalign .1

    # These control the actions on show and hide.
    on show:
        alpha 0 xalign 1.1
        linear .5 alpha 1.0 xalign .9
    on hide:
        linear 2.0 alpha 0.0 xalign 1.1

    ## FORUM help.

default pl = PointLocker()
default plb = PointLocker_B() #If I delete this, Game Crashes because it´s not found. Fuck...
default pLockerC = PointLocker_C()

transform PointAnimation(loc):
    # These control the position.
    subpixel True
    xpos 1.1 
    ypos loc
    alpha 0

    # These control the actions on show and hide.
    on show:
        parallel:
            linear .25 alpha 1.0
        parallel:
            ease .5 xpos 0.80
    on hide:
        parallel:
            linear 2.0 alpha 0.0
        parallel:
            ease .0 xpos 0.80

screen Outer_dpScreen(message):
    use InnerScreen(message, 0.2)
    timer 3.0 action Hide("Outer_dpScreen")

screen Outer_npScreen(message):
    use InnerScreen(message, 0.3)
    timer 3.0 action Hide("Outer_npScreen")

screen Outer_mpScreen(message):
    use InnerScreen(message, 0.4)
    timer 3.0 action Hide("Outer_mpScreen")
    
screen InnerScreen(message, loc):
    if PlatinumHelp == True:
        text message at PointAnimation(loc)

init python:        
    class PointLocker(object):
        def __init__(self):
            self.dp = 0
            self.np = 0
            self.mp = 0
            
        def ch_pts(self, type, num):
            if num >= 0:
                start = "{color=#6c3}{size=30}+"
            else:
                start = "{color=#f33}{size=30}"
            end = "{/size}{/color}%s{image=images/menu/heart_icon.png}" % ("{color=#c63}{size=15}D{/size}{/color}" 
                if type == 'dp' else "{color=#969}{size=15}N{/size}{/color}" 
                if type == 'np' else "{color=#993}{size=15}M{/size}{/color}"
                if type == 'mp' else "{color=#993}{size=15}M{/size}{/color}") #Meritxell what?
            end = "{/size}{/color}%s" % ("{image=gui/icons/heart_d.png}" 
                if type == 'dp' else "{image=gui/icons/heart_n.png}" 
                if type == 'np' else "{image=gui/icons/heart_m.png}"
                if type == 'mp' else "{image=gui/icons/heart_m.png}")
            message = "%s %d %s" % (start, num, end)
            
            if type == "dp":
                self.dp += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "np":
                self.np += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "mp":
                self.mp += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message) #Hide this if you don´t want appear the message from Meritxell
    
        ##BlackBorder to name characters
    style.default.outlines = [(1, "#000c", 1, 1)]
    
        ##To avoid Bold in the label name of the characters.
    style.say_label.bold = True
    
        ## Trying to put modern Multi-language in the fucking game.

###############################
###############################
###############################  ## Hiromi and Txell Points

screen Outer_hi_domScreen(message):
    use InnerScreen(message, 0.1)
    timer 3.0 action Hide("Outer_hi_domScreen")

screen Outer_hi_pleScreen(message):
    use InnerScreen(message, 0.15)
    timer 3.0 action Hide("Outer_hi_pleScreen")

screen Outer_hi_hapScreen(message):
    use InnerScreen(message, 0.2)
    timer 3.0 action Hide("Outer_hi_hapScreen")

screen Outer_hi_loveScreen(message):
    use InnerScreen(message, 0.25)
    timer 3.0 action Hide("Outer_hi_loveScreen")

screen Outer_hi_dilassScreen(message):
    use InnerScreen(message, 0.3)
    timer 3.0 action Hide("Outer_hi_dilassScreen")

screen Outer_hi_dithroatScreen(message):
    use InnerScreen(message, 0.35)
    timer 3.0 action Hide("Outer_hi_dilthroatScreen")

screen Outer_hi_painassScreen(message):
    use InnerScreen(message, 0.4)
    timer 3.0 action Hide("Outer_hi_painassScreen")

screen Outer_hi_stiScreen(message):
    use InnerScreen(message, 0.45)
    timer 3.0 action Hide("Outer_hi_stiScreen")

screen Outer_hi_orgScreen(message):
    use InnerScreen(message, 0.5)
    timer 3.0 action Hide("Outer_hi_orgScreen")

init python:    
    
    class PointLocker_B(object): # This will have to be deleted, but so far it crashes OLD saved games.
        def __init__(self):
            # Hiromi
            self.hi_dom = 0
            self.hi_ple = 0
            self.hi_hap = 0
            self.hi_love = 0
            self.hi_sti = 0 # stimulation to have an orgasm.
            self.hi_org = 0


            # Txell
            self.tx_dom = 0
            self.tx_ple = 0
            self.tx_hap = 0
            self.tx_love = 0
            self.tx_sti = 0
            self.tx_org = 0

            
        def ch_pts_B(self, type, num):

            if num >= 0:
                start = "{color=#6c3}{size=30}+"
            else:
                start = "{color=#f33}{size=30}"

            end = "{/size}{/color}%s{image=images/menu/heart_icon.png}" % ("{color=#c63}{size=15}D{/size}{/color}")
            end = "{/size}{/color}%s" % ("{image=gui/icons/dungeon/dun_dom_hi.png}" #Dom if type == hi_dom (Weird way to See it... But DAMN PROGRAMMING! FUCK OFF!)
                if type == 'hi_dom' else "{image=gui/icons/dungeon/dun_ple_hi.png}" 
                if type == 'hi_ple' else "{image=gui/icons/dungeon/dun_sti_hi.png}"
                if type == 'hi_sti' else "{image=gui/icons/dungeon/dun_hap_hi.png}"
                if type == 'hi_hap' else "{image=gui/icons/dungeon./dun_painanal_hi.png}"
                if type == 'hi_painass' else "{image=gui/icons/dungeon/dun_dilanal_hi_01.png}"
                if type == 'hi_dilass' else "{image=gui/icons/dungeon/dun_dilthroat_hi.png}"
                if type == 'hi_dilthroat' else "{image=gui/icons/heart_hi.png}"
                if type == 'hi_love' else "{image=gui/icons/dungeon/dun_org_hi.png}"
                if type == 'hi_org' else "{image=gui/icons/dungeon/dun_org_hi.png}")
            message = "%s %d %s" % (start, num, end)
            
            if type == "hi_dom":
                self.hi_dom += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "hi_ple":
                self.hi_ple += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "hi_sti":
                self.hi_sti += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "hi_hap":
                self.hi_hap += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "hi_painass":
                self.hi_painass += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "hi_love":
                self.hi_love += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "hi_dilass":
                self.hi_dilass += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "hi_dilthroat":
                self.hi_dilthroat += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "hi_org":
                self.hi_org += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)

        ##BlackBorder to name characters
    style.default.outlines = [(1, "#000c", 1, 1)]
    
        ##To avoid Bold in the label name of the characters.
    style.say_label.bold = True
    
           
    class PointLocker_C(object):
        def __init__(self):
            # Hiromi
            self.hi_dom = 0
            self.hi_ple = 0
            self.hi_hap = 0
            self.hi_love = 0
            self.hi_sti = 0 # stimulation to have an orgasm.
            self.hi_org = 0

            self.hi_painass = 0
            self.hi_paindick = 0
            
            self.hi_dilass = 0 # Dilatation of the asshole.
            self.hi_dilthroat = 0 # Dilatation of the throat.

            self.hi_time = 0


            # Txell
            self.tx_dom = 0
            self.tx_ple = 0
            self.tx_hap = 0
            self.tx_love = 0
            self.tx_sti = 0
            self.tx_org = 0

            self.tx_painass = 0
            self.tx_painpussy = 0
            
            self.tx_dilass = 0
            self.tx_dilpussy = 0
            self.tx_dilthroat = 0 # Dilatation of the throat.

            self.tx_time = 0

            # MC
            self.mc_ple = 0
            self.mc_sti = 0
            self.mc_org = 0

            self.mc_painass = 0
            self.mc_paindick = 0

            self.mc_dilass = 0
            self.mc_dilthroat = 0

            self.mc_time = 0
            
        def ch_pts_C(self, type, num):

            if num >= 0:
                start = "{color=#6c3}{size=30}+"
            else:
                start = "{color=#f33}{size=30}"

            end = "{/size}{/color}%s{image=images/menu/heart_icon.png}" % ("{color=#c63}{size=15}D{/size}{/color}")
            end = "{/size}{/color}%s" % ("{image=gui/icons/dungeon/dun_dom_hi.png}" #Dom if type == hi_dom (Weird way to See it... But DAMN PROGRAMMING! FUCK OFF!)
                if type == 'hi_dom' else "{image=gui/icons/dungeon/dun_ple_hi.png}" 
                if type == 'hi_ple' else "{image=gui/icons/dungeon/dun_sti_hi.png}"
                if type == 'hi_sti' else "{image=gui/icons/dungeon/dun_hap_hi.png}"
                if type == 'hi_hap' else "{image=gui/icons/dungeon./dun_painanal_hi.png}"
                if type == 'hi_painass' else "{image=gui/icons/dungeon/dun_dilanal_hi_01.png}"
                if type == 'hi_dilass' else "{image=gui/icons/dungeon/dun_dilthroat_hi.png}"
                if type == 'hi_dilthroat' else "{image=gui/icons/heart_hi.png}"
                if type == 'hi_love' else "{image=gui/icons/dungeon/dun_org_hi.png}"
                if type == 'hi_org' else "{image=gui/icons/dungeon/dun_org_hi.png}")
            message = "%s %d %s" % (start, num, end)
            
            if type == "hi_dom":
                self.hi_dom += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "hi_ple":
                self.hi_ple += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "hi_sti":
                self.hi_sti += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "hi_hap":
                self.hi_hap += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "hi_painass":
                self.hi_painass += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "hi_love":
                self.hi_love += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "hi_dilass":
                self.hi_dilass += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "hi_dilthroat":
                self.hi_dilthroat += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)
            elif type == "hi_org":
                self.hi_org += num
                if PlatinumHelp == True:
                    renpy.show_screen("Outer_{}Screen".format(type), message)

###############################
###############################
###############################

init -3 python:
    if persistent.lang is None:
        persistent.lang = "Español (original)"

    lang = persistent.lang


label splashscreen:
    
    scene black
    
    #Booleans
    $ neus_glasses = True
        
    menu:
        "Español (original)":
            $renpy.change_language (None)
        "English":
            $renpy.change_language ("english")
            if PlatinumHelp == True:
                $ p_pos = (_("{color=#6b4}Positive Points Message{/color}"))
                $ p_neg = (_("{color=#e22}Negative Points Message{/color}"))
                $ p_negx2 = (_("{color=#e22}Negative Points Repetitive Message{/color}"))
            
    scene black
    call startmenudisclaimer
    scene startmenu splashscreen02 with dissolve
    pause 
    scene black with fade
    pause 0.1
    
    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True
            
            _preferences.volumes['music'] *= .40
            # You could also set 'sfx' and 'voice'.
            _preferences.volumes["sfx"] *= .60
            # You could also set 'sfx' and 'voice'.
            _preferences.volumes['voice'] *= .0
            # You could also set 'sfx' and 'voice'.
    
    return

label after_load:
    if not hasattr(store.mc_body, "first_dice_rolls"):
        $ store.mc_body.first_dice_rolls = []
        $ store.mc_body.second_dice_rolls = []
        $ store.mc_body.flashing_1 = 0.0
        $ store.mc_body.flashing_2 = 0.0

        $ store.girl_1.first_dice_rolls = []
        $ store.girl_1.second_dice_rolls = []
        $ store.girl_1.flashing = 0.0
        $ store.girl_1.did_a_roll = True


###############################
###############################
###############################


###############################
###############################
###############################



###############################
###############################
###############################

init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #

# ((OriginPoint, All 0 Means Center), Time, dist= Distance)

define sshake = Shake((0, 0, 0, 0), 0.25, dist=2)
define sshake02 = Shake((0, 0, 0, 0), 0.25, dist=4) 
define sshake03 = Shake((0, 0, 0, 0), 0.25, dist=8)

define sshake_soft = Shake((0, 0, 0, 0), 0.25, dist=5)


###############################
###############################
###############################

default ped_1_20_dictionary = {}
default ped_1_10_dictionary = {}
default ped_1_5_dictionary = {}

init python:
    def ped_check_1_20(ped_list):

        if ped_list not in ped_1_20_dictionary:
            ped_1_20_dictionary[ped_list] = list(range(1,21))

        global ped_check_list_result

        while True:
            randomnum_1to20 = renpy.random.randint(1, 20)

            if (1 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 1:
                ped_check_list_result = 1
                ped_1_20_dictionary[ped_list].remove(1)
                #ped_list.remove(1)
                #renpy.say(progcheck, "1")
                break

            elif (2 in ped_1_20_dictionary[ped_list])and randomnum_1to20 == 2:
                ped_check_list_result = 2
                ped_1_20_dictionary[ped_list].remove(2)
                break

            elif (3 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 3:
                ped_check_list_result = 3
                ped_1_20_dictionary[ped_list].remove(3)
                break

            elif (4 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 4:
                ped_check_list_result = 4
                ped_1_20_dictionary[ped_list].remove(4)
                break

            elif (5 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 5:
                ped_check_list_result = 5
                ped_1_20_dictionary[ped_list].remove(5)
                break

            elif (6 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 6:
                ped_check_list_result = 6
                ped_1_20_dictionary[ped_list].remove(6)
                break

            elif (7 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 7:
                ped_check_list_result = 7
                ped_1_20_dictionary[ped_list].remove(7)
                break

            elif (8 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 8:
                ped_check_list_result = 8
                ped_1_20_dictionary[ped_list].remove(8)
                break

            elif (9 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 9:
                ped_check_list_result = 9
                ped_1_20_dictionary[ped_list].remove(9)
                break

            elif (10 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 10:
                ped_check_list_result = 10
                ped_1_20_dictionary[ped_list].remove(10)
                break

            if (11 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 11:
                ped_check_list_result = 11
                ped_1_20_dictionary[ped_list].remove(11)
                break

            elif (12 in ped_1_20_dictionary[ped_list])and randomnum_1to20 == 12:
                ped_check_list_result = 12
                ped_1_20_dictionary[ped_list].remove(12)
                break

            elif (13 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 13:
                ped_check_list_result = 13
                ped_1_20_dictionary[ped_list].remove(13)
                break

            elif (14 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 14:
                ped_check_list_result = 14
                ped_1_20_dictionary[ped_list].remove(14)
                break

            elif (15 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 15:
                ped_check_list_result = 15
                ped_1_20_dictionary[ped_list].remove(15)
                break

            elif (16 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 16:
                ped_check_list_result = 16
                ped_1_20_dictionary[ped_list].remove(16)
                break

            elif (17 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 17:
                ped_check_list_result = 17
                ped_1_20_dictionary[ped_list].remove(17)
                break

            elif (18 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 18:
                ped_check_list_result = 18
                ped_1_20_dictionary[ped_list].remove(18)
                break

            elif (19 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 19:
                ped_check_list_result = 19
                ped_1_20_dictionary[ped_list].remove(19)
                break

            elif (20 in ped_1_20_dictionary[ped_list]) and randomnum_1to20 == 20:
                ped_check_list_result = 20
                ped_1_20_dictionary[ped_list].remove(20)
                break

            elif not ped_1_20_dictionary[ped_list]:
                ped_check_list_result = 123
                break

    # $ ped_times_1_5("test01")

    # if ped_check_list_result == 1:

    #     progcheck "First time."

    # elif ped_check_list_result == 2:

    #     progcheck "2 time."

    # elif ped_check_list_result == 3:

    #     progcheck "3 time."

    # elif ped_check_list_result == 4:

    #     progcheck "4 time."

    # elif ped_check_list_result == 5:

    #     progcheck "5 time."

    # else:

    #     progcheck "ELSE..."

init python:

    def ped_times_1_5(ped_list):

        if ped_list not in ped_1_5_dictionary:
            ped_1_5_dictionary[ped_list] = list(range(1,6))

            global ped_check_list_result

        while True:

            if (1 in ped_1_5_dictionary[ped_list]):
                ped_check_list_result = 1
                ped_1_5_dictionary[ped_list].remove(1)
                break

            elif (2 in ped_1_5_dictionary[ped_list]):
                ped_check_list_result = 2
                ped_1_5_dictionary[ped_list].remove(2)
                break

            elif (3 in ped_1_5_dictionary[ped_list]):
                ped_check_list_result = 3
                ped_1_5_dictionary[ped_list].remove(3)
                break

            elif (4 in ped_1_5_dictionary[ped_list]):
                ped_check_list_result = 4
                ped_1_5_dictionary[ped_list].remove(4)
                break

            elif (5 in ped_1_5_dictionary[ped_list]):
                ped_check_list_result = 5
                ped_1_5_dictionary[ped_list].remove(5)
                break

            else:
                ped_check_list_result = 123
                break

    def ped_times_1_10(ped_list):

        if ped_list not in ped_1_10_dictionary:
            ped_1_10_dictionary[ped_list] = list(range(1,6))

            global ped_check_list_result

        while True:

            if (1 in ped_1_10_dictionary[ped_list]):
                ped_check_list_result = 1
                ped_1_10_dictionary[ped_list].remove(1)
                break

            elif (2 in ped_1_10_dictionary[ped_list]):
                ped_check_list_result = 2
                ped_1_10_dictionary[ped_list].remove(2)
                break

            elif (3 in ped_1_10_dictionary[ped_list]):
                ped_check_list_result = 3
                ped_1_10_dictionary[ped_list].remove(3)
                break

            elif (4 in ped_1_10_dictionary[ped_list]):
                ped_check_list_result = 4
                ped_1_10_dictionary[ped_list].remove(4)
                break

            elif (5 in ped_1_10_dictionary[ped_list]):
                ped_check_list_result = 5
                ped_1_10_dictionary[ped_list].remove(5)
                break

            elif (6 in ped_1_10_dictionary[ped_list]):
                ped_check_list_result = 6
                ped_1_10_dictionary[ped_list].remove(6)
                break

            elif (7 in ped_1_10_dictionary[ped_list]):
                ped_check_list_result = 7
                ped_1_10_dictionary[ped_list].remove(7)
                break

            elif (8 in ped_1_10_dictionary[ped_list]):
                ped_check_list_result = 8
                ped_1_10_dictionary[ped_list].remove(8)
                break

            elif (9 in ped_1_10_dictionary[ped_list]):
                ped_check_list_result = 9
                ped_1_10_dictionary[ped_list].remove(9)
                break

            elif (10 in ped_1_10_dictionary[ped_list]):
                ped_check_list_result = 10
                ped_1_10_dictionary[ped_list].remove(10)
                break

            else:
                ped_check_list_result = 123
                break


    def ped_check_1_10(ped_list):

        if ped_list not in ped_1_10_dictionary:
            ped_1_10_dictionary[ped_list] = list(range(1,11))

        global ped_check_list_result

        while True:
            randomnum_1to10 = renpy.random.randint(1, 10)

            if (1 in ped_1_10_dictionary[ped_list]) and randomnum_1to10 == 1:
                ped_check_list_result = 1
                ped_1_10_dictionary[ped_list].remove(1)
                #ped_list.remove(1)
                #renpy.say(progcheck, "1")
                break

            elif (2 in ped_1_10_dictionary[ped_list])and randomnum_1to10 == 2:
                ped_check_list_result = 2
                ped_1_10_dictionary[ped_list].remove(2)
                break

            elif (3 in ped_1_10_dictionary[ped_list]) and randomnum_1to10 == 3:
                ped_check_list_result = 3
                ped_1_10_dictionary[ped_list].remove(3)
                break

            elif (4 in ped_1_10_dictionary[ped_list]) and randomnum_1to10 == 4:
                ped_check_list_result = 4
                ped_1_10_dictionary[ped_list].remove(4)
                break

            elif (5 in ped_1_10_dictionary[ped_list]) and randomnum_1to10 == 5:
                ped_check_list_result = 5
                ped_1_10_dictionary[ped_list].remove(5)
                break

            elif (6 in ped_1_10_dictionary[ped_list]) and randomnum_1to10 == 6:
                ped_check_list_result = 6
                ped_1_10_dictionary[ped_list].remove(6)
                break

            elif (7 in ped_1_10_dictionary[ped_list]) and randomnum_1to10 == 7:
                ped_check_list_result = 7
                ped_1_10_dictionary[ped_list].remove(7)
                break

            elif (8 in ped_1_10_dictionary[ped_list]) and randomnum_1to10 == 8:
                ped_check_list_result = 8
                ped_1_10_dictionary[ped_list].remove(8)
                break

            elif (9 in ped_1_10_dictionary[ped_list]) and randomnum_1to10 == 9:
                ped_check_list_result = 9
                ped_1_10_dictionary[ped_list].remove(9)
                break

            elif (10 in ped_1_10_dictionary[ped_list]) and randomnum_1to10 == 10:
                ped_check_list_result = 10
                ped_1_10_dictionary[ped_list].remove(10)
                break

            elif not ped_1_10_dictionary[ped_list]:
                ped_check_list_result = 123
                break

    def ped_check_1_5(ped_list):

        if ped_list not in ped_1_5_dictionary:
            ped_1_5_dictionary[ped_list] = list(range(1,6))

        global ped_check_list_result

        while True:
            randomnum_1to5 = renpy.random.randint(1, 5)

            if (1 in ped_1_5_dictionary[ped_list]) and randomnum_1to5 == 1:
                ped_check_list_result = 1
                ped_1_5_dictionary[ped_list].remove(1)
                #ped_list.remove(1)
                #renpy.say(progcheck, "1")
                break

            elif (2 in ped_1_5_dictionary[ped_list])and randomnum_1to5 == 2:
                ped_check_list_result = 2
                ped_1_5_dictionary[ped_list].remove(2)
                break

            elif (3 in ped_1_5_dictionary[ped_list]) and randomnum_1to5 == 3:
                ped_check_list_result = 3
                ped_1_5_dictionary[ped_list].remove(3)
                break

            elif (4 in ped_1_5_dictionary[ped_list]) and randomnum_1to5 == 4:
                ped_check_list_result = 4
                ped_1_5_dictionary[ped_list].remove(4)
                break

            elif (5 in ped_1_5_dictionary[ped_list]) and randomnum_1to5 == 5:
                ped_check_list_result = 5
                ped_1_5_dictionary[ped_list].remove(5)
                break

            elif not ped_1_5_dictionary[ped_list]:
                ped_check_list_result = 123
                break

        return



# NEYUNSE

# Para saber si el jugador está jugando la versión de 32 bits o la de 64 bits

# init python:
#     import platform
    
#     def get_Arch():
#         # mas info en https://docs.python.org/3/library/platform.html
#         arch = platform.architecture()
        
#         print(arch[0])
    
#     get_Arch() # >> 64bit / 32bit (no se si sale como 32 o 82 deberás comprobarlo)


# screen loquesea():
#       #...
#       if get_Arch() == "64bit":
#             #...
#       else:
#             #...

## Por si me interesa:

# init offset = -3
# define SO = None
# init python:
#     import platform
#     print platform.system()
#     if platform.system() == 'Windows':
#         SO = 'OSWIN'
#     elif platform.system() == 'Linux':
#         SO = 'OSLIN'
#     elif platform.system() == 'Darwin':
#         SO = 'OSDAR'
#     else:
#         SO = 'N/A'