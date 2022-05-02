
#############################################
## Gallery Sections
#############################################

# TODO: Translate
default gallery_image_sections = [
    _("Día 1, 2 y 3 (1"),
    _("Día 4 (2"),
    _("Día 5a (3"),
    _("Día 5b (4"),
    _("Epílogo (5"),
    _("Otros"),
    _("Fondos"),
    _("Finales"),
    ]

default gallery_image_sections_index = 0
default gallery_image_sections_page = [0] * len(gallery_image_sections)

default gallery_image_thumbnail_cols = 4
default gallery_image_thumbnail_rows = 3

# Note that the actual Image Galleries reflect these sections.
# They are created and populated in gallery_images.rpy under
#the name
#
# store.gallery_image_objects
#
# If the relevant Image Gallery has no unlocked images it will 
# not be accessible through the navigation

# Default settings for viewport and zooming

default gallery_image_size = (800, 600)
default gallery_image_size_done = False

# These must be floats (for python 2.7 math) and maintain 4:3 aspect
default gallery_viewport_size = (720.0, 540.0)

# These are recalculated per image so values here are moot
# [current, min, max, range]
default gallery_zoom_settings = [1.0, 0.2, 2.0, 1.8]

default gallery_type = "image"


#############################################
## Gallery Styles - to get bits centred in their areas 
#############################################

style gallery_outer_frame:
    padding (0,0)
    background None
    xfill True
    xalign 0.5

style gallery_inner_frame:
    background None
    padding (0,0)
    xalign 0.5


#############################################
## Gallery Screens 
#############################################

# Wrapper screen to hold the various galleries
screen gallery(type="image"):

    tag menu
    
    use game_menu('Gallery'): # TODO: Translate

        frame:
            style "gallery_outer_frame"
            xsize 450

            vbox:

                spacing 10

                use gallery_types

                use expression "gallery_{}".format(gallery_type)

# Navigation between the various galleries
screen gallery_types():

    frame:
        style "gallery_outer_frame"

        frame:
            style "gallery_inner_frame"

            hbox:
                spacing 20
                # TODO: Translate
                textbutton _("Images"):

                    action SetVariable("gallery_type", "image")

                textbutton _("Replays"):

                    action SetVariable("gallery_type", "replay")

                textbutton _("Music"):

                    action SetVariable("gallery_type", "music")

# Thumbnail selection screen for image gallery
# Contains grid of paged thumbnails, page navigation, section navigation
screen gallery_image():

    $ gallery = gallery_image_objects[gallery_image_sections_index]

    $ button_index_to_name = {
        k:v for k,v in [
            (gallery.buttons[j].index, j) 
            for j in gallery.buttons
        ]
    }

    $ current_page = gallery_image_sections_page[gallery_image_sections_index]

    $ grid_size = gallery_image_thumbnail_cols * gallery_image_thumbnail_rows

    $ section_name = gallery_image_sections[gallery_image_sections_index]

    $ start_index = current_page * grid_size

    frame:
        style "gallery_inner_frame"

        text "[section_name!qt]" xalign 0.5 ypos 10

        grid gallery_image_thumbnail_cols gallery_image_thumbnail_rows:

            style_prefix "slot"
            xalign 0.5
            ypos 52
            spacing 10

            for button_index in range(start_index, start_index + grid_size):

                if button_index < len(gallery.button_list):

                    use gallery_image_thumbnail(
                        gallery,
                        button_index, 
                        button_index_to_name[button_index])

                else:

                    add Null(xysize=(100,100))

        vbox:
            style_prefix "page"
            yalign 1.0
            spacing gui.page_spacing

            use gallery_image_section_pagination(gallery_image_objects)


            use gallery_image_sections(gallery_image_objects)

