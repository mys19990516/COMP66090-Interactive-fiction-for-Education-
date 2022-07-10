init python:

    timeout_label = False
    score1=0
    isshake=False
    q1=False
    q2=False
    q3=False

    def scoring1(mark):

        global score1

        score1+=mark

        if score1>=200:
            score1=0

        return score1


label chapter3:

    # scene white
    # with fade
    #
    # show text "Summer vacation time is always fast, a new semester has arrived."
    # pause
    #
    # show text "It is customary for Missy to give a meeting to all students on the first day of the new term."
    # pause
    #
    # scene bg classroom
    # with dissolve
    #
    # show Missy Normal at center:
    #     xalign 0.8
    #
    # Missy "Hello everyone, I hope all of you had a great holiday."
    # Missy "Most people should have been restricted from travelling due to the covid-19."
    # Missy "However, with the improvement of the epidemic,"
    # Missy "travel restrictions have all been canceled for the new term!"
    # Missy "In the new semester, to make up for not travelling in the summer vacation."
    # Missy "The university offers an exchange programme for our majors."
    # Missy "All students are welcome!"
    # Missy "You will go to universities around the world for 3 months of study."
    # Missy "All students are welcome to sign up!"
    #
    # hide Missy
    #
    # $showplayer()
    #
    # show kevin:
    #     zoom 0.5
    #     xalign 1.0 yalign 0.35
    #     linear 0.5 xalign 0.7
    #
    # Kevin "Do you want to participate?"
    #
    # menu:
    #     "No, I don't":
    #         Mys "I prefer to stay in our school."
    #         Kevin "Come on! It's gonna be fun. We can experience cultures from other places."
    #         Mys "OK!"
    #     "Yes, I want":
    #         Mys "I would love to participate!"
    #         Mys "It was always my dream to go to Von Neumann University (the best computer university in the world)."
    #         Kevin "Then let's go!"
    #
    #
    #
    # hide kevin
    # $hideplayer()
    #
    # show Missy Normal at center:
    #     xalign 0.8
    #
    # Missy "I've already heard from some students said they really want to go."
    # Missy "But before you sign up, I would like to remind you about the safety about the placement."
    #
    # $showplayer()
    #
    #
    # Mys "I have a questions."
    #
    # show Missy Laugh at center:
    #     xalign 0.8
    # Missy "I am happy to answer them."
    #
    # menu question:
    #     "what is a placement?":
    #         $q1=True
    #         Mys "What is a placement?"
    #         Missy "Placement involves transferring your supervision to a third party placement provider who is usually said to be another organisation."
    #         Missy "It is clear that exchange learning is a placement."
    #         jump question
    #
    #     "What should I do to attend?":
    #         $q2=True
    #         Mys "What should I do to attend?"
    #         Missy "Many of the school's activities are part of the placement."
    #         Missy "If the activity is a placement, you must apply to the school and wait for its approval."
    #         Mys "If the school doesn't approve me to attend, "
    #         Mys "or if I don't submit an application, can I still attend?"
    #         Missy "Then you can't take part, so please remember to always submit an application! "
    #         Missy "So you need to be able to discern what activities are placements."
    #
    #         jump question
    #
    #     "What do I need to be aware of regarding the safety of placement?":
    #         $q3=True
    #         Mys "What do I need to be aware of regarding the safety of placement?"
    #         Missy "The safety of our students is always our primary concern, even when your supervision is diverted."
    #
    #         Missy "There are three main stages of security in resettlement: before, during and after resettlement."
    #         Missy "The main thing that schools may ask you to provide after placement is reports on standard templates or electronic questionnaires."
    #         Missy "Or the school may ask you to share your experiences for the following year's students."
    #         Missy "The focus of placement safety is pre and post placement."
    #
    #         Missy "Before placing, you first need to consider the practicality of the placement."
    #         Missy "Practicality means do you need a visa or other travel document? "
    #         Missy "Is your passport valid?"
    #         Missy "Will you have enough money to cover the costs of your placement,"
    #         Missy "and will you be able to access additional funds in case of an emergency? "
    #         Missy "Considering all of these will help ensure that everything you need is in place before you leave our university."
    #
    #         Missy "You then need to consider the risks in 6 ways. "
    #         Missy "Your work, your travel and transport, your location or area, your general and environmental health."
    #         Missy "Your personal traits, characteristics, abilities and your insurance arrangements."
    #
    #         Missy "In placement, -you should be in regular contact with your workplace supervisor."
    #         Missy "Communicate with your school on a regular basis."
    #         Missy "You should also establish emergency contact arrangements."
    #
    #         jump question
    #
    #     "OK, I don't have question now." if q1 and q2 and q3:
    #
    #         Mys "OK, I don't have question now."
    #
    #         Missy "All right. Please come to me and apply now"
    #
    #         "After missy, you and kevin signd up for the event."
    #
    #         Kevin "[povname], I have some question about these."
    #         Kevin "Can you help me?"
    #         Mys "Sure!"
    #         Missy "I am also here for you, Kevin. To prevent [povname] from giving you wrong answers."



