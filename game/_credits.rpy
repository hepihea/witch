## Credits

transform c_parriba:
    subpixel True
    yalign 0.0
    pause 2.0
    linear 200 yalign 1.0  # 30 segundos en total

style c_styleTitle:
    font "fonts/whatever it takes.ttf"
    bold True
    size 20
    xalign 0.5
    outlines [ (0.5, "#303", 0, 1) ]

style c_styleCredits:
    font "fonts/whatever it takes.ttf"
    size 35
    xalign 0.5
    text_align 0.5
    outlines [ (0.7, "#303", 0, 1) ]


default c_spaceNum = 60

screen c_creditos():
    #add "#000"  # Fondo negro
    vbox at c_parriba:
        xfill True

        # DIRECTOR
        null height 600  # 1080 píxeles vacíos para empezar con la página vacía
        text _("Creador-Guionista-Programador-Artista").upper() style "c_styleTitle"
        text ("""I don't clean myself (aka: Jonnymelabo)
        """) style "c_styleCredits"
        null height c_spaceNum  # 300 px de espacio vacío

        # MUSIC
        text _("Música").upper() style "c_styleTitle"
        text ("""Alcaknight
Kevin MacLeod
        """) style "c_styleCredits"
        null height c_spaceNum  # 300 px de espacio vacío

        # ART- PROGRAMMING

        text _("Asistente principal en el arte").upper() style "c_styleTitle"
        text ("""Javier Martínez
        """) style "c_styleCredits"
        null height c_spaceNum  # 300 px de espacio vacío


        text _("Otros asistentes en el arte").upper() style "c_styleTitle"
        text ("""Noix
Faeydawn
graphic--Ops
Rockmor
        """) style "c_styleCredits"
        null height c_spaceNum  # 300 px de espacio vacío


        text _("Principal artista de fondo").upper() style "c_styleTitle"
        text ("""Ombobon
        """) style "c_styleCredits"
        null height c_spaceNum  # 300 px de espacio vacío

        text _("Otros artistas de fondo").upper() style "c_styleTitle"
        text ("""Kerim Akyuz
        """) style "c_styleCredits"
        null height c_spaceNum  # 300 px de espacio vacío


        text _("Ayuda en programación").upper() style "c_styleTitle"
        text ("""DragonHP
Xavimat
Matalla
Neyunse
GameForge
Titutitech

Renpy-Español Discord
Ren'py Discord
LemmaSoft Forum
        """) style "c_styleCredits"
        null height c_spaceNum  # 300 px de espacio vacío


        text _("Revisión del texto en Español").upper() style "c_styleTitle"
        text ("""Letropía
        """) style "c_styleCredits"
        null height c_spaceNum  # 300 px de espacio vacío

        text _("Traducción al inglés a lo largo de los años").upper() style "c_styleTitle"
        text ("""DoubleMoth
Gamma
Ras Alaghe
Nyrreah
Nesherius Gaming
Jeremy Johnson
Robert M.
Dario H.
Grímur Kamban
IancuAndIuliana
StormX
Yvonne Chimmy
        """) style "c_styleCredits"
        null height c_spaceNum  # 300 px de espacio vacío

        text _("Alfa Testers originales").upper() style "c_styleTitle"
        text ("""Xavi F.
Neus G.
Neyebur A.
Lord Bonnie
Animaster Tresmil
Rubén C.
Jacobo P.
Dina T.
Avril G.
Gonzálo G.
Irene V.
Rafael V.
Jorge M.
Elisabet X.

Sorry if I forgot someone.
        """) style "c_styleCredits"
        null height c_spaceNum  # 300 px de espacio vacío
        text _("Patrons").upper() style "c_styleTitle"

        text ""

## Patrons over 500$
        text _("Legends").upper() style "c_styleTitle"

        text ("""FallenCypher
Nick Cave
KOOLAID
CHRIS Dibbs
Robert(Ermine)Silver
Erok
MP
MeCL
Novamarauder
Harem Heroes
srusnak102
Tyler Tamse
Allen Berg
Bruce McMinn
E Esco
Ruefaust
        """) style "c_styleCredits"
        null height c_spaceNum  # 300 px de espacio vacío