# Each thumbnail has its own screen
# Just so we do not clutter the main screen too much
screen gallery_image_thumbnail(gallery, button_index, button_name):

    $ button = gallery.button_list[button_index]
    $ thumbnail, crop = gallery.thumbnail_info(button)

    imagebutton:

        style_prefix None

        # Unlocked idle thumbnail
        idle AlphaMask(
            Transform(thumbnail, crop=crop, maxsize=(100,100)),
            "images/gallery/gThumbs/gThumb_mask.webp")

        # Unlocked hover thumbnail
        hover AlphaMask(
            Transform(thumbnail, crop=crop, maxsize=(100,100)),
            "images/gallery/gThumbs/gThumb_mask.webp")

        # Unlocked hover and idle foregrounds (simple tint)
        idle_foreground "images/gallery/gThumbs/gThumb_idle_overlay.webp"
        hover_foreground "images/gallery/gThumbs/gThumb_hover_overlay.webp"

        # The Locked thumbnail
        insensitive Composite(
            (100, 100),
            (0, 0), AlphaMask(
                Transform(thumbnail, crop=crop, maxsize=(100,100)),
                "images/gallery/gThumbs/gThumb_mask.webp"),
            (0, 0), Transform(
                "images/gallery/gThumbs/gThumb_locked.webp",
                alpha=0.85),
            (0, 0), "images/gallery/gThumbs/gThumb_hover_overlay.webp")

        action gallery.Action(button_name)