label exam:
    scene bg exam
    with fade

    show kevin:
        zoom 0.5
        xalign 1.0 yalign 0.35
        linear 0.5 xalign 0.9

    $timeout_label = True
    $showscore=True
label q1:

    $score1=0

    $ timeout_label = "q2"

    if isshake:
        with hpunch
        $isshake=False
    menu:
        Kevin "The school has arranged for me to carry out relevant experiments in the laboratory of a chemical company. Is this the right event for me?"

        "Incorrect":
            $showplayer()

            Mys "That's incorrect. Because we are computer science students, it is very dangerous to do chemistry experiments without training."
            Mys "We need to consider the risks at your job. "
            Mys "They include the nature of the work hazards you may be exposed to, "
            Mys "such as sharp objects, tools, hazardous chemicals or potentially dangerous people or animals."
            $hideplayer()

            $scoring1(8.34)

            Kevin "Which aspect does this belong to?"

            menu:

                "Your work":

                    $scoring1(8.34)

                "Your travel and transport":
                    with hpunch

                    $scoring1(0)

                "Your location or region":
                    with hpunch

                    $scoring1(0)

                "Your general and environmental health":
                    with hpunch

                    $scoring1(0)

                "Your personal traits, characteristics, abilities":
                    with hpunch

                    $scoring1(0)

                "Your insurance arrangements":
                    with hpunch

                    $scoring1(0)

        "Correct":
            with hpunch

            show Missy Normal at center:
                xalign 0.2

            Missy "[povname],your are wrong. Because we are computer science students, it is very dangerous to do chemistry experiments without training."
            Missy "We need to consider the risks at your job. "
            Missy "They include the nature of the work hazards you may be exposed to, "
            Missy "such as sharp objects, tools, hazardous chemicals or potentially dangerous people or animals."

            Missy "Which aspect does this belong to?"

            hide Missy Normal
            menu:
                "Your work":

                    $scoring1(8.34)

                "Your travel and transport":
                    with hpunch

                    $scoring1(0)

                "Your location or region":
                    with hpunch

                    $scoring1(0)

                "Your general and environmental health":
                    with hpunch

                    $scoring1(0)

                "Your personal traits, characteristics, abilities":
                    with hpunch

                    $scoring1(0)

                "Your insurance arrangements":
                    with hpunch

                    $scoring1(0)

