init python:

    class Girl():

        def __init__(self, name, base_dir, enslavement=0, pleasure=0):
            """
            Main Girl Object.

            name. String. Name of the girl.
            base_dir: String. Path to the folder which contains the images.
            enslavement: Integer. Enslavement Points.
            pleasure: Integer. Pleasure Points.

            store: Dict. Stores details about the poses.

            Attributes underneath are internal and are updated after every interaction.

            first_dice: Integer. Result of the roll. Default is 0.
            second_dice: Integer. Result of the roll. Default is 0.
            roll_success: Boolean. True if the roll was a success. Default is False.
            result: String. Contains the result of the dice roll. Default is "".
            repeat: String. How many times an action has been done. Default is "".
            """

            self.name = name
            self.base_dir = base_dir

            self._enslavement = enslavement
            self._pleasure = pleasure

            self.last_action_name = ""
            self.difficulty = 0

            self.first_dice = 0
            self.second_dice = 0
            self.roll_success = False
            self.result = "Not Rolled"
            self.repeat = ""
            self.total_try = 0
            self.total_fail = 0
            self.total_success = 0

            self.first_dice_rolls = []
            self.second_dice_rolls = []
            self.flashing = 0.0
            self.did_a_roll= True

            self.orgasm = 0

            self.max_pleasure = {
                #0: 50,
                #1: 100,
                #2: 150,
                #3: 200,
                #4: 250
                0: 50,
                1: 75,
                2: 100,
                3: 125,
                4: 150
            }

            self.store = {}

        @property
        def pleasure(self):
            return self._pleasure

        @pleasure.setter
        def pleasure(self, value):
            if PlatinumHelp:
                delta = value - self._pleasure
                renpy.show_screen("show_minigame_notification", delta=delta, kind="pleasure", name="toast_pleasure", _tag="toast_pleasure")
            self._pleasure = value

        @property
        def enslavement(self):
            return self._enslavement

        @enslavement.setter
        def enslavement(self, value):
            if PlatinumHelp:
                delta = value - self._enslavement
                renpy.show_screen("show_minigame_notification", delta=delta, kind="enslavement", name="toast_enslavement", _tag="toast_enslavement")
            self._enslavement = value

        def reg_pose(self, pose):
            """
            Registers all pose.

            pose: Instance of Pose.
            """

            self.store[pose.id] = pose

        def switch_pose(self, id):
            """
            Switch Pose.

            id: ID of the pose.
            """

            self.roll = False
            return self.store[id]

        def get_max_pleasure(self):
            if self.orgasm > 2:
                return self.max_pleasure[4]
            return self.max_pleasure[self.orgasm]

        def check_if_orgasm(self):
            if self.pleasure > self.get_max_pleasure():
                self.orgasm += 1
                self.pleasure = 0
                return True

            return False

    class Pose():


        def __init__(self, id, name, girl, bg):
            """
            Main Pose Object.

            id: String. A unique id given to a pose.
            name: String. Name of the pose.
            girl: Instance of Girl.
            bg: String. Name of the image.
            """

            self.id = id
            self.name = name
            self.bg = bg
            self.store = []

            # Registers this pose with the Girl.
            girl.reg_pose(self)

        def add_part(self, part):
            self.store.append(part)

        def return_part(self):
            return self.store

    class BodyPart():

        def __init__(self, id, name, image, x, y, girl, pose, zoom=1.0):
            self.id = id
            self.name = name
            self.image = image
            self.x = x
            self.y = y
            self.zoom = zoom
            self.girl = girl

            self.store = {}

            pose.add_part(self)

        def add_action(self, id, name, difficulty, pleasure, enslavement, mc_pleasure, primary_part, backup_part, blocked_actions=[], image=None, image_idle=None, image_hover=None):

            self.store[id] = PartAction(id, name, difficulty, pleasure, enslavement, mc_pleasure, primary_part, backup_part, self.girl, blocked_actions, image, image_idle, image_hover)

        def get_action(self, id):
            if id not in self.store:
                return {}
            return self.store[id]

    class PartAction():

        def __init__(self, id, name, difficulty, pleasure, enslavement, mc_pleasure, primary_part, backup_part, girl, blocked_actions=[], image=None, image_idle=None, image_hover=None):
            self.id = id
            self.name = name
            self.image = image
            self.image_idle = image_idle
            self.image_hover = image_hover
            self.difficulty = difficulty
            self.pleasure = pleasure
            self.enslavement = enslavement
            self.mc_pleasure = mc_pleasure
            self.primary_part = primary_part
            self.backup_part = backup_part
            self.girl = getattr(store, girl)
            self.blocked_actions = blocked_actions

            self.times_done = 0
            self.times_failed = 0

        def is_sensitive(self):
            """
            Returns True if player can do this action.
            """

            # Check to see if an action is already being done which makes doing this action impossible
            if self.blocked_actions:
                if mc_body.is_doing_action(part, action):
                    return False
            return True

        def times_action_done(self):
            """
            Returns how many times an action has been done.
            """

            if not self.times_done:
                return "not_happened"

            if self.times_done == 1:
                return "once"

            elif self.times_done == 2:
                return "twice"

            elif self.times_done == 3:
                return "thrice"

            elif self.times_done == 4:
                return "fourth"

            elif self.times_done == 5:
                return "fifth"

            elif self.times_done == 6:
                return "sixth"

            elif self.times_done < 7:
                return "repetitive"

            else:
                return "repeated_lots"

        def do(self):
            """
            This method is called when a player tries to perform an action.

            part: The part used to perform the action
            """

            if "dick" in self.id:
                extra = mc_body.dick_speed
            else:
                extra = 0

            if not mc_body.get_current_action("dick"):
                mc_body.dick_speed = 0

            ##

            #afternight04__prehfix_dick_speed = mc_body.dick_speed

            # Find out the actual difficulty as the difficulty decreases 1 point per 10 points of enslavement.
            difficulty_decrease = self.girl.enslavement / 10
            actual_difficulty = value_dict(self.difficulty, self.times_done) - difficulty_decrease + extra

            # Normalise difficulty
            if actual_difficulty < 0:
                actual_difficulty = 0
            result, rolled = roll_dice(actual_difficulty)

            # Update the value for the MC Roll
            mc_body.difficulty = actual_difficulty
            mc_body.result = result
            mc_body.first_dice = rolled[0]
            mc_body.second_dice = rolled[1]
            mc_body.roll_success = False
            mc_body.first_dice_rolls = renpy.random.sample(xrange(1, 10), 9)
            mc_body.second_dice_rolls = renpy.random.sample(xrange(1, 10), 9)
            mc_body.flashing_1 = 3.0
            mc_body.flashing_2 = 3.0

            # Set all the rolls to False
            self.girl.first_dice = 0
            self.girl.second_dice = 0
            self.girl.roll_success = False
            self.girl.result = "Not rolled"
            self.girl.last_action_name = self.name
            self.girl.did_a_roll = False

            # Find out if the current action is eligible for any bonuses
            # If yes, update the values accordingly.
            bonus = {} # mc_body.set_action(self.id, self.primary_part, self.backup_part)

            for tag, value in bonus.iteritems():
                if "pleasure_you" == tag:
                    mc_body.pleasure += value
                else:
                    old = getattr(self.girl, tag)
                    setattr(self.girl, tag, old+value)

            if "fail" in result:
                self.fail_action(result, actual_difficulty)
            else:
                self.passed_action(result, actual_difficulty)

        def calc_her_diff(self, difficulty):
            """
            This method calculates the difficulty of the "HER ROLL" and returns True if the roll was a success.

            difficulty: Integer. His roll diffculty.
            """

            if not self.times_done:
                # Index which contains "HER ROLL DIFFICULTY" based on "HIS ROLL DIFFICULTY"
                her_diff_index = {6: 9, 7: 8, 8: 7, 9: 6, 99: 10}

                # If difficulty is greater than 10, only double 10 should be successful.
                if difficulty > 10:
                    her_difficulty = 11
                else:
                    her_difficulty = her_diff_index[difficulty]
            else:
                her_difficulty = value_dict(girl_difficulty, self.times_done)

            # If a "HER ROLL" has taken place, update the values
            result, rolled = roll_dice(her_difficulty)
            self.girl.first_dice = rolled[0]
            self.girl.second_dice = rolled[1]
            self.girl.difficulty = her_difficulty
            self.girl.did_a_roll = True

            # If the action failed, do nothing.
            if "fail" in result:
                self.girl.result = "fail"
                self.girl.roll_success = False
                return
            
            self.girl.roll_success = True
            self.girl.result = "pass"

        def fail_action(self, result, difficulty):
            """
            Called if the MC fails in a dice roll.

            result: String. The result of the dice roll.
            difficulty: Integer. The difficulty by which the dice was rolled.
            """

            if result == "super_fail" and difficulty >= 10:
                #mc_body.pleasure += 15 # DragoonHP CODE NOT FINISHED
                #self.girl.enslavement -= 10
                self.girl.roll_success = True
                self.girl.result = "pass"

                #if self.girl.enslavement < 0: # Whaaat...? No... I don´t think so... xD
                    #self.girl.enslavement = 0

            elif result == "fail" and difficulty >= 10:
                #mc_body.pleasure += 10 # DragoonHP CODE NOT FINISHED
                self.girl.roll_success = True
                self.girl.result = "pass"

            elif result == "fail" or self.times_done:
                # If MC fails in his roll and his difficulty was less than 10, determine if "HER ROLL" was a success
                self.calc_her_diff(difficulty)

            self.times_failed += 1
            self.girl.repeat = self.times_action_done()
            self.girl.total_fail = self.times_failed
            self.girl.total_success = self.times_done #It works!
            self.girl.total_try = self.times_done + self.times_failed


            renpy.jump(self.id)

        def passed_action(self, result, difficulty):
            """
            This method is called when "HIS ROLL" is a success

            result: String. Result of the roll.
            difficulty: Integer: The diffculty at which the roll happened.
            """

            # Update the variables value
            #self.girl.enslavement += value_dict(self.enslavement, self.times_done)
            #self.girl.pleasure += value_dict(self.pleasure, self.times_done)
            #mc_body.pleasure += value_dict(self.mc_pleasure, self.times_done)

            # If MC/his dicculty is less than 6, roll the dice wil 10 difficulty or the Girl/her
            if difficulty < 6:
                self.calc_her_diff(99)

            elif self.times_done:
                self.calc_her_diff(difficulty)

            self.times_done += 1

            self.girl.repeat = self.times_action_done()
            self.girl.total_fail = self.times_failed
            self.girl.total_success = self.times_done
            self.girl.total_try = self.times_done + self.times_failed
            mc_body.roll_success = True

            renpy.jump(self.id)

        @property
        def idle(self):
            return self.image_idle

        @property
        def hover(self):
            return self.image_hover

    def dynamic_first_dice(st, at):
        mc_body.flashing_1 -= 0.15
        if mc_body.flashing_1 < 0:
            mc_body.flashing_1 = 0

        if mc_body.first_dice_rolls:
            return Text(str(mc_body.first_dice_rolls.pop())), 0.15
        return Text(str(mc_body.first_dice)), 0.15

    def dynamic_second_dice(st, at):
        mc_body.flashing_2 -= 0.15
        print mc_body.flashing_2
        if mc_body.flashing_2 < 0:
            mc_body.flashing_2 = 0

        if mc_body.second_dice_rolls:
            return Text(str(mc_body.second_dice_rolls.pop())), 0.15
        return Text(str(mc_body.second_dice)), 0.15

