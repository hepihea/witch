init python:

    class McBody():

        def __init__(self):
            """
            MC Main Object.

            last_swapped: String. Used for combo; tells which part was lat swapped for combos.
            difficulty: Integer. Actual difficulty of the last roll.
            first_dice: Integer. Result of the roll. Default is 0.
            second_dice: Integer. Result of the roll. Default is 0.
            roll_success: Boolean. True if the roll was a success. Default is False.
            result: String. Contains the result of the dice roll. Default is "".
            orgasm: Integer. Number of times player has experienced orgasm
            """

            self.store = {
                "right_hand": "",
                "left_hand": "",
                "tongue": "",
                "dick": ""
            }

            self.last_swapped = ""
            self.difficulty = 0
            self.first_dice = 0
            self.second_dice = 0
            self.roll_success = False
            self.result = ""

            self.first_dice_rolls = []
            self.second_dice_rolls = []
            self.flashing_1 = 0.0
            self.flashing_2 = 0.0

            self._pleasure = 0
            self.orgasm = 0

            self.max_pleasure = {
                #0: 50,
                #1: 100,
                #2: 150, #This is in theory the last one.
                #3: 200,
                #4: 250
                #-1: 25 # bar -01 
                0: 50, #bar 00 
                1: 75, # bar 01 --59
                2: 100, #bar 02 --        This is in theory the last one.
                3: 125, # bar 03 --
                4: 150 # bar 04 --118 Divide it for 6
            }

            self.combo_store = {}
            self.bonus_store = {}

            self.dick_speed = 0

        @property
        def pleasure(self):
            return self._pleasure

        @pleasure.setter
        def pleasure(self, value):
            if PlatinumHelp:
                delta = value - self._pleasure
                renpy.show_screen("show_minigame_notification", delta=delta, kind="his_pleasure", name="toast_his_pleasure", _tag="toast_his_pleasure")
            self._pleasure = value

        def get_current_action(self, part):
            """
            Return the id of the current action performed by a mc part.

            part: String. Name of the part.
            """

            if part not in self.store:
                return "Unvalid part"

            return self.store[part]

        def get_max_pleasure(self):
            return self.max_pleasure[2]
            return self.max_pleasure[self.orgasm]

        def is_doing_action(self, part, action_id):
            """
            Returns True if an MC part is doing the provided action.

            part: String. Name of the part.
            action_id: String. Id of the action.
            """

            if part not in self.store:
                return "Unvalid part"

            return self.store[part] == action

        def set_action(self, action_id, primary_part, backup_part, check_bonus=True):
            # Check to see which MC body part we can assign this action to.
            if not self.store[primary_part]:
                part = primary_part
            elif not self.store[backup_part]:
                part = backup_part
            elif self.last_swapped == "primary":
                part = backup_part
                self.last_swapped = "backup"
            else:
                part = primary_part
                self.last_swapped = "primary"

            self.store[part] = action_id
            
            if check_bonus:
                return self.check_combo(part, action_id)

        def right_hand(self, action):
            self.store["right_hand"] = action
            self.check_combo("right_hand", action)

        def left_hand(self, action):
            self.store["left_hand"] = action
            self.check_combo("left_hand", action)

        def tongue(self, action):
            self.store["tongue"] = action
            self.check_combo("tongue", action)

        def dick(self, action):
            self.store["dick"] = action
            self.check_combo("dick", action)

        def add_combo(self, part_1, id_1, part_2, id_2, enslavement=0, her_diffculty=0, pleasure_you=0, pleasure_her=0):
            """
            part_1: ID of the MC Part
            part_2: ID of the MC Part
            id_1: ID of the action
            id_2: ID of the action
            """

            self.combo_store[(part_1, id_1)] = (part_2, id_2)
            self.combo_store[(part_2, id_2)] = (part_1, id_1)

            self.bonus_store[(part_1, id_1, part_2, id_2)] = {
                "enslavement": enslavement,
                "difficulty": her_difficulty,
                "pleasure": pleasure,
                "pleasure_you": pleasure_you,
            }

        def check_combo(self, part, id):
            second = None
            match = ()

            # Check if their is a bonus for the present combination of moves
            if part in self.bonus_store:
                second = self.bonus_store[part]

                # If the second part didn't match, return
                if self.store[second[0]] != second[1]:
                    return {}

                # If there is a combination, throw bonus
                return self.bonus_store[(part, id, second[0], second[1])]

            return {}

        def check_if_orgasm(self):
            if self.pleasure > self.max_pleasure[self.orgasm]:
                self.orgasm += 1
                self.pleasure = 0
                return True

            return False

        @property
        def clear(self):
            self.right_hand = ""
            self.left_hand = ""
            self.tongue = ""
            self.dick = ""

        def clear_dick(self):
            self.store["dick"] = ""
