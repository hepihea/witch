
default p_prot_NotJustMasturbate_with_p_didac = False
default p_prot_NotJustMasturbate_with_p_txell = False
default p_prot_NotJustMasturbate_with_p_any = False
default p_prot_NotJustMasturbate_with_p_both = False

default p_prot_NotJustMasturbate_with_p_neus = False

default afternight05_Pedrera_n_Neus_Warning_4Times_cunnilingusTxell = False
default afternight05_Pedrera_Neus_Warning_4Times_cunnilingusTxell = False

default afternight05_Pedrera_Sex_NeusLastWarning_Times = 0

default afternight05_Pedrera_Sex_NeusLastWarning_GrandMother = 0

default afternight05_Pedrera_Neus_Warning_tongue = 0
default afternight05_Pedrera_n_Neus_Warning_tongue = 0

default afternight05_Pedrera_hugNeus = False

default p_txell_NoSex_Confirmed = False

default p_prot_likesTwoWomenKissing = False

default p_didac_cunnilingus_p_txell_orgasm = 0

default p_dictCloseOrgasm = {}

default p_neus_orgasm_TRY = 0

default afternight05_Pedrera_n_Neus_Warning_Cond = False

default p_prot_restTemp = 0

default p_txell_orgasmByYou = 0

init python:

    class Pedrera_Body():

        def __init__(self):

            # self.closeKicks = 0
            # self.closeKicksTotal = self.closeKicks

            self.id = id

            self.start = 0 # To know if they started or not.

            self.action = "rest" # Wich Action is doing right now.
            self.b_action = "rest" # Wich 2nd action is doing right now.

            self.orgasm = 0 # How many orgasms did you had.
            self.closeOrgasm = 0 # How close is to Orgasm.
            self.orgasmScene = False # to call or not the Orgasm Scene.
            self.pleasure = 0 # How much pain or pleasure you're having, even if you're far from orgasm.
            self.enslavement = 0 # Not sure if I will need that.

            self.closeOrgasmTotal = 0

            # happiness
            # love

            ##

            # SEAL

            self.seal = "empty" # If the character had received your sperm and later Neus Kiss.
            self.cumReceived = "oral" # oral, vaginal, anal

            # POSITIONS

            self.pos = "rest"

            self.pos_oral = 0
            self.pos_doggy = 0
            self.pos_missionary = 0
            self.pos_69 = 0

            self.pos_oral_rest = 0
            self.pos_doggy_rest = 0
            self.pos_missionary_rest = 0
            self.pos_69_rest = 0

            self.restTurns = 0 # How many times you did nothing at all.
            self.angryTurns = 0

            #self.doingNothingTurns = 0

            ##

            # ACTIONS

            self.kiss_received = 0
            self.kiss_done = 0

            self.kiss_p_prot = 0
            self.kiss_p_didac = 0
            self.kiss_p_txell = 0
            self.kiss_p_neus = 0

            self.masturbate = 0

            self.titwank_done = 0
            self.titwank_done_TRY = 0
            self.titwank_done_FAILED = 0

            self.titwank_received = 0
            self.titwank_received_TRY = 0
            self.titwank_received_FAILED = 0

            self.blowjob_done = 0
            self.blowjob_done_TRY = 0
            self.blowjob_done_FAILED = 0

            self.blowjob_received = 0
            self.blowjob_received_TRY = 0
            self.blowjob_received_FAILED = 0

            self.blowjob_69_done = 0
            self.blowjob_69_received = 0

            self.blowjobDeep_done = 0
            self.blowjobDeep_received = 0
            self.blowjobDeep_received_TRY = 0 # Not sure if I will use this one.
            self.blowjobDeep_received_FAILED = 0
            self.blowjobDeep_received_FAILED_temp = 0

            self.blowjobDeep_69_done = 0
            self.blowjobDeep_69_received = 0

            #self.throat_pain_rejected = 0 # She rejected to suck your cock anymore.

            self.cunnilingus_done = 0
            self.cunnilingus_received = 0
            self.cunnilingus_received_TRY = 0
            self.cunnilingus_received_FAILED = 0

            self.cunnilingus_69_done = 0
            self.cunnilingus_69_received = 0
            self.cunnilingus_69_received_TRY = 0
            self.cunnilingus_69_received_FAILED = 0

            self.cunnilingus_missionary_done = 0
            self.cunnilingus_missionary_received = 0
            self.cunnilingus_missionary_received_TRY = 0
            self.cunnilingus_missionary_received_FAILED = 0

            self.cunnilingus_received_from_p_didac = 0
            self.cunnilingus_received_from_p_txell = 0
            self.cunnilingus_received_from_p_neus = 0

            # self.cunnilingus_received_from_ + %p_active = 0 # FOR FUTURE, does it could work?

            self.anilingus_done = 0
            self.anilingus_received = 0
            self.anilingus_received_TRY = 0
            self.anilingus_received_FAILED = 0

            self.anilingus_received_from_p_didac = 0
            self.anilingus_received_from_p_txell = 0
            self.anilingus_received_from_p_neus = 0

            #

            self.vaginal_done = 0
            self.vaginal_received = 0
            self.vaginal_received_TRY = 0
            self.vaginal_received_FAILED = 0

            self.vaginalDeep_done = 0
            self.vaginalDeep_received = 0
            self.vaginalDeep_received_TRY = 0
            self.vaginalDeep_received_FAILED = 0

            self.anal_done = 0
            self.anal_received = 0
            self.anal_received_TRY = 0
            self.anal_received_FAILED = 0

            self.analDeep_done = 0
            self.analDeep_received = 0
            self.analDeep_received_TRY = 0
            self.analDeep_received_FAILED = 0

            self.anal_fingered_done = 0
            self.vaginal_fingered_done = 0
            self.clitoris_fingered_done = 0

            self.anal_fingered_received = 0
            self.vaginal_fingered_received = 0
            self.clitoris_fingered_received = 0

            self.anal_fingered_received_TRY= 0
            self.anal_fingered_received_FAILED = 0
            self.vaginal_fingered_received_TRY = 0
            self.vaginal_fingered_received_FAILED = 0
            self.clitoris_fingered_received_TRY = 0
            self.clitoris_fingered_received_FAILED = 0

            self.buttockSlaps_received = 0 #How Many Slaps received.


            #

            self.creampie_vaginal = 0
            self.creampie_anal = 0
            self.creampie_oral = 0
            self.creampie_total = 0

            #

            self.throat_dilatation = 0 # to have less pain.
            self.vaginal_dilatation = 0
            self.anal_dilatation = 0

            self.anal_pain = 0
            self.vaginal_pain = 0
            self.throat_pain = 0
            self.dick_pain = 0
            self.buttocks_pain = 0
            self.body_pain = 0 # rest of the body

            self.anal_pain_received = 0
            self.vaginal_pain_received = 0
            self.throat_pain_received = 0
            self.dick_pain_received = 0
            self.buttocks_pain_received = 0 # Painful
            self.buttockSlaps_well_received = 0 # Not Painful
            self.body_pain_received = 0 # rest of the body

            self.dick_speed = 0

            self.takeDickOutTimes = 0 # Times you took your dick Off from her.

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

        #@property
        def check_closeOrgasmTotal(self):

            self.closeOrgasmTotal = int(self.closeOrgasm + (self.pleasure*0.1))

            #return self.closeOrgasmTotal
        def check_max_pleasure(self):

            # ORGASM

            if self.closeOrgasmTotal > self.max_pleasure[self.orgasm]:
                self.orgasmScene = True
                #return True

        def check_pleasure(self):

            if self.id == "p_prot":

                if p_prot.action not in ["masturbate", "blowjob_received", "blowjobDeep_received", "vaginal_done", "vaginalDeep_done", "anal_done", "analDeep_done"]:

                    if (
                        (self.orgasm == 0 and self.closeOrgasm > 20) or
                        (self.orgasm == 1 and self.closeOrgasm > 30) or
                        (self.orgasm == 2 and self.closeOrgasm > 40)
                        ):
                        self.closeOrgasm -= 3
                        self.pleasure -= 3

            # Receive finger in asshole.

            if self.b_action == "anal_fingered_received":
                self.closeOrgasm += 1
                self.pleasure += 2

            # MASTURBATE

            if self.action == "masturbate":
                self.closeOrgasm += 5
                self.pleasure += 15 #Just to go faster #4 is the original

            # TITWANK

            if self.action == "titwank_received":
                self.closeOrgasm += 7
                self.pleasure += 8

            # KISS

            if self.b_action == "kiss_received":
                #self.closeOrgasm += 2
                self.pleasure += 4

            if self.b_action == "kiss_done":
                #self.closeOrgasm += 1
                self.pleasure += 2

            # CUNNILINGUS

            if self.action == "cunnilingus_received" or self.b_action == "cunnilingus_received":
                self.closeOrgasm += 7
                self.pleasure += 8
                self.vaginal_dilatation += 1
                self.vaginal_pain -= 1

            if self.action == "cunnilingus_done":
                #self.closeOrgasm += 1
                self.pleasure += 1

            # ANILINGUS

            if self.action == "anilingus_received" or self.b_action == "anilingus_received":
                self.closeOrgasm += 7
                self.pleasure += 8
                self.anal_dilatation += 1
                self.anal_pain -= 1

            if self.action == "anilingus_done":
                #self.closeOrgasm += 1
                self.pleasure += 1

            # BLOWJOB

            if self.action == "blowjob_done":
                
                if self.throat_pain > 0:
                    #self.closeOrgasm -= 2
                    self.pleasure -= 3
                    debug("Painful Deepthroat")
                else:
                    #self.closeOrgasm += 2
                    self.pleasure += 3

            if self.action == "blowjob_received" or self.b_action == "blowjob_received":

                if self.dick_pain > 0:
                    debug("Receiving a PAINFUL blowjob")
                    self.closeOrgasm += 3
                    self.pleasure += 6
                else:
                    self.closeOrgasm += 10 # 10
                    self.pleasure += 12

            # DEEPTHROAT

            if self.action == "blowjobDeep_done":

                if self.throat_pain > 0:
                    #self.closeOrgasm -= 4
                    self.pleasure -= 2
                else:
                    #self.closeOrgasm += 3
                    self.pleasure += 5

            if self.action == "blowjobDeep_received" or self.b_action == "blowjobDeep_received":

                if self.dick_pain > 0:
                    self.closeOrgasm += 6
                    self.pleasure += 8
                else:
                    self.closeOrgasm += 14 #18
                    self.pleasure += 16

            # VAGINAL

            if self.action == "vaginal_done":

                if self.dick_pain > 0:
                    self.closeOrgasm += 2
                    self.pleasure += 3
                else:
                    self.closeOrgasm += 5 # 10
                    self.pleasure += 6

            if self.action == "vaginal_received" or self.b_action == "vaginal_received":

                if self.vaginal_pain > 0:
                    self.closeOrgasm += 2
                    self.pleasure += 3
                else:
                    self.closeOrgasm += 6 # 15
                    self.pleasure += 7

            # VAGINAL_DEEP

            if self.action == "vaginalDeep_done":

                if self.dick_pain > 0:
                    self.closeOrgasm += 3
                    self.pleasure += 6
                else:
                    self.closeOrgasm += 6 # 15
                    self.pleasure += 7

            if self.action == "vaginalDeep_received" or self.b_action == "vaginalDeep_received":

                if self.vaginal_pain > 0:
                    self.closeOrgasm -= 1 # +5
                    self.pleasure += 1
                else:
                    self.closeOrgasm += 7 # 18
                    self.pleasure += 6

            # ANAL

            if self.action == "anal_done":

                if self.dick_pain > 0:
                    self.closeOrgasm += 3
                    self.pleasure += 4
                else:
                    self.closeOrgasm += 6 # 12
                    self.pleasure += 7

            if self.action == "anal_received" or self.b_action == "anal_received":

                if self.anal_pain > 0:
                    self.closeOrgasm -= 1
                    self.pleasure += 1
                else:
                    self.closeOrgasm += 3 # 8
                    self.pleasure += 5

            # ANAL_DEEP

            if self.action == "analDeep_done":

                if self.dick_pain > 0:
                    self.closeOrgasm += 3 # +5
                    self.pleasure += 4
                else:
                    self.closeOrgasm += 7 # 18
                    self.pleasure += 8
                    

            if self.action == "analDeep_received" or self.b_action == "analDeep_received":

                if self.anal_pain > 0:
                    self.closeOrgasm -= 3 # +5
                    self.pleasure += 4
                else:
                    self.closeOrgasm += 5 # 12
                    self.pleasure += 7



            #return self.closeOrgasm

        def check_pain(self):

            if self.anal_pain > 0:
                self.anal_pain -= 1

            if self.vaginal_pain > 0:
                self.vaginal_pain -= 1

            if self.throat_pain > 0:
                self.throat_pain -= 1

            if self.dick_pain > 0:
                self.dick_pain -= 1

            if self.buttocks_pain > 0:
                self.buttocks_pain -= 1

            if self.body_pain > 0:
                self.body_pain -= 1

        def p_closeToOrgasm(self):

            if self not in p_dictCloseOrgasm:
                p_dictCloseOrgasm[self] = -1

            if (self.orgasm >= 4 and self.closeOrgasmTotal > 135 or
            self.orgasm == 3 and self.closeOrgasmTotal > 115 or
            self.orgasm == 2 and self.closeOrgasmTotal > 90 or
            self.orgasm == 1 and self.closeOrgasmTotal > 65 or
            self.orgasm == 0 and self.closeOrgasmTotal > 40):
                if p_dictCloseOrgasm[self] == -4:
                    p_dictCloseOrgasm[self] = 4

            elif (self.orgasm >= 4 and self.closeOrgasmTotal > 100 or
            self.orgasm == 3 and self.closeOrgasmTotal > 85 or
            self.orgasm == 2 and self.closeOrgasmTotal > 75 or
            self.orgasm == 1 and self.closeOrgasmTotal > 50 or
            self.orgasm == 0 and self.closeOrgasmTotal > 30):
                if p_dictCloseOrgasm[self] == -3:
                    p_dictCloseOrgasm[self] = 3

            elif (self.orgasm >= 4 and self.closeOrgasmTotal > 75 or
            self.orgasm == 3 and self.closeOrgasmTotal > 60 or
            self.orgasm == 2 and self.closeOrgasmTotal > 45 or
            self.orgasm == 1 and self.closeOrgasmTotal > 35 or
            self.orgasm == 0 and self.closeOrgasmTotal > 20):
                if p_dictCloseOrgasm[self] == -2:
                    p_dictCloseOrgasm[self] = 2

            elif (self.orgasm >= 4 and self.closeOrgasmTotal > 50 or
            self.orgasm == 3 and self.closeOrgasmTotal > 40 or
            self.orgasm == 2 and self.closeOrgasmTotal > 35 or
            self.orgasm == 1 and self.closeOrgasmTotal > 25 or
            self.orgasm == 0 and self.closeOrgasmTotal > 10):
                if p_dictCloseOrgasm[self] == -1:
                    p_dictCloseOrgasm[self] = 1




    class Pedrera_Girl(Pedrera_Body):

        def __init__(self):

            Pedrera_Body.__init__(self)

            #self.p_girl_active = p_didac

            self.closeOrgasm_check = 0
            self.throat_dilatation_check = 0
            self.vaginal_dilatation_check = 0
            self.anal_dilatation_check = 0



label afternight05_Pedrera_Sex_Check_closeOrgasm_Check:

    $ p_prot.check_closeOrgasmTotal()
    $ p_neus.check_closeOrgasmTotal()
    $ p_didac.check_closeOrgasmTotal()
    $ p_txell.check_closeOrgasmTotal()

    $ debug ("CloseOrgasm_Check")

    return

label afternight05_Pedrera_Sex_af_numbers:

    call afternight05_Pedrera_Sex_Check_closeOrgasm_Check

    $ p_prot.check_pleasure()
    $ p_neus.check_pleasure()
    $ p_didac.check_pleasure()
    $ p_txell.check_pleasure()

    #$ debug ("Pleasure_Check")

    $ p_prot.check_pain()
    $ p_neus.check_pain()
    $ p_didac.check_pain()
    $ p_txell.check_pain()

    #$ debug ("Pain_Check")

    $ p_prot.check_max_pleasure()
    $ p_neus.check_max_pleasure()
    $ p_didac.check_max_pleasure()
    $ p_txell.check_max_pleasure()

    #$ debug ("Max_pleasure_Check")

    call ped_checkStatusgirl

    if p_active == "p_neus":
        call p_neus_whispers

    if p_characters_action == "rest":

        $ p_prot.action = "rest"

        if p_active == "p_didac":

            $ p_didac.action = "rest"

        $ p_characters_action = ""

    return

label ped_checkStatusgirl:

## THROAT VAGINAL ANAL dilatation check.

    if (
        p_prot.action in ["oral_received", "oralDeep_received", "vaginal_done", "vaginalDeep_done", "anal_done", "analDeep_done"] or
        p_prot.b_action in ["oral_received", "oralDeep_received"]
        ):

        if p_prot.pos == "oral" and p_prot.action == "blowjob_received" and ped_sex_general_action_Cond == "o03_01":

            pause 1.0

            pt "Caray..."

            pt "Parece que se lo est?? tomando m??s en serio..."


        if (
            (p_prot.action == "blowjob_received" and p_girl_active.throat_dilatation >= 4) or
            (p_prot.action == "vaginal_done" and p_girl_active.vaginal_dilatation >= 4) or
            (p_prot.action == "anal_done" and p_girl_active.anal_dilatation >= 4)
            ):

            if (
                (p_prot.action == "blowjob_received" and p_girl_active.throat_dilatation_check == 0) or 
                (p_prot.action == "vaginal_done" and p_girl_active.vaginal_dilatation_check == 0) or 
                (p_prot.action == "anal_done" and p_girl_active.anal_dilatation_check == 0)
                ):

                if p_girl_active.throat_dilatation_check == 0:
                    $ p_girl_active.throat_dilatation_check = 1

                elif p_girl_active.vaginal_dilatation_check == 0:
                    $ p_girl_active.vaginal_dilatation_check = 1

                elif p_girl_active.anal_dilatation_check == 0:
                    $ p_girl_active.anal_dilatation_check = 1

                if p_prot.action == "blowjob_received":

                    pt "Es posible que ahora le entre entera..."

                else:

                    pt "Dir??a que est?? suficientemente dilatada..."

        elif (
            (p_prot.action == "blowjob_received" and p_girl_active.throat_dilatation == 3) or
            (p_prot.action == "vaginal_done" and p_girl_active.vaginal_dilatation == 3) or
            (p_prot.action == "anal_done" and p_girl_active.anal_dilatation == 3)
            ):

            if p_prot.action == "blowjob_received":

                pt "Parece que ya no le dan tantas arcadas..."

            else:

                pt "Parece que empieza a estar bastante dilatada aqu?? abajo..."

        elif (
            (p_prot.action == "blowjob_received" and p_girl_active.throat_dilatation == 2) or
            (p_prot.action == "vaginal_done" and p_girl_active.vaginal_dilatation == 2) or
            (p_prot.action == "anal_done" and p_girl_active.anal_dilatation == 2)
            ):

            pt "Un poco m??s y quiz??s pueda met??rsela entera..."

        elif (
            (p_prot.action == "blowjob_received" and p_girl_active.throat_dilatation == 1) or
            (p_prot.action == "vaginal_done" and p_girl_active.vaginal_dilatation == 1) or
            (p_prot.action == "anal_done" and p_girl_active.anal_dilatation == 1)
            ):

            pt "Parece que a??n no est?? preparada para recibirla entera..."

        elif (
            (p_prot.action == "blowjob_received" and p_girl_active.throat_dilatation == -1) or
            (p_prot.action == "vaginal_done" and p_girl_active.vaginal_dilatation == -1) or
            (p_prot.action == "anal_done" and p_girl_active.anal_dilatation == -1)
            ):

            pt "Es posible que a??n le duela si intento met??rsela entera..."

        elif (
            (p_prot.action == "blowjob_received" and p_girl_active.throat_dilatation == -2) or
            (p_prot.action == "vaginal_done" and p_girl_active.vaginal_dilatation == -2) or
            (p_prot.action == "anal_done" and p_girl_active.anal_dilatation == -2)
            ):

            pt "Parece que le duele..."

        elif (
            (p_prot.action == "blowjob_received" and p_girl_active.throat_dilatation == -3) or
            (p_prot.action == "vaginal_done" and p_girl_active.vaginal_dilatation == -3) or
            (p_prot.action == "anal_done" and p_girl_active.anal_dilatation == -3)
            ):

            pt "Tiene pinta de que le duele bastante..."

        elif (
            (p_prot.action == "blowjob_received" and p_girl_active.throat_dilatation == -4) or
            (p_prot.action == "vaginal_done" and p_girl_active.vaginal_dilatation ==-4) or
            (p_prot.action == "anal_done" and p_girl_active.anal_dilatation == -4)
            ):

            pt "Tiene que dolerle un mont??n..."

        elif (
            (p_prot.action == "blowjob_received" and p_girl_active.throat_dilatation == -5) or
            (p_prot.action == "vaginal_done" and p_girl_active.vaginal_dilatation == -5) or
            (p_prot.action == "anal_done" and p_girl_active.anal_dilatation == -5)
            ):

            pt "Aunque le duela, sigue sin apartarme..."

        elif (
            (p_prot.action == "blowjob_received" and p_girl_active.throat_dilatation == -6) or
            (p_prot.action == "vaginal_done" and p_girl_active.vaginal_dilatation == -6) or
            (p_prot.action == "anal_done" and p_girl_active.anal_dilatation == -6)
            ):

            if p_prot.pos == "oral":
                pt "Lo raro es que no me muerda."

            else:
                pt "Lo raro es que no me de una patada..."

        elif (
            (p_prot.action == "blowjob_received" and p_girl_active.throat_dilatation <= -7) or
            (p_prot.action == "vaginal_done" and p_girl_active.vaginal_dilatation <= -7) or
            (p_prot.action == "anal_done" and p_girl_active.anal_dilatation <= -7)
            ):

            pass

            #pt "Es posible que a??n le duela si intento met??rsela entera..."


    ## P_PROT checkOrgasm

        if p_dictCloseOrgasm[p_prot] == 0:
            $ p_dictCloseOrgasm[p_prot] = -1

        elif p_dictCloseOrgasm[p_prot] == 1:
            $ p_dictCloseOrgasm[p_prot] = -2

            if p_prot.orgasm == 0:
                pt "Realmente la tengo bien dura..."
            elif p_prot.orgasm == 1:
                pt "Vuelvo a tenerla super dura..."
            elif p_prot.orgasm == 2:
                pt "Es incre??ble que vuelva a tenerla tan dura..."

        elif p_dictCloseOrgasm[p_prot] == 2:
            $ p_dictCloseOrgasm[p_prot] = -3

            pt "Si sigo as??,"

            if p_prot.orgasm == 0:
                extend " no tardar?? en correrme..."
            elif p_prot.orgasm == 1:
                extend " no tardar?? en volver a correrme..."
            elif p_prot.orgasm == 2:
                extend " no tardar?? en volver a correrme por tercera vez..."

        elif p_dictCloseOrgasm[p_prot] == 3:
            $ p_dictCloseOrgasm[p_prot] = -4

            pt "Mierda..."

            pt "No aguantar?? mucho m??s..."

        elif p_dictCloseOrgasm[p_prot] == 4:
            $ p_dictCloseOrgasm[p_prot] = -5

            pt "Estoy a punto..."

    # Close Orgasm Check

        if (p_girl_active.orgasm >= 4 and p_girl_active.closeOrgasmTotal > 145 or
            p_girl_active.orgasm == 3 and p_girl_active.closeOrgasmTotal > 120 or
            p_girl_active.orgasm == 2 and p_girl_active.closeOrgasmTotal > 95 or
            p_girl_active.orgasm == 1 and p_girl_active.closeOrgasmTotal > 70 or
            p_girl_active.orgasm == 0 and p_girl_active.closeOrgasmTotal > 45):

            if p_girl_active.closeOrgasm_check == 4:
                $ p_girl_active.closeOrgasm_check = 5
            
                pt "Est?? a punto..."

        elif (p_girl_active.orgasm >= 4 and p_girl_active.closeOrgasmTotal > 135 or
            p_girl_active.orgasm == 3 and p_girl_active.closeOrgasmTotal > 115 or
            p_girl_active.orgasm == 2 and p_girl_active.closeOrgasmTotal > 90 or
            p_girl_active.orgasm == 1 and p_girl_active.closeOrgasmTotal > 65 or
            p_girl_active.orgasm == 0 and p_girl_active.closeOrgasmTotal > 40):

            if p_girl_active.closeOrgasm_check == 3:
                $ p_girl_active.closeOrgasm_check = 4
            
                pt "No le falta demasiado..."

        elif (p_girl_active.orgasm >= 4 and p_girl_active.closeOrgasmTotal > 100 or
            p_girl_active.orgasm == 3 and p_girl_active.closeOrgasmTotal > 85 or
            p_girl_active.orgasm == 2 and p_girl_active.closeOrgasmTotal > 75 or
            p_girl_active.orgasm == 1 and p_girl_active.closeOrgasmTotal > 50 or
            p_girl_active.orgasm == 0 and p_girl_active.closeOrgasmTotal > 30):

            if p_girl_active.closeOrgasm_check == 2:
                $ p_girl_active.closeOrgasm_check = 3
            
                pt "Parece que le falta poco..."

        elif (p_girl_active.orgasm >= 4 and p_girl_active.closeOrgasmTotal > 75 or
            p_girl_active.orgasm == 3 and p_girl_active.closeOrgasmTotal > 60 or
            p_girl_active.orgasm == 2 and p_girl_active.closeOrgasmTotal > 45 or
            p_girl_active.orgasm == 1 and p_girl_active.closeOrgasmTotal > 35 or
            p_girl_active.orgasm == 0 and p_girl_active.closeOrgasmTotal > 20):

            if p_girl_active.closeOrgasm_check == 1:
                $ p_girl_active.closeOrgasm_check = 2
            
                pt "Se est?? empezando a poner cachonda..."

        elif (p_girl_active.orgasm >= 4 and p_girl_active.closeOrgasmTotal > 50 or
            p_girl_active.orgasm == 3 and p_girl_active.closeOrgasmTotal > 40 or
            p_girl_active.orgasm == 2 and p_girl_active.closeOrgasmTotal > 35 or
            p_girl_active.orgasm == 1 and p_girl_active.closeOrgasmTotal > 25 or
            p_girl_active.orgasm == 0 and p_girl_active.closeOrgasmTotal > 10):

            if p_girl_active.closeOrgasm_check == 0:
                $ p_girl_active.closeOrgasm_check = 1
            
                pt "Cada vez le falta menos..."

    return

label p_character_throat_pain_common:

    if (p_active == "p_didac" and p_didac.throat_pain >= 5) or (p_active == "p_txell" and p_txell.throat_pain >= 5) or (p_active == "p_neus" and p_neus.throat_pain >= 5):

        pt "Parece que tardar?? en poder volver a met??rsela en la garganta..."

        pt "Se la he metido demasiadas veces sin que estuviera preparada..."

    elif (p_active == "p_didac" and p_didac.throat_pain == 4)  or (p_active == "p_txell" and p_txell.throat_pain == 4) or (p_active == "p_neus" and p_neus.throat_pain == 4):

        pt "Parece que a??n le duele bastante..."

    elif (p_active == "p_didac" and p_didac.throat_pain == 3) or (p_active == "p_txell" and p_txell.throat_pain == 3) or (p_active == "p_neus" and p_neus.throat_pain == 3):

        pt "A??n deber??a de esperar un poco m??s..."

    elif (p_active == "p_didac" and p_didac.throat_pain == 2) or (p_active == "p_txell" and p_txell.throat_pain == 2) or (p_active == "p_neus" and p_neus.throat_pain == 2):

        pt "No parece que le quede mucho para poder convencerla..."

    elif (p_active == "p_didac" and p_didac.throat_pain == 1) or (p_active == "p_txell" and p_txell.throat_pain == 1) or (p_active == "p_neus" and p_neus.throat_pain == 1):

        pt "Quiz??s la pr??xima vez ya me deje met??rsela..."

    return

label p_neus_orgasmHurry_label:
    if p_neus.orgasm == 0:
        if p_neus.closeOrgasmTotal > 20:
            if float(p_neus.closeOrgasmTotal/50.0) > float(p_prot.closeOrgasmTotal/125.0):
                $ p_neus_orgasmHurry = True
    elif p_neus.orgasm == 1:
        if p_neus.closeOrgasmTotal > 30:
            if float(p_neus.closeOrgasmTotal/75.0) > float(p_prot.closeOrgasmTotal/125.0):
                $ p_neus_orgasmHurry = True
    else:
        $ p_neus_orgasmHurry = False
    return

label afternight05_Pedrera_Sex_After:

    #call p_prot_previousSex # Is this really necessary? Before? What the fuck?!

    call p_neus_orgasmHurry_label

    call afternight05_Pedrera_Sex_checkingOrgasm

    call afternight05_Pedrera_Sex_af_numbers

    if p_didac.action == "cunnilingus_done_p_txell":

        $ p_didac.cunnilingus_done += 1
        $ p_txell.cunnilingus_received_from_p_didac += 1
        $ p_txell.vaginal_dilatation += 1
        $ p_txell.closeOrgasm += 3
        $ p_txell.pleasure += 4

    if p_prot.action not in ["cunnilingus_done", "anilingus_done"]:

        $ afternight05_Pedrera_Neus_Warning_tongue = 0

####################################################################################################
###################################################################################################
##################################################################################################
    
    #if p_pneus.orgasmScene == True or p_didac.orgasmScene == True or p_txell.orgasmScene == True:
    if p_girl_active.orgasmScene == True:
        $ p_girl_active.closeOrgasm_check = 0

    if p_neus.orgasmScene == True:

        $ p_neus_orgasm_TRY += 1

        if p_neus_orgasm_TRY == 1:

            play sound "audio/sfx/fall09.ogg"

            scene black
            with vpunch
            with vpunch

            p "{size=60}??AAUCH!{/size}"

            call p_neus_orgasm_warning

        else:

            $ ped_sex_general_zoom_Cond = "face"
            $ ped_sex_general_expression_Cond = "talk"
            call pedrera_sex_p_general_talk

            $ debug ("Neus having an orgasm.")

            if p_prot.pos == "69":
                if p_prot.b_action in p_prot_69_blowjob_received:
                    call ped_sex_69_mc_blowjob_Stop
                    with Dissolve(0.5)

            if p_prot.pos == "oral":

                progcheck "Oral position is even possible??"

                $ nteye = "front06"
                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                show gensex_oral_n_frontHead_exp_eyebrows sadx06
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

            elif p_prot.pos == "missionary":

                $ nteye = "front06"
                show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                show gensex_missionary_n_head_exp_eyebrows sadx06
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

            elif p_prot.pos == "69":

                show gensex_69_L_d_mouth sad_Talkingx06
                with dissolve

            ne "??Mi-"

            extend "mierda!"

            if p_prot.pos == "oral":
                $ nteye = "front07"
                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx005
                show gensex_oral_n_frontHead_exp_eyebrows sadx07
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

            elif p_prot.pos == "missionary":
                $ nteye = "front07"
                show gensex_missionary_n_head_exp_mouth sad_Talkingx005
                show gensex_missionary_n_head_exp_eyebrows sadx07
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx07
                with dissolve

            ne "????No!!"

            if p_prot.pos == "oral":
                $ nteye = "front04"
                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx10
                show gensex_oral_n_frontHead_exp_eyebrows angryx05
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

            elif p_prot.pos == "missionary":
                $ nteye = "front04"
                show gensex_missionary_n_head_exp_mouth sad_Talkingx10
                show gensex_missionary_n_head_exp_eyebrows angryx05
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx09
                with dissolve

            ne "??[protname]!"

            if p_prot.pos == "oral":
                $ nteye = "front06"
                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx010
                show gensex_oral_n_frontHead_exp_eyebrows angryx06
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

            elif p_prot.pos == "missionary":
                $ nteye = "front06"
                show gensex_missionary_n_head_exp_mouth sad_Talkingx010
                show gensex_missionary_n_head_exp_eyebrows angryx06
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx10
                with dissolve

            ne "??Te-"

            extend "te hab??a dicho que no!"

            jump p_neus_orgasmRealScene

        $ p_neus.orgasmScene = False

    if p_didac.orgasmScene == True:

        $ debug ("Didac having an orgasm.")

        if p_didac.b_action in ["vaginal_received"]:
            $ ped_sex_general_action_Cond = "vdcum01"
        elif p_didac.b_action in ["vaginalDeep_received"]:
            $ ped_sex_general_action_Cond = "vdcum02"
        elif p_didac.b_action in ["anal_received"]:
            $ ped_sex_general_action_Cond = "adcum01"
        elif p_didac.b_action in ["analDeep_received"]:
            $ ped_sex_general_action_Cond = "adcum02"
        else:
            
            if p_prot.pos != "69":
                $ ped_sex_general_action_Cond = "00"
                $ p_prot.action = "rest"

                if p_didac.action != "cunnilingus_done_p_txell":
                    $ p_didac.action = "rest"

        if p_didac.orgasm == 0:
            $ ped_sex_general_action_b_Cond = "sdcum01"
        elif p_didac.orgasm == 1:
            $ ped_sex_general_action_b_Cond = "sdcum02"
        elif p_didac.orgasm == 2:
            $ ped_sex_general_action_b_Cond = "sdcum03"
        elif p_didac.orgasm >= 3:
            $ ped_sex_general_action_b_Cond = "sdcum04"

        $ randomnum_1to10 = renpy.random.randint(1, 10)

        if p_prot.pos == "missionary":

            $ ped_sex_general_zoom_Cond = ""
            $ ped_sex_general_expression_Cond = "talk"
            #$ ped_sex_general_action_Cond = "talk"
            call pedrera_sex_p_general_talk

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 06
                show gensex_missionary_d_head_exp_pupils front06
                show gensex_missionary_d_head_exp_eyebrows sadx07
                show gensex_missionary_d_head_exp_mouth sad_Talkingx13

        elif p_prot.pos == "doggy":

            $ ped_sex_general_zoom_Cond = "crotch"

            call pedrera_sex_p_general_talk

        elif p_prot.pos == "69":

            $ ped_sex_general_expression_Cond = "talk"
            $ ped_sex_general_action_b_Cond = "69b_00_00b"
            call pedrera_sex_p_general_talk

            if randomnum_1to10 in range(1,8):
                show gensex_69_L_d_mouth sad_Talkingx005
            else:
                show gensex_69_L_d_mouth happybiting_Silentx10

        with vpunch

        if randomnum_1to10 == 1:

            d "{size=70}??AAAHMMMm..!{/size}"

        elif randomnum_1to10 == 2:

            d "{size=70}??Ahhhmm...!{/size}"

        elif randomnum_1to10 == 3:

            d "{size=70}??AAah-ahmm...!{/size}"

        elif randomnum_1to10 == 4:

            d "{size=70}??AAHHMMMmm...!{/size}"

        elif randomnum_1to10 == 5:

            d "{size=70}??AA-Aahmm...!{/size}"

        elif randomnum_1to10 == 6:

            d "{size=70}??AAHHhhmm...!{/size}"

        elif randomnum_1to10 == 7:

            d "{size=70}??AAAaah-ahhmm...!{/size}"

        elif randomnum_1to10 == 8:

            d "{size=70}??HUUUHhmmm...!{/size}"

        elif randomnum_1to10 == 9:

            d "{size=70}??Huhmmfmm...!{/size}"

        elif randomnum_1to10 == 10:

            d "{size=70}??FFMmhmmm...!{/size}"

        if p_prot.pos == "69":
            $ p_prot.action = "rest"
            $ p_didac.action = "rest"

            $ p_prot.b_action = "rest"
            $ p_girl_active.b_action = "rest"

            $ ped_sex_general_69_cover = "over"
            $ ped_sex_general_action_Cond = "69_00_00" # MC Not Licking
            $ ped_sex_general_action_b_Cond = "69b_00_00b" # Didac Have dick in fron face.
            # Vaginal cumshot on 69?

        else:

            $ ped_sex_general_action_b_Cond = ""

        $ p_prot.action = "rest"
        if p_didac.action != "cunnilingus_done_p_txell":
            $ p_didac.action = "rest"


        $ p_didac.orgasm += 1
        $ p_didac.closeOrgasm = 0
        $ p_didac.pleasure = -50

        $ p_didac.orgasmScene = False

        # if p_prot.pos == "doggy":
        #     $ ped_sex_general_action_Cond = "00"
        #     call pedrera_sex_p_general_talk

        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
            show gensex_missionary_d_head_exp_eyes 08
            show gensex_missionary_d_head_exp_pupils front08
            show gensex_missionary_d_head_exp_eyebrows sadx05
            show gensex_missionary_d_head_exp_mouth sad_Talkingx04
            with Dissolve(1.0)

        elif p_prot.pos == "69":
            #$ ped_sex_general_action_Cond = "vt00_00"
            call pedrera_sex_p_general_talk

            show gensex_69_L_d_mouth sad_Talkingx005
            with Dissolve(1.0)

        d "Aaaahhh.... aaahhh.... ahhh...."

        if p_prot.pos == "doggy":
            $ ped_sex_general_zoom_Cond = "face"
            call pedrera_sex_p_general_talk
            with fade_short

        if p_didac.orgasm == 1:

            if p_didac.action == "cunnilingus_done_p_txell":

                d "Seg??s grab??n..."

            else:

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":

                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows sadx06
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx005

                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx002
                with dissolve


                d "Ser??s cabr??n..."

            if p_prot.pos in ["69"]:

                show gensex_69_L_d_mouth sadbiting_Silentx02
                with dissolve

                p "??Tanto te ha gustado mi lengua?"

                show gensex_69_L_d_mouth sadbiting_Silentx06
                with dissolve

                d "Tssk..."

                show gensex_69_L_d_mouth sad_Talkingx05
                with dissolve

                d "??C??llate un rato y sigue lamiendo!"

                show gensex_69_L_d_mouth sadbiting_Silentx04
                with dissolve

            elif p_prot.pos in ["oral"]:

                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx02
                show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                with dissolve

                p "Te has corrido mientras me la estabas chupando..."

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                with dissolve

                p "Es algo sorprendente,"

                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                with dissolve

                p "??No crees?"

                if p_prot.vaginal_done > 0:

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx06
                    show gensex_oral_d_frontHead_exp_eyebrows angryx02
                    with dissolve

                    d "??Tambi??n me la has metido!"

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_d_frontHead_exp_eyebrows angryx02
                    with dissolve

                    d "??Eso tambi??n cuenta!"

                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris front03
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx03
                    show gensex_oral_d_frontHead_exp_eyebrows suspiciousx01
                    with dissolve

                    p "Ya,"

                    extend " ya..."

                    show gensex_oral_d_frontHead_exp_eyes 00
                    show gensex_oral_d_frontHead_exp_iris front00
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
                    show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                    with dissolve

                    p "pero ahora no te la estoy metiendo..."

                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris right03
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx03
                    show gensex_oral_d_frontHead_exp_eyebrows angryx01
                    with dissolve

                    d "..."

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
                    show gensex_oral_d_frontHead_exp_eyebrows angryx02
                    with dissolve

                    d "Tssk..."

                elif p_prot.anal_done > 0:

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx03
                    show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                    with dissolve

                    d "??Tambi??n me la has metido por el culo!"

                    show gensex_oral_d_frontHead_exp_eyes 00
                    show gensex_oral_d_frontHead_exp_iris front00
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx03
                    show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                    with dissolve

                    p "Lo que significa que no te disgusta tanto..."

                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris right03
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx03
                    show gensex_oral_d_frontHead_exp_eyebrows angryx01
                    with dissolve

                    d "..."

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
                    show gensex_oral_d_frontHead_exp_eyebrows angryx02
                    with dissolve

                    d "Tsskk..."

            else:

                if p_prot.pos == "doggy":

                    $ ped_sex_general_zoom_Cond = "crotch"
                    call pedrera_sex_p_general_talk
                    with fade_short

                elif p_prot.pos == "missionary":

                    if p_didac.action != "cunnilingus_done_p_txell":

                        show gensex_missionary_d_head_exp_eyes 05
                        show gensex_missionary_d_head_exp_pupils front05
                        show gensex_missionary_d_head_exp_eyebrows sadx07
                        show gensex_missionary_d_head_exp_mouth happybiting_Silentx11
                        with dissolve

                else:

                    $ debug("In which pose are you?")

                    $ debug ("In which pose are you?")


                if p_prot.vaginal_done == 0 and p_prot.anal_done == 0:

                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_d_frontHead_exp_eyebrows suspiciousx01
                    with dissolve

                    d "Has conseguido que me corra solo con tu lengua..."

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx2
                    show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                    with dissolve

                    p "??Y tanto te ha disgustado?"

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
                    show gensex_oral_d_frontHead_exp_eyebrows angryx02
                    with dissolve

                    d "Tsskk..."

                else:

                    #if p_didac.anilingus_received

                    if ((p_didac.cunnilingus_received > p_didac.vaginal_received + p_didac.anal_received) or 
                        (p_didac.anilingus_received > p_didac.vaginal_received + p_didac.anal_received)):

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx04
                            with dissolve

                        d "La madre que te pari??..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx01
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx07
                            with dissolve

                        d "Que jodida lengua tienes cabr??n..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils front01
                            show gensex_missionary_d_head_exp_eyebrows surprisex01
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05
                            with dissolve

                        if p_didac.cunnilingus_received > p_didac.anilingus_received:

                            p "Eres t?? el que me ped??as que te follase todo el tiempo."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 04
                                show gensex_missionary_d_head_exp_pupils front04
                                show gensex_missionary_d_head_exp_eyebrows suspiciousx01
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx06
                                with dissolve

                            d "Un poco m??s de tu poll??n tampoco hubiera estado mal..."

                        else:

                            if p_didac.cunnilingus_received == 0:

                                p "Y eso que no te la he pasado por d??nde m??s te hubiera gustado..."

                            else:
                        
                                p "Y eso que mayormente lo has disfrutado por detr??s..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 03
                                show gensex_missionary_d_head_exp_pupils right03
                                show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
                                with dissolve

                            d "..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 04
                                show gensex_missionary_d_head_exp_pupils front04
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx08
                                with dissolve

                            d "??Acaso buscabas algo por ah?? dentro?"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils front01
                            show gensex_missionary_d_head_exp_eyebrows surprisex02
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx08
                            with dissolve

                        p "??Es que tienes alguna queja?"

                        if p_prot.pos == "doggy":
                            $ ped_sex_general_zoom_Cond = "face"
                            call pedrera_sex_p_general_talk
                            with fade_short

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows surprisex02
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx003
                            with dissolve

                        d "Por ahora quiz??s no..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows angryx01
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx08
                            with dissolve

                        d "Pero espero que tarde o temprano me la metas d??nde ya sabes..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                            with dissolve

                        d "??Me explico...?"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth happybiting_Silentx06
                            with dissolve

                        p "..."

                        pt "La madre que lo..."

                    elif p_didac.vaginal_received + p_didac.vaginalDeep_received > p_didac.anal_received + p_didac.analDeep_received:

                        #if p_prot.action in ["vaginal_done", "vaginalDeep_done"]:
                        # Vaginal Done more than Anal.

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows sadx02
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx06
                            with dissolve

                        d "Has conseguido que me corra con tu enorme poll??n..."

                        if p_prot.anal_done > 0:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 01
                                show gensex_missionary_d_head_exp_pupils front01
                                show gensex_missionary_d_head_exp_eyebrows surprisex01
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                                with dissolve

                            p "Tambi??n te la he metido por detr??s..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 03
                                show gensex_missionary_d_head_exp_pupils front03
                                show gensex_missionary_d_head_exp_eyebrows angryx05
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                                with dissolve

                            d "??Eso no cuenta!"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils front05
                                show gensex_missionary_d_head_exp_eyebrows sadx03
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx11
                                with dissolve

                            pt "Ya..."

                    else:

                        #elif p_prot.action in ["anal_done", "analDeep_done"]:
                        # Anal done more than Vaginal.

                        p "??Te sorprendes que te hayas corrido teniendo mi polla en tu trasero?"

                        d "..."

                        if p_didac.vaginal_received > 0:

                            d "??Tambi??n me la has metido por delante!"

                            if p_didac.anal_received > p_didac.vaginal_received:

                                p "Pero te la he metido m??s veces por detr??s,"

                                p "y lo sabes..."

                                d "..."

                                d "Tskk..."

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 00
                show gensex_missionary_d_head_exp_pupils front00
                show gensex_missionary_d_head_exp_eyebrows surprisex01
                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Silentx03

            with dissolve

            p "Eso es que no te ha gustado?"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 03
                show gensex_missionary_d_head_exp_pupils front03
                show gensex_missionary_d_head_exp_eyebrows angryx04
                show gensex_missionary_d_head_exp_mouth sad_Talkingx13
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx05
                
            with dissolve

            d "Eso significa que ya est??s tardando en continuar."

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 05
                show gensex_missionary_d_head_exp_pupils front05
                show gensex_missionary_d_head_exp_eyebrows sadx03
                show gensex_missionary_d_head_exp_mouth happybiting_Silentx07
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth happybiting_Silentx07
                
            with dissolve

        elif p_didac.orgasm == 2:

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 06
                show gensex_missionary_d_head_exp_pupils front06
                show gensex_missionary_d_head_exp_eyebrows sadx03
                show gensex_missionary_d_head_exp_mouth happy_Talkingx05
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth happy_Talkingx05
                
            with dissolve

            d "Puto cabr??n..."

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 05
                show gensex_missionary_d_head_exp_pupils front05
                show gensex_missionary_d_head_exp_eyebrows sadx04
                show gensex_missionary_d_head_exp_mouth happy_Talkingx07
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth happy_Talkingx07
                
            with dissolve

            d "Has conseguido que llegue a dos..."

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 02
                show gensex_missionary_d_head_exp_pupils front02
                show gensex_missionary_d_head_exp_eyebrows surprisex01
                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sadbiting_Silentx05
                
            with dissolve

            p "??Te sorprende?"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 05
                show gensex_missionary_d_head_exp_pupils front05
                show gensex_missionary_d_head_exp_eyebrows angryx02
                show gensex_missionary_d_head_exp_mouth happy_Talkingx12
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth happy_Talkingx12
                
            with dissolve

            d "??Calla y no pares!"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 06
                show gensex_missionary_d_head_exp_pupils front06
                show gensex_missionary_d_head_exp_eyebrows sadx04
                show gensex_missionary_d_head_exp_mouth happybiting_Silentx12
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth happybiting_Silentx12
                
            with dissolve

        else:

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 07
                show gensex_missionary_d_head_exp_pupils front07
                show gensex_missionary_d_head_exp_eyebrows sadx04
                show gensex_missionary_d_head_exp_mouth sad_Talkingx03
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx03
                
            with dissolve

            d "La madre que te..."

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 08
                show gensex_missionary_d_head_exp_pupils front08
                show gensex_missionary_d_head_exp_eyebrows sadx06
                show gensex_missionary_d_head_exp_mouth sad_Talkingx02
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx02
                
            with dissolve

            d "Dios..."

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 06
                show gensex_missionary_d_head_exp_pupils front06
                show gensex_missionary_d_head_exp_eyebrows sadx05
                show gensex_missionary_d_head_exp_mouth happy_Talkingx08
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth happy_Talkingx08
                
            with dissolve

            d "Ya llevo [p_didac.orgasm]..."

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 04
                show gensex_missionary_d_head_exp_pupils front04
                show gensex_missionary_d_head_exp_eyebrows angryx03
                show gensex_missionary_d_head_exp_mouth happy_Talkingx08
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth happy_Talkingx08
                
            with dissolve

            d "??No pares!"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 06
                show gensex_missionary_d_head_exp_pupils front06
                show gensex_missionary_d_head_exp_eyebrows sadx05
                show gensex_missionary_d_head_exp_mouth happybiting_Silentx09
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth happybiting_Silentx09
                
            with dissolve

        if p_didac.pos == "doggy":
            $ ped_sex_general_zoom_Cond = ""
            call pedrera_sex_p_general_talk
            with fade

    if p_txell.orgasmScene == True:

        $ debug ("Txell having an orgasm.")

        if p_prot.pos == "69":
            show gensex_69_L_d_mouth sadbiting_Silentx04
            with dissolve

        elif p_prot.pos == "oral":
            show gensex_oral_m_frontHead_exp_eyes 01
            show gensex_oral_m_frontHead_exp_iris front01
            show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx08
            show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
            with dissolve

        tx "??Ughh...!"

        with vpunch

        if p_prot.pos == "69":
            show gensex_69_L_d_mouth sad_Talkingx008
            with dissolve

        elif p_prot.pos == "oral":
            show gensex_oral_m_frontHead_exp_eyes 06
            show gensex_oral_m_frontHead_exp_iris front06
            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
            show gensex_oral_m_frontHead_exp_eyebrows sadx04
            with dissolve

        $ randomnum_1to10 = renpy.random.randint(1, 10)

        if randomnum_1to10 == 1:

            tx "{size=70}??AAAHMMMm..!{/size}"

        elif randomnum_1to10 == 2:

            tx "{size=70}??Ahhhmm...!{/size}"

        elif randomnum_1to10 == 3:

            tx "{size=70}??AAah-ahmm...!{/size}"

        elif randomnum_1to10 == 4:

            tx "{size=70}??AAHHMMMmm...!{/size}"

        elif randomnum_1to10 == 5:

            tx "{size=70}??Huhmmfmm...!{/size}"

        elif randomnum_1to10 == 6:

            tx "{size=70}??AAHHhhmm...!{/size}"

        elif randomnum_1to10 == 7:

            tx "{size=70}??HUUUHhmmm...!{/size}"

        elif randomnum_1to10 == 8:

            tx "{size=70}??AAAaah-ahhmm...!{/size}"

        elif randomnum_1to10 == 9:

            tx "{size=70}??AA-Aahmm...!{/size}"

        elif randomnum_1to10 == 10:

            tx "{size=70}??FFMmhmmm...!{/size}"

        $ p_txell.orgasm += 1
        $ p_txell.closeOrgasm = 0
        $ p_txell.pleasure = -50
        $ p_txell_orgasmByYou = p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm

        $ p_txell.orgasmScene = False

        if p_prot.pos == "69":
            show gensex_69_L_d_mouth sadbiting_Silentx06
            with dissolve

        elif p_prot.pos == "oral":
            show gensex_oral_m_frontHead_exp_eyes 08
            show gensex_oral_m_frontHead_exp_iris front08
            show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx10
            show gensex_oral_m_frontHead_exp_eyebrows sadx06
            with dissolve

        n "Mordi??ndose el labio con suma sugerencia."

        if p_prot.pos == "69":
            show gensex_69_L_d_mouth happybiting_Silentx06
            with dissolve

        elif p_prot.pos == "oral":
            show gensex_oral_m_frontHead_exp_eyes 08
            show gensex_oral_m_frontHead_exp_iris front08
            show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx09
            show gensex_oral_m_frontHead_exp_eyebrows sadx03
            with dissolve

        tx "MMmmmmmfhhhmm...."

###################
        if p_didac.action == "cunnilingus_done_p_txell":
            $ p_didac_cunnilingus_p_txell_orgasm += 1

###################
        #if p_prot.action == "cunnilingus_done":
        if FuckM_Start_Cond == False:

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happy_Talkingx04
            elif p_prot.pos == "oral":
                show gensex_oral_m_frontHead_exp_eyes 05
                show gensex_oral_m_frontHead_exp_iris front05
                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                show gensex_oral_m_frontHead_exp_eyebrows sadx02
            with dissolve

            if p_girl_active.orgasm == 1:

                tx "??Ser?? posible...?"

            elif p_girl_active.orgasm == 2:

                tx "No me lo puedo creer..."

            elif p_girl_active.orgasm == 3:

                tx "????En serio?!"

            elif p_girl_active.orgasm >= 4:

                tx "??Bendigo la madre que te pari??!"

###################
            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happy_Talkingx06
            elif p_prot.pos == "oral":
                show gensex_oral_m_frontHead_exp_eyes 04
                show gensex_oral_m_frontHead_exp_iris front04
                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx07
                show gensex_oral_m_frontHead_exp_eyebrows sadx03
            with dissolve

            if p_girl_active.orgasm == 1:

                tx "Parece que despu??s de todo no se te da tan mal..."

            elif p_girl_active.orgasm == 2:

                tx "??Has conseguido que tenga dos orgasmos!"

            elif p_girl_active.orgasm == 3:

                tx "??Ya llevo tres orgasmos!"

            elif p_girl_active.orgasm >= 4:

                tx "??No s?? ni cuantos orgasmos llevo ya!"


###################

            if p_prot.pos == "oral":

                show gensex_oral_m_frontHead_exp_eyes 05
                show gensex_oral_m_frontHead_exp_iris front05
                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                with dissolve

                tx "Y al final me he corrido estando de rodillas..."

                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth happybiting_Silentx04
                show gensex_oral_m_frontHead_exp_eyebrows sadx02
                with dissolve

                tx "Hmmm..."

###################
            #if p_girl_active.orgasm > 1 and p_prot_NotJustMasturbate_with_p_txell == False:
            if p_didac_cunnilingus_p_txell_orgasm == 0:

                if p_prot.pos == "69":
                    show gensex_69_L_d_mouth happy_Talkingx05
                elif p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris down05
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                    show gensex_oral_m_frontHead_exp_eyebrows sadx03
                with dissolve

                tx "Y solo has usado tu lengua..."

            else:

                if p_prot.pos == "69":
                    show gensex_69_L_d_mouth happy_Talkingx04
                elif p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 03
                    show gensex_oral_m_frontHead_exp_iris front03
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows sadx01
                with dissolve

                tx "Bueno,"

                if p_prot.pos == "69":
                    show gensex_69_L_d_mouth happy_Talkingx05
                elif p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                with dissolve


                if p_didac_cunnilingus_p_txell_orgasm == 1:

                    tx "en realidad uno de ellos ha sido gracias a D??dac..."

                else:

                    tx "en realidad [p_didac_cunnilingus_p_txell_orgasm] de ellos han sido gracias a D??dac..."

                if p_prot.pos == "69":
                    show gensex_69_L_d_mouth happy_Talkingx03
                elif p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx003
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                with dissolve


                if p_didac_cunnilingus_p_txell_orgasm > (p_girl_active.orgasm - p_didac_cunnilingus_p_txell_orgasm):

                    tx "Te lleva algo de ventaja..."

                elif p_didac_cunnilingus_p_txell_orgasm == (p_girl_active.orgasm - p_didac_cunnilingus_p_txell_orgasm):

                    tx "Est??is empatados..."

                    if p_prot.pos == "69":
                        show gensex_69_L_d_mouth happy_Talkingx04
                    elif p_prot.pos == "oral":
                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows sadx01
                    with dissolve


                    tx "Tendr??s que mejorar un poco si no quieres que te compare con D??dac..."


###################
            
            if p_girl_active.orgasm - p_didac_cunnilingus_p_txell_orgasm <= 1:

                if p_prot.pos == "69":
                    show gensex_69_L_d_mouth happy_Talkingx03
                elif p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx03
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                with dissolve

                tx "Espero que no me decepciones..."

            elif p_girl_active.orgasm - p_didac_cunnilingus_p_txell_orgasm == 2:

                if p_prot.pos == "69":
                    show gensex_69_L_d_mouth happy_Talkingx06
                elif p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx08
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                with dissolve

                tx "Me sorprendes [protname]..."

            elif p_girl_active.orgasm - p_didac_cunnilingus_p_txell_orgasm == 3:

                if p_prot.pos == "69":
                    show gensex_69_L_d_mouth happy_Talkingx04
                elif p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 03
                    show gensex_oral_m_frontHead_exp_iris front03
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                with dissolve

                tx "Me tienes sin palabras..."

            elif p_girl_active.orgasm - p_didac_cunnilingus_p_txell_orgasm >= 4:

                if p_prot.pos == "69":
                    show gensex_69_L_d_mouth happy_Talkingx06
                elif p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 01
                    show gensex_oral_m_frontHead_exp_iris front01
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx07
                    show gensex_oral_m_frontHead_exp_eyebrows sadx01
                with dissolve

                tx "Realmente has superado mis expectativas..."

            
###################

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happybiting_Silentx04
            elif p_prot.pos == "oral":
                show gensex_oral_m_frontHead_exp_eyes 05
                show gensex_oral_m_frontHead_exp_iris front05
                show gensex_oral_m_frontHead_exp_mouth happybiting_Silentx04
                show gensex_oral_m_frontHead_exp_eyebrows sadx02
            with dissolve


            if p_girl_active.orgasm - p_didac_cunnilingus_p_txell_orgasm <= 0:

                pt "La madre que la..."

            elif p_girl_active.orgasm - p_didac_cunnilingus_p_txell_orgasm == 1:

                pt "??Es que no est?? nunca contenta...?"

            elif p_girl_active.orgasm - p_didac_cunnilingus_p_txell_orgasm == 2:

                pt "Pues esp??rate y ver??s..."

            elif p_girl_active.orgasm - p_didac_cunnilingus_p_txell_orgasm == 3:

                if p_prot.action == "cunnilingus_done":
                    p "Meg alego gue geconozgas el talento agjeno."
                else:
                    p "Me alegro que reconozcas el talento ajeno."

            elif p_girl_active.orgasm - p_didac_cunnilingus_p_txell_orgasm >= 4:

                if p_prot.action == "cunnilingus_done":
                    p "A??gn no he tegminado."
                else:
                    p "A??n no he terminado."

    call afternight05_Pedrera_Sex_Check_closeOrgasm_Check

    #############################################
#############################################

    if p_prot.orgasmScene == True:

        if p_prot_NotJustMasturbate_with_p_didac == True or p_prot_NotJustMasturbate_with_p_txell == True:
            $ p_prot_NotJustMasturbate_with_p_any = True
        if p_prot_NotJustMasturbate_with_p_didac == True and p_prot_NotJustMasturbate_with_p_txell == True:
            $ p_prot_NotJustMasturbate_with_p_both = True

        $ p_prot.orgasmScene = False

        #$ debug ("Protagonist Cum// Close to Orgasm is: [p_prot.closeOrgasm] / Maximum Pleasure is: [p_prot.max_pleasure[p_prot.orgasm]]")

        ####

        show closetocum_mc

        if music_play != "nonstop":
            play music "audio/music/kevinmacleod/nonstop.ogg" fadein 2.0 fadeout 3.0
            $ music_play = "nonstop"

        # if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell" and ped_sex_general_zoom_Cond != "crotch":
        #     show gensex_missionary_n_head_exp_eyes 06
        #     show gensex_missionary_n_head_exp_iris front06
        #     show gensex_missionary_n_head_exp_eyebrows sadx04
        #     show gensex_missionary_n_head_exp_mouth happybiting_Silentx05
        #     with dissolve

        if p_prot.orgasm == 0:

            pt "Dios..."

            pt "Ya no puedo m??s."

        elif p_prot.orgasm == 1:

            pt "Mierda..."

            pt "Ya ser?? mi segunda vez..."

        elif p_prot.orgasm == 2:

            pt "Mierda..."

            pt "ya no puedo m??s..."

            show screen Points()
            hide screen Points_PedreraSex

            #scene day05
            #with fade
        else:

            aj "THIS SHOULDN'T BE READABLE 964958+6"

        #### DIDAC

        if p_active == "p_didac":

            if p_prot.pos == "doggy":
                $ ped_sex_general_zoom_Cond = "face"
                call pedrera_sex_p_general_talk
                with fade_short

            elif p_prot.pos == "oral":
                if p_didac.action == "titwank_done":
                    $ ped_sex_general_expression_Cond = "talk"
                    $ ped_sex_general_action_Cond = "talk"
                    call pedrera_sex_p_general_talk

            elif p_prot.pos == "69":
                $ ped_sex_general_expression_Cond = "talk"
                $ ped_sex_general_action_b_Cond = "69b_00_00b"
                call pedrera_sex_p_general_talk

            show closetocum_mc

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell" and ped_sex_general_zoom_Cond == "crotch":
                $ ped_sex_general_zoom_Cond = ""
                $ ped_sex_general_expression_Cond = "talk"
                $ ped_sex_general_action_Cond = "talk"
                call pedrera_sex_p_general_talk

            if p_didac.orgasm == 0:

                if p_prot.pos == "oral":

                    $ ped_sex_blow_MChand = "off"
                    $ ped_sex_general_expression_Cond = "talk"
                    $ ped_sex_general_action_Cond = "talk" # blowbjob slow
                    call pedrera_sex_p_general_talk

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx16
                    show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                    with dissolve

                elif p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils front01
                    show gensex_missionary_d_head_exp_eyebrows angryx03
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx22
                    with dissolve

                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx10
                    if p_prot.b_action in ["blowjob_received", "blowjobDeep_received"]:
                        with Dissolve(0.5)
                    else:
                        with dissolve


                d "{size=30}????YA TE VAS A CORRER?!{/size}"

            elif p_didac.action == "blowjob_done" or p_didac.orgasm == 1:

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx13
                    show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                    with dissolve

                elif p_prot.pos == "missionary":

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils front01
                        show gensex_missionary_d_head_exp_eyebrows surprisex01
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx14
                        with dissolve

                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx08
                    with dissolve

                d "????Ya te vas a correr?!"

            elif p_didac.orgasm == 2:

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                    show gensex_oral_d_frontHead_exp_eyebrows sadx02
                    with dissolve

                elif p_prot.pos == "missionary":
                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils front01
                        show gensex_missionary_d_head_exp_eyebrows sadx01
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx08
                        with dissolve

                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx05
                    with dissolve

                d "Te vas a correr..."

                extend" ??Verdad?"

            elif p_didac.orgasm == 3:

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth happy_Talkingx05
                    show gensex_oral_d_frontHead_exp_eyebrows serious
                    with dissolve

                elif p_prot.pos == "missionary":
                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 02
                        show gensex_missionary_d_head_exp_pupils front02
                        show gensex_missionary_d_head_exp_eyebrows serious
                        show gensex_missionary_d_head_exp_mouth happy_Talkingx05
                        with dissolve

                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth happy_Talkingx05
                    with dissolve

                d "Por fin te corres..."

            elif p_didac.orgasm >= 4:

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth happy_Talkingx07
                    show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                    with dissolve

                elif p_prot.pos == "missionary":
                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils front04
                        show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                        show gensex_missionary_d_head_exp_mouth happy_Talkingx07
                        with dissolve

                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth happy_Talkingx07
                    with dissolve

                d "La madre que te pari??..."

                extend " ya era hora de que te corrieras t?? tambi??n."

            ###

            if p_prot_NotJustMasturbate_with_p_didac == False:

                $ p_prot.pos = "oral"

            if p_prot.pos == "oral":

                if p_prot_NotJustMasturbate_with_p_didac == False:

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "??Pero si solo te la has estado machacando!"

                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris front03
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    d "??Podr??as haber...!"

                elif p_didac.action == "blowjob_done":

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    d "??Pero no lo hagas mientras te la estoy chupando!"

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx16
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    d "??No quiero que te corras en mi boca!"

                else:

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    d "??Al menos espera a ponerme a cuatro patas!"

            else:

                if p_didac.orgasm <= 1:

                    if p_prot.pos == "oral":

                        show gensex_oral_d_frontHead_exp_eyes 02
                        show gensex_oral_d_frontHead_exp_iris front02
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                        show gensex_oral_d_frontHead_exp_eyebrows angryx03
                        with dissolve

                    elif p_prot.pos == "missionary":
                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 03
                            show gensex_missionary_d_head_exp_pupils front03
                            show gensex_missionary_d_head_exp_eyebrows angryx05
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx19
                            with dissolve

                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx11
                        with dissolve

                    d "????No pod??as aguantar un poco m??s?!"

                    if p_txell.seal == "empty":

                        if p_prot.pos == "oral":
                            show gensex_oral_d_frontHead_exp_eyes 01
                            show gensex_oral_d_frontHead_exp_iris right01
                            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx13
                            show gensex_oral_d_frontHead_exp_eyebrows angryx02
                            with dissolve

                        elif p_prot.pos == "missionary":
                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 01
                                show gensex_missionary_d_head_exp_pupils right01
                                show gensex_missionary_d_head_exp_eyebrows angryx02
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx18
                                with dissolve

                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx09
                            with dissolve

                        d "??Tendr??a que haber empezado la tetuda!"

                        if p_prot.pos == "oral":
                            show gensex_oral_d_frontHead_exp_eyes 04
                            show gensex_oral_d_frontHead_exp_iris right04
                            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                            show gensex_oral_d_frontHead_exp_eyebrows angryx03
                            with dissolve

                        elif p_prot.pos == "missionary":
                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 04
                                show gensex_missionary_d_head_exp_pupils front04
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx19
                                with dissolve

                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx008
                            with dissolve

                        d "Seguro que entonces hubieras aguantado m??s..."

                        if p_prot.pos == "oral":
                            show gensex_oral_d_frontHead_exp_eyes 02
                            show gensex_oral_d_frontHead_exp_iris right02
                            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
                            show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                            with dissolve

                        elif p_prot.pos == "missionary":
                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 02
                                show gensex_missionary_d_head_exp_pupils right02
                                show gensex_missionary_d_head_exp_eyebrows angryx01
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                                with dissolve

                        elif p_prot.pos == "doggy":
                            $ Pedrera_char_Cond = "TxellClose_b"
                            call Pedrera_char_lab

                            show m_exp_mouth happy_Talkingx05
                            show m_exp_eyes 03
                            show m_exp_piris front03
                            show m_exp_eyebrows angryx03
                            with fade_short

                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx06
                            with dissolve

                        tx "Has sido t?? quien ha insistido en ser la primera."

                        if p_prot.pos == "oral":
                            show gensex_oral_d_frontHead_exp_eyes 04
                            show gensex_oral_d_frontHead_exp_iris left04
                            show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
                            show gensex_oral_d_frontHead_exp_eyebrows angryx04
                            with dissolve

                        elif p_prot.pos == "missionary":
                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 04
                                show gensex_missionary_d_head_exp_pupils right04
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sad_Silentx07
                                with dissolve

                        elif p_prot.pos == "doggy":
                            show m_exp_mouth happy_Silentx04
                            show m_exp_eyes 05
                            show m_exp_piris front05
                            show m_exp_eyebrows angryx02
                            with dissolve

                            pause 0.2

                            $ ped_sex_general_zoom_Cond = "face"
                            call pedrera_sex_p_general_talk
                            with fade_short

                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx09
                            with dissolve

                        d "..."

                        if p_prot.pos == "oral":
                            show gensex_oral_d_frontHead_exp_eyes 00
                            show gensex_oral_d_frontHead_exp_iris right00
                            show gensex_oral_d_frontHead_exp_mouth sad_Silentx04
                            show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                            with dissolve

                        elif p_prot.pos == "missionary":
                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 01
                                show gensex_missionary_d_head_exp_pupils right01
                                show gensex_missionary_d_head_exp_eyebrows surprisex01
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx08
                                with dissolve

                        elif p_prot.pos == "doggy":
                            $ Pedrera_char_Cond = "TxellClose_b"
                            call Pedrera_char_lab

                            show m_exp_mouth happy_Talkingx06
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            show m_exp_eyebrows surprisex01
                            with fade_short

                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx08
                            with dissolve

                        tx "Te lo hubieras pensado mejor antes..."

                        if p_prot.pos == "oral":
                            show gensex_oral_d_frontHead_exp_eyes 04
                            show gensex_oral_d_frontHead_exp_iris left04
                            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                            show gensex_oral_d_frontHead_exp_eyebrows angryx03
                            with dissolve

                        elif p_prot.pos == "missionary":
                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 03
                                show gensex_missionary_d_head_exp_pupils left03
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
                                with dissolve

                        elif p_prot.pos == "doggy":
                            show m_exp_mouth happy_Silentx06
                            show m_exp_eyes 05
                            show m_exp_piris front05
                            show m_exp_eyebrows angryx02
                            with dissolve

                            pause 0.2

                            $ ped_sex_general_zoom_Cond = "face"
                            call pedrera_sex_p_general_talk
                            with fade_short

                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx07
                            with dissolve

                        d "Tssk."

                        if p_didac.orgasm == 0:

                            if p_prot.pos == "oral":
                                show gensex_oral_d_frontHead_exp_eyes 04
                                show gensex_oral_d_frontHead_exp_iris right04
                                show gensex_oral_d_frontHead_exp_mouth sad_Silentx04
                                show gensex_oral_d_frontHead_exp_eyebrows angryx01
                                with dissolve

                            elif p_prot.pos == "missionary":
                                if p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 04
                                    show gensex_missionary_d_head_exp_pupils right04
                                    show gensex_missionary_d_head_exp_eyebrows angryx01
                                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                                    with dissolve

                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Silentx05
                                with dissolve

                            tx "Aunque viendo que no has tenido ni un solo orgasmo,"

                            if p_prot.pos == "oral":
                                show gensex_oral_d_frontHead_exp_eyes 03
                                show gensex_oral_d_frontHead_exp_iris right03
                                show gensex_oral_d_frontHead_exp_mouth sad_Silentx03
                                show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                                with dissolve

                            elif p_prot.pos == "missionary":
                                if p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 03
                                    show gensex_missionary_d_head_exp_pupils right03
                                    show gensex_missionary_d_head_exp_eyebrows surprisex01
                                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx07
                                    with dissolve

                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Silentx04
                                with dissolve

                            tx "tampoco creo que me vaya a perder nada especial..."

                            if p_prot.pos == "oral":
                                show gensex_oral_d_frontHead_exp_eyes 05
                                show gensex_oral_d_frontHead_exp_iris front05
                                show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
                                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                                with dissolve

                            elif p_prot.pos == "missionary":
                                if p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 05
                                    show gensex_missionary_d_head_exp_pupils front05
                                    show gensex_missionary_d_head_exp_eyebrows angryx03
                                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05
                                    with dissolve



                elif p_didac.orgasm == 2:

                    if p_prot.pos == "missionary":
                        if p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows sadx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                            with dissolve

                    d "??No podr??as haber aguantado un poquito m??s?..."

                    if p_txell.seal == "sealed":

                        if (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) < 2:

                            if p_prot.pos == "missionary":
                                if p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 01
                                    show gensex_missionary_d_head_exp_pupils right01
                                    show gensex_missionary_d_head_exp_eyebrows surprisex01
                                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                                    with dissolve

                            tx "No te quejes,"

                            if (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) == 0:

                                if p_prot.pos == "missionary":
                                    if p_didac.action != "cunnilingus_done_p_txell":
                                        show gensex_missionary_d_head_exp_eyes 04
                                        show gensex_missionary_d_head_exp_pupils right04
                                        show gensex_missionary_d_head_exp_eyebrows serious
                                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05
                                        with dissolve

                                tx "que por lo menos has tenido alg??n orgasmo."

                            elif (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) == 1:

                                if p_prot.pos == "missionary":
                                    if p_didac.action != "cunnilingus_done_p_txell":
                                        show gensex_missionary_d_head_exp_eyes 04
                                        show gensex_missionary_d_head_exp_pupils right04
                                        show gensex_missionary_d_head_exp_eyebrows sadx01
                                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx07
                                        with dissolve

                                tx "que por lo menos has tenido dos..."

                        elif (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) == 2:

                            if p_prot.pos == "missionary":
                                if p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 01
                                    show gensex_missionary_d_head_exp_pupils right01
                                    show gensex_missionary_d_head_exp_eyebrows surprisex01
                                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                                    with dissolve

                            tx "Es curioso que hayas tenido los mismos orgasmos que yo,"

                            if p_prot.pos == "missionary":
                                if p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 03
                                    show gensex_missionary_d_head_exp_pupils right03
                                    show gensex_missionary_d_head_exp_eyebrows serious
                                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx03
                                    with dissolve

                            tx "pensaba que contigo se se lo trabar??a m??s,"

                            if p_prot.pos == "missionary":
                                if p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 04
                                    show gensex_missionary_d_head_exp_pupils right04
                                    show gensex_missionary_d_head_exp_eyebrows sadx03
                                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx08
                                    with dissolve

                            tx "al ser la segunda vez..."

                        elif (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) > 2:

                            if p_prot.pos == "missionary":
                                if p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 04
                                    show gensex_missionary_d_head_exp_pupils right04
                                    show gensex_missionary_d_head_exp_eyebrows sadx04
                                    show gensex_missionary_d_head_exp_mouth happybiting_Silentx05
                                    with dissolve

                            tx "Es curioso que se lo haya trabajado m??s conmigo que contigo,"

                            if p_prot.pos == "missionary":
                                if p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 05
                                    show gensex_missionary_d_head_exp_pupils right05
                                    show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                                    show gensex_missionary_d_head_exp_mouth happybiting_Silentx08
                                    with dissolve

                            tx "??Por qu?? ser??...?"

                    else:

                        if p_prot.pos == "missionary":
                            if p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 02
                                show gensex_missionary_d_head_exp_pupils right02
                                show gensex_missionary_d_head_exp_eyebrows normal
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                                with dissolve

                        tx "Dos orgasmos tampoco es que sean muchos,"

                        extend " pero es mejor que nada."

                        if FuckM_Start_Cond:

                            if p_prot.pos == "missionary":
                                if p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 04
                                    show gensex_missionary_d_head_exp_pupils right04
                                    show gensex_missionary_d_head_exp_eyebrows suspiciousx01
                                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx07
                                    with dissolve

                            tx "Habr?? que ver qu?? consigue hacer conmigo..."

                    if p_prot.pos == "missionary":
                        if p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows angryx01
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx08
                            with dissolve

                    d "Tskk..."

                    if p_prot.pos == "missionary":
                        if p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx01
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx004
                            with dissolve

                    d "Esperaba disfrutarlo un poco m??s..."

                    if p_prot.pos == "missionary":
                        if p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows sadx02
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
                            with dissolve

                elif p_didac.orgasm == 3:

                    $ ped_sex_general_zoom_Cond = "face"
                    call pedrera_sex_p_general_talk

                    $ debug ("Didac Had 3 orgasms before you finished with her.")

                    if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":

                        $ Pedrera_char_Cond = "TxellSuperClose_show"
                        call Pedrera_char_lab

                    else:

                        $ Pedrera_char_Cond = "TxellClose_b_show"
                        call Pedrera_char_lab

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows sadx01
                    with fade_short

                    tx "Has conseguido que tenga tres orgasmos..."

                    show m_exp_mouth happy_Talkingx07
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows sadx02
                    with dissolve

                    tx "Bueno,"

                    tx "supongo que tampoco se te puede pedir demasiado."

                    show m_exp_mouth happy_Silentx04
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows serious
                    with dissolve

                    $ Pedrera_char_Cond = "p_nobody"
                    call Pedrera_char_lab

                    if p_txell.seal == "sealed":

                        if (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) <= 3:

                            if (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) == 0:

                                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 04
                                    show gensex_missionary_d_head_exp_pupils right04
                                    show gensex_missionary_d_head_exp_eyebrows angryx02
                                    show gensex_missionary_d_head_exp_mouth happy_Talkingx06
                                    with dissolve

                                d "??Lo dices por envidia!"

                                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 05
                                    show gensex_missionary_d_head_exp_pupils right05
                                    show gensex_missionary_d_head_exp_eyebrows angryx01
                                    show gensex_missionary_d_head_exp_mouth happy_Talkingx07
                                    with dissolve

                                d "Ya que t?? no has tenido ni un solo orgasmo."

                                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 05
                                    show gensex_missionary_d_head_exp_pupils right05
                                    show gensex_missionary_d_head_exp_eyebrows angryx02
                                    show gensex_missionary_d_head_exp_mouth happy_Silentx06
                                    with dissolve

                            elif (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) == 1:

                                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 04
                                    show gensex_missionary_d_head_exp_pupils right04
                                    show gensex_missionary_d_head_exp_eyebrows angryx02
                                    show gensex_missionary_d_head_exp_mouth happy_Talkingx06
                                    with dissolve

                                d "Te picas porque solo has tenido un orgasmo,"

                                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 05
                                    show gensex_missionary_d_head_exp_pupils right05
                                    show gensex_missionary_d_head_exp_eyebrows angryx03
                                    show gensex_missionary_d_head_exp_mouth happy_Talkingx08
                                    with dissolve

                                d "??verdad?"

                                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 05
                                    show gensex_missionary_d_head_exp_pupils right05
                                    show gensex_missionary_d_head_exp_eyebrows angryx02
                                    show gensex_missionary_d_head_exp_mouth happy_Silentx06
                                    with dissolve

                            elif (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) == 2:

                                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 03
                                    show gensex_missionary_d_head_exp_pupils right03
                                    show gensex_missionary_d_head_exp_eyebrows normal
                                    show gensex_missionary_d_head_exp_mouth sad_Talkingx004
                                    with dissolve

                                d "Contigo solo ha tenido dos orgasmos..."

                                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 04
                                    show gensex_missionary_d_head_exp_pupils right04
                                    show gensex_missionary_d_head_exp_eyebrows sadx01
                                    show gensex_missionary_d_head_exp_mouth happy_Talkingx04
                                    with dissolve

                                d "Que pena,"

                                extend " ??verdad?"

                                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 05
                                    show gensex_missionary_d_head_exp_pupils right05
                                    show gensex_missionary_d_head_exp_eyebrows angryx02
                                    show gensex_missionary_d_head_exp_mouth happy_Silentx06
                                    with dissolve

                            elif (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) == 3:

                                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 03
                                    show gensex_missionary_d_head_exp_pupils right03
                                    show gensex_missionary_d_head_exp_eyebrows angryx02
                                    show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                                    with dissolve

                                d "??Si has tenido los mismos orgasmos que yo!"

                                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 04
                                    show gensex_missionary_d_head_exp_pupils right04
                                    show gensex_missionary_d_head_exp_eyebrows suspiciousx01
                                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx03
                                    with dissolve


                            if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":

                                $ Pedrera_char_Cond = "TxellSuperClose_show"
                                call Pedrera_char_lab

                            else:

                                $ Pedrera_char_Cond = "TxellClose_b_show"
                                call Pedrera_char_lab

                            show m_exp_mouth sadbiting_Silentx04
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            show m_exp_eyebrows angryx01
                            with fade_short

                            tx "..."

                            show m_exp_mouth sadbiting_Silentx06
                            show m_exp_eyes 05
                            show m_exp_piris right05
                            show m_exp_eyebrows angryx03
                            with dissolve

                            pause 0.2

                            $ Pedrera_char_Cond = "p_nobody"
                            call Pedrera_char_lab

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 03
                                show gensex_missionary_d_head_exp_pupils right03
                                show gensex_missionary_d_head_exp_eyebrows angryx01
                                show gensex_missionary_d_head_exp_mouth happy_Talkingx08
                                with fade_short

                            d "??No te hagas la sobrada ahora!"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 04
                                show gensex_missionary_d_head_exp_pupils right04
                                show gensex_missionary_d_head_exp_eyebrows angryx02
                                show gensex_missionary_d_head_exp_mouth happybiting_Silentx07
                                with dissolve

                            pause 0.2

                            if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":

                                $ Pedrera_char_Cond = "TxellSuperClose_show"
                                call Pedrera_char_lab

                            else:

                                $ Pedrera_char_Cond = "TxellClose_b_show"
                                call Pedrera_char_lab

                            show m_exp_mouth sad_Silentx05
                            show m_exp_eyes 08
                            show m_exp_piris front08
                            show m_exp_eyebrows angryx03
                            with fade_short

                            tx "..."

                            show m_exp_mouth sadbiting_Silentx04
                            show m_exp_eyes 05
                            show m_exp_piris right05
                            show m_exp_eyebrows angryx02

                            pause 0.2

                            $ Pedrera_char_Cond = "NeusClose_show"
                            call Pedrera_char_lab

                            show neus_exp_mouth sad_Talkingx08
                            $ nteye = 4
                            call neus_exp_tears_tears
                            show neus_exp_iris right04
                            show neus_exp_eyebrows angryx03
                            with fade_short

                            ne "??Os recuerdo que esto no es una competici??n!"

                            show neus_exp_mouth sad_Silentx07
                            $ nteye = 5
                            call neus_exp_tears_tears
                            show neus_exp_iris right05
                            show neus_exp_eyebrows angryx02

                            pause 0.2

                            if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":

                                $ Pedrera_char_Cond = "TxellSuperClose_show"
                                call Pedrera_char_lab

                            else:

                                $ Pedrera_char_Cond = "TxellClose_b_show"
                                call Pedrera_char_lab

                            show m_exp_mouth sad_Silentx03
                            show m_exp_eyes 02
                            show m_exp_piris left02
                            show m_exp_eyebrows sadx01
                            with fade_short

                            tx "..."

                            show m_exp_mouth sadbiting_Silentx04
                            show m_exp_eyes 04
                            show m_exp_piris right04
                            show m_exp_eyebrows sadx03
                            with dissolve

                            pause 0.2

                            $ Pedrera_char_Cond = "p_nobody"
                            call Pedrera_char_lab

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 08
                                show gensex_missionary_d_head_exp_pupils front08
                                show gensex_missionary_d_head_exp_eyebrows sadx01
                                show gensex_missionary_d_head_exp_mouth happybiting_Silentx05
                                with fade_short

                            pause 0.2

                        else:

                            show m_exp_mouth happy_Talkingx05
                            show m_exp_eyes 08
                            show m_exp_piris front08
                            show m_exp_eyebrows surprisex01
                            with dissolve

                            tx "Aunque lo curioso es que yo haya tenido m??s orgasmos que t??."

                            show m_exp_mouth happy_Talkingx04
                            show m_exp_eyes 04
                            show m_exp_piris down04
                            show m_exp_eyebrows normal
                            with dissolve

                            tx "??Por qu?? ser??...?"

                            show m_exp_mouth happy_Silentx06
                            show m_exp_eyes 05
                            show m_exp_piris down05
                            show m_exp_eyebrows angryx02
                            with dissolve

                            pause 0.2

                            $ Pedrera_char_Cond = "p_nobody"
                            call Pedrera_char_lab

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 03
                                show gensex_missionary_d_head_exp_pupils right03
                                show gensex_missionary_d_head_exp_eyebrows serious
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx03
                                with fade_short

                            d "..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 00
                                show gensex_missionary_d_head_exp_pupils right00
                                show gensex_missionary_d_head_exp_eyebrows surprisex02
                                show gensex_missionary_d_head_exp_mouth sad_Silentx04
                                with dissolve

                            tx "Quiz??s eres m??s fr??gida de lo que te imaginas."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 01
                                show gensex_missionary_d_head_exp_pupils right01
                                show gensex_missionary_d_head_exp_eyebrows angryx03
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx12
                                with dissolve

                            d "??O t?? una cerda ninf??mana que no acepta su bisexualidad!"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 02
                                show gensex_missionary_d_head_exp_pupils right02
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth happy_Silentx05
                                with dissolve

                            if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":

                                $ Pedrera_char_Cond = "TxellSuperClose_show"
                                call Pedrera_char_lab

                            else:

                                $ Pedrera_char_Cond = "TxellClose_b_show"
                                call Pedrera_char_lab

                            show m_exp_mouth sad_Silentx03
                            show m_exp_eyes 00
                            show m_exp_piris front00
                            show m_exp_eyebrows surprisex02
                            with fade_short

                            tx "..."

                            show m_exp_mouth sad_Silentx07
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            show m_exp_eyebrows angryx04
                            with dissolve

                            pause 0.2

                            $ Pedrera_char_Cond = "NeusClose_show"
                            call Pedrera_char_lab

                            show neus_exp_mouth sad_Talkingx08
                            $ nteye = 4
                            call neus_exp_tears_tears
                            show neus_exp_iris right04
                            show neus_exp_eyebrows angryx03
                            with fade_short

                            ne "????Quer??is dejarlo ya?!"

                            show neus_exp_mouth sad_Talkingx09
                            $ nteye = 5
                            call neus_exp_tears_tears
                            show neus_exp_iris right05
                            show neus_exp_eyebrows angryx04

                            ne "??Os recuerdo que esto no es una competici??n!"

                            show neus_exp_mouth sad_Silentx04
                            $ nteye = 8
                            call neus_exp_tears_tears
                            show neus_exp_iris front08
                            show neus_exp_eyebrows angryx03

                            pause 0.2

                            $ Pedrera_char_Cond = "p_nobody"
                            call Pedrera_char_lab

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 08
                                show gensex_missionary_d_head_exp_pupils front08
                                show gensex_missionary_d_head_exp_eyebrows sadx01
                                show gensex_missionary_d_head_exp_mouth happybiting_Silentx03
                                with fade_short

                    else:

                        show m_exp_mouth happy_Silentx05
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows angryx01
                        with dissolve

                        tx "Habr?? que ver si consigues lo mismo conmigo."

                        show m_exp_mouth happy_Silentx07
                        show m_exp_eyes 03
                        show m_exp_piris front03
                        show m_exp_eyebrows angryx02
                        with dissolve

                        tx "Aunque me sorprender??a bastante."

                        show m_exp_mouth happy_Silentx05
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows angryx01
                        with dissolve

                        pause 0.2

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils right05
                            show gensex_missionary_d_head_exp_eyebrows angryx01
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                            with fade_short

                elif p_didac.orgasm >= 4:

                    $ ped_sex_general_zoom_Cond = "face"
                    call pedrera_sex_p_general_talk

                    $ debug ("Didac Had more than 3 orgasms before you finished with her.")

                    if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":

                        $ Pedrera_char_Cond = "TxellSuperClose_show"
                        call Pedrera_char_lab

                    else:

                        $ Pedrera_char_Cond = "TxellClose_b_show"
                        call Pedrera_char_lab

                    show m_exp_mouth sad_Talkingx03
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows serious
                    with fade_short

                    tx "Has conseguido que tenga [p_didac.orgasm] orgasmos."

                    if p_txell.seal == "sealed":

                        if (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) == 1:

                            show m_exp_mouth sad_Talkingx06
                            show m_exp_eyes 04
                            show m_exp_piris down04
                            show m_exp_eyebrows suspiciousx02
                            with dissolve

                            tx "Y yo me he tenido que conformar con simplemente uno..."

                            show m_exp_mouth sad_Silentx06
                            show m_exp_eyes 08
                            show m_exp_piris front08
                            show m_exp_eyebrows suspiciousx03
                            with dissolve


                        elif (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) == 2:

                            show m_exp_mouth sad_Talkingx05
                            show m_exp_eyes 04
                            show m_exp_piris down04
                            show m_exp_eyebrows suspiciousx01
                            with dissolve

                            tx "Y yo me he tenido que conformar con dos..."

                            show m_exp_mouth sad_Silentx05
                            show m_exp_eyes 08
                            show m_exp_piris front08
                            show m_exp_eyebrows suspiciousx02
                            with dissolve

                        elif (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) == 3:

                            show m_exp_mouth sad_Talkingx04
                            show m_exp_eyes 04
                            show m_exp_piris down04
                            show m_exp_eyebrows normal
                            with dissolve

                            tx "Y yo me he tenido que conformar con tres..."

                            show m_exp_mouth sad_Silentx04
                            show m_exp_eyes 08
                            show m_exp_piris front08
                            show m_exp_eyebrows suspiciousx01
                            with dissolve

                        if (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) <= 3:

                            if FuckM_Start_Cond:

                                pass

                                # CONDITIONAL depending of if you had sex PASIVE or ACTIVE with her. FOR FUTURE

                            else:

                                pt "??Como si me lo hubiera puesto tan f??cil!"

                            show m_exp_mouth sad_Silentx02
                            show m_exp_eyes 01
                            show m_exp_piris down01
                            show m_exp_eyebrows surprisex02
                            with dissolve

                            d "Al final ha sido buena idea que empezara contigo."

                            show m_exp_mouth sadbiting_Silentx04
                            show m_exp_eyes 04
                            show m_exp_piris right04
                            show m_exp_eyebrows angryx02
                            with dissolve

                            tx "Pffft..."

                            show m_exp_mouth sadbiting_Silentx05
                            show m_exp_eyes 05
                            show m_exp_piris right05
                            show m_exp_eyebrows sdx01
                            with dissolve

                        else:

                            if (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) > p_didac.orgasm:

                                show m_exp_mouth happy_Talkingx05
                                show m_exp_eyes 03
                                show m_exp_piris down03
                                show m_exp_eyebrows angryx02
                                with dissolve

                                tx "Lo m??s curioso es que yo haya tenido m??s que t??..."

                                show m_exp_mouth happy_Silentx05
                                show m_exp_eyes 05
                                show m_exp_piris down05
                                show m_exp_eyebrows angryx03
                                with dissolve

                                pause 0.2

                                $ Pedrera_char_Cond = "p_nobody"
                                call Pedrera_char_lab

                                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 08
                                    show gensex_missionary_d_head_exp_pupils front08
                                    show gensex_missionary_d_head_exp_eyebrows angryx05
                                    show gensex_missionary_d_head_exp_mouth sad_Silentx08
                                    with fade_short

                                d "..."

                                $ Pedrera_char_Cond = "NeusClose_show"
                                call Pedrera_char_lab

                                show neus_exp_mouth sad_Talkingx08
                                $ nteye = 4
                                call neus_exp_tears_tears
                                show neus_exp_iris front04
                                show neus_exp_eyebrows angryx03
                                with hpunch

                                ne "??Os recuerdo que no es una competici??n!"

                                show neus_exp_mouth sad_Silentx05
                                $ nteye = 5
                                call neus_exp_tears_tears
                                show neus_exp_iris right05
                                show neus_exp_eyebrows angryx04
                                with dissolve

                                pause 0.2

                                if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":

                                    $ Pedrera_char_Cond = "TxellSuperClose_show"
                                    call Pedrera_char_lab

                                else:

                                    $ Pedrera_char_Cond = "TxellClose_b_show"
                                    call Pedrera_char_lab

                                show m_exp_mouth sadbiting_Silentx03
                                show m_exp_eyes 05
                                show m_exp_piris right05
                                show m_exp_eyebrows sadx01
                                with dissolve

                                tx "..."

                            elif (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) == p_didac.orgasm:

                                show m_exp_mouth sad_Talkingx04
                                show m_exp_eyes 05
                                show m_exp_piris down05
                                show m_exp_eyebrows suspiciousx02
                                with dissolve

                                tx "Has tenido exactamente los mismos que yo..."

                                show m_exp_mouth sad_Talkingx03
                                show m_exp_eyes 08
                                show m_exp_piris front08
                                show m_exp_eyebrows sadx02
                                with dissolve

                                tx "Es hasta curioso..."

                                show m_exp_mouth happybiting_Silentx03
                                show m_exp_eyes 04
                                show m_exp_piris front04
                                show m_exp_eyebrows serious
                                with dissolve

                                pause 0.2

                                $ Pedrera_char_Cond = "p_nobody"
                                call Pedrera_char_lab

                                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 08
                                    show gensex_missionary_d_head_exp_pupils front08
                                    show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                                    with fade_short

                                d "..."

                            else:

                                show m_exp_mouth sad_Silentx02
                                show m_exp_eyes 01
                                show m_exp_piris down01
                                show m_exp_eyebrows surprisex01
                                with dissolve

                                d "Por lo menos he tenido m??s que t??."

                                show m_exp_mouth sad_Silentx06
                                show m_exp_eyes 05
                                show m_exp_piris down05
                                show m_exp_eyebrows angryx02
                                with dissolve

                                tx "..."

                                show m_exp_mouth sad_Talkingx05
                                show m_exp_eyes 08
                                show m_exp_piris front08
                                show m_exp_eyebrows suspiciousx02
                                with dissolve

                                tx "Tampoco es una competici??n."

                                d "Eso suelen decir los perdedores..."

                                show m_exp_mouth sadbiting_Silentx05
                                show m_exp_eyes 01
                                show m_exp_piris down01
                                show m_exp_eyebrows angryx03
                                with dissolve

                                tx "..."

                                show m_exp_mouth sad_Silentx07
                                show m_exp_eyes 05
                                show m_exp_piris right05
                                show m_exp_eyebrows angryx05
                                with dissolve

                    else:

                        show m_exp_mouth sad_Talkingx05
                        show m_exp_eyes 08
                        show m_exp_piris front08
                        show m_exp_eyebrows surprisex01
                        with dissolve

                        tx "Sinceramente no me lo esperaba."

                        show m_exp_mouth happy_Talkingx04
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows serious
                        with dissolve

                        tx "Habr?? que ver si eres capaz de hacer lo mismo conmigo."

                        show m_exp_mouth happy_Silentx04
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows angryx01
                        with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

            $ ped_sex_general_zoom_Cond = "face"
            call pedrera_sex_p_general_talk

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 08
                show gensex_missionary_d_head_exp_pupils front08
                show gensex_missionary_d_head_exp_eyebrows serious
                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx03
                with dissolve

        #### TXELL

        if p_active == "p_txell":

            if p_prot.pos == "doggy":
                $ ped_sex_general_zoom_Cond = "face"
                call pedrera_sex_p_general_talk
                with fade_short

            if p_prot.pos == "oral":
                $ ped_sex_general_expression_Cond = "talk"
                if p_prot.action == "titwank_received":
                    $ ped_sex_general_action_Cond = "ob00_00b"
                else:
                    $ ped_sex_general_action_Cond = "o00_00"
                call pedrera_sex_p_general_talk

            elif p_prot.pos == "69":
                $ ped_sex_general_expression_Cond = "talk"
                $ ped_sex_general_action_b_Cond = "69b_00_00b"
                call pedrera_sex_p_general_talk

            show closetocum_mc

            if p_prot_NotJustMasturbate_with_p_txell == False:

                if p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 03
                    show gensex_oral_m_frontHead_exp_iris front03
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                else:
                    show gensex_69_L_d_mouth happy_Talkingx04
                if p_prot.pos != "doggy":
                    with fade_short

                tx "Al final solo has usado tus manos..."

                if p_didac.seal == "sealed": 

                    if p_prot_NotJustMasturbate_with_p_didac == False:

                        if p_prot.pos == "oral":
                            show gensex_oral_m_frontHead_exp_eyes 03
                            show gensex_oral_m_frontHead_exp_iris right03
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                            show gensex_oral_m_frontHead_exp_eyebrows normal
                        else:
                            show gensex_69_L_d_mouth sad_Talkingx003
                        if p_prot.pos != "doggy":
                            with dissolve

                        tx "Incluso con D??dac."

                    elif p_didac.seal == "sealed":

                        if p_prot.pos == "oral":
                            show gensex_oral_m_frontHead_exp_eyes 03
                            show gensex_oral_m_frontHead_exp_iris right03
                            show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                            show gensex_oral_m_frontHead_exp_eyebrows sadx02
                        with dissolve

                        tx "Aunque con D??dac no hayas soportado la tentaci??n..."

                    if p_prot_NotJustMasturbate_with_p_any == False:

                        if p_prot.pos == "oral":
                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                        with dissolve

                        tx "Me alegra ver que has sido fiel a tu palabra con Neus."

                else:

                    if p_prot.pos == "oral":
                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows serious
                    with dissolve

                    tx "Aunque habr?? que ver qu?? haces con D??dac..."

            else:

                if p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                else:
                    show gensex_69_L_d_mouth sad_Talkingx04
                if p_prot.pos != "doggy":
                    with fade_short

                tx "??As?? que este es tu l??mite?..."

                if (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) <= 0:

                    if p_prot.pos == "oral":
                        show gensex_oral_m_frontHead_exp_eyes 08
                        show gensex_oral_m_frontHead_exp_iris front08
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                    else:
                        show gensex_69_L_d_mouth sad_Talkingx03
                    if p_prot.pos != "doggy":
                        with dissolve

                    tx "No s?? por qu?? me esperaba algo m??s de ti..."

                elif (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) == 1:

                    if p_prot.pos == "oral":
                        show gensex_oral_m_frontHead_exp_eyes 05
                        show gensex_oral_m_frontHead_exp_iris front05
                        show gensex_oral_m_frontHead_exp_mouth happy_Talkingx02
                        show gensex_oral_m_frontHead_exp_eyebrows sadx02
                    else:
                        show gensex_69_L_d_mouth happy_Talkingx03
                    if p_prot.pos != "doggy":
                        with dissolve

                    tx "Por lo menos me has dado un orgasmo..."

                    if p_txell.vaginal_received == 0 and p_txell.anal_received == 0:

                        if p_prot.pos == "oral":
                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth happy_Talkingx03
                            show gensex_oral_m_frontHead_exp_eyebrows sadx03
                        else:
                            show gensex_69_L_d_mouth happy_Talkingx04
                        if p_prot.pos != "doggy":
                            with dissolve

                        tx "Supongo que tiene su m??rito..."

                elif (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm)  == 2:

                    if p_prot.pos == "oral":
                        show gensex_oral_m_frontHead_exp_eyes 08
                        show gensex_oral_m_frontHead_exp_iris front08
                        show gensex_oral_m_frontHead_exp_mouth happy_Talkingx03
                        show gensex_oral_m_frontHead_exp_eyebrows sadx02
                    else:
                        show gensex_69_L_d_mouth happy_Talkingx05
                    if p_prot.pos != "doggy":
                        with dissolve

                    tx "Por lo menos me has dado dos orgasmos,"

                    if p_prot.pos == "oral":
                        show gensex_oral_m_frontHead_exp_eyes 05
                        show gensex_oral_m_frontHead_exp_iris front05
                        show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows sadx03
                    else:
                        show gensex_69_L_d_mouth happy_Talkingx04
                    if p_prot.pos != "doggy":
                        with dissolve

                    tx "reconozco que es m??s de lo que me esperaba..."

                elif (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) == 3:

                    if p_prot.pos == "oral":
                        show gensex_oral_m_frontHead_exp_eyes 03
                        show gensex_oral_m_frontHead_exp_iris front03
                        show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                        show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                    else:
                        show gensex_69_L_d_mouth happy_Talkingx05
                    if p_prot.pos != "doggy":
                        with dissolve

                    tx "Me has dado tres orgasmos..."

                    if p_prot.pos == "oral":
                        show gensex_oral_m_frontHead_exp_eyes 05
                        show gensex_oral_m_frontHead_exp_iris front05
                        show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                        show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                    else:
                        show gensex_69_L_d_mouth happy_Talkingx04
                    if p_prot.pos != "doggy":
                        with dissolve

                    tx "es bastante m??s de lo que me esperaba..."

                elif (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) == 4:

                    if p_prot.pos == "oral":
                        show gensex_oral_m_frontHead_exp_eyes 02
                        show gensex_oral_m_frontHead_exp_iris front02
                        show gensex_oral_m_frontHead_exp_mouth happy_Talkingx07
                        show gensex_oral_m_frontHead_exp_eyebrows sadx02
                    else:
                        show gensex_69_L_d_mouth happy_Talkingx06
                    if p_prot.pos != "doggy":
                        with dissolve

                    tx "Has logrado que tenga hasta cuatro orgasmos..."

                    if p_prot.pos == "oral":
                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                        show gensex_oral_m_frontHead_exp_eyebrows sadx04
                    else:
                        show gensex_69_L_d_mouth happy_Talkingx05
                    if p_prot.pos != "doggy":
                        with dissolve

                    tx "Me has sorprendido gratamente [protname]..."

                elif (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) >= 5:

                    if p_prot.pos == "oral":
                        show gensex_oral_m_frontHead_exp_eyes 05
                        show gensex_oral_m_frontHead_exp_iris front05
                        show gensex_oral_m_frontHead_exp_mouth happy_Talkingx07
                        show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                    else:
                        show gensex_69_L_d_mouth happy_Talkingx04
                    if p_prot.pos != "doggy":
                        with dissolve

                    tx "Realmente has sido una caja de sorpresas [protname]..."

                    if p_prot.pos == "oral":
                        show gensex_oral_m_frontHead_exp_eyes 08
                        show gensex_oral_m_frontHead_exp_iris front08
                        show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                        show gensex_oral_m_frontHead_exp_eyebrows sadx03
                    else:
                        show gensex_69_L_d_mouth happy_Talkingx06
                    if p_prot.pos != "doggy":
                        with dissolve

                    tx "Has logrado que tenga hasta [p_txell.orgasm] orgasmos..."

                    if p_prot.pos == "oral":
                        show gensex_oral_m_frontHead_exp_eyes 05
                        show gensex_oral_m_frontHead_exp_iris front05
                        show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                        show gensex_oral_m_frontHead_exp_eyebrows sadx04
                    else:
                        show gensex_69_L_d_mouth happy_Talkingx05
                    if p_prot.pos != "doggy":
                        with dissolve

                    tx "Nunca me hubiera imaginado esto de ti..."

                if (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) > 0 and p_txell.vaginal_received == 0 and p_txell.anal_received == 0:

                    if p_prot.pos == "oral":
                        show gensex_oral_m_frontHead_exp_eyes 08
                        show gensex_oral_m_frontHead_exp_iris front08
                        show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                        show gensex_oral_m_frontHead_exp_eyebrows sadx03
                    else:
                        show gensex_69_L_d_mouth happy_Talkingx06
                    if p_prot.pos != "doggy":
                        with dissolve

                    tx "Especialmente teniendo en cuenta que lo has logrado usando solo la lengua..."

            if p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 02
                    show gensex_oral_m_frontHead_exp_iris down02
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
            else:
                show gensex_69_L_d_mouth sadbiting_Silentx03
            if p_prot.pos != "doggy":
                with dissolve

        jump afternight05_Pedrera_Sex_Cumshot


    return

label afternight05_Pedrera_Sex_Cumshot:

    if p_active == "p_didac":

        if p_didac.orgasm == 0:

            if p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris down01
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx05
                show gensex_oral_d_frontHead_exp_eyebrows surprisex02

            elif p_prot.pos == "missionary":
                if p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils down01
                    show gensex_missionary_d_head_exp_eyebrows surprisex01
                    show gensex_missionary_d_head_exp_mouth sad_Silentx05


        elif p_didac.orgasm == 1:

            if p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris down01
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx03
                show gensex_oral_d_frontHead_exp_eyebrows surprisex01

            elif p_prot.pos == "missionary":
                if p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils down01
                    show gensex_missionary_d_head_exp_eyebrows surprisex01
                    show gensex_missionary_d_head_exp_mouth sad_Silentx03

        elif p_didac.orgasm == 2:

            if p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris down02
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows sadx01

            elif p_prot.pos == "missionary":
                if p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils down02
                    show gensex_missionary_d_head_exp_eyebrows sadx01
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04

        elif p_didac.orgasm == 3:

            if p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris down02
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
                show gensex_oral_d_frontHead_exp_eyebrows sadx02

            elif p_prot.pos == "missionary":
                if p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils down02
                    show gensex_missionary_d_head_exp_eyebrows sadx02
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05

        elif p_didac.orgasm >= 4:

            if p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris down03
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx07
                show gensex_oral_d_frontHead_exp_eyebrows sadx04

            elif p_prot.pos == "missionary":
                if p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 03
                    show gensex_missionary_d_head_exp_pupils down03
                    show gensex_missionary_d_head_exp_eyebrows sadx04
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx07

        if p_prot.pos == "doggy":
            $ ped_sex_general_zoom_Cond = "crotch"
            call pedrera_sex_p_general_talk

    show closetocum_mc zorder 99
    with vpunch

    p "??Ugh!"

    if p_active == "p_didac":

        # Neus Warning about put it inside.

        if p_didac.pos in ["oral", "69"]:

            #if p_prot.action != "blowjob_done": # In theory Didac has already his dick out. (Talking)

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Talkingx07
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris front03
            show neus_exp_eyebrows angryx01
            with fade_short

            if p_didac.blowjob_done > 0:

                ne "??M??tetela otra vez dentro!"

            else:

                ne "??M??tetela dentro!"

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

            if p_prot.pos == "oral":

                #call pedrera_sex_p_general_talk

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris right02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                show gensex_oral_d_frontHead_exp_eyebrows angryx03

            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx09

            with fade_short

            d "??Que no la quiero en mi boca!"

            if p_prot.pos == "oral":

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris right02
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx07
                show gensex_oral_d_frontHead_exp_eyebrows sadx04

            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Silentx07
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Talkingx09
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows angryx03
            with fade_short

            ne "{size=40}??AHORA!{/size}"

            show neus_exp_mouth sad_Silentx04
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows angryx04
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

            if p_prot.pos == "oral":
                #call pedrera_sex_p_general_talk

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris right04
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx10
                show gensex_oral_d_frontHead_exp_eyebrows angryx04

            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Silentx06

            with fade_short

            d "Tsssk..."

            if p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris down03
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx05
                show gensex_oral_d_frontHead_exp_eyebrows sadx03

            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Silentx08

            with dissolve

            pause 0.2

            #$ p_didac.action = "blowjob_received" # No because this is used later.


        else:

            if p_prot.action not in ["vaginal_done", "vaginalDeep_done", "anal_done", "analDeep_done"]:

                $ Pedrera_char_Cond = "NeusClose_show"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Talkingx07
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris front03
                show neus_exp_eyebrows angryx02
                with fade_short

                ne "??R??pido!"

                show neus_exp_mouth sad_Talkingx08
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris front02
                show neus_exp_eyebrows angryx01
                with dissolve

                ne "??M??tesela!"

                $ Pedrera_char_Cond = "p_nobody"
                call Pedrera_char_lab

                if p_prot.pos == "doggy":
                    $ ped_sex_general_zoom_Cond = "face"
                    call pedrera_sex_p_general_talk

                elif p_prot.pos == "missionary":
                    $ ped_sex_general_zoom_Cond = ""
                    $ ped_sex_general_expression_Cond = "talk"
                    #$ ped_sex_general_action_Cond = "talk"
                    call pedrera_sex_p_general_talk

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils right01
                        show gensex_missionary_d_head_exp_eyebrows serious
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04

                else:
                    scene day05

                with fade_short

                if DidacPregnant:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils right01
                        show gensex_missionary_d_head_exp_eyebrows sadx01
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx03
                        with dissolve

                    d "????Tan pronto?!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 02
                        show gensex_missionary_d_head_exp_pupils front02
                        show gensex_missionary_d_head_exp_eyebrows sadx02
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx02
                        with dissolve

                    d "Seguro que puede aguantar un poco m??s..."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 03
                        show gensex_missionary_d_head_exp_pupils front03
                        show gensex_missionary_d_head_exp_eyebrows sadx03
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                        with dissolve

                else:

                    d "????Por el culo?!"

                    if p_didac.anal_received == 0:

                        d "??Ni de co??a!"

                    ne "Pues entonces p??ntelo en la boca."

                    if p_didac.anal_received == 0:

                        d "??Tssk!"

                        $ p_didac.pos = "oral"

                    else:

                        d "??Menos a??n!"

                $ Pedrera_char_Cond = "NeusClose_show"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Talkingx09
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows angryx03
                with fade_short

                ne "??AHORA!"

                show neus_exp_mouth sad_Silentx06
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris front05
                show neus_exp_eyebrows angryx03
                with dissolve

                pause 0.2

            else:

                $ debug("You have already your dick inside of her.")
                
                $ debug ("You already have your dick inside of her.")

    elif p_active == "p_txell":

        $ debug("Txell just before receive your cum (Neus exclamation.")

        $ debug ("Txell just before receive your cum (Neus exclamation).")

        $ Pedrera_char_Cond = "NeusClose_show"
        call Pedrera_char_lab

        show neus_exp_mouth sad_Talkingx04
        $ nteye = 3
        call neus_exp_tears_tears
        show neus_exp_iris front03
        show neus_exp_eyebrows sadx01
        with fade_short

        if p_didac.pos in ["oral", "69"]:

            if p_prot.action != "blowjob_done":

                ne "Txell..."

                pause 0.2

                $ Pedrera_char_Cond = "p_nobody"
                call Pedrera_char_lab

                if p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx02
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01

                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx02
                with fade_short

                tx "Lo s??,"

                extend " lo s??..."

        else:

            if p_prot.action not in ["vaginal_done", "vaginalDeep_done", "anal_done", "analDeep_done"]:

                ne "Txell,"

                extend " est?? a..."

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx03
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "p_nobody"
                call Pedrera_char_lab

                if p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx02
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01

                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx02

                with fade_short

                tx "Lo s??,"

                extend " lo s??..."

                if p_prot.pos == "oral":
                    $ ped_sex_general_expression_Cond = "closed"
                    $ ped_sex_general_action_Cond = "o02_03"
                call pedrera_sex_p_general_talk

                #scene day05
                with fade


    elif p_active == "p_neus":

        $ debug ("Neus just before receive your cum.")

        if p_prot.pos == "69" or p_prot.pos == "oral":

            if p_prot.b_action in ["blowjob_received", "blowjobDeep_received"]:
                $ p_neus.cumReceived = "oral"
                progcheck "Cum in mouth."

            else:
                $ p_neus.cumReceived = "pre-oral"
                progcheck "Cum not yet in mouth."

        else:

            if p_prot.action in["vaginal_done", "vaginalDeep_done"]:
                $ p_neus.cumReceived = "vaginal"
                progcheck "Cum in Vagina."

            elif p_prot.action in ["anal_done", "analDeep_done"]:
                $ p_neus.cumReceived = "anal"
                progcheck "Cum in Ass."

            else:
                $ p_neus.cumReceived = "unknown"
                progcheck "He can cum on back or stomach.?!"


        if p_prot.pos == "69":
            if p_neus.action not in ["blowjob_done", "blowjobDeep_done"]:
                show gensex_69_L_d_mouth happybiting_Silentx03
        elif p_prot.pos == "oral":
            if p_prot.b_action == "blowjob_received", "blowjobDeep_received":
                $ ped_sex_general_expression_Cond = "lustToYou"
                #$ ped_sex_general_action_Cond = "o01_01"
                call pedrera_sex_p_general_talk
            else:
                $ nteye = "down03"
                show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx06
                show gensex_oral_n_frontHead_exp_eyebrows sadx01
                call gensex_oral_n_frontHead_exp_tears_tears
        elif p_prot.pos == "missionary":
            $ ped_sex_general_expression_Cond = "talk"
            call pedrera_sex_p_general_talk

            $ nteye = "down03"
            show gensex_missionary_n_head_exp_mouth happybiting_Silentx06
            show gensex_missionary_n_head_exp_eyebrows sadx01
            call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

        p "[neusname]..."

        if p_neus.cumReceived == "pre-oral":

            scene day06
            with fade_short

            n "R??pidamente te agarra por las nalgas"

            if p_neus.blowjobDeep_done > 0:

                n "y se mete tu polla entera en la garganta."

            else:

                n "y se mete tu polla en su boca."

        elif p_neus.cumReceived == "unknown":
            # NOT FINISHED EXPRESSIONS only done for MISISONARY
            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happybiting_Silentx03
            elif p_prot.pos == "oral":
                if p_prot.b_action == "blowjob_received", "blowjobDeep_received":
                    $ ped_sex_general_expression_Cond = "lustToYou"
                    #$ ped_sex_general_action_Cond = "o01_01"
                    call pedrera_sex_p_general_talk
                else:
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_n_frontHead_exp_eyebrows sadx01
                    call gensex_oral_n_frontHead_exp_tears_tears
            elif p_prot.pos == "missionary":
                $ ped_sex_general_expression_Cond = "talk"
                call pedrera_sex_p_general_talk

                $ nteye = "front02"
                show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                show gensex_missionary_n_head_exp_eyebrows sadx01
                call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            ne "R??pido!"

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happybiting_Silentx03
            elif p_prot.pos == "oral":
                if p_prot.b_action == "blowjob_received", "blowjobDeep_received":
                    $ ped_sex_general_expression_Cond = "lustToYou"
                    call pedrera_sex_p_general_talk
                else:
                    $ nteye = "front03"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                    show gensex_oral_n_frontHead_exp_eyebrows normal
                    call gensex_oral_n_frontHead_exp_tears_tears
            elif p_prot.pos == "missionary":

                $ nteye = "front03"
                show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                show gensex_missionary_n_head_exp_eyebrows normal
                call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            ne "M??temela dentro!"

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happybiting_Silentx03
            elif p_prot.pos == "oral":
                if p_prot.b_action == "blowjob_received", "blowjobDeep_received":
                    $ ped_sex_general_expression_Cond = "lustToYou"
                    call pedrera_sex_p_general_talk
                else:
                    $ nteye = "front04"
                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                    show gensex_oral_n_frontHead_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
            elif p_prot.pos == "missionary":

                $ nteye = "front04"
                show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                show gensex_missionary_n_head_exp_eyebrows sadx04
                call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            p "Pero..."

            extend " ??D??nde?"

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happybiting_Silentx03
            elif p_prot.pos == "oral":
                if p_prot.b_action == "blowjob_received", "blowjobDeep_received":
                    $ ped_sex_general_expression_Cond = "lustToYou"
                    call pedrera_sex_p_general_talk
                else:
                    $ nteye = "front08"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx004
                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
            elif p_prot.pos == "missionary":
                $ ped_sex_general_expression_Cond = "talk"
                call pedrera_sex_p_general_talk

                $ nteye = "front08"
                show gensex_missionary_n_head_exp_mouth sad_Talkingx004
                show gensex_missionary_n_head_exp_eyebrows sadx05
                call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            if p_neus.vaginal_received > 0:

                ne "Ya sabes d??nde la quiero,"

            else:

                ne "Ya sabes que me gustar??a que fuera d??nde no has querido penetrarme,"

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happybiting_Silentx03
            elif p_prot.pos == "oral":
                if p_prot.b_action == "blowjob_received", "blowjobDeep_received":
                    $ ped_sex_general_expression_Cond = "lustToYou"
                    #$ ped_sex_general_action_Cond = "o01_01"
                    call pedrera_sex_p_general_talk
                else:
                    $ nteye = "right02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_n_frontHead_exp_eyebrows sadx03
                    call gensex_oral_n_frontHead_exp_tears_tears
            elif p_prot.pos == "missionary":
                $ ped_sex_general_expression_Cond = "talk"
                call pedrera_sex_p_general_talk

                $ nteye = "right02"
                show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                show gensex_missionary_n_head_exp_eyebrows sadx03
                call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            ne "pero eres t?? quien debe elegir."

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happybiting_Silentx03
            elif p_prot.pos == "oral":
                if p_prot.b_action == "blowjob_received", "blowjobDeep_received":
                    $ ped_sex_general_expression_Cond = "lustToYou"
                    #$ ped_sex_general_action_Cond = "o01_01"
                    call pedrera_sex_p_general_talk
                else:
                    $ nteye = "front01"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx07
                    show gensex_oral_n_frontHead_exp_eyebrows sadx01
                    call gensex_oral_n_frontHead_exp_tears_tears
            elif p_prot.pos == "missionary":
                $ ped_sex_general_expression_Cond = "talk"
                call pedrera_sex_p_general_talk

                $ nteye = "front01"
                show gensex_missionary_n_head_exp_mouth sad_Talkingx07
                show gensex_missionary_n_head_exp_eyebrows sadx01
                call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            ne "??Pero hazlo ya!"

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happybiting_Silentx03
            elif p_prot.pos == "oral":
                if p_prot.b_action == "blowjob_received", "blowjobDeep_received":
                    $ ped_sex_general_expression_Cond = "lustToYou"
                    #$ ped_sex_general_action_Cond = "o01_01"
                    call pedrera_sex_p_general_talk
                else:
                    $ nteye = "front05"
                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx04
                    show gensex_oral_n_frontHead_exp_eyebrows sadx03
                    call gensex_oral_n_frontHead_exp_tears_tears
            elif p_prot.pos == "missionary":
                $ ped_sex_general_expression_Cond = "talk"
                call pedrera_sex_p_general_talk

                $ nteye = "front05"
                show gensex_missionary_n_head_exp_mouth sadbiting_Silentx04
                show gensex_missionary_n_head_exp_eyebrows sadx03
                call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            menu:

                pt "??D??nde?"

                "<Correrse en su vagina>":
                    $ p_neus.cumReceived = "vaginal"
                    jump p_neus_pre_received_label
                    
                "<Correrse en su ano>":
                    $ p_neus.cumReceived = "anal"
                    jump p_neus_pre_received_label

                "<Correrse en su barriga>" if p_prot.pos == "missionary" and not gensex_ILoveYouNeus:
                    $ p_neus.cumReceived = "stomach"
                    jump p_neus_pre_wrong_received_label

                "<Correrse en sus nalgas>" if p_prot.pos == "doggy" and not gensex_ILoveYouNeus:
                    $ p_neus.cumReceived = "buttocks"
                    jump p_neus_pre_wrong_received_label

        else:

            if p_prot.pos == "69":
                if p_prot.b_action == "blowjob_received", "blowjobDeep_received":
                    call ped_sex_69_mc_blowjob_Stop
                    show closetocum_mc zorder 99
                    with Dissolve(0.5)
                show gensex_69_L_d_mouth happy_Talkingx04
            elif p_prot.pos == "oral":
                call p_neus_blowjob_stop_label

                $ nteye = "front04"
                show gensex_oral_n_frontHead_exp_mouth happy_Talkingx05
                show gensex_oral_n_frontHead_exp_eyebrows sadx05
                call gensex_oral_n_frontHead_exp_tears_tears
            elif p_prot.pos == "missionary":
                $ nteye = "front04"
                show gensex_missionary_n_head_exp_mouth happy_Talkingx05
                show gensex_missionary_n_head_exp_eyebrows sadx05
                call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            ne "Lo s??,"

            extend " lo s??..."

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happybiting_Silentx06
            elif p_prot.pos == "oral":
                $ nteye = "down05"
                show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx15
                show gensex_oral_n_frontHead_exp_eyebrows sadx06
                call gensex_oral_n_frontHead_exp_tears_tears
            elif p_prot.pos == "missionary":
                $ nteye = "down05"
                show gensex_missionary_n_head_exp_mouth happybiting_Silentx15
                show gensex_missionary_n_head_exp_eyebrows sadx06
                call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            n "Una sonrisa de ni??a traviesa se dibuja en su rostro."

        if p_prot.pos == "69":
            call p_69_blowjob_after_label
            show closetocum_mc zorder 99
            with Dissolve(0.5)

    ####

    $ p_prot.orgasm += 1
    $ p_prot.closeOrgasm = 0
    if p_prot.pleasure > 50:
        $ p_prot.pleasure = -50
    else:
        $ p_prot.pleasure = 0

    if p_active == "p_didac":
        $ p_didac.seal = "received"
    elif p_active == "p_txell":
        $ p_txell.seal = "received"
    elif p_active == "p_neus":
        $ p_neus.seal = "received"

    ####

    if p_didac.seal == "received":

        $ debug ("Didac receives your cum.")

        if p_didac.pos in ["oral", "69"]:

            # scene day05
            # with fade

            $ p_didac.cumReceived = "oral"

            n "A rega??adientes,"

            if p_prot.pos == "oral":
                #$ ped_sex_blow_MChand = "off" # This is for forcing Didac to Deepthroat.
                $ ped_sex_general_expression_Cond = "closed"
                if p_didac.blowjobDeep_done > 1:
                    $ p_prot.action = "blowjobDeep_received"
                    $ p_didac.action = "blowjobDeep_done"
                    $ ped_sex_general_action_Cond = "o04_03"

                else:
                    $ p_prot.action = "blowjob_received"
                    $ p_didac.action = "blowjob_done"
                    $ ped_sex_general_action_Cond = "o02_02"
                call pedrera_sex_p_general_talk

            if p_prot.pos == "69":
                $ ped_sex_general_expression_Cond = ""
                $ ped_sex_general_action_b_Cond = "69b_02_01"
                call pedrera_sex_p_general_talk
            with Dissolve(0.5)

            if p_didac.action == "blowjob_received":

                n "D??dac profundiza con sus fauces sobre tu miembro,"

            else:

                n "D??dac introduce tu falo en sus fauces,"

            n "adentr??ndola en su garganta tanto como le es posible,"

            n "y con una expresi??n no demasiado agradable"

            $ debug ("ORAL CREAMPIE")

            # if p_prot.pos != "69":
            #     #"WTF DUDE?" # No expressions appear in the cumshot in her mouth-throat.
            #     $ ped_sex_general_expression_Cond = "angry"
            #     $ ped_sex_general_action_Cond = "ocum01"
            #     call pedrera_sex_p_general_talk

            show closetocum_mc

            pause 2.0

            show afternight04_sexbattle_effects white_cumming:
                truecenter

            pause 1.0

            scene black
            with fade

            n "empieza a recibir el chorro de esperma que emana de tu miembro."

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Talkingx05
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris front03
            show neus_exp_eyebrows angryx01
            with fade_short

            ne "Traga."

            show neus_exp_mouth sad_Talkingx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows serious
            with dissolve

            ne "No te dejes ni una gota."

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows serious
            with dissolve

            pause 0.2

            if p_prot.pos == "69":
                $ ped_sex_general_69_cover = "over"
                #$ ped_sex_general_expression_Cond = "talk"
                $ ped_sex_general_action_Cond = "69_00_00"
                call pedrera_sex_p_general_talk
                with fade_short

            else:
                $ ped_sex_general_expression_Cond = "angryRight"
                call pedrera_sex_p_general_talk
                with fade_short


            n "Con una mirada de pocos amigos,"

            if p_prot.pos == "oral":
                $ ped_sex_general_expression_Cond = "closed"
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

            ono "glup"

            extend " glup"

            extend " glup"

            n "obedece las ??rdenes de [neusname]."

        else:

            # scene day05
            # with fade

            # if p_prot.pos == "doggy":
            #     $ ped_sex_general_zoom_Cond = "crotch"
            #     call pedrera_sex_p_general_talk
            #     with fade_short

            if p_prot.action not in ["vaginal_done", "vaginalDeep_done", "anal_done", "analDeep_done"]:

                n "R??pidamente,"

                if DidacPregnant:

                    $ p_prot.action = "vaginal_done"
                    $ p_didac.b_action = "vaginal_received"

                    $ ped_sex_general_zoom_Cond = "crotch"
                    $ ped_sex_general_action_Cond = "v00_03"
                    call pedrera_sex_p_general_talk
                    with fade_short

                    n "diriges tu erecto miembro a sus labios menores completamente empapados."


                else:

                    $ p_prot.action = "anal_done"
                    $ p_didac.b_action = "anal_received"

                    $ ped_sex_general_zoom_Cond = "crotch"
                    $ ped_sex_general_action_Cond = "a00_03"
                    call pedrera_sex_p_general_talk
                    with fade_short

                    n "diriges tu erecto miembro a su cavidad anal."

            #if DidacPregnant:
            if p_prot.action in ["vaginal_done", "vaginalDeep_done"]:

                # $ p_prot.action = "vaginal_done"
                # $ p_didac.b_action = "vaginal_received"

                $ p_didac.cumReceived = "vaginal"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell" and ped_sex_general_zoom_Cond != "crotch":
                    if p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 08
                        show gensex_missionary_d_head_exp_pupils front08
                        show gensex_missionary_d_head_exp_eyebrows sadx04
                        show gensex_missionary_d_head_exp_mouth happybiting_Silentx08

                with Dissolve(0.5)

                d "??HHHHmmmm...!"

            else:

                if afternight04_Anal_dick_med_Speed_1_Success > 0:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 02
                        show gensex_missionary_d_head_exp_pupils front02
                        show gensex_missionary_d_head_exp_eyebrows angryx06
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx23
                        with dissolve

                    d "??Estar??s de co??a!"

                else:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils front04
                        show gensex_missionary_d_head_exp_eyebrows angryx05
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx12
                        with dissolve

                    d "Joder..."

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sad_Silentx10
                    with dissolve

                $ p_didac.cumReceived = "anal"

                # if p_prot.action != "vaginalDeep_done":
                #     $ p_prot.action = "anal_done"
                #     $ p_didac.action = "anal_received"

                # $ ped_sex_general_zoom_Cond = "crotch"
                # if ped_sex_general_action_Cond == "a0_03":
                #     $ ped_sex_general_action_Cond = "a01_03"

                call pedrera_sex_p_general_talk
                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 08
                    show gensex_missionary_d_head_exp_pupils front08
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                    show gensex_missionary_d_head_exp_mouth sad_Silentx08
                with Dissolve(0.5)

                if afternight04_Anal_dick_med_Speed_1_Success == 0:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 06
                        show gensex_missionary_d_head_exp_pupils front06
                        show gensex_missionary_d_head_exp_eyebrows angryx05
                        show gensex_missionary_d_head_exp_mouth sad_Silentx08
                        with dissolve

                    d "??UUUGHH!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils front04
                        show gensex_missionary_d_head_exp_eyebrows angryx04
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx09
                        with dissolve

                    d "??Hijo de puta!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 05
                        show gensex_missionary_d_head_exp_pupils front05
                        show gensex_missionary_d_head_exp_eyebrows angryx03
                        show gensex_missionary_d_head_exp_mouth sad_Silentx06
                        with dissolve

                else:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 06
                        show gensex_missionary_d_head_exp_pupils front06
                        show gensex_missionary_d_head_exp_eyebrows sadx04
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx08
                        with dissolve

                    d "??HHhmm...!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 05
                        show gensex_missionary_d_head_exp_pupils front05
                        show gensex_missionary_d_head_exp_eyebrows angryx04
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                        with dissolve

                    d "Cabr??n..."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 08
                        show gensex_missionary_d_head_exp_pupils front08
                        show gensex_missionary_d_head_exp_eyebrows sadx05
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx08
                        with dissolve

                pause 0.2

            $ debug ("CUMSHOT!")

            if p_prot.pos in ["doggy", "missionary"]:
                $ ped_sex_general_zoom_Cond = "crotch"

            if p_didac.b_action == "vaginal_received":
                $ ped_sex_general_action_Cond = "vcum01"
            elif p_didac.b_action == "vaginalDeep_received":
                $ ped_sex_general_action_Cond = "vcum02"
            elif p_didac.b_action == "anal_received":
                $ ped_sex_general_action_Cond = "acum01"
            elif p_didac.b_action == "analDeep_received":
                $ ped_sex_general_action_Cond = "acum02"
            else:
                $ debug ("ORAL CREAMPIE")
                $ ped_sex_general_action_Cond = "ocum01"

            call pedrera_sex_p_general_talk

            show closetocum_mc

            pause 2.0

            show afternight04_sexbattle_effects white_cumming:
                truecenter

            pause 1.0

            scene black
            with fade

            n "Sientes el habitual cosquilleo"

            n "al mismo tiempo que el flujo de esperma recorriendo internamente a lo largo de tu falo."

            p "HHhmmm..."

        ##

        call afternight05_Pedrera_Sex_Check_closeOrgasm_Check

        $ p_didac.seal = "sealed"

        ##

        if p_didac.cumReceived == "oral":

            if p_prot.pos == "69":
                $ ped_sex_general_69_cover = "over"
                $ ped_sex_general_expression_Cond = "talk"
                $ ped_sex_general_action_Cond = "69_00_00"
                $ ped_sex_general_action_b_Cond = "69b_00_00b"
                call pedrera_sex_p_general_talk

                show gensex_69_L_d_mouth sad_Silentx05

            if p_prot.pos == "oral":

                $ ped_sex_general_expression_Cond = "talk"
                $ ped_sex_general_action_Cond = "o00_00"
                call pedrera_sex_p_general_talk

                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx03
                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_eyebrows angryx03

            with Dissolve(1.0)

            d "..."

            if music_play != "almost_new_kevin":
                play music "audio/music/kevinmacleod/almost_new_kevin.ogg" fadein 10.0 fadeout 3.0
                $ music_play = "almost_new_kevin"

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx09

            else:
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris right04
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
            with dissolve

            d "??Est??s contenta?"

            if p_prot.pos == "69":

                show gensex_69_L_d_mouth sad_Silentx07

            else:
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx02
                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris right05
                show gensex_oral_d_frontHead_exp_eyebrows angryx02
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Talkingx06
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows angryx02
            with fade_short

            ne "Sigue chupando;"

            extend " hasta la ??ltima gota."

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx01
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

            if p_prot.pos == "69":
                call pedrera_sex_p_general_talk
                show gensex_69_L_d_mouth sad_Talkingx07
            else:

                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris right02
                show gensex_oral_d_frontHead_exp_eyebrows angryx03

            with fade_short

            d "??La madre que te pari??!"

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx08

            else:
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris right01
                show gensex_oral_d_frontHead_exp_eyebrows angryx04

            with dissolve

            d "??Si le chupo m??s se quedar?? sin polla, joder!"

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Silentx07
            else:
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris right05
                show gensex_oral_d_frontHead_exp_eyebrows angryx03

            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Silentx04
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx01
            with fade_short

            ne "..."

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx02
            with Dissolve(0.5)

            pause 0.2

            $ ped_cs_kiss_eyes_Cond = "right"
            $ ped_cs_kiss_n_arm_Cond = "down"

            # Neus en frente de D??dac labios cerrados. luego abiertos. Ojos de D??dac mir??ndola a ella y mir??ndote a ti.

            scene ped_cs_kissBef_nd_01:
                subpixel True
                truecenter
                zoom 1.0 xpos 0.5 ypos -0.2 # Down
                easein_quad 10.0 zoom 0.8 xpos 0.5 ypos 0.6 # Center
            with fade

            n "Con cierto titubeo, se acerca a D??dac."

            $ ped_cs_kiss_eyes_Cond = "rightDown"

            show ped_cs_kissBef_nd_01
            with dissolve

            d "??Qu??-"

            extend "qu?? haces?"

            if pl.dp > 50:
                $ ped_cs_kiss_eyes_Cond = "camera"

            else:
                $ ped_cs_kiss_eyes_Cond = "right"

            show ped_cs_kissBef_nd_01:
                easein_quad 20.0 zoom 0.4 xpos 0.5 ypos 0.5 # Whole image
            with dissolve

            if DidacPregnant:

                ne "Tranquila..."

            else:

                ne "Tranquilo..."

            extend " d??jate llevar."

            # Mano Neus mejilla mientras besa, Ojos D??dac abiertos y luego cerrados. Lengua larga entremezcl??ndose.

            $ ped_cs_kiss_eyes_Cond = "rightDown"
            $ ped_cs_kiss_n_arm_Cond = "cheek"
            show ped_cs_kissBef_nd_01
            with Dissolve(0.5)

            n "Acarici??ndole la mejilla con una mano y poni??ndose de rodillas junto a ella"

            window hide dissolve
            pause

            scene ped_cs_kissAf_nd_comp_01:
                subpixel True
                truecenter
                zoom 1.5 ypos -0.9 # Down Zoom
                easein_quad 25.0 zoom 1.0 ypos 1.15 # Center image
            with fade

            n "acerca sus labios a los suyos con el brillo viol??ceo en sus ojos."

            n "D??dac se queda petrificado sin saber muy bien c??mo reaccionar,"
            
            n "te mira de reojo, mientras Neus abre sugerentemente su boca invit??ndole a hacer lo propio,"

            n "-casi sin resistencia- accede, y as?? entremezclan sus lenguas"

            n "en lo que sin duda te parece un beso bastante apasionado."

            show ped_cs_kissAf_nd_comp_01:
                easein_quad 15.0 zoom 0.4 xpos 0.5 ypos 0.5 # General image

            n "Observas como Neus usando ambas manos para agarrarse a su cuello"

            n "mientras sigue profundizando en su beso,"

            n "D??dac empieza a gemir ahogadamente, no tanto como protesta,"

            n "sino m??s bien como una insospechada -y aparentemente agradable- sorpresa."

            window hide dissolve
            pause

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            # show neus_body naked # She's stil fucking dressed!!!!!
            # show neus_arm_l naked
            # show neus_arm_r naked

            show neus_exp_mouth sad_Talkingx001
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx01
            with fade

            n "Finalmente separa sus labios mientras se le va apagando el brillo de sus ojos."

            show neus_exp_mouth sad_Talkingx03
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris right03
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "Su-"

            extend "supongo que con esto es suficiente..."

            show neus_exp_mouth happybiting_Silentx03
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx02
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond =  "TxellClose_b_show"
            call Pedrera_char_lab

            show m_exp_mouth sadbiting_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows sadx02
            with fade

            n "En ese instante te fijas en Meritxell,"

            show m_exp_mouth happybiting_Silentx01
            show m_exp_eyes 05
            show m_exp_piris down05
            show m_exp_eyebrows sadx03
            with dissolve

            n "que est?? acarici??ndose la entrepierna con sus dedos completamente empapados en su jugo"

            show m_exp_mouth happybiting_Silentx02
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx04
            with dissolve

            n "-casi c??mo si hubiera olvidado que hay gente observ??ndola-."

            #$ debug ("Neus kisses D??dac's mouth to seal your cum.")

        else:

            n "Te dispones a sacarla..."

            $ Pedrera_char_Cond = "NeusSuperClose"
            call Pedrera_char_lab

            show n_closefromup_mouth sad_Talkingx004
            show n_closefromup_iris front01
            $ nteye = 1
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows surprisex01
            with fade_short

            ne "??Espera!"

            show n_closefromup_mouth sadbiting_Silentx03
            show n_closefromup_iris front02
            $ nteye = 2
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx01
            with dissolve

            p "Hmmm...?"

            show n_closefromup_mouth sad_Talkingx04
            show n_closefromup_iris down04
            $ nteye = 4
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx02
            with dissolve

            ne "Siempre queda alguna gota despu??s de la corrida."

            show n_closefromup_mouth sadbiting_Silentx04
            show n_closefromup_iris front04
            $ nteye = 4
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx01
            with dissolve

            p "Quedar?? como mucho el preseminal..."

            show n_closefromup_mouth sadbiting_Silentx06
            show n_closefromup_iris front05
            $ nteye = 5
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx03
            with dissolve

            pt "??O esto se llamar??a post-seminal?"

            # NOT FINISHED... what the fuck I do here?
            scene day05
            with fade

            n "Sientes la c??lida mano de Neus agarr??ndote los test??culos."

            p "????Qu??...?!"

            ne "S?? lo que me hago."

            n "Para luego usar el pulgar y el resto de sus dedos para presionar desde la base de tu miembro,"

            n "hasta chocar con su entrepierna."

            ne "Ahora s??cala despacio."

            n "Presiona a??n con m??s fuerza el centro inferior de tu miembro,"

            n "como si intentara quitarle todo el contenido al tubo de la pasta de dientes."

            p "??Ugh!"

            ne "He dicho despacio."

            p "Vale,"

            extend " vale..."

            n "Con cierta parsimonia,"

            n "logras sacar todo el miembro de su interior sintiendo sus dedos alcanzando tu rojizo glande"

            n "extrayendo de ??l un buen chorro de esperma solidificado entre sus dedos."

            n "Durante unos segundos se lo queda mirando con unos ojos intensos, como si estuviera fam??lica,"

            n "hasta que finalmente se los introduce en su boca"

            n "y sus ojos empiezan a brillar con ese color viol??ceo."

            n "Al darse cuenta de lo que ha hecho te aparta con brutalidad,"

            scene black
            with hpunch

            p "??EEYyyy!"

            if p_didac.cumReceived == "vaginal":
                scene ped_cs_cunTop_d_01:
                    subpixel True
                    truecenter
                    zoom 1.0 xpos 0.0 ypos 0.4 # Face Neus
                    ease 15.0 zoom 0.8 xpos 1.0 ypos 0.8 # Face Didac.
            else:
                scene ped_cs_aniTop_nd:
                    subpixel True
                    truecenter
                    zoom 0.7  ypos -1.0 # Her pussy
                    easeout_quad 7.0 zoom 0.85  ypos 0.9 # Neus head
                    easein_quad 7.0 zoom 1.0 xpos 0.55 ypos 2.5 # Didac Face

            with fade_short

            n "mientras separa a??n m??s las piernas de D??dac para introducir su lengua en su entrepierna."

            d "??UUhhhmmmm...!"

            if p_didac.cumReceived == "vaginal":

                n "Hundiendo sus labios en su cavidad vaginal con una mirada lasciva y brillante"

            else:

                n "Hundiendo sus labios en su cavidad anal con una mirada lasciva y brillante"

            

            n "al mismo tiempo que D??dac empieza a retorcerse de placer sobre la cama."

            if p_didac.cumReceived == "vaginal":
                show ped_cs_cunTop_d_01:
                    ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5 # General

            else:
                show ped_cs_aniTop_nd:
                    ease 10.0 zoom 0.31 xpos 0.5 ypos 0.6 # General

            d "????Jodeeeeer!!"

            n "Con un chorro incluso mayor del que t?? has sido capaz de lograr con tu miembro"

            n "empapa el rostro de [neusname]."

            n "A??n as??, sigue indagando con su lengua en su interior,"

            n "casi como si la estuviera succionando por completo."

            d "????Pero cuanto le mide la lengua a esta t??a?!"

            window hide dissolve
            pause

            scene black
            with fade

            if p_didac.cumReceived == "vaginal":

                n "Poco despu??s aparta su rostro de su entrepierna"

                n "con su longeva lengua empapada en sus jugos."

            else:

                n "Poco despu??s aparta su rostro de su agujero anal"

                n "con su longeva lengua."

            # NOT FINISHED

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth happybiting_Silentx06
            $ nteye = 6
            call neus_exp_tears_tears
            show neus_exp_iris front06
            show neus_exp_eyebrows sadx04
            with fade_short

            n "Paulatinamente sus ojos vuelven a la normalidad."

            show neus_exp_mouth happy_Talkingx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris down04
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "Creo que con esto es suficiente..."

            show neus_exp_mouth happybiting_Silentx04
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx05
            with dissolve

            p "..."

        #else:
            #$ debug ("ERROR Where does she licks? 2645965364")


        if p_txell.seal != "sealed":

            if p_didac.cumReceived != "oral":
                $ Pedrera_char_Cond =  "TxellClose_b"
                call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows surprisex001

            if p_didac.cumReceived != "oral":
                with fade
            else:
                with dissolve

            tx "Supongo que ahora me toca a mi."

            show m_exp_mouth happy_Silentx01
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            $ p_girl_active = p_txell
            $ p_active = "p_txell"
            $ p_activen = "txell"
            $ p_activeno = "_m"

            call p_any_restart

            jump afternight05_Pedrera_Sex

    if p_txell.seal == "received":

        $ debug ("Txell receives your cum.")

        if p_prot.pos == "oral":
            #$ ped_sex_blow_MChand = "off" # This is for forcing Didac to Deepthroat.
            $ ped_sex_general_expression_Cond = "closed"
            if p_didac.blowjobDeep_done > 1:
                $ p_prot.action = "blowjobDeep_received"
                $ p_didac.action = "blowjobDeep_done"
                $ ped_sex_general_action_Cond = "o04_03"

            else:
                $ p_prot.action = "blowjob_received"
                $ p_didac.action = "blowjob_done"
                $ ped_sex_general_action_Cond = "o02_02"
            call pedrera_sex_p_general_talk

        if p_prot.pos == "69":
            $ ped_sex_general_expression_Cond = ""
            $ ped_sex_general_action_b_Cond = "69b_04_04"
            call pedrera_sex_p_general_talk

            show closetocum_mc

        with Dissolve(0.5)

        if p_txell.pos in ["oral", "69"]:

            $ p_txell.cumReceived = "oral"

            n "Agarr??ndote de las nalgas,"

            if p_txell.action == "blowjob_received":

                n "profundiza con sus fauces sobre tu miembro,"

            else:

                n "introduce tu falo en sus fauces,"

            n "adentr??ndola casi por completo en su garganta,"

            n "y con una expresi??n p??cara y juguetona,"

            show afternight04_sexbattle_effects white_cumming:
                truecenter

            n "empieza a recibir el chorro de esperma que emana de tu miembro."

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Talkingx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx02
            with fade_short

            ne "No te dejes ni una gota."

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx03
            with dissolve

            pause 0.2

            if p_prot.pos == "oral":
                #$ ped_sex_blow_MChand = "off" # This is for forcing Didac to Deepthroat.
                $ ped_sex_general_expression_Cond = "closed"
                if p_didac.blowjobDeep_done > 1:
                    $ p_prot.action = "blowjobDeep_received"
                    $ p_didac.action = "blowjobDeep_done"
                    $ ped_sex_general_action_Cond = "o04_02"

                else:
                    $ p_prot.action = "blowjob_received"
                    $ p_didac.action = "blowjob_done"
                    $ ped_sex_general_action_Cond = "o03_01"
                call pedrera_sex_p_general_talk

            elif p_prot.pos == "69":
                $ ped_sex_general_expression_Cond = ""
                $ ped_sex_general_action_b_Cond = "69b_04_01"
                call pedrera_sex_p_general_talk

            tx "Huh-huhmm..."

            n "Casi como si asintiera con la cabeza,"

            ono "glup"

            extend " glup"

            extend " glup"

            n "sientes que succiona cada cent??metro c??bico de tu espeso l??quido blanco."

        else:

            if p_prot.action not in ["vaginal_done", "vaginalDeep_done", "anal_done", "analDeep_done"]:

                n "R??pidamente,"

                if TxellPregnant:

                    n "diriges tu erecto miembro a sus labios menores completamente empapados."

                else:

                    n "diriges tu erecto miembro a su cavidad anal."

            if TxellPregnant:

                $ p_prot.action = "vaginal_done"
                $ p_txell.b_action = "vaginal_received"

                $ p_txell.cumReceived = "vaginal"

            else:

                $ p_prot.action = "anal_done"
                $ p_txell.b_action = "anal_received"

                $ p_txell.cumReceived = "anal"

            tx "??HHHMMMMmmm...!"

            n "Sientes el habitual cosquilleo"

            n "al mismo tiempo que el flujo de esperma recorriendo internamente a lo largo de tu falo."

            p "HHhmmm..."

        call afternight05_Pedrera_Sex_Check_closeOrgasm_Check

        if p_txell.cumReceived == "oral":

            n "Sientes tu polla completamente succionada por las contracciones de su c??lida garganta"

            n "mientras su lengua juguetea t??midamente con la base de tus test??culos."

            pt "??Diooos...!"

            if p_txell.blowjobDeep_received > 0:

                pt "????Lesbiana?!"

                pt "??Mis cojones!"

                pt "????C??mo co??o se lo ha hecho para met??rsela entera de golpe?!"

            if p_prot.pos == "oral":
                $ ped_sex_general_action_Cond = "o01_01"
                call pedrera_sex_p_general_talk

            elif p_prot.pos == "69":
                $ ped_sex_general_expression_Cond = ""
                $ ped_sex_general_action_b_Cond = "69b_01_01"
                call pedrera_sex_p_general_talk

            with Dissolve(0.5)

            n "Lentamente va apartando su rostro de tu ombligo"

            n "mientras sientes sus labios recorrer lo largo y ancho de tu miembro"

            n "su lengua sigue jugueteando con tu a??n palpitante miembro;"

            n "para justo al final, cuando sus labios rodean tu rojizo glande,"

            n "hace un ??ltimo chupet??n en la punta succionando lo poco que le queda a tu miembro que dar."

            $ ped_sex_general_expression_Cond = "talk"

            if p_prot.pos == "oral":
                $ ped_sex_general_action_Cond = "o00_00"
                call pedrera_sex_p_general_talk

                show gensex_oral_m_frontHead_exp_eyes 05
                show gensex_oral_m_frontHead_exp_iris left05
                show gensex_oral_m_frontHead_exp_mouth happybiting_Silentx02
                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02

            elif p_prot.pos == "69":
                $ ped_sex_general_action_b_Cond = "69b_00_00"
                call pedrera_sex_p_general_talk

                show gensex_69_L_d_mouth sadbiting_Silentx02

            with Dissolve(0.5)

            tx "Hmmm..."

            if music_play != "meritxell_theme":
                play music "audio/music/meritxell_theme.ogg" fadein 10.0 fadeout 3.0
                $ music_play = "meritxell_theme"

            $ Pedrera_char_Cond = "TxellClose_b"
            call Pedrera_char_lab

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with fade

            n "R??pidamente se aparta de ti y se pone en pie."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris left03
            show m_exp_eyebrows normal
            with dissolve

            tx "??Con esto hay suficiente?"

            show m_exp_mouth happybiting_Silentx04
            show m_exp_eyes 04
            show m_exp_piris left04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Talkingx03
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris right03
            show neus_exp_eyebrows sadx01
            with fade_short

            ne "Supongo que s??."

            show neus_exp_mouth sadbiting_Silentx01
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris right02
            show neus_exp_eyebrows normal
            with dissolve

            tx "??Y ahora?"

            show neus_exp_mouth happy_Talkingx06
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris right04
            show neus_exp_eyebrows angryx01
            with dissolve

            ne "Ya sabes lo que viene ahora."

            show neus_exp_mouth happybiting_Silentx04
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx01
            with dissolve

            pause 0.2

            scene ped_cs_kissBef_nd_01:
                subpixel True
                truecenter
                zoom 1.0 xpos 0.5 ypos -0.2 # Down
                easein_quad 10.0 zoom 0.8 xpos 0.5 ypos 0.6 # Center
            with fade

            n "Con paso firme y una mirada seductora se acerca a Meritxell."

            n "Justo cuando llega en frente de ella,"

            $ ped_cs_kiss_n_arm_Cond = "cheek"
            show ped_cs_kissBef_nd_01:
                easein_quad 20.0 zoom 0.4 xpos 0.5 ypos 0.5
            with Dissolve(0.5)

            n "le acaricia la mejilla con cierta ternura"

            n "mientras se pone de rodillas ante ella."

            window hide dissolve
            pause

            scene ped_cs_kissAf_nd_comp_01:
                subpixel True
                truecenter
                zoom 1.5 ypos -0.9 # Down Zoom
                easein_quad 25.0 zoom 1.0 ypos 1.15 # Center image
            with fade

            n "Esta le devuelve una mirada de deseo y ambas se mezclan en un profundo beso."

            n "A medida que sus labios se abren y se cierran,"

            n "ves sus lenguas entremezclarse"

            n "y lo que parece una gota de tu espeso esperma derramarse por la mejilla de Meritxell;"

            n "poco antes de que esta llegue al l??mite d??nde termina su mand??bula,"

            n "los brillantes ojos de Neus se fijan en ella,"

            n "y separ??ndose ligeramente,"

            n "desliza su longeva lengua para relamer esa perdida l??grima blanca,"

            n "para luego retomar el acalorado beso."

            show ped_cs_kissAf_nd_comp_01:
                easein_quad 15.0 zoom 0.4 xpos 0.5 ypos 0.5 # General image

            tx "????HHHHmmm...!!"

            n "Un ahogado pero agudo gemido sale de los labios de Meritxell"

            n "mientras ves que sus piernas tiemblan descontroladamente"

            n "y cae rendida sobre el cuerpo de Neus que sigue sujet??ndola y bes??ndola sin descanso,"

            n "como si fuera un depredador terminando con el sufrimiento de su presa."

            pt "??Acaba de tener un orgasmo?"

            pt "Si ni siquiera ha..."

            n "Finalmente separa sus labios,"

            n "mientras la sigue sujetando para que no caiga"

            n "sin dejar de juguetear con su enorme lengua."

            window hide dissolve
            pause

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            # show neus_body naked # She's stil fucking dressed!!!!!
            # show neus_arm_l naked
            # show neus_arm_r naked

            show neus_exp_mouth sad_Talkingx001
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx01
            with fade

            n "Lentamente, el brillo en sus ojos se va apagando."

            show neus_exp_mouth happy_Talkingx03
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "Su-"

            extend "supongo que con esto es suficiente..."

            show neus_exp_mouth happybiting_Silentx06
            $ nteye = 6
            call neus_exp_tears_tears
            show neus_exp_iris front06
            show neus_exp_eyebrows sadx04
            with dissolve

            n "Pasados unos segundos,"

            show neus_exp_mouth happy_Silentx05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx01
            with dissolve

            n "separa sus p??rpados como si se despertara de un profundo sue??o."

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris left02
            show neus_exp_eyebrows surprisex01
            with dissolve

            tx "Cre-"

            extend " creo que a??n me queda un poco de su esperma debajo de la lengua..."

            show neus_exp_mouth happybiting_Silentx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris left04
            show neus_exp_eyebrows serious
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx003
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows surprisex01
            with dissolve

            ne "No seas tonta Txell,"

            show neus_exp_mouth happy_Talkingx06
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris left03
            show neus_exp_eyebrows serious
            with dissolve

            ne "ya he repasado esa parte la mar de bien,"

            extend " y lo sabes..."

            show neus_exp_mouth happybiting_Silentx05
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx01
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "TxellClose_b"
            call Pedrera_char_lab

            show m_exp_mouth sadbiting_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows sadx01
            with fade_short

            n "Meritxell te dirige una mirada de s??plica y deseo..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows sadx03
            with dissolve

            tx "??Puedo volver a besarla?"

            show m_exp_mouth sadbiting_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows sadx04
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Silentx02
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris left01
            show neus_exp_eyebrows surprisex01
            with fade_short

            ne "..."

            show neus_exp_mouth sadbiting_Silentx02
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows surprisex02
            with dissolve

            menu:

                pt "??Me pide permiso?"

                "Por supuesto que s??.":
                    call p_Help

                    $pl.ch_pts("np",1)
                    $pl.ch_pts("mp",2)

                    call NeusPermissionToKissTxell

                "Preferir??a que no.":
                    call p_Help

                    $pl.ch_pts("np",1)
                    $pl.ch_pts("mp",-5)

                    show neus_exp_mouth happy_Silentx02
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris front05
                    show neus_exp_eyebrows sadx01
                    with dissolve

                    ne "..."

                    $ Pedrera_char_Cond = "TxellClose_b"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Talkingx02
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows sadx03
                    with fade_short

                    tx "Lo entiendo..."

                    show m_exp_mouth sadbiting_Silentx06
                    show m_exp_eyes 05
                    show m_exp_piris down05
                    show m_exp_eyebrows sadx04
                    with dissolve

                    pause 0.2

                    $ Pedrera_char_Cond = "NeusClose_show"
                    call Pedrera_char_lab

                    show neus_exp_mouth sad_Talkingx03
                    $ nteye = 3
                    call neus_exp_tears_tears
                    show neus_exp_iris left03
                    show neus_exp_eyebrows sadx02
                    with dissolve

                    ne "Lo siento Txell..."

                    show neus_exp_mouth sadbiting_Silentx04
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris left04
                    show neus_exp_eyebrows sadx03
                    with dissolve

                    pause 0.2

                    $ Pedrera_char_Cond = "TxellClose_b"
                    call Pedrera_char_lab

                    show m_exp_mouth happy_Talkingx02
                    show m_exp_eyes 05
                    show m_exp_piris right05
                    show m_exp_eyebrows sadx02
                    with fade_short

                    tx "No pasa nada..."

                    show m_exp_mouth happy_Talkingx04
                    show m_exp_eyes 06
                    show m_exp_piris front06
                    show m_exp_eyebrows sadx03
                    with dissolve

                    tx "Simplemente,"

                    extend " ten??a que intentarlo."

                    show m_exp_mouth sadbiting_Silentx05
                    show m_exp_eyes 05
                    show m_exp_piris left05
                    show m_exp_eyebrows sadx05
                    with dissolve

                "No es a mi a quien tienes que ped??rselo.":
                    call p_Help

                    $pl.ch_pts("np",1)
                    $pl.ch_pts("mp",2)

                    call NeusPermissionToKissTxell

        else:

            aj "Here is where you had cum inside TXELL pussy or asshole. Not done yet."

            # FOR FUTURE

        $ p_txell.seal = "sealed"

        if p_didac.seal != "sealed":

            $ Pedrera_char_Cond = "DidacClose"
            call Pedrera_char_lab

            show didacf_mouth sad_Talkingx004
            show didacf_eyes 08
            show didacf_pupils front08
            show didacf_eyebrows angryx04
            with fade_short

            d "??Por fin es mi turno!"

            $ p_girl_active = p_didac
            $ p_active = "p_didac"
            $ p_activen = "didac"
            $ p_activeno = "_d"

            call p_any_restart

            jump afternight05_Pedrera_Sex


    if p_neus.seal == "received":

        jump p_neus_received_label

        # $ debug ("Neus receives your cum.")
        # scene black
        # with fade
        # $ p_neus.seal = "sealed"
        # $ debug ("Neus Keeps sucking your cock or fucking you... or whatever.")
        # call WIP
        # jump endupdate

    ##

    if (p_txell.seal and p_didac.seal) == "sealed" and p_neus.seal != "sealed":

        $ debug ("Ahora es el turno de Neus.")

        $ Pedrera_char_Cond = "NeusClose_show"
        call Pedrera_char_lab

        show neus_exp_mouth sad_Silentx03
        $ nteye = 1
        call neus_exp_tears_tears
        show neus_exp_iris front01
        show neus_exp_eyebrows surprisex01
        with fade

        p "Parece que D??dac y Txell ya han recibido su parte."

        show neus_exp_mouth sad_Silentx02
        $ nteye = 2
        call neus_exp_tears_tears
        show neus_exp_iris left02
        show neus_exp_eyebrows normal
        with dissolve

        tx "Eso parece."

        show neus_exp_mouth sadbiting_Silentx03
        $ nteye = 0
        call neus_exp_tears_tears
        show neus_exp_iris front00
        show neus_exp_eyebrows surprisex02
        with dissolve

        n "Fijas tu mirada en [neusname]."

        show neus_exp_mouth happybiting_Silentx04
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris left04
        show neus_exp_eyebrows sadx02
        with dissolve

        ne "..."

        show neus_exp_mouth sadbiting_Silentx02
        $ nteye = 1
        call neus_exp_tears_tears
        show neus_exp_iris right01
        show neus_exp_eyebrows surprisex01
        with dissolve

        d "A??n queda mucha noche por delante,"

        if music_play != "didac_theme":
            play music "audio/music/didac_theme.ogg" fadein 10.0 fadeout 3.0
            $ music_play = "didac_theme"

        $ Pedrera_char_Cond = "DidacClose"
        call Pedrera_char_lab

        show didacf_mouth happy_Talkingx06
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils front04
        show didacf_eyebrows angryx02
        with fade_short

        d "podr??amos seguir,"

        extend " ??no?"

        show didacf_mouth sadbiting_Silentx04
        $ dteye = 1
        call didac_exp_tears_tears
        show didacf_pupils left01
        show didacf_eyebrows surprisex01
        with dissolve

        tx "No queda tanto;"

        show didacf_mouth sad_Silentx05
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils left04
        show didacf_eyebrows angryx01
        with dissolve

        $ Pedrera_char_Cond =  "TxellDidac"
        call Pedrera_char_lab

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows normal

        show didacf_mouth sad_Silentx04
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils left04
        show didacf_eyebrows angryx01
        with fade

        tx "adem??s,"

        show m_exp_mouth sad_Talkingx004
        show m_exp_eyes 03
        show m_exp_piris right03
        show m_exp_eyebrows surprisex01

        show didacf_mouth sad_Silentx05
        $ dteye = 3
        call didac_exp_tears_tears
        show didacf_pupils left03
        show didacf_eyebrows suspiciousx01
        with dissolve

        tx "sabes bien que tu compa??ero de piso"

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows suspiciousx01

        show didacf_mouth sad_Silentx05
        $ dteye = 1
        call didac_exp_tears_tears
        show didacf_pupils left01
        show didacf_eyebrows surprisex01
        with dissolve

        tx "no va a poder tener m??s de tres corridas en una sola noche."

        show m_exp_mouth sad_Talkingx02
        show m_exp_eyes 04
        show m_exp_piris left04
        show m_exp_eyebrows serious

        show didacf_mouth sad_Silentx07
        $ dteye = 3
        call didac_exp_tears_tears
        show didacf_pupils left03
        show didacf_eyebrows angryx02
        with dissolve

        tx "Sin mencionar que Neus..."

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 03
        show m_exp_piris right03
        show m_exp_eyebrows surprisex01

        show didacf_mouth sad_Talkingx08
        $ dteye = 2
        call didac_exp_tears_tears
        show didacf_pupils left02
        show didacf_eyebrows angryx03
        with dissolve

        d "??Tampoco digo que se me vuelva a correr dentro, joder!"

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows suspiciousx02

        if p_didac.vaginal_received > 0:

            show didacf_mouth sad_Talkingx05
            $ dteye = 3
            call didac_exp_tears_tears
            show didacf_pupils front03
            show didacf_eyebrows sadx01
            with dissolve

            d "Me conformo con que me la vuelva a meter..."

        else:

            show didacf_mouth sad_Talkingx07
            $ dteye = 3
            call didac_exp_tears_tears
            show didacf_pupils front03
            show didacf_eyebrows angryx02
            with dissolve

            d "??Me conformo con que al menos me la meta una jodida vez!"

        show m_exp_mouth sad_Silentx05
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows sadx01

        show didacf_mouth sadbiting_Silentx04
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils front04
        show didacf_eyebrows serious
        with dissolve

        pause 0.2

        play sound "audio/sfx/fall09.ogg"

        scene black
        with hpunch

        n "Meritxell le coge del brazo para arrastrarlo a la puerta que lleva al pasillo."

        $ Pedrera_char_Cond =  "TxellDidac"
        call Pedrera_char_lab

        show bg ped_door # NOT FINISHED, it should be close to the door.

        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows serious

        show didacf_mouth sad_Talkingx08
        $ dteye = 3
        call didac_exp_tears_tears
        show didacf_pupils left03
        show didacf_eyebrows angryx02
        with fade

        d "????Qu?? co??o haces?!"

        if music_play != "meritxell_theme":
            play music "audio/music/meritxell_theme.ogg" fadein 10.0 fadeout 3.0
            $ music_play = "meritxell_theme"

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris right03
        show m_exp_eyebrows surprisex001

        show didacf_mouth sad_Silentx02
        $ dteye = 1
        call didac_exp_tears_tears
        show didacf_pupils left01
        show didacf_eyebrows serious
        with dissolve

        if p_txell_cunnilingus_received_from_p_didac_at_missionary > 0:

            tx "Antes me has dicho que te gustar??a volverme a comerme el co??o."

        else:

            tx "Antes me has dicho que te hubiera gustado comerme el co??o."

        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows suspiciousx01

        show didacf_mouth sad_Talkingx06
        $ dteye = 2
        call didac_exp_tears_tears
        show didacf_pupils left02
        show didacf_eyebrows suspiciousx01
        with dissolve

        d "??Yo he dicho eso?"

        show m_exp_mouth happy_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows surprisex01

        show didacf_mouth sad_Silentx03
        $ dteye = 1
        call didac_exp_tears_tears
        show didacf_pupils left01
        show didacf_eyebrows surprisex01
        with dissolve

        tx "??No te gustar??a averiguar lo buena que soy en ello?"

        if DidacPregnant == False:

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows suspiciousx02

            show didacf_mouth sad_Silentx03
            $ dteye = 0
            call didac_exp_tears_tears
            show didacf_pupils left00
            show didacf_eyebrows surprisex02
            with dissolve

            tx "Antes de que vuelvas a recuperar tu..."

            extend " polla."

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows suspiciousx02

            show didacf_mouth sadbiting_Silentx04
            $ dteye = 2
            call didac_exp_tears_tears
            show didacf_pupils down02
            show didacf_eyebrows suspiciousx02
            with dissolve

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows suspiciousx02

        show didacf_mouth sadbiting_Silentx05
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils left04
        show didacf_eyebrows serious
        with dissolve

        d "..."

        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 02
        show m_exp_piris right02
        show m_exp_eyebrows serious

        show didacf_mouth sadbiting_Silentx06
        $ dteye = 3
        call didac_exp_tears_tears
        show didacf_pupils front03
        show didacf_eyebrows sadx01
        with dissolve

        n "D??dac te dirige una mirada entre la resignaci??n y la curiosidad."

        show m_exp_mouth sad_Silentx01
        show m_exp_eyes 01
        show m_exp_piris right01
        show m_exp_eyebrows surprisex01

        show didacf_mouth sad_Talkingx05
        $ dteye = 8
        call didac_exp_tears_tears
        show didacf_pupils front08
        show didacf_eyebrows angryx02
        with dissolve

        d "Bah..."

        show m_exp_mouth happy_Silentx03
        show m_exp_eyes 03
        show m_exp_piris right03
        show m_exp_eyebrows normal

        show didacf_mouth sad_Talkingx06
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils left04
        show didacf_eyebrows angryx02
        with dissolve

        d "Supongo que no voy a perder nada en probarlo..."

        show m_exp_mouth happy_Talkingx08
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex001

        show didacf_mouth sad_Silentx04
        $ dteye = 5
        call didac_exp_tears_tears
        show didacf_pupils left05
        show didacf_eyebrows suspiciousx02
        with dissolve

        tx "Te garantizo que no."

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 02
        show m_exp_piris right02
        show m_exp_eyebrows serious

        show didacf_mouth sad_Talkingx004
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils left04
        show didacf_eyebrows surprisex01
        with dissolve

        d "No tienes abuela,"

        extend " ??verdad?"

        if p_txell.blowjob_done > 0:

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            show m_exp_eyebrows angryx01

            show didacf_mouth sadbiting_Silentx02
            $ dteye = 1
            call didac_exp_tears_tears
            show didacf_pupils left01
            show didacf_eyebrows surprisex02
            with dissolve

            tx "No solo soy capaz de tragarme pollas enormes..."

        show m_exp_mouth happy_Talkingx06
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex01

        show didacf_mouth sadbiting_Silentx03
        $ dteye = 2
        call didac_exp_tears_tears
        show didacf_pupils left02
        show didacf_eyebrows surprisex02
        with dissolve

        tx "Soy mujer,"

        extend " tengo co??o,"

        show m_exp_mouth happy_Talkingx08
        show m_exp_eyes 03
        show m_exp_piris right03
        show m_exp_eyebrows angryx02

        show didacf_mouth sadbiting_Silentx04
        $ dteye = 3
        call didac_exp_tears_tears
        show didacf_pupils left03
        show didacf_eyebrows suspiciousx01
        with dissolve

        tx "y te recuerdo que he estado con m??s mujeres que hombres."

        show m_exp_mouth happy_Talkingx07
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows surprisex01

        show didacf_mouth sadbiting_Silentx02
        $ dteye = 2
        call didac_exp_tears_tears
        show didacf_pupils left02
        show didacf_eyebrows surprisex01
        with dissolve

        tx "Algo habr?? aprendido con el tiempo,"

        extend " ??no te parece?"

        show m_exp_mouth happy_Silentx05
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows angryx01

        show didacf_mouth sad_Silentx03
        $ dteye = 2
        call didac_exp_tears_tears
        show didacf_pupils left02
        show didacf_eyebrows suspiciousx01
        with dissolve

        d "..."

        show m_exp_mouth happy_Silentx06
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows angryx02

        show didacf_mouth sad_Talkingx04
        $ dteye = 1
        call didac_exp_tears_tears
        show didacf_pupils left01
        show didacf_eyebrows suspiciousx02
        with dissolve

        d "Supongo."

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex01

        show didacf_mouth sadbiting_Silentx02
        $ dteye = 1
        call didac_exp_tears_tears
        show didacf_pupils left01
        show didacf_eyebrows surprisex02
        with dissolve

        tx "Pues no me discutas,"

        extend " y s??gueme."

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 02
        show m_exp_piris left02
        show m_exp_eyebrows surprisex01

        show didacf_mouth sad_Silentx05
        $ dteye = 5
        call didac_exp_tears_tears
        show didacf_pupils left05
        show didacf_eyebrows angryx02
        with dissolve

        ne "Txell..."

        if music_play != "almost_new_kevin":
            play music "audio/music/kevinmacleod/almost_new_kevin.ogg" fadein 10.0 fadeout 3.0
            $ music_play = "almost_new_kevin"

        $ Pedrera_char_Cond = "TxellClose_b"
        call Pedrera_char_lab

        show m_exp_mouth sad_Talkingx03
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows sadx01
        with fade

        tx "S??,"

        extend " lo s??,"

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris left03
        show m_exp_eyebrows sadx01
        with dissolve

        tx "no podemos salir del edificio ni tampoco ir muy lejos."

        show m_exp_mouth happy_Talkingx04
        show m_exp_eyes 02
        show m_exp_piris left02
        show m_exp_eyebrows sadx02
        with dissolve

        tx "Tranquila,"

        extend " soy consciente del peligro."

        show m_exp_mouth happy_Silentx02
        show m_exp_eyes 03
        show m_exp_piris left03
        show m_exp_eyebrows sadx01
        with dissolve

        pause 0.2

        $ Pedrera_char_Cond = "NeusClose_show"
        call Pedrera_char_lab

        show neus_exp_mouth sadbiting_Silentx03
        $ nteye = 6
        call neus_exp_tears_tears
        show neus_exp_iris front06
        show neus_exp_eyebrows sadx02
        with fade

        ne "..."

        show neus_exp_mouth happy_Talkingx02
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_iris right05
        show neus_exp_eyebrows sadx03
        with dissolve

        ne "Gracias."

        show neus_exp_mouth sad_Silentx03
        $ nteye = 0
        call neus_exp_tears_tears
        show neus_exp_iris right00
        show neus_exp_eyebrows surprisex01
        with dissolve

        tx "Ya me dar??s \"las gracias\", despu??s."

        show neus_exp_mouth happy_Talkingx07
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris right04
        show neus_exp_eyebrows sadx04
        with dissolve

        ne "Ser??s tonta..."

        show neus_exp_mouth happy_Silentx04
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_iris right05
        show neus_exp_eyebrows sadx03
        with dissolve

        pause 0.2

        # DOOR CLOSED

        play sound "audio/sfx/door_close01.ogg"

        scene night04_pedrera_baba01_background:
            subpixel True
            zoom 0.6
            easein_quad 0.5zoom 0.4
        show night04_pedrera_baba01_door:
            subpixel True
            zoom 0.5
            easein_quad 0.5 zoom 0.4
        show night04_pedrera_baba01_frame:
            subpixel True
            zoom 0.5
            easein_quad 0.5 zoom 0.4
        with hpunch

        ono "Pam"

        n "Meritxell cierra la puerta despu??s de hacer salir a D??dac"

        n "dej??ndoos a [neusname] y a ti completamente a solas en la habitaci??n."

        $ Pedrera_char_Cond = "NeusClose_show"
        call Pedrera_char_lab

        show neus_exp_mouth sadbiting_Silentx01
        $ nteye = 0
        call neus_exp_tears_tears
        show neus_exp_iris front00
        show neus_exp_eyebrows surprisex02
        with fade

        ne "..."

        if music_play != "bittersweet":
            play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 10.0 fadeout 3.0
            $ music_play = "bittersweet"

        show neus_exp_mouth sadbiting_Silentx04
        $ nteye = 2
        call neus_exp_tears_tears
        show neus_exp_iris right02
        show neus_exp_eyebrows sadx01
        with dissolve

        n "Un silencio inc??modo inunda el lugar."

        show neus_exp_mouth sadbiting_Silentx05
        $ nteye = 8
        call neus_exp_tears_tears
        show neus_exp_iris front08
        show neus_exp_eyebrows sadx02
        with dissolve

        p "[neusname]..."

        # CONDITIONAL

        show neus_exp_mouth sad_Talkingx04
        $ nteye = 2
        call neus_exp_tears_tears
        show neus_exp_iris front02
        show neus_exp_eyebrows sadx03
        with dissolve

        if ped_neusname_angry:

            
            ne "??Tanto te molest?? que no te dijera mi nombre real?"

        elif neusname == "Neus":

            ne "Veo que sigues usando el nombre que me puse para escapar de Padre..."

            show neus_exp_mouth sad_Talkingx03
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris front03
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "??Tanto te molest?? que no te dijera mi nombre real?"

        else:

            ne "??Te molest?? que no te dijera mi nombre real?"

        show neus_exp_mouth sadbiting_Silentx04
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris front04
        show neus_exp_eyebrows sadx04
        with dissolve

        p "..."

        show neus_exp_mouth sadbiting_Silentx03
        $ nteye = 2
        call neus_exp_tears_tears
        show neus_exp_iris front02
        show neus_exp_eyebrows sadx02
        with dissolve

        if ped_neusname_angry:

            p "Simplemente, me hubiera gustado pensar que confiabas m??s en mi."

        else:

            p "Dime tonto,"

            extend " pero uno tiene esa ilusi??n de creer que existe esa confianza."

        show neus_exp_mouth sad_Talkingx05
        $ nteye = 8
        call neus_exp_tears_tears
        show neus_exp_iris front08
        show neus_exp_eyebrows sadx04
        with dissolve

        ne "No era una cuesti??n de confianza,"

        show neus_exp_mouth sad_Talkingx04
        $ nteye = 3
        call neus_exp_tears_tears
        show neus_exp_iris front03
        show neus_exp_eyebrows sadx05
        with dissolve

        ne "solo intentaba protegerte."

        show neus_exp_mouth sad_Talkingx06
        $ nteye = 1
        call neus_exp_tears_tears
        show neus_exp_iris front01
        show neus_exp_eyebrows sadx03
        with dissolve

        ne "Si hubieras indagado sobre mi y mi pasado..."

        show neus_exp_mouth sad_Talkingx04
        $ nteye = 3
        call neus_exp_tears_tears
        show neus_exp_iris front03
        show neus_exp_eyebrows sadx05
        with dissolve

        ne "probablemente Padre hubiera acabado..."

        show neus_exp_mouth sadbiting_Silentx06
        $ nteye = 6
        call neus_exp_tears_tears
        show neus_exp_iris front06
        show neus_exp_eyebrows sadx06
        with dissolve

        p "..."

        $ ntlong = 2

        show neus_exp_mouth sad_Talkingx03
        $ nteye = 8
        call neus_exp_tears_tears
        show neus_exp_iris front08
        show neus_exp_eyebrows sadx04
        with dissolve

        ne "Aunque de todos modos por lo visto ya era demasiado tarde..."

        show neus_exp_mouth sadbiting_Silentx02
        $ nteye = 1
        call neus_exp_tears_tears
        show neus_exp_iris front01
        show neus_exp_eyebrows normal
        with dissolve

        p "??C??mo prefieres que te llame?"

        show neus_exp_mouth happy_Talkingx03
        $ nteye = 3
        call neus_exp_tears_tears
        show neus_exp_iris front03
        show neus_exp_eyebrows sadx01
        with dissolve

        ne "Me gusta que me llames [neusname]."

        $ ntlong = 3

        show neus_exp_mouth happy_Talkingx05
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris front04
        show neus_exp_eyebrows sadx02
        with dissolve

        ne "Al fin y al cabo,"

        if neusname == "Neus":

            extend " as?? es como me conociste."

        elif neusname == "Elur":

            extend " es mi verdadero nombre."

        else:

            aj "ERROR 4897"

        $ ntlong = 4

        show neus_exp_mouth happy_Silentx03
        $ nteye = 6
        call neus_exp_tears_tears
        show neus_exp_iris front06
        show neus_exp_eyebrows sadx05
        with dissolve

        #n "Unas l??grimas empapan su rostro."
        p "..."

        show neus_exp_mouth sad_Silentx03
        $ nteye = 2
        call neus_exp_tears_tears
        show neus_exp_iris front02
        show neus_exp_eyebrows sadx01
        with dissolve

        p "[neusname]..."

        show neus_exp_mouth sad_Talkingx01
        $ nteye = 1
        call neus_exp_tears_tears
        show neus_exp_iris down01
        show neus_exp_eyebrows surprisex01
        with dissolve

        ne "??Uh...?"

        $ ntlong = 5

        show neus_exp_mouth sad_Talkingx04
        $ nteye = 7
        call neus_exp_tears_tears
        show neus_exp_iris front07
        show neus_exp_eyebrows sadx06
        with dissolve

        ne "Lo siento..."

        extend " perd??name."

        show neus_exp_mouth sad_Silentx05
        $ nteye = 8
        call neus_exp_tears_tears
        show neus_exp_iris front08
        show neus_exp_eyebrows sadx04
        with dissolve

        p "..."

        show neus_exp_mouth sad_Talkingx004
        $ nteye = 04
        call neus_exp_tears_tears
        show neus_exp_iris down04
        show neus_exp_eyebrows sadx03
        with dissolve

        ne "No deber??a estar llorando..."

        show neus_exp_mouth happy_Talkingx05
        $ nteye = 03
        call neus_exp_tears_tears
        show neus_exp_iris front03
        show neus_exp_eyebrows sadx04
        with dissolve

        ne "estoy contigo,"

        extend " a solas..."

        show neus_exp_mouth happy_Talkingx06
        $ nteye = 07
        call neus_exp_tears_tears
        show neus_exp_iris front07
        show neus_exp_eyebrows sadx03
        with dissolve

        ne "Esto es lo que he estado esperando todo este tiempo..."

        show neus_exp_mouth sad_Talkingx04
        $ nteye = 05
        call neus_exp_tears_tears
        show neus_exp_iris front05
        show neus_exp_eyebrows sadx04
        with dissolve

        ne "Pero..."

        show neus_exp_mouth sad_Talkingx05
        $ nteye = 8
        call neus_exp_tears_tears
        show neus_exp_iris front08
        show neus_exp_eyebrows sadx05
        with dissolve

        ne "Pensar??s que soy una ni??a est??pida..."

        show neus_exp_mouth sad_Silentx04
        $ nteye = 8
        call neus_exp_tears_tears
        show neus_exp_iris front08
        show neus_exp_eyebrows sadx04
        with dissolve

        pt "En realidad me pregunto cuantos a??os tendr??s realmente..."

        show neus_exp_mouth sad_Talkingx06
        $ nteye = 3
        call neus_exp_tears_tears
        show neus_exp_iris right03
        show neus_exp_eyebrows sadx04
        with dissolve

        ne "Con ellas aqu?? presentes he podido aguantar mejor las apariencias,"

        show neus_exp_mouth sad_Talkingx07
        $ nteye = 1
        call neus_exp_tears_tears
        show neus_exp_iris right01
        show neus_exp_eyebrows sadx03
        with dissolve

        ne "pero contigo a solas..."

        extend " es como..."

        show neus_exp_mouth sad_Talkingx05
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris front04
        show neus_exp_eyebrows sadx04
        with dissolve

        ne "Siento que te mereces algo mejor."

        show neus_exp_mouth sadbiting_Silentx05
        $ nteye = 6
        call neus_exp_tears_tears
        show neus_exp_iris front06
        show neus_exp_eyebrows sadx06
        with dissolve

        menu:

            pt "Algo mejor..."

            "??Por qu?? dices eso?":
                call p_Help

                $pl.ch_pts("np",1)

                show neus_exp_mouth sadbiting_Silentx06
                $ nteye = 7
                call neus_exp_tears_tears
                show neus_exp_iris front07
                show neus_exp_eyebrows sadx07
                with dissolve

                pause 0.2

            "Eso no es verdad, y lo sabes.":
                call p_Help

                $pl.ch_pts("np",2)

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris front05
                show neus_exp_eyebrows sadx06
                with dissolve

                pause 0.2

            "Todos podemos mejorar.":
                call p_Help

                show neus_exp_mouth sad_Silentx05
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_iris front08
                show neus_exp_eyebrows sadx07
                with dissolve

            "...":
                call p_Help

        ne "..."

        show neus_exp_mouth sad_Talkingx03
        $ nteye = 8
        call neus_exp_tears_tears
        show neus_exp_iris front08
        show neus_exp_eyebrows sadx04
        with dissolve

        ne "No la conociste."

        show neus_exp_mouth sad_Talkingx05
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris left04
        show neus_exp_eyebrows sadx03
        with dissolve

        ne "Pero..."

        show neus_exp_mouth sad_Talkingx07
        $ nteye = 1
        call neus_exp_tears_tears
        show neus_exp_iris left01
        show neus_exp_eyebrows sadx02
        with dissolve

        ne "Durante todo el tiempo que he estado en Barcelona,"

        show neus_exp_mouth sad_Talkingx04
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris front04
        show neus_exp_eyebrows sadx01
        with dissolve

        ne "no ha dejado de hablar maravillas sobre ti,"

        show neus_exp_mouth happy_Talkingx03
        $ nteye = 3
        call neus_exp_tears_tears
        show neus_exp_iris front03
        show neus_exp_eyebrows sadx02
        with dissolve

        ne "de lo feliz y orgullosa que se sent??a de haber tomado esa decisi??n,"

        show neus_exp_mouth sad_Talkingx05
        $ nteye = 8
        call neus_exp_tears_tears
        show neus_exp_iris front08
        show neus_exp_eyebrows sadx03
        with dissolve

        ne "de haberte visto crecer..."

        show neus_exp_mouth sadbiting_Silentx05
        $ nteye = 7
        call neus_exp_tears_tears
        show neus_exp_iris front07
        show neus_exp_eyebrows sadx04
        with dissolve

        p "..."

        show neus_exp_mouth sad_Talkingx04
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_iris front05
        show neus_exp_eyebrows sadx03
        with dissolve

        ne "Te amaba con locura."

        show neus_exp_mouth sadbiting_Silentx04
        $ nteye = 2
        call neus_exp_tears_tears
        show neus_exp_iris front02
        show neus_exp_eyebrows sadx01
        with dissolve

        p "No est?? muerta,"

        extend " ??Verdad?"

        show neus_exp_mouth sadbiting_Silentx05
        $ nteye = 8
        call neus_exp_tears_tears
        show neus_exp_iris front08
        show neus_exp_eyebrows sadx02
        with dissolve

        ne "..."

        show neus_exp_mouth sadbiting_Silentx06
        $ nteye = 6
        call neus_exp_tears_tears
        show neus_exp_iris front06
        show neus_exp_eyebrows sadx03
        with dissolve

        p "??Por qu?? hablas en pasado?"

        show neus_exp_mouth sad_Talkingx03
        $ nteye = 7
        call neus_exp_tears_tears
        show neus_exp_iris front07
        show neus_exp_eyebrows sadx02
        with dissolve

        ne "No conoces a Padre..."

        extend " ??l..."

        show neus_exp_mouth sadbiting_Silentx06
        $ nteye = 7
        call neus_exp_tears_tears
        show neus_exp_iris front07
        show neus_exp_eyebrows sadx06
        with dissolve

        p "..."

        show neus_exp_mouth sad_Talkingx03
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris left04
        show neus_exp_eyebrows sadx05
        with dissolve

        ne "Ahora mismo estar??a mejor muerta..."

        show neus_exp_mouth sadbiting_Silentx04
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_iris left05
        show neus_exp_eyebrows sadx06
        with dissolve

        p "..."

        show neus_exp_mouth sadbiting_Silentx07
        $ nteye = 7
        call neus_exp_tears_tears
        show neus_exp_iris front07
        show neus_exp_eyebrows sadx07
        with dissolve

        play sound "audio/sfx/fall07.ogg"

        if music_play != "heartbreaking":
            play music "audio/music/kevinmacleod/sad/heartbreaking.ogg" fadein 10.0 fadeout 3.0
            $ music_play = "heartbreaking"

        scene ped_hugneus_comp 01:
            subpixel True
            truecenter
            #zoom 0.35 xpos 0.47 ypos 0.42 # Full Scene
            #zoom 0.3 ypos 0.0 # To check Hand.

            #zoom 0.35 xpos 0.47 ypos 0.42 # Full Scene # TEST
            zoom 1.0 xpos 1.0 ypos 0.15 # Beginning Entrance to Face Neus.
            easein_quad 0.2 zoom 1.0 xpos 0.4 ypos 0.15 # Face Neus.

        with hpunch
        with hpunch

        n "Con cierto ??mpetu, sientes el impacto de su cuerpo contra tu pecho al descubierto,"

        ne "Por mi culpa..."

        show ped_hugneus_comp 01:
            ease 10.0 zoom 0.5 xpos 0.43 ypos 0.35 # General Scene.

        n "con su rostro oculto entre su pelo y tus pectorales,"

        ne "mam??..."

        n "empap??ndote la piel con sus l??grimas."

        menu:

            pt "[neusname]..."

            "<Abrazarla>":
                call p_Help

                $pl.ch_pts("np",3)

                $ afternight05_Pedrera_hugNeus = True

                scene ped_hugneus_comp 02:
                    subpixel True
                    truecenter
                    zoom 0.5 xpos 0.5 ypos 0.35 # General Scene.
                with Dissolve(2.0)

                n "Suavemente, la rodeas con tus brazos."

                show ped_hugneus_comp 02:
                    easein 30.0 zoom 1.0 xpos 0.4 ypos 0.15 # Face Neus.

                n "Sientes la agitada e intermitente respiraci??n que emana de entre sus sollozos,"

                n "los latidos de su coraz??n,"

                n "su c??lida mejilla junto al gimoteo de sus labios sobre tu piel."

                n "El tiempo parece transcurrir a un ritmo distinto,"

                n "a pesar de la situaci??n, del lugar,"

                n "sentirla entre tus brazos, rota por dentro y por fuera, sincera y abierta,"

                n "te deja sin saber muy bien qu?? decir."

            "<No hacer nada>":
                call p_Help

        if afternight05_Pedrera_hugNeus == False:
            show ped_hugneus_comp 01:
                zoom 1.0 xpos 0.4 ypos 0.15 # Face Neus.
            with fade

        ne "Lo siento..."

        menu:

            "Deja de decir eso.":
                call p_Help

                $pl.ch_pts("np",1)

                ne "..."

            "No necesitas pedirme perd??n.":
                call p_Help

                $pl.ch_pts("np",2)

                ne "Por supuesto que s??..."

                ne "Por mi culpa tendr??s que abandonar tu ciudad,"

                ne "no podr??s volver a ver tu padres adoptivos,"

                extend " ni a tus amigos,"

                ne "y tu vida..."

                ne "Nada volver?? a ser como antes,"

                ne "y todo es por mi culpa."

            "...":
                call p_Help

        menu:

            "Es verdad que no conoc?? a Madre, pero gracias a ella te he conocido a ti.":
                call p_Help

                $pl.ch_pts("np",2)

                ne "..."

                n "Sientes que se te arropa con m??s intensidad."

            "Tampoco es que fuera muy agradable a la vista...":
                call p_Help

                $pl.ch_pts("np",-2)

                ne "??No seas idiota!"

                ne "??Ese no es su verdadero aspecto!"

                ne "??Luc??a as?? para poder mantenerte con vida!"

                p "..."

                ne "No tienes ni idea del dolor y el sacrificio..."

                p "..."

            "...":
                call p_Help

        if afternight05_Pedrera_hugNeus == False:
            show ped_hugneus_comp 01:
                easein 25.0 zoom 0.4 xpos 0.5 ypos 0.35 
        else:
            show ped_hugneus_comp 02:
                easein 25.0 zoom 0.4 xpos 0.5 ypos 0.35             

        ne "No..."

        extend " no es as?? como hab??a imaginado nuestra primera noche..."

        if pl.np > 170: # NUMBER NOT SURE.

            ne "Tampoco cre?? que acabara enamor??ndome tan perdidamente de ti."

        elif pl.np > 120:

            ne "Tampoco cre?? que me acabar??as gustando tanto..."

        else:

            ne "Aunque me hubiera gustado tener m??s tiempo para conocerte mejor."

        p "..."

        ne "Es solo que..."

        ne "Si hubiera hecho las cosas de otra manera..."

        extend " yo..."

        menu:

            "??Puedo besarte?":
                call p_Help
                $pl.ch_pts("np",2)

                $ Pedrera_char_Cond = "NeusSuperClose"
                call Pedrera_char_lab

                show n_closefromup_mouth sadbiting_Silentx03
                show n_closefromup_iris front01
                $ nteye = 1
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows surprisex01
                with fade

                ne "..."

                show n_closefromup_mouth happy_Talkingx04
                show n_closefromup_iris front05
                $ nteye = 5
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx04
                with dissolve

                ne "Eso no lo preguntes,"

                extend " tonto."

                show n_closefromup_mouth happybiting_Silentx05
                show n_closefromup_iris front06
                $ nteye = 6
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx03
                with dissolve

                pause 0.2

                scene bg dark_a_blurry_01
                show kiss_ f_n_01:
                    truecenter
                with fade

                pause 0.2

                show kiss_ f_n_10
                with dissolve_1s

                pause 0.2

                show kiss_ f_n_12
                with dissolve_1s

                n "Acercando vuestros labios os mezcl??is en un dulce beso."

                show kiss_ f_n_02
                with dissolve_1s

                pause 0.2

                show kiss_ f_n_01
                with dissolve_1s

                pause 0.2

            "<Besarla>":
                call p_Help
                $pl.ch_pts("np",2)

                scene bg dark_a_blurry_01
                show kiss_ f_n_01:
                    truecenter
                with fade

                pause 0.2

                show kiss_ f_n_10
                with dissolve_1s

                pause 0.2

                show kiss_ f_n_12
                with dissolve_1s

                n "Acercas tus labios a los suyos y os mezcl??is en un dulce beso."

                show kiss_ f_n_02
                with dissolve_1s

                pause 0.2

                show kiss_ f_n_01
                with dissolve_1s

                pause 0.2

            "...":
                call p_Help

        if music_play != "clearWaters":
            play music "audio/music/kevinmacleod/happy/clearWaters.ogg" fadein 10.0 fadeout 3.0
            $ music_play = "clearWaters"     

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_mouth happy_Talkingx04
        show n_closefromup_iris down05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx01
        with fade

        ne "Me alegra ver que sigues teni??ndola dura,"

        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_iris front06
        $ nteye = 6
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        ne "a pesar del trote que ya llevas..."

        show n_closefromup_mouth happy_Talkingx03
        show n_closefromup_iris left04
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "Especialmente estando solamente yo en la habitaci??n."

        show n_closefromup_mouth sadbiting_Silentx04
        show n_closefromup_iris left05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        menu:

            pt "??Qu?? se supone que le debo responder a eso...?"

            "A veces s?? que pienso que eres algo est??pida.":
                call p_Help

                $pl.ch_pts("np",1)

                show n_closefromup_mouth extra_burlesque
                show n_closefromup_iris front07
                $ nteye = 7
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows angryx02
                with dissolve

                n "Ves como te saca la lengua como si fuera una ni??a peque??a."

                show n_closefromup_mouth happybiting_Silentx03
                show n_closefromup_iris front05
                $ nteye = 5
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx01
                with dissolve

                menu:

                    "Ya te he dicho que estoy enamorado de ti.":
                        call p_Help

                        #$pl.ch_pts("np",2) # Not put, it's done later.

                        call afternight05_Pedrera_ItoldYouILoveYou

                    "...":
                        call p_Help


            "Sabes perfectamente que est?? as?? de dura por ti.":
                call p_Help

                if p_prot_NotJustMasturbate_with_p_any:

                    $pl.ch_pts("np",-1)

                    show n_closefromup_mouth sad_Talkingx03
                    show n_closefromup_iris right05
                    $ nteye = 5
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows sadx02
                    with dissolve

                    ne "Me gustar??a pensar que ??nicamente es por mi,"

                    show n_closefromup_mouth sad_Talkingx05
                    show n_closefromup_iris front08
                    $ nteye = 8
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows sadx03
                    with dissolve

                    ne "pero supongo que eso ser??a pedir demasiado..."

                    show n_closefromup_mouth sadbiting_Silentx04
                    show n_closefromup_iris front05
                    $ nteye = 5
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows sadx02
                    with dissolve

                    p "??A qu?? te refieres?"

                    if p_prot_NotJustMasturbate_with_p_both == False:

                        show n_closefromup_mouth sad_Talkingx04
                        show n_closefromup_iris right04
                        $ nteye = 4
                        call n_closefromup_tears_tears
                        show n_closefromup_eyebrows sadx03
                        with dissolve

                        if p_prot_NotJustMasturbate_with_p_didac:

                            ne "Me imagino que el cuerpo de D??dac debe de gustarte mucho..."

                        elif p_prot_NotJustMasturbate_with_p_txell:

                            ne "Me imagino que no puedo competir con el cuerpo de Meritxell..."

                    else:

                        show n_closefromup_mouth sad_Talkingx06
                        show n_closefromup_iris right04
                        $ nteye = 4
                        call n_closefromup_tears_tears
                        show n_closefromup_eyebrows angryx02
                        with dissolve

                        ne "Como si no hubieras hecho nada m??s que masturbarte con ellas..."

                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_iris right05
                    $ nteye = 5
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows sadx04
                    with dissolve

                    p "..."

                    if afternight05_Pedrera_Sex_SaidJustWithNeus:

                        $pl.ch_pts("np",-2)

                        show n_closefromup_mouth sad_Talkingx03
                        show n_closefromup_iris front08
                        $ nteye = 8
                        call n_closefromup_tears_tears
                        show n_closefromup_eyebrows sadx03
                        with dissolve

                        ne "Lo m??s triste es que te hab??a cre??do..."

                        show n_closefromup_mouth happy_Talkingx04
                        show n_closefromup_iris front06
                        $ nteye = 6
                        call n_closefromup_tears_tears
                        show n_closefromup_eyebrows sadx04
                        with dissolve

                        ne "Supongo que no aprendo."

                        $ ntlong = 5

                        show n_closefromup_mouth sadbiting_Silentx05
                        show n_closefromup_iris front08
                        $ nteye = 8
                        call n_closefromup_tears_tears
                        show n_closefromup_eyebrows sadx06
                        with dissolve

                else:

                    $pl.ch_pts("np",2)

                    show n_closefromup_mouth sad_Talkingx01
                    show n_closefromup_iris front01
                    $ nteye = 1
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows surprisex02
                    with dissolve

                    ne "Euhh..."

                    $ nteye = 4

                    $ nblush = 4
                    show n_closefromup_mouth happybiting_Silentx06
                    show n_closefromup_iris right04
                    $ nteye = 4
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows sadx04
                    with dissolve

                    ne "Hmm..."

            "Ya te he dicho que estoy enamorado de ti." if afternight05_Pedrera_WhyNotKillMe_WhoILove:
                call p_Help

                call afternight05_Pedrera_ItoldYouILoveYou

            "...":
                call p_Help

        ne "..."

        menu:

            pt "En realidad ella tambi??n parece haber disfrutado bastante al final..."

            "<Decirle que no te ha gustado verla besarse con otra>" if p_didac.cumReceived == "oral" or p_txell.cumReceived == "oral":
                call p_Help

                call afternight05_Pedrera_Sex_HardToSee_kiss
                    #ne "??A qu?? te refieres...?"

            "<Decirle que te ha disgustado verla pasar su lengua por una entrepierna ajena>" if p_didac.cumReceived in ["vaginal", "anal"] or p_txell.cumReceived in ["vaginal", "anal"]:
                call p_Help

                call afternight05_Pedrera_Sex_HardToSee_oralSex
                    #ne "??A qu?? te refieres...?"

            "...":
                call p_Help

        show n_closefromup_mouth sadbiting_Silentx05
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx01
        with dissolve

        ne "..."

        show n_closefromup_mouth sad_Talkingx02
        show n_closefromup_iris right05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        ne "No me gustar??a que te sintieras obligado a hacerlo conmigo..."

        show n_closefromup_mouth sadbiting_Silentx07
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        menu:

            pt "??Obligado...?"

            "??No me crees cuando te digo que estoy enamorado de ti?" if afternight05_Pedrera_WhyNotKillMe_WhoILove:
                call p_Help

                if p_prot_NotJustMasturbate_with_p_any:

                    show n_closefromup_mouth sadbiting_Silentx02
                    show n_closefromup_iris front01
                    $ nteye = 1
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows surprisex01
                    with dissolve


                else:

                    show n_closefromup_mouth sadbiting_Silentx03
                    show n_closefromup_iris front00
                    $ nteye = 0
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows surprisex02
                    with dissolve

                ne "..."

                if p_prot_NotJustMasturbate_with_p_any:

                    $pl.ch_pts("np",-1)

                    show n_closefromup_mouth sad_Talkingx04
                    show n_closefromup_iris right04
                    $ nteye = 4
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows sadx02
                    with dissolve

                    ne "Supongo que ten??a esperanzas de que conmigo te conformaras."

                    show n_closefromup_mouth sadbiting_Silentx03
                    show n_closefromup_iris right05
                    $ nteye = 5
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows sadx03
                    with dissolve

                    p "..."

                    show n_closefromup_mouth happy_Talkingx03
                    show n_closefromup_iris down05
                    $ nteye = 5
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows sadx03
                    with dissolve

                    ne "Pero al menos me alegra saber que consigo pon??rtela dura despu??s de dos corridas."

                    show n_closefromup_mouth happybiting_Silentx03
                    show n_closefromup_iris front05
                    $ nteye = 5
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows sadx02
                    with dissolve

                    p "No seas tonta..."

                    show n_closefromup_mouth sadbiting_Silentx04
                    show n_closefromup_iris right05
                    $ nteye = 5
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows sadx03
                    with dissolve

                    ne "..."

                else:

                    $pl.ch_pts("np",3)

                    show n_closefromup_mouth sad_Talkingx05
                    show n_closefromup_iris right02
                    $ nteye = 2
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows sadx01
                    with dissolve

                    ne "Supongo..."

                    extend " que me sigue costando de creer."

                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_iris front00
                    $ nteye = 0
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows surprisex02
                    with dissolve

                    p "Pues no dudes tanto."

                    show n_closefromup_mouth happy_Silentx03
                    show n_closefromup_iris front05
                    $ nteye = 5
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows sadx02
                    with dissolve

                    ne "..."

                    show n_closefromup_mouth happybiting_Silentx06
                    show n_closefromup_iris front07
                    $ nteye = 7
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows sadx03
                    with dissolve

                    n "Una dulce sonrisa se dibuja en su rostro."

            "Deja de decir idioteces, tonta.":
                call p_Help

                $pl.ch_pts("np",1)

                show n_closefromup_mouth sad_Silentx03
                show n_closefromup_iris front01
                $ nteye = 1
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows surprisex01
                with dissolve

                ne "..."

                show n_closefromup_mouth happybiting_Silentx05
                show n_closefromup_iris front06
                $ nteye = 6
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx02
                with dissolve

                n "Una dulce sonrisa se dibuja en su rostro."

            "...":
                call p_Help


        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        ne "Aunque hay algo que quiero pedirte..."

        show n_closefromup_mouth sadbiting_Silentx05
        show n_closefromup_iris front05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        menu:

            pt "??Por qu?? ser?? que esto no suena demasiado bien...?"

            "T?? dir??s.":
                call p_Help

                $pl.ch_pts("np",1)


                show n_closefromup_mouth happy_Silentx02
                show n_closefromup_iris front05
                $ nteye = 5
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx01
                with dissolve

                
            "Espero que no me pidas meterme algo por detr??s...":
                call p_Help

                $pl.ch_pts("np",-1)

                show n_closefromup_mouth sad_Talkingx14
                show n_closefromup_iris front02
                $ nteye = 2
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows angryx04
                with dissolve

                ne "??No digas tonter??as!"

                show n_closefromup_mouth sad_Silentx08
                show n_closefromup_iris front08
                $ nteye = 8
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows angryx05
                with dissolve

                p "..."

                show n_closefromup_mouth sad_Silentx06
                show n_closefromup_iris front08
                $ nteye = 8
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows angryx03
                with dissolve

            "Por ti, lo que sea.":
                call p_Help

                $pl.ch_pts("np",2)

                show n_closefromup_mouth happy_Silentx04
                show n_closefromup_iris front05
                $ nteye = 5
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx03
                with dissolve

            "...":
                call p_Help

        ne "..."

        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx01
        with dissolve

        ne "Por favor,"

        extend " c??rrete antes de que yo tenga un orgasmo."

        show n_closefromup_mouth sadbiting_Silentx04
        show n_closefromup_iris front05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        p "????C??mo dices?!"

        show n_closefromup_mouth sadbiting_Silentx05
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        p "??Por qu?? iba a hacer eso?"

        menu:

            pt "????No quiere tener ni un orgasmo?!"

            "Quiero que lo disfrutes tanto como yo.":
                call p_Help

                $pl.ch_pts("np",1)

                show n_closefromup_mouth sadbiting_Silentx02
                show n_closefromup_iris front01
                $ nteye = 1
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx01
                with dissolve

                ne "..."

                show n_closefromup_mouth happy_Talkingx04
                show n_closefromup_iris front05
                $ nteye = 5
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx02
                with dissolve

                ne "Yo tambi??n espero disfrutarlo,"

                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_iris front08
                $ nteye = 8
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx04
                with dissolve

                ne "pero sin orgasmos..."

                show n_closefromup_mouth sadbiting_Silentx05
                show n_closefromup_iris right05
                $ nteye = 5
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx02
                with dissolve

                p "????Por qu???!"


            "Lo que quiero es que tengas tantos orgasmos que ma??ana no seas capaz ni de andar.":
                call p_Help

                $pl.ch_pts("np",2)

                show n_closefromup_mouth sad_Silentx02
                show n_closefromup_iris front00
                $ nteye = 0
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows surprisex02
                with dissolve

                ne "..."

                show n_closefromup_mouth happy_Talkingx06
                show n_closefromup_iris right01
                $ nteye = 1
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx02
                with dissolve

                ne "Bueno,"

                extend " eso tampoco ser??a muy conveniente si tenemos que salir huyendo..."

                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_iris right04
                $ nteye = 4
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx03
                with dissolve

                ne "Pero..."

                show n_closefromup_mouth sadbiting_Silentx05
                show n_closefromup_iris right05
                $ nteye = 5
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx04
                with dissolve

            "...":
                call p_Help

                show n_closefromup_mouth sadbiting_Silentx06
                show n_closefromup_iris front08
                $ nteye = 8
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx04
                with dissolve

        ne "..."

        if ntlong > 0:
            $ ntlong -= 1

        show n_closefromup_mouth sad_Talkingx003
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        ne "No-"

        extend "no quiero correrme,"

        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "no esta noche."

        show n_closefromup_mouth sadbiting_Silentx04
        show n_closefromup_iris front04
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        p "??Y se puede saber por qu?? no?"

        show n_closefromup_mouth sadbiting_Silentx08
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        ne "..."

        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_iris right02
        $ nteye = 2
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "Porque..."

        extend " si me corro..."

        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_iris right04
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        ne "te har?? cosas horribles."

        show n_closefromup_mouth sadbiting_Silentx08
        show n_closefromup_iris right05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx05
        with dissolve

        p "??A qu?? te refieres?"

        show n_closefromup_mouth sad_Talkingx06
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        ne "Cuando llego al orgasmo..."

        extend " dejo de ser yo misma."

        show n_closefromup_mouth sad_Talkingx07
        show n_closefromup_iris front01
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "Ser?? incapaz de controlar mi cuerpo y mis acciones."

        show n_closefromup_mouth sad_Talkingx09
        show n_closefromup_iris right01
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        ne "Me transformar?? en algo que es probable que acabes odiando,"

        show n_closefromup_mouth sad_Talkingx08
        show n_closefromup_iris right04
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx05
        with dissolve

        ne "y es algo que jam??s me perdonar??a."

        if night04_Neus_Blowjob_Cum_Affirmative:

            show n_closefromup_mouth sadbiting_Silentx04
            show n_closefromup_iris front01
            $ nteye = 1
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows surprisex01
            with dissolve

            p "??Es esta la raz??n por la que ayer no me dejaste hacerte nada mientras te ten??a de rodillas?"

            show n_closefromup_mouth sad_Talkingx05
            show n_closefromup_iris front05
            $ nteye = 5
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx04
            with dissolve

            ne "As?? es..."

            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_iris front08
            $ nteye = 8
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx06
            with dissolve

            p "..."

            show n_closefromup_mouth happy_Talkingx06
            show n_closefromup_iris front05
            $ nteye = 5
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx04
            with dissolve

            ne "Aunque lo disfrut?? mucho m??s de lo que te imaginas,"

            extend " en serio."

            show n_closefromup_mouth happybiting_Silentx06
            show n_closefromup_iris front06
            $ nteye = 6
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx05
            with dissolve

            pt "Creo que eso no lo pongo en duda..."

            show n_closefromup_mouth sadbiting_Silentx07
            show n_closefromup_iris front08
            $ nteye = 8
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx06
            with dissolve

        else:

            show n_closefromup_mouth sadbiting_Silentx07
            show n_closefromup_iris right05
            $ nteye = 5
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx05
            with dissolve

        p "..."

        if ntlong > 0:
            $ ntlong -= 1

        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        ne "Por eso te pido;"

        show n_closefromup_mouth sad_Talkingx004
        show n_closefromup_iris front02
        $ nteye = 2
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx05
        with dissolve

        ne "por favor..."

        extend " haz lo que sea para que no llegue al orgasmo."

        show n_closefromup_mouth sadbiting_Silentx04
        show n_closefromup_iris front01
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows surprisex01
        with dissolve

        p "??Te vas a convertir en un monstruo?"

        show n_closefromup_mouth sad_Talkingx01
        show n_closefromup_iris right00
        $ nteye = 0
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows surprisex02
        with dissolve

        ne "Euh..."

        show n_closefromup_mouth sad_Talkingx03
        show n_closefromup_iris right04
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx01
        with dissolve

        ne "M??s bien en algo no humano..."

        show n_closefromup_mouth sadbiting_Silentx08
        show n_closefromup_iris front00
        $ nteye = 0
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows surprisex02
        with dissolve

        p "??Te van a salir alas y colmillos?"

        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_iris front04
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "Es muy probable..."

        show n_closefromup_mouth sadbiting_Silentx09
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx05
        with dissolve

        pt "????Es que ni lo sabe?!"

        show n_closefromup_mouth sadbiting_Silentx12
        show n_closefromup_iris front00
        $ nteye = 0
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows surprisex02
        with dissolve

        p "??Podr??as llegar a matarme?"

        show n_closefromup_mouth sadbiting_Silentx04
        show n_closefromup_iris right01
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx01
        with dissolve

        ne "..."

        show n_closefromup_mouth sad_Talkingx003
        show n_closefromup_iris right02
        $ nteye = 2
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows suspiciousx01
        with dissolve

        ne "No..."

        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_iris right04
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "no creo que a tanto..."

        show n_closefromup_mouth sadbiting_Silentx09
        show n_closefromup_iris right05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows suspiciousx02
        with dissolve

        pt "????No cree?!"

        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        ne "Es solo que..."

        extend " saldr?? una parte de mi que no quiero que veas."

        show n_closefromup_mouth sadbiting_Silentx02
        show n_closefromup_iris front00
        $ nteye = 0
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows surprisex02
        with dissolve

        p "??Me meter??s tu cola o tu polla m??gica por detr??s?"

        show n_closefromup_mouth sad_Talkingx005
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows angryx03
        with dissolve

        ne "No,"

        show n_closefromup_mouth sad_Talkingx06
        show n_closefromup_iris front05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows angryx01
        with dissolve

        ne "a menos que me lo pidas."

        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_iris front04
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx01
        with dissolve

        ne "Lo cual no te recomiendo,"

        show n_closefromup_mouth sad_Talkingx08
        show n_closefromup_iris right02
        $ nteye = 2
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        ne "suelo ser bastante salvaje cuando..."

        show n_closefromup_mouth sad_Talkingx07
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "dejo de ser yo misma."

        show n_closefromup_mouth sadbiting_Silentx07
        show n_closefromup_iris front01
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows serious
        with dissolve

        p "Pero exactamente,"

        extend " ??en qu?? te transformar??as?"

        show n_closefromup_mouth sadbiting_Silentx05
        show n_closefromup_iris front00
        $ nteye = 0
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows normal
        with dissolve

        p "??En un demonio,"

        extend " en un drag??n,"

        extend " en una vampiresa,"

        extend " en una s??cubo,"

        extend " en una cabra...?"

        show n_closefromup_mouth sadbiting_Silentx08
        show n_closefromup_iris right02
        $ nteye = 2
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows suspiciousx01
        with dissolve

        ne "..."

        show n_closefromup_mouth sad_Talkingx07
        show n_closefromup_iris right01
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows surprisex01
        with dissolve

        ne "Generalmente me transformo en aquello que mi cuerpo pide..."

        show n_closefromup_mouth sadbiting_Silentx09
        show n_closefromup_iris front00
        $ nteye = 0
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows surprisex02
        with dissolve

        p "No me aclaras una mierda con eso."

        show n_closefromup_mouth sad_Talkingx03
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "Lo siento..."

        show n_closefromup_mouth sadbiting_Silentx11
        show n_closefromup_iris right04
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        pt "No s?? si sentirme excitado o aterrorizado..."

        # CONDITIONAL

        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_iris front05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "Lo mejor ser??a que te masturbaras en frente de m??,"

        if p_prot_NotJustMasturbate_with_p_both == False:

            show n_closefromup_mouth sad_Talkingx04
            show n_closefromup_iris front08
            $ nteye = 8
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx05
            with dissolve

            ne "como has hecho con ellas..."

        else:

            if p_prot_NotJustMasturbate_with_p_didac == True:

                show n_closefromup_mouth sad_Talkingx05
                show n_closefromup_iris front08
                $ nteye = 8
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx06
                with dissolve

                ne "como has hecho con D??dac..."

            elif p_prot_NotJustMasturbate_with_p_txell == True:

                show n_closefromup_mouth sad_Talkingx04
                show n_closefromup_iris front08
                $ nteye = 8
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx04
                with dissolve

                ne "como has hecho con Txell..."

        show n_closefromup_mouth sad_Talkingx004
        show n_closefromup_iris right04
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        ne "aunque confieso que me gustar??a poder sentirla dentro de m??..."

        show n_closefromup_mouth sadbiting_Silentx12
        show n_closefromup_iris right05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        p "..."

        show n_closefromup_mouth sad_Talkingx06
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        ne "D??nde elijas terminar,"

        extend " tambi??n ser?? cosa tuya..."

        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_iris front04
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        ne "al fin y al cabo es tu esperma."

        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        ne "Pero..."

        extend " si me transformo,"

        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_iris front05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx05
        with dissolve

        ne "me temo que ya no podr??s tomar muchas m??s elecciones."

        show n_closefromup_mouth sadbiting_Silentx09
        show n_closefromup_iris front01
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx01
        with dissolve

        p "??Me vas a violar?"

        show n_closefromup_mouth sadbiting_Silentx11
        show n_closefromup_iris right01
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "..."

        show n_closefromup_mouth sad_Talkingx02
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx05
        with dissolve

        ne "Es muy probable."

        show n_closefromup_mouth sadbiting_Silentx14
        show n_closefromup_iris front06
        $ nteye = 6
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx06
        with dissolve

        p "..."

        show n_closefromup_mouth sad_Talkingx08
        show n_closefromup_iris front02
        $ nteye = 2
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx05
        with dissolve

        ne "Solo te pido eso, [protname]."

        if ntlong < 5:
            $ ntlong += 1

        show n_closefromup_mouth sad_Talkingx02
        show n_closefromup_iris front05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx05
        with dissolve

        ne "Por favor,"

        extend " c??rrete antes de que yo lo haga."

        call afternight05_Pedrera_NeusNaked

        jump afternight05_Pedrera_Sex_before


label afternight05_Pedrera_NeusNaked:

    if night05_elysium_NeusNaked:

        $ night05_elysium_NeusNaked = True

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show bg el_bedroom_b:
            truecenter
            zoom 0.5

        show n_closefromup_mouth sadbiting_Silentx06
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with fade_short

    else:

        show n_closefromup_mouth sadbiting_Silentx06
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

    p "..."

    if music_play != "musicForManatees":
        play music "audio/music/kevinmacleod/happy/musicForManatees.ogg" fadein 10.0 fadeout 3.0
        $ music_play = "musicForManatees"

    if not gensex_INotLoveYouNeus:

        scene bg dark_a_blurry_01
        show kiss_ n_n_03:
            truecenter
            zoom 1.4
            rotate -25
        with fade

        n "Vuelve a ponerse de puntillas para acercarse a tus labios y darte un dulce beso,"

    else:

        n "Te mira con cara de circunstancias"

    scene pedrera05_neus_complete_body sd_image:
        subpixel True
        truecenter
        zoom 4.5 ypos 0.9 # Head
        easein_quad 25.0 ypos -0.2 # Boobs.
    with fade

    ne "..."

    show pedrera05_neus_complete_body naked_image
    with Dissolve(1.5)

    n "mientras desabrocha el lazo frontal que sujeta su reducido cors??,"

    n "exhibiendo as?? sus modestos pechos con sus pezones duros y rosados."

    window hide dissolve
    pause

    scene pedrera05_neus_complete_body sd_image:
        subpixel True
        truecenter
        zoom 5.0 ypos -1.4 # Pelvis
        easein_quad 25.0 ypos -2.1 # Vagina
    with fade

    n "seguidamente oyes como se quita el cintur??n y deja caer su diminuta falda al suelo,"

    show pedrera05_neus_complete_body naked_image
    with Dissolve(1.5)

    n "al mismo tiempo que se quita las medias, sus hombreras, y la cinta que le rodea el cuello."

    window hide dissolve
    pause

    $ Pedrera_char_Cond = "NeusFar"
    call Pedrera_char_lab

    if night05_elysium_NeusNaked:
        show bg el_bedroom_blur:
            truecenter
            zoom 0.5

    show neus_body naked
    show neus_arm_l naked
    show neus_arm_r naked

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx05
    with fade

    n "Completamente desnuda ante ti:"

    show neus_exp_mouth sad_Talkingx06
    $ nteye = 8
    call neus_exp_tears_tears
    show neus_exp_iris front08
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "Siento que tengas que conformarte con esto..."

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_iris front06
    show neus_exp_eyebrows sadx06
    with dissolve

    menu:

        pt "Realmente, tiene menos autoestima que una prostituta de noventa y nueve centavos..."

        "Idiota.":
            call p_Help
            $pl.ch_pts("np",1)

            if gensex_INotLoveYouNeus:
                $pl.ch_pts("np",-1)

                show neus_exp_mouth sad_Talkingx04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris right04
                show neus_exp_eyebrows sadx05
                with dissolve

                ne "Tampoco hace falta que me llames as??..."

                show neus_exp_mouth sad_Silentx08
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris right05
                show neus_exp_eyebrows sadx07
                with dissolve

            else:
                $pl.ch_pts("np",1)

            $ Pedrera_char_Cond = "NeusSuperClose"
            call Pedrera_char_lab

            show n_closefromup_body naked

            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_iris front00
            $ nteye = 0
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows surprisex02
            with fade_short

            n "Te acercas sugerentemente hacia ella."

            if gensex_INotLoveYouNeus:

                show n_closefromup_mouth sad_Silentx04
                show n_closefromup_iris right05
                $ nteye = 5
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx03
                with dissolve

                pause 0.2

            else:

                show n_closefromup_mouth happy_Silentx04
                show n_closefromup_iris front06
                $ nteye = 6
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx02
                with dissolve

                n "Una gr??cil sonrisa aparece en sus labios."

        "Tambi??n podr??as modificar tu cuerpo si quisieras.":

            call p_Help

            $pl.ch_pts("np",-2)

            if ntlong < 5:
                $ ntlong += 1

            show neus_exp_mouth sadbiting_Silentx06
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows angryx03
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx09
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows angryx04
            with dissolve

            ne "No es algo que pueda hacer a la ligera,"

            show neus_exp_mouth sad_Talkingx08
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows angryx04
            with dissolve

            ne "adem??s necesito toda la energ??a posible para poder escapar ma??ana,"

            show neus_exp_mouth sad_Talkingx07
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris right02
            show neus_exp_eyebrows angryx02
            with dissolve

            ne "no..."

            extend " no creo que sea momento para..."

            show neus_exp_mouth sadbiting_Silentx07
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx04
            with dissolve

            p "..."

            show neus_exp_mouth sad_Talkingx04
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx06
            with dissolve

            ne "Supongo que he sido un poco ilusa al pensar"

            show neus_exp_mouth sad_Talkingx05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx05
            with dissolve

            ne "que te conformar??as con mi cuerpo actual..."

            show neus_exp_mouth sad_Silentx08
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx06
            with dissolve

            p "[neusname]..."

            show neus_exp_mouth sad_Talkingx04
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris left05
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "No importa,"

            show neus_exp_mouth sad_Talkingx02
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris left05
            show neus_exp_eyebrows sadx05
            with dissolve

            ne "ahora..."

            show neus_exp_mouth sadbiting_Silentx06
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx06
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusSuperClose"
            call Pedrera_char_lab

            show n_closefromup_body naked

            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_iris front08
            $ nteye = 8
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx05
            with fade

            n "Se acerca tambaleante hasta a escasos cent??metros de ti."

        "Eres perfecta tal y como eres." if not gensex_INotLoveYouNeus:
            call p_Help

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows surprisex02
            with dissolve

            ne "..."

            show neus_exp_mouth happy_Talkingx03
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris front03
            show neus_exp_eyebrows sadx01
            with dissolve

            ne "Mira que eres cursi cuando quieres..."

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows surprisex01
            with dissolve

            p "Lo digo en serio."

            if p_prot_NotJustMasturbate_with_p_any:

                $pl.ch_pts("np",-2)

                show neus_exp_mouth sad_Talkingx05
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris right04
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "Me resultar??a m??s f??cil de creer"

                show neus_exp_mouth sad_Talkingx04
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris right05
                show neus_exp_eyebrows sadx04
                with dissolve

                if p_prot_NotJustMasturbate_with_p_both == True:

                    ne "si no fuera porque con ellas no te has conformado con solo masturbarte..."

                else:

                    if p_prot_NotJustMasturbate_with_p_didac == True:

                        ne "si no fuera porque con D??dac no te has conformado solo con masturbarte..."

                    elif p_prot_NotJustMasturbate_with_p_txell == True:

                        ne "si no fuera porque con Txell no te has conformado solo con masturbarte..."

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_iris front08
                show neus_exp_eyebrows sadx04
                with dissolve

                p "..."

                show neus_exp_mouth sad_Talkingx02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "Tranquilo,"

                extend " lo entiendo..."

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris right04
                show neus_exp_eyebrows sadx04
                with dissolve

                p "[neusname]..."

                show neus_exp_mouth sadbiting_Silentx06
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_iris front08
                show neus_exp_eyebrows sadx05
                with dissolve

                $ Pedrera_char_Cond = "NeusSuperClose"
                call Pedrera_char_lab

                show n_closefromup_body naked

                show n_closefromup_mouth sadbiting_Silentx05
                show n_closefromup_iris front08
                $ nteye = 8
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx05
                with fade

            else:

                $pl.ch_pts("np",2)

                show neus_exp_mouth sadbiting_Silentx02
                $ nteye = 0
                call neus_exp_tears_tears
                show neus_exp_iris front00
                show neus_exp_eyebrows surprisex02
                with dissolve

                ne "..."

                show neus_exp_mouth happy_Talkingx04
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris right03
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "Gracias..."

                show neus_exp_mouth happybiting_Silentx05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris front05
                show neus_exp_eyebrows sadx04
                with dissolve

                p "..."

                show neus_exp_mouth happy_Talkingx08
                $ nteye = 7
                call neus_exp_tears_tears
                show neus_exp_iris front07
                show neus_exp_eyebrows sadx05
                with dissolve

                ne "De verdad."

                show neus_exp_mouth happy_Silentx07
                $ nteye = 6
                call neus_exp_tears_tears
                show neus_exp_iris front06
                show neus_exp_eyebrows sadx04
                with dissolve

                p "..."

                $ Pedrera_char_Cond = "NeusSuperClose"
                call Pedrera_char_lab

                show n_closefromup_body naked

                show n_closefromup_mouth happybiting_Silentx05
                show n_closefromup_iris front06
                $ nteye = 6
                call n_closefromup_tears_tears
                show n_closefromup_eyebrows sadx02
                with fade

                n "Se te acerca lentamente."

    return

label afternight05_Pedrera_Sex_before:

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_body naked

        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_iris front05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "Soy toda tuya."

        call endtranslation

        show n_closefromup_mouth happybiting_Silentx02
        show n_closefromup_iris front06
        $ nteye = 6
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        $ ntlong = 1
        $ nblush = 3
        $ nblushNumber = "03"

        $ p_girl_active = p_neus
        $ p_active = "p_neus"
        $ p_activen = "neus"
        $ p_activeno = "_n"
        $ nleye = "horny"
        $ ped_neus_whispers_sfx03 = 0.0
        $ ped_neus_whispers_sfx04 = 0.0

        call p_any_restart

        jump afternight05_Pedrera_Sex

    


#     $ self.orgasm = 0 # How many orgasms did you had.
#     $ self.closeOrgasm = 0 # How close is to Orgasm.
#     $ self.pleasure = 0 # How much pain or pleasure you're having, even if you're far from orgasm.

label afternight05_Pedrera_Sex_DTChoose:

    $ p_didac.throat_dilatation = afternight04__MMouth_dick_Deep_Success - afternight04__MMouth_dick_Deep_Failed

    menu:

        pt "??Con quien?"

        "<D??dac>":
            call p_Help

            $ p_girl_active = p_didac
            $ p_active = "p_didac"
            $ p_activen = "didac"
            $ p_activeno = "_d"

            jump afternight05_Pedrera_Sex

        "<Txell>":
            call p_Help

            $ p_girl_active = p_txell
            $ p_active = "p_txell"
            $ p_activen = "txell"
            $ p_activeno = "_m"

            jump afternight05_Pedrera_Sex

            #call WIP
            #jump afternight05_Pedrera_Sex_DTChoose

        "<Con las dos a la vez>":
            call p_Help

            #$ p_girl_active = p_both
            $ p_active = "p_both"
            $ p_activen = "both"
            $ p_activeno = "_b"

            call WIP

            jump afternight05_Pedrera_Sex_DTChoose



label afternight05_Pedrera_Sex:

    if p_active == "p_didac":

        if p_didac.start == 0:

            if music_play != "funkorama":
                play music "audio/music/kevinmacleod/happy/funkorama.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "funkorama"

            $ p_didac.start = 1

            if p_txell.start > 0:

                show didacf_mouth sad_Talkingx05
                show didacf_eyes 03
                show didacf_pupils front03
                show didacf_eyebrows angryx03
                with dissolve

                d "Te acuerdas de mi,"

                extend " ??verdad?"

                show didacf_mouth sad_Talkingx08
                show didacf_eyes 04
                show didacf_pupils front04
                show didacf_eyebrows angryx04
                with dissolve

                d "??Acaso soy tu segundo plato?"

                if DidacSex_Vaginal:

                    show didacf_mouth sadbiting_Silentx02
                    show didacf_eyes 00
                    show didacf_pupils front00
                    show didacf_eyebrows surprisex01
                    with dissolve

                    p "??No crees que ya te he follado bastante estos ??ltimos d??as?"

                    show didacf_mouth sad_Talkingx004
                    show didacf_eyes 08
                    show didacf_pupils front08
                    show didacf_eyebrows normal
                    with dissolve

                    d "Creo que nunca es suficiente."

                else:

                    show didacf_mouth sad_Silentx06
                    show didacf_eyes 05
                    show didacf_pupils front05
                    show didacf_eyebrows angryx04
                    with dissolve

                    menu:

                        pt "??Segundo plato?"

                        "Te he reservado en segundo lugar, para durar m??s tiempo contigo.":
                            call p_Help

                            $pl.ch_pts("dp",2)
                            $pl.ch_pts("mp",-2)
                            $pl.ch_pts("np",-1)

                            show didacf_blush 03
                            show didacf_mouth sad_Silentx02
                            show didacf_eyes 01
                            show didacf_pupils front01
                            show didacf_eyebrows surprisex02
                            with dissolve

                            d "..."

                            show didacf_blush 04
                            show didacf_mouth sad_Talkingx03
                            show didacf_eyes 02
                            show didacf_pupils front02
                            show didacf_eyebrows sadx01
                            with dissolve

                            d "Euhm..."

                            show didacf_mouth sad_Talkingx08
                            show didacf_eyes 04
                            show didacf_pupils front04
                            show didacf_eyebrows angryx04
                            with dissolve

                            d "????Me est??s tomando el pelo?!"

                            show didacf_mouth sad_Silentx03
                            show didacf_eyes 02
                            show didacf_pupils front02
                            show didacf_eyebrows serious
                            with dissolve

                            p "??No me crees...?"

                            show didacf_blush 05
                            show didacf_mouth sadbiting_Silentx03
                            show didacf_eyes 01
                            show didacf_pupils left01
                            show didacf_eyebrows suspiciousx01
                            with dissolve

                            d "..."

                            show didacf_blush 03
                            show didacf_mouth sad_Talkingx09
                            show didacf_eyes 08
                            show didacf_pupils front08
                            show didacf_eyebrows angryx04
                            with dissolve

                            d "??No me seas gilipollas!"

                        "Tienes unos pechos grandes D??dac, pero no tanto como Meritxell...":
                            call p_Help

                            $pl.ch_pts("dp",-2)
                            $pl.ch_pts("np",-3)
                            $pl.ch_pts("mp",2)

                            show didacf_mouth sad_Silentx02
                            show didacf_eyes 01
                            show didacf_pupils front01
                            show didacf_eyebrows surprisex02
                            with dissolve

                            d "..."

                            show didacf_mouth sad_Talkingx03
                            show didacf_eyes 02
                            show didacf_pupils front02
                            show didacf_eyebrows suspiciousx02
                            with dissolve

                            d "Se..."

                            show didacf_mouth sad_Talkingx09
                            show didacf_eyes 01
                            show didacf_pupils front01
                            show didacf_eyebrows angryx04
                            with dissolve

                            d "??SER??S CAPULLO!"

                            show didacf_mouth sad_Silentx02
                            show didacf_eyes 00
                            show didacf_pupils right00
                            show didacf_eyebrows serious
                            with dissolve

                            tx "??Te molesta la verdad?"

                            show didacf_mouth sad_Silentx05
                            show didacf_eyes 08
                            show didacf_pupils right08
                            show didacf_eyebrows angryx03
                            with dissolve

                            pause 0.2

                            $ Pedrera_char_Cond = "TxellClose_b"
                            call Pedrera_char_lab

                            show m_exp_mouth happy_Silentx05
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            show m_exp_eyebrows suspiciousx01
                            with fade_short

                            d "..."

                            show m_exp_mouth sad_Silentx02
                            show m_exp_eyes 00
                            show m_exp_piris front00
                            show m_exp_eyebrows surprisex002
                            with dissolve

                            d "??Al menos no parecer?? {a=https://es.wikipedia.org/wiki/Quasimodo}el jorobado de {i}Notre Dame{/i}{/a} dentro de unos a??os!"

                            show m_exp_mouth sad_Silentx07
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            show m_exp_eyebrows angryx05
                            with dissolve

                            tx "..."

                            show m_exp_mouth sad_Silentx08
                            show m_exp_eyes 08
                            show m_exp_piris front08
                            show m_exp_eyebrows angryx04
                            with dissolve

                            $ Pedrera_char_Cond = "DidacClose"
                            call Pedrera_char_lab

                        "??Est??s celosa?":
                            call p_Help

                            $pl.ch_pts("dp",1)

                            show didacf_mouth sad_Silentx02
                            show didacf_eyes 00
                            show didacf_pupils front00
                            show didacf_eyebrows surprisex02
                            with dissolve

                            d "..."

                            show didacf_blush 03
                            show didacf_mouth sad_Talkingx02
                            show didacf_eyes 01
                            show didacf_pupils front01
                            show didacf_eyebrows normal
                            with dissolve

                            d "??Qu??...?"

                            show didacf_blush 04
                            show didacf_mouth sad_Talkingx07
                            show didacf_eyes 02
                            show didacf_pupils front02
                            show didacf_eyebrows angryx03
                            with dissolve

                            d "????De qu?? co??o hablas imb??cil?!"

                            show didacf_mouth sad_Silentx05
                            show didacf_eyes 01
                            show didacf_pupils right01
                            show didacf_eyebrows serious
                            with dissolve

                            tx "Est?? claro que no se equivoca."

                            show didacf_mouth sad_Talkingx06
                            show didacf_eyes 02
                            show didacf_pupils right02
                            show didacf_eyebrows angryx03
                            with dissolve

                            d "????C??mo dices?!"

                            $ Pedrera_char_Cond = "TxellClose_b"
                            call Pedrera_char_lab

                            show m_exp_mouth happy_Talkingx05
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            show m_exp_eyebrows sadx01
                            with fade_short

                            tx "Eres m??s transparente que un papel de {a=https://es.wikipedia.org/wiki/Celof??n}celof??n{/a}."

                            show m_exp_mouth happy_Silentx04
                            show m_exp_eyes 05
                            show m_exp_piris front05
                            show m_exp_eyebrows angryx02s
                            with dissolve

                            pause 0.2

                            $ Pedrera_char_Cond = "DidacClose"
                            call Pedrera_char_lab

                            show didacf_mouth sad_Talkingx003
                            show didacf_eyes 05
                            show didacf_pupils right05
                            show didacf_eyebrows angryx04
                            with fade_short

                            d "??No estoy celosa!"

                            show didacf_mouth sad_Silentx03
                            show didacf_eyes 00
                            show didacf_pupils right00
                            show didacf_eyebrows serious
                            with dissolve

                            tx "??Entonces por qu?? est??s gritando?"

                            show didacf_mouth sad_Silentx06
                            show didacf_eyes 03
                            show didacf_pupils left03
                            show didacf_eyebrows angryx04
                            with dissolve

                            d "..."

                            show didacf_mouth sad_Talkingx07
                            show didacf_eyes 08
                            show didacf_pupils front08
                            show didacf_eyebrows angryx04
                            with dissolve

                            d "??Sois un par de imb??ciles!"

                            show didacf_mouth sadbiting_Silentx04
                            show didacf_eyes 05
                            show didacf_pupils front05
                            show didacf_eyebrows angryx03
                            with dissolve

                            d "..."

                        "...":
                            call p_Help

                            pass


                show didacf_mouth sad_Talkingx05
                show didacf_eyes 04
                show didacf_pupils front04
                show didacf_eyebrows angryx03
                with dissolve

                d "Ahora c??llate y empieza."

                show didacf_mouth sadbiting_Silentx04
                show didacf_eyes 05
                show didacf_pupils front05
                show didacf_eyebrows sadx01
                with dissolve


            else:

                if music_play != "funkorama":
                    play music "audio/music/kevinmacleod/happy/funkorama.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "funkorama"

                $ p_didac.start = 1

                $ Pedrera_char_Cond = "DidacClose"
                call Pedrera_char_lab

                show didacf_mouth happy_Talkingx05
                $ dteye = 3
                call didac_exp_tears_tears
                show didacf_pupils front03
                show didacf_eyebrows surprisex01
                with fade

                d "Vaya..."

                show didacf_mouth happy_Talkingx03
                $ dteye = 5
                call didac_exp_tears_tears
                show didacf_pupils front05
                show didacf_eyebrows surprisex02
                with dissolve

                d "Que honor que empieces conmigo."

                if afternight04_Anal_dick_med_Speed_1_Done > 0:

                    show didacf_mouth happy_Talkingx05
                    $ dteye = 2
                    call didac_exp_tears_tears
                    show didacf_pupils front02
                    show didacf_eyebrows suspiciousx01
                    with dissolve

                    d "??Y bien...?"

                    show didacf_mouth happy_Talkingx04
                    $ dteye = 5
                    call didac_exp_tears_tears
                    show didacf_pupils front05
                    show didacf_eyebrows angryx01
                    with dissolve

                    d "??Por d??nde me la quieres meter?"

                    show didacf_mouth happybiting_Silentx05
                    $ dteye = 4
                    call didac_exp_tears_tears
                    show didacf_pupils front04
                    show didacf_eyebrows angryx01
                    with dissolve

                else:

                    show didacf_mouth happybiting_Silentx03
                    $ dteye = 4
                    call didac_exp_tears_tears
                    show didacf_pupils front04
                    show didacf_eyebrows suspiciousx01
                    with dissolve


    elif p_active == "p_txell":

        if music_play != "grooveGrove":
            play music "audio/music/kevinmacleod/sad/grooveGrove.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "grooveGrove"

        if p_txell.start == 0:

            #########################################################

            if config.version < "00.15.04": #
                call endupdatescript
            
            #######################################################

            $ p_txell.start = 1

            if p_didac.start > 1:

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows suspiciousx02
                with dissolve

                tx "Hmm..."

                show m_exp_mouth sad_Talkingx002
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows surprisex01
                with dissolve

                tx "No voy a negar que me ha dolido que lo eligieras a ??l antes que a mi,"

                show m_exp_mouth sad_Talkingx03
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows surprisex002
                with dissolve

                tx "pero supongo que es normal."

                show m_exp_mouth sad_Talkingx003
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex001
                with dissolve

                tx "??l te da m??s f??cilmente lo que le pides,"

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows surprisex002
                with dissolve

                tx "y eso es lo que te gusta,"

                extend " ??no?"

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 01
                show m_exp_piris front01
                show m_exp_eyebrows surprisex02
                with dissolve

                p "??Te vas a quejar todo el rato?"

                show m_exp_mouth sadbiting_Silentx04
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows angryx03
                with dissolve

                tx "..."

                show m_exp_mouth sad_Talkingx003
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows suspiciousx02
                with dissolve

                tx "??Qu?? quieres que haga?"

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows serious
                with dissolve

            else:

                #########################################################

                if config.version < "00.15.04": #
                    call endupdatescript
                
                #######################################################

                $ p_txell.start = 1

                $ Pedrera_char_Cond = "TxellClose_b"
                call Pedrera_char_lab

                show m_exp_mouth happy_Talkingx04
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx02
                with fade

                tx "As?? que quieres empezar conmigo..."

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows suspiciousx01
                with dissolve

                tx "Pensaba que te molaba follarte a tu amigo tetudo."

                show m_exp_mouth happy_Silentx04
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows angryx01
                with dissolve

                menu:

                    "T?? las tienes m??s grandes.":
                        call p_Help

                        $pl.ch_pts("dp",-2)
                        $pl.ch_pts("mp",3)
                        $pl.ch_pts("np",-1)

                        show m_exp_mouth sad_Silentx02
                        show m_exp_eyes 02
                        show m_exp_piris front02
                        show m_exp_eyebrows surprisex01
                        with dissolve

                        tx "..."

                        show m_exp_mouth happy_Silentx05
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows angryx01
                        with dissolve

                        tx "Hmm..."

                        show m_exp_mouth happy_Talkingx06
                        show m_exp_eyes 03
                        show m_exp_piris front03
                        show m_exp_eyebrows angryx02
                        with dissolve

                        tx "Y te aseguro que s?? hacerlo mejor que ??l."

                        show m_exp_mouth happy_Silentx06
                        show m_exp_eyes 05
                        show m_exp_piris right05
                        show m_exp_eyebrows surprisex001
                        with dissolve

                    "Te he elegido a ti primera, para tener m??s tiempo con D??dac despu??s.":
                        call p_Help

                        $pl.ch_pts("dp",2)
                        $pl.ch_pts("mp",-1)

                        show m_exp_mouth sad_Silentx04
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows suspiciousx01
                        with dissolve

                        tx "Hmmm..."

                        show m_exp_mouth sad_Talkingx04
                        show m_exp_eyes 04
                        show m_exp_piris left04
                        show m_exp_eyebrows surprisex002
                        with dissolve

                        tx "Quiz??s sea mejor as??."

                        show m_exp_mouth sadbiting_Silentx03
                        show m_exp_eyes 05
                        show m_exp_piris left05
                        show m_exp_eyebrows normal
                        with dissolve

                    "??No quieres que empiece contigo?":
                        call p_Help

                        $pl.ch_pts("dp",-1)

                        show m_exp_mouth sad_Silentx03
                        show m_exp_eyes 03
                        show m_exp_piris front03
                        show m_exp_eyebrows normal
                        with dissolve

                        tx "Hmmm..."

                        show m_exp_mouth sad_Talkingx04
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows surprisex002
                        with dissolve

                        tx "Cuanto antes terminemos con esto,"

                        extend " quiz??s mejor."

                        show m_exp_mouth sad_Silentx03
                        show m_exp_eyes 05
                        show m_exp_piris right05
                        show m_exp_eyebrows normal
                        with dissolve

    elif p_active == "p_neus":

        if music_play != "forever_dreaming":
            play music "audio/music/alcaknight/forever_dreaming.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "forever_dreaming"

        if p_neus.start == 0:
            #progcheck "beginning"
            $ p_neus.start = 1

        # else:
        #     progcheck "Not beginning"

    menu afternight05_Pedrera_Sex_choice(screen="dun_choice_screen"):

        pt "??Qu?? postura elijo?"

        "Ponerla de rodillas":
            call p_Help

            if p_active == "p_didac":
                #########################################################
                if config.version < "00.14.09": # You can have Blowjob with Didac.
                    call endupdatescript
                #######################################################
            elif p_active == "p_txell":
                #########################################################
                if config.version < "00.15.05": # You can have Blowjob with Txell.
                    call endupdatescript
                #######################################################
            elif p_active == "p_neus":
                #########################################################
                if config.version < "00.15.07": # You can have Blowjob with Neus.
                    call endupdatescript
                #######################################################

            if p_active == "p_neus":
                $ p_neuspos = "gensex_oral_n_frontHead_exp_"

            call afternight05_Pedrera_Sex_changeposNull

            $ ped_sex_general_action_Cond = "o00_00"

            $ p_prot.pos = "oral"
            $ p_prot.pos_oral += 1

            if p_active == "p_didac":
                $ p_didac.pos = "oral"
                $ p_didac.pos_oral += 1
            elif p_active == "p_txell":
                $ p_txell.pos = "oral"
                $ p_txell.pos_oral += 1
            elif p_active == "p_neus":
                # if programming_check == False: 
                #     call WIP
                #     jump afternight05_Pedrera_Sex_choice

                $ p_neus.pos = "oral"
                $ p_neus.pos_oral += 1

        "Ponerla abierta de piernas sobre la cama":
            call p_Help

            if p_active == "p_didac":
                #########################################################
                if config.version < "00.15.01": #
                    call endupdatescript
                #######################################################
            # elif p_active == "p_txell":
            #     #########################################################
            #     if config.version < "00.15.05": #
            #         call endupdatescript
            #     #######################################################
            elif p_active == "p_neus":
                #########################################################
                if config.version < "00.15.09": #
                    call endupdatescript
                #######################################################

            if p_active == "p_neus":
                $ p_neuspos = "gensex_missionary_n_head_exp_"

            call afternight05_Pedrera_Sex_changeposNull

            $ p_prot.pos = "missionary"
            $ p_prot.pos_missionary += 1

            if p_active == "p_didac":
                $ p_didac.pos = "missionary"
                $ p_didac.pos_missionary += 1
            elif p_active == "p_txell":

                if p_txell_NoSex_Confirmed:
                    jump afternight05_Pedrera_Sex_label

                elif FuckM_Start_Cond == False:
                    $ p_txell.pos = "missionary"
                    jump p_txell_NoSex

                else:

                    $ p_txell.pos = "missionary"
                    $ p_txell.pos_missionary += 1

            elif p_active == "p_neus":
                $ p_neus.pos = "missionary"
                $ p_neus.pos_missionary += 1

        "Ponerla a cuatro patas sobre la cama":
            call p_Help

            if p_active == "p_didac":
                #########################################################
                if config.version < "00.15.01": #
                    call endupdatescript
                #######################################################
            # elif p_active == "p_txell":
            #     #########################################################
            #     if config.version < "00.15.05": #
            #         call endupdatescript
            #     #######################################################
            elif p_active == "p_neus":
                #########################################################
                if config.version < "00.15.09": #
                    call endupdatescript
                #######################################################

            call afternight05_Pedrera_Sex_changeposNull

            $ p_prot.pos = "doggy"
            $ p_prot.pos_doggy += 1

            if p_active == "p_didac":
                $ p_didac.pos = "doggy"
                $ p_didac.pos_doggy += 1

            elif p_active == "p_txell":

                if p_txell_NoSex_Confirmed:
                    jump afternight05_Pedrera_Sex_label

                elif FuckM_Start_Cond == False:
                    $ p_txell.pos = "doggy"
                    jump p_txell_NoSex

                else:
                    $ p_txell.pos = "doggy"
                    $ p_txell.pos_doggy += 1

            elif p_active == "p_neus":
                $ p_neus.pos = "doggy"
                $ p_neus.pos_doggy += 1

        "Hacer un 69 sobre la cama":
            call p_Help

            if p_active == "p_didac":
                #########################################################
                if config.version < "00.14.09": #
                    call endupdatescript
                #######################################################
            elif p_active == "p_txell":
                #########################################################
                if config.version < "00.15.03": #
                    call endupdatescript
                #######################################################
            elif p_active == "p_neus":
                #########################################################
                if config.version < "00.16.01": #
                    call endupdatescript
                #######################################################

            call afternight05_Pedrera_Sex_changeposNull

            $ p_prot.pos = "69"
            #$ p_prot.pos_69 += 1

            if p_active == "p_didac":
                $ p_didac.pos = "69"
                #$ p_didac.pos_69 += 1
            elif p_active == "p_txell":
                $ p_txell.pos = "69"
                #$ p_txell.pos_69 += 1
            elif p_active == "p_neus":

                # if programming_check == False: 
                #     call WIP
                #     jump afternight05_Pedrera_Sex_choice

                $ p_neus.pos = "69"
                #$ p_neus.pos_69 += 1

    $ p_prot.action = "rest"
    $ p_didac.action = "rest"
    $ p_txell.action = "rest"
    $ p_neus.action = "rest"

    scene black
    with fade

    call expression "afternight05_Pedrera_Sex_" + p_active + "_" + p_prot.pos

    call afternight05_Pedrera_Sex_After

    jump afternight05_Pedrera_Sex_action

label afternight05_Pedrera_Sex_action:

    if p_prot.pos == "missionary" and p_txell_cunnilingus_received_from_p_didac_at_missionary > 1:
        $ p_txell_cunnilingus_received_from_p_didac_at_missionary += 1
        $ p_didac.action = "cunnilingus_done_p_txell"

    elif p_prot.pos == "missionary" and p_txell_cunnilingus_received_from_p_didac_at_missionary == 1:
        pass

    else:
        if p_didac.action == "cunnilingus_done_p_txell":
            $ p_didac.b_action = "" # not finished, I don't know if this is correct...

    if p_prot.pos == "oral" and p_prot_anal_fingered_received_from_p_txell > 0 and p_prot.action not in ["titwank_received_TRY", "titwank_received"]:
        $ p_prot.b_action = "anal_fingered_received"

    else:

        if p_prot.b_action == "anal_fingered_received":
            $ p_didac.b_action = ""

    menu afternight05_Pedrera_Sex_action_choice(screen="dun_choice_screen"):

        "<Seguir sin hacer nada>" if p_prot.action == "rest" and p_prot.b_action == "rest":

            call p_Help

            $ p_prot_sameAction = True

        "<Seguir igual>" if p_prot.action != "rest" or p_prot.b_action != "rest": # This one can be problematic.

            call p_Help

            $ p_prot_sameAction = True

        "<Masturbarte>" if p_prot.pos == "oral" and p_prot.action in ["rest", "takeDickOut"]: # and p_prot.b_action == "rest": No because Txell finger you.
            call p_Help

            $ p_prot.action = "masturbate"

        "<Dejar de masturbarte>" if p_prot.pos == "oral" and p_prot.action in ["masturbate"]: # and p_prot.b_action == "rest": No because Txell finger you.

            call p_Help

            $ p_prot.action = "rest"

        "<Pedirle una cubana>" if p_prot.pos == "oral" and p_prot.action == "rest": # and p_prot.b_action == "rest":

            call p_Help

            $ p_prot.action = "titwank_received_TRY"

            if p_active == "p_didac":
                $ p_prot_NotJustMasturbate_with_p_didac = True
            elif p_active == "p_txell":
                $ p_prot_NotJustMasturbate_with_p_txell = True
            elif p_active == "p_neus":
                $ p_prot_NotJustMasturbate_with_p_neus = True

        "<Besarla>" if (p_prot.pos == "missionary") and (p_didac.action != "cunnilingus_done_p_txell") and (p_prot.action not in ["cunnilingus_done", "anilingus_done"]):

            call p_Help

            $ p_prot.b_action = "kiss_TRY"

            if p_active == "p_didac":
                $ p_prot_NotJustMasturbate_with_p_didac = True
            elif p_active == "p_txell":
                $ p_prot_NotJustMasturbate_with_p_txell = True
            elif p_active == "p_neus":
                $ p_prot_NotJustMasturbate_with_p_neus = True

        "<Met??rsela en la garganta>" if p_active != "p_txell" and p_prot.b_action == "blowjob_received":
            ##69 Pose?

            # $ p_prot_NotJustMasturbate_with_p_didac = True # NOT NECESSARY You already did it.

            if p_prot.b_action == "blowjob_received":
                $ p_prot.b_action = "blowjobDeep_received_TRY"

        "<Met??rsela en la garganta>" if p_active != "p_txell" and p_prot.pos == "oral" and p_prot.action == "blowjob_received":

            $ p_prot.action = "blowjobDeep_received_TRY"


        "<Met??rsela m??s adentro>" if p_prot.action in ["vaginal_done", "anal_done"] and p_active != "p_txell":

            call p_Help

            # $ p_prot_NotJustMasturbate_with_p_didac = True # NOT NECESSARY

            if p_prot.action == "vaginal_done":
                $ p_prot.action = "vaginalDeep_done_TRY"

            ##

            if p_prot.action == "anal_done":
                $ p_prot.action = "analDeep_done_TRY"


        "<No met??rsela tan a dentro>" if p_prot.action in ["vaginalDeep_done", "analDeep_done", "blowjobDeep_received"] and p_active != "p_txell":

            call p_Help

            if p_prot.action == "vaginalDeep_done":
                $ p_prot.b_action = "vaginal_done"
                #$ p_didac.vaginal_done += 1

                if p_active == "p_didac":
                    $ p_didac.b_action = "vaginal_received"
                    #$ p_didac.vaginal_received += 1

                elif p_active == "p_txell":
                    $ p_txell.b_action = "vaginal_received"
                    #$ p_txell.vaginal_received += 1

                elif p_active == "p_neus":
                    $ p_neus.b_action = "vaginal_received"
                    #$ p_neus.vaginal_received += 1

            ##

            if p_prot.action == "analDeep_done":
                $ p_prot.action = "anal_done"
                #$ p_didac.anal_done += 1

                if p_active == "p_didac":
                    $ p_didac.b_action = "anal_received"
                    #$ p_didac.anal_received += 1

                elif p_active == "p_txell":
                    $ p_txell.b_action = "anal_received"
                    #$ p_txell.anal_received += 1

                elif p_active == "p_neus":
                    $ p_neus.b_action = "anal_received"
                    #$ p_neus.anal_received += 1

            ##

            if p_prot.action == "blowjobDeep_received":
                $ p_prot.action = "blowjob_received"
                #$ p_didac.blowjob_done += 1

                if p_active == "p_didac":
                    $ p_didac.b_action = "blowjob_done"
                    #$ p_didac.blowjob_done += 1

                elif p_active == "p_txell":
                    $ p_txell.b_action = "blowjob_done"
                    #$ p_txell.blowjob_done += 1

                elif p_active == "p_neus":
                    $ p_neus.b_action = "blowjob_done"
                    #$ p_neus.blowjob_done += 1

        "<Sacarla>" if p_prot.pos != "69" and p_prot.action in ["vaginalDeep_done", "analDeep_done", "vaginal_done", "anal_done", "cunnilingus_done", "anilingus_done", "titwank_received"]:

            call p_Help

            if p_prot.action in ["cunnilingus_done", "anilingus_done"]:
                $ p_prot.action = "takeTongueOut"
                $ p_prot.b_action = "rest"
            else:
                $ p_prot.action = "takeDickOut"
                $ p_prot.b_action = "rest"

            if p_prot.pos not in ["69", "oral"]:
                if p_active == "p_didac":
                    $ p_didac.action = "rest"
                elif p_active == "p_txell":
                    $ p_txell.action = "rest"
                elif p_active == "p_neus":
                    $ p_neus.action = "rest"

        "<Sacarla de su boca>" if (p_prot.pos == "69" and p_prot.b_action in ["blowjob_received", "blowjobDeep_received"]) or (p_prot.pos == "oral" and p_prot.action in ["blowjob_received", "blowjobDeep_received"]):

            if p_prot.pos == "69":
                $ p_prot.b_action = "takeDickOut"
            if p_prot.pos == "oral":
                $ p_prot.action = "takeDickOut"


        "<Detener el cunnilingus>" if p_prot.pos == "69" and p_prot.action == "cunnilingus_done":

            $ p_prot.action = "takeTongueOut"


        "<Met??rsela en la boca>" if p_prot.pos == "oral" and p_prot.action not in ["blowjob_received", "blowjobDeep_received"]:

            call p_Help

            if p_active == "p_didac":
                $ p_prot_NotJustMasturbate_with_p_didac = True
            elif p_active == "p_txell":
                $ p_prot_NotJustMasturbate_with_p_txell = True
            elif p_active == "p_neus":
                $ p_prot_NotJustMasturbate_with_p_neus = True

            if p_active == "p_txell" and p_txell_blowjobDeep_done_ACCEPTED:

                if p_prot.pos == "oral":
                    $ p_prot.action = "blowjobDeep_received"
                    $ p_txell.action = "blowjobDeep_done"

                elif p_prot == "69":
                    $ p_prot.b_action = "blowjobDeep_received"
                    $ p_txell.action = "blowjobDeep_done"

                else:
                    pass
                    
            else:

                if p_prot.pos == "oral":
                    $ p_prot.action = "blowjob_received_TRY"

                elif p_prot == "69":
                    $ p_prot.b_action = "blowjob_received_TRY"
                else:
                    pass

        "<Intentar met??rsela en la boca>" if p_prot.pos == "69" and p_prot.b_action not in ["blowjob_received", "blowjobDeep_received"]:

            #call afternight05_Pedrera_Sex_actionNull

            call p_Help

            if p_active == "p_didac":
                $ p_prot_NotJustMasturbate_with_p_didac = True
            elif p_active == "p_txell":
                $ p_prot_NotJustMasturbate_with_p_txell = True
            elif p_active == "p_neus":
                $ p_prot_NotJustMasturbate_with_p_neus = True

            $ p_prot.b_action = "blowjob_received_TRY" # Not sure if it's the best expression, but...


        "<Sexo vaginal>" if (p_prot.pos in ["missionary", "doggy"]) and (p_prot.action not in ["vaginal_done", "vaginalDeep_done"]):

            if p_active == "p_neus" and p_prot.pos == "69":
                pass
            else:
                call afternight05_Pedrera_Sex_actionNull

            call p_Help

            if p_active == "p_didac":
                $ p_prot_NotJustMasturbate_with_p_didac = True
            elif p_active == "p_txell":
                $ p_prot_NotJustMasturbate_with_p_txell = True
            elif p_active == "p_neus":
                $ p_prot_NotJustMasturbate_with_p_neus = True

            $ p_prot.action = "vaginal_done_TRY"

        "<Sexo Anal>" if (p_prot.pos in ["missionary", "doggy"]) and p_prot.action not in ["anal_done", "analDeep_done"]:

            if p_active == "p_neus" and p_prot.pos == "69":
                pass
            else:
                call afternight05_Pedrera_Sex_actionNull

            call p_Help

            if p_active == "p_didac":
                $ p_prot_NotJustMasturbate_with_p_didac = True
            elif p_active == "p_txell":
                $ p_prot_NotJustMasturbate_with_p_txell = True
            elif p_active == "p_neus":
                $ p_prot_NotJustMasturbate_with_p_neus = True

            $ p_prot.action = "anal_done_TRY"
        "<Hacerle un cunnilingus>" if p_prot.pos in ["missionary", "69"] and p_prot.action != "cunnilingus_done":

            if p_active == "p_neus" and p_prot.pos == "69":
                pass
            else:
                call afternight05_Pedrera_Sex_actionNull

            call p_Help

            $ p_prot.action = "cunnilingus_done"

            if p_active == "p_didac":
                $ p_didac.b_action = "cunnilingus_received"

            elif p_active == "p_txell":
                $ p_txell.b_action = "cunnilingus_received"

            elif p_active == "p_neus":
                $ p_neus.b_action = "cunnilingus_received"

        "<Hacerle un anilingus>" if p_prot.pos == "doggy" and p_prot.action != "anilingus_done":

            if p_active == "p_neus" and p_prot.pos == "69":
                pass
            else:
                call afternight05_Pedrera_Sex_actionNull

            call p_Help

            $ p_prot.action = "anilingus_done"

            if p_active == "p_didac":
                $ p_didac.action = "anilingus_received"

            elif p_active == "p_txell":
                $ p_txell.action = "anilingus_received"

            elif p_active == "p_neus":
                $ p_neus.action = "anilingus_received"

        "<Azotarle las nalgas>" if p_prot.pos == "doggy" and p_prot.action not in ["cunnilingus_done", "anilingus_done"]:

            call p_Help

            if p_active == "p_didac":
                $ p_didac.buttocks_pain += 3
                if p_didac.buttocks_pain < 6:
                    $ p_didac.pleasure += 2
                else:
                    $ p_didac.pleasure -= 2

            if p_active == "p_txell":
                $ p_txell.buttocks_pain += 3
                if p_txell.buttocks_pain < 6:
                    $ p_txell.pleasure += 2
                else:
                    $ p_txell.pleasure -= 2

            if p_active == "p_neus":
                $ p_neus.buttocks_pain += 3
                if p_neus.buttocks_pain < 6:
                    $ p_neus.pleasure += 2
                else:
                    $ p_neus.pleasure -= 2

            $ p_prot.b_action = "buttocks_slap"

        "<Elegir otra postura>":

            call p_Help

            call afternight05_Pedrera_Sex_changeposNull

            if p_prot.restTurns > 2:
                $ p_prot.restTurns -= 1 # RESTART the repetition of doing nothing.

            jump afternight05_Pedrera_Sex

    call expression "afternight05_Pedrera_Sex_" + p_active + "_" + p_prot.pos

    call afternight05_Pedrera_Sex_After

    jump afternight05_Pedrera_Sex_action


######################################################################
######################################################################

######################################################################
######################################################################

label afternight05_Pedrera_Sex_NakeYou:

    # Removing Clothes.

    if p_didac.start == 1 or p_txell.start == 1 or p_neus.start == 1:

        if p_didac.start > 1 or p_txell.start > 1:
            pass
        else:

            if p_prot.pos == "oral":
                if p_active == "p_didac":
                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx03
                    show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                    with fade_short

                elif p_active == "p_txell":
                    show gensex_oral_m_frontHead_exp_eyes 02
                    show gensex_oral_m_frontHead_exp_iris front02
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                    show gensex_oral_m_frontHead_exp_eyebrows serious
                    with fade_short

            elif p_prot.pos == "missionary":
                if p_active == "p_didac":
                    show gensex_missionary_d_head_exp_blush 02
                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils front01
                    show gensex_missionary_d_head_exp_eyebrows surprisex01
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                    with fade_short


            n "H??bilmente te quitas la camisa,"

            if p_prot.pos == "oral":
                if p_active == "p_didac":
                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris down02
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx04
                    show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                    with dissolve

                elif p_active == "p_txell":
                    show gensex_oral_m_frontHead_exp_eyes 03
                    show gensex_oral_m_frontHead_exp_iris down03
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                    with dissolve

            elif p_prot.pos == "missionary":

                $ ped_sex_general_zoom_Cond = "face"
                call pedrera_sex_p_general_talk

                if p_active == "p_didac":
                    show gensex_missionary_d_head_exp_blush 03
                    show gensex_missionary_d_head_exp_eyes 03
                    show gensex_missionary_d_head_exp_pupils front03
                    show gensex_missionary_d_head_exp_eyebrows sadx01
                    show gensex_missionary_d_head_exp_mouth happybiting_Silentx02

            with Dissolve(0.5)

            n "para luego bajarte los pantalones junto con los b??xeres."

    if p_prot.pos == "oral":

        if p_active == "p_didac":

            show gensex_oral_d_frontHead_exp_eyes 02
            show gensex_oral_d_frontHead_exp_iris down02
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx03
            show gensex_oral_d_frontHead_exp_eyebrows suspiciousx01

        elif p_active == "p_txell":
            show gensex_oral_m_frontHead_exp_eyes 04
            show gensex_oral_m_frontHead_exp_iris down04
            show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
            show gensex_oral_m_frontHead_exp_eyebrows normal
            with dissolve

        elif p_active == "p_neus":
            $ nteye = "front06"
            show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx05
            show gensex_oral_n_frontHead_exp_eyebrows sadx03
            call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

        if p_didac.start == 1 or p_txell.start == 1 or p_neus.start == 1:
            with dissolve
        else:
            with fade

        n "Le indicas que se ponga de rodillas ante ti."

    elif p_prot.pos == "missionary":

        if p_active == "p_didac":

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 02
                show gensex_missionary_d_head_exp_pupils front02
                show gensex_missionary_d_head_exp_eyebrows normal
                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10

        elif p_active == "p_neus":
            $ nteye = "front05"
            show gensex_missionary_n_head_exp_mouth happybiting_Silentx05
            show gensex_missionary_n_head_exp_eyebrows sadx03
            call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve


        if p_didac.start == 1 or p_txell.start == 1 or p_neus.start == 1:
            with dissolve
        else:
            with fade

        n "Le indicas que se acomode en la cama."

    elif p_prot.pos == "doggy":

        $ ped_sex_general_zoom_Cond = ""
        call pedrera_sex_p_general_talk

        if p_didac.start == 1 or p_txell.start == 1 or p_neus.start == 1:
            with dissolve
        else:
            with fade

        n "Le indicas que se ponga a cuatro patas sobre la cama."

    elif p_prot.pos == "69":

        # show gensex_69_L_d_mouth sad_Silentx02
        # with dissolve

        n "Le indicas que se acomode en la cama mientras te pones encima de ella,"

        # show gensex_69_L_d_mouth sad_Silentx04
        # with dissolve

        n "acercando tu rostro a su entrepierna y tu polla a sus labios."

    ##

    #if p_prot.pos not in ["69", "doggy"]:

    if p_active == "p_didac":

        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
            show gensex_missionary_d_head_exp_eyes 04
            show gensex_missionary_d_head_exp_pupils down04
            show gensex_missionary_d_head_exp_eyebrows suspiciousx02
            show gensex_missionary_d_head_exp_mouth happy_Talkingx02

        elif p_prot.pos == "oral":
            show gensex_oral_d_frontHead_exp_eyes 05
            show gensex_oral_d_frontHead_exp_iris front05
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx04
            show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02

        elif p_prot.pos == "69":
            show gensex_69_L_d_mouth sad_Talkingx002

        elif p_prot.pos == "doggy":

            $ ped_sex_general_zoom_Cond = "crotch"
            #$ ped_sex_general_action_Cond = "v00_00"
            call pedrera_sex_p_general_talk

        with dissolve

        d "Al menos me alegra ver que sigue estando bien dura."

    elif p_active == "p_txell":

        if p_prot.pos == "oral":

            show gensex_oral_m_frontHead_exp_eyes 05
            show gensex_oral_m_frontHead_exp_iris down05
            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
            show gensex_oral_m_frontHead_exp_eyebrows surprisex001
            with dissolve

        elif p_prot.pos == "69":

            $ ped_sex_general_69_cover = "over"
            $ ped_sex_general_expression_Cond = "talk"
            $ ped_sex_general_action_Cond = "69_00_00"
            $ ped_sex_general_action_b_Cond = "69b_00_00"
            call pedrera_sex_p_general_talk

            show gensex_69_L_d_mouth happy_Talkingx01
            with Dissolve(0.2)

        tx "Veo que al menos tu polla no necesita preliminares para ponerse dura..."

    elif p_active == "p_neus":

        if p_prot.pos in ["oral", "69"]:
            
            if p_neus_orgasmHurry:

                if p_prot.pos == "oral":
                    $ nteye = "front08"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_n_frontHead_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

                ne "S??..."

                if p_prot.pos == "oral":
                    $ nteye = "front05"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_n_frontHead_exp_eyebrows sadx03
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

                ne "Es mejor que use mi lengua,"

                if p_prot.pos == "oral":
                    $ nteye = "front08"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx03
                    show gensex_oral_n_frontHead_exp_eyebrows sadx06
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

                ne "as?? no correr?? peligro de correrme antes."

                if p_prot.pos == "oral":
                    $ nteye = "down05"
                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx07
                    show gensex_oral_n_frontHead_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

            else:

                if p_prot.pos == "oral":
                    $ nteye = "front03"
                    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx05
                    show gensex_oral_n_frontHead_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

                ne "??Prefieres que empiece con mi lengua?"

                if p_prot.pos == "oral":
                    $ nteye = "down04"
                    show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx08
                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

        elif p_prot.pos in ["doggy"]:

            $ ped_sex_general_zoom_Cond = "face"
            call pedrera_sex_p_general_talk
            with fade_short

            ne "??A cuatro patas...?" # naughty tone

            if p_neus_orgasmHurry:

                ne "[protname]..."

                ne "Aunque me encantar??a que me follaras como a una perrita en celo..."

                ne "ahora no es el mejor momento,"

                ne "me temo que no aguantar?? mucho m??s..."

        else:
            
            if p_neus_orgasmHurry:

                if p_prot.pos == "missionary":
                    $ nteye = "front08"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                    show gensex_missionary_n_head_exp_eyebrows sadx03
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

                ne "Aunque he estado noches enteras sin dormir so??ando este momento..."

                if gensex_ILoveYouNeus:

                    if p_prot.pos == "missionary":
                        $ nteye = "front04"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx003
                        show gensex_missionary_n_head_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                        with dissolve

                    ne "Si me haces el amor en esta postura,"

                else:

                    if p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx006
                        show gensex_missionary_n_head_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                        with dissolve

                    ne "Si me follas en esta postura,"

                if p_prot.pos == "missionary":
                    $ nteye = "front03"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx07
                    show gensex_missionary_n_head_exp_eyebrows sadx06
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

                ne "no s?? si ser?? capaz de resistir el orgasmo."

                if p_prot.pos == "missionary":
                    $ nteye = "front05"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                    show gensex_missionary_n_head_exp_eyebrows sadx07
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

                ne "Por favor [protname]..."

                if p_prot.pos == "missionary":
                    $ nteye = "front08"
                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx07
                    show gensex_missionary_n_head_exp_eyebrows sadx08
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

            else:

                if p_prot.pos == "missionary":
                    $ nteye = "front08"
                    show gensex_missionary_n_head_exp_mouth happy_Silentx05
                    show gensex_missionary_n_head_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

                ne "..."

                if p_prot.pos == "missionary":
                    $ ped_sex_general_zoom_Cond = "face"
                    call pedrera_sex_p_general_talk

                    $ nteye = "front05"
                    show gensex_missionary_n_head_exp_mouth happy_Talkingx06
                    show gensex_missionary_n_head_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with Dissolve(0.5)

                ne "Por fin..."

    if p_active == "p_didac":
        $ p_didac.start = 2
    elif p_active == "p_txell":
        $ p_txell.start = 2
    elif p_active == "p_neus":
        $ p_neus.start = 2

    return

######################################################################
######################################################################

label afternight05_Pedrera_Sex_checkingOrgasm:

    call afternight05_Pedrera_Sex_Check_after_restNumbers

    $ p_prot.p_closeToOrgasm()
    $ p_neus.p_closeToOrgasm()
    $ p_didac.p_closeToOrgasm()
    $ p_txell.p_closeToOrgasm()
    return

label ped_reduceRestTurns:

    if p_prot.restTurns > 4:
        $ p_prot.restTurns -= 2

    $ p_prot_restTemp = 0

    return

label afternight05_Pedrera_Sex_Check_after_restNumbers:

    #progcheck "Waiting01: p_prot.restTurns = [p_prot.restTurns]"

    if afternight05_Pedrera_n_Neus_Warning_Cond == True:
        # Already done.
        $ afternight05_Pedrera_n_Neus_Warning_Cond = False
    else:
        if p_prot.action not in ["masturbate", "titwank_received", "vaginal_done", "vaginalDeep_done", "anal_done", "analDeep_done", "blowjob_received", "blowjobDeep_received"] and p_prot.b_action not in ["blowjob_received", "blowjobDeep_received"]:
            #progcheck "You're not receiving pleasure."
            if p_prot.action in ["cunnilingus_done", "anilingus_done"]:
                pass
                #progcheck "You're giving pleasure."

            $ p_prot.restTurns += 1
            $ p_prot_restTemp += 1

            if p_prot.pos == "oral":
                $ p_prot.pos_oral_rest += 1

            elif p_prot.pos == "69":

                $ p_prot.pos_69_rest += 1

            elif p_prot.pos == "doggy":

                $ p_prot.pos_doggy_rest += 1

            elif p_prot.pos == "missionary":

                $ p_prot.pos_missionary_rest += 1

        else:

            #progcheck "You're receiving pleasure. p_prot.restTurns = [p_prot.restTurns]"

            if p_prot.restTurns > 1:
                $ p_prot.restTurns -= 2
            $ p_prot_restTemp = 0

            #progcheck "You're receiving pleasure. p_prot.restTurns = [p_prot.restTurns]"

    #progcheck "Waiting02: p_prot.restTurns = [p_prot.restTurns]"



    return

label afternight05_Pedrera_Neus_Warning:

    ###

    $ randomnum_1to5 = renpy.random.randint(1, 5)

    ###

    $ debug ("Neus_Warning.")

    if p_prot.b_action == "blowjob_received":

        pass

    elif p_prot.action in ["cunnilingus_done", "anilingus_done"]:

        $ afternight05_Pedrera_Neus_Warning_tongue += 1

        if afternight05_Pedrera_Neus_Warning_tongue > 1:
            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

        if afternight05_Pedrera_Neus_Warning_tongue == 1:

            pass

        elif afternight05_Pedrera_Neus_Warning_tongue in [2, 3]:

            $ ped_check_1_10("ped_neus_warning_01_list")

            # if ped_check_list_result in range(1,11):

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_iris front02
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx02
            with fade_short

            if ped_check_list_result == 1:
                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show neus_exp_mouth sad_Talkingx05
                    show gensex_oral_n_frontHead_exp_eyebrows sadx02
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                    show gensex_missionary_n_head_exp_eyebrows sadx02
                    call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

                ne "No me parece mal que prepares el camino,"

                extend " pero..."

            elif ped_check_list_result == 2:

                ne "Deber??as hacer algo m??s que usar tu lengua."

            elif ped_check_list_result == 3:

                ne "No la tienes d??nde deber??a estar..."

            elif ped_check_list_result == 4:

                if ((p_active == "p_didac" and (p_didac.anal_received == 0 and p_didac.vaginal_received == 0)) or
                    (p_active == "p_txell" and (p_txell.anal_received == 0 and p_txell.vaginal_received == 0))):

                    ne "Deber??as empezar a ponerla en su interior."

                else:

                    ne "Deber??as volver a pon??rsela en su interior."

            elif ped_check_list_result == 5:

                ne "Entiendo que tengas un tama??o enorme y debas..."

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_iris front03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "Pero quiz??s deber??as usar tu mano si no le cabe..."

            elif ped_check_list_result == 6:

                ne "Esta bien que quieras ser servicial y dar placer..."

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "Pero si no terminas pronto..."

            elif ped_check_list_result == 7:

                ne "No digo que hacer eso est?? mal..."

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "Pero si te va a tomar mucho tiempo,"

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_iris front02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "quiz??s te masturbaras,"

                show neus_exp_mouth sad_Talkingx002
                show neus_exp_iris right05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "o..."

            elif ped_check_list_result == 8:

                ne "No dudo que seas bueno con la lengua,"

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "pero eso no te ayudar?? a terminar antes..."

            elif ped_check_list_result == 9:

                ne "Es amable por tu parte que te preocupes por su placer,"

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "pero..."

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_iris front03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "Recuerda que t?? eres la prioridad."

            elif ped_check_list_result == 10:

                ne "Si solo usas tu lengua..."


            ##

            show neus_exp_mouth sad_Talkingx07
            show neus_exp_iris front01
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx04
            with dissolve

            $ ped_check_1_10("ped_neus_warning_02_list")

            if ped_check_list_result == 1:

                ne "Se nos har?? de d??a..."

            elif ped_check_list_result == 2:

                ne "El tiempo va pasando..."

            elif ped_check_list_result == 3:

                ne "No tenemos toda la noche..."

            elif ped_check_list_result == 4:

                ne "Como te corras fuera,"

                extend" no habr?? suficiente esperma para las tres..."

                show neus_exp_mouth sadbiting_Silentx06
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                p "Tranquila,"

                extend " lo controlo..."

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_iris front08
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "..."

            elif ped_check_list_result == 5:

                ne "Se est?? haciendo tarde..."

            elif ped_check_list_result == 6:

                ne "Te lo est??s tomando a broma..."

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "y yo te estoy hablando muy en serio, [protname]..."

            elif ped_check_list_result == 7:

                ne "Creo que no entiendes el peligro..."

            elif ped_check_list_result == 8:

                ne "No conoces a Padre lo suficiente como para temerlo..."

            elif ped_check_list_result == 9:

                if p_active == "p_txell" and p_didac.seal != "sealed":

                    ne "A??n falta D??dac..."

                elif p_active == "p_didac" and p_txell.seal != "sealed":

                    ne "A??n falta Txell..."

                else:

                    ne "A??n faltar?? yo..."

            elif ped_check_list_result == 10:

                ne "No tenemos toda la noche."

            else:

                ne "[protname]..."

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_iris front05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx03
            with Dissolve(0.5)

        else:

        #if afternight05_Pedrera_Neus_Warning_tongue == 4:

            call afternight05_Pedrera_Neus_Warning_4Times


######

    elif p_prot.restTurns > 1:

        window hide dissolve
        pause 0.2

        $ Pedrera_char_Cond = "NeusClose_show"
        call Pedrera_char_lab

        if p_prot.restTurns == 2:

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_iris front04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx05
            with fade

            ne "Tiene raz??n."

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_iris front02
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx03
            with dissolve

            $ ped_check_1_10("ped_neus_warning_03_list")

            if ped_check_list_result == 1:

                ne "Sino haces algo,"

                extend " se nos har?? de d??a."

            elif ped_check_list_result == 2:

                ne "No podemos estar as?? toda la noche."

            elif ped_check_list_result == 3:

                ne "Haz algo."

                show neus_exp_mouth sad_Talkingx07
                show neus_exp_iris front03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "Pero algo que te lleve a ti tambi??n al orgasmo."

            elif ped_check_list_result == 4:

                ne "No tenemos toda la noche."

                show neus_exp_mouth sad_Talkingx07
                show neus_exp_iris front03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "[protname],"

                extend " si no haces algo,"

                show neus_exp_mouth sad_Talkingx06
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx05
                with dissolve

                ne "lo tendr?? que hacer yo."

            elif ped_check_list_result == 5:

                ne "No lo dec??a en broma,"

                extend " [protname]"

                show neus_exp_mouth sad_Talkingx06
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx05
                with dissolve

                ne "No tenemos toda la noche."

            elif ped_check_list_result == 6:

                ne "Si amanece,"

                extend " ser?? demasiado tarde..."

            elif ped_check_list_result == 7:

                ne "No podemos perder el tiempo as??..."

            elif ped_check_list_result == 8:

                ne "Enti??ndelo..."

            elif ped_check_list_result == 9:

                ne "No me obligues..."

            elif ped_check_list_result == 10:

                ne "No quiero tener que obligarte..."

            else:

                ne "[protname]..."

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_iris front05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx04
            with dissolve

        elif p_prot.restTurns == 3:

            $ ped_check_1_10("ped_neus_warning_04_list")

            if ped_check_list_result == 1:

                show neus_exp_mouth sad_Talkingx08
                show neus_exp_iris front03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03
                with fade_short

                ne "Si sigues as??,"

                extend " voy a tener que intervenir."

            elif ped_check_list_result == 2:

                show neus_exp_mouth sad_Talkingx06
                show neus_exp_iris front03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx02
                with dissolve

                ne "[protname],"

                extend " por favor..."

                show neus_exp_mouth sad_Talkingx08
                show neus_exp_iris front02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "haz algo,"

                if p_neus.throat_pain > 0:

                    extend " aunque me duela la garganta..."

                else:

                    extend " o tendr?? que hacerlo por ti."

            elif ped_check_list_result == 3:

                show neus_exp_mouth sad_Talkingx08
                show neus_exp_iris front02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx04

                if p_active == "p_didac":

                    ne "D??dac tiene raz??n."

                elif p_active == "p_txell":

                    ne "Txell tiene raz??n."

                show neus_exp_mouth sad_Talkingx09
                show neus_exp_iris front03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx04
                with dissolve

                ne "Si no haces nada,"

                extend " al final tendr?? que intervenir."

                show neus_exp_mouth sad_Talkingx10
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03
                with dissolve

                ne "No tenemos toda la noche."

            elif ped_check_list_result == 4:

                show neus_exp_mouth sad_Talkingx09
                show neus_exp_iris front02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03
                with fade_short

                ne "Ahora en serio [protname]."

                show neus_exp_mouth sad_Talkingx08
                show neus_exp_iris front03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx04
                with dissolve

                ne "Si sigues sin hacer nada con ??l,"

                show neus_exp_mouth sad_Talkingx10
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx04
                with dissolve

                ne "voy a tener que tomar medidas dr??sticas."

            elif ped_check_list_result == 5:

                show neus_exp_mouth sad_Talkingx07
                show neus_exp_iris front08
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03
                with fade_short

                ne "Al final har?? algo que no te va a gustar."

            elif ped_check_list_result == 6:

                show neus_exp_mouth sad_Talkingx07
                show neus_exp_iris front08
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03
                with fade_short

                ne "??Te lo est??s tomando a broma,"

                show neus_exp_mouth sad_Talkingx06
                show neus_exp_iris front03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx04
                with dissolve

                ne "y yo te estoy hablando muy en serio, [protname]."

            elif ped_check_list_result == 7:

                show neus_exp_mouth sad_Talkingx07
                show neus_exp_iris front08
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03
                with fade_short

                ne "??[protname]!"

                show neus_exp_mouth sad_Talkingx004
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx04
                with dissolve

                ne "No me hagas repetirlo..."

            elif ped_check_list_result == 8:

                show neus_exp_mouth sad_Talkingx07
                show neus_exp_iris front08
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03
                with fade_short

                ne "????Acaso no lo entiendes?!"

                show neus_exp_mouth sad_Talkingx08
                show neus_exp_iris front03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "Esto no es una broma, [protname]."

            elif ped_check_list_result == 9:

                show neus_exp_mouth sad_Talkingx07
                show neus_exp_iris front02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03
                with fade_short

                ne "??[protname]!"

                show neus_exp_mouth sad_Talkingx06
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx04
                with dissolve

                ne "Se me est?? acabando la paciencia..."

            elif ped_check_list_result == 10:

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with fade_short

                ne "Por favor,"

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_iris front05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "ya sabes que no tenemos toda la noche..."

            else:

                show neus_exp_mouth sad_Talkingx06
                show neus_exp_iris front08
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx04
                with fade_short

                ne "??[prontname]!"

            show neus_exp_mouth sad_Silentx06
            show neus_exp_iris front05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx02
            with dissolve

        elif p_prot.restTurns >= 4:

            call afternight05_Pedrera_Neus_Warning_4Times


    $ Pedrera_char_Cond = "p_nobody"
    # if p_prot.restTurns > 2: # fade should work fine with after two. \\ It doesn't work if there are facless expressions later.
    #     $ debug("Warning_Neus fade")
    #     with fade

    call Pedrera_char_lab
    return

label afternight05_Pedrera_Neus_Warning_4Times:

    $ Pedrera_char_Cond = "NeusClose_show"
    call Pedrera_char_lab

    if p_prot.restTurns == 4 or afternight05_Pedrera_Neus_Warning_tongue == 4:

        show neus_exp_mouth sad_Talkingx07
        show neus_exp_iris front02
        $ nteye = 2
        call neus_exp_tears_tears
        show neus_exp_eyebrows angryx03
        with dissolve

        $ ped_check_1_10("ped_neus_warning_05_list")

        if ped_check_list_result == 1: 

            ne "Es mi ??ltimo aviso."

        elif ped_check_list_result == 2:

            ne "No te lo volver?? a repetir, [protname]."

        elif ped_check_list_result == 3:

            ne "[protname]."

            show neus_exp_mouth sad_Talkingx10
            show neus_exp_iris front03
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx04
            with dissolve

            ne "Basta ya."

            show neus_exp_mouth sad_Talkingx11
            show neus_exp_iris front04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx04
            with dissolve

            ne "O tendr?? que tomar medidas dr??sticas."

        elif ped_check_list_result == 4:

            ne "[protname],"

            extend " no te lo volver?? a repetir."

        elif ped_check_list_result == 5:

            ne "Esta es mi ??ltima advertencia."

        elif ped_check_list_result == 6:

            ne "Es mi ??ltima advertencia."

        elif ped_check_list_result == 7:

            ne "Se acab??."

            show neus_exp_mouth sad_Talkingx08
            show neus_exp_iris front04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx04
            with dissolve

            ne "No volver?? a repet??rtelo."

        elif ped_check_list_result == 8:

            ne "Este es mi ultimatum, [protname]."

        elif ped_check_list_result == 9:

            ne "La pr??xima vez tomar?? cartas en el asunto yo misma."

        elif ped_check_list_result == 10:

            ne "Ya no te lo volver?? a repetir."

        else:

            ne "No te lo volver?? a repetir."

        show neus_exp_mouth sad_Silentx06
        show neus_exp_iris front05
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_eyebrows angryx04
        with dissolve

        if p_active == "p_txell" and p_prot.action == "cunnilingus_done":

            if afternight05_Pedrera_Neus_Warning_4Times_cunnilingusTxell == False:

                pause 0.2

                $ Pedrera_char_Cond = "p_nobody"
                call Pedrera_char_lab

                show gensex_69_L_d_mouth happy_Talkingx03
                with fade_short

                tx "No seas as?? Neus..."

                show gensex_69_L_d_mouth happy_Talkingx04
                with dissolve

                tx "El chico lo est?? intentando,"

                show gensex_69_L_d_mouth happy_Talkingx03
                with dissolve

                tx "dale un poco m??s de tiempo."

                show gensex_69_L_d_mouth happy_Silentx02
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "NeusClose_show"
                call Pedrera_char_lab

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_iris front05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx02
                with fade_short

                ne "..."

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_iris front08
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "Siempre y cuando no tard??is demasiado."

                show neus_exp_mouth sad_Silentx04
                show neus_exp_iris right05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx04
                with dissolve

                $ afternight05_Pedrera_Neus_Warning_4Times_cunnilingusTxell = True
                $ afternight05_Pedrera_Neus_Warning_tongue = -1
                $ p_prot.restTurns = -1

                pause 0.2

            else:

                show neus_exp_mouth sad_Talkingx06
                show neus_exp_iris front03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03
                with dissolve

                ne "Y no me sirve la excusa de antes,"

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03
                with dissolve

                ne "ya os he dado suficiente tiempo."

                show neus_exp_mouth sad_Silentx05
                show neus_exp_iris front05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx04
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "p_nobody"
                call Pedrera_char_lab

                if (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) > p_didac_cunnilingus_p_txell_orgasm and p_txell.orgasm > 0 and p_prot.action == "cunnilingus_done":

                    $ randomnum_1to5 = renpy.random.randint(1, 5)

                    show gensex_69_L_d_mouth happy_Talkingx03
                    with fade_short

                    if randomnum_1to5 == 1: 

                        tx "En realidad,"

                        show gensex_69_L_d_mouth happy_Talkingx05
                        with dissolve

                        tx "sorprendentemente,"

                        if (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) == 1:

                            extend " ya ha conseguido que tenga un orgasmo."

                        else:

                            extend " ya ha conseguido que tenga [p_txell_orgasmByYou] orgasmos."

                        show gensex_69_L_d_mouth happy_Talkingx04
                        with dissolve

                        tx "Si no me lo pide,"

                        show gensex_69_L_d_mouth happy_Talkingx06
                        with dissolve

                        tx "es porque no quiere..."

                    elif randomnum_1to5 == 2:

                        tx "Parece que quiera darme otro orgasmo..."

                        if p_txell_orgasmByYou > 1:

                            show gensex_69_L_d_mouth happy_Talkingx06
                            with dissolve

                            tx "Y eso que ya lleva [p_txell_orgasmByYou]..."

                    elif randomnum_1to5 == 3:

                        tx "No ser?? porque a mi no se me da bien..."

                    elif randomnum_1to5 == 4:

                        tx "Yo no me quejo..."

                    elif randomnum_1to5 == 5:

                        if p_txell_orgasmByYou == 1:

                            tx "Y eso que ya me ha dado un orgasmo..."

                        else:

                            extend " Y eso que ya me ha dado [p_txell_orgasmByYou] orgasmos..."

                    show gensex_69_L_d_mouth happybiting_Silentx04
                    with dissolve

                else:

                    $ randomnum_1to5 = renpy.random.randint(1, 5)

                    show gensex_69_L_d_mouth happy_Talkingx05
                    with fade_short

                    if randomnum_1to5 == 1: 

                        tx "Lo siento chico, eres demasiado lento."

                        show gensex_69_L_d_mouth sad_Talkingx003
                        with dissolve

                        tx "Tampoco me esperaba otra cosa..."

                    elif randomnum_1to5 == 2:

                        tx "Lo has intentado."

                    elif randomnum_1to5 == 3:

                        tx "Lo siento,"

                        show gensex_69_L_d_mouth sad_Talkingx003
                        with dissolve

                        tx "pero parece que soy demasiada mujer para ti."

                    elif randomnum_1to5 == 4:

                        tx "No parece que haya habido suerte."

                    elif randomnum_1to5 == 5:

                        tx "Parece que a??n te falta algo de pr??ctica."

                    show gensex_69_L_d_mouth happy_Silentx03
                    with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "NeusClose_show"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Silentx04
                show neus_exp_iris right05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with fade_short

                ne "..."

    elif p_prot.restTurns >= 5 or afternight05_Pedrera_Neus_Warning_tongue >= 5:

        show neus_exp_mouth sad_Talkingx11
        show neus_exp_iris front04
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_eyebrows angryx05
        with dissolve

        #$ ped_check_1_10("ped_missionary_rest_neus_list")

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1: 

            ne "??Te he avisado!"

        elif randomnum_1to5 == 2: 

            ne "??Como quieras!"

        elif randomnum_1to5 == 3:

            ne "??No me dejas otro remedio!"

        elif randomnum_1to5 == 4:

            ne "??Pensaba que lo entender??as!"

        elif randomnum_1to5 == 5:

            ne "??Lo hago para salvarnos!"

        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_iris front05
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_eyebrows sadx02
        with dissolve

        call afternight05_Pedrera_Sex_NeusLastWarning
            # n "De pronto, sientes como si algo se removiera por dentro de tu bolsa escrotal,"
            # n "al mismo tiempo que un cosquilleo que cubre desde tus ingles hasta casi la altura de tu ombligo."
            # p "??Qu?? demonios...?"

    ##

    $ Pedrera_char_Cond = "p_nobody"
    call Pedrera_char_lab

    ##

    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
        pass
    else:
        pass

    return

######################################################################
######################################################################


label afternight05_Pedrera_Sex_NeusLastWarning:

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    $ nleye = "full"

    $ nblush = 2
    show n_closefromup_mouth sad_Silentx05
    $ nteye = "front00b"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows angryx03
    with flash_short


    $ afternight05_Pedrera_Sex_NeusLastWarning_Times += 1

    if afternight05_Pedrera_Sex_NeusLastWarning_Times == 1:

        n "El rostro de Neus se planta justo delante de ti con sus ojos viol??ceos brillantes."

        show n_closefromup_mouth sad_Silentx04
        $ nteye = "front02b"
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows angryx03
        with dissolve

        p "??Qu??...?"

        show n_closefromup_mouth sad_Silentx06
        $ nteye = "front08"
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx01
        with dissolve

        n "Sientes como cada m??sculo de tu cuerpo se petrifica, incapaz de hacer ninguna acci??n."

        show n_closefromup_mouth sad_Talkingx04
        $ nteye = "right02"
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "Txell,"

        extend " ??Podr??as ayudarme a...?"

        show n_closefromup_mouth sadbiting_Silentx03
        $ nteye = "right05"
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        pause 0.2

        $ Pedrera_char_Cond = "TxellClose_b"
        call Pedrera_char_lab

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 02
        show m_exp_piris left02
        show m_exp_eyebrows sadx01
        with fade

        tx "Por ti,"

        extend " lo que sea."

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx02
        with dissolve

        pause 0.2

        scene day05
        with fade_short

        n "Sientes la mano de la rubia acariciando tu miembro."

        p "??Qu??...?"

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_mouth sad_Talkingx03
        $ nteye = "front03"
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with fade_short

        ne "Lo siento [protname]."

        show n_closefromup_mouth sad_Talkingx04
        $ nteye = "front05"
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        ne "Pero ya te he dicho que no tenemos toda la noche."

        $ nleye = ""

        show n_closefromup_mouth sadbiting_Silentx04
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx05
        with dissolve

        pause 0.2

        scene day05
        with fade_short

        p "..."

    elif afternight05_Pedrera_Sex_NeusLastWarning_Times == 2:

        show n_closefromup_mouth sad_Silentx05
        $ nteye = "front02b"
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows angryx04
        with dissolve

        n "Por segunda vez,"

        $ ntlong += 1

        show n_closefromup_mouth sadbiting_Silentx05
        $ nteye = "front03"
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve
        
        n "el rostro de Neus se planta justo delante de ti con sus ojos brillantes."

        show n_closefromup_mouth sad_Silentx06
        $ nteye = "front05"
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        p "..."

        #$ nleye = ""

        show n_closefromup_mouth sad_Silentx04
        $ nteye = "front08"
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        n "Vuelves a sentir como tu cuerpo no responde a ninguna de las acciones que pretendes llevar a cabo."

        show n_closefromup_mouth sad_Talkingx05
        $ nteye = "right02"
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        ne "Txell..."

        show n_closefromup_mouth sad_Silentx05
        $ nteye = "right02"
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        $ Pedrera_char_Cond = "TxellClose_b"
        call Pedrera_char_lab

        show m_exp_mouth happy_Talkingx03
        show m_exp_eyes 02
        show m_exp_piris left02
        show m_exp_eyebrows sadx01
        with fade_short

        tx "Tranquila,"

        extend " ya me pongo a ello."

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx01
        with dissolve

        n "Su mano vuelve a acariciar tu erecto miembro."

        scene day05
        with fade_short

        p "Ughh..."

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_mouth sad_Talkingx05
        $ nteye = "front02"
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx01
        with fade_short

        ne "[protname]..."

        show n_closefromup_mouth sad_Talkingx04
        $ nteye = "front08"
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        ne "No me siento a gusto forz??ndote a esto,"

        show n_closefromup_mouth sad_Talkingx07
        $ nteye = "front03"
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        ne "pero de verdad,"

        extend " no tenemos toda la noche."

        show n_closefromup_mouth sadbiting_Silentx05
        $ nteye = "front04"
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx05
        with dissolve

        $ nleye = ""

    if p_active == "p_didac":

        $ Pedrera_char_Cond = "DidacClose"
        call Pedrera_char_lab

        show didacf_mouth sad_Talkingx08
        $ dteye = 2
        call didac_exp_tears_tears
        show didacf_pupils front02
        show didacf_eyebrows angryx04
        with fade_short

        d "????Y tiene que ser cuando es mi turno?!"

        show didacf_mouth sadbiting_Silentx04
        $ dteye = 0
        call didac_exp_tears_tears
        show didacf_pupils down00
        show didacf_eyebrows surprisex01
        with dissolve

        tx "Si tienes que buscar a un culpable,"

        extend " ya sabes quien es el responsable."

        show didacf_mouth sad_Talkingx09
        $ dteye = 8
        call didac_exp_tears_tears
        show didacf_pupils front08
        show didacf_eyebrows angryx04
        with dissolve

        d "??La madre que te pari?? [protname]!"

        show didacf_mouth sad_Silentx09
        $ dteye = 5
        call didac_exp_tears_tears
        show didacf_pupils front05
        show didacf_eyebrows angryx04
        with dissolve

        pause 0.2

    elif p_active == "p_txell":

        scene day05
        with fade

        if p_didac.seal == "sealed":

            d "La que representa que es tan experta..."
        
        else:

            d "Seguro que conmigo no necesitar?? esto..."

        tx "No te quejes tanto,"

        if p_didac.seal == "sealed":

            extend " que contigo ya lo ha hecho."

            d "..."

        else:

            extend " que ahora vendr?? tu turno."

            d "Hmmmm..."

    if afternight05_Pedrera_Sex_NeusLastWarning_Times == 1:

        scene day05
        with fade_short

        n "De pronto percibes su segunda mano agarr??ndotela tambi??n,"

        n "mientras las desliza a lo largo y ancho de tu erecto miembro."

        menu:

            pt "Mierda, mierda, mierda... ??Piensa en algo!"

            "<Intentar recordar a tu bisabuela cuando ejerc??a presi??n con sus u??as en los granos de pus de sus pies>":
                call p_Help

                call afternight05_Pedrera_Sex_NeusLastWarning_ResistingTxellMast

            "<No recordar esa imagen>":
                call p_Help

        pt "??Joder!"

    elif afternight05_Pedrera_Sex_NeusLastWarning_Times == 2:

        scene day05
        with fade_short

        menu:

            "<Volver al adorable recuerdo que tu entra??able bisabuela comparti?? contigo>":

                if afternight05_Pedrera_Sex_NeusLastWarning_GrandMother > 0:

                    call p_Help

                    call afternight05_Pedrera_Sex_NeusLastWarning_ResistingTxellMast


            "<Evitar a toda costa ese recuerdo>":

                    call p_Help

                    p "??Ughh!..."

                    if afternight05_Pedrera_Sex_NeusLastWarning_GrandMother > 0:
                        
                        tx "Ya sab??a yo que esta vez no aguantar??as demasiado."

        pt "??Mierda!"

    $ p_prot.closeOrgasm += 100
    $ p_prot.pleasure += 10

    jump afternight05_Pedrera_Sex_Cumshot


label afternight05_Pedrera_Sex_NeusLastWarning_ResistingTxellMast:

    $  afternight05_Pedrera_Sex_NeusLastWarning_GrandMother += 1

    if afternight05_Pedrera_Sex_NeusLastWarning_GrandMother == 1:

        pt "De hecho,"

        extend " ahora que lo pienso,"

        pt "biol??gicamente no era mi verdadera bisabuela..."

        with vpunch

        p "??Ugh!"

        n "Con todas tus fuerzas intentas evitar que se salga con la suya,"

        n "mientras Neus no te quita los ojos de encima."

        tx "Hmmm..."

        tx "No quieres ponerme las cosas f??ciles,"

        extend " ??Verdad?"

        tx "Tranquilo,"

        extend " tengo experiencia en eso tambi??n..."

        n "Sutilmente aparta una de las manos y sientes como la acerca a tus nalgas."

        p "????Qu??-"

        extend " Qu?? pretendes hacer?!"

        tx "Ohh,"

        extend" creo que ya te lo imaginas..."

        ne "..."

        n "Un dedo curioso empieza a juguetear por el interior de tu agujero anal."

        pt "Ser??..."

        n "Al mismo tiempo que sientes su c??lida lengua acariciando la sensible carne del glande de tu polla."


    elif afternight05_Pedrera_Sex_NeusLastWarning_GrandMother == 2:

        p "Ugh..."

        tx "Hmmm..."

        n "A pesar de que vuelve a usar la ambas manos para intentar que te corras,"

        n "mantienes las fuerzas para evitar el orgasmo."

        tx "??De verdad?"

        tx "??Otra vez?"

        tx "??Tanto te gusta que juguetee con tu agujero de atr??s con mi dedo?"

        p "..."

        n "Sin demasiada demora,"

        n "vuelves a sentir su dedo juguet??n en tu cavidad anal mientras vuelve a lamer la punta de tu glande"

        n "e inevitablemente vuelves a sentir el cosquilleo que anuncia lo inevitable."

    elif afternight05_Pedrera_Sex_NeusLastWarning_GrandMother == 3:

        aj "Not yet done."

    return


#####

label NeusPermissionToKissTxell:

    show neus_exp_mouth sadbiting_Silentx01
    $ nteye = 0
    call neus_exp_tears_tears
    show neus_exp_iris front00
    show neus_exp_eyebrows surprisex03
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx003
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris front01
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "??De-"

    extend "de verdad que no te molesta, [protname]?"

    show neus_exp_mouth sadbiting_Silentx03
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx01
    with dissolve

    menu:

        pt "??Le importa mi opini??n?"

        "No es que me entusiasme la idea, pero no soy quien para decirte lo que puedes, o no puedes hacer.":

            $pl.ch_pts("np",-1)
            $pl.ch_pts("mp",-3)

            show neus_exp_mouth sad_Silentx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows angryx02
            with dissolve

            tx "..."

            show neus_exp_mouth sad_Talkingx06
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows angryx01
            with dissolve

            ne "Si te lo pregunto,"

            extend " es porque me importa tu opini??n,"

            show neus_exp_mouth sad_Talkingx005
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows angryx03
            with dissolve

            ne "??idiota!"

            show neus_exp_mouth sad_Silentx02
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris left01
            show neus_exp_eyebrows surprisex01
            with dissolve

            tx "No importa Neus..."

            $ Pedrera_char_Cond = "TxellClose_b"
            call Pedrera_char_lab

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris right03
            show m_exp_eyebrows sadx01
            with fade_short

            tx "Simplemente,"

            extend " quer??a intentarlo."

            show m_exp_mouth happybiting_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows sadx03
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Talkingx02
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx03
            with fade_short

            ne "Meritxell..."

            show neus_exp_mouth sad_Talkingx01
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx05
            with dissolve

            ne "Lo siento..."

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris left05
            show neus_exp_eyebrows sadx04
            with dissolve

            tx "No importa,"

            $ Pedrera_char_Cond = "TxellClose_b"
            call Pedrera_char_lab

            show m_exp_mouth happy_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows sadx01
            with fade_short

            tx "al menos he podido besarte una vez."

            $ Pedrera_char_Cond = "TxellClose_b"
            call Pedrera_char_lab

            show m_exp_mouth happybiting_Silentx05
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows sadx02
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth happy_Silentx03
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris left05
            show neus_exp_eyebrows sadx03
            with fade_short

            ne "..."

        "Mi opini??n no importa.":

            $pl.ch_pts("np",-1)
            $pl.ch_pts("mp",-2)

            show neus_exp_mouth sad_Talkingx09
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows angryx04
            with dissolve

            ne "??Claro que importa!"

            show neus_exp_mouth sad_Talkingx08
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows angryx03
            with dissolve

            ne "??A m?? me importa!"

            show neus_exp_mouth sad_Silentx07
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows angryx04
            with dissolve

            p "..."

            show neus_exp_mouth sad_Silentx04
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris left01
            show neus_exp_eyebrows serious
            with dissolve

            tx "No pasa nada..."

            show neus_exp_mouth sad_Silentx03
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx01
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "TxellClose_b"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with fade_short

            tx "Ten??a que intentarlo..."

            show m_exp_mouth happybiting_Silentx04
            show m_exp_eyes 06
            show m_exp_piris front06
            show m_exp_eyebrows sadx04
            with dissolve

            ne "Txell..."

            show m_exp_mouth sadbiting_Silentx05
            show m_exp_eyes 05
            show m_exp_piris left05
            show m_exp_eyebrows sadx05
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Talkingx03
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "Lo siento..."

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris left05
            show neus_exp_eyebrows sadx04
            with dissolve

        "??C??mo me va a molestar ver a dos hermosas mujeres bes??ndose ante mi?":

            $pl.ch_pts("np",1)
            $pl.ch_pts("mp",5)

            $ p_prot_likesTwoWomenKissing = True

            show neus_exp_mouth sad_Talkingx002
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows surprisex01
            with dissolve

            ne "??Lo-"

            extend "lo dices de verdad?"

            show neus_exp_mouth sad_Talkingx01
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris right02
            show neus_exp_eyebrows sadx01
            with dissolve

            ne "Yo..."

            show neus_exp_mouth sadbiting_Silentx02
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris left01
            show neus_exp_eyebrows surprisex02
            with dissolve

            pause 0.2

            scene ped_cs_kissAf_nd_comp_01:
                subpixel True
                truecenter
                zoom 1.5 ypos -0.9 # Down Zoom
                easein_quad 25.0 zoom 1.0 ypos 1.15 # Center image
            with fade

            n "Con suavidad, Meritxell acaricia su mejilla"

            n "del mismo modo en que se lo hab??a hecho ella antes."

            n "Y con suma sensualidad,"

            n "acerca sus labios a los suyos para juguetear con su lengua"

            n "y mezclarse en un suave y -gradualmente- apasionado beso"

            n "que [neusname] acepta gratamente."

            show ped_cs_kissAf_nd_comp_01:
                easein_quad 15.0 zoom 0.4 xpos 0.5 ypos 0.5 # General image

            n "No solo es de mayor intensidad,"

            n "Meritxell aprovecha para agarrarle su desnudo trasero"

            n "sin que [neusname] ofrezca demasiada resistencia."

            n "Observas el brillo de sus ojos de nuevo,"

            n "Mientras no tan solo sus piernas, sino su cuerpo entero vuelve a temblar de nuevo."

            # NOT FINISHED
            scene day05
            with fade_short

            tx "????HHHHMMMM!!"

            n "Su gemido es con a??n m??s intensidad."

            n "Con su tembleque, [neusname] acaba perdi??ndola de entre sus brazos y finalmente cae en el suelo."

            n "Sin perder un segundo, la sigue en su ca??da y desde el mismo suelo,"

            n "sigue bes??ndola con frenes?? mientras le agarra de sus enormes pechos,"

            n "Txell sigue tambaleando y gimiendo sin detenerse por un instante."

            n "Finalmente interrumpe su movimiento bucal y Meritxell cesa en su tambaleo err??tico,"

            n "lentamente se va apartando de su rostro mostrando su longeva lengua en su ascensi??n"

            n "mientras te dirige una mirada entre deseo y lujuria con una sonrisa de oreja a oreja,"

            if night04_Neus_Blowjob_Cum_Affirmative:

                n "que te recuerda un poco a la expresi??n que te hizo ayer poco antes de perder la consciencia."

            else:

                n "una imagen -probablemente- m??s aterradora que excitante."

            n "Paulatinamente se le va apagando el brillo en los ojos,"

            n "al mismo tiempo que su rostro vuelve a ser el de siempre."

            tx "..."

            n "Desde el mismo suelo y sin apenas fuerzas para poder moverse..."

            tx "Gracias."

            ne "No me des las gracias,"

            extend " tonta..."

            ne "Sabes bien que tambi??n lo he disfrutado."

            tx "Me alegra o??r eso."

    return

label p_txell_NoSex:

    $ Pedrera_char_Cond =  "TxellClose_b"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    if p_txell.pos == "doggy":

        tx "??Que me ponga a cuatro patas?"

    elif p_txell.pos == "missionary":

        tx "??Que me abra de piernas?"

    else:

        aj "ERROR 18786"

    if music_play != "dreamsBecomeReal_slow":
        play music "audio/music/kevinmacleod/sad/dreamsBecomeReal_slow.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "dreamsBecomeReal_slow"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "??Est??s pensando hacer,"

    extend " lo que creo que est??s pensando?"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "Es posible."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "Sabes perfectamente que no me vas a follar,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "??verdad?"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex002
    with dissolve

    menu:

        pt "??Puedo convencerla...?"

        "??Y por qu?? no?":
            call p_Help

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows suspiciousx01
            with dissolve

            tx "..."

            show m_exp_mouth happy_Talkingx04
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows sadx01
            with dissolve

            tx "Por que no me pones de esa manera,"

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows suspiciousx01
            with dissolve

            tx "y lo sabes."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "Ten??a que intentarlo."

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx01
            with dissolve

            tx "Psst..."

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            tx "Si t?? lo dices..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows serious
            with dissolve

        "Si no haces lo que te pido, lo m??s probable es que ma??ana mueras, o incluso, que te ocurra algo peor.":
            call p_Help

            $pl.ch_pts("dp",-3)
            $pl.ch_pts("mp",-10)
            $pl.ch_pts("np",-8)

            $ ntlong = 1

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "..."

            if music_play != "QuinnsSongANewMan":
                play music "audio/music/kevinmacleod/sad/QuinnsSongANewMan.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "QuinnsSongANewMan"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "??En serio...?"

            show m_exp_mouth sad_Talkingx08
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows angryx03
            with dissolve

            tx "??Amenazarme es tu mejor baza?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 00
            show m_exp_piris front00
            show m_exp_eyebrows surprisex002
            with dissolve

            p "T??matelo como prefieras."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows angryx03
            with dissolve

            p "Pero sabes que tengo raz??n."

            show m_exp_mouth sad_Silentx07
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx04
            with dissolve

            tx "..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris left02
            show m_exp_eyebrows serious
            with dissolve

            ne "[protname]..."

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Talkingx03
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris front03
            show neus_exp_eyebrows sadx02
            with fade

            ne "??Por qu?? le has dicho eso?"

            show neus_exp_mouth sad_Talkingx02
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "T?? no eres as??..."

            show neus_exp_mouth sadbiting_Silentx02
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows serious
            with dissolve

            p "No soy as?? contigo,"

            extend " ni con la mayor??a de la gente,"

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 0
            call neus_exp_tears_tears
            show neus_exp_iris front00
            show neus_exp_eyebrows surprisex02
            with dissolve

            p "pero con gentuza como ella..."

            show neus_exp_mouth sad_Silentx03
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris right04
            show neus_exp_eyebrows sadx02
            with dissolve

            p "act??o de la manera que se merece."

            $ Pedrera_char_Cond =  "TxellClose_b"
            call Pedrera_char_lab

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx03
            with fade_short

            tx "..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 00
            show m_exp_piris front00
            show m_exp_eyebrows surprisex02
            with dissolve

            p "??Acaso nunca te ha contado lo que hace con los hombres que intentan flirtear con ella?"

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows angryx01
            with dissolve

            p "??C??mo intenta humillarlos y re??rse de ellos?"

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows angryx02
            with dissolve

            p "??No crees que se merece una lecci??n?"

            # Conditional Sex with her? Subimissive? FOR FUTURE

            if afternoon05_NeusMeeting_Told:

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows sadx02
                with dissolve

            else:

                show m_exp_mouth sad_Silentx05
                show m_exp_eyes 01
                show m_exp_piris front01
                show m_exp_eyebrows angryx01
                with dissolve

            tx "..."

            if afternoon05_NeusMeeting_Told:

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows sadx01
                with dissolve

                tx "Pens?? que ya no pensabas eso de mi despu??s de lo que te mostr?? en mi biblioteca..."

                show m_exp_mouth sadbiting_Silentx04
                show m_exp_eyes 01
                show m_exp_piris front01
                show m_exp_eyebrows serious
                with dissolve

                p "Pues pensaste mal."

                show m_exp_mouth sad_Silentx06
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx02
                with dissolve

                tx "..."

                show m_exp_mouth sadbiting_Silentx03
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows sadx01
                with dissolve

            $ ntlong = 2

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Talkingx06
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris front03
            show neus_exp_eyebrows angryx02
            with fade

            $ ntlong = 3

            ne "Es probable que su actitud no tenga justificaci??n,"

            show neus_exp_mouth sad_Talkingx05
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris right02
            show neus_exp_eyebrows sadx01
            with dissolve

            ne " y hasta puede ser denunciable,"

            show neus_exp_mouth sad_Talkingx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows angryx02
            with dissolve

            ne "pero lo que t?? est??s exigiendo..."

            extend " es mucho peor."

            $ ntlong = 4

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx02
            with dissolve

            n "Una l??grima empieza a deslizarse por su mejilla."

            menu:

                pt "Parece que [neusname] est?? hablando muy en serio aqu??..."

                "Mi cuerpo, mi decisi??n. Si no acepta mis condiciones, por mi puede morirse.":
                    call p_Help

                    $pl.ch_pts("dp",-20)
                    $pl.ch_pts("mp",-50)
                    $pl.ch_pts("np",-100)

                    show neus_exp_mouth sadbiting_Silentx02
                    $ nteye = 0
                    call neus_exp_tears_tears
                    show neus_exp_iris front00
                    show neus_exp_eyebrows surprisex02
                    with dissolve

                    ne "..."

                    if music_play != "dayOfChaos":
                        play music "audio/music/kevinmacleod/creepy/dayOfChaos.ogg" fadein 3.0 fadeout 3.0
                    $ music_play = "dayOfChaos"


                    show neus_exp_mouth sad_Silentx02
                    $ nteye = 1
                    call neus_exp_tears_tears
                    show neus_exp_iris front01
                    show neus_exp_eyebrows serious
                    with dissolve

                    $ Pedrera_char_Cond =  "TxellClose_b"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Talkingx10
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx03
                    with fade_short

                    tx "??Lo est??s diciendo en serio?"

                    show m_exp_mouth sad_Talkingx12
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows angryx04
                    with dissolve

                    tx "????Me vas a forzar a follarte porque te molest?? que me riera de ti?!"

                    show m_exp_mouth sad_Silentx06
                    show m_exp_eyes 00
                    show m_exp_piris front00
                    show m_exp_eyebrows surprisex01
                    with dissolve

                    p "Y de todos los hombres que te has re??do."

                    show m_exp_mouth sad_Silentx09
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx04
                    with dissolve

                    tx "..."

                    show m_exp_mouth sad_Talkingx11
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows angryx04
                    with dissolve

                    tx "????Ahora vas de defensor de los d??biles hombres musculados"

                    show m_exp_mouth sad_Talkingx12
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows angryx05
                    with dissolve

                    tx "que no pueden hacerlo por ellos mismos?!"

                    show m_exp_mouth sad_Silentx06
                    show m_exp_eyes 00
                    show m_exp_piris front00
                    show m_exp_eyebrows angryx01
                    with dissolve

                    p "La fuerza o el f??sico no tiene nada que ver aqu??."

                    show m_exp_mouth sad_Talkingx11
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx04
                    with dissolve

                    tx "??Y qu?? me dices de las veces que tu compa??ero de piso con sus est??pidos amigos"

                    show m_exp_mouth sad_Talkingx09
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx05
                    with dissolve

                    tx "se han estado burlando de mis desproporcionados atributos f??sicos,"

                    show m_exp_mouth sad_Talkingx10
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx06
                    with dissolve

                    tx "que me hayan estado dibujando desnuda en clase,"

                    show m_exp_mouth sad_Talkingx11
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows angryx07
                    with dissolve

                    tx "toc??ndome el culo en los pasillos de clase o incluso en la calle,"

                    show m_exp_mouth sad_Talkingx09
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx06
                    with dissolve

                    tx "intentado espiar mientras estaba en el ba??o,"

                    show m_exp_mouth sad_Talkingx08
                    show m_exp_eyes 01
                    show m_exp_piris right01
                    show m_exp_eyebrows angryx07
                    with dissolve

                    tx "la de piropos asquerosos sin gusto ni gracia que me han llegado a lanzar"

                    show m_exp_mouth sad_Talkingx09
                    show m_exp_eyes 03
                    show m_exp_piris right03
                    show m_exp_eyebrows angryx05
                    with dissolve

                    tx "a veces incluso a medio cent??metro de mi cara,"

                    show m_exp_mouth sad_Talkingx07
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    show m_exp_eyebrows angryx06
                    with dissolve

                    tx "agarr??ndome del brazo para que les prestara atenci??n,"

                    show m_exp_mouth sad_Talkingx08
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    show m_exp_eyebrows angryx05
                    with dissolve

                    tx "algunos incluso bes??ndome o magre??ndome los pechos."

                    show m_exp_mouth sad_Talkingx10
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows angryx06
                    with dissolve

                    tx "??Y te estoy hablando solamente de lo que ha ocurrido en la escuela de Ilustraci??n!"

                    show m_exp_mouth sad_Talkingx12
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows angryx07
                    with dissolve

                    tx "????A esos tambi??n los defiendes?!"

                    show m_exp_mouth sad_Silentx15
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx06
                    with dissolve

                    p "Por supuesto que no."

                    show m_exp_mouth sad_Silentx14
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows angryx07
                    with dissolve

                    p "Lo ??nico que hice fue acudir a la cita a la que en teor??a t?? misma me invitaste."

                    show m_exp_mouth sad_Talkingx08
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx05
                    with dissolve

                    tx "??Eres consciente que no fui yo quien te invit?? realmente,"

                    extend " ??verdad?"

                    show m_exp_mouth sad_Silentx08
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx04
                    with dissolve

                    p "Lo s??,"

                    show m_exp_mouth sad_Silentx07
                    show m_exp_eyes 01
                    show m_exp_piris front01
                    show m_exp_eyebrows angryx01
                    with dissolve

                    p "A??n as?? te mereces un escarmiento por aquellos a los que humillaste"

                    show m_exp_mouth sad_Silentx10
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows angryx05
                    with dissolve

                    p "sin que hubieran cometido otro pecado,"

                    extend " que el de interesarse por ti."

                    show m_exp_mouth sad_Talkingx09
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows angryx07
                    with dissolve

                    tx "??Sabes la cantidad de t??os que me llaman haci??ndose pasar por mujeres"

                    show m_exp_mouth sad_Talkingx10
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx05
                    with dissolve

                    tx "o haci??ndose el imb??cil para intentar quedar conmigo?"

                    show m_exp_mouth sad_Talkingx11
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows angryx06
                    with dissolve

                    tx "????La de t??os que me acosan por las redes sociales?!"

                    show m_exp_mouth sad_Talkingx12
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows angryx07
                    with dissolve

                    tx "????La de hombres que me chantajean con dar a conocer mi pasado de prostituta de lujo?!"

                    show m_exp_mouth sad_Silentx12
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx07
                    with dissolve

                    p "No estoy defendiendo a esos."

                    show m_exp_mouth sad_Talkingx008
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows angryx07
                    with dissolve

                    tx "No..."

                    show m_exp_mouth sad_Talkingx08
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx06
                    with dissolve

                    tx "Est??s haciendo algo mucho peor."

                    show m_exp_mouth sad_Talkingx10
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows angryx07
                    with dissolve

                    tx "??Amenazarme con dejarme morir si no me dejo follar por ti!"

                    show m_exp_mouth sad_Silentx11
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx07
                    with dissolve

                    p "..."

                    show m_exp_mouth sad_Silentx10
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx07
                    with dissolve

                    $ Pedrera_char_Cond = "NeusClose_show"
                    call Pedrera_char_lab

                    show neus_exp_mouth sad_Talkingx06
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris front04
                    show neus_exp_eyebrows sadx04
                    with fade

                    ne "[protname]..."

                    if music_play != "heartbreaking":
                        play music "audio/music/kevinmacleod/sad/heartbreaking.ogg" fadein 3.0 fadeout 3.0
                    $ music_play = "heartbreaking"

                    $ ntlong = 5

                    show neus_exp_mouth sadbiting_Silentx07
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris front05
                    show neus_exp_eyebrows sadx07
                    with dissolve

                    p "..."

                    show neus_exp_mouth sad_Talkingx07
                    $ nteye = 8
                    call neus_exp_tears_tears
                    show neus_exp_iris front08
                    show neus_exp_eyebrows angryx03
                    with dissolve

                    ne "Si la actitud de Txell es deplorable,"

                    show neus_exp_mouth sad_Talkingx08
                    $ nteye = 3
                    call neus_exp_tears_tears
                    show neus_exp_iris front03
                    show neus_exp_eyebrows angryx05
                    with dissolve

                    ne "la tuya..."

                    extend " es..."

                    show neus_exp_mouth sadbiting_Silentx07
                    $ nteye = 7
                    call neus_exp_tears_tears
                    show neus_exp_iris front07
                    show neus_exp_eyebrows sadx07
                    with dissolve

                    n "Sus l??grimas apenas le permiten el habla."

                    $ Pedrera_char_Cond = "TxellClose_b"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Talkingx03
                    show m_exp_eyes 04
                    show m_exp_piris left04
                    show m_exp_eyebrows sadx05
                    with dissolve

                    tx "Neus..."

                    show m_exp_mouth sad_Talkingx02
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows sadx04
                    with dissolve

                    tx "Si es lo que realmente quiere,"

                    extend " yo..."

                    $ Pedrera_char_Cond = "NeusClose_show"
                    call Pedrera_char_lab

                    show neus_exp_mouth sad_Talkingx005
                    $ nteye = 2
                    call neus_exp_tears_tears
                    show neus_exp_iris right02
                    show neus_exp_eyebrows angryx02
                    with fade_short

                    ne "No."

                    show neus_exp_mouth sad_Talkingx07
                    $ nteye = 3
                    call neus_exp_tears_tears
                    show neus_exp_iris front03
                    show neus_exp_eyebrows angryx03
                    with dissolve

                    ne "??Esto se va a terminar aqu??,"

                    show neus_exp_mouth sad_Talkingx10
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris front04
                    show neus_exp_eyebrows angryx04
                    with dissolve

                    ne "y ahora!"

                    show neus_exp_mouth sad_Silentx10
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris front05
                    show neus_exp_eyebrows angryx05
                    with dissolve

                    call WIP

                    jump endupdate

                    # FOR FUTURE

                    # bad ending.

                "Quiz??s tengas raz??n...":

                    call p_Help

                    $pl.ch_pts("dp",1)
                    $pl.ch_pts("mp",1)
                    $pl.ch_pts("np",2)

                    $ Pedrera_char_Cond =  "TxellClose_b"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows suspiciousx02
                    with fade_short

                    tx "??Solo quiz??s?"

                    show m_exp_mouth sad_Silentx04
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows angryx03
                    with dissolve

                    p "..."

                    $ ntlong = 3

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 02
                    show m_exp_piris left02
                    show m_exp_eyebrows surprisex01
                    with dissolve

                    ne "??Txell!"

                    $ Pedrera_char_Cond = "NeusClose_show"
                    call Pedrera_char_lab

                    show neus_exp_mouth sad_Talkingx06
                    $ nteye = 3
                    call neus_exp_tears_tears
                    show neus_exp_iris right03
                    show neus_exp_eyebrows angryx03
                    with fade_short

                    ne "No metas m??s le??a en el fuego."

                    show neus_exp_mouth sad_Talkingx05
                    $ nteye = 2
                    call neus_exp_tears_tears
                    show neus_exp_iris right02
                    show neus_exp_eyebrows angryx01
                    with dissolve

                    ne "Ya te dije en su momento lo que pensaba de lo que hac??as con los hombres en el MACBA,"

                    show neus_exp_mouth sad_Talkingx08
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris right04
                    show neus_exp_eyebrows angryx03
                    with dissolve

                    ne "??y me juraste que no lo volver??as a hacer!"

                    show neus_exp_mouth sad_Silentx07
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris right05
                    show neus_exp_eyebrows angryx04
                    with dissolve

                    $ Pedrera_char_Cond =  "TxellClose_b"
                    call Pedrera_char_lab

                    show m_exp_mouth sadbiting_Silentx03
                    show m_exp_eyes 02
                    show m_exp_piris left02
                    show m_exp_eyebrows sadx01
                    with fade_short

                    tx "..."

                    show m_exp_mouth sad_Talkingx003
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows sadx03
                    with dissolve

                    tx "Lo siento."

                    show m_exp_mouth sadbiting_Silentx04
                    show m_exp_eyes 05
                    show m_exp_piris right05
                    show m_exp_eyebrows sadx04
                    with dissolve

                    ne "Pero por favor, [protname],"

                    $ Pedrera_char_Cond = "NeusClose_show"
                    call Pedrera_char_lab

                    show neus_exp_mouth sad_Talkingx05
                    $ nteye = 3
                    call neus_exp_tears_tears
                    show neus_exp_iris front03
                    show neus_exp_eyebrows sadx01
                    with fade_short

                    ne "no vuelvas a amenazar a nadie de esta manera."

                    show neus_exp_mouth sad_Talkingx04
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris front04
                    show neus_exp_eyebrows sadx03
                    with dissolve

                    ne "No seas como Padre,"

                    show neus_exp_mouth sad_Talkingx03
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris front05
                    show neus_exp_eyebrows sadx06
                    with dissolve

                    ne "te lo pido..."

                    show neus_exp_mouth sadbiting_Silentx04
                    $ nteye = 6
                    call neus_exp_tears_tears
                    show neus_exp_iris front06
                    show neus_exp_eyebrows sadx05
                    with dissolve

                    pause 0.2

                    $ Pedrera_char_Cond =  "TxellClose_b"
                    call Pedrera_char_lab

                    show m_exp_mouth sadbiting_Silentx04
                    show m_exp_eyes 05
                    show m_exp_piris right05
                    show m_exp_eyebrows sadx02
                    with fade

        "Seguro que te va encantar.":
            call p_Help

            $pl.ch_pts("mp",-3)
            $pl.ch_pts("np",-1)

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex002
            with dissolve

            if afternoon05_Library_Continue_Cond:

                tx "Pensaba que despu??s de lo que te cont?? en mi despacho,"

            elif afternoon04_MACBA_TxellTruth_Cond:

                tx "Pensaba que despu??s de lo que te cont?? en el museo,"

            else:

                tx "Pensaba que despu??s de lo que le ha ocurrido a Neus,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            tx "tendr??as algo m??s de materia gris en esa cabeza hueca tuya,"

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "pero aparentemente,"

            extend " me equivoqu??."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            pt "Mierda..."

        "Si tienes miedo de quedarte embarazada, tambi??n te puedo dar por detr??s.":
            call p_Help

            $pl.ch_pts("mp",-2)
            $pl.ch_pts("np",-1)

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "..."

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "??Qu?? te hace pensar que tengo el m??s m??nimo inter??s en que me des por detr??s?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex002
            with dissolve

            p "Sabes lo grande que la tengo."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows suspiciousx01
            with dissolve

            tx "??Y se supone que ese es tu mejor argumento?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex001
            with dissolve

            p "..."

            show m_exp_mouth sad_Talkingx02
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Madre m??a..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows serious
            with dissolve

            p "..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows normal
            with dissolve

            tx "No, [protname]."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows suspiciousx01
            with dissolve

            tx "No quiero que me des ni por delante,"

            extend " ni por detr??s."

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            tx "Olv??date de eso."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            pt "Mierda..."


    $ p_txell_NoSex_Confirmed = True

    

    jump afternight05_Pedrera_Sex


label afternight05_Pedrera_Sex_label:

    pt "No creo que sea buena opci??n pedirle eso..."

    jump afternight05_Pedrera_Sex


#####

label afternight05_Pedrera_ItoldYouILoveYou:

    if p_prot_NotJustMasturbate_with_p_didac == True:

        if afternight05_Pedrera_Sex_SaidJustWithNeus:

            $pl.ch_pts("np",-4)

            show n_closefromup_mouth sad_Talkingx04
            show n_closefromup_iris front08
            $ nteye = 8
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx03
            with dissolve

            ne "Tambi??n dijiste que ??nicamente lo har??as conmigo..."

            show n_closefromup_mouth sad_Talkingx03
            show n_closefromup_iris right04
            $ nteye = 4
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx04
            with dissolve

            ne "y no has usado simplemente tus manos para masturbarte..."

        else:

            $pl.ch_pts("np",-2)

            show n_closefromup_mouth sad_Talkingx03
            show n_closefromup_iris right05
            $ nteye = 5
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx04
            with dissolve

            ne "Pero est?? claro que no te importa hacer otras cosas aparte de masturbarte con otras..."

        if p_prot.titwank_received > 0:

            $pl.ch_pts("np",-2)

            show n_closefromup_mouth sad_Talkingx02
            show n_closefromup_iris front08
            $ nteye = 8
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx04
            with dissolve

            ne "Siento no tener unos pechos tan grandes como D??dac y Meritxell."

        show n_closefromup_mouth sadbiting_Silentx04
        show n_closefromup_iris front06
        $ nteye = 6
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        #p "..."

    else:

        $pl.ch_pts("np",2)

        show n_closefromup_mouth sad_Silentx03
        show n_closefromup_iris front01
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows surprisex01
        with dissolve

        ne "..."

        show n_closefromup_mouth sad_Silentx02
        show n_closefromup_iris front00
        $ nteye = 0
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows surprisex02
        with dissolve

        p "Si he me masturbado delante de ellas ha sido ??nicamente porque t?? me lo has pedido."

        show n_closefromup_mouth sadbiting_Silentx04
        show n_closefromup_iris right01
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx01
        with dissolve

        ne "..."

        show n_closefromup_mouth sad_Talkingx03
        show n_closefromup_iris front04
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "Bueno,"

        extend " supongo que tambi??n porque eres consciente de que es la ??nica manera de salvarles la vida..."

        show n_closefromup_mouth sad_Silentx02
        show n_closefromup_iris front01
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows normal
        with dissolve

        p "S??,"

        extend " supongo que tambi??n eso tambi??n es una raz??n de peso."

        show n_closefromup_mouth happy_Silentx03
        show n_closefromup_iris front02
        $ nteye = 2
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows serious
        with dissolve

        ne "Hmm..."

        show n_closefromup_mouth happy_Silentx06
        show n_closefromup_iris front06
        $ nteye = 6
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx01
        with dissolve

        n "Una dulce sonrisa aparece en sus labios."

        if pl.np > 150:

            show n_closefromup_mouth happy_Talkingx04
            show n_closefromup_iris front05
            $ nteye = 5
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx03
            with dissolve

            ne "??C??mo no enamorarme de ti?"

            show n_closefromup_mouth happy_Silentx03
            show n_closefromup_iris front06
            $ nteye = 6
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx04
            with dissolve

    if music_play != "grooveGrove":
        play music "audio/music/kevinmacleod/sad/grooveGrove.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "grooveGrove"

    return

label afternight05_Pedrera_Sex_HardToSee_beginning:

    show n_closefromup_mouth sad_Silentx03
    show n_closefromup_iris front00
    $ nteye = 0
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows surprisex02
    with dissolve

    p "Tambi??n me ha resultado dif??cil..."

    show n_closefromup_mouth sad_Talkingx03
    show n_closefromup_iris front02
    $ nteye = 2
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx01
    with dissolve

    ne "??A qu?? te refieres...?"

    show n_closefromup_mouth sadbiting_Silentx04
    show n_closefromup_iris front01
    $ nteye = 1
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows normal
    with dissolve

    return

label afternight05_Pedrera_Sex_HardToSee_kiss:

    call afternight05_Pedrera_Sex_HardToSee_beginning

    show n_closefromup_mouth sad_Silentx02
    show n_closefromup_iris front00
    $ nteye = 0
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows surprisex02
    with dissolve

    if p_didac.cumReceived == "oral" and p_txell.cumReceived == "oral":

        p "El ver besarte tan apasionadamente con ambas,"
    else:

        if p_didac.cumReceived == "oral":

            p "El verte besarte tan apasionadamente con D??dac,"

        if p_txell.cumReceived == "oral":

            p "El verte besarte tan apasionadamente con Txell,"

    extend " no ha sido algo f??cil de digerir."

    if p_prot_likesTwoWomenKissing:

        $pl.ch_pts("np",-3)

        show n_closefromup_mouth sad_Talkingx09
        show n_closefromup_iris front02
        $ nteye = 2
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows angryx03
        with dissolve

        ne "??Pero si antes me has dicho que no te molestaba ver a dos hermosas mujeres bes??ndose!"

        show n_closefromup_mouth sadbiting_Silentx07
        show n_closefromup_iris front01
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows angryx02
        with dissolve

        p "..."

        show n_closefromup_mouth sad_Talkingx07
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows angryx02
        with dissolve

        ne "??Acl??rate!"

        show n_closefromup_mouth sad_Talkingx09
        show n_closefromup_iris front05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows angryx02
        with dissolve

        ne "??Y no te vayas contradiciendo cada dos por tres!"

        show n_closefromup_mouth sad_Silentx06
        show n_closefromup_iris right05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows angryx02
        with dissolve

        pt "Raz??n,"

        extend " tiene..."

    else:

        show n_closefromup_mouth sadbiting_Silentx08
        show n_closefromup_iris front00
        $ nteye = 0
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows surprisex02
        with dissolve

        ne "..."

        show n_closefromup_mouth sad_Talkingx02
        show n_closefromup_iris right05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "Lo-"

        extend "lo siento..."

        show n_closefromup_mouth sad_Talkingx03
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        ne "Pero sabes que era necesario..."

        show n_closefromup_mouth sadbiting_Silentx07
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx05
        with dissolve

        call afternight05_Pedrera_Sex_HardToSee_general
            # p "??Y era necesario tambi??n que lo gozaras del modo en que lo has hecho?"

    return

        #ne "..."
        #ne "No me gustar??a que te sintieras obligado a hacerlo conmigo..."

label afternight05_Pedrera_Sex_HardToSee_oralSex:

    call afternight05_Pedrera_Sex_HardToSee_beginning

    if p_didac.cumReceived in ["vaginal", "anal"] and p_txell.cumReceived in ["vaginal", "anal"]:

        p "Ver c??mo les pasabas tu lengua a ambas por su entrepierna,"

    else:

        if p_didac.cumReceived in ["vaginal", "anal"]:

            p "Ver c??mo le pasabas la lengua a D??dac por su entrepierna,"

        if p_txell.cumReceived in ["vaginal", "anal"]:

            p "Ver c??mo le pasabas la lengua a Meritxell por su entrepierna,"

    show n_closefromup_mouth sadbiting_Silentx03
    show n_closefromup_iris front00
    $ nteye = 0
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows surprisex02
    with dissolve

    p "no ha sido algo..."

    show n_closefromup_mouth sadbiting_Silentx06
    show n_closefromup_iris front05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx04
    with dissolve

    p "agradable de ver."

    show n_closefromup_mouth sadbiting_Silentx08
    show n_closefromup_iris right05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx05
    with dissolve

    ne "..."

    show n_closefromup_mouth sad_Talkingx03
    show n_closefromup_iris right02
    $ nteye = 2
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx02
    with dissolve

    ne "Cre??a que te gustar??a ver a dos chicas hacerlo entre ellas,"

    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_iris down05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx03
    with dissolve

    ne "al fin y al cabo,"

    extend " es una fantas??a bastante com??n entre los hombres..."

    show n_closefromup_mouth sadbiting_Silentx06
    show n_closefromup_iris front05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx04
    with dissolve

    menu:

        "Cuando son dos desconocidas, quiz??s, pero no cuando veo a la persona amada hacerlo con otra.":
            call p_Help

            $pl.ch_pts("np",1)

            show n_closefromup_mouth sadbiting_Silentx06
            show n_closefromup_iris front00
            $ nteye = 0
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows surprisex02
            with dissolve

            ne "..."

            show n_closefromup_mouth sad_Talkingx06
            show n_closefromup_iris front05
            $ nteye = 5
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx03
            with dissolve

            ne "[protname]..."

            show n_closefromup_mouth sad_Talkingx05
            show n_closefromup_iris front08
            $ nteye = 8
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx05
            with dissolve

            ne "Lo siento..."

        "Lo encuentro algo bastante antinatural y de mal gusto.":
            call p_Help

            $pl.ch_pts("np",-5)

            show n_closefromup_mouth sadbiting_Silentx04
            show n_closefromup_iris front01
            $ nteye = 1
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows surprisex01
            with dissolve

            ne "..."

            show n_closefromup_mouth sad_Talkingx07
            show n_closefromup_iris front02
            $ nteye = 2
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows angryx02
            with dissolve

            ne "No te ten??a por alguien tan carca..."

            show n_closefromup_mouth sadbiting_Silentx06
            show n_closefromup_iris front00
            $ nteye = 0
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows surprisex02
            with dissolve

            p "Pues es lo que hay."

            show n_closefromup_mouth sadbiting_Silentx08
            show n_closefromup_iris right05
            $ nteye = 5
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx05
            with dissolve

            ne "..."

        "Pues ser?? la excepci??n, pero no me gusta.":
            call p_Help

            $pl.ch_pts("np",-1)

            show n_closefromup_mouth sadbiting_Silentx06
            show n_closefromup_iris front00
            $ nteye = 0
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows surprisex02
            with dissolve

            ne "..."

            show n_closefromup_mouth sad_Talkingx03
            show n_closefromup_iris front05
            $ nteye = 5
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx04
            with dissolve

            ne "Lo lamento..."

    show n_closefromup_mouth sad_Talkingx07
    show n_closefromup_iris right04
    $ nteye = 4
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx06
    with dissolve

    ne "Pero sabes que lo ten??a que hacer para poder salvarlas."

    show n_closefromup_mouth sadbiting_Silentx07
    show n_closefromup_iris right05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx05
    with dissolve

    call afternight05_Pedrera_Sex_HardToSee_general

    return

        #ne "..."
        #ne "No me gustar??a que te sintieras obligado a hacerlo conmigo..."


label afternight05_Pedrera_Sex_HardToSee_general:

    # CHOICE

    menu:

        "??Y era necesario tambi??n que lo gozaras del modo en que lo has hecho?":
            call p_Help

            $pl.ch_pts("np",-2)

            show n_closefromup_mouth sadbiting_Silentx09
            show n_closefromup_iris front00
            $ nteye = 0
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows surprisex01
            with dissolve

            ne "..."

            show n_closefromup_mouth sad_Talkingx002
            show n_closefromup_iris front05
            $ nteye = 5
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx03
            with dissolve

            ne "No..."

            show n_closefromup_mouth sad_Talkingx004
            show n_closefromup_iris right05
            $ nteye = 5
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx04
            with dissolve

            ne "Eso no lo era..."

            show n_closefromup_mouth sadbiting_Silentx09
            show n_closefromup_iris front08
            $ nteye = 8
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx05
            with dissolve

            menu:

                "????Entonces?!":

                    call p_Help

                    $pl.ch_pts("np",-2)

                    show n_closefromup_mouth sad_Talkingx03
                    show n_closefromup_iris front05
                    $ nteye = 5
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows sadx06
                    with dissolve

                    ne "Lo siento..."

                    show n_closefromup_mouth sadbiting_Silentx08
                    show n_closefromup_iris front05
                    $ nteye = 5
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows sadx05
                    with dissolve

                "Eso demuestra que no te importa lo que opino.":

                    call p_Help

                    $pl.ch_pts("np",-1)

                    show n_closefromup_mouth sad_Talkingx12
                    show n_closefromup_iris front01
                    $ nteye = 1
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows angryx03
                    with dissolve

                    ne "??Eso no es verdad!"

                    show n_closefromup_mouth sadbiting_Silentx08
                    show n_closefromup_iris front00
                    $ nteye = 0
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows surprisex02
                    with dissolve

                    p "??Entonces c??mo lo explicas?"

                    show n_closefromup_mouth sadbiting_Silentx10
                    show n_closefromup_iris right05
                    $ nteye = 5
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows sadx05
                    with dissolve

                "Me dio asco.":

                    call p_Help

                    $pl.ch_pts("np",-4)

                    show n_closefromup_mouth sadbiting_Silentx06
                    show n_closefromup_iris front00
                    $ nteye = 0
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows surprisex02
                    with dissolve

                    ne "..."

                    show n_closefromup_mouth sad_Talkingx08
                    show n_closefromup_iris front02
                    $ nteye = 2
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows suspiciousx02
                    with dissolve

                    ne "??Asco...?"

                    show n_closefromup_mouth sadbiting_Silentx07
                    show n_closefromup_iris front00
                    $ nteye = 0
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows normal
                    with dissolve

                    p "S??."

                    show n_closefromup_mouth sad_Talkingx04
                    show n_closefromup_iris front05
                    $ nteye = 5
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows sadx04
                    with dissolve

                    ne "Pensaba que me amabas,"

                    extend " no que te hac??a asco."

                    show n_closefromup_mouth sadbiting_Silentx06
                    show n_closefromup_iris front02
                    $ nteye = 2
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows angryx03
                    with dissolve

                    p "Es antinatural."

                    show n_closefromup_mouth sad_Silentx07
                    show n_closefromup_iris right05
                    $ nteye = 5
                    call n_closefromup_tears_tears
                    show n_closefromup_eyebrows angryx04
                    with dissolve

            ne "..."

            show n_closefromup_mouth sad_Talkingx04
            show n_closefromup_iris front08
            $ nteye = 8
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx04
            with dissolve

            ne "Cuando se trata de esperma,"

            extend " especialmente si es el tuyo,"

            show n_closefromup_mouth sad_Talkingx06
            show n_closefromup_iris front02
            $ nteye = 2
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx03
            with dissolve

            ne "me resulta muy dif??cil controlarme..."

            show n_closefromup_mouth sad_Talkingx02
            show n_closefromup_iris front08
            $ nteye = 8
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx05
            with dissolve

            ne "Lo lamento."

            # show n_closefromup_mouth sadbiting_Silentx09
            # show n_closefromup_iris front06
            # $ nteye = 6
            # call n_closefromup_tears_tears
            # show n_closefromup_eyebrows sadx06
            # with dissolve

            # p "..."

        "...":
            call p_Help

    return

label afternight05_Pedrera_Sex_changeposNull:

    call ped_reduceRestTurns

    $ p_prot.action = "rest"
    $ p_prot.b_action = "rest"

    $ p_didac.action = "rest"
    $ p_didac.b_action = "rest"

    $ p_txell.action = "rest"
    $ p_txell.b_action = "rest"

    $ p_neus.action = "rest"
    $ p_neus.b_action = "rest"

    return

label afternight05_Pedrera_Sex_actionNull:

    $ p_prot.action = "rest"
    if p_didac.action != "cunnilingus_done_p_txell":
        $ p_didac.action = "rest"
    $ p_txell.action = "rest"
    $ p_neus.action = "rest"

    return

label afternight05_Pedrera_Sex_TOTAL_actionNull:

    $ p_prot.action = "rest"
    $ p_prot.b_action = "rest"

    $ p_girl_active.action = "rest"
    $ p_girl_active.b_action = "rest"

    return

label p_neus_orgasm_warning:

    $ nleye = "horny"

    $ nblush += 1

    if p_prot.pos == "69":
        call ped_sex_69_mc_blowjob_Stop

        show gensex_69_L_d_mouth sad_Talkingx09

    elif p_prot.pos == "oral":

        call p_neus_blowjob_stop_label

        $ nteye = "front07"
        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx008
        show gensex_oral_n_frontHead_exp_eyebrows angryx04
        call gensex_oral_n_frontHead_exp_tears_tears
    with vpunch

    ne "??No!"

    if p_prot.pos == "69":
        show gensex_69_L_d_mouth sad_Silentx08
        with dissolve

    scene black
    with fade_short

    stop music fadeout 1.0
    $ music_play = "stop"

    $ renpy.music.set_volume(0.0, delay=2.0, channel='sfx2')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='sfx3')

    pt "????Me ha dado una patada?!"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    show n_closefromup_mouth sadbiting_Silentx04
    #show n_closefromup_iris front08
    $ nteye = "front08"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows angryx02
    with vpunch

    n "Sientes su cuerpo sobre el tuyo."

    show n_closefromup_mouth sad_Talkingx08
    #show n_closefromup_iris front01
    $ nteye = "front00"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows angryx03
    with dissolve

    ne "??A??n no!"

    if music_play != "rightBehindYou":
        play music "audio/music/kevinmacleod/creepy/rightBehindYou.ogg" fadein 5.0 fadeout 3.0
        $ music_play = "rightBehindYou"


    $ nleye = "full"

    show n_closefromup_mouth sadbiting_Silentx09
    $ nteye = "front00"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows angryx04
    with dissolve

    pt "Sus ojos otra vez..."

    $ p_neus.orgasm = 0 
    $ p_neus.closeOrgasmTotal = 0
    $ p_neus.closeOrgasm = 0
    $ p_neus.pleasure = 0

    show n_closefromup_mouth sad_Talkingx07
    $ nteye = "front08"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows angryx05
    with dissolve

    ne "??[protname]!"

    show n_closefromup_mouth sad_Talkingx09
    $ nteye = "front01"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows angryx04
    with dissolve

    ne "??Te dije que no me quer??a correr!"

    show n_closefromup_mouth sad_Talkingx06
    $ nteye = "front04"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx03
    with dissolve

    ne "????Es que no lo entiendes?!"

    $ ped_neus_whispers_sfx04 = 0.0
    $ ped_neus_whispers_sfx03 = 0.0
    $ p_neus.closeOrgasmTotal = 0
    $ p_neus.closeOrgasm = 0
    $ p_neus.pleasure = 0
    $ nblush = 0

    $ nleye = "horny"

    show n_closefromup_mouth sad_Talkingx004
    $ nteye = "front08"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx04
    with dissolve

    ne "No te va a gustar lo que vas a ver de mi..."

    show n_closefromup_mouth sadbiting_Silentx06
    $ nteye = "front01"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows normal
    with dissolve

    p "Eso no lo sabes,"

    show n_closefromup_mouth sad_Silentx07
    $ nteye = "front08"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows angryx03
    with dissolve

    p "es posible que..."

    show n_closefromup_mouth sad_Talkingx007
    $ nteye = "front00"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows angryx04
    with dissolve

    ne "??No!"

    show n_closefromup_mouth sad_Talkingx03
    $ nteye = "front05"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx04
    with dissolve

    ne "Por favor..."

    show n_closefromup_mouth sad_Talkingx04
    $ nteye = "front03"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx06
    with dissolve

    ne "no lo hagas..."

    show n_closefromup_mouth sad_Talkingx05
    $ nteye = "front05"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx04
    with dissolve

    ne "Esto no lo podr?? volver a hacer,"

    show n_closefromup_mouth sad_Talkingx06
    $ nteye = "right03"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx05
    with dissolve

    ne "si vuelvo a estar tan cerca del orgasmo,"

    show n_closefromup_mouth sad_Talkingx04
    $ nteye = "right05"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx06
    with dissolve

    ne "ya no podr?? evitarlo."

    show n_closefromup_mouth sadbiting_Silentx06
    $ nteye = "front05"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx07
    with dissolve

    p "..."

    show n_closefromup_mouth sadbiting_Silentx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx05
    with dissolve

    if music_play != "aura":
        play music "audio/music/alcaknight/aura.ogg" fadein 5.0 fadeout 3.0
        $ music_play = "aura"


    $ p_prot.action = "rest"
    $ p_prot.b_action = "rest"
    $ p_girl_active.action = "rest"
    $ p_girl_active.b_action = "rest"

    $ p_neus.orgasmScene = False

    $ p_neus.orgasm = 1 # Fake Orgasm.
    $ p_neus.closeOrgasmTotal = 0
    $ p_neus.closeOrgasm = 0
    $ p_neus.pleasure = 0

    ## "Should I decide which pose to do now?"

    jump afternight05_Pedrera_Sex

label p_any_restart:

    $ p_prot.action = "rest"
    $ p_prot.b_action = "rest"
    $ p_didac.action = "rest"
    $ p_didac.b_action = "rest"
    $ p_txell.action = "rest"
    $ p_txell.b_action = "rest"
    $ p_neus.action = "rest"
    $ p_neus.b_action = "rest"
    $ p_prot.restTurns = 0
    #$ p_prot.doingNothingTurns = 0
    $ takeDickOut_Cond = 0

    $ p_prot.pos_oral_rest = 0
    $ p_prot.pos_69_rest = 0
    $ p_prot.pos_missionary_rest = 0
    $ p_prot.pos_doggy_rest = 0

    $ p_prot.masturbate = 0

    return



###########


######


##########


label afternight05_Pedrera_n_Neus_Warning:
    
    call afternight05_Pedrera_Sex_Check_after_restNumbers

    $ afternight05_Pedrera_n_Neus_Warning_Cond = True

    if p_active == "p_neus" and p_prot.pos == "69" and p_prot.b_action == "rest":

        ## progcheck "Neus is not sucking your dick."

        pass

    elif (
        ((p_active == "p_neus" and p_neus_orgasmHurry == False) and (p_prot.action in ["cunnilingus_done", "anilingus_done"] or p_prot.b_action == "cunnilingus_done")) or
        p_active == "p_neus" and p_prot.pos == "69" and p_prot.b_action in ["blowjob_received", "blowjobDeep_received"] or
        p_prot.action in ["vaginal_done", "vaginalDeep_done", "anal_done", "analDeep_done", "blowjob_received", "blowjobDeep_received"]
        ):

        if p_prot.action in ["vaginal_done", "vaginalDeep_done", "anal_done", "analDeep_done", "blowjob_received", "blowjobDeep_received"]:
            pass
            #progcheck "MC is receiving pleasure."

        if p_active == "p_neus" and p_prot.pos == "69" and p_prot.b_action in ["blowjob_received", "blowjobDeep_received"]:
            pass
            #progcheck "MC is being sucked by Neus in 69"

        elif p_active == "p_neus":

            if p_neus_orgasmHurry == False: #Neus is not in a hurry.
                pass
            else:

                aj "ERROR... this shouldn't happen."

        else:

            aj "ERROR... Is it Neus or not?"

        return
    ###

    $ randomnum_1to5 = renpy.random.randint(1, 5)

    ###

    $ debug ("Neus_Warning.")

    if p_prot.b_action == "blowjob_received":

        pass

    elif p_prot.action in ["cunnilingus_done", "anilingus_done"]:

        $ afternight05_Pedrera_Neus_Warning_tongue += 1

        # if afternight05_Pedrera_Neus_Warning_tongue > 1:
        #     $ Pedrera_char_Cond = "NeusClose_show"
        #     call Pedrera_char_lab

        #if afternight05_Pedrera_Neus_Warning_tongue == 1:
        if p_prot_restTemp == 1:

            pass

        #elif afternight05_Pedrera_Neus_Warning_tongue in [2, 3]:
        elif p_prot_restTemp in [2,3]:

            $ ped_check_1_10("ped_n_neus_warning_01_list")

            # if ped_check_list_result in range(1,11):
            #     show neus_exp_mouth sad_Talkingx05
            #     show neus_exp_iris front02
            #     $ nteye = 2
            #     call neus_exp_tears_tears
            #     show neus_exp_eyebrows sadx02
            #     with fade_short


            if ped_check_list_result == 1:

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                    show gensex_missionary_n_head_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                ne "No me parece mal que prepares el camino,"

                if p_prot.pos == "oral":
                    $ nteye = "front04"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx03
                    show gensex_oral_n_frontHead_exp_eyebrows sadx06
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front04"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx03
                    show gensex_missionary_n_head_exp_eyebrows sadx06
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx02
                with dissolve

                ne "pero..."

            elif ped_check_list_result == 2:

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                    show gensex_missionary_n_head_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                ne "Deber??as hacer algo m??s que usar tu lengua."

                if gensex_ILoveYouNeus:

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                        show gensex_oral_n_frontHead_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front04"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                        show gensex_missionary_n_head_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx006
                    with dissolve

                    p "??No te gusta lo que hago?"

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx02
                        show gensex_oral_n_frontHead_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front08"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx02
                        show gensex_missionary_n_head_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx01
                    with dissolve

                    ne "Demasiado..."

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front03"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                        show gensex_missionary_n_head_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx05
                    with dissolve

                    ne "Ese es el problema..."

                elif gensex_YoureAMonster:

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx04
                        show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front00"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx04
                        show gensex_missionary_n_head_exp_eyebrows surprisex01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx03
                    with dissolve

                    p "Har?? lo que me parezca."

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sad_Silentx05
                        show gensex_oral_n_frontHead_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front04"
                        show gensex_missionary_n_head_exp_mouth sad_Silentx05
                        show gensex_missionary_n_head_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx04
                    with dissolve

                    ne "..."

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx08
                        show gensex_oral_n_frontHead_exp_eyebrows sadx08
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "right05"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx08
                        show gensex_missionary_n_head_exp_eyebrows sadx08
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx06
                    with dissolve

                else:

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx02
                        show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx02
                        show gensex_missionary_n_head_exp_eyebrows surprisex01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx02
                    with dissolve

                    p "Sabes que te encanta."

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                        show gensex_oral_n_frontHead_exp_eyebrows suspiciousx02
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front05"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                        show gensex_missionary_n_head_exp_eyebrows suspiciousx02
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx04
                    with dissolve

                    ne "..."

            elif ped_check_list_result == 3:

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                    show gensex_missionary_n_head_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx06
                with dissolve

                ne "No la tienes d??nde deber??a estar..."

                if gensex_ILoveYouNeus:

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                        show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                        show gensex_missionary_n_head_exp_eyebrows surprisex01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    p "??Y d??nde deber??a estar?"

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                        show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front04"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                        show gensex_missionary_n_head_exp_eyebrows surprisex01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx05
                    with dissolve

                    ne "..."

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx002
                        show gensex_oral_n_frontHead_exp_eyebrows sadx02
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front08"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx002
                        show gensex_missionary_n_head_exp_eyebrows sadx02
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx002
                    with dissolve

                    ne "Tonto..."

                else:

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                        show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front01"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                        show gensex_missionary_n_head_exp_eyebrows surprisex01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    p "Creo que tengo derecho a elegir hacer lo que me plazca,"

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx10
                        show gensex_oral_n_frontHead_exp_eyebrows suspiciousx02
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx10
                        show gensex_missionary_n_head_exp_eyebrows suspiciousx02
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx07
                    with dissolve

                    p "al fin y al cabo es lo que has hecho t?? conmigo."

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx12
                        show gensex_oral_n_frontHead_exp_eyebrows sadx03
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "right03"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx12
                        show gensex_missionary_n_head_exp_eyebrows sadx03
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx06
                    with dissolve

                    ne "..."

            elif ped_check_list_result == 4:

                if ((p_active == "p_neus" and (p_neus.vaginal_received == 0))):

                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_n_frontHead_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                        show gensex_missionary_n_head_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx06
                    with dissolve

                    ne "Me hubiera gustado poder sentirla dentro..."

                    if p_neus.anal_received == 0:

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front08"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                            show gensex_missionary_n_head_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx004
                        with dissolve

                        ne "Aunque fuera por detr??s..."

                else:

                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_n_frontHead_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                        show gensex_missionary_n_head_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx03
                    with dissolve

                    ne "Me gustar??a volver a sentirla dentro...."

                if p_prot.pos == "oral":
                    $ nteye = "front00"
                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx07
                    show gensex_oral_n_frontHead_exp_eyebrows sadx06
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front08"
                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx07
                    show gensex_missionary_n_head_exp_eyebrows sadx06
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sadbiting_Silentx05
                with dissolve

                menu:

                    pt "Realmente quiere sentirla dentro..."

                    "Har?? lo que me plazca." if gensex_ILoveYouNeus == False:
                        call p_Help
                        $pl.ch_pts("np",-2)

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front01"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx03
                            show gensex_missionary_n_head_exp_eyebrows surprisex02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx03
                        with dissolve

                        ne "..."

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx03
                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right04"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx03
                            show gensex_missionary_n_head_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx002
                        with dissolve

                        ne "Lo-"

                        extend "lo siento..."

                    "??Tambi??n te hubiera gustado matar a alg??n otro ni??o?" if gensex_ILoveYouNeus == False:
                        call p_Help
                        $pl.ch_pts("np",-8)

                        $ gensex_INotLoveYouNeus = True
                        $ gensex_YoureAMonster = True

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front00"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx03
                            show gensex_missionary_n_head_exp_eyebrows surprisex02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx02
                        with dissolve

                        ne "..."

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx02
                            show gensex_oral_n_frontHead_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front02"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx02
                            show gensex_missionary_n_head_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx001
                        with dissolve

                        ne "[protname]..."

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx001
                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right04"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx001
                            show gensex_missionary_n_head_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx01
                        with dissolve

                        ne "Yo..."

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx04
                            show gensex_oral_n_frontHead_exp_eyebrows sadx07
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front08"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx04
                            show gensex_missionary_n_head_exp_eyebrows sadx07
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx02
                        with dissolve

                        ne "Lo siento..."

                        $ ntlong += 1

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx04
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front00"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx04
                            show gensex_missionary_n_head_exp_eyebrows surprisex02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx03
                        with dissolve

                        p "Tus disculpas no le devolver??n la vida."

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front05"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx03
                            show gensex_missionary_n_head_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx04
                        with dissolve

                        ne "..."

                        $ ntlong += 1

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx09
                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front08"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx09
                            show gensex_missionary_n_head_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx05
                        with dissolve

                        ne "..."

                    "Si me lo pides bien, quiz??s lo haga m??s tarde.":
                        call p_Help
                        #$pl.ch_pts("np",-2)

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front01"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx03
                            show gensex_missionary_n_head_exp_eyebrows surprisex02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx03
                        with dissolve

                        ne "..."

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx003
                            show gensex_oral_n_frontHead_exp_eyebrows angryx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front04"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx003
                            show gensex_missionary_n_head_exp_eyebrows angryx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx002
                        with dissolve

                        ne "Eres malo..."

                    "Ya la tienes dentro, ??no te gusta lo que te estoy haciendo?":
                        call p_Help
                        $pl.ch_pts("np",2)

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx07
                            show gensex_oral_n_frontHead_exp_eyebrows angryx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front03"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx07
                            show gensex_missionary_n_head_exp_eyebrows angryx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx05
                        with dissolve

                        ne "Sabes perfectamente a qu?? me refiero."

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx007
                            show gensex_oral_n_frontHead_exp_eyebrows angryx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front08"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx007
                            show gensex_missionary_n_head_exp_eyebrows angryx04
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx005
                        with dissolve

                        ne "??Y por supuesto que me encanta!"

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx003
                            show gensex_oral_n_frontHead_exp_eyebrows angryx01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front04"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx003
                            show gensex_missionary_n_head_exp_eyebrows angryx01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx002
                        with dissolve

                        ne "Tonto..."

                    "No te quejes tanto...":
                        call p_Help
                        $pl.ch_pts("np",-1)

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx08
                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front04"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx08
                            show gensex_missionary_n_head_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx06
                        with dissolve

                        ne "..."

            elif ped_check_list_result == 5:

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                    show gensex_missionary_n_head_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                ne "Entiendo que tengas un tama??o enorme y debas..."

                if p_prot.pos == "oral":
                    $ nteye = "front00"
                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx08
                    show gensex_oral_n_frontHead_exp_eyebrows sadx06
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front08"
                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx08
                    show gensex_missionary_n_head_exp_eyebrows sadx06
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sadbiting_Silentx06
                with dissolve

                ne "..."

                if p_prot.pos == "oral":
                    $ nteye = "front00"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx006
                    show gensex_oral_n_frontHead_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx006
                    show gensex_missionary_n_head_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx005
                with dissolve

                ne "Pero quiz??s deber??as dejar que te lo hiciera yo a ti..."

            elif ped_check_list_result == 6:

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                    show gensex_missionary_n_head_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                ne "Me alegra que te guste tanto pasar tu lengua por mi entrepierna,"

                if p_prot.pos == "oral":
                    $ nteye = "front00"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx03
                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front08"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx03
                    show gensex_missionary_n_head_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx02
                with dissolve

                ne "de verdad..."

                if p_prot.pos == "oral":
                    $ nteye = "front00"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_n_frontHead_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "down04"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                    show gensex_missionary_n_head_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

                ne "Pero si no terminas pronto..."

                if p_neus_orgasmHurry:

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front06"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                        show gensex_missionary_n_head_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx003
                    with dissolve

                    ne "No creo pueda aguantar mucho m??s..."

            elif ped_check_list_result == 7:

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                    show gensex_missionary_n_head_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                ne "Si sigues as??..."

                if p_prot.pos == "oral":
                    $ nteye = "front00"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_n_frontHead_exp_eyebrows sadx07
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front05"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                    show gensex_missionary_n_head_exp_eyebrows sadx07
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

                if p_neus_orgasmHurry:

                    ne "No aguantar?? mucho m??s..."

                else:

                    ne "No creo que pueda aguantar mucho m??s..."

            elif ped_check_list_result == 8:

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx006
                    show gensex_oral_n_frontHead_exp_eyebrows angryx02
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "down03"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx006
                    show gensex_missionary_n_head_exp_eyebrows angryx02
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx004
                with dissolve

                ne "Si con tu enorme polla no fuera suficiente,"

                if p_prot.pos == "oral":
                    $ nteye = "front00"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_n_frontHead_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front06"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                    show gensex_missionary_n_head_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

                ne "Encima se te da realmente bien usar la lengua..."

                if p_prot.pos == "oral":
                    $ nteye = "front00"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx03
                    show gensex_oral_n_frontHead_exp_eyebrows sadx07
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "down05"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx03
                    show gensex_missionary_n_head_exp_eyebrows sadx07
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx02
                with dissolve

                ne "Me pregunto con cuantas habr??s estado para ser tan bueno con ella..."

                if p_prot.pos == "oral":
                    $ nteye = "front00"
                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx07
                    show gensex_oral_n_frontHead_exp_eyebrows sadx06
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front08"
                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx07
                    show gensex_missionary_n_head_exp_eyebrows sadx06
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sadbiting_Silentx05
                with dissolve

                menu:

                    pt "????Con cuantas he estado?!"

                    "Podr??a preguntarte lo mismo.":
                        call p_Help
                        #$pl.ch_pts("np",2)

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front02"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx03
                            show gensex_missionary_n_head_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx02
                        with dissolve

                        ne "..."

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx08
                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right05"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx08
                            show gensex_missionary_n_head_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx06
                        with dissolve

                        ne "..."

                    "??Tienes que preguntarme esto ahora?":
                        call p_Help
                        $pl.ch_pts("np",-1)

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front02"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx03
                            show gensex_missionary_n_head_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx03
                        with dissolve

                        ne "..."

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx03
                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "down05"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx03
                            show gensex_missionary_n_head_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx02
                        with dissolve

                        ne "Lo siento..."

                    "M??s de las que te puedas imaginar.":
                        call p_Help
                        $pl.ch_pts("np",-3)

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx02
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front01"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx02
                            show gensex_missionary_n_head_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx02
                        with dissolve

                        ne "..."

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx02
                            show gensex_oral_n_frontHead_exp_eyebrows sadx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front05"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx02
                            show gensex_missionary_n_head_exp_eyebrows sadx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx001
                        with dissolve

                        ne "Ya..."

                    "Disfr??talo y no pienses en eso.":
                        call p_Help
                        $pl.ch_pts("np",1)

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front02"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx03
                            show gensex_missionary_n_head_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx03
                        with dissolve

                        ne "..."

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx002
                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "down05"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx002
                            show gensex_missionary_n_head_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx001
                        with dissolve

                        ne "Lo-"

                        extend "lo siento..."

                        if gensex_YoureAMonster == False and gensex_INotLoveYouNeus == False:

                            if p_prot.pos == "oral":
                                $ nteye = "front00"
                                show gensex_oral_n_frontHead_exp_mouth sad_Silentx05
                                show gensex_oral_n_frontHead_exp_eyebrows sadx01
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front04"
                                show gensex_missionary_n_head_exp_mouth sad_Silentx05
                                show gensex_missionary_n_head_exp_eyebrows sadx01
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Silentx04
                            with dissolve

                            p "No te disculpes tanto, [neusname]."

                            if p_prot.pos == "oral":
                                $ nteye = "front00"
                                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx01
                                show gensex_oral_n_frontHead_exp_eyebrows sadx03
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front08"
                                show gensex_missionary_n_head_exp_mouth sad_Talkingx01
                                show gensex_missionary_n_head_exp_eyebrows sadx03
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Talkingx01
                            with dissolve

                            ne "Lo..."

                            if p_prot.pos == "oral":
                                $ nteye = "front00"
                                show gensex_oral_n_frontHead_exp_mouth sad_Silentx06
                                show gensex_oral_n_frontHead_exp_eyebrows suspiciousx03
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "right02"
                                show gensex_missionary_n_head_exp_mouth sad_Silentx06
                                show gensex_missionary_n_head_exp_eyebrows suspiciousx03
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Silentx04
                            with dissolve

                            p "..."

                            if p_prot.pos == "oral":
                                $ nteye = "front00"
                                show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx05
                                show gensex_oral_n_frontHead_exp_eyebrows sadx06
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front06"
                                show gensex_missionary_n_head_exp_mouth happybiting_Silentx05
                                show gensex_missionary_n_head_exp_eyebrows sadx06
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth happybiting_Silentx05
                            with dissolve

                            ne "..."

                            if p_prot.pos == "oral":
                                $ nteye = "front00"
                                show gensex_oral_n_frontHead_exp_mouth happy_Talkingx03
                                show gensex_oral_n_frontHead_exp_eyebrows sadx03
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front05"
                                show gensex_missionary_n_head_exp_mouth happy_Talkingx03
                                show gensex_missionary_n_head_exp_eyebrows sadx03
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth happy_Talkingx02
                            with dissolve

                            ne "Gracias."

                    "??Quieres que pare?":
                        call p_Help
                        $pl.ch_pts("np",1)

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front02"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx03
                            show gensex_missionary_n_head_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx02
                        with dissolve

                        ne "..."

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth happy_Talkingx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front04"
                            show gensex_missionary_n_head_exp_mouth happy_Talkingx06
                            show gensex_missionary_n_head_exp_eyebrows sadx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth happy_Talkingx05
                        with dissolve

                        ne "No..."

                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                            show gensex_oral_n_frontHead_exp_eyebrows angryx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front06"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                            show gensex_missionary_n_head_exp_eyebrows angryx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx05
                        with dissolve

                        ne "Digo,"

                        extend " s??..."

                        if p_neus_orgasmHurry:

                            if p_prot.pos == "oral":
                                $ nteye = "front00"
                                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx03
                                show gensex_oral_n_frontHead_exp_eyebrows sadx03
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "down04"
                                show gensex_missionary_n_head_exp_mouth sad_Talkingx03
                                show gensex_missionary_n_head_exp_eyebrows sadx03
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Talkingx02
                            with dissolve

                            ne "Es solo que..."

                            if p_prot.pos == "oral":
                                $ nteye = "front00"
                                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                                show gensex_oral_n_frontHead_exp_eyebrows sadx05
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front07"
                                show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                                show gensex_missionary_n_head_exp_eyebrows sadx05
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Talkingx04
                            with dissolve

                            ne "estoy casi a punto, [protname]..."

                        else:

                            if p_prot.pos == "oral":
                                $ nteye = "front00"
                                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx004
                                show gensex_oral_n_frontHead_exp_eyebrows sadx03
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front08"
                                show gensex_missionary_n_head_exp_mouth sad_Talkingx004
                                show gensex_missionary_n_head_exp_eyebrows sadx03
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Talkingx003
                            with dissolve

                            ne "No lo s??..."

                            if p_prot.pos == "oral":
                                $ nteye = "front00"
                                show gensex_oral_n_frontHead_exp_mouth happy_Talkingx05
                                show gensex_oral_n_frontHead_exp_eyebrows sadx05
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "down04"
                                show gensex_missionary_n_head_exp_mouth happy_Talkingx05
                                show gensex_missionary_n_head_exp_eyebrows sadx05
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Talkingx04
                            with dissolve

                            ne "Realmente me encanta,"

                            if p_prot.pos == "oral":
                                $ nteye = "front00"
                                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx07
                                show gensex_oral_n_frontHead_exp_eyebrows angryx02
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front07"
                                show gensex_missionary_n_head_exp_mouth sad_Talkingx07
                                show gensex_missionary_n_head_exp_eyebrows angryx02
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Talkingx06
                            with dissolve

                            ne "pero..."

                            if p_prot.pos == "oral":
                                $ nteye = "front00"
                                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                                show gensex_oral_n_frontHead_exp_eyebrows serious
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front03"
                                show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                                show gensex_missionary_n_head_exp_eyebrows serious
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Talkingx04
                            with dissolve

                            ne "No creo que vaya a aguantar mucho m??s este ritmo..."

            elif ped_check_list_result == 9:

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                    show gensex_missionary_n_head_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                ne "Te agradezco lo que haces por mi [protname],"

                if p_prot.pos == "oral":
                    $ nteye = "front00"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_n_frontHead_exp_eyebrows sadx03
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front08"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                    show gensex_missionary_n_head_exp_eyebrows sadx03
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx005
                with dissolve

                ne "pero de verdad..."

                if p_neus_orgasmHurry:

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx08
                        show gensex_oral_n_frontHead_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front06"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx08
                        show gensex_missionary_n_head_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx004
                    with dissolve

                    ne "Estoy a punto de correrme,"

                else:

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx07
                        show gensex_oral_n_frontHead_exp_eyebrows serious
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front05"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx07
                        show gensex_missionary_n_head_exp_eyebrows serious
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx06
                    with dissolve

                    ne "as?? conseguir??s que me corra antes que t??,"

                if p_prot.pos == "oral":
                    $ nteye = "front00"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx09
                    show gensex_oral_n_frontHead_exp_eyebrows angryx03
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front04"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx09
                    show gensex_missionary_n_head_exp_eyebrows angryx03
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx006
                with dissolve

                ne "y no la tienes d??nde deber??a de estar..."

            elif ped_check_list_result == 10:

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                    show gensex_missionary_n_head_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx06
                with dissolve

                ne "Si solo usas tu lengua..."


            ##

            $ ped_check_1_10("ped_n_neus_warning_02_list")

            if ped_check_list_result == 1:

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx07
                    show gensex_oral_n_frontHead_exp_eyebrows sadx02
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx07
                    show gensex_missionary_n_head_exp_eyebrows sadx02
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx06
                with dissolve

                ne "Se nos har?? de d??a..."

                if p_prot.pos == "oral":
                    $ nteye = "front05"
                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx07
                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front05"
                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx07
                    show gensex_missionary_n_head_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sadbiting_Silentx06
                with dissolve

            elif ped_check_list_result == 2:

                if p_prot.pos == "oral":
                    $ nteye = "front04"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx07
                    show gensex_oral_n_frontHead_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front04"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx07
                    show gensex_missionary_n_head_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx06
                with dissolve

                ne "El tiempo va pasando..."

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx09
                    show gensex_oral_n_frontHead_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front05"
                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx09
                    show gensex_missionary_n_head_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sadbiting_Silentx06
                with dissolve

            elif ped_check_list_result == 3:

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx07
                    show gensex_oral_n_frontHead_exp_eyebrows sadx02
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx07
                    show gensex_missionary_n_head_exp_eyebrows sadx02
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx06
                with dissolve

                ne "No tenemos toda la noche..."

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx09
                    show gensex_oral_n_frontHead_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front05"
                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx09
                    show gensex_missionary_n_head_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sadbiting_Silentx06
                with dissolve

            elif ped_check_list_result == 4:

                if p_prot.pos == "oral":
                    $ nteye = "front03"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx07
                    show gensex_oral_n_frontHead_exp_eyebrows sadx06
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front03"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx07
                    show gensex_missionary_n_head_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx06
                with dissolve

                ne "Como te corras fuera..."

                if gensex_YoureAMonster == False and gensex_INotLoveYouNeus == False:

                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx03
                        show gensex_oral_n_frontHead_exp_eyebrows sadx01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx03
                        show gensex_missionary_n_head_exp_eyebrows sadx01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx03
                    with dissolve

                    p "Tranquila,"

                    extend " lo controlo..."

                    if p_prot.pos == "oral":
                        $ nteye = "front05"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx04
                        show gensex_oral_n_frontHead_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front05"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx04
                        show gensex_missionary_n_head_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx04
                    with dissolve

                else:

                    if p_prot.pos == "oral":
                        $ nteye = "front08"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front08"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                        show gensex_missionary_n_head_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx05
                    with dissolve

            elif ped_check_list_result == 5:

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx07
                    show gensex_oral_n_frontHead_exp_eyebrows sadx02
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx07
                    show gensex_missionary_n_head_exp_eyebrows sadx02
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx003
                with dissolve

                ne "Se est?? haciendo tarde..."

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx09
                    show gensex_oral_n_frontHead_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front05"
                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx09
                    show gensex_missionary_n_head_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sadbiting_Silentx05
                with dissolve

            elif ped_check_list_result == 6:

                if p_prot.pos == "oral":
                    $ nteye = "front01"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx07
                    show gensex_oral_n_frontHead_exp_eyebrows angryx03
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front01"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx07
                    show gensex_missionary_n_head_exp_eyebrows angryx03
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx06
                with dissolve

                ne "Realmente lo est??s tomando a broma..."

                if p_prot.pos == "oral":
                    $ nteye = "front03"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx11
                    show gensex_oral_n_frontHead_exp_eyebrows sadx02
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front03"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx11
                    show gensex_missionary_n_head_exp_eyebrows sadx02
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx005
                with dissolve

                ne "y yo te estoy hablando muy en serio, [protname]..."

                if gensex_YoureAMonster:

                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                        show gensex_oral_n_frontHead_exp_eyebrows sadx01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front00"
                        show gensex_missionary_n_head_exp_mouth sad_Silentx03
                        show gensex_missionary_n_head_exp_eyebrows sadx01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Silentx03
                    with dissolve

                    p "Nunca me tomar??a en broma a una asesina en serie."

                    if p_prot.pos == "oral":
                        $ nteye = "front04"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                        show gensex_oral_n_frontHead_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front04"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                        show gensex_missionary_n_head_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx04
                    with dissolve

                    ne "..."

                    $ ntlong += 1

                    if p_prot.pos == "oral":
                        $ nteye = "right05"
                        show gensex_oral_n_frontHead_exp_mouth sad_Silentx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx09
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "right05"
                        show gensex_missionary_n_head_exp_mouth sad_Silentx06
                        show gensex_missionary_n_head_exp_eyebrows sadx08
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Silentx05
                    with dissolve

                else:

                    if p_prot.pos == "oral":
                        $ nteye = "front08"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx07
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front08"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                        show gensex_missionary_n_head_exp_eyebrows sadx07
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx05
                    with dissolve

            elif ped_check_list_result == 7:

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx07
                    show gensex_oral_n_frontHead_exp_eyebrows sadx02
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx07
                    show gensex_missionary_n_head_exp_eyebrows sadx02
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx06
                with dissolve

                ne "Si sigues as??..."

                if p_prot.action == "cunnilingus_done" or p_prot.action == "anilingus_done":

                    p "Shhh..."

                    p "Disfr??talo."

                if p_prot.pos == "oral":
                    $ nteye = "front08"
                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                    show gensex_oral_n_frontHead_exp_eyebrows sadx07
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front08"
                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                    show gensex_missionary_n_head_exp_eyebrows sadx07
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sadbiting_Silentx05
                with dissolve

            elif ped_check_list_result == 8:

                if p_prot.pos == "oral":
                    $ nteye = "front08"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_n_frontHead_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front08"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                    show gensex_missionary_n_head_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

                ne "Si conocieras mejor a Padre,"

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx07
                    show gensex_oral_n_frontHead_exp_eyebrows sadx06
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx07
                    show gensex_missionary_n_head_exp_eyebrows sadx06
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx005
                with dissolve

                ne "entender??as porque te pido que te corras pronto..."

                if p_prot.pos == "oral":
                    $ nteye = "front05"
                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                    show gensex_oral_n_frontHead_exp_eyebrows sadx07
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front05"
                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                    show gensex_missionary_n_head_exp_eyebrows sadx07
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sadbiting_Silentx05
                with dissolve

            elif ped_check_list_result == 9:

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx005
                    show gensex_oral_n_frontHead_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx005
                    show gensex_missionary_n_head_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx003
                with dissolve

                ne "Enti??ndelo..."

                if gensex_YoureAMonster:

                    if p_prot.pos == "oral":
                        $ nteye = "front03"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx03
                        show gensex_oral_n_frontHead_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front03"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx03
                        show gensex_missionary_n_head_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx03
                    with dissolve

                    p "Lo entiendo,"

                    extend " lo entiendo demasiado bien."

                if p_prot.pos == "oral":
                    $ nteye = "front08"
                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx05
                    show gensex_oral_n_frontHead_exp_eyebrows sadx07
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front08"
                    show gensex_missionary_n_head_exp_mouth sad_Silentx05
                    show gensex_missionary_n_head_exp_eyebrows sadx07
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Silentx04
                with dissolve


            elif ped_check_list_result == 10:

                if p_prot.pos == "oral":
                    $ nteye = "front01"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                    show gensex_oral_n_frontHead_exp_eyebrows sadx03
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front01"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                    show gensex_missionary_n_head_exp_eyebrows sadx03
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve


                ne "No tenemos toda la noche."

                if p_prot.pos == "oral":
                    $ nteye = "front03"
                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front03"
                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                    show gensex_missionary_n_head_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sadbiting_Silentx05
                with dissolve


            else:

                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_n_frontHead_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                    show gensex_missionary_n_head_exp_eyebrows sadx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve


                ne "[protname]..."

                if p_prot.pos == "oral":
                    $ nteye = "front08"
                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front08"
                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                    show gensex_missionary_n_head_exp_eyebrows sadx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sadbiting_Silentx04
                with dissolve

        # if p_prot_restTemp > 3:
        else:

            call afternight05_Pedrera_n_Neus_Warning_4Times
            #call p_neus_rest_calm_label # This can't be used, we are already in side the Warning.
            


######

    elif p_prot.restTurns > 1:

        window hide dissolve
        pause 0.2

        # $ Pedrera_char_Cond = "NeusClose_show"
        # call Pedrera_char_lab

        if p_prot.restTurns == 2:

            $ ped_check_1_10("ped_n_neus_warning_03_list")

            if ped_check_list_result == 1:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                        show gensex_missionary_n_head_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve


                ne "Sino haces algo,"

                extend " se nos har?? de d??a."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                        show gensex_oral_n_frontHead_exp_eyebrows serious
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Silentx03
                        show gensex_missionary_n_head_exp_eyebrows serious
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Silentx01
                    with dissolve

                p "Por lo que tengo entendido,"

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front01"
                        show gensex_oral_n_frontHead_exp_mouth sad_Silentx02
                        show gensex_oral_n_frontHead_exp_eyebrows normal
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front01"
                        show gensex_missionary_n_head_exp_mouth sad_Silentx02
                        show gensex_missionary_n_head_exp_eyebrows normal
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Silentx01
                    with dissolve

                p "Txell y D??dac ya est??n selladas."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front00"
                        show gensex_oral_n_frontHead_exp_mouth sad_Silentx01
                        show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front00"
                        show gensex_missionary_n_head_exp_mouth sad_Silentx01
                        show gensex_missionary_n_head_exp_eyebrows surprisex02
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Silentx01
                    with dissolve

                p "Solo faltas t??."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "right01"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx04
                        show gensex_oral_n_frontHead_exp_eyebrows suspiciousx02
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "right01"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx04
                        show gensex_missionary_n_head_exp_eyebrows suspiciousx02
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx03
                    with dissolve

                ne "..."

                if gensex_YoureAMonster == True or gensex_INotLoveYouNeus == True:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex001
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front00"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                            show gensex_missionary_n_head_exp_eyebrows surprisex001
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx04
                        with dissolve

                    p "As?? que te puedes esperar,"

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front03"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front03"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                            show gensex_missionary_n_head_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx05
                        with dissolve

                    p "no hay ninguna prisa."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front08"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                        show gensex_oral_n_frontHead_exp_eyebrows sadx08
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front08"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                        show gensex_missionary_n_head_exp_eyebrows sadx08
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx03
                    with dissolve

                ne "[protname]..."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front05"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx005
                        show gensex_oral_n_frontHead_exp_eyebrows sadx09
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front05"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx005
                        show gensex_missionary_n_head_exp_eyebrows sadx08
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx004
                    with dissolve

                ne "Tienes razones para estar decepcionado conmigo,"

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx006
                        show gensex_oral_n_frontHead_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx006
                        show gensex_missionary_n_head_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx005
                    with dissolve

                ne "pero tan pronto como despunte el sol en el horizonte,"

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front03"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx07
                        show gensex_oral_n_frontHead_exp_eyebrows sadx09
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front03"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx07
                        show gensex_missionary_n_head_exp_eyebrows sadx08
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx05
                    with dissolve

                ne "tendremos que salir de aqu?? lo m??s deprisa que podamos"

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front01"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx09
                        show gensex_oral_n_frontHead_exp_eyebrows sadx03
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front01"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx09
                        show gensex_missionary_n_head_exp_eyebrows sadx03
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx07
                    with dissolve

                ne "y probablemente tenga que usar mis poderes para..."

                if gensex_YoureAMonster == True or gensex_INotLoveYouNeus == True:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front01"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx03
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front01"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx03
                            show gensex_missionary_n_head_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx02
                        with dissolve

                    p "??Ni hablar!"

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx02
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front00"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx02
                            show gensex_missionary_n_head_exp_eyebrows surprisex02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx01
                        with dissolve

                    p "No vas a usar esos poderes nunca m??s."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front02"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                            show gensex_oral_n_frontHead_exp_eyebrows sadx02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front02"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                            show gensex_missionary_n_head_exp_eyebrows sadx02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx04
                        with dissolve

                    ne "..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front08"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front08"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                            show gensex_missionary_n_head_exp_eyebrows sadx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx05
                        with dissolve

                    ne "Te prometo que no los usar?? a menos que sea estrictamente necesario..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front00"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                            show gensex_missionary_n_head_exp_eyebrows surprisex02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx04
                        with dissolve

                    p "??Era necesario que los usaras con esa pareja en el vag??n del funicular cuando ??bamos al Tibidabo?"

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front02"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx04
                            show gensex_oral_n_frontHead_exp_eyebrows sadx04
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front02"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx04
                            show gensex_missionary_n_head_exp_eyebrows sadx04
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx03
                        with dissolve

                    ne "..."

                    $ ntlong += 1

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front03"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx003
                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front03"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx003
                            show gensex_missionary_n_head_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx0032
                        with dissolve

                    ne "No..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "right02"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx002
                            show gensex_oral_n_frontHead_exp_eyebrows sadx07
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right02"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx002
                            show gensex_missionary_n_head_exp_eyebrows sadx07
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx001
                        with dissolve

                    ne "Yo..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "right04"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right04"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                            show gensex_missionary_n_head_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx03
                        with dissolve

                    ne "solo quer??a..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx04
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front00"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx04
                            show gensex_missionary_n_head_exp_eyebrows surprisex02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx03
                        with dissolve

                    p "Tener el capricho de estar solos en el vag??n para ense??arme que no llevabas bragas."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front05"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front05"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx06
                            show gensex_missionary_n_head_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx05
                        with dissolve

                    ne "..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front02"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx04
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front02"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                            show gensex_missionary_n_head_exp_eyebrows sadx04
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx04
                        with dissolve

                    p "??Es eso lo que entiendes por estrictamente necesario?"

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front08"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx008
                            show gensex_oral_n_frontHead_exp_eyebrows angryx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front08"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx008
                            show gensex_missionary_n_head_exp_eyebrows angryx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx006
                        with dissolve

                    ne "??No!"

                    $ ntlong += 1

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front03"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx08
                            show gensex_oral_n_frontHead_exp_eyebrows angryx04
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front03"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx08
                            show gensex_missionary_n_head_exp_eyebrows angryx04
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx05
                        with dissolve

                    ne "Por supuesto que no..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front02"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx04
                            show gensex_oral_n_frontHead_exp_eyebrows sadx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front02"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx04
                            show gensex_missionary_n_head_exp_eyebrows sadx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx03
                        with dissolve

                    p "????Entonces?!"

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "right03"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right03"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                            show gensex_missionary_n_head_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx05
                        with dissolve

                    ne "..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front08"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx03
                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front08"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx03
                            show gensex_missionary_n_head_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx02
                        with dissolve

                    ne "Lo-"

                    extend "lo siento..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_n_frontHead_exp_eyebrows sadx01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front00"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx03
                            show gensex_missionary_n_head_exp_eyebrows sadx01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx03
                        with dissolve

                    p "Eso d??selo a los padres de ese ni??o."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front04"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front04"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                            show gensex_missionary_n_head_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx05
                        with dissolve

                    ne "..."

                    $ ntlong += 1

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "right05"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx07
                            show gensex_oral_n_frontHead_exp_eyebrows sadx10
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right05"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx07
                            show gensex_missionary_n_head_exp_eyebrows sadx10
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx06
                        with dissolve

                else:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front01"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx02
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front01"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx02
                            show gensex_missionary_n_head_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx01
                        with dissolve

                    p "??De verdad es necesario que los vuelvas a usar?"

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front03"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                            show gensex_oral_n_frontHead_exp_eyebrows sadx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front03"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                            show gensex_missionary_n_head_exp_eyebrows sadx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx03
                        with dissolve

                    ne "Solo si es estrictamente necesario,"

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front08"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front08"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                            show gensex_missionary_n_head_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx05
                        with dissolve

                    ne "no sabes de lo que es capaz Padre..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "right02"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                            show gensex_oral_n_frontHead_exp_eyebrows sadx04
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right02"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                            show gensex_missionary_n_head_exp_eyebrows sadx04
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx04
                        with dissolve

                    ne "incluso a pleno d??a,"

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "right04"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right04"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                            show gensex_missionary_n_head_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx03
                        with dissolve

                    ne "especialmente a menos de veinticuatro horas para el solsticio..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "right05"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx04
                            show gensex_oral_n_frontHead_exp_eyebrows sadx07
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right05"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx04
                            show gensex_missionary_n_head_exp_eyebrows sadx07
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx03
                        with dissolve

                    menu:

                        pt "Antes del solsticio..."

                        "Me f??o de ti." if gensex_ILoveYouNeus == True:
                            call p_Help
                            $pl.ch_pts("np",3)

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front01"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                                    show gensex_oral_n_frontHead_exp_eyebrows normal
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front01"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx03
                                    show gensex_missionary_n_head_exp_eyebrows normal
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx02
                                with dissolve

                            ne "..."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front06"
                                    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx06
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front06"
                                    show gensex_missionary_n_head_exp_mouth happy_Talkingx06
                                    show gensex_missionary_n_head_exp_eyebrows sadx02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth happy_Talkingx05
                                with dissolve

                            ne "Gracias [protname],"

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front07"
                                    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx09
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front07"
                                    show gensex_missionary_n_head_exp_mouth happy_Talkingx09
                                    show gensex_missionary_n_head_exp_eyebrows sadx05
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth happy_Talkingx07
                                with dissolve

                            ne "muchas gracias."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front06"
                                    show gensex_oral_n_frontHead_exp_mouth happy_Silentx08
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx04
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front06"
                                    show gensex_missionary_n_head_exp_mouth happy_Silentx08
                                    show gensex_missionary_n_head_exp_eyebrows sadx04
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth happy_Silentx06
                                with dissolve

                        "Lo entiendo.":
                            call p_Help
                            $pl.ch_pts("np",1)

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front06"
                                    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx05
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx04
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front06"
                                    show gensex_missionary_n_head_exp_mouth happy_Talkingx05
                                    show gensex_missionary_n_head_exp_eyebrows sadx04
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth happy_Talkingx04
                                with dissolve

                            ne "Gracias por entenderlo."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front08"
                                    show gensex_oral_n_frontHead_exp_mouth happy_Silentx04
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx09
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front08"
                                    show gensex_missionary_n_head_exp_mouth happy_Silentx04
                                    show gensex_missionary_n_head_exp_eyebrows sadx08
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth happy_Silentx03
                                with dissolve

                        "No me parece bien.":
                            call p_Help
                            #$pl.ch_pts("np",-1)

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front05"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx01
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front05"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx03
                                    show gensex_missionary_n_head_exp_eyebrows sadx01
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx02
                                with dissolve

                            ne "..."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front08"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx07
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front08"
                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                                    show gensex_missionary_n_head_exp_eyebrows sadx07
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Talkingx03
                                with dissolve

                            ne "Lo siento..."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front08"
                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx04
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx09
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front08"
                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx04
                                    show gensex_missionary_n_head_exp_eyebrows sadx08
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sadbiting_Silentx03
                                with dissolve

                        "...":
                            call p_Help
                            #$pl.ch_pts("np",2)

            elif ped_check_list_result == 2:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                        show gensex_missionary_n_head_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx05
                    with dissolve

                ne "No podemos estar as?? toda la noche."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front05"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front05"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                        show gensex_missionary_n_head_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx04
                    with dissolve

            elif ped_check_list_result == 3:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                        show gensex_missionary_n_head_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx05
                    with dissolve
                ne "Ser??a bueno que hicieras algo que tambi??n te llevara al orgasmo..."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front05"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front05"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                        show gensex_missionary_n_head_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx05
                    with dissolve

            elif ped_check_list_result == 4:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                        show gensex_missionary_n_head_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx05
                    with dissolve

                ne "[protname],"

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front03"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx08
                        show gensex_oral_n_frontHead_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front03"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx08
                        show gensex_missionary_n_head_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx06
                    with dissolve

                ne "no tenemos toda la noche."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx09
                        show gensex_oral_n_frontHead_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx09
                        show gensex_missionary_n_head_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx07
                    with dissolve

                ne "Si no haces algo,"

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front04"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_n_frontHead_exp_eyebrows sadx08
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front04"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                        show gensex_missionary_n_head_exp_eyebrows sadx08
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx03
                    with dissolve

                ne "lo tendr?? que hacer yo."

                if gensex_YoureAMonster:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front01"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx04
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front01"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx04
                            show gensex_missionary_n_head_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx04
                        with dissolve

                    p "Lo dices como si fuera la primera vez que haces algo horrible."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front03"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                            show gensex_oral_n_frontHead_exp_eyebrows sadx04
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front03"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                            show gensex_missionary_n_head_exp_eyebrows sadx04
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx05
                        with dissolve

                    ne "[protname]..."

                    $ ntlong += 1

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front04"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front04"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                            show gensex_missionary_n_head_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx04
                        with dissolve

                    ne "No seas as??,"

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front05"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx07
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front05"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                            show gensex_missionary_n_head_exp_eyebrows sadx07
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx05
                        with dissolve

                    ne "por favor..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front06"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front06"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                            show gensex_missionary_n_head_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx05
                        with dissolve

                else:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front05"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front05"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                            show gensex_missionary_n_head_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx05
                        with dissolve

            elif ped_check_list_result == 5:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                        show gensex_missionary_n_head_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx05
                    with dissolve

                ne "No lo dec??a en broma,"

                extend " [protname]"

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front03"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                        show gensex_oral_n_frontHead_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front03"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                        show gensex_missionary_n_head_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                ne "No tenemos toda la noche."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front05"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx08
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front05"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                        show gensex_missionary_n_head_exp_eyebrows sadx08
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx05
                    with dissolve

            elif ped_check_list_result == 6:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                        show gensex_missionary_n_head_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                ne "Si amanece,"

                extend " ser?? demasiado tarde..."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front05"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front05"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                        show gensex_missionary_n_head_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx05
                    with dissolve

            elif ped_check_list_result == 7:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                        show gensex_missionary_n_head_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx05
                    with dissolve

                ne "No podemos perder el tiempo as??..."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front04"
                        show gensex_oral_n_frontHead_exp_mouth sad_Silentx04
                        show gensex_oral_n_frontHead_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front04"
                        show gensex_missionary_n_head_exp_mouth sad_Silentx04
                        show gensex_missionary_n_head_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Silentx03
                    with dissolve

                menu:

                    pt "Perder el tiempo..."

                    "Yo no lo llamar??a perder el tiempo."if gensex_ILoveYouNeus:
                        call p_Help
                        $pl.ch_pts("np",1)

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "front01"
                                show gensex_oral_n_frontHead_exp_mouth sad_Silentx02
                                show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front01"
                                show gensex_missionary_n_head_exp_mouth sad_Silentx02
                                show gensex_missionary_n_head_exp_eyebrows surprisex01
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Silentx01
                            with dissolve

                        ne "..."

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "front08"
                                show gensex_oral_n_frontHead_exp_mouth happy_Talkingx05
                                show gensex_oral_n_frontHead_exp_eyebrows sadx05
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front08"
                                show gensex_missionary_n_head_exp_mouth happy_Talkingx05
                                show gensex_missionary_n_head_exp_eyebrows sadx05
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth happy_Talkingx04
                            with dissolve

                        ne "No seas tonto..."

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "front05"
                                show gensex_oral_n_frontHead_exp_mouth happy_Silentx06
                                show gensex_oral_n_frontHead_exp_eyebrows sadx04
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front05"
                                show gensex_missionary_n_head_exp_mouth happy_Silentx06
                                show gensex_missionary_n_head_exp_eyebrows sadx04
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth happy_Silentx05
                            with dissolve

                    "Me importa un r??bano lo que pienses." if gensex_YoureAMonster == True or gensex_INotLoveYouNeus == True:
                        call p_Help
                        $pl.ch_pts("np",-3)

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "front00"
                                show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx04
                                show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front00"
                                show gensex_missionary_n_head_exp_mouth sadbiting_Silentx04
                                show gensex_missionary_n_head_exp_eyebrows surprisex02
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sadbiting_Silentx03
                            with dissolve

                        ne "..."

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "front02"
                                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                                show gensex_oral_n_frontHead_exp_eyebrows sadx04
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front02"
                                show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                                show gensex_missionary_n_head_exp_eyebrows sadx04
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Talkingx03
                            with dissolve

                        ne "??Por qu?? eres as???"

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "front04"
                                show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx03
                                show gensex_oral_n_frontHead_exp_eyebrows sadx06
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front04"
                                show gensex_missionary_n_head_exp_mouth sadbiting_Silentx03
                                show gensex_missionary_n_head_exp_eyebrows sadx06
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sadx05
                            with dissolve

                        p "Sabes muy bien el por qu??."

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "right05"
                                show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                                show gensex_oral_n_frontHead_exp_eyebrows sadx08
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "right05"
                                show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                                show gensex_missionary_n_head_exp_eyebrows sadx08
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sadbiting_Silentx04
                            with dissolve

                        ne "..."

                    "Lo entiendo." if gensex_YoureAMonster == False:
                        call p_Help
                        $pl.ch_pts("np",1)

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "front03"
                                show gensex_oral_n_frontHead_exp_mouth happy_Talkingx05
                                show gensex_oral_n_frontHead_exp_eyebrows sadx02
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front03"
                                show gensex_missionary_n_head_exp_mouth happy_Talkingx05
                                show gensex_missionary_n_head_exp_eyebrows sadx02
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth happy_Talkingx04
                            with dissolve

                        ne "Gracias [protname]."

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "front06"
                                show gensex_oral_n_frontHead_exp_mouth happy_Silentx06
                                show gensex_oral_n_frontHead_exp_eyebrows sadx05
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front06"
                                show gensex_missionary_n_head_exp_mouth happy_Silentx06
                                show gensex_missionary_n_head_exp_eyebrows sadx05
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth happy_Silentx05
                            with dissolve

                    "...":
                        call p_Help
                        #$pl.ch_pts("np",2)

            elif ped_check_list_result == 8:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                        show gensex_missionary_n_head_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                ne "Enti??ndelo..."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front05"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx09
                        show gensex_oral_n_frontHead_exp_eyebrows sadx07
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front05"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx09
                        show gensex_missionary_n_head_exp_eyebrows sadx07
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx06
                    with dissolve

            elif ped_check_list_result == 9:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                        show gensex_missionary_n_head_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx05
                    with dissolve

                ne "No me obligues..."

                if gensex_YoureAMonster:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front01"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front01"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx03
                            show gensex_missionary_n_head_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx02
                        with dissolve

                    p "??Te resulta m??s dif??cil obligar que matar?"

                    $ ntlong += 1

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front03"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx09
                            show gensex_oral_n_frontHead_exp_eyebrows sadx07
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front03"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx09
                            show gensex_missionary_n_head_exp_eyebrows sadx07
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx06
                        with dissolve

                    ne "..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "right05"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx09
                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right05"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx09
                            show gensex_missionary_n_head_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx07
                        with dissolve

                else:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front04"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front04"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                            show gensex_missionary_n_head_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx04
                        with dissolve

            elif ped_check_list_result == 10:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front08"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx005
                        show gensex_oral_n_frontHead_exp_eyebrows sadx03
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front08"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx005
                        show gensex_missionary_n_head_exp_eyebrows sadx03
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx004
                    with dissolve

                ne "No quiero tener que obligarte..."

                if gensex_YoureAMonster:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front00"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx03
                            show gensex_missionary_n_head_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx02
                        with dissolve

                    p "Y sin embargo,"

                    extend " lo har??s."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front04"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx05
                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front04"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx05
                            show gensex_missionary_n_head_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx04
                        with dissolve

                    ne "..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "right05"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx07
                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right05"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx07
                            show gensex_missionary_n_head_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx05
                        with dissolve

                else:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front08"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                            show gensex_oral_n_frontHead_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front08"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                            show gensex_missionary_n_head_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx03
                        with dissolve

            else:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front03"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                        show gensex_oral_n_frontHead_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front03"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                        show gensex_missionary_n_head_exp_eyebrows sadx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                ne "[protname]..."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front05"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front05"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                        show gensex_missionary_n_head_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx05
                    with dissolve

            # show neus_exp_mouth sadbiting_Silentx05
            # show neus_exp_iris front05
            # $ nteye = 5
            # call neus_exp_tears_tears
            # show neus_exp_eyebrows sadx04
            # with dissolve

        elif p_prot.restTurns == 3:

            $ ped_check_1_10("ped_n_neus_warning_04_list")

            if ped_check_list_result == 1:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front03"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx08
                        show gensex_oral_n_frontHead_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front03"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx08
                        show gensex_missionary_n_head_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx05
                    with dissolve

                ne "Si sigues as??,"

                extend " voy a tener que..."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front04"
                        show gensex_oral_n_frontHead_exp_mouth sad_Silentx07
                        show gensex_oral_n_frontHead_exp_eyebrows angryx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front04"
                        show gensex_missionary_n_head_exp_mouth sad_Silentx07
                        show gensex_missionary_n_head_exp_eyebrows angryx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Silentx06
                    with dissolve

                menu:

                    pt "??No se atreve a terminar la frase?"

                    "??Violarme?":
                        call p_Help
                        $pl.ch_pts("np",-1)

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "front00"
                                show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx03
                                show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front00"
                                show gensex_missionary_n_head_exp_mouth sadbiting_Silentx03
                                show gensex_missionary_n_head_exp_eyebrows surprisex02
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sadbiting_Silentx02
                            with dissolve

                        ne "..."

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "right03"
                                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx005
                                show gensex_oral_n_frontHead_exp_eyebrows suspiciousx02
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "right03"
                                show gensex_missionary_n_head_exp_mouth sad_Talkingx005
                                show gensex_missionary_n_head_exp_eyebrows suspiciousx02
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Talkingx004
                            with dissolve

                        ne "No lo llamar??a as??..."

                        if gensex_YoureAMonster or gensex_INotLoveYouNeus:

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front00"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx04
                                    show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front00"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx04
                                    show gensex_missionary_n_head_exp_eyebrows surprisex02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx03
                                with dissolve

                            p "Pero aparentemente eres toda una experta en eso."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front03"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx07
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front03"
                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                                    show gensex_missionary_n_head_exp_eyebrows sadx07
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Talkingx04
                                with dissolve

                            ne "[protname]..."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front05"
                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx07
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx08
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front05"
                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx07
                                    show gensex_missionary_n_head_exp_eyebrows sadx08
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sadbiting_Silentx05
                                with dissolve

                        else:

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front01"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx02
                                    show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front01"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx02
                                    show gensex_missionary_n_head_exp_eyebrows surprisex01
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx01
                                with dissolve

                            p "??C??mo lo llamar??as entonces?"

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "right02"
                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx07
                                    show gensex_oral_n_frontHead_exp_eyebrows suspiciousx03
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "right02"
                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx07
                                    show gensex_missionary_n_head_exp_eyebrows suspiciousx03
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sadbiting_Silentx06
                                with dissolve

                        if gensex_YoureAMonster == False and gensex_INotLoveYouNeus == False:

                            menu:

                                "Tampoco es que me vaya a quejar, eh...":
                                    call p_Help
                                    $pl.ch_pts("np",5)

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front01"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx02
                                            show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front01"
                                            show gensex_missionary_n_head_exp_mouth sad_Silentx02
                                            show gensex_missionary_n_head_exp_eyebrows surprisex01
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Silentx01
                                        with dissolve

                                    ne "..."

                                    $ nblush += 1

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front05"
                                            show gensex_oral_n_frontHead_exp_mouth happy_Talkingx09
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx03
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front05"
                                            show gensex_missionary_n_head_exp_mouth happy_Talkingx09
                                            show gensex_missionary_n_head_exp_eyebrows sadx03
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth happy_Talkingx04
                                        with dissolve

                                    ne "Tonto..."

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front07"
                                            show gensex_oral_n_frontHead_exp_mouth happy_Silentx07
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx04
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front07"
                                            show gensex_missionary_n_head_exp_mouth happy_Silentx07
                                            show gensex_missionary_n_head_exp_eyebrows sadx04
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth happybiting_Silentx04
                                        with dissolve

                                "...":
                                    call p_Help

                    "??Tomar la iniciativa?":
                        call p_Help

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "front02"
                                show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx04
                                show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front02"
                                show gensex_missionary_n_head_exp_mouth sadbiting_Silentx04
                                show gensex_missionary_n_head_exp_eyebrows surprisex01
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sadbiting_Silentx03
                            with dissolve

                        ne "..."

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "front03"
                                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                                show gensex_oral_n_frontHead_exp_eyebrows sadx03
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front03"
                                show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                                show gensex_missionary_n_head_exp_eyebrows sadx03
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Talkingx04
                            with dissolve

                        ne "Si me obligas a ello,"

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "front04"
                                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx03
                                show gensex_oral_n_frontHead_exp_eyebrows serious
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front04"
                                show gensex_missionary_n_head_exp_mouth sad_Talkingx03
                                show gensex_missionary_n_head_exp_eyebrows serious
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Talkingx02
                            with dissolve

                        ne "s??."

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "front04"
                                show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx08
                                show gensex_oral_n_frontHead_exp_eyebrows sadx04
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front04"
                                show gensex_missionary_n_head_exp_mouth sadbiting_Silentx08
                                show gensex_missionary_n_head_exp_eyebrows sadx04
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sadbiting_Silentx06
                            with dissolve

                        menu:

                            "Lo dices como si no fueras a disfrutarlo.":
                                call p_Help

                                if p_prot.pos in ["oral", "missionary", "69"]:
                                    if p_prot.pos == "oral":
                                        $ nteye = "front01"
                                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                                        show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                                        call gensex_oral_n_frontHead_exp_tears_tears
                                    elif p_prot.pos == "missionary":
                                        $ nteye = "front01"
                                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                                        show gensex_missionary_n_head_exp_eyebrows surprisex01
                                        call gensex_oral_n_frontHead_exp_tears_tears
                                    elif p_prot.pos == "69":
                                        show gensex_69_L_d_mouth sadbiting_Silentx04
                                    with dissolve

                                ne "..."

                                if p_prot.pos in ["oral", "missionary", "69"]:
                                    if p_prot.pos == "oral":
                                        $ nteye = "right02"
                                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx003
                                        show gensex_oral_n_frontHead_exp_eyebrows suspiciousx02
                                        call gensex_oral_n_frontHead_exp_tears_tears
                                    elif p_prot.pos == "missionary":
                                        $ nteye = "right02"
                                        show gensex_missionary_n_head_exp_mouth sad_Talkingx003
                                        show gensex_missionary_n_head_exp_eyebrows suspiciousx02
                                        call gensex_oral_n_frontHead_exp_tears_tears
                                    elif p_prot.pos == "69":
                                        show gensex_69_L_d_mouth sad_Talkingx002
                                    with dissolve

                                ne "Euhh..."

                                if p_prot.pos in ["oral", "missionary", "69"]:
                                    if p_prot.pos == "oral":
                                        $ nteye = "right04"
                                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                                        show gensex_oral_n_frontHead_exp_eyebrows sadx03
                                        call gensex_oral_n_frontHead_exp_tears_tears
                                    elif p_prot.pos == "missionary":
                                        $ nteye = "right04"
                                        show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                                        show gensex_missionary_n_head_exp_eyebrows sadx03
                                        call gensex_oral_n_frontHead_exp_tears_tears
                                    elif p_prot.pos == "69":
                                        show gensex_69_L_d_mouth sad_Talkingx05
                                    with dissolve

                                ne "Eso no tiene nada que ver."

                                if p_prot.pos in ["oral", "missionary", "69"]:
                                    if p_prot.pos == "oral":
                                        $ nteye = "front02"
                                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx04
                                        show gensex_oral_n_frontHead_exp_eyebrows suspiciousx02
                                        call gensex_oral_n_frontHead_exp_tears_tears
                                    elif p_prot.pos == "missionary":
                                        $ nteye = "front02"
                                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx04
                                        show gensex_missionary_n_head_exp_eyebrows suspiciousx02
                                        call gensex_oral_n_frontHead_exp_tears_tears
                                    elif p_prot.pos == "69":
                                        show gensex_69_L_d_mouth sadbiting_Silentx03
                                    with dissolve

                                p "No lo niegas."

                                if gensex_YoureAMonster:

                                    $pl.ch_pts("np",-4)

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front03"
                                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx07
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx02
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front03"
                                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx07
                                            show gensex_missionary_n_head_exp_eyebrows sadx02
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sadbiting_Silentx06
                                        with dissolve

                                    p "En el fondo es lo que eres."

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front04"
                                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx10
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx05
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front04"
                                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx10
                                            show gensex_missionary_n_head_exp_eyebrows sadx05
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sadbiting_Silentx07
                                        with dissolve

                                    p "Por mucho que intentes enga??arte a ti misma."

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front06"
                                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx15
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front06"
                                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx15
                                            show gensex_missionary_n_head_exp_eyebrows sadx08
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sadbiting_Silentx08
                                        with dissolve

                                    ne "..."

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front04"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx03
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front04"
                                            show gensex_missionary_n_head_exp_mouth sad_Talkingx03
                                            show gensex_missionary_n_head_exp_eyebrows sadx06
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Talkingx02
                                        with dissolve

                                    ne "[protname]..."

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front04"
                                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx08
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front04"
                                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx08
                                            show gensex_missionary_n_head_exp_eyebrows sadx08
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sadbiting_Silentx06
                                        with dissolve

                                    ne "..."

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "right05"
                                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx09
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx10
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "right05"
                                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx09
                                            show gensex_missionary_n_head_exp_eyebrows sadx10
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sadbiting_Silentx07
                                        with dissolve

                                else:

                                    $pl.ch_pts("np",1)

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front05"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx005
                                            show gensex_oral_n_frontHead_exp_eyebrows angryx02
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front05"
                                            show gensex_missionary_n_head_exp_mouth sad_Talkingx005
                                            show gensex_missionary_n_head_exp_eyebrows angryx02
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Talkingx004
                                        with dissolve

                                    ne "Idiota..."

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front06"
                                            show gensex_oral_n_frontHead_exp_mouth happy_Silentx06
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx04
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front06"
                                            show gensex_missionary_n_head_exp_mouth happy_Silentx06
                                            show gensex_missionary_n_head_exp_eyebrows sadx04
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth happy_Silentx05
                                        with dissolve

                            "Yo no te obligo a nada.":
                                call p_Help
                                $pl.ch_pts("np",-2)

                                if p_prot.pos in ["oral", "missionary", "69"]:
                                    if p_prot.pos == "oral":
                                        $ nteye = "front03"
                                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx12
                                        show gensex_oral_n_frontHead_exp_eyebrows angryx05
                                        call gensex_oral_n_frontHead_exp_tears_tears
                                    elif p_prot.pos == "missionary":
                                        $ nteye = "front03"
                                        show gensex_missionary_n_head_exp_mouth sad_Talkingx12
                                        show gensex_missionary_n_head_exp_eyebrows angryx05
                                        call gensex_oral_n_frontHead_exp_tears_tears
                                    elif p_prot.pos == "69":
                                        show gensex_69_L_d_mouth sad_Talkingx08
                                    with dissolve

                                ne "Tu falta de acci??n me obligar??."

                                if p_prot.pos in ["oral", "missionary", "69"]:
                                    if p_prot.pos == "oral":
                                        $ nteye = "right05"
                                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                                        show gensex_oral_n_frontHead_exp_eyebrows sadx04
                                        call gensex_oral_n_frontHead_exp_tears_tears
                                    elif p_prot.pos == "missionary":
                                        $ nteye = "right05"
                                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                                        show gensex_missionary_n_head_exp_eyebrows sadx04
                                        call gensex_oral_n_frontHead_exp_tears_tears
                                    elif p_prot.pos == "69":
                                        show gensex_69_L_d_mouth sadbiting_Silentx05
                                    with dissolve

                    "??Qu?? har??s?":
                        call p_Help
                        #$pl.ch_pts("np",5)

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "front04"
                                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                                show gensex_oral_n_frontHead_exp_eyebrows sadx04
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front04"
                                show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                                show gensex_missionary_n_head_exp_eyebrows sadx04
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Talkingx05
                            with dissolve

                        ne "Ya sabes lo que tendr?? que hacer."

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "front02"
                                show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx01
                                show gensex_oral_n_frontHead_exp_eyebrows sadx01
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front02"
                                show gensex_missionary_n_head_exp_mouth sadbiting_Silentx01
                                show gensex_missionary_n_head_exp_eyebrows sadx01
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sadbiting_Silentx01
                            with dissolve

                        p "Lo dices como si no lo fueras a disfrutar."

                        if p_prot.pos in ["oral", "missionary", "69"]:
                            if p_prot.pos == "oral":
                                $ nteye = "front04"
                                show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx08
                                show gensex_oral_n_frontHead_exp_eyebrows sadx06
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "missionary":
                                $ nteye = "front04"
                                show gensex_missionary_n_head_exp_mouth sadbiting_Silentx08
                                show gensex_missionary_n_head_exp_eyebrows sadx06
                                call gensex_oral_n_frontHead_exp_tears_tears
                            elif p_prot.pos == "69":
                                show gensex_69_L_d_mouth sadbiting_Silentx06
                            with dissolve

                        ne "..."

                        if gensex_YoureAMonster:

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front02"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx04
                                    show gensex_oral_n_frontHead_exp_eyebrows suspiciousx01
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front02"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx04
                                    show gensex_missionary_n_head_exp_eyebrows suspiciousx01
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx03
                                with dissolve

                            p "En el fondo eres lo que eres."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front01"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx16
                                    show gensex_oral_n_frontHead_exp_eyebrows angryx05
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front01"
                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx16
                                    show gensex_missionary_n_head_exp_eyebrows angryx05
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Talkingx09
                                with dissolve

                            ne "??No es eso!"

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front04"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx13
                                    show gensex_oral_n_frontHead_exp_eyebrows angryx04
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front04"
                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx13
                                    show gensex_missionary_n_head_exp_eyebrows angryx04
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Talkingx07
                                with dissolve

                            ne "??Eres t?? quien...!"

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front08"
                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx12
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx08
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front08"
                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx12
                                    show gensex_missionary_n_head_exp_eyebrows sadx08
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sadbiting_Silentx06
                                with dissolve

                            menu:

                                pt "??Soy yo quien... qu???"

                                "??Eso es lo que le dir??as a una mujer que no quiere follar contigo?":
                                    call p_Help
                                    $pl.ch_pts("np",-3)

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front01"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx06
                                            show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front01"
                                            show gensex_missionary_n_head_exp_mouth sad_Silentx06
                                            show gensex_missionary_n_head_exp_eyebrows surprisex02
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Silentx05
                                        with dissolve

                                    p "??Que la violas por su culpa,"

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front00"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx09
                                            show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front00"
                                            show gensex_missionary_n_head_exp_mouth sad_Silentx09
                                            show gensex_missionary_n_head_exp_eyebrows surprisex02
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Silentx07
                                        with dissolve

                                    p "porque no quiere follar?"

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front03"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx09
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front03"
                                            show gensex_missionary_n_head_exp_mouth sad_Silentx09
                                            show gensex_missionary_n_head_exp_eyebrows sadx06
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Silentx06
                                        with dissolve

                                    ne "..."

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front08"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front08"
                                            show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                                            show gensex_missionary_n_head_exp_eyebrows sadx08
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Talkingx04
                                        with dissolve

                                    ne "[protname]..."

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front06"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx006
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx09
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front06"
                                            show gensex_missionary_n_head_exp_mouth sad_Talkingx006
                                            show gensex_missionary_n_head_exp_eyebrows sadx08
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Talkingx005
                                        with dissolve

                                    ne "No es lo mismo,"

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front02"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx10
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx07
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front02"
                                            show gensex_missionary_n_head_exp_mouth sad_Talkingx10
                                            show gensex_missionary_n_head_exp_eyebrows sadx07
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Talkingx08
                                        with dissolve

                                    ne "y lo sabes."

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front03"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx08
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx09
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front03"
                                            show gensex_missionary_n_head_exp_mouth sad_Talkingx08
                                            show gensex_missionary_n_head_exp_eyebrows sadx08
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Talkingx06
                                        with dissolve

                                    ne "No te haces una idea de c??mo es Padre..."

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front05"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx05
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front05"
                                            show gensex_missionary_n_head_exp_mouth sad_Silentx05
                                            show gensex_missionary_n_head_exp_eyebrows sadx08
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Silentx04
                                        with dissolve

                                    p "No,"

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front03"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx04
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx01
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front03"
                                            show gensex_missionary_n_head_exp_mouth sad_Silentx04
                                            show gensex_missionary_n_head_exp_eyebrows sadx01
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Silentx03
                                        with dissolve

                                    p "a ??l quiz??s no lo conozco tan bien,"

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front05"
                                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx11
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front05"
                                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx11
                                            show gensex_missionary_n_head_exp_eyebrows sadx08
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sadbiting_Silentx08
                                        with dissolve

                                    p "pero a ti empiezo a entenderte."

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front08"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx16
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx10
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front08"
                                            show gensex_missionary_n_head_exp_mouth sad_Silentx16
                                            show gensex_missionary_n_head_exp_eyebrows sadx10
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Silentx06
                                        with dissolve

                                    ne "..."

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front04"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx12
                                            show gensex_oral_n_frontHead_exp_eyebrows angryx06
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front04"
                                            show gensex_missionary_n_head_exp_mouth sad_Talkingx12
                                            show gensex_missionary_n_head_exp_eyebrows angryx06
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Talkingx09
                                        with dissolve

                                    ne "??Realmente me ves como ??l?"

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front05"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx10
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front05"
                                            show gensex_missionary_n_head_exp_mouth sad_Silentx10
                                            show gensex_missionary_n_head_exp_eyebrows sadx08
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Silentx04
                                        with dissolve

                                    menu:

                                        pt "Como ??l..."

                                        "De tal palo, tal astilla.":
                                            call p_Help
                                            $pl.ch_pts("np",-5)

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front00"
                                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx06
                                                    show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front00"
                                                    show gensex_missionary_n_head_exp_mouth sad_Silentx06
                                                    show gensex_missionary_n_head_exp_eyebrows surprisex01
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sad_Silentx05
                                                with dissolve

                                            ne "..."

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front04"
                                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx09
                                                    show gensex_oral_n_frontHead_exp_eyebrows angryx05
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front04"
                                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx09
                                                    show gensex_missionary_n_head_exp_eyebrows angryx05
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sad_Talkingx07
                                                with dissolve

                                            ne "Tambi??n es tu padre,"

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front02"
                                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx21
                                                    show gensex_oral_n_frontHead_exp_eyebrows angryx06
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front02"
                                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx21
                                                    show gensex_missionary_n_head_exp_eyebrows angryx06
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sad_Talkingx12
                                                with dissolve

                                            ne "??y no por ello has asesinado a nadie!"

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front01"
                                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx08
                                                    show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front01"
                                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx08
                                                    show gensex_missionary_n_head_exp_eyebrows surprisex01
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sadbiting_Silentx06
                                                with dissolve

                                            p "Eso demuestra que soy mejor persona que t??."

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front03"
                                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx08
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx08
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front03"
                                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx08
                                                    show gensex_missionary_n_head_exp_eyebrows sadx08
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sad_Talkingx06
                                                with dissolve

                                            ne "No sabes por lo que he pasado..."

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front02"
                                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx11
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx01
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front02"
                                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx11
                                                    show gensex_missionary_n_head_exp_eyebrows sadx01
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sadbiting_Silentx08
                                                with dissolve

                                            p "??Y eso justifica que mataras a ese ni??o?"

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front05"
                                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx14
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx10
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front05"
                                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx14
                                                    show gensex_missionary_n_head_exp_eyebrows sadx10
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sadbiting_Silentx09
                                                with dissolve

                                            ne "..."

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front08"
                                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx003
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx08
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front08"
                                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx003
                                                    show gensex_missionary_n_head_exp_eyebrows sadx08
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sad_Talkingx002
                                                with dissolve

                                            ne "No..."

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "right03"
                                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx03
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx07
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "right03"
                                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx03
                                                    show gensex_missionary_n_head_exp_eyebrows sadx07
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sad_Talkingx02
                                                with dissolve

                                            ne "Supongo que no..."

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "right00"
                                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx04
                                                    show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "right00"
                                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx04
                                                    show gensex_missionary_n_head_exp_eyebrows surprisex02
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sadbiting_Silentx03
                                                with dissolve

                                            p "????Supones?!"

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front03"
                                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx10
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx08
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front03"
                                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx10
                                                    show gensex_missionary_n_head_exp_eyebrows sadx08
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sadbiting_Silentx08
                                                with dissolve

                                            ne "..."

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front06"
                                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx006
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx09
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front06"
                                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx006
                                                    show gensex_missionary_n_head_exp_eyebrows sadx08
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sad_Talkingx005
                                                with dissolve

                                            ne "Lo siento..."

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front02"
                                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx06
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx07
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front02"
                                                    show gensex_missionary_n_head_exp_mouth sad_Silentx06
                                                    show gensex_missionary_n_head_exp_eyebrows sadx07
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sad_Silentx05
                                                with dissolve

                                            p "Eso d??selo a sus padres."

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "right05"
                                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx10
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx10
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "right05"
                                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx10
                                                    show gensex_missionary_n_head_exp_eyebrows sadx10
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sadbiting_Silentx07
                                                with dissolve

                                        "Quiz??s ??l sea peor, pero desde luego, tampoco te veo muy arrepentida de tus actos.":
                                            call p_Help
                                            $pl.ch_pts("np",-3)

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front01"
                                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx02
                                                    show gensex_oral_n_frontHead_exp_eyebrows serious
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front01"
                                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx02
                                                    show gensex_missionary_n_head_exp_eyebrows serious
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sadbiting_Silentx01
                                                with dissolve

                                            ne "..."

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front02"
                                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx02
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx03
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front02"
                                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx02
                                                    show gensex_missionary_n_head_exp_eyebrows sadx03
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sadbiting_Silentx01
                                                with dissolve

                                            p "Simplemente ten??as que ped??rmelo,"

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front00"
                                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx01
                                                    show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front00"
                                                    show gensex_missionary_n_head_exp_mouth sad_Silentx01
                                                    show gensex_missionary_n_head_exp_eyebrows surprisex01
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sad_Silentx01
                                                with dissolve

                                            p "no asesinar a un ni??o y convertir a D??dac en mujer,"

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front02"
                                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx09
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx03
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front02"
                                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx09
                                                    show gensex_missionary_n_head_exp_eyebrows sadx03
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sadbiting_Silentx06
                                                with dissolve

                                            p "acus??ndolo de haberte violado,"

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "right04"
                                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx14
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "right04"
                                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx14
                                                    show gensex_missionary_n_head_exp_eyebrows sadx05
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sadbiting_Silentx08
                                                with dissolve

                                            p "para luego hacerme chantaje con ??l."

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "right05"
                                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx003
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx07
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "right05"
                                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx003
                                                    show gensex_missionary_n_head_exp_eyebrows sadx07
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sad_Talkingx002
                                                with dissolve

                                            ne "Lo-"

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front06"
                                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx006
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx08
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front06"
                                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx006
                                                    show gensex_missionary_n_head_exp_eyebrows sadx08
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sad_Talkingx004
                                                with dissolve

                                            ne "lo siento..."

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front03"
                                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx10
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front03"
                                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx10
                                                    show gensex_missionary_n_head_exp_eyebrows sadx05
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sadbiting_Silentx08
                                                with dissolve

                                            p "Eso d??selo a los padres del ni??o que has matado."

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "right05"
                                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx15
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx09
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "right05"
                                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx15
                                                    show gensex_missionary_n_head_exp_eyebrows sadx08
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sadbiting_Silentx09
                                                with dissolve

                                        "Que finjas arrepentimiento, no te exculpa de todos los cr??menes que has cometido.":
                                            call p_Help
                                            $pl.ch_pts("np",-8)

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front03"
                                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx09
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx07
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front03"
                                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx09
                                                    show gensex_missionary_n_head_exp_eyebrows sadx07
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sad_Talkingx07
                                                with dissolve

                                            ne "No lo estoy fingiendo..."

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front02"
                                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx06
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx04
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front02"
                                                    show gensex_missionary_n_head_exp_mouth sad_Silentx06
                                                    show gensex_missionary_n_head_exp_eyebrows sadx04
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sad_Silentx04
                                                with dissolve

                                            p "Lo que t?? digas."

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front04"
                                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx03
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx08
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front04"
                                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx03
                                                    show gensex_missionary_n_head_exp_eyebrows sadx08
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sad_Talkingx02
                                                with dissolve

                                            ne "Te lo prometo..."

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "front01"
                                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx10
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx03
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "front01"
                                                    show gensex_missionary_n_head_exp_mouth sad_Silentx10
                                                    show gensex_missionary_n_head_exp_eyebrows sadx03
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sad_Silentx04
                                                with dissolve

                                            p "Eso d??selo a los padres del ni??o al que has matado."

                                            if p_prot.pos in ["oral", "missionary", "69"]:
                                                if p_prot.pos == "oral":
                                                    $ nteye = "right05"
                                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx12
                                                    show gensex_oral_n_frontHead_exp_eyebrows sadx09
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "missionary":
                                                    $ nteye = "right05"
                                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx12
                                                    show gensex_missionary_n_head_exp_eyebrows sadx08
                                                    call gensex_oral_n_frontHead_exp_tears_tears
                                                elif p_prot.pos == "69":
                                                    show gensex_69_L_d_mouth sadbiting_Silentx08
                                                with dissolve

                                    #ne "..."

                                "...":
                                    call p_Help

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "right05"
                                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx12
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx09
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "right05"
                                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx12
                                            show gensex_missionary_n_head_exp_eyebrows sadx08
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sadbiting_Silentx09
                                        with dissolve


                        else:

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front08"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front08"
                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                                    show gensex_missionary_n_head_exp_eyebrows sadx05
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Talkingx002
                                with dissolve

                            ne "Prefiero no responder a eso."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "right05"
                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx09
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx08
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "right05"
                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx09
                                    show gensex_missionary_n_head_exp_eyebrows sadx08
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sadbiting_Silentx06
                                with dissolve

                    "...":
                        call p_Help


            elif ped_check_list_result == 2:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front03"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx006
                        show gensex_oral_n_frontHead_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front03"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx006
                        show gensex_missionary_n_head_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx005
                    with dissolve

                ne "[protname],"

                extend " por favor..."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front04"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx07
                        show gensex_oral_n_frontHead_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front04"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx07
                        show gensex_missionary_n_head_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx06
                    with dissolve

                ne "haz algo,"

                extend " o tendr?? que hacerlo por ti."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front01"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                        show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front01"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                        show gensex_missionary_n_head_exp_eyebrows surprisex01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx05
                    with dissolve

                p "Lo est??s deseando,"

                extend " ??Verdad?"

                if gensex_YoureAMonster or gensex_INotLoveYouNeus:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front01"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx005
                            show gensex_oral_n_frontHead_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front01"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx005
                            show gensex_missionary_n_head_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx004
                        with dissolve

                    ne "No seas as??..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front08"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front08"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                            show gensex_missionary_n_head_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx05
                        with dissolve

                else:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front08"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx08
                            show gensex_oral_n_frontHead_exp_eyebrows sadx04
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front08"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx08
                            show gensex_missionary_n_head_exp_eyebrows sadx04
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx06
                        with dissolve

                    ne "..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "right02"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right02"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                            show gensex_missionary_n_head_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx003
                        with dissolve

                    ne "Me da miedo que no te vaya a gustar esa parte de mi..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front01"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx04
                            show gensex_oral_n_frontHead_exp_eyebrows sadx01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front01"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx04
                            show gensex_missionary_n_head_exp_eyebrows sadx01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx03
                        with dissolve

                    p "??Es que tienes doble personalidad?"

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front04"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx05
                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front04"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx05
                            show gensex_missionary_n_head_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx04
                        with dissolve

                    ne "..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front08"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx006
                            show gensex_oral_n_frontHead_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front08"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx006
                            show gensex_missionary_n_head_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx005
                        with dissolve

                    ne "Digamos que pierdo bastante la raz??n cuando me caliento demasiado."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front05"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx04
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front05"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                            show gensex_missionary_n_head_exp_eyebrows sadx04
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx05
                        with dissolve

                    p "No parece tan peligroso."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front08"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx07
                            show gensex_oral_n_frontHead_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front08"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx07
                            show gensex_missionary_n_head_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx06
                        with dissolve

                    ne "A veces he acabado matando a la otra persona sin darme cuenta cuando estoy en ese estado."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "right05"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx12
                            show gensex_oral_n_frontHead_exp_eyebrows sadx09
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right05"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx12
                            show gensex_missionary_n_head_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx08
                        with dissolve

                    pt "Vale,"

                    extend " quiz??s s?? suena un poco peligroso..."


            elif ped_check_list_result == 3:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front01"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx08
                        show gensex_oral_n_frontHead_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front01"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx08
                        show gensex_missionary_n_head_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx06
                    with dissolve

                ne "Si no haces nada,"

                extend " al final tendr?? que hacerlo yo."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front04"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx12
                        show gensex_oral_n_frontHead_exp_eyebrows angryx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front04"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx12
                        show gensex_missionary_n_head_exp_eyebrows angryx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx08
                    with dissolve

                ne "No tenemos toda la noche."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front05"
                        show gensex_oral_n_frontHead_exp_mouth sad_Silentx12
                        show gensex_oral_n_frontHead_exp_eyebrows angryx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front05"
                        show gensex_missionary_n_head_exp_mouth sad_Silentx12
                        show gensex_missionary_n_head_exp_eyebrows angryx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Silentx05
                    with dissolve

            elif ped_check_list_result == 4:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front01"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx10
                        show gensex_oral_n_frontHead_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front01"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx10
                        show gensex_missionary_n_head_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx06
                    with dissolve

                ne "Ahora en serio [protname]."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx12
                        show gensex_oral_n_frontHead_exp_eyebrows angryx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx12
                        show gensex_missionary_n_head_exp_eyebrows angryx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx07
                    with dissolve

                ne "Si sigues sin hacer nada,"

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front03"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx14
                        show gensex_oral_n_frontHead_exp_eyebrows angryx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front03"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx14
                        show gensex_missionary_n_head_exp_eyebrows angryx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx08
                    with dissolve

                ne "voy a tener que tomar medidas dr??sticas."

                if gensex_YoureAMonster:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front00"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front00"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx03
                            show gensex_missionary_n_head_exp_eyebrows surprisex02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx02
                        with dissolve

                    p "??Vas a matarme?"

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front01"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
                            show gensex_oral_n_frontHead_exp_eyebrows suspiciousx02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front01"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx04
                            show gensex_missionary_n_head_exp_eyebrows suspiciousx02
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx03
                        with dissolve

                    ne "????Qu???!"

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front02"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx005
                            show gensex_oral_n_frontHead_exp_eyebrows angryx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front02"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx005
                            show gensex_missionary_n_head_exp_eyebrows angryx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx004
                        with dissolve

                    ne "??No!"

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front01"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx03
                            show gensex_oral_n_frontHead_exp_eyebrows sadx01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front01"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx03
                            show gensex_missionary_n_head_exp_eyebrows sadx01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx02
                        with dissolve

                    menu:

                        "??Por qu?? perder??as tu fuente de alimento?":
                            call p_Help
                            $pl.ch_pts("np",-3)

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front00"
                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx02
                                    show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front00"
                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx02
                                    show gensex_missionary_n_head_exp_eyebrows surprisex02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sadbiting_Silentx01
                                with dissolve

                            ne "..."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front01"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx05
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx01
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front01"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx05
                                    show gensex_missionary_n_head_exp_eyebrows sadx01
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx04
                                with dissolve

                            p "Lo m??s probable es que me conviertas en piedra"

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front02"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx12
                                    show gensex_oral_n_frontHead_exp_eyebrows angryx02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front02"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx12
                                    show gensex_missionary_n_head_exp_eyebrows angryx02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx05
                                with dissolve

                            p "y me mantengas vivo como si fuera una planta a la que le va sacando el fruto,"

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front08"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx16
                                    show gensex_oral_n_frontHead_exp_eyebrows angryx05
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front08"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx16
                                    show gensex_missionary_n_head_exp_eyebrows angryx05
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx05
                                with dissolve

                            p "??no es as???"

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front01"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx006
                                    show gensex_oral_n_frontHead_exp_eyebrows angryx06
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front01"
                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx006
                                    show gensex_missionary_n_head_exp_eyebrows angryx06
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Talkingx005
                                with dissolve

                            ne "??No!"

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front02"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx12
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front02"
                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx12
                                    show gensex_missionary_n_head_exp_eyebrows sadx02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Talkingx08
                                with dissolve

                            ne "??Nunca te har??a algo as??!"

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front01"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                                    show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front01"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx03
                                    show gensex_missionary_n_head_exp_eyebrows surprisex02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx02
                                with dissolve

                            p "Es lo que dijo Padre."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "right04"
                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "right04"
                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                                    show gensex_missionary_n_head_exp_eyebrows sadx05
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sadbiting_Silentx04
                                with dissolve

                            ne "..."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front08"
                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx08
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx06
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front08"
                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx08
                                    show gensex_missionary_n_head_exp_eyebrows sadx06
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sadbiting_Silentx06
                                with dissolve

                            p "Probablemente es lo que estabas planeando si hubiera resultado ser como ??l,"

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front05"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx08
                                    show gensex_oral_n_frontHead_exp_eyebrows angryx05
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front05"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx08
                                    show gensex_missionary_n_head_exp_eyebrows angryx05
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx07
                                with dissolve

                            p "??me equivoco?"

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front01"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx17
                                    show gensex_oral_n_frontHead_exp_eyebrows angryx06
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front01"
                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx17
                                    show gensex_missionary_n_head_exp_eyebrows angryx06
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Talkingx08
                                with dissolve

                            ne "??Por supuesto que te equivocas!"

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front00"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx05
                                    show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front00"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx05
                                    show gensex_missionary_n_head_exp_eyebrows surprisex02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx04
                                with dissolve

                            p "??Y por qu?? deber??a creerte?"

                            $ ntlong += 1

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front03"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx18
                                    show gensex_oral_n_frontHead_exp_eyebrows angryx07
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front03"
                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx18
                                    show gensex_missionary_n_head_exp_eyebrows angryx07
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Talkingx09
                                with dissolve

                            ne "??Por que no soy como ??l!"

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front01"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx05
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx01
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front01"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx05
                                    show gensex_missionary_n_head_exp_eyebrows sadx01
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx04
                                with dissolve

                            p "Eso es lo que te gustan pensar,"

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front04"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx10
                                    show gensex_oral_n_frontHead_exp_eyebrows angryx06
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front04"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx10
                                    show gensex_missionary_n_head_exp_eyebrows angryx06
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx04
                                with dissolve

                            p "??verdad?"

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front08"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx009
                                    show gensex_oral_n_frontHead_exp_eyebrows angryx06
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front08"
                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx009
                                    show gensex_missionary_n_head_exp_eyebrows angryx06
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Talkingx007
                                with dissolve

                            ne "Preferir??a estar muerta antes que eso."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "down01"
                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                                    show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "down01"
                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                                    show gensex_missionary_n_head_exp_eyebrows surprisex02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sadbiting_Silentx04
                                with dissolve

                            p "Tampoco es que el suicidio sea una opci??n tan f??cil para ti,"

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front01"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx05
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx01
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front01"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx05
                                    show gensex_missionary_n_head_exp_eyebrows sadx01
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx04
                                with dissolve

                            p "por lo que he entendido."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front04"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx05
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx05
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front04"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx05
                                    show gensex_missionary_n_head_exp_eyebrows sadx05
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx04
                                with dissolve

                            ne "..."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front04"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx03
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx07
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front04"
                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx03
                                    show gensex_missionary_n_head_exp_eyebrows sadx07
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Talkingx02
                                with dissolve

                            ne "??Por qu?? eres as?? [protname]?"

                            $ ntlong += 1

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front05"
                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx09
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front05"
                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                                    show gensex_missionary_n_head_exp_eyebrows sadx08
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sadbiting_Silentx04
                                with dissolve

                            menu:

                                pt "??Por qu???..."

                                "Porque me das asco.":
                                    call p_Help
                                    $pl.ch_pts("np",-8)

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front00"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx05
                                            show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front00"
                                            show gensex_missionary_n_head_exp_mouth sad_Silentx05
                                            show gensex_missionary_n_head_exp_eyebrows surprisex02
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Silentx04
                                        with dissolve

                                "Porque me has mentido.":
                                    call p_Help
                                    $pl.ch_pts("np",-3)

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front02"
                                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx03
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front02"
                                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                                            show gensex_missionary_n_head_exp_eyebrows sadx03
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sadbiting_Silentx05
                                        with dissolve

                                "Porque has matado a un ni??o inocente.":
                                    call p_Help
                                    $pl.ch_pts("np",-2)

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front01"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx06
                                            show gensex_oral_n_frontHead_exp_eyebrows surprisex02
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front01"
                                            show gensex_missionary_n_head_exp_mouth sad_Silentx06
                                            show gensex_missionary_n_head_exp_eyebrows surprisex02
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Silentx05
                                        with dissolve

                                "Porque no puedo perdonarte.":
                                    call p_Help
                                    $pl.ch_pts("np",-3)

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front02"
                                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx06
                                            show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front02"
                                            show gensex_missionary_n_head_exp_mouth sad_Silentx06
                                            show gensex_missionary_n_head_exp_eyebrows surprisex01
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sad_Silentx05
                                        with dissolve

                                "Porque te lo mereces.":
                                    call p_Help
                                    $pl.ch_pts("np",-5)

                                    if p_prot.pos in ["oral", "missionary", "69"]:
                                        if p_prot.pos == "oral":
                                            $ nteye = "front01"
                                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx07
                                            show gensex_oral_n_frontHead_exp_eyebrows sadx01
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "missionary":
                                            $ nteye = "front01"
                                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx07
                                            show gensex_missionary_n_head_exp_eyebrows sadx01
                                            call gensex_oral_n_frontHead_exp_tears_tears
                                        elif p_prot.pos == "69":
                                            show gensex_69_L_d_mouth sadbiting_Silentx06
                                        with dissolve

                            ne "..."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "right05"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx09
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx09
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "right05"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx09
                                    show gensex_missionary_n_head_exp_eyebrows sadx08
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx07
                                with dissolve

                        "...":
                            call p_Help
                            $pl.ch_pts("np",-1)

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front04"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx06
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx08
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front04"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx06
                                    show gensex_missionary_n_head_exp_eyebrows sadx08
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx05
                                with dissolve

                else:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front04"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                            show gensex_oral_n_frontHead_exp_eyebrows angryx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front04"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                            show gensex_missionary_n_head_exp_eyebrows angryx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx04
                        with dissolve

            elif ped_check_list_result == 5:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front03"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx005
                        show gensex_oral_n_frontHead_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front03"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx005
                        show gensex_missionary_n_head_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx004
                    with dissolve

                ne "Al final har?? algo que no te va a gustar."

                if gensex_YoureAMonster == True:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front01"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front01"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                            show gensex_missionary_n_head_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx05
                        with dissolve

                    p "Viniendo de ti tampoco me sorprende."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front04"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                            show gensex_oral_n_frontHead_exp_eyebrows sadx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front04"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                            show gensex_missionary_n_head_exp_eyebrows sadx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx04
                        with dissolve

                    ne "..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front08"
                            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx02
                            show gensex_oral_n_frontHead_exp_eyebrows sadx07
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front08"
                            show gensex_missionary_n_head_exp_mouth sad_Talkingx02
                            show gensex_missionary_n_head_exp_eyebrows sadx07
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx01
                        with dissolve

                    ne "??Por qu?? eres as???"

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front03"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx08
                            show gensex_oral_n_frontHead_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front03"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx08
                            show gensex_missionary_n_head_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx06
                        with dissolve

                    p "??Acaso me equivoco?"

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "right05"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx08
                            show gensex_oral_n_frontHead_exp_eyebrows sadx09
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right05"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx08
                            show gensex_missionary_n_head_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx07
                        with dissolve

                    ne "..."

                else:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front04"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                            show gensex_oral_n_frontHead_exp_eyebrows angryx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front04"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                            show gensex_missionary_n_head_exp_eyebrows angryx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx04
                        with dissolve

                    menu:

                        pt "??Algo que no me va a gustar?..."

                        "??Quien te dice que no me va a gustar?":
                            call p_Help
                            $pl.ch_pts("np",1)

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front03"
                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx03
                                    show gensex_oral_n_frontHead_exp_eyebrows suspiciousx03
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front03"
                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx03
                                    show gensex_missionary_n_head_exp_eyebrows suspiciousx03
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sadbiting_Silentx02
                                with dissolve

                            "..."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front08"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx005
                                    show gensex_oral_n_frontHead_exp_eyebrows angryx06
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front08"
                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx005
                                    show gensex_missionary_n_head_exp_eyebrows angryx06
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Talkingx004
                                with dissolve

                            "No sabes de lo que est??s hablando."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "right05"
                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                                    show gensex_oral_n_frontHead_exp_eyebrows sadx06
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "right05"
                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                                    show gensex_missionary_n_head_exp_eyebrows sadx06
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sadbiting_Silentx05
                                with dissolve

                        "Quiz??s te sorprenda...":
                            call p_Help
                            $pl.ch_pts("np",1)

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front01"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx04
                                    show gensex_oral_n_frontHead_exp_eyebrows suspiciousx01
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front01"
                                    show gensex_missionary_n_head_exp_mouth sad_Silentx04
                                    show gensex_missionary_n_head_exp_eyebrows suspiciousx01
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Silentx03
                                with dissolve

                            ne "..."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front03"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                                    show gensex_oral_n_frontHead_exp_eyebrows angryx03
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front03"
                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                                    show gensex_missionary_n_head_exp_eyebrows angryx03
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Talkingx05
                                with dissolve

                            ne "Cuando tengas una cola metida por el culo,"

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front04"
                                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx006
                                    show gensex_oral_n_frontHead_exp_eyebrows surprisex002
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front04"
                                    show gensex_missionary_n_head_exp_mouth sad_Talkingx006
                                    show gensex_missionary_n_head_exp_eyebrows surprisex002
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sad_Talkingx005
                                with dissolve

                            ne "no creo que opines igual..."

                            if p_prot.pos in ["oral", "missionary", "69"]:
                                if p_prot.pos == "oral":
                                    $ nteye = "front05"
                                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                                    show gensex_oral_n_frontHead_exp_eyebrows suspiciousx02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "missionary":
                                    $ nteye = "front05"
                                    show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                                    show gensex_missionary_n_head_exp_eyebrows suspiciousx02
                                    call gensex_oral_n_frontHead_exp_tears_tears
                                elif p_prot.pos == "69":
                                    show gensex_69_L_d_mouth sadbiting_Silentx05
                                with dissolve

                            p "..."

                        "...":
                            call p_Help

            elif ped_check_list_result == 6:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front01"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx10
                        show gensex_oral_n_frontHead_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front01"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx10
                        show gensex_missionary_n_head_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx06
                    with dissolve

                ne "??Te lo est??s tomando a broma,"

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx09
                        show gensex_oral_n_frontHead_exp_eyebrows sadx02
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx09
                        show gensex_missionary_n_head_exp_eyebrows sadx02
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx05
                    with dissolve

                ne "y yo te estoy hablando muy en serio, [protname]."

                if gensex_YoureAMonster:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front01"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx04
                            show gensex_oral_n_frontHead_exp_eyebrows sadx01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front01"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx04
                            show gensex_missionary_n_head_exp_eyebrows sadx01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx03
                        with dissolve

                    p "Lo que t?? digas."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front03"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx07
                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front03"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx07
                            show gensex_missionary_n_head_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx06
                        with dissolve

                    ne "..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "right05"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx09
                            show gensex_oral_n_frontHead_exp_eyebrows sadx10
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right05"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx09
                            show gensex_missionary_n_head_exp_eyebrows sadx10
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx08
                        with dissolve

                else:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front05"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                            show gensex_oral_n_frontHead_exp_eyebrows sadx04
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front05"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                            show gensex_missionary_n_head_exp_eyebrows sadx04
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx04
                        with dissolve

            elif ped_check_list_result == 7:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front01"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx10
                        show gensex_oral_n_frontHead_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front01"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx10
                        show gensex_missionary_n_head_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx06
                    with dissolve

                ne "??[protname]!"

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front04"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                        show gensex_oral_n_frontHead_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front04"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                        show gensex_missionary_n_head_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                ne "No me hagas repetirlo..."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front05"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx08
                        show gensex_oral_n_frontHead_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front05"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx08
                        show gensex_missionary_n_head_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx06
                    with dissolve

            elif ped_check_list_result == 8:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front01"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx10
                        show gensex_oral_n_frontHead_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front01"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx10
                        show gensex_missionary_n_head_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx05
                    with dissolve

                ne "????Acaso no lo entiendes?!"

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx12
                        show gensex_oral_n_frontHead_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx12
                        show gensex_missionary_n_head_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx007
                    with dissolve

                ne "Esto no es una broma, [protname]."

                if gensex_YoureAMonster:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front01"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx04
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front01"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx04
                            show gensex_missionary_n_head_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx03
                        with dissolve

                    p "Desde luego que nada de esto es una broma."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front04"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front04"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx06
                            show gensex_missionary_n_head_exp_eyebrows sadx05
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx05
                        with dissolve

                    ne "..."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "right04"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx05
                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right04"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx05
                            show gensex_missionary_n_head_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx04
                        with dissolve

                else:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front03"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx09
                            show gensex_oral_n_frontHead_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front03"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx09
                            show gensex_missionary_n_head_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx05
                        with dissolve

            elif ped_check_list_result == 9:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front04"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front04"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                        show gensex_missionary_n_head_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx05
                    with dissolve

                ne "??[protname]!"

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front03"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx09
                        show gensex_oral_n_frontHead_exp_eyebrows angryx03
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front03"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx09
                        show gensex_missionary_n_head_exp_eyebrows angryx03
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx07
                    with dissolve

                ne "Te he dicho que no tenemos toda la noche..."

                if gensex_INotLoveYouNeus or gensex_YoureAMonster:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front01"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front01"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx03
                            show gensex_missionary_n_head_exp_eyebrows surprisex01
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx02
                        with dissolve

                    p "??Matar??s alg??n otro ni??o?"

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front02"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx10
                            show gensex_oral_n_frontHead_exp_eyebrows sadx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front02"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx10
                            show gensex_missionary_n_head_exp_eyebrows sadx03
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx08
                        with dissolve

                    p "Aparentemente eso te soluciona los problemas."

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front04"
                            show gensex_oral_n_frontHead_exp_mouth sad_Silentx15
                            show gensex_oral_n_frontHead_exp_eyebrows angryx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front04"
                            show gensex_missionary_n_head_exp_mouth sad_Silentx15
                            show gensex_missionary_n_head_exp_eyebrows angryx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx04
                        with dissolve

                    ne "..."

                    $ ntlong += 1

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "right05"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx11
                            show gensex_oral_n_frontHead_exp_eyebrows sadx09
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "right05"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx11
                            show gensex_missionary_n_head_exp_eyebrows sadx08
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx08
                        with dissolve

                else:

                    if p_prot.pos in ["oral", "missionary", "69"]:
                        if p_prot.pos == "oral":
                            $ nteye = "front05"
                            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
                            show gensex_oral_n_frontHead_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "missionary":
                            $ nteye = "front05"
                            show gensex_missionary_n_head_exp_mouth sadbiting_Silentx06
                            show gensex_missionary_n_head_exp_eyebrows sadx06
                            call gensex_oral_n_frontHead_exp_tears_tears
                        elif p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx05
                        with dissolve

            elif ped_check_list_result == 10:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front04"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front04"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx06
                        show gensex_missionary_n_head_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                ne "Por favor,"

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx08
                        show gensex_oral_n_frontHead_exp_eyebrows sadx07
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx08
                        show gensex_missionary_n_head_exp_eyebrows sadx07
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx06
                    with dissolve

                ne "ya sabes que no tenemos toda la noche..."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front05"
                        show gensex_oral_n_frontHead_exp_mouth sad_Silentx06
                        show gensex_oral_n_frontHead_exp_eyebrows sadx09
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front05"
                        show gensex_missionary_n_head_exp_mouth sad_Silentx06
                        show gensex_missionary_n_head_exp_eyebrows sadx08
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Silentx05
                    with dissolve

            else:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx10
                        show gensex_oral_n_frontHead_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front02"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx10
                        show gensex_missionary_n_head_exp_eyebrows angryx04
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx05
                    with dissolve

                ne "??[protname]!"

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front03"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx07
                        show gensex_oral_n_frontHead_exp_eyebrows sadx08
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front03"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx07
                        show gensex_missionary_n_head_exp_eyebrows sadx08
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx06
                    with dissolve


        elif p_prot.restTurns >= 4:

            call afternight05_Pedrera_n_Neus_Warning_4Times

    return

label afternight05_Pedrera_n_Neus_Warning_4Times:

    # $ Pedrera_char_Cond = "NeusClose_show"
    # call Pedrera_char_lab

    if p_prot.restTurns == 4 or afternight05_Pedrera_n_Neus_Warning_tongue == 4:

        if p_prot.pos in ["oral", "missionary", "69"]:
            if p_prot.pos == "oral":
                $ nteye = "front02"
                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx07
                show gensex_oral_n_frontHead_exp_eyebrows angryx04
                call gensex_oral_n_frontHead_exp_tears_tears
            elif p_prot.pos == "missionary":
                $ nteye = "front02"
                show gensex_missionary_n_head_exp_mouth sad_Talkingx07
                show gensex_missionary_n_head_exp_eyebrows angryx04
                call gensex_oral_n_frontHead_exp_tears_tears
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx06
            with dissolve

        $ ped_check_1_10("ped_n_neus_warning_05_list")

        if ped_check_list_result == 1: 

            ne "Es mi ??ltimo aviso."

            if p_prot.pos in ["oral", "missionary", "69"]:
                if p_prot.pos == "oral":
                    $ nteye = "front04"
                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx07
                    show gensex_oral_n_frontHead_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front04"
                    show gensex_missionary_n_head_exp_mouth sad_Silentx07
                    show gensex_missionary_n_head_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Silentx06
                with dissolve

        elif ped_check_list_result == 2:

            ne "No te lo volver?? a repetir, [protname]."

            if p_prot.pos in ["oral", "missionary", "69"]:
                if p_prot.pos == "oral":
                    $ nteye = "front04"
                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx07
                    show gensex_oral_n_frontHead_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front04"
                    show gensex_missionary_n_head_exp_mouth sad_Silentx07
                    show gensex_missionary_n_head_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Silentx05
                with dissolve

        elif ped_check_list_result == 3:

            ne "[protname]."

            if p_prot.pos in ["oral", "missionary", "69"]:
                if p_prot.pos == "oral":
                    $ nteye = "front03"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx09
                    show gensex_oral_n_frontHead_exp_eyebrows angryx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front03"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx09
                    show gensex_missionary_n_head_exp_eyebrows angryx04
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx06
                with dissolve

            ne "Basta ya."

            if p_prot.pos in ["oral", "missionary", "69"]:
                if p_prot.pos == "oral":
                    $ nteye = "front04"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx10
                    show gensex_oral_n_frontHead_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front04"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx10
                    show gensex_missionary_n_head_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx07
                with dissolve

            ne "O tendr?? que tomar medidas dr??sticas."

            if gensex_YoureAMonster:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front01"
                        show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                        show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front01"
                        show gensex_missionary_n_head_exp_mouth sad_Silentx03
                        show gensex_missionary_n_head_exp_eyebrows surprisex01
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Silentx02
                    with dissolve

                if p_prot.pos == "oral":
                    $ nteye = "front01"
                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                    show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

                p "De eso no me cabe ninguna duda."

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front03"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx05
                        show gensex_oral_n_frontHead_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front03"
                        show gensex_missionary_n_head_exp_mouth sad_Talkingx05
                        show gensex_missionary_n_head_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                ne "[protname]..."

                $ ntlong += 1

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front08"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                        show gensex_oral_n_frontHead_exp_eyebrows sadx08
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front08"
                        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx05
                        show gensex_missionary_n_head_exp_eyebrows sadx08
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx04
                    with dissolve

            else:

                if p_prot.pos in ["oral", "missionary", "69"]:
                    if p_prot.pos == "oral":
                        $ nteye = "front05"
                        show gensex_oral_n_frontHead_exp_mouth sad_Silentx12
                        show gensex_oral_n_frontHead_exp_eyebrows angryx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "missionary":
                        $ nteye = "front05"
                        show gensex_missionary_n_head_exp_mouth sad_Silentx12
                        show gensex_missionary_n_head_exp_eyebrows angryx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                    elif p_prot.pos == "69":
                        show gensex_69_L_d_mouth sad_Silentx05
                    with dissolve

        elif ped_check_list_result == 4:

            ne "[protname],"

            extend " no te lo volver?? a repetir."

            if p_prot.pos in ["oral", "missionary", "69"]:
                if p_prot.pos == "oral":
                    $ nteye = "front04"
                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx07
                    show gensex_oral_n_frontHead_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front04"
                    show gensex_missionary_n_head_exp_mouth sad_Silentx07
                    show gensex_missionary_n_head_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Silentx06
                with dissolve

        elif ped_check_list_result == 5:

            ne "Esta es mi ??ltima advertencia."

            if p_prot.pos in ["oral", "missionary", "69"]:
                if p_prot.pos == "oral":
                    $ nteye = "front04"
                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx07
                    show gensex_oral_n_frontHead_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front04"
                    show gensex_missionary_n_head_exp_mouth sad_Silentx07
                    show gensex_missionary_n_head_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Silentx06
                with dissolve

        elif ped_check_list_result == 6:

            ne "Es mi ??ltima advertencia."

            if p_prot.pos in ["oral", "missionary", "69"]:
                if p_prot.pos == "oral":
                    $ nteye = "front04"
                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx07
                    show gensex_oral_n_frontHead_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front04"
                    show gensex_missionary_n_head_exp_mouth sad_Silentx07
                    show gensex_missionary_n_head_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Silentx06
                with dissolve

        elif ped_check_list_result == 7:

            ne "Se acab??."

            if p_prot.pos in ["oral", "missionary", "69"]:
                if p_prot.pos == "oral":
                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx18
                    show gensex_oral_n_frontHead_exp_eyebrows angryx07
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front02"
                    show gensex_missionary_n_head_exp_mouth sad_Talkingx18
                    show gensex_missionary_n_head_exp_eyebrows angryx07
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Talkingx05
                with dissolve

            ne "No volver?? a repet??rtelo."

            if p_prot.pos in ["oral", "missionary", "69"]:
                if p_prot.pos == "oral":
                    $ nteye = "front04"
                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx07
                    show gensex_oral_n_frontHead_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front04"
                    show gensex_missionary_n_head_exp_mouth sad_Silentx07
                    show gensex_missionary_n_head_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Silentx06
                with dissolve

        elif ped_check_list_result == 8:

            ne "Este es mi ultimatum, [protname]."

            if p_prot.pos in ["oral", "missionary", "69"]:
                if p_prot.pos == "oral":
                    $ nteye = "front05"
                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx07
                    show gensex_oral_n_frontHead_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front05"
                    show gensex_missionary_n_head_exp_mouth sad_Silentx07
                    show gensex_missionary_n_head_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Silentx06
                with dissolve

        elif ped_check_list_result == 9:

            ne "La pr??xima vez tomar?? cartas en el asunto."

            if p_prot.pos in ["oral", "missionary", "69"]:
                if p_prot.pos == "oral":
                    $ nteye = "front03"
                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx09
                    show gensex_oral_n_frontHead_exp_eyebrows angryx06
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front03"
                    show gensex_missionary_n_head_exp_mouth sad_Silentx09
                    show gensex_missionary_n_head_exp_eyebrows angryx06
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Silentx07
                with dissolve

        elif ped_check_list_result == 10:

            ne "Ya no te lo volver?? a repetir."

            if p_prot.pos in ["oral", "missionary", "69"]:
                if p_prot.pos == "oral":
                    $ nteye = "front03"
                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx06
                    show gensex_oral_n_frontHead_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front03"
                    show gensex_missionary_n_head_exp_mouth sad_Silentx06
                    show gensex_missionary_n_head_exp_eyebrows angryx05
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Silentx05
                with dissolve

        else:

            ne "No te lo volver?? a repetir."

            if p_prot.pos in ["oral", "missionary", "69"]:
                if p_prot.pos == "oral":
                    $ nteye = "front05"
                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx08
                    show gensex_oral_n_frontHead_exp_eyebrows angryx06
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "missionary":
                    $ nteye = "front05"
                    show gensex_missionary_n_head_exp_mouth sad_Silentx08
                    show gensex_missionary_n_head_exp_eyebrows angryx06
                    call gensex_oral_n_frontHead_exp_tears_tears
                elif p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Silentx07
                with dissolve

    elif p_prot.restTurns >= 5 or afternight05_Pedrera_n_Neus_Warning_tongue >= 5:

        # show neus_exp_mouth sad_Talkingx11
        # show neus_exp_iris front04
        # $ nteye = 5
        # call neus_exp_tears_tears
        # show neus_exp_eyebrows angryx05
        # with dissolve

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if p_prot.pos in ["oral", "missionary", "69"]:
            if p_prot.pos == "oral":
                $ nteye = "front00"
                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx20
                show gensex_oral_n_frontHead_exp_eyebrows angryx05
                call gensex_oral_n_frontHead_exp_tears_tears
            elif p_prot.pos == "missionary":
                $ nteye = "front00"
                show gensex_missionary_n_head_exp_mouth sad_Talkingx20
                show gensex_missionary_n_head_exp_eyebrows angryx05
                call gensex_oral_n_frontHead_exp_tears_tears
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx08
            with dissolve

        if randomnum_1to5 == 1: 

            ne "??Te he avisado!"

        elif randomnum_1to5 == 2: 

            ne "??Como quieras!"

        elif randomnum_1to5 == 3:

            ne "??No me dejas otro remedio!"

        elif randomnum_1to5 == 4:

            ne "??Pensaba que lo entender??as!"

        elif randomnum_1to5 == 5:

            ne "??Lo hago para salvarnos!"

        if p_prot.pos in ["oral", "missionary", "69"]:
            if p_prot.pos == "oral":
                $ nteye = "front01"
                show gensex_oral_n_frontHead_exp_mouth sad_Silentx20
                show gensex_oral_n_frontHead_exp_eyebrows angryx06
                call gensex_oral_n_frontHead_exp_tears_tears
            elif p_prot.pos == "missionary":
                $ nteye = "front01"
                show gensex_missionary_n_head_exp_mouth sad_Silentx20
                show gensex_missionary_n_head_exp_eyebrows angryx06
                call gensex_oral_n_frontHead_exp_tears_tears
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Silentx08
            with dissolve

        # show neus_exp_mouth sadbiting_Silentx06
        # show neus_exp_iris front05
        # $ nteye = 5
        # call neus_exp_tears_tears
        # show neus_exp_eyebrows sadx02
        # with dissolve

        pause 0.2

        call afternight05_Pedrera_Sex_n_NeusLastWarning
            # n "De pronto, sientes como si algo se removiera por dentro de tu bolsa escrotal,"
            # n "al mismo tiempo que un cosquilleo que cubre desde tus ingles hasta casi la altura de tu ombligo."
            # p "??Qu?? demonios...?"

    ##

    # $ Pedrera_char_Cond = "p_nobody"
    # call Pedrera_char_lab

    ##

    return


label p_prot_moans_01_label:

    $ ped_check_1_10("ped_moans_p_prot_01_list")
    #$ randomnum_1to10 = renpy.random.randint(1, 10)

    if ped_check_list_result == 1:

        p "Hmmm..."

    elif ped_check_list_result == 2:

        p "Ahmm..."

    elif ped_check_list_result == 3:

        p "Geez..."

    elif ped_check_list_result == 4:

        p "Co??o..."

    elif ped_check_list_result == 5:

        p "??Hmmm...!"

    elif ped_check_list_result == 6:

        p "MMm..."

    elif ped_check_list_result == 7:

        p "Ahh..."

    elif ped_check_list_result == 8:

        p "Mmmfhmm..."

    elif ped_check_list_result == 9:

        p "Joder..."

    elif ped_check_list_result == 10:

        p "Hmmhn..."

    return

label afternight05_Pedrera_Sex_n_NeusLastWarning:

    play sound "audio/sfx/meme_surprise02.ogg"
    stop music fadeout 2.0

    scene black
    with vpunch

    n "Sientes que no eres capaz de mover ni un solo m??sculo de tu cuerpo."

    if p_prot.pos == "69":

        n "Sientes su cuerpo alej??ndose de ti mientras te empuja con fuerza para que reposes tu espalda sobre la cama."

    if p_prot.pos not in ["oral", "69"]:

        p "??Ugh!"

        n "Con un fuerte empuj??n te tira encima de la cama."

    if music_play != "killers":
        play music "audio/music/kevinmacleod/killers.ogg" fadein 10.0 fadeout 3.0
        $ music_play = "killers"   

    $ nleye = "full"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front08"
    show n_closefromup_mouth sadbiting_Silentx04
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with fade_short

    p "[neusname]..."

    $ nteye = "front00"
    show n_closefromup_mouth sad_Silentx08
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with Dissolve(0.5)

    n "Sus ojos brillan con una intensidad que pr??cticamente te dejan ciego."

    call WIP

    ## WORK IN PROGRESS

    jump endupdate


###################################
###################################

# call ped_sex_69_blowjob_received_01      ## Blowjob
# call ped_sex_69_blowjobDeep_received_01  ## Deepthroat

label ped_sex_69_mc_blowjob_scene_Stop:

    $ p_prot.b_action = "rest"
    $ p_girl_active.action = "rest"

    call ped_sex_69_mc_blowjob_Stop

    return

label ped_sex_69_mc_blowjob_Stop:

    $ ped_sex_general_expression_Cond = "talk"
    $ ped_sex_general_action_b_Cond = "69b_00_00"
    call pedrera_sex_p_general_talk

    return

label ped_sex_69_blowjob_received_01:

    $ p_neus.action = "blowjob_done"
    $ p_prot.b_action = "blowjob_received"

    $ ped_sex_general_expression_Cond = ""

    if p_neus.blowjob_done >= 6:
        $ ped_sex_general_action_b_Cond = "69b_02_05"
    elif p_neus.blowjob_done == 5:
        $ ped_sex_general_action_b_Cond = "69b_01_03"
    elif p_neus.blowjob_done == 4:
        $ ped_sex_general_action_b_Cond = "69b_01_01"
    elif p_neus.blowjob_done == 3:
        $ ped_sex_general_action_b_Cond = "69b_01_05"
    elif p_neus.blowjob_done == 2:
        $ ped_sex_general_action_b_Cond = "69b_01_03"
    elif p_neus.blowjob_done == 1:
        $ ped_sex_general_action_b_Cond = "69b_01_01"

    call pedrera_sex_p_general_talk

    return

label ped_sex_69_blowjob_received_02:

    $ p_neus.action = "blowjob_done"
    $ p_prot.b_action = "blowjob_received"

    $ ped_sex_general_expression_Cond = ""
    if p_neus.blowjob_done >= 5:
        $ ped_sex_general_action_b_Cond = "69b_02_05"
    elif p_neus.blowjob_done == 4:
        $ ped_sex_general_action_b_Cond = "69b_02_04"
    elif p_neus.blowjob_done == 3:
        $ ped_sex_general_action_b_Cond = "69b_02_02"
    elif p_neus.blowjob_done == 2:
        $ ped_sex_general_action_b_Cond = "69b_01_04"
    elif p_neus.blowjob_done == 1:
        $ ped_sex_general_action_b_Cond = "69b_01_02"

    call pedrera_sex_p_general_talk

    return

label ped_sex_69_blowjobDeep_received_01:

    $ p_prot.b_action = "blowjobDeep_received"
    $ p_neus.action = "blowjobDeep_done"

    $ ped_sex_general_expression_Cond = ""


    if p_neus.blowjobDeep_done >= 6:
        $ ped_sex_general_action_b_Cond = "69b_04_05"
    elif p_neus.blowjobDeep_done == 5:
        $ ped_sex_general_action_b_Cond = "69b_04_03"
    elif p_neus.blowjobDeep_done == 4:
        $ ped_sex_general_action_b_Cond = "69b_04_01"
    elif p_neus.blowjobDeep_done == 3:
        $ ped_sex_general_action_b_Cond = "69b_03_05"
    elif p_neus.blowjobDeep_done == 2:
        $ ped_sex_general_action_b_Cond = "69b_03_03"
    else:
        $ ped_sex_general_action_b_Cond = "69b_03_01"
    call pedrera_sex_p_general_talk

    return

label ped_sex_69_blowjobDeep_received_02:

    $ p_prot.b_action = "blowjobDeep_received"
    $ p_neus.action = "blowjobDeep_done"

    $ ped_sex_general_expression_Cond = ""

    if p_neus.blowjobDeep_done >= 5:
        $ ped_sex_general_action_b_Cond = "69b_04_05"
    elif p_neus.blowjobDeep_done == 4:
        $ ped_sex_general_action_b_Cond = "69b_04_04"
    elif p_neus.blowjobDeep_done == 3:
        $ ped_sex_general_action_b_Cond = "69b_04_02"
    elif p_neus.blowjobDeep_done == 2:
        $ ped_sex_general_action_b_Cond = "69b_03_04"
    else:
        $ ped_sex_general_action_b_Cond = "69b_03_02"
    call pedrera_sex_p_general_talk

    return


label ped_sex_69_mc_lickpussyStop:

    $ p_prot.action = "rest"
    $ p_girl_active_b_action = "rest"

    $ ped_sex_general_69_cover = "over"
    $ ped_sex_general_action_Cond = "69_00_00"
    call pedrera_sex_p_general_talk

    return

label ped_sex_69_mc_lickpussy01:

    if eval("p_" + p_activen + ".cunnilingus_received" ) == 1:
        $ ped_sex_general_action_Cond = "69_00_01"
    elif eval("p_" + p_activen + ".cunnilingus_received") == 2:
        $ ped_sex_general_action_Cond = "69_00_02"
    elif eval("p_" + p_activen + ".cunnilingus_received") == 3:
        $ ped_sex_general_action_Cond = "69_00_03"
    elif eval("p_" + p_activen + ".cunnilingus_received") == 4:
        $ ped_sex_general_action_Cond = "69_00_04"

    ## FROM HERE THE REST IS IGNORED IF SHE IS SUCKING YOUR COCK.

    elif eval("p_" + p_activen + ".cunnilingus_received") == 5:

        n "Finalmente,"

        if p_prot.pos == "69" and p_prot.b_action not in("blowjob_received", "blowjobDeep_received"):
            if p_active == "p_txell":
                show gensex_69_L_d_mouth sadbiting_Silentx06
                with dissolve
            elif p_active == "p_didac":
                show gensex_69_L_d_mouth sadbiting_Silentx07
                with dissolve
            elif p_active == "p_neus":
                show gensex_69_L_d_mouth sadbiting_Silentx05
                with dissolve
        
        n "introduces tu lengua para juguetear con sus paredes vaginales internas."

        $ ped_sex_general_action_Cond = "69_02_02"
    elif eval("p_" + p_activen + ".cunnilingus_received") == 6:
        $ ped_sex_general_action_Cond = "69_02_03"
    elif eval("p_" + p_activen + ".cunnilingus_received") == 7:
        $ ped_sex_general_action_Cond = "69_02_04"
    ##
    elif eval("p_" + p_activen + ".cunnilingus_received") == 8:

        $ ped_sex_general_action_Cond = "69_02_04"
        call pedrera_sex_p_general_talk
        with Dissolve(0.5)

        n "Con cierta pericia,"

        n "consigues incluso alargar a??n m??s tu longeva lengua en su interior."

        $ ped_sex_general_69_cover = "dissolve"

        $ ped_sex_general_action_Cond = "69_03_02"
    elif eval("p_" + p_activen + ".cunnilingus_received") == 9:
        $ ped_sex_general_action_Cond = "69_03_03"
    elif eval("p_" + p_activen + ".cunnilingus_received") == 10:
        $ ped_sex_general_action_Cond = "69_03_04"
    elif eval("p_" + p_activen + ".cunnilingus_received") >= 11:
        $ ped_sex_general_action_Cond = "69_03_05"

    call pedrera_sex_p_general_talk


    $ p_prot.action = "cunnilingus_done"
    $ p_girl_active.b_action = "cunnilingus_received"

    return

label ped_sex_69_mc_lickpussy02:

    $ ped_sex_general_69_cover = "dissolve"

    # # These three lines does exactly the same function, one is normal, other is getattr and the other is eval.
    # if p_didac.cunnilingus_received == 1:
    # if getattr("p_" + p_activen + ".cun_received" ) == 1: # Recommended by Remix
    # if eval("p_" + p_activen + ".cunnilingus_received") == 1: # Recommeded by Xavimat

    #if getattr("p_" + p_activen, cunnilingus_received) == 1:
    if eval("p_" + p_activen + ".cunnilingus_received" ) == 1:
        $ ped_sex_general_action_Cond = "69_01_01"
    elif eval("p_" + p_activen + ".cunnilingus_received") == 2:
        $ ped_sex_general_action_Cond = "69_01_02"
    elif eval("p_" + p_activen + ".cunnilingus_received") == 3:
        $ ped_sex_general_action_Cond = "69_01_03"
    elif eval("p_" + p_activen + ".cunnilingus_received") == 4:
        $ ped_sex_general_action_Cond = "69_01_04"

    ## FROM HERE THE REST IS IGNORED IF SHE IS SUCKING YOUR COCK.

    elif eval("p_" + p_activen + ".cunnilingus_received") == 5:

        $ ped_sex_general_action_Cond = "69_02_03"
    elif eval("p_" + p_activen + ".cunnilingus_received") == 6:
        $ ped_sex_general_action_Cond = "69_02_04"
    elif eval("p_" + p_activen + ".cunnilingus_received") == 7:
        $ ped_sex_general_action_Cond = "69_02_04"
    ##
    elif eval("p_" + p_activen + ".cunnilingus_received") == 8:

        $ ped_sex_general_action_Cond = "69_03_03"
    elif eval("p_" + p_activen + ".cunnilingus_received") == 9:
        $ ped_sex_general_action_Cond = "69_03_04"
    elif eval("p_" + p_activen + ".cunnilingus_received") == 10:
        $ ped_sex_general_action_Cond = "69_03_05"
    elif eval("p_" + p_activen + ".cunnilingus_received") >= 11:
        $ ped_sex_general_action_Cond = "69_03_05"

    call pedrera_sex_p_general_talk

    $ p_prot.action = "cunnilingus_done"
    $ p_girl_active.b_action = "cunnilingus_received"

    return