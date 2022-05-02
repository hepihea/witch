default ac_p = ""
default ac_d = ""

# Are you submisive or active?
# How many orgasms?
# how many splashes on the ass?

init python:

    import renpy.store as ren_store

    class afterMorning05_Body():
        def __init__(self, ide, name):
            self.ide = ide
            self.name = name

            # $ af5_p.active = "af5_d"

            self.pos = "oral"
            self.action = "rest"
            self.b_action = "rest"

            self._test = "motherFuckerTest"

            self.orgasms = 0

            # self.submission = 0 # Needed?
            # self.love = 0 # Needed?

            self.happiness = 0
            self.pleasure = 0

            self.arousal = 1 # Decided on pleasure and max pleasure.

            # Dilatation
            self.dilThroat = 0 # Dilatation Throat
            self.dilAnal = 0 # Dilatation Ass
            self.dilVaginal = 0 # Dilatation Vagina #Not necessary for him, but fuck!
            # Pain Power
            self.painThroat = 0 # How much in Pain Throat
            self.painAnal = 0 # How much pain do you have for anal Sex.
            self.painVaginal = 0 # Vaginal Pain.
            self.painDick = 0

            # Still not sure about these ones:

            self.pain_dict = {} # Dictionary. How many times # Body, Throat, anal, buttocks, vaginal, dick ...
            # self.painThroat_received = 0 # Times
            # self.painAnal_received = 0
            # self.painVaginal_received = 0
            
            # self.painDick_received = 0
            # self.buttocks_pain_received = 0 # Painful
            # self.buttockSlaps_well_received = 0 # Not Painful
            # self.body_pain_received = 0 # rest of the body

            ####
            
            self.assSmacks = 0
            self.takeDickOutTimes = 0 # Times you took your dick Off from her.

            self.orgasmScene = False # To call Orgasm Scene

            self.closeOrgasmTotal = 0
            self.closeOrgasm = 0
            self.max_pleasure = {
                0: 50, #bar 00 
                1: 75, # bar 01 --59
                2: 100, #bar 02 --        This is in theory the last one.
                3: 125, # bar 03 --
                4: 150, # bar 04 --118 Divide it for 6
                5: 175,
                6: 200,
                7: 225,
                8: 250,
                9: 300,
                10: 400,
                11: 500,
                12: 1000
            }   

        def check_closeOrgasmTotal(self):
            # if self.pleasure > 100:
            #     self.pleasure = 100
            if self.orgasms > 0:
                if self.pleasure > self.max_pleasure[self.orgasms] * self.orgasms:
                    self.pleasure = self.max_pleasure[self.orgasms] * self.orgasms
            else:
                if self.pleasure > self.max_pleasure[self.orgasms]:
                    self.pleasure = self.max_pleasure[self.orgasms]

            self.closeOrgasmTotal = int(self.closeOrgasm + (self.pleasure*0.1))

            if self.pleasure > ((self.max_pleasure[self.orgasms]//3)*2):
                self.arousal = 3
            elif self.pleasure < (self.max_pleasure[self.orgasms]//3):
                self.arousal = 2
            elif self.pleasure < 0:
                self.arousal = 1
            else:
                self.arousal = 0

        def closeOrgasMax(self):
            # Orgasm
            if self.closeOrgasmTotal > self.max_pleasure[self.orgasms]:
                print("{} had an orgasm!". format(self.name))

                self.orgasmScene = True

                #self.active = ""
                self.orgasms += 1

                if self.orgasms > 5:
                    self.pleasure = 10
                elif self.orgasms > 4:
                    self.pleasure = 15
                elif self.orgasms > 3:
                    self.pleasure = 20
                elif self.orgasms > 2:
                    self.pleasure = 25
                elif self.orgasms > 1:
                    self.pleasure = 30
                elif self.orgasms > 0:
                    self.pleasure = 35

                if self.pleasure < 0:
                    self.pleasure = 0

                self.closeOrgasm = 0
                self.closeOrgasmTotal = 0

        def checkSex(self):

            if self.ide in ["af5_p", "m6_p"]:

                if ac_p.action not in ["masturbate", "blowjob_received", "blowjobDeep_received", "vaginal_done", "vaginalDeep_done", "anal_done", "analDeep_done"]:

                    # if (
                    #         (self.orgasms == 0 and self.closeOrgasm > 20) or
                    #         (self.orgasms == 1 and self.closeOrgasm > 30) or
                    #         (self.orgasms == 2 and self.closeOrgasm > 40)
                    #         ):
                    if self.closeOrgasmTotal > (self.max_pleasure[self.orgasms]//3):
                        self.closeOrgasm -= 3
                        if self.pleasure > 3:
                            self.pleasure -= 3
                    else:
                        self.closeOrgasm -= 1
                        if self.pleasure > 3:
                            self.pleasure -= 2

            if self.ide in ["af5_d", "m6_d"]:

                if ac_p.action not in ["vaginal_done", "vaginalDeep_done", "anal_done", "analDeep_done", "cunnilngus_done", "anilingus_done", "analFingered_done", "vaginalFingered_done"]:

                    if self.closeOrgasmTotal > (self.max_pleasure[self.orgasms]//3):
                        self.closeOrgasm -= 2
                        if self.pleasure > 3:
                            self.pleasure -= 3
                        self.happiness -= 2
                    else:
                        self.closeOrgasm -= 1
                        if self.pleasure > 3:
                            self.pleasure -= 2
                        self.happiness -= 5

            # if self.id == "p_prot":
            #     if p_prot.action not in ["masturbate", "blowjob_received", "blowjobDeep_received", "vaginal_done", "vaginalDeep_done", "anal_done", "analDeep_done"]:

            # Receive finger in asshole.

            if self.b_action == "anal_fingered_received":
                self.closeOrgasm += 1
                self.pleasure += 2
                self.happiness -= 1

            if self.action == "masturbate":
                self.closeOrgasm += 8
                self.pleasure += 5

            # TITWANK

            if self.action == "titwank_received":
                self.closeOrgasm += 7
                self.pleasure += 8

            if self.action == "titwank_done":
                self.closeOrgasm -= 1
                self.pleasure += 1
                self.happiness -= 1

            if self.b_action == "kiss_received":
                #self.closeOrgasm += 2
                self.pleasure += 4
                #self.happiness -= 1

            if self.b_action == "kiss_done":
                #self.closeOrgasm += 1
                self.pleasure += 2

            # CUNNILINGUS

            if self.action == "cunnilingus_received" or self.b_action == "cunnilingus_received":
                self.closeOrgasm += 7
                self.pleasure += 8
                self.dilVaginal += 1
                self.painVaginal -= 1
                self.happiness -= 1

            if self.action == "cunnilingus_done":
                #self.closeOrgasm += 1
                self.pleasure += 1

            # ANILINGUS

            if self.action == "anilingus_received" or self.b_action == "anilingus_received":
                self.closeOrgasm += 7
                self.pleasure += 8
                self.dilAnal += 1
                self.painAnal -= 1
                self.happiness -= 2


            if self.action == "anilingus_done":
                #self.closeOrgasm += 1
                self.pleasure += 1

            # BLOWJOB

            if self.action == "blowjob_done":
                if self.painThroat > 0:
                    #debug("Painful Deepthroat")
                    self.pleasure -= 3
                    self.happiness -= 3
                else:
                    #self.closeOrgasm += 2
                    self.pleasure += 3
                    self.happiness -= 1

            if self.action == "blowjob_received" or self.b_action == "blowjob_received":
                if self.painDick > 0:
                    debug("Receiving a PAINFUL blowjob")
                    self.closeOrgasm += 3
                    self.pleasure += 6
                else:
                    self.closeOrgasm += 10 # 10
                    self.pleasure += 12

            # DEEPTHROAT

            if self.action == "blowjobDeep_done":

                if self.painThroat > 0:
                    #self.closeOrgasm -= 4
                    self.pleasure -= 2
                    self.happiness -= 6

                else:
                    #self.closeOrgasm += 3
                    self.pleasure += 5
                    self.happiness -= 1

            if self.action == "blowjobDeep_received" or self.b_action == "blowjobDeep_received":

                if self.painDick > 0:
                    self.closeOrgasm += 6
                    self.pleasure += 8
                else:
                    self.closeOrgasm += 14 #18
                    self.pleasure += 16

            # VAGINAL

            if self.action == "vaginal_done":

                if self.painDick > 0:
                    self.closeOrgasm += 2
                    self.pleasure += 3
                else:
                    self.closeOrgasm += 5 # 10
                    self.pleasure += 6

            if self.action == "vaginal_received" or self.b_action == "vaginal_received":

                if self.painVaginal > 0:
                    self.closeOrgasm += 2
                    self.pleasure += 3
                    self.happiness += 1
                else:
                    self.closeOrgasm += 6 # 15
                    self.pleasure += 7
                    self.happiness += 3

            # VAGINAL_DEEP

            if self.action == "vaginalDeep_done":

                if self.painDick > 0:
                    self.closeOrgasm += 3
                    self.pleasure += 6
                else:
                    self.closeOrgasm += 6 # 15
                    self.pleasure += 7

            if self.action == "vaginalDeep_received" or self.b_action == "vaginalDeep_received":

                if self.painVaginal > 0:
                    self.closeOrgasm -= 1 # +5
                    self.pleasure += 1

                else:
                    self.closeOrgasm += 7 # 18
                    self.pleasure += 6
                    self.happiness += 2

            if self.ide in ["af5_d", "m6_d"]:
                if ac_p.b_action == "buttocks_slap_done":
                    if p_d.painButtocks > 10:
                        self.closeOrgasm -= 3
                        self.pleasure -= 4
                        self.happiness -= 4
                    else:
                        self.closeOrgasm += 1
                        self.happiness -= 1

            # ANAL

            if self.action == "anal_done":
                if self.painDick > 0:
                    self.closeOrgasm += 3
                    self.pleasure += 4
                else:
                    self.closeOrgasm += 6 # 12
                    self.pleasure += 7

            if self.action == "anal_received" or self.b_action == "anal_received":

                if self.painAnal > 0:
                    self.closeOrgasm -= 1
                    self.pleasure += 1
                    self.happiness -= 5
                else:
                    self.closeOrgasm += 3 # 8
                    self.pleasure += 5
                    self.happiness -= 2

            # ANAL_DEEP

            if self.action == "analDeep_done":

                if self.painDick > 0:
                    self.closeOrgasm += 3 # +5
                    self.pleasure += 4

                else:
                    self.closeOrgasm += 7 # 18
                    self.pleasure += 8
                    

            if self.action == "analDeep_received" or self.b_action == "analDeep_received":

                if self.painAnal > 0:
                    self.closeOrgasm -= 3 # +5
                    self.pleasure += 4
                    self.happiness -= 10
                else:
                    self.closeOrgasm += 5 # 12
                    self.pleasure += 7
                    self.happiness -= 2


        def checkPain(self):

            # NOT_FINISHED

            # Can you suck his dick?

            if self.painThroat > 0:
                self.painThroat -= 1
            if self.painAnal > 0:
                self.painAnal -= 1
            if self.painVaginal > 0:
                self.painVaginal -= 1

            if self.ide in ["af5_d", "m6_d"]:

                if self.dilThroat < 1 and self.painThroat < 1:
                    self.dilThroat += 1
                if self.dilAnal < 1 and self.painAnal < 1:
                    self.dilAnal += 1
                if self.dilVaginal < 1 and self.painVaginal < 1:
                    self.dilVaginal += 1

            if self.pleasure < 1:
                self.pleasure += 1
                

        def afFunc(self):

            self.checkSex()
            self.closeOrgasMax()
            self.check_closeOrgasmTotal()
            self.checkPain()

    class afterMorning05_F(afterMorning05_Body):
        def __init__(self, ide, name):
            #super().__init__()
            super(afterMorning05_F, self).__init__(ide, name)
            self.boobsSmacks = 0
            self.assSmacks = 0
            self.faceSlap = 0 # Slaps she received.
            self.faceSlapGiven = 0 # Slaps she did on your face.
            self._cumReceived = {} # 1: mouth, throat, belly, ground, bed, etc...
            
            self._position = [] #List to know in which position you're now and before
            self._positions = {} # 1: Missionary, Vagina Against wall, doggystyle on bed ## Last is the actual position.
            self._sexAction = [] # List to know what you're doing and what you did before.
            self._sexActions = {} # vaginal: 2, anal: 3 # ETC

        def cumReception(self, loc):
            if loc not in self._cumReceived:
                self._cumReceived[loc] = 1
            else:
                self._cumReceived[loc] += 1

        def changePos(self, pos):
            if pos not in self._positions:
                self._positions[pos] = 1
            else:
                self._positions[pos] += 1
            self._position.append(pos)

        def changeSexAction(self, act):
            if act not in self._sexActions:
                self._sexActions[act] = 1
            else:
                self._sexActions[act] += 1
            self._sexAction.append(act)

        


# ## TEST 
#         @property
#         def test(self):
#             print("Eyooouuuh!")
#             return self._test

#         @test.setter
#         def test(self, object):
#             print("Bitch, you're")
#             #self._test = object


# ## CUM RECEIVED: Mouth, Throat, belly, ground, etc...
#         @property
#         def cumReceived(self):
#             return self._cumReceived

#         @cumReceived.setter
#         def cumReceived(self, place):
#             if _cumReceived not in self._cumReceived:
#                 self._cumReceived[place] += 1
#             else:
#                 self._cumReceived[place] = 1

#         ## Example: m_d.cumReceved("mouth") # If you cum in her mouth.

# ## POSITIONS: Doggystyle, Missionary, Against Wall, etc...
#         @property
#         def positions(self):
#             return self._positions

#         @property
#         def position(self):
#             return self._position

#         @positions.setter
#         def position(self, pos):
#             if pos not in self._positions:
#                 self._positions[pos] = 1
#             else:
#                 self._positions[pos] += 1

#             self.position.append(pos)

#         ## Example: m_d.position("doggystyleBed") #Adds 1 in the dictionary and at the end of list.

# # SEX ACTIONS: Vaginal, Anal, Blowjob, Deepthroat, ...
#         @property
#         def sexActions(self):
#             print("Boutch")
#             return self._sexActions

#         @property
#         def sexAction(self):
#             print("Bitch")
#             return self._sexAction # It's a list, not the dictionary.

#         @sexAction.setter
#         def sexAction(self, action):
#             print("Hello fucking world", action)
#             # if action not in self._sexActions:
#             #     self._sexActions[action] = 1
#             # else:
#             #     self._sexActions[action] += 1

#             # self._sexAction.append(action)

#         ## Example: m_d.sexAction("blowjob") #Adds 1 in the dictionary and at the end of the list.


    class afterMorning05_M(afterMorning05_Body):
        def __init__(self, ide, name):
            #super().__init__()
            super(afterMorning05_M, self).__init__(ide, name)
            self.ballsSmacks = 0
            self.condom = False

            self.restTurns = 0

################################################################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
################################################################################

label ac_sex_defining: #For AfterMorning 05 and for Morning 06 with Didac.

    # NOT_FINISHED, SHOW screen of points top left screen.

    hide screen Points
    show screen PointsDidacSex()

    $ ac_p = ""
    $ ac_d = ""

    if pdaytime == "05_afternoon":
        $ af5_p = afterMorning05_M("af5_p", protname)
        $ af5_d = afterMorning05_F("af5_d", _("Dídac"))

        $ af5_p.active = "af5_d"

        $ ac_p = af5_p
        $ ac_d = af5_d

        $ af5_p.pleasure = 10
        $ af5_p.closeOrgasm = 30
        $ af5_p.dilThroat = -1
        $ af5_p.dilAnal = -1
        $ af5_p.painAnal= 0


        $ af5_d.pleasure = 10
        $ af5_d.closeOrgasm = 40

        ## Dilatation Throat
        if afternight04__MMouth_dick_Deep_Success > 2:
            $ af5_d.dilThroat = 60
        elif afternight04__MMouth_dick_Deep_Success > 1:
            $ af5_d.dilThroat = 50
        elif afternight04__MMouth_dick_Deep_Success > 0:
            $ af5_d.dilThroat = 40
        elif afternight04__MMouth_dick_Success > 2:
            $ af5_d.dilThroat = 30
        elif afternight04__MMouth_dick_Success > 1:
            $ af5_d.dilThroat = 20
        elif afternight04__MMouth_dick_Success > 0:
            $ af5_d.dilThroat = 10
        else:
            $ af5_d.dilThroat = -1


        if afternight04_Anal_dick_deep_Speed_2_Success > 2:
            $ af5_d.dilAnal = 60
        elif afternight04_Anal_dick_deep_Speed_2_Success > 1:
            $ af5_d.dilAnal = 50
        elif afternight04_Anal_dick_deep_Speed_2_Success > 0:
            $ af5_d.dilAnal = 40
        elif afternight04_Anal_dick_deep_Speed_1_Success > 2:
            $ af5_d.dilAnal = 30
        elif afternight04_Anal_dick_deep_Speed_1_Success > 1:
            $ af5_d.dilAnal = 20
        elif afternight04_Anal_dick_deep_Speed_1_Success > 0:
            $ af5_d.dilAnal = 10
        elif afternight04_Anal_dick_med_Speed_2_Success > 0:
            $ af5_d.dilAnal = 5
        elif afternight04_Anal_dick_med_Speed_1_Success > 0:
            $ af5_d.dilAnal = 2


        $ af5_d.happiness = pl.dp - dundiff #50


    if pdaytime == "06_morning":
        $ m6_p = afterMorning05_M("m6_p", protname)
        $ m6_d = afterMorning05_F("m6_d", _("Dídac"))

        $ ac_p = m6_p
        $ ac_d = m6_d

        $ m6_p.active = "m6_d"
    
    return


label ac_sex_aft:

    # $ af5_d.changePos("knees")
    # $ af5_d.changeSexAction("blowjob")
    # $ af5_d.cumReception("mouth")

    $ ac_d.afFunc()
    $ ac_p.afFunc()
    
    if ac_d.orgasmScene:
        call ac_sex__ac_d_orgasm_
    elif ac_p.orgasmScene:
        call ac_sex__ac_p_orgasm_
    

    if ac_p.pos != "her" and ac_d.happiness < 0:
        progcheck "Didac Changes position because she's angry."

        call ac_sex_changeposNull

        if ac_p.restTurns > 2:
            $ ac_p.restTurns -= 1 # RESTART the repetition of doing nothing.

        $ ac_p.pos = "her"

    return


################################################################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
################################################################################


#screen PointsDungeon():
screen PointsDidacSex():

    #default tt = Tooltip("No button selected.")

    if PlatinumHelp == True:

        zorder 99

        default hideDPoints = "<"
        
        #if Tendolarsversion == True:
        key "p" action ToggleScreenVariable('hideDPoints', True, False)
        
        #if Tendolarsversion == True:
        hbox:
            xalign 0.0
            yalign 0.055

            if hideDPoints == "<":
                frame:
                    background  "#000a"
                    hbox:

                        # dilAnal

                        imagebutton:
                            if ac_p.dilAnal < 0:
                                idle 'gui/icons/dungeon/dun_dilanal_mc_01.png'
                            else:
                                if ac_p.dilAnal < 60:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_02.png'
                                elif ac_p.dilAnal < 70:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_03.png'
                                elif ac_p.dilAnal < 80:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_04.png'
                                elif ac_p.dilAnal < 90:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_05.png'
                                elif ac_p.dilAnal < 100:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_06.png'
                                elif ac_p.dilAnal < 110:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_07.png'
                                elif ac_p.dilAnal < 120:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_08.png'
                                elif ac_p.dilAnal < 135:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_09.png'
                                else:
                                    idle 'gui/icons/dungeon/dun_dilanal_mc_10.png'

                            hover "gui/icons/dungeon/dun_dilanal_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Tu dilatación anal: {}".format(ac_p.dilAnal), style="dungeon_tooltip")

                        if ac_p.dilAnal < 0:
                            bar:
                                style "dungeon_bars_neg"
                                value ac_p.dilAnal + dundiff
                                range 150
                        else:
                            bar:
                                style "dungeon_bars"
                                value ac_p.dilAnal + dundiff
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_dilanal.png"
                                range 150
                        text "{size=15} {/size}"

                        # PAINANAL

                        imagebutton:
                            if ac_p.painAnal< 0:
                                idle 'gui/icons/dungeon./dun_painanal_neg_mc.png'
                            else:
                                idle 'gui/icons/dungeon./dun_painanal_pos_mc.png'
                            hover "gui/icons/dungeon./dun_painanal_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Dolor en tu agujero anal: {}".format(ac_p.painAnal), style="dungeon_tooltip")

                        if ac_p.painAnal< 0:
                            bar:
                                style "dungeon_bars_neg"
                                value ac_p.painAnal+ dundiff
                                range 150
                        else:
                            bar:
                                style "dungeon_bars"
                                value ac_p.painAnal+ dundiff
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_painanal.png"
                                range 150
                        text "{size=15} {/size}"

                        # DILTHROAT

                        imagebutton:
                            if ac_p.dilThroat < 0:
                                idle 'gui/icons/dungeon/dun_dilthroat_neg_mc.png'
                            else:
                                idle 'gui/icons/dungeon/dun_dilthroat_pos_mc.png'
                            hover "gui/icons/dungeon/dun_dilthroat_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Tu \"gag reflex\": {}".format(ac_p.dilThroat), style="dungeon_tooltip")

                        if ac_p.dilThroat < 0:
                            bar:
                                style "dungeon_bars_neg"
                                value ac_p.dilThroat + dundiff
                                range 150
                        else:
                            bar:
                                style "dungeon_bars"
                                value ac_p.dilThroat + dundiff
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_dilthroat.png"
                                range 150
                        text "{size=15} {/size}"

                        # PLEASURE

                        imagebutton:
                            if ac_p.pleasure < 0:
                                idle 'gui/icons/dungeon/dun_ple_neg_mc.png'
                            else:
                                idle 'gui/icons/dungeon/dun_ple_pos_mc.png'
                            hover "gui/icons/dungeon/dun_ple_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Tu placer: {}".format(ac_p.pleasure), style="dungeon_tooltip")

                        if ac_p.pleasure < 0:
                            bar:
                                style "dungeon_bars_neg"
                                right_bar "gui/slider/horizontal_idle_bar_dungeon_ple.png"
                                value ac_p.pleasure #+ dundiff
                                range 150
                                #range ac_p.max_pleasure[ac_p.orgasms]
                        else:
                            bar:
                                style "dungeon_bars"
                                value ac_p.pleasure #+ dundiff
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_ple.png"
                                right_bar "gui/slider/horizontal_idle_bar_dungeon_ple.png"
                                #range 150
                                if ac_p.orgasms > 0:
                                    range ac_p.max_pleasure[ac_p.orgasms] * ac_p.orgasms #- dundiff
                                else:
                                    range ac_p.max_pleasure[ac_p.orgasms]
                        text "{size=15} {/size}"

                        # STIMULATION

                        imagebutton:
                            idle 'gui/icons/dungeon/dun_sti_pos_mc.png'
                            hover "gui/icons/dungeon/dun_sti_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Proximidad al orgasmo: {}".format(ac_p.closeOrgasmTotal), style="dungeon_tooltip")
                        bar:
                            style "dungeon_bars"
                            value ac_p.closeOrgasmTotal
                            right_bar "gui/slider/horizontal_idle_bar_dungeon_empty.png"
                            left_bar "gui/slider/horizontal_hover_bar_dungeon_sti.png"
                            range ac_p.max_pleasure[ac_p.orgasms]
                            #range 150

                        text "{size=15} {/size}"

                        # ORGASM

                        imagebutton:
                            idle 'gui/icons/dungeon/dun_org_pos_mc.png'
                            hover "gui/icons/dungeon/dun_org_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Orgasmos: {}".format(ac_p.orgasms), style="dungeon_tooltip")

                        text "{size=15}{size=15}{color=#966} [ac_p.orgasms]{/color}{/size}"

                        

        hbox:
            xalign 0.0
            yalign 0.0

            if hideDPoints == "<":
                frame:
                    background  "#000a"
                    hbox:

                        # new DILATATION ASSHOLE

                        imagebutton:
                            if ac_d.dilAnal < 0:
                                idle 'gui/icons/dungeon/dun_dilanal_hi_01.png'
                            else:
                                if ac_d.dilAnal < 60:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_02.png'
                                elif ac_d.dilAnal < 70:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_03.png'
                                elif ac_d.dilAnal < 80:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_04.png'
                                elif ac_d.dilAnal < 90:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_05.png'
                                elif ac_d.dilAnal < 100:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_06.png'
                                elif ac_d.dilAnal < 110:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_07.png'
                                elif ac_d.dilAnal < 120:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_08.png'
                                elif ac_d.dilAnal < 135:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_09.png'
                                else:
                                    idle 'gui/icons/dungeon/dun_dilanal_hi_10.png'

                            hover "gui/icons/dungeon/dun_dilanal_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Dilatación Anal: {}".format(ac_d.dilAnal), style="dungeon_tooltip")

                        if ac_d.dilAnal < 0:
                            bar:
                                style "dungeon_bars_neg"
                                value ac_d.dilAnal + dundiff
                                range 150
                        else:

                            bar:
                                style "dungeon_bars"
                                value ac_d.dilAnal + dundiff
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_dilanal.png"
                                range 150
                        text "{size=15} {/size}"

                        # PAIN ASSHOLE

                        imagebutton:
                            if ac_d.painAnal< 0:
                                idle 'gui/icons/dungeon./dun_painanal_neg_hi.png'
                            else:
                                idle 'gui/icons/dungeon./dun_painanal_pos_hi.png'
                            hover "gui/icons/dungeon./dun_painanal_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Dolor anal: {}".format(ac_d.painAnal), style="dungeon_tooltip")

                        if ac_d.painAnal< 0:
                            bar:
                                style "dungeon_bars_neg"
                                value ac_d.painAnal+ dundiff
                                range 150
                        else:
                            bar:
                                style "dungeon_bars"
                                value ac_d.painAnal+ dundiff
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_painanal.png"
                                range 150
                        text "{size=15} {/size}"

                        # DILATATION THROAT

                        imagebutton:
                            if ac_d.dilThroat < 0:
                                idle 'gui/icons/dungeon/dun_dilthroat_neg_hi.png'
                            else:
                                idle 'gui/icons/dungeon/dun_dilthroat_pos_hi.png'
                            hover "gui/icons/dungeon/dun_dilthroat_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Gag Reflex: {}".format(ac_d.dilThroat), style="dungeon_tooltip")

                        if ac_d.dilThroat < 0:
                            bar:
                                style "dungeon_bars_neg"
                                value ac_d.dilThroat + dundiff
                                range 150
                        else:
                            bar:
                                style "dungeon_bars"
                                value ac_d.dilThroat + dundiff
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_dilthroat.png"
                                range 150
                        text "{size=15} {/size}"

                        # # DOMINATION

                        # imagebutton:
                        #     if ac_d.submission < 0:
                        #         idle 'gui/icons/dungeon/dun_dom_neg_hi.png'
                        #     else:
                        #         idle 'gui/icons/dungeon/dun_dom_pos_hi.png'
                        #     hover "gui/icons/dungeon/dun_dom_hover_def.png" 
                        #     action NullAction() align (.5, .5)
                        #     hover_foreground Text("Dominación: {}".format(ac_d.submission - dundiff), style="dungeon_tooltip")

                        # #text "{size=10} {/size}"

                        # if ac_d.submission < 0:
                        #     bar:
                        #         style "dungeon_bars_neg"
                        #         value ac_d.submission + dundiff
                        #         range 150
                        # else:
                        #     bar:
                        #         style "dungeon_bars"
                        #         value ac_d.submission + dundiff
                        #         left_bar "gui/slider/horizontal_hover_bar_dungeon_dom.png"
                        #         range 150
                        # text "{size=15} {/size}"
                        
                        # # LOVE

                        # imagebutton:
                        #     if ac_d.love < 0:
                        #         idle 'gui/icons/heart_neg_hi.png'
                        #     else:
                        #         idle 'gui/icons/heart_hi.png'
                        #     hover "gui/icons/heart_hover_def.png" 
                        #     action NullAction() align (.5, .5)
                        #     hover_foreground Text("Adoración: {}".format(ac_d.love), style="dungeon_tooltip")


                        # if ac_d.love < 0:
                        #     bar:
                        #         style "dungeon_bars_neg"
                        #         value ac_d.love + dundiff
                        #         range 150
                        # else:
                        #     bar:
                        #         style "dungeon_bars"
                        #         value ac_d.love + dundiff
                        #         left_bar "gui/slider/horizontal_hover_bar_dungeon_love.png"
                        #         range 150
                        # text "{size=15} {/size}"

                        
                        # PLEASURE
                        imagebutton:
                            if ac_d.pleasure < 0:
                                idle 'gui/icons/dungeon/dun_ple_neg_hi.png'
                            else:
                                idle 'gui/icons/dungeon/dun_ple_pos_hi.png'
                            hover "gui/icons/dungeon/dun_ple_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Dolor/Placer: {}".format(ac_d.pleasure), style="dungeon_tooltip")

                        if ac_d.pleasure < 0:
                            bar:
                                style "dungeon_bars_neg"
                                right_bar "gui/slider/horizontal_idle_bar_dungeon_ple.png"
                                value ac_d.pleasure + dundiff
                                range 150
                        else:
                            bar:
                                style "dungeon_bars"
                                value ac_d.pleasure + dundiff
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_ple.png"
                                right_bar "gui/slider/horizontal_idle_bar_dungeon_ple.png"
                                range 150
                        text "{size=15} {/size}"
                        
                        # new STIMULATION to orgasm.

                        imagebutton:
                            if ac_d.closeOrgasmTotal < (0):
                                idle 'gui/icons/dungeon/dun_sti_pos_hi.png'
                            else:
                                idle 'gui/icons/dungeon/dun_sti_pos_hi.png'
                            hover "gui/icons/dungeon/dun_sti_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Proximidad al orgasmo: {}".format(ac_d.closeOrgasmTotal), style="dungeon_tooltip")
                        bar:
                            style "dungeon_bars"
                            value ac_d.closeOrgasmTotal
                            left_bar "gui/slider/horizontal_hover_bar_dungeon_sti.png"
                            right_bar "gui/slider/horizontal_idle_bar_dungeon_empty.png"
                            range ac_d.max_pleasure[ac_d.orgasms]
                            #range 150

                        text "{size=15} {/size}"

                        ## ORGASMS

                        imagebutton:
                            idle 'gui/icons/dungeon/dun_org_pos_hi.png'
                            hover "gui/icons/dungeon/dun_org_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Orgasmos: {}".format(ac_d.orgasms), style="dungeon_tooltip")

                        text "{size=15}{size=15}{color=#966} [ac_d.orgasms]{/color}{/size}"

                        text "{size=15} {/size}" ## Separator

                        # HAPPINESS

                        imagebutton:
                            if ac_d.happiness < 0:
                                idle 'gui/icons/dungeon/dun_hap_neg_hi.png'
                            else:
                                idle 'gui/icons/dungeon/dun_hap_pos_hi.png'
                            hover "gui/icons/dungeon/dun_hap_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text("Enfado/Felicidad: {}".format(ac_d.happiness), style="dungeon_tooltip")

                        if ac_d.happiness < 0:
                            bar:
                                style "dungeon_bars_neg"
                                value ac_d.happiness + dundiff
                                range 150
                        else:
                            bar:
                                style "dungeon_bars"
                                value ac_d.happiness + dundiff
                                left_bar "gui/slider/horizontal_hover_bar_dungeon_hap.png"
                                range 150
                        text "{size=15} {/size}"

            textbutton (_(hideDPoints)) text_color hideDPoints_color():
                action ToggleScreenVariable('hideDPoints', "<", ">")

            # textbutton _(hidePoints) text_color hidePoints_color():
            #     action ToggleScreenVariable('hidePoints', "<", ">")


        # hbox:
        #     xalign 1.0
        #     yalign 0.0

        #     #if hide == "<":
        #     frame:
        #         background  "#000a"
        #         hbox:

        #             # TIME

        #             #imagebutton:
        #                 #idle 'gui/icons/dungeon/clock_base.png'
        #                 #hover "gui/icons/dungeon/clock_right.png" 
        #                 #action NullAction() align (.5, .5)
        #                 #hover_foreground Text("Time: {}".format(pLockerC.hi_time), style="dungeon_tooltip")

        #             #text "{size=15}{size=15}{color=#966} [pLockerC.hi_org]{/color}{/size}"
        #         #vbox align .5, .5:
        #             fixed fit_first True:
        #                 #add "gui/icons/dungeon/clock_base.png"
        #                 imagebutton:
        #                     idle 'gui/icons/dungeon/clock_base.png'
        #                     hover "gui/icons/dungeon/clock_right.png" 
        #                     action NullAction() align (.5, .5)
        #                     hover_foreground Text("Time passed: {} minutes".format(int(pLockerC.hi_time / 3)), style="dungeon_tooltip_time")
        #                 if pLockerC.hi_time <=180:
        #                     add AlphaBlend(Transform("gui/icons/dungeon/clock_mask.png", align = (.5, .5), rotate=pLockerC.hi_time), "gui/icons/dungeon/clock_right.png" , Solid("#0000"), alpha=True)
        #                 else:
        #                     add AlphaBlend(Transform("gui/icons/dungeon/clock_mask.png", align = (.5, .5), rotate=pLockerC.hi_time), "gui/icons/dungeon/clock_full.png" , Solid("#0000"), alpha=True)
        #                     add "gui/icons/dungeon/clock_right.png"
                            
                    #bar value ScreenVariableValue("pLockerC.hi_time", 360) xsize 100

