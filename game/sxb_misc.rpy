init python:

    class DoAction(Action):

        def __init__(self, part):
            self.part = part

        def __call__(self):
            self.part.do()

    def roll_dice(difficulty):
        """
        This function returns if the roll was a success or not.

        diffculty: Integer. The diffculty at which the roll will happen.
        """

        ########################################

        ## If difficulty is lower than 6, it's auto pass
        if difficulty <= 5:
            return "easy_pass", ("-", "-")

        ## Calculate the value of both the dice rolls.
        value_1 = renpy.random.randint(1, 10)
        value_2 = renpy.random.randint(1, 10)

        #########################################

        ## If difficulty is lower than 6, it's auto pass
        #if difficulty <= 6:
            #value_1 = 6
            #value_2 = 6
        #else:
            ## Calculate the value of both the dice rolls.
            #value_1 = renpy.random.randint(1, 10)
            #value_2 = renpy.random.randint(1, 10)

        #########################################

        # If player gets 1 on both the dice, they fail
        if value_1 == 1 and value_2 == 1:
            return "super_fail", (1, 1)
        elif value_1 == 10 and value_2 == 10:
            return "super_pass", (10, 10)

        if max(value_1, value_2) >= difficulty:
            return "pass", (value_1, value_2)
        else:
            return "fail", (value_1, value_2)

    def get_dick_action(kind="Pussy", level="up"):
        if kind == "Anal hole":
            kind = "Anal"

        if level == "up":
            _lookup = {
                "": "{}_dick_low".format(kind),
                "{}_dick_out".format(kind): "{}_dick_low".format(kind),
                "{}_dick_low".format(kind): "{}_dick_med".format(kind),
                "{}_dick_med".format(kind): "{}_dick_deep".format(kind),
                "{}_dick_deep".format(kind): "{}_dick_deep".format(kind)
            }
        else:
            _lookup = {
                "": "{}_dick_out".format(kind),
                "{}_dick_out".format(kind): "{}_dick_out".format(kind),
                "{}_dick_low".format(kind): "{}_dick_out".format(kind),
                "{}_dick_med".format(kind): "{}_dick_low".format(kind),
                "{}_dick_deep".format(kind): "{}_dick_med".format(kind)

            }

        if mc_body.get_current_action("dick") not in _lookup:
            return _lookup[ "{}_dick_out".format(kind) ]
        else:
            return _lookup[ mc_body.get_current_action("dick") ]

    def get_dick_speed_image(prefix, suffix, min, max, level):

        if level == "up":
            if mc_body.dick_speed+1 > max:
                return prefix + str(max) + suffix
            return prefix + str(mc_body.dick_speed+1) + suffix

        elif level == "down":
            if mc_body.dick_speed > max:
                return prefix + str(max) + suffix
            return prefix + str(mc_body.dick_speed) + suffix

    def get_bar(current):
        if current == 0:
            return "images/sexbattle/premium_dashboard/bar_pleasure_frame_00.webp"
        elif current == 1:
            return "images/sexbattle/premium_dashboard/bar_pleasure_frame_01.webp"
        elif current == 2:
            return "images/sexbattle/premium_dashboard/bar_pleasure_frame_02.webp"
        elif current == 2:
            return "images/sexbattle/premium_dashboard/bar_pleasure_frame_03.webp"
        else:
            return "images/sexbattle/premium_dashboard/bar_pleasure_frame_04.webp"

    def value_dict(d, key):
        if key in d:
            return d[key]
        return d["default"]

    def show_expressions_func(show_expressions):
        for im, atl in show_expressions:
            renpy.show(name=im, at_list=[atl])
        
transform zoom_button(z):
    zoom z

transform set_alpha(level):
    alpha level