# Image gallery page navigation for when there are more thumbnails
# than fit in the grid
screen gallery_image_section_pagination(gal_objects=None):

    $ gallery = gal_objects[gallery_image_sections_index]
    $ num_buttons = len(gallery.button_list)
    $ grid_size = gallery_image_thumbnail_cols * gallery_image_thumbnail_rows
    $ current_page = gallery_image_sections_page[gallery_image_sections_index]
    $ num_pages = int(num_buttons // grid_size) + 1

    if not num_buttons > grid_size:

        add Null()

    else:

        frame:
            style "gallery_outer_frame"

            frame:
                style "gallery_inner_frame"

                hbox:
                    spacing gui.page_spacing

                    textbutton _("<"):
                        sensitive current_page > 0
                        action SetDict(
                            gallery_image_sections_page,
                            gallery_image_sections_index,
                            current_page - 1)

                    ### Upto 5 named/indexed pages by number
                    for k in range(current_page - 2, current_page + 4): # Default: current_page +3 //Día 01 Fondos?

                        if 0 <= k <= num_pages - 1:

                            textbutton "{}".format(k+1):
                                selected (current_page == k)
                                action SetDict(
                                    gallery_image_sections_page,
                                    gallery_image_sections_index,
                                    k)

                    textbutton _(">"):
                        sensitive current_page < num_pages - 1
                        action SetDict(
                            gallery_image_sections_page,
                            gallery_image_sections_index,
                            current_page + 1)
            # add "bg_dark_a_blurry_02"

# Image gallery section navigation
screen gallery_image_sections(gal_objects=None):

    frame:
        style "gallery_outer_frame"

        frame:
            style "gallery_inner_frame"

            hbox:

                spacing gui.page_spacing

                for idx,section_name in enumerate(gallery_image_sections):

                    $ locked = True

                    if (gal_objects[idx] 
                            and hasattr(gal_objects[idx], "button_list")):

                        python:

                            for gal_button in gal_objects[idx].button_list:

                                if gal_button.check_unlock():

                                    locked = False

                                    break

                    if section_name[-1] in "12345":

                        $ section_name = section_name[-1]

                    textbutton "[section_name]":

                        sensitive not locked

                        action SetVariable("gallery_image_sections_index", idx)


# Displays a set of images in the gallery, or indicates that the images
# are locked. This is given the following arguments:
#
# locked
#     True if the image is locked.
# displayables
#     A list of transformed displayables that should be shown to the user.
# index
#     A 1-based index of the image being shown.
# count
#     The number of images attached to the current button.
# gallery
#     The image gallery object.


# This is the screen that displays each image when the thumbnail is
# clicked. 
screen _gallery:

    python:

        if not gallery_image_size_done:

            vp_image_size = gallery_image_size

            try:

                calc_image_size = renpy.render( 
                    ImageReference(
                        displayables[0].child.child.name[0]), 
                        0, 0, 0, 0).get_size()

                if calc_image_size[0]:

                    vp_image_size = (
                        int(calc_image_size[0]),
                        int(calc_image_size[1]))

            except:

                pass

            gallery_zoom_settings[0] = 0.0

            gallery_zoom_settings[1] = min(
                gallery_viewport_size[0] / vp_image_size[0],
                gallery_viewport_size[0] / vp_image_size[1])

            gallery_zoom_settings[2] = max(1.4, gallery_zoom_settings[1] * 10)

            gallery_zoom_settings[3] = (
                gallery_zoom_settings[2] - gallery_zoom_settings[1])          

            gallery_image_size_done = True

            # TODO: Specify default zoom level (minimum/just fit or other)
        

    key "viewport_wheelup" action SetDict(
        gallery_zoom_settings, 0, 
        min(1.0, gallery_zoom_settings[0] + 0.1))

    key "viewport_wheeldown" action SetDict(
        gallery_zoom_settings, 0, 
        max(0.0, gallery_zoom_settings[0] - 0.1))

    add "bg_dark_a_blurry_02"
    fixed:
        if locked:
            #add "#000"
            # TODO: Translate
            text _("Image [index] of [count] locked.") align (0.5, 0.5)
        else:
            viewport:
                id "viewer_viewport"
                area (40, 5, 720, 540)
                draggable True
                for d in displayables:
                    add Transform(d, zoom=(
                        gallery_zoom_settings[1] 
                        + (gallery_zoom_settings[0] 
                           * gallery_zoom_settings[3])))

    fixed:

        use gallery_image_navigation

        # text "[vp_image_size]" at truecenter yoffset -100

    if gallery.slideshow:
        timer gallery.slideshow_delay action Return("next") repeat True

    key "game_menu" action gallery.Return()

# This screen includes the frame overlay, the buttons to
# control movement between images linked to the thumbnail
# and shows a bar to indicate zoom level
screen gallery_image_navigation:
    fixed:

        # TODO: Create proper overlay graphic for this frame
        # TODO: Adjust frame properties to suit image

        frame:
            area (0,0, 800, 600)
            background Frame(
                "images/gallery/gThumbs/viewport_overlay.webp", 50, 15, 50, 65)

        # The buttons at the base (zoom bar, slideshow and return)

        fixed:
            area (50, 540, 700, 60)

            text _("Image [index] of [count]") align (0.0, 0.5)

            bar value DictValue(
                gallery_zoom_settings, 0, 
                range=1.0
                ) style "slider_bar" xysize (200, 10) yalign 0.5 xpos 300

            imagebutton:
                idle "images/gallery/gThumbs/g_slideshow_idle.webp"
                hover "images/gallery/gThumbs/g_slideshow_hover.webp"
                #idle Solid('#F88', xysize=(36,36))
                action gallery.ToggleSlideshow()
                align (1.0, 0.5)
                xoffset -50
                yoffset 2

            imagebutton:
                idle "images/gallery/gThumbs/g_return_idle.webp"
                hover "images/gallery/gThumbs/g_return_hover.webp"
                #idle Solid('#F88', xysize=(36,36))
                action gallery.Return()
                align (1.0, 0.5)
                yoffset 2


        # Previous Button 
        button:
            area (0, 0, 100, 540)

            idle_foreground Image ("images/gallery/gThumbs/g_d_previous_idle.webp", align=(0.75, 0.5))
            #idle_foreground Solid('#F777', xysize=(36,72), align=(0.75, 0.5))
            hover_foreground Image ("images/gallery/gThumbs/g_d_previous_hover.webp", align=(0.75, 0.5))

            action gallery.Previous(unlocked=gallery.unlocked_advance)


        # Next Button
        button:
            area (700, 0, 100, 540)
            idle_foreground Image ("images/gallery/gThumbs/g_d_next_idle.webp", align=(0.25, 0.5))
            #idle_foreground Solid('#F777', xysize=(36,72), align=(0.25, 0.5))
            hover_foreground Image ("images/gallery/gThumbs/g_d_next_hover.webp", align=(0.25, 0.5))

            action gallery.Next(unlocked=gallery.unlocked_advance)


# Screens ready for Replay and Music galleries

screen gallery_replay():

    fixed:

        # TODO: Translate
        text _("Under Construction") align (0.5, 0.5)


screen gallery_music():

    fixed:

        # TODO: Translate
        text _("Under Construction") align (0.5, 0.5)