#define dun_time_angle =  int(pLockerC.hi_time / 3)
      
#python:
    #def dun_time_angle():
        #return 10 * 5 # Degrees / 30 = Hours in half day. \\ Degrees / 6 = Minutes in an hour. \\ Degrees / 3 = Minutes in 2 hours (120 minutes)



################################################################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
################################################################################
########################################
################################################################################
################################################################################
################################################################################

label ac_sex_action_label:

    menu ac_sex_action_choice(screen="dun_choice_screen"):

        "<Seguir sin hacer nada>" if ac_p.action == "rest" and ac_p.b_action == "rest":
            call p_Help

            $ ac_p_sameAction = True

        "<Seguir igual>" if ac_p.action != "rest" or ac_p.b_action != "rest": # This one can be problematic.
            call p_Help

            $ ac_p_sameAction = True

        "<Masturbarte>" if ac_p.pos == "oral" and ac_p.action in ["rest", "takeDickOut"]:
            call p_Help

            $ ac_p.action = "masturbate"

        "<Dejar de masturbarte>" if ac_p.pos == "oral" and ac_p.action in ["masturbate"]:
            call p_Help

            $ ac_p.action = "rest"

        "<Pedirle una cubana>" if ac_p.pos == "oral" and ac_p.action == "rest":
            call p_Help

            $ ac_p.action = "titwank_received_TRY"

        "<Besarla>" if (ac_p.pos == "missionary") and (ac_p.action not in ["cunnilingus_done", "anilingus_done"]):
            call p_Help

            $ ac_p.b_action = "kiss_TRY"

        "<Metérsela en la garganta>" if ((ac_p.pos == "oral" and ac_p.action == "blowjob_received")
            or (ac_p.pos == "69" and ac_p.b_action == "blowjob_received")): 
        #Does it work in 69 pose?
            call p_Help

            if ac_p.action == "blowjob_received":
                $ ac_p.action = "blowjobDeep_received_TRY"
            if ac_p.b_action == "blowjob_received":
                $ ac_p.b_action = "blowjobDeep_received_TRY"

        "<Metérsela más adentro>" if ac_p.pos != "her" and ac_p.action in ["vaginal_done", "anal_done"]:
            call p_Help

            if ac_p.action == "vaginal_done":
                $ ac_p.action = "vaginalDeep_done_TRY"

            ##

            if ac_p.action == "anal_done":
                $ ac_p.action = "analDeep_done_TRY"

        "<Metérsela en la boca>" if (ac_p.pos in "oral" and ac_p.action not in ["blowjob_received", "blowjobDeep_received"]) or (ac_p.pos in "69" and ac_p.b_action not in ["blowjob_received", "blowjobDeep_received"]):
            call p_Help

            if ac_p.pos == "oral":
                $ ac_p.action = "blowjob_received_TRY"

            elif ac_p.pos == "69":
                $ ac_p.b_action = "blowjob_received_TRY"

        "<Sexo vaginal>" if (ac_p.pos in ["missionary", "doggy", "wall"]) and (ac_p.action not in ["vaginal_done", "vaginalDeep_done"]):
            call p_Help

            #call afternight05_Pedrera_Sex_actionNull # What does it do?
            call ac_sex_actionNull

            $ ac_p.action = "vaginal_done_TRY"

        "<Sexo Anal>" if (ac_p.pos in ["missionary", "doggy", "wall"]) and ac_p.action not in ["anal_done", "analDeep_done"]:
            call p_Help

            call ac_sex_actionNull

            $ ac_p.action = "anal_done_TRY"

        "<Azotarle las nalgas>" if ac_p.pos == "doggy" and ac_p.action not in ["cunnilingus_done", "anilingus_done"]:

            call p_Help

            # if p_active == "p_didac":
            #     $ p_didac.buttocks_pain += 3
            #     if p_didac.buttocks_pain < 6:
            #         $ p_didac.pleasure += 2
            #     else:
            #         $ p_didac.pleasure -= 2

            $ ac_p.b_action = "buttocks_slap_done"

        "<Elegir otra postura>":
            call p_Help

            call ac_sex_changeposNull #What does it does?

            if ac_p.restTurns > 2:
                $ ac_p.restTurns -= 1 # RESTART the repetition of doing nothing.

            jump ac_sex_pose_label


    #call expression "ac_sex_" + ac_p.active + "_" + ac_p.pos
    call expression "ac_sex__" + ac_p.pos + "_"

    call ac_sex_aft

    jump ac_sex_action_label