label q2:

    if isshake:
        with hpunch
        $isshake=False

    $ timeout_label = "q3"
    menu:


        Kevin "I found I have to pass an intersection with no traffic lights and a lot of vehicles from my hostel to placement everyday, and I can only choose to walk or cycle to the placement."

        "Incorrect":

            $showplayer()

            Mys "That's incorrect. Intersections without traffic lights are very dangerous and there is a high risk of traffic accidents."

            Mys "Depending on the nature and location of the placement, "
            Mys "you may also face significant health, safety and welfare issues associated with travelling to and from the placement and to and from your accommodation."
            Mys "You should consider the hazards and benefits of different types of public transport, self-driving, walking or cycling."
            $hideplayer()
            Kevin "Which aspect does this belong to?"

            $scoring1(8.34)

            menu:
                "Your work":
                    with hpunch
                    $scoring1(0)

                "Your travel and transport":
                    $scoring1(8.34)


                "Your location or region":
                    with hpunch

                    $scoring1(0)

                "Your general and environmental health":
                    with hpunch

                    $scoring1(0)

                "Your personal traits, characteristics, abilities":
                    with hpunch

                    $scoring1(0)

                "Your insurance arrangements":
                    with hpunch

                    $scoring1(0)

        "Correct":
            with hpunch

            show Missy Normal at center:
                xalign 0.2

            Missy "[povname] is wrong. Intersections without traffic lights are very dangerous and there is a high risk of traffic accidents."

            Missy "Depending on the nature and location of the placement, "
            Missy "you may also face significant health, safety and welfare issues associated with travelling to and from the placement and to and from your accommodation."
            Missy "You should consider the hazards and benefits of different types of public transport, self-driving, walking or cycling."

            Missy "Which aspect does this belong to?"

            hide Missy Normal

            menu:
                "Your work":
                    with hpunch

                    $scoring1(0)

                "Your travel and transport":

                    $scoring1(8.34)


                "Your location or region":
                    with hpunch

                    $scoring1(0)

                "Your general and environmental health":
                    with hpunch

                    $scoring1(0)

                "Your personal traits, characteristics, abilities":
                    with hpunch

                    $scoring1(0)

                "Your insurance arrangements":
                    with hpunch

                    $scoring1(0)
label q3:

    if isshake:
        with hpunch
        $isshake=False

    $ timeout_label = "q4"
    menu:

        Kevin "The country I will visit is more resistant to black clothing, so I should leave my black clothes at home."

        "Incorrect":
            with hpunch

            show Missy Normal at center:
                xalign 0.2

            Missy "[povname] is wrong. Knowing the culture of the country in advance is the right thing to do."

            Missy "The location of the placement can have a considerable impact, "
            Missy "especially if it is located in an area or country/region that you are unfamiliar with."
            Missy "You should also be aware of the local culture. "
            Missy "For example, to understand which standards of dress and behaviour are acceptable and which may cause offence."

            Missy "Which aspect does this belong to?"

            hide Missy Normal

            menu:
                "Your work":
                    with hpunch
                    $scoring1(0)


                "Your travel and transport":
                    with hpunch
                    $scoring1(0)

                "Your location or region":
                    $scoring1(8.34)

                "Your general and environmental health":
                    with hpunch
                    $scoring1(0)

                "Your personal traits, characteristics, abilities":
                    with hpunch
                    $scoring1(0)

                "Your insurance arrangements":
                    with hpunch
                    $scoring1(0)

        "Correct":
            $scoring1(8.34)
            $showplayer()

            Mys "That's correct. Knowing the culture of the country in advance is the right thing to do."

            Mys "The location of the placement can have a considerable impact, "
            Mys "especially if it is located in an area or country/region that you are unfamiliar with."
            Mys "You should also be aware of the local culture. "
            Mys "For example, to understand which standards of dress and behaviour are acceptable and which may cause offence."

            $hideplayer()

            Kevin "Which aspect does this belong to?"

            menu:
                "Your work":
                    with hpunch
                    $scoring1(0)

                "Your travel and transport":
                    with hpunch
                    $scoring1(0)

                "Your location or region":
                    $scoring1(8.34)

                "Your general and environmental health":
                    with hpunch
                    $scoring1(0)

                "Your personal traits, characteristics, abilities":
                    with hpunch
                    $scoring1(0)

                "Your insurance arrangements":
                    with hpunch
                    $scoring1(0)