screen show_minigame_notification(delta, kind, off=-100, name):
    zorder 99
    timer 2.0 action Hide(name)

    default toast_pos = {
        "his_pleasure": (0, 0),
        "enslavement": (0, 50),
        "pleasure": (0, 75)
        
    }
    if delta > 0:
        default string = "{color=#6abd45}{size=20}+"
    else:
        default string = "{color=#ed2024}{size=20}"

    if kind == "enslavement":
        default string_2 = string + "[delta] " + "{image=icon_enslavery_didac}" + "{/color}"
    elif kind == "pleasure":
        default string_2 = string + "[delta] " + "{image=icon_pleasure_didac}" +"{/color}"
    else:
        default string_2 = string + "[delta] " + "{image=icon_pleasure_you}" + "{/color}"  

    text string_2 at _notify_minigame_transform(toast_pos[kind], off)

transform _notify_minigame_transform(xypos, off):
    # These control the position.
    pos xypos

    # These control the actions on show and hide.
    on show:
        subpixel True
        #alpha 0 xoffset off
        #linear .5 alpha 1.0 xoffset -(off) #DragoonHP
        alpha 0.0 xpos -0.05
        easein_quad 0.5 alpha 1.0 xpos 0.02
        pause 2.0

    on hide:
        easeout_quad 2.0 alpha 0.0 xoffset off

transform blink:
    alpha 1.0
    easein_quad 0.5 alpha 0.0
    easeout_quad 0.5 alpha 2.0
    repeat
