# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.





image Missy Laugh =Composite(
      (100,300),
      (0,-650),"images/character/Missy/Missy-Laugh.png"
)
image Missy Grin =Composite(
      (100,300),
      (0,-650),"images/character/Missy/Missy-Grin.png"
)
image Missy Normal =Composite(
      (100,300),
      (0,-650),"images/character/Missy/Missy-Normal.png"
)
image Missy Rage =Composite(
      (100,300),
      (0,-650),"images/character/Missy/Missy-Rage.png"
)
image Missy Smile =Composite(
      (100,300),
      (0,-650),"images/character/Missy/Missy-Smile.png"
)
image Missy Surprise =Composite(
      (100,300),
      (0,-650),"images/character/Missy/Missy-Surprise.png"
)
image Missy Mad =Composite(
      (100,300),
      (0,-650),"images/character/Missy/Missy-Mad.png"
)
image Missy Sad =Composite(
      (100,300),
      (0,-650),"images/character/Missy/Missy-Sad.png"
)

image player_a  = Composite(
    (300, 600),
    (-90, -208), "Create 1/Hair/Style1_Dark.png",
    (303, 222), "Create 1/Expressions/Expression5.png",
    (-17, 497), "Create 1/Costume/cos1.png",
    (-115, -260), "Create 1/Accessories/acc1.png",

)

# # The game starts here.

default IsInputname = False
define mys = Character("Mys",image="player_a")
define Missy = Character("Missy",image="missy")
define Kevin = Character("Kevin")
define povname = "Messi"
define Mys = Character("[povname]",image="player_a")
define Security = Character("Security")
define Supervisor = Character("Supervisor")


image purple:
    "#BB143B"
image logo2:
    contains:
        "images/scene/uom-logo.png"
        truecenter

transform c1:
    pos(700, 250)
    zoom 0.5

transform c2:
    pos(250, 170)
    zoom 0.5

transform s:
    pos(200, 170)
    zoom 0.5

transform fl:
    zoom 0.5
    xalign -0.5 yalign 0.25
    linear 0.5 xalign -0.2

transform ml:
    zoom 0.5
    xalign 0.0 yalign 0.35
    linear 0.5 xalign 0.1

transform x:
    zoom 0.5
    xalign 0.2 yalign 0.35

init:
    transform speaking:
        linear 0.05  xoffset 6
        linear 0.05  xoffset -8
        linear 0.05  xoffset -6
        linear 0.05  xoffset 8
        linear 0.05  xoffset -6
        linear 0.05  xoffset 8
        linear 0.05  xoffset -6
        linear 0.05  xoffset 8
        linear 0.05  xoffset -6
        linear 0.05  xoffset 8
        linear 0.05  xoffset -6
        linear 0.05  xoffset 8
        linear 0.05  xoffset -6
        linear 0.05  xoffset 8
        linear 0.05  xoffset -6
        linear 0.05  xoffset 8

    transform shaking:
        linear 0.1  yoffset 6
        linear 0.1  yoffset -8
        linear 0.1  yoffset -6
        linear 0.1  yoffset 8
        linear 0.1  yoffset 0

    default player = 1
    default gender = 1
    default isMale = True

init python:

    def showplayercenter():
        if isMale:

            renpy.show("player m",at_list=[c1])
        else:
            renpy.show("player f",at_list=[c2])

    def showplayer():
        if isMale:

            renpy.show("player m",at_list=[ml])
        else:
            renpy.show("player f",at_list=[fl])

    def hideplayer():
        if isMale:

            renpy.hide("player m")
        else:
            renpy.hide("player f")


