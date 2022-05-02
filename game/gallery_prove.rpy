# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#     # PERSISTENTS
# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# init -1 python:
# # Image gallery unlocks

# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# # Empty slot placeholder
# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#     if persistent.emptyGSlot is None:
#         persistent.emptyGSlot = True
# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# # day 01
# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#     # Neus Bite Didac Hand.
#     if persistent.unlock_rape_neus_hand is None:
#         persistent.unlock_rape_neus_hand = False
#     # Neus Bite Didac Dick
#     if persistent.unlock_rape_neus_dick is None:
#         persistent.unlock_rape_neus_dick = False
#     # Neus Get Out
#     if persistent.unlock_rape_neus_out is None:
#         persistent.unlock_rape_neus_out = False
    

# init python:
#     if persistent.galleryPage is None:
#         persistent.galleryPage = '1'
    
#     class ImageGalleryItem(object):
#         def __init__(self, thumbnailImage, images, sceneName, lockCondition):
#             self.thumbnailImage = thumbnailImage
#             self.images = images
#             self.sceneName = sceneName
#             self.lockCondition = lockCondition

#         def isUnlocked(self):
#             return getattr(persistent, self.lockCondition, False)

#         def isNotAPlaceholder(self):
#             return self.images and self.isUnlocked()

#         def getThumbnail(self):
#             if self.isUnlocked():
#                 return self.thumbnailImage
#             else:
#                 return 'gThumb_wip'

#         def getSceneName(self):
#             if self.isUnlocked():
#                 return self.sceneName
#             else:
#                 return ''

#         def playimages(self):
#             if not self.images:
#                 return
#             for image in self.images:
#                 renpy.show(image, layer='screens', zorder=5)
#                 renpy.with_statement(dissolve)
#                 renpy.pause()
#                 renpy.hide(image, layer='screens')

#     # We need to create one more element in the page list than we actually need
#     # because of the way the fileslot pages work in Ren'Py
#     galleryPageCount = 4
#     imageGalleryPageCollection = [None] * galleryPageCount
#     # Keep the 0th element empty
#     imageGalleryPageCollection[0] = None

    # Gallery page 1
    # imageGalleryPageCollection[1] = [
    #     add g.make_button("rape_neus", 
    #         "gThumb_rape_neus_b", 
    #         "gThumb_wip", hover_border= 
    #         "gThumb_rape_neus", 
    #         xalign=0.0, yalign=0.0, xysize=(100,100))
    #     ImageGalleryItem('gThumb_wip', [], 'Number 01', 'persistent.emptyGSlot'),
    #     ImageGalleryItem('gThumb_wip', [], 'Prove 02', 'persistent.emptyGSlot'),
    #     ImageGalleryItem('gThumb_wip', [], 'Aerejé', 'persistent.emptyGSlot'),
    #     ImageGalleryItem('gThumb_wip', [], 'Ja', 'persistent.emptyGSlot'),
    #     ImageGalleryItem('gThumb_wip', [], 'Dje', 'persistent.emptyGSlot'),
    #     ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
    #     ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
    #     ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
    #     ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
    #     ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
    #     ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
    #     ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot')
    # ]

#     # Gallery page 2
#     imageGalleryPageCollection[2] = [
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot')
#     ]

#     # Gallery page 3
#     imageGalleryPageCollection[3] = [
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot'),
#         ImageGalleryItem('gThumb_wip', [], '', 'persistent.emptyGSlot')
#     ]


# ##################################################################
# ########################################################################
# ##################################################################
# ########################################################################
# ##################################################################
# ########################################################################
# ##################################################################
# ########################################################################
# ##################################################################
# ########################################################################

#     class ImageGalleryPage(Action, DictEquality):
#         def __init__(self, page):
#             self.page = str(page)

#         def __call__(self):
#             if not self.get_sensitive():
#                 return
#             persistent.galleryPage = self.page
#             renpy.restart_interaction()

#         def get_selected(self):
#             return self.page == persistent.galleryPage

#         def predict(self):
#             _predict_file_page(self.page)

#     class ImageGalleryNextPage(Action, DictEquality):
#         def __init__(self):
#             page = int(persistent.galleryPage)
#             if page < (len(imageGalleryPageCollection) - 1):
#                 page += 1

#             self.page = str(page)

#         def __call__(self):
#             if not self.get_sensitive():
#                 return

#             persistent.galleryPage = self.page
#             renpy.restart_interaction()

#         def get_sensitive(self):
#             return self.page is not None

#         def predict(self):
#             _predict_file_page(self.page)

#     class ImageGalleryPreviousPage(Action, DictEquality):
#         def __init__(self):
#             page = int(persistent.galleryPage)
#             if page > 1:
#                 page -= 1

#             self.page = str(page)

#         def __call__(self):
#             if not self.get_sensitive():
#                 return

#             persistent.galleryPage = self.page
#             renpy.restart_interaction()

#         def get_sensitive(self):
#             return self.page

#         def predict(self):
#             _predict_file_page(self.page)

#     def ImageGalleryPlay(slot):
#         imageGalleryPageCollection[int(persistent.galleryPage)][slot].playVideos()

#     def ImageGallerySceneName(slot):
#         if slot >= len(imageGalleryPageCollection[int(persistent.galleryPage)]):
#             return ''
#         return imageGalleryPageCollection[int(persistent.galleryPage)][slot].getSceneName()

#     def ImageGalleryThumbnail(slot):
#         # if slot >= len(imageGalleryPageCollection[int(persistent.galleryPage)]):
#         #     return Null()
#         return imageGalleryPageCollection[int(persistent.galleryPage)][slot].getThumbnail()


# label playGalleryImages(gallerySlot):
#     $ imageGalleryPageCollection[int(persistent.galleryPage)][gallerySlot].playVideos()

# label openImageGallery():
#     call screen imageGallery with dissolve
#     with dissolve

# screen imageGallery():
#     tag menu
#     use game_menu('Gallery'):
#         fixed:
#             order_reverse True
#             grid 4 3:
#                 style_prefix "slot"
#                 xalign 0.5
#                 yalign 0.5
#                 xpos 0.45
#                 ypos 0.4
#                 spacing 10
#                 for i in range(4 * 3):
#                     $ gallerySlot = i
#                     button:
#                         xsize 100
#                         action If(imageGalleryPageCollection[int(persistent.galleryPage)][gallerySlot].isNotAPlaceholder(), Call('playGalleryImages', gallerySlot), NullAction())
#                         has vbox
#                         add ImageGalleryThumbnail(gallerySlot)
#                         text ImageGallerySceneName(gallerySlot):
#                             style "slot_name_text"

#             hbox:
#                 style_prefix "page"
#                 xalign 0.5
#                 yalign 1.0
#                 spacing gui.page_spacing
#                 textbutton _("<") action ImageGalleryPreviousPage()
#                 for page in range(1, len(imageGalleryPageCollection)):
#                     textbutton "[page]" action  ImageGalleryPage(page)
#                 textbutton _(">") action ImageGalleryNextPage()