label q4:

    if isshake:
        with hpunch
        $isshake=False

    $ timeout_label = "q5"
    menu:
        Kevin "Before I go, I should search for information about the local area. Find out about the local climate food habits, etc."

        "Incorrect":
            with hpunch

            show Missy Normal at center:
                xalign 0.2

            Missy "[povname] is wrong. You should get to know the local conditions and daily life before you go."

            Missy "You may face significant health, safety and welfare issues related to the environmental conditions in your workplace or general location, your accommodation or your food and drink."
            Missy "Consider the prevailing climate, look for reviews about where you will be staying."
            Missy " and try to find advice on where to eat and where to avoid."

            Missy "Which aspect does this belong to?"

            hide Missy Normal

            menu:
                "Your work":
                    with hpunch
                    $scoring1(0)

                "Your travel and transport":
                    with hpunch
                    $scoring1(0)

                "Your location or region":
                    with hpunch
                    $scoring1(0)

                "Your general and environmental health":
                    $scoring1(8.34)

                "Your personal traits, characteristics, abilities":
                    with hpunch
                    $scoring1(0)

                "Your insurance arrangements":
                    with hpunch
                    $scoring1(0)

        "Correct":
            $scoring1(8.34)
            $showplayer()

            Mys "That's correct. You should get to know the local conditions and daily life before you go."

            Mys "You may face significant health, safety and welfare issues related to the environmental conditions in your workplace or general location, your accommodation or your food and drink."
            Mys "Consider the prevailing climate, look for reviews about where you will be staying."
            Mys " and try to find advice on where to eat and where to avoid."
            $hideplayer()
            Kevin "Which aspect does this belong to?"

            menu:
                "Your work":
                    with hpunch
                    $scoring1(0)

                "Your travel and transport":
                    with hpunch
                    $scoring1(0)

                "Your location or region":
                    with hpunch
                    $scoring1(0)

                "Your general and environmental health":
                    $scoring1(8.34)

                "Your personal traits, characteristics, abilities":
                    with hpunch
                    $scoring1(0)

                "Your insurance arrangements":
                    with hpunch
                    $scoring1(0)


label q5:

    if isshake:
        with hpunch
        $isshake=False

    $ timeout_label = "q6"
    menu:
        Kevin "I need to make yourself more independent and stronger before I go."

        "Incorrect":
            with hpunch

            show Missy Normal at center:
                xalign 0.2

            Missy "[povname] is wrong. Our personalities always have a huge impact."

            Missy "Your personal health, knowledge, skills, experience and personality may have an impact on your health and safety in a particular environment."

            Missy "Which aspect does this belong to?"

            hide Missy Normal
            menu:
                "Your work":
                    with hpunch
                    $scoring1(0)

                "Your travel and transport":
                    with hpunch
                    $scoring1(0)

                "Your location or region":
                    with hpunch
                    $scoring1(0)

                "Your general and environmental health":
                    with hpunch
                    $scoring1(0)

                "Your personal traits, characteristics, abilities":
                    $scoring1(8.34)

                "Your insurance arrangements":
                    with hpunch
                    $scoring1(0)

        "Correct":
            $scoring1(8.34)
            $showplayer()

            Mys  "That's right. Our personalities always have a huge impact."

            Mys "Your personal health, knowledge, skills, experience and personality may have an impact on your health and safety in a particular environment."

            $hideplayer()

            Kevin "Which aspect does this belong to?"

            menu:
                "Your work":
                    with hpunch
                    $scoring1(0)

                "Your travel and transport":
                    with hpunch
                    $scoring1(0)

                "Your location or region":
                    with hpunch
                    $scoring1(0)

                "Your general and environmental health":
                    with hpunch
                    $scoring1(0)

                "Your personal traits, characteristics, abilities":
                    $scoring1(8.34)

                "Your insurance arrangements":
                    with hpunch
                    $scoring1(0)