########################################################


label ac_sex_actionNull:
    $ ac_p.action = "rest"
    $ ac_d.action = "rest"
    return

label ac_sex_changeposNull:
    # call ped_reduceRestTurns
    $ ac_p.action = "rest"
    $ ac_p.b_action = "rest"
    $ ac_d.action = "rest"
    $ ac_d.b_action = "rest"
    return  

#label am05_DSex_pose_label:
label ac_sex_pose_label:

    #aj "Aquí empezaría el juego."

    menu ac_sex_pose_choice(screen="dun_choice_screen"):

        pt "¿Qué postura elijo?"

        "Ponerla de rodillas":
            call p_Help
            $ ac_p.pos = "oral"

        "Ponerla abierta de piernas sobre la cama":
            call p_Help
            $ ac_p.pos = "missionary"

        "Ponerla a cuatro patas sobre la cama":
            call p_Help
            $ ac_p.pos = "doggystyle"

        "Hacer un 69 sobre la cama":
            call p_Help
            $ ac_p.pos = "69"

        "Ponerla contra la pared":
            call p_Help

            $ ac_p.pos = "wall"

        "Dejar que ella decida ella":
            call p_Help

            $ ac_p.pos = "her"

    $ ac_d.changePos(ac_p.pos)

    $ ac_p.action = "rest"
    $ ac_p.b_action = "rest"

    $ ac_d.action = "rest"
    $ ac_d.b_action = "rest"

    # $ p_prot.action = "rest"
    # $ p_didac.action = "rest"
    # $ p_txell.action = "rest"
    # $ p_neus.action = "rest"

    # scene black
    # with fade

    # call expression "afternight05_Pedrera_Sex_" + p_active + "_" + p_prot.pos
    # label afternight05_Pedrera_Sex_p_didac_oral:
    call expression "ac_sex__" + ac_p.pos + "_"

    call ac_sex_aft

    # call m6_DSex__After

    jump ac_sex_action_label


