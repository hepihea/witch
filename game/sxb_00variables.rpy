default pleasure_you = 0

default current_girl = None
default can_click = True

# Dice Scene instances
default mc_body = McBody()
default girl_1 = Girl(name="Name", base_dir="images/")

##
default pose_1 = Pose("pose_1", "Lying Down", girl_1, bg="afternight04_sexbattle_d_scene a")

default pose01_remove= BodyPart("remove", "Remove All", Solid("#00ff00"), 30, 30, "girl_1", pose_1, zoom=1.0) # NEW

default pose01_right_boob = BodyPart("right_boob", "Right Boob", Solid("#00ff00"), 160, 100, "girl_1", pose_1, zoom=0.95)
default pose01_right_nipple = BodyPart("right_nipple", "Right Nipple", Solid("#00ff00"), 173, 128, "girl_1", pose_1, zoom=0.15) # NEW

default pose01_right_leg = BodyPart("right_leg", "Right Leg", Solid ("0f0"), -20, 250, "girl_1", pose_1, zoom=2.0) # NEW
default pose01_left_leg = BodyPart("left_leg", "Left Leg", Solid ("0f0"), 400, 150, "girl_1", pose_1, zoom=2.0) # NEW

default pose01_mouth = BodyPart("mouth", "Mouth", Solid("#0f0"), 268, 90, "girl_1", pose_1, zoom=0.3) # NEW

default pose01_left_boob = BodyPart("left_boob", "Left Boob", Solid("#00ff00"), 295, 90, "girl_1", pose_1, zoom=0.95)
default pose01_left_nipple = BodyPart("left_nipple", "Left Nipple", Solid("#00ff00"), 370, 105, "girl_1", pose_1, zoom=0.15) # NEW

default pose01_stomach = BodyPart("stomach", "Stomach", Solid("#0f0"), 190, 160, "girl_1", pose_1, zoom=1.5) # NEW
default pose01_belly = BodyPart("belly", "Belly Button", Solid("#0f0"), 260, 238, "girl_1", pose_1, zoom=0.25) # NEW

default pose01_right_arm = BodyPart("right_arm", "Right Arm", Solid("#00ff00"), 375, 170, "girl_1", pose_1, zoom=0.7) # NEW

default pose01_left_buttock = BodyPart("left_buttock", "Left Buttock", Solid ("0f0"), 330, 370, "girl_1", pose_1, zoom=1.3) # NEW
default pose01_right_buttock = BodyPart("right_buttock", "Right Buttock", Solid ("0f0"), 170, 400, "girl_1", pose_1, zoom=1.3) # NEW

default pose01_pussy = BodyPart("pussy", "Pussy", Solid("#00ff00"), 255, 375, "girl_1", pose_1, zoom=0.9)
default pose01_clitoris= BodyPart("clitoris", "Clitoris", Solid("#00ff00"), 298, 405, "girl_1", pose_1, zoom=0.15) # NEW

default pose01_anal= BodyPart("anal", "Anal hole", Solid("#00ff00"), 325, 480, "girl_1", pose_1, zoom=0.15) # NEW




###
default pose_2 = Pose("pose_2", "Doggy Style", girl_1, bg="d_pose02")

default pose02_remove= BodyPart("remove", "Remove All", Solid("#00ff00"), 30, 30, "girl_1", pose_2, zoom=1.0) # NEW

default pose02_right_arm = BodyPart("right_arm", "Right Arm", Solid("#00ff00"), 340, 150, "girl_1", pose_2, zoom=0.75)

default pose02_left_boob = BodyPart("left_boob", "Left Boob", Solid("#00ff00"), 200, 190, "girl_1", pose_2, zoom=0.5)

default pose02_right_buttock = BodyPart("right_buttock", "Right Buttock", Solid ("0f0"), 285, 320, "girl_1", pose_2, zoom=0.95) # NEW
default pose02_left_buttock = BodyPart("left_buttock", "Left Buttock", Solid ("0f0"), 180, 320, "girl_1", pose_2, zoom=0.95) # NEW

default pose02_anal= BodyPart("anal", "Anal hole", Solid("#00ff00"), 285, 410, "girl_1", pose_2, zoom=0.15) # NEW

default pose02_pussy = BodyPart("pussy", "Pussy", Solid("#00ff00"), 282, 420, "girl_1", pose_2, zoom=0.2)

##
default pose_3 = Pose("pose_3", "Doggy Style", girl_1, bg="d_pose03")

default pose03_remove= BodyPart("remove", "Remove All", Solid("#00ff00"), 30, 30, "girl_1", pose_3, zoom=1.0) # NEW

default pose03_mouth = BodyPart("mouth", "Mouth", Solid("#00ff00"), 300, 90, "girl_1", pose_3, zoom=0.3)

default pose03_right_arm = BodyPart("right_arm", "Right Arm", Solid("#00ff00"), 140, 240, "girl_1", pose_3, zoom=0.65)

default pose03_right_boob = BodyPart("right_boob", "Right Boob", Solid("#00ff00"), 310, 160, "girl_1", pose_3, zoom=0.6)

default pose03_right_nipple = BodyPart("right_nipple", "Right Nipple", Solid("#00ff00"), 360, 183, "girl_1", pose_3, zoom=0.15) # NEW

default pose03_right_buttock = BodyPart("right_buttock", "Right Buttock", Solid ("0f0"), 285, 320, "girl_1", pose_3, zoom=0.95) # NEW
#default pose03_left_buttock = BodyPart("left_buttock", "Left Buttock", Solid ("0f0"), 180, 320, "girl_1", pose_3, zoom=0.95) # That hand is busy.

default pose03_anal= BodyPart("anal", "Anal hole", Solid("#00ff00"), 285, 410, "girl_1", pose_3, zoom=0.15) # NEW

default pose03_pussy = BodyPart("pussy", "Pussy", Solid("#00ff00"), 282, 420, "girl_1", pose_3, zoom=0.2)


default girl_difficulty = {
    1: 8,
    2: 7,
    3: 6,
    4: 5,
    5: 4,
    6: 3,
    7: 2,
    8: 1,
    "default": 0
}