label q6:

    if isshake:
        with hpunch
        $isshake=False

    $ timeout_label = "result"
    menu:
        Kevin "We are very strong and therefore do not need to care about insurance."

        "Incorrect":
            $showplayer()

            Mys"That's not right. We should insure ourselves, accidents can happen at any time."

            Mys "You may need to obtain travel and medical insurance prior to before going on placement."
            Mys "Make sure you consider and understand the scope and limitations of your insurance to ensure you are fully covered."
            $hideplayer()

            Kevin "Which aspect does this belong to?"
            $scoring1(8.34)

            menu:
                "Your work":
                    with hpunch
                    $scoring1(0)

                "Your travel and transport":
                    with hpunch
                    $scoring1(0)

                "Your location or region":
                    with hpunch
                    $scoring1(0)

                "Your general and environmental health":
                    with hpunch
                    $scoring1(0)

                "Your personal traits, characteristics, abilities":
                    with hpunch
                    $scoring1(0)

                "Your insurance arrangements":
                    $scoring1(8.34)

        "Correct":
            with hpunch

            show Missy Normal at center:
                xalign 0.2

            Missy "[povname] is wrong. We should insure ourselves, accidents can happen at any time."

            Missy "You may need to obtain travel and medical insurance prior to before going on placement."
            Missy "Make sure you consider and understand the scope and limitations of your insurance to ensure you are fully covered."


            Missy "Which aspect does this belong to?"

            hide Missy Normal
            menu:
                "Your work":
                    with hpunch
                    $scoring1(0)

                "Your travel and transport":
                    with hpunch
                    $scoring1(0)

                "Your location or region":
                    with hpunch
                    $scoring1(0)

                "Your general and environmental health":
                    with hpunch
                    $scoring1(0)

                "Your personal traits, characteristics, abilities":
                    with hpunch
                    $scoring1(0)

                "Your insurance arrangements":
                    $scoring1(8.34)