# label before_main_menu:
#     scene purple
#     show logo2
#     with dissolve
#     $ renpy.pause(2.0, hard=True)
#     hide logo2
#     with dissolve
#
#     return
label start:

    # scene white
    # with fade
    #
    # show text "Welcome to Health and Safety Education Interactive Fiction"
    # pause
    #
    # show text "Congratulations on your coming to the University of Manchester Computer Science!"
    # pause
    # show text "The University of Manchester is a world-renowned university"
    # pause
    # show text "Getting into the University of Manchester is proof that you are a very good student."
    # pause
    # show text "As a world-renowned university, the University of Manchester takes the health and safety of its students very seriously"
    # pause
    # show text "so teaching them something about health and safety is essential."
    # pause
    # show text "You will play the Health and Safety Education interactive fiction game"
    # pause
    # show text "explore the plot and learn about health and safety."
    # pause

    scene bg university
    with fade

    # python:
    #
    #    povname=renpy.input("First of all, please give your character a personalized name,")
    #    len_name = int(len(povname))
    #    if len_name != 0:
    #        IsInputname = True
    #        "Very good! [povname] sounds great"
    #    else:
    #
    #        povname= "Messi"
    #        "It doesn't look like you want to give yourself a name. Nevermind, we gave you a name: Messi"
    #
    #
    # if IsInputname:
    #
    #        "Very good! [povname] sounds great"
    # else:
    #        "It doesn't look like you want to give yourself a name. Nevermind, we gave you a name: Messi"
    #
    # "[povname], choose an image you like next."
    menu:
        #"[povname], choose an image you like next."
        "I want to choose a male.":

            call screen create_male
            $showplayercenter()
            "Nice look!"
        "I want to choose a female.":
            $isMale=False

            call screen create_female
            $showplayercenter()
            "Nice look!"
        "I don't want to choose.":

            $showplayercenter()

            "No worries. We created the character for you"


    # "Your best friend, Kevin, has also been accepted to the University of Manchester"
    # show kevin:
    #     zoom 0.5
    #     xalign 1.0 yalign 0.35
    #     linear 0.5 xalign 0.9
    # "You will spend your time with him at the University of Manchester!"
    #
    #
    # "On the first day of school, you attended a freshers' meeting with Kevin, where you met Missy, the head of your major."
    # hide kevin
    # scene bg classroom
    # with dissolve
    # show Missy Smile at center:
    #      xalign 1.0
    #      linear 0.5 xalign 0.7
    #
    #
    # # These display lines of dialogue.
    #
    #
    # Missy "Hello everyone! Welcome to Computing at the University of Manchester, I am Missy, your cohort advisor."
    # Missy "I will be responsible for your health and safety, behaviour and academic performance during your time at the University."
    # Missy "Please think of me as your friend! If you want to chat, I'm happy to listen and my office is always open for you!"
    #
    # $showplayer()
    #
    # Mys "Wow!, nice to see you!!!"
    #
    # $hideplayer()
    #
    # hide Missy Smile
    #
    # show Missy Laugh at center:
    #     xalign 0.7
    #
    # Missy "Nice to see you, too!!"
    #
    # hide Missy Laugh
    #
    # show Missy Normal at center:
    #     xalign 0.7
    #
    # Missy "First, let's talk about health and safety at university."
    # Missy "A university is a large, complex organisation. Universities are densely populated."
    # Missy "Except teachers and students. There are numerous staffs, researchers in university."
    # Missy "In addition, universities often have a lot of expensive laboratory equipment and dangerous items (chemicals, biological viruses)"
    # Missy "which can often result in injuries and property damage in the event of a safety incident"
    # Missy "Our staffs and students often carry out an extremely wide range of activities, do you think it is possible to provide a risk-free environment?"
    # Missy "I would like to pick one person to answer this question. ......mys,thanks for the compliment. You seem to be very active.Can you answer my question?"
    #
    # menu:
    #     "Impossible":
    #
    #         Missy "You are right, because some activities will involve new or different or unpredictable risks."
    #     "Possible":
    #
    #         Missy "Oops, wrong answer. It is impossible to create a risk-free environment."
    #         Missy "Because some of these activities involve new or different or unpredictable risks."
    #
    # Missy "So it is important that you understand the risks associated with your work and how to deal with them."
    #
    # Missy "Before you go ahead, we will tell you the results of the risk assessment, give you information on what you can do to keep yourself and others safe."
    # Missy "Please make sure you read the information and make good use of it, as it can sometimes be crucial."
    # Missy "It is possible that we may have missed certain risks."
    # Missy "So if you find a vulnerability, please do report it to me or to the security department"
    # Missy "We would be very grateful for any suggestions you may have. This will help us to improve our measures to better protect students and staff."
    # Missy "Remember to always follow the usage instructions we have set out when carrying out activities."
    # Missy "These instructions are effective in protecting your life and property and that of others."
    # Missy "If you are injured in an accident, we have trained first aiders."
    # Missy "You can find their details in the First Aid notices at the entrance to the building."
    # Missy "Like this."
    #
    # show contact:
    #     pos(800, 180)
    #
    # Missy "If you are in a serious medical emergency, call Security immediately, because Security can help direct the ambulance to you."
    # Missy "Finally, if you are unsure about anything, please do ask questions. Okay, now does anyone have any questions?"
    #
    # hide contact
    #
    # $showplayer()
    #
    # Mys "I have a problem!"
    # Missy "Very good, mys, please ask your questions."
    # Mys "What is the number to call for an ambulance, please?"
    # Missy "I'm sorry I forgot that the University of Manchester is an internationally renowned university, "
    # Missy "so there will be a lot of foreign students coming to study. These foreign students are not very familiar with the UK."
    # Missy "In the UK, the number to call for an ambulance is 999."
    # Mys "Thank you!"
    # Missy " My pleasure."
    # Missy " Okay, any more questions?"
    # "......"
    # Missy "I guess there's none, so next I'll talk about the study......"
    #
    # hide Missy Normal
    #
    # show kevin at center:
    #     zoom 0.5
    #     xalign 1.0 yalign 0.42
    #     linear 0.5 xalign 0.7
    #
    # Kevin "What did supervisor say just now, I was watching TikTok and didn't hear it, hahaha"
    #
    # Mys "She just spoke about health and safety, do you need me to repeat that for you?"
    #
    # Kevin "No hahaha, I don't think I need to know that at university, it's safe, I'm gonna go back to the TikTok"
    #
    # Mys "Well, I'll go on listening to Missy then, I think you'd better listen to it."
    #
    # Kevin "It's ok, I think TikTok is more interesting than the supervisor's speech, hahaha"
    #
    # hide kevin
    #
    # $hideplayer()
    #
    # "After the freshman meeting, your college life officially begins"

    jump first_chapter



    return