# label m6_DSex__After:

    # call m6_DSex_checkingOrgasm

    # call m6_DSex_af_numbers



# label m6_DSex_checkingOrgasm:

#     #call afternight05_Pedrera_Sex_Check_after_restNumbers
#     call m6_DSex_Check_after_restNumbers

#     $ m6_p.p_closeToOrgasm() # NOT_FINISHED
#     $ m6_d.p_closeToOrgasm()
#     return


label ac_sex_Check_after_restNumbers:
    
    # If you don't fuck Didac often, she will jump over you and dominate you.

    if afternight05_Pedrera_n_Neus_Warning_Cond == True:
        # Already done.
        $ afternight05_Pedrera_n_Neus_Warning_Cond = False

    else:
        if ac_p.action not in ["masturbate", "titwank_received", "vaginal_done", "vaginalDeep_done", "anal_done", "analDeep_done", "blowjob_received", "blowjobDeep_received"] and ac_p.b_action not in ["blowjob_received", "blowjobDeep_received"]:
            #progcheck "You're not receiving pleasure."
            if ac_p.action in ["cunnilingus_done", "anilingus_done"]:
                pass
                #progcheck "You're giving pleasure."

            $ ac_p.restTurns += 1
            $ ac_p += 1

            if ac_p.pos == "oral":
                $ ac_p.pos_oral_rest += 1

            elif ac_p.pos == "69":

                $ ac_p.pos_69_rest += 1

            elif ac_p.pos == "doggy":

                $ ac_p.pos_doggy_rest += 1

            elif ac_p.pos == "missionary":

                $ ac_p.pos_missionary_rest += 1

        else:

            #progcheck "You're receiving pleasure. p_prot.restTurns = [p_prot.restTurns]"

            if ac_p.restTurns > 1:
                $ ac_p.restTurns -= 2
            $ ac_p = 0

            #progcheck "You're receiving pleasure. p_prot.restTurns = [p_prot.restTurns]"

    #progcheck "Waiting02: p_prot.restTurns = [p_prot.restTurns]"

    return