label result:

    if isshake:
        with hpunch
        $isshake=False

    $timeout_label = False


    show Missy Normal at center:
        xalign 0.7
    Missy "OK, [povname], I've been watching your performance,"
    Missy "and rated your answers."

    if score1>=83.4:

        Missy "Your score is [score1]. I think you are well aware of the risks that may arise."

        Missy "You can contact me to apply for the exchange student program."

        $showscore=False
        $timeout_label = None
    else:

        Missy "Your score is [score1]. I think you haven't fully understood the risks that may arise. "

        Missy "Looks like you're not ready for the event."

        Missy "If you don't pass, you can take the test again."

        $showscore=False
        $timeout_label = None

        jump exam


    "Kevin finally changed the placement location because he want to accompany you."
    "You ended up at the Von Neumann University (the best computer university) with kecin, to study computing as interactive students."

    scene white
    with fade

    show text "First day at Von Neumann University"
    pause

    scene bg entrance
    with dissolve

    $showplayer()

    show kevin:
        zoom 0.5
        xalign 1.0 yalign 0.35
        linear 0.5 xalign 0.7

    Mys "Wow, is this the best computer university in the world? it's really great!"
    Kevin "I can't wait to get in!"
    Mys "Let's hurry in."
    Kevin "There is a access control system at the entrance, do we have to swipe the student card Missy gave us to get in?"
    Mys "It should be, the school needs the student card to verify the student's identity. "
    Mys "Non-campus personnel always pose a security issue."
    Mys "Let me try it with my student card."
    "......"

    Mys "How come the machine is not responding?"
    Kevin "Is it because our card has not been activated yet?"

    Mys "I don't think so, this is what Missy sent us. Certainly no problem."
    Kevin "I noticed that there was no supervision next to it, "
    Kevin "and this gate is not high, we can turn over. And there was no supervision."

    $hideplayer()
    hide kevin

    menu:

        "Contact Missy to resolve the problem":

            $showplayer()

            show kevin:
                zoom 0.5
                xalign 1.0 yalign 0.35
                linear 0.5 xalign 0.7

            Kevin "Missy has said to contact our school if you have a problem outside. "
            Mys "Let's contact her first."

            Mys "Missy, our student card can't go through the entrance of the school. what's going on?"

            show Missy Surprise at center:
                xalign 0.8

            Missy "This shouldn't happen, I activated them myself when I gave you the student cards."
            Missy "I'll check them again."
            "......"

            show Missy Normal at center:
                xalign 0.8
            Missy "I know. The student card needs to be activated by VON Neumann University."
            Missy "I have contacted the their staff. It should be ready in a few minutes."

            Mys "Missy student card is ready to use, thank you very much."
            Missy "You're welcome. Please remember to contact the school if you have any difficulties out there."
            "The school will provide you with help."
            Mys "OK!"

            "After a while, your student card is ready for use."

        "Follow Kevin over the gate":



            $showplayer()

            show kevin:
                zoom 0.5
                xalign 1.0 yalign 0.35
                linear 0.5 xalign 0.7

            Mys "I really want to go in and have a look. "
            Mys "It shouldn't be a problem to climb over. "
            Mys "And we are university students. It's just that the student card is temporarily unavailable."

            Kevin "It's easy to turn over, come over here."
            Mys "No problem!"
            Mys "finally getting into the best computer university."

            scene bg university2
            with dissolve

            "You just rolled over and the security guard appeared."


            show security:
                zoom 1.0
                xalign 1.0 yalign 0.35
                linear 0.5 xalign 0.7

            Security "Stop! Who are you? Who gave you permission to go through the gates?"

            $showplayer()
            Mys "We are exchange students of the university."
            Mys "we are not bad people and we have student cards."

            Security "Give me your student card and I'll try it."
            "......"
            Security "Your student card doesn't work."
            Security "Although your name is on it, it may be fake."
            Security "I'm going to arrest you!"
            Mys "don't..."

            hide security

            "After your arrest, Missy got the news. "
            show Missy Rage at center:
                xalign 0.7

            Missy "How can you go through the gates privately? "
            Missy "Didn't I tell you to contact the school if you encounter any problems?"
            Missy "You'll ruin our school's reputation!"
            Missy "The student card needs to be activated by VON Neumann university and our university. "
            Missy "When you swiped your card, the staff of Von Neumann University has not activated it for you!"
            Missy "You should have contacted me!"

            Mys "I'm sorry."
            Mys "It won't happen next time"

            Missy "There is no more next time for you."
            Missy "This is your last exchange student program."
            Missy "You will be banned from future activities."
            Mys "Don't..."
            Missy "Also you will be fined £5,000 by the local police!"
            Missy "It's your choice."
            "......"

            hide Missy
            $hideplayer()

            "After paying the fine at the police station"

    #
    # scene bg university1
    # with dissolve
    # $showplayer()
    #
    # show kevin:
    #     zoom 0.5
    #     xalign 1.0 yalign 0.35
    #     linear 0.5 xalign 0.7
    #
    # Mys "We're in, finally."
    # Kevin "Yes, we must have a good tour of the campus."
    #
    # "Then you begin your studies at the VON Neumann University."
    # "But life is not always peaceful."
    # "On this day you are using the computer in the computer building to study as usual."
    #
    # scene bg screen
    # with dissolve
    #
    # Mys "Wait, why is my computer screen suddenly white?"
    # Kevin "Look, the computer screen shows a line."
    # Kevin "You have been poisoned, to detoxify please pay £300! "
    # Kevin "Do not turn off your computer, or your computer will be destroyed."
    # Mys "What should I do? How about turning it off?"
    # Kevin "The word on the computer screen says not to turn it off."
    # Mys "So maybe the hackers tricked us? "
    # Mys "I don't think their technology is that great. He's scaring me."
    # Kevin "I thought it would be better to inform the supervisor in charge of us at the VON Neumann University."
    # Kevin "Missy said that if you have any problems during the placement, you should contact your local supervisor first."
    #
    # menu:
    #
    #     "Shutdown":
    #
    #
    #         Mys "Rebooting solves all problems!"
    #
    #         scene bg screenblack
    #         with dissolve
    #
    #         $showplayer()
    #
    #         show kevin:
    #             zoom 0.5
    #             xalign 1.0 yalign 0.35
    #             linear 0.5 xalign 0.7
    #
    #         Mys "My god, the computer can't open! "
    #         Mys "What should I do?. All my data is in there."
    #         Kevin "Notify the supervisor quickly!"
    #
    #         scene bg desk
    #         with dissolve
    #
    #         $showplayer()
    #
    #         show supervisor:
    #             xalign 1.0 yalign 0.35
    #             linear 0.5 xalign 0.7
    #
    #         Mys "Supervisor, my computer is poisoned and it won't open, which means our firewall is vulnerable!"
    #         Mys "Hackers may have access to our information."
    #
    #
    #         Supervisor "Yes, I understand. Please remember to let me know if you encounter any problems in school."
    #         Supervisor "We will check and close the loopholes immediately."
    #         Mys "Can that computer still be repaired?"
    #         Supervisor "I don't think so, they are very skilled."
    #         Supervisor "If there's any of your homework in there, I'm afraid you'll have to redo it."
    #         Mys "Oh my God. Help....."
    #     "Notify supervisor":
    #
    #         $showplayer()
    #
    #         show kevin:
    #             zoom 0.5
    #             xalign 1.0 yalign 0.35
    #             linear 0.5 xalign 0.7
    #
    #         Mys "It makes sense, as the best computer university in the world, their computers must have excellent firewalls."
    #         Mys "If hackers can break it, they must be very skilled."
    #         Kevin "Notify the supervisor quickly!"
    #
    #         scene bg desk
    #         with dissolve
    #
    #         $showplayer()
    #
    #
    #         Mys "Supervisor, my computer has been poisoned."
    #         Mys "I'm afraid to operate it casually. Our system has loopholes!"
    #
    #         show supervisor:
    #             xalign 1.0 yalign 0.35
    #             linear 0.5 xalign 0.7
    #
    #         Supervisor "Luckily you informed me in time. "
    #         Supervisor "I'm sending the staff to search it. See if it can be fixed."
    #         "......"
    #         Supervisor "We've found the vulnerability and your computer should work now."
    #         Mys "Thanks so much!"
    #         Supervisor "I would also like to thank you"
    #         Supervisor "If you had not informed us in time, all the computers in our school might have been poisoned. "
    #         Supervisor "It would have caused a lot of damage."
    #         Supervisor "Please remember to let me know in the first instance if you have any questions."
    #         Mys "No problem."
    #
    # scene bg view
    # with dissolve
    #
    # "After the viral crisis, you decide to go to the window to get some fresh air and relax your brain."
    # "You open the tiktok at the window."
    #
    # $showplayer()
    #
    # Mys "hahaha, this video is so funny."
    # "Suddenly a gust of wind blew, and you didn't hold your phone steady and dropped it."
    # Mys "Oh my god! I'm so unlucky."
    # "You rush downstairs to check your phone."
    #
    # scene bg breakscreen
    # with dissolve
    #
    # $showplayer()
    # show kevin:
    #     zoom 0.5
    #     xalign 1.0 yalign 0.35
    #     linear 0.5 xalign 0.7
    #
    # Mys "It's finished, It's completely broken."
    # Kevin "Looks like you need a new phone."
    # Mys "Damn! The phone card is also broken."
    # Kevin "Come on, I'll walk you to get a new phone and a mobile phone card."
    #
    # scene bg store
    # with dissolve
    #
    # $showplayer()
    # show kevin:
    #     zoom 0.5
    #     xalign 1.0 yalign 0.35
    #     linear 0.5 xalign 0.7
    #
    # "Electronic Market"
    # Mys "Ok, this is the phone I want."
    # Kevin "Next it's time for the new phone number."
    # Mys "Wow, 1111111111, that's definitely a really great mobile number!"
    # Kevin "Indeed, very memorable!"
    # Mys "Then it's decidedly it."
    # Mys "OK, we're done shopping, let's go!"
    # Kevin "Are you forgetting something?"
    # Mys "What is it?"
    # Kevin "You should update your contact details at missy."
    # Kevin "You must also ensure that the university has up-to-date contact information for you on Campus Solutions. "
    # Kevin "You need to know how to contact you during your placement in the event of an emergency."
    # Kevin "You should also ensure that you check your email regularly while away from the University."
    #
    # Mys "But this is not our country's mobile phone card, I will replace it when I go back."
    # Kevin "You should replace it immediately, it's very important!"
    # Mys "I really don't think there's anything wrong with changing to a fixed mobile number when I go back. This one is only temporary."
    #
    # $hideplayer()
    # hide kevin
    # menu:
    #     "Update":
    #
    #         $showplayer()
    #
    #         Mys "I should update. The contact details must be up to date."
    #
    #         Mys "ok, I'm done updating."
    #         "You got a call from missy just after your phone was updated."
    #         Mys "hi, missy. what a coincidence, I just updated my phone number."
    #
    #         show Missy Sad at center:
    #             xalign 0.7
    #
    #         Missy "I've been calling your original phone number for a long time, but I can't get through."
    #         Missy "Thank God you have updated your contact details."
    #         Mys "I should thank kevin, who convinced me to update it."
    #         Missy "I now have something very urgent to inform you."
    #         Missy "A variant of the COVID-19 has appeared in your area!"
    #         Missy "Our country wants to guarantee our safety by interrupting flights with the country you are in within 72 hours!"
    #         Missy "You need to come back immediately!"
    #         Missy "Otherwise, I don't know when you will be back!"
    #
    #         Mys "Oh my goodness, I get it."
    #         Mys "Thank you!"
    #         Missy "It's still very important to keep your contact details open!"
    #
    #     "Don't Update":
    #
    #         $showplayer()
    #         show kevin:
    #             zoom 0.5
    #             xalign 1.0 yalign 0.35
    #             linear 0.5 xalign 0.7
    #
    #
    #         Mys "If I update now, I still have to update it when I go back to Manchester. "
    #         Mys "It's a hassle. I don't usually use my mobile number, I can just use email."
    #
    #         Kevin "Well, it's your choice and I respect that."
    #
    #         scene bg dormitory
    #         with dissolve
    #
    #         "On this night"
    #         "You hear a heavy knock on the door."
    #
    #
    #         "Mys, Mys, wake up, something big is happening!"
    #
    #         $showplayer()
    #         Mys "Who's there?"
    #
    #         Kevin "I am Kevin."
    #
    #         show kevin:
    #             zoom 0.5
    #             xalign 1.0 yalign 0.35
    #
    #             linear 0.5 xalign 0.7
    #         Mys "I'm so sleepy, it's 2am. What's going on."
    #         Kevin "I just got a call from Missy."
    #         Kevin "Missy says we have a local variant of the COVID-19!"
    #         Kevin "Our country is going to interrupt flights with the country you are in within 72 hours as a way of keeping us safe!"
    #         Kevin "We need to go back immediately! Otherwise we don't know when we'll be back!"
    #
    #         Mys "Oh my goodness, I get it."
    #         Mys "Don't forget to update your contact details, Missy can't reach you. She is very anxious."
    #         Mys "OK!"
    #
    #         "After the update"
    #         hide kevin
    #
    #         show Missy Rage at center:
    #
    #             xalign 0.7
    #
    #
    #         Missy "Mys, what the hell were you thinking?"
    #         Missy "Why don't you update your contact details. I'm going crazy."
    #
    #         Mys "I don't think it's necessary to update this number, I won't use it when I go back."
    #         Missy "This thought is wrong!"
    #         Missy "You should keep your contact details open at all times."
    #         Mys "I understand, missy, and I'm very sorry"
    #         Missy "Kevin told you, didn't he?"
    #
    #         Mys "I've got it. We'll go back tomorrow."
    #
    #         "Finally you made it back to Manchester without incident."
    #
    #
    #
    # scene bg graduation
    # with dissolve
    #
    # "Everything went well in your later university life."
    # "On graduation ceremony"
    #
    # show Missy Laugh at center:
    #     xalign 0.8
    #
    # $showplayer()
    # show kevin:
    #     zoom 0.5
    #     xalign 1.0 yalign 0.35
    #     linear 0.5 xalign 0.7
    #
    # Missy "Congratulations on successfully completing your studies."
    # "At the same time, congratulations on your healthy and safe university experience."
    # "I wish you the best of luck in the future."
    #
    # Kevin "Thank you Missy!"
    # Mys "Thanks!!"
    #
    # "You ended up finishing your studies successfully and finding the right job. "
    # "Life has been on top ever since."
    #
    # scene white
    # with fade
    #
    # show text "The game is over! We hope you have learnt about health and safety at university."
    # pause



   #  With regard to the type of placement, a minigame can be made. placement in progress, security problems are found, contact the workplace supervisor. Discover that the student card is not working, contact the school, which finds that it needs to be updated. Mobile phone is broken, choose whether to update emergency contact details.