## Patrons over 200$
        text _("Unbelivable").upper() style "c_styleTitle"

        text ("""FallenCypher
Nick Cave
KOOLAID
CHRIS Dibbs
Robert(Ermine)Silver
Erok
MP
MeCL
Novamarauder
Harem Heroes
srusnak102
Tyler Tamse
Allen Berg
Bruce McMinn
E Esco
Ruefaust
        """) style "c_styleCredits"
        null height c_spaceNum  # 300 px de espacio vacío

## Patrons over 100$
        text _("Amazing").upper() style "c_styleTitle"

        text ("""FallenCypher
Nick Cave
KOOLAID
CHRIS Dibbs
Robert(Ermine)Silver
Erok
MP
MeCL
Novamarauder
Harem Heroes
srusnak102
Tyler Tamse
Allen Berg
Bruce McMinn
E Esco
Ruefaust
        """) style "c_styleCredits"
        null height c_spaceNum  # 300 px de espacio vacío

        text _("Discord Fans").upper() style "c_styleTitle"
        text ("""Souta
SlayerWitcher
Staffie85
No One Of Consequence
maplesweet
shamanwolf
JDapiro
Pandemonium
Nehehyr

GregBold
Ryki
CL
arthur morgan
Sebas
Suntacasa
Akat (fatcheckarmenia.com)
Melon
2501
Booyah!_72
The DAHAKA
fosfoglicerato quinasa xd
Limba
MolotvKiller
Zecausso
KingOfClubs
ash12345
Rukkard
DuoNineXcore
M4 Sopmod II
Aaron
Mufaso
Knives The Sadistic Dragon
ernest
new account ernest//1276
Neyunse
        """) style "c_styleCredits"
        null height c_spaceNum  # 300 px de espacio vacío

        text _("Agradecimientos").upper() style "c_styleTitle"
        text ("""Antonia M.
Joan M. C.
        """) style "c_styleCredits"

        text _("Agradecimiento especial").upper() style "c_styleTitle"
        text ("""Óscar M.
        """) style "c_styleCredits"
        
        null height c_spaceNum  # 300 px de espacio vacío
        null height c_spaceNum  # 300 px de espacio vacío

        text _("Motor gráfico").upper() style "c_styleTitle"
        text ("""Ren'py versión: [renpy.version_only]
        """) style "c_styleCredits"
        null height c_spaceNum  # 300 px de espacio vacío



        null height 600  # Un últimoo null para que quede la pantalla vacía

    add "darkness_b01" at c_darkness

transform c_darkness:
    zoom 0.5
    alpha 0.0
    easein 2.0 alpha 1.0

# screen c_title_screen():
#     #add "#000"  # Fondo negro
#     vbox at c_parriba:
#         xfill True

image pwaw_title_light = "images/startmenu/pwaw_title_light.webp"
image pwaw_title_dark = "images/startmenu/pwaw_title_dark.webp"

image pwaw_title_comp:

    contains:
        "pwaw_title_dark"
        truecenter
        alpha 0.0
        easeout_quad 5.0 alpha 1.0
        pause 3.0
        easein_quad 5.0 alpha 0.0

    contains:
        "pwaw_title_light"
        truecenter
        additive 0.3
        alpha 0.0
        easeout_expo 5.0 alpha 1.0
        pause 3.0
        easein_expo 5.0 alpha 0.0 additive 0.0

label c_title:

    hide screen Points_PedreraSex
    hide screen Points
    hide screen quick_menu

    scene black
    with fade_long1s

    show pwaw_title_comp:
        truecenter
        zoom 0.2

    pause 13.0

    return

label credits_label:

    # hide screen Points_PedreraSex
    # hide screen Points
    # hide screen quick_menu

    pause 1.0

    show screen c_creditos
    with dissolve

    pause 1.0
    return  