###########################################################################
###########################################################################
####################################################################################################
###########################################################################
###########################################################################


label ac_sex_testTextAction:

    if ac_p.action == "rest" and ac_p.b_action == "rest":

        progcheck "pos: [ac_p.pos]// You're resting."

    else:

        progcheck "pos: [ac_p.pos]// A: [ac_p.action]/ B: [ac_p.b_action]/ "

    return


label ac_sex__oral_:

    call ac_sex_testTextAction

    if ac_p.action == "masturbate":

        $ ac_p.b_action = "rest"
        $ ac_d.action = "rest"
        $ ac_d.b_action = "rest"

        progcheck "Action: [ac_p.action]"

        d "¿Me estás tomando el pelo?"

## ORAL Blowjob
    elif ac_p.action in ["blowjob_received_TRY", "blowjob_received"]:

        if ac_p.action == "blowjob_received_TRY":
            progcheck "Asking for a blowjob."

            if ac_d.dilThroat > 0:

                if (
                    afternight04__MMouth_dick_Success > 0 and ac_d.arousal >= 1 and ac_d.happiness > 50 or
                    ac_d.arousal >= 3 and ac_d.happiness > 90
                    ):
                    $ ac_p.action = "blowjob_received"
                    $ ac_d.action = "blowjob_done"

                    if afternight04__MMouth_dick_Success > 0:

                        d "Bueno... si ya lo hice una vez..."

                    else:

                        d "Hmmm.. mira que eres pesado cuando quieres."
                else:

                    d "Ni de coña me meto eso en la boca."
            else:

                d "¡¿Es que no ves que me sigue doliendo la garganta por tu culpa?!"
        else:

            progcheck "Blowjob Again."

        if ac_p.action != "blowjob_done":
            $ ac_d.action = "rest"
            $ ac_d.action = "rest"

