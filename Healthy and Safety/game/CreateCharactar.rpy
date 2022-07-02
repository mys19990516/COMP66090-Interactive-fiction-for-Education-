init:
    default expression = 1
    default hairstyle = 1
    default hair_color = "Dark"
    default costume = 1
    default acc = 1
    


image player f= Composite(
    (300, 600),
    (600, -208), "Create 2/Hair/Style[hairstyle]_[hair_color].png",
    (1313, 350), "Create 2/Expressions/Expression[expression].png",
    (600, -210), "Create 2/Costume/cos[costume].png",
    (600, -220), "Create 2/Accessories/acc[acc].png",
)
# layeredimage keri:
#
#     always:
#         "Create 1/Hair/Style1_Blond.png"
#     always:
#         "Create 1/Costume/cos1.png"
#         pos(300,600)
#
#
#     group mouth:
#
#         attribute happy default:
#             "Create 1/Expressions/Expression1.png"
#
#         attribute angry:
#             "Create 1/Expressions/Expression2.png"
#
#         attribute talk:
#             "Create 1/Expressions/Expression3.png"





screen create_female():

    $gender=2

    modal True

    imagemap:
        ground "Dressup_Screen/background.png"
        idle "Dressup_Screen/idle.png"
        hover "Dressup_Screen/hover.png"
        selected_idle "Dressup_Screen/selected.png"
        selected_hover "Dressup_Screen/selected.png"

        hotspot(268, 112, 77, 77) action SetVariable("expression", 1)
        hotspot(365, 112, 77, 77) action SetVariable("expression", 2)
        hotspot(463, 112, 77, 77) action SetVariable("expression", 3)
        hotspot(560, 112, 77, 77) action SetVariable("expression", 4)
        hotspot(655, 112, 77, 77) action SetVariable("expression", 5)

        ##Hairstyle##
        hotspot(268, 233, 77, 77) action SetVariable("hairstyle", 1)
        hotspot(365, 233, 77, 77) action SetVariable("hairstyle", 2)
        hotspot(463, 233, 77, 77) action SetVariable("hairstyle", 3)
        hotspot(560, 233, 77, 77) action SetVariable("hairstyle", 4)
        hotspot(655, 233, 77, 77) action SetVariable("hairstyle", 5)

        ##Hair Color##
        hotspot(268, 354, 77, 77) action SetVariable("hair_color", "Pink")
        hotspot(365, 354, 77, 77) action SetVariable("hair_color", "Dark")
        hotspot(463, 354, 77, 77) action SetVariable("hair_color", "Brown")
        hotspot(560, 354, 77, 77) action SetVariable("hair_color", "Silver")
        hotspot(655, 354, 77, 77) action SetVariable("hair_color", "Blond")

        ##Costume##
        hotspot(268, 450, 77, 77) action SetVariable("costume", 1)
        hotspot(365, 450, 77, 77) action SetVariable("costume", 2)
        hotspot(463, 450, 77, 77) action SetVariable("costume", 3)
        hotspot(560, 450, 77, 77) action SetVariable("costume", 4)
        hotspot(655, 450, 77, 77) action SetVariable("costume", 5)

        ##Accessori##
        hotspot(268, 540, 77, 77) action SetVariable("acc", 1)
        hotspot(365, 540, 77, 77) action SetVariable("acc", 2)
        hotspot(463, 540, 77, 77) action SetVariable("acc", 3)
        hotspot(560, 540, 77, 77) action SetVariable("acc", 4)
        hotspot(655, 540, 77, 77) action SetVariable("acc", 5)

        ##Continue##
        hotspot(1600,30, 350, 180) action Return()

    add "player f":
        pos(600, 80)
        zoom 0.5

image player m= Composite(
        (300, 600),
        (-90, -208), "Create 1/Hair/Style[hairstyle]_[hair_color].png",
        (303, 222), "Create 1/Expressions/Expression[expression].png",
        (-17, 497), "Create 1/Costume/cos[costume].png",
        (-115, -260), "Create 1/Accessories/acc[acc].png",

)

screen create_male():
    modal True

    imagemap:
        ground "Dressup_Screen/background.png"
        idle "Dressup_Screen/idle.png"
        hover "Dressup_Screen/hover.png"
        selected_idle "Dressup_Screen/selected.png"
        selected_hover "Dressup_Screen/selected.png"

        ##Expression##
        hotspot(268, 112, 77, 77) action SetVariable("expression", 1)
        hotspot(365, 112, 77, 77) action SetVariable("expression", 2)
        hotspot(463, 112, 77, 77) action SetVariable("expression", 3)
        hotspot(560, 112, 77, 77) action SetVariable("expression", 4)
        hotspot(655, 112, 77, 77) action SetVariable("expression", 5)

        ##Hairstyle##
        hotspot(268, 233, 77, 77) action SetVariable("hairstyle", 1)
        hotspot(365, 233, 77, 77) action SetVariable("hairstyle", 2)
        hotspot(463, 233, 77, 77) action SetVariable("hairstyle", 3)
        hotspot(560, 233, 77, 77) action SetVariable("hairstyle", 4)
        hotspot(655, 233, 77, 77) action SetVariable("hairstyle", 5)

        ##Hair Color##
        hotspot(268, 354, 77, 77) action SetVariable("hair_color", "Red")
        hotspot(365, 354, 77, 77) action SetVariable("hair_color", "Dark")
        hotspot(463, 354, 77, 77) action SetVariable("hair_color", "Brown")
        hotspot(560, 354, 77, 77) action SetVariable("hair_color", "Silver")
        hotspot(655, 354, 77, 77) action SetVariable("hair_color", "Blond")

        ##Costume##
        hotspot(268, 450, 77, 77) action SetVariable("costume", 1)
        hotspot(365, 450, 77, 77) action SetVariable("costume", 2)
        hotspot(463, 450, 77, 77) action SetVariable("costume", 3)
        hotspot(560, 450, 77, 77) action SetVariable("costume", 4)
        hotspot(655, 450, 77, 77) action SetVariable("costume", 5)

        ##Accessori##
        hotspot(268, 540, 77, 77) action SetVariable("acc", 1)
        hotspot(365, 540, 77, 77) action SetVariable("acc", 2)
        hotspot(463, 540, 77, 77) action SetVariable("acc", 3)
        hotspot(560, 540, 77, 77) action SetVariable("acc", 4)
        hotspot(655, 540, 77, 77) action SetVariable("acc", 5)

        ##Continue##
        hotspot(1600,30, 350, 180) action Return()

    add "player m":
        pos(1400, 400)
        zoom 0.5
