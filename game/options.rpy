## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The (_()) surrounding the string marks it as eligible for translation.


init -1 python:
    Tendolarsversion = True #True=10$Patrons .
    Platinumversion = True # True =1$, 3$ and 5$.

    programming_check = False ## progcheck text is visible if it´s True.
    Steam_check = False # For Steam Version.
    PlatinumHelp = False # Keep this False for No Cheating.



###################################
######################################################################
######################################################################
    Tendolarsversionvisited = False #DON´T CHANGE THAT, keep it FALSE!

    if Tendolarsversion == True or Platinumversion == True:
        config.autosave_slots = 10
        config.has_autosave = True
        config.autosave_on_choice = True
        config.autosave_on_quit = True
    else:
        config.autosave_slots = 0
        config.has_autosave = False
        config.autosave_on_choice = False
        config.autosave_on_quit = False

    if Tendolarsversion or Platinumversion:
        PlatinumHelp = True
    
define config.name = (_("Pacto con una Bruja"))

#define config.autosave_slots = 10
#define config.has_autosave = True
#define config.autosave_on_choice = True
#define config.autosave_on_quit = True


define is_save_allowed = True #To allow save for EVERYBODY or just for PREMIUM.



###############################################################
###############################################################

## The version of the game.

define config.version = "00.18.02_b"


#######################################################

    ### The last update is this one:

    # #########################################################

    # if config.version < "00.14.06": # Library Part
    #     call endupdatescript
    
    # #######################################################



#Activate 10$ (Dolars) Version, where there´s no ending point.

default Tendolarstext = "PREMIUM"
default Platinumtext = "PLATINUM"

#define Tendolarstext = "PREMIUM" # Better use Default, since this can change.
#define Platinumtext = "PLATINUM"

## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True #Leave it TRUE!!!!

## Text that is placed on the game's about screen. To insert a blank line
## between paragraphs, write \n\n.

define gui.about = (_(""))


## As of Ren'Py 7.4 (late 2020), Model-Based rendering needs to be enabled to be used. This is done by setting config.gl2 to True, using:
#define config.gl2 = True

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "pact_with_a_witch"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
##define config.has_voice = True # This Blocks the Voice Acting and blocks also the bar for that.
define config.fix_rollback_without_choice = True
##define config.developer = True #To acces Dev Menu, DragoonHP

################################################################################
################################################################################

#######################
## Code from booom313

#define config.variants = ["large", "pc", "touch", None] # NOT FINISHED, it doesn´t work :(

################################################################################
################################################################################


#######################
## Code from Remix (from Discord) Not use the without _mb anymore)
#in MegaBytes 300 is the default https://renpy.org/doc/html/config.html#var-config.image_cache_size).

define config.image_cache_size = None
# default is 16 


define config.image_cache_size_mb = 300
# default is 300



# It increases the amount of images Ren'Py can store in RAM
# It will consume more memory but should provide a smoother play experience
################################################################################
################################################################################

        ## If True, Ren'Py will write information about the image cache to image_cache.txt.

#define config.debug_image_cache = True


        ##In theory is for eliminate the cache files... but I don´t know how it work exactly...

define config.imagemap_cache = False #DragoonHP: If you use imagemaps in game, set it to True. Otherwise, let it be.

################################################################################
################################################################################


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

#define config.main_menu_music = "main-menu-theme.ogg"
define config.main_menu_music = "audio/music/alcaknight/despair.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur. Each
## variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = fade


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "pactwithawitch0.2-1475777953"


## Icon
## ########################################################################'

## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory,
    ## "game/**.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.
    if Tendolarsversion:
        build.directory_name = "PREMIUM_pact_with_a_witch_v" + config.version
    elif Platinumversion:
        build.directory_name = "PLATINUM_pact_with_a_witch_v" + config.version
    else:
        build.directory_name = "pact_with_a_witch_v" + config.version

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    
    build.classify("**.psd", None)
    build.classify("**.tga", None)
    build.classify("**.bmp", None)
    build.classify("**.lip", None) #Old Clip Studio Files.
    build.classify("**.clip", None) #New Clip Studio Files
    build.classify("**.mp3", None)
    build.classify("**.rar", None)
    build.classify("**.zip", None)
    
    
    build.classify('game/images/startmenu/promotion/**', None) #Whatever in this folder is deleted in Build.

    ## To archive files, classify them as 'archive'.
    
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.webp', 'archive')
    build.classify('game/**.rpy', 'archive') #If you don´t want to archieve them, just put a # in front of it, like if you delete it.
    build.classify('game/**.rpyc', 'archive')#If you don´t want to archieve them, just put a # in front of it, like if you delete it
    build.classify('game/**.rtf', 'archive')
    
    build.classify("**.ttf", 'archive') #True Type Font
    build.classify("**.otf", 'archive') #Open Type Font

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"


####################################################################################
######################################################################
####################################################################################
####################################################################################
######################################################################
####################################################################################
####################################################################################
######################################################################
####################################################################################
####################################################################################
######################################################################
####################################################################################

# init python:
#     def the_voice(identifier):        
#         if _preferences.language == "english":
#             return "audio/voice/english/*/" + identifier + ".ogg"            
        
#     config.auto_voice = the_voice

init python:

    vvoice = 0.0 ## This for start the game with Voice Volume = 0 (Delete Persistent)

    all_voices = [i for i in renpy.list_files() if i.startswith("audio/voice/") and i.endswith(".ogg")]

    def the_voice(identifier):
        if _preferences.language == "english":
            for i in all_voices:
                if identifier in i:
                    return i

    config.auto_voice = the_voice

# init python:
    
#     vvoice=1.0

#     # voices
#     if _preferences.language == "english":
#         config.has_voice = True
#         config.auto_voice = "audio/voice/english/{id}.ogg"
#         vvoice=1.0
#     else:
#         config.has_voice = False