## ORAL Blowjob_Deep
    elif ac_p.action in ["blowjobDeep_received_TRY", "blowjobDeep_received"]:

        if ac_p.action == "blowjobDeep_received_TRY":
            progcheck "Asking for a Deepthroat."

            if ac_d.pleasure > 0 and ac_d.dilThroat > 75:

                if (
                    afternight04__MMouth_dick_Deep_Success > 0 and ac_d.arousal >= 1 and ac_d.happiness > 50 or
                    ac_d.arousal >= 3 and ac_d.happiness > 90
                    ):
                    $ ac_p.action = "blowjobDeep_received"
                    $ ac_d.action = "blowjobDeep_done"

                    if afternight04__MMouth_dick_Deep_Success > 0:

                        d "¡Ghmmm!..."

                    else:

                        d "Hmmm.."

                else:

                    d "¡Nig de goña!"
            else:

                # Need to put different levels of dilThroat. To know how close you're to get in.

                $ ac_d.pleasure -= 3
                $ ac_d.dilThroat -= 5

                $ ac_p.action = "rest"
                $ ac_d.action = "rest"

                d "¡Cough! ¡cough!"

                d "¡Que no me cabe joder!"
        else:

            progcheck "Deepthroat Again."

## ORAL Titwank   
    elif ac_p.action in ["titwank_received_TRY", "titwank_received"]:
        
        if ac_p.action == "titwank_received_TRY":
            progcheck "Asking for a titwank."

            $ ac_p.action = "titwank_received"
            $ ac_d.action = "titwank_done"

        else:

            progcheck "Titwank Again."


    return

label ac_sex__69_:

    call ac_sex_testTextAction

    return

label ac_sex__doggystyle_:

    call ac_sex_testTextAction

    return

label ac_sex__missionary_:

    if ac_p.b_action in ["kiss_TRY", "kiss_done"]:

        if ac_p.b_action == "kiss_TRY":

            progcheck "Asking for a Kiss."

            if (
                (
                    afternight04__MMouth_Tongue_Success > 0 and 
                ac_d.arousal >= 1 and 
                ac_d.happiness > 30
                ) or
                ( ac_d.arousal >=3 and
                    ac_d.happiness > 90
                    )
                ):

                $ ac_p.b_action = "kiss_done"
                $ ac_d.b_action = "kiss_received"

                progcheck "You're kissing her."

            else:
                progcheck "She doesn't want to kiss you."
                $ ac_p.b_action = "rest"
                $ ac_d.b_action = "rest"

        elif ac_p.b_action == "kiss_done":

            progcheck "You keep kissing her."

    call ac_sex_testTextAction

    return

label ac_sex__wall_:

    call ac_sex_testTextAction

    return

label ac_sex__her_:

    progcheck "She basically fucks you."

    $ ac_p.action = "vaginal_done"
    $ ac_d.action ="vaginal_received"
    $ ac_p.b_action = "rest"
    $ ac_d.b_action = "rest"

    return

label ac_sex__ac_d_orgasm_:

    if ac_d.arousal == 3:
        progcheck "She's having a super Orgasm"
    elif ac_d.arousal == 2:
        progcheck "She's having a normal Orgasm"
    elif ac_d.arousal == 1:
        progcheck "She's having a mediocre Orgasm"
    elif ac_d.arousal == 0:
        progcheck "She's having a terrible Orgasm"
    else:
        progcheck "ERROR 299"

    $ ac_d.orgasmScene = False

    return

label ac_sex__ac_p_orgasm_:

    if ac_p.arousal == 3:
        progcheck "He's having a super Orgasm"
    elif ac_p.arousal == 2:
        progcheck "He's having a normal Orgasm"
    elif ac_p.arousal == 1:
        progcheck "He's having a mediocre Orgasm"
    elif ac_p.arousal == 0:
        progcheck "He's having a terrible Orgasm"
    else:
        progcheck "ERROR 298"

    $ ac_p.orgasmScene = False

    if ac_p.orgasms >= 3:
        progcheck "YOu had your 3 orgasms."


        hide screen PointsDidacSex
        show screen Points()
        scene black
        with fade

        window hide dissolve
        pause

        if pdaytime == "05_afternoon":

            jump night05_DidacHome
                # ono "RIIIING"
                # p "Hmmm..."
                # n "Oyes el particular sonido de llamada de tu móvil."
                # pt "¿Qué hora es?"
                # n "Antes de que seas capaz de reaccionar"
                # n "Dídac se levanta a toda prisa dirigiéndose al suelo"
                # n "dónde -escondido entre tus pantalones- está tu celular."
                # d "Neus..."
                # d "¿Es este el nombre de la bruja?"

        elif pdaytime == "06_morning":

            jump morning06_Df_afterSex
                # ono "Riiiiiing"
                # P "Uhhmm..."
                # d "¿Aún estás en la cama?"
                # n "Ves a Dídac de pie con una toalla"
                # n "y con el pelo mojado"
                # n "como si se hubiera terminado de duchar."
                # p "¿Cómo es que tienes tanta energía?"

        elif pdaytime == "06_night_DidacMale":

            call WIP

            jump gameover

        else:

            aj "Minigame should end ERROR 49886"

    return