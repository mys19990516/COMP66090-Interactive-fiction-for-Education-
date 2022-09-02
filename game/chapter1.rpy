init:
    default close_firedoor = False
    default HaveFire=False

label first_chapter:

    scene white
    show text "Chapter 1"
    with fade
    pause 1.0

    show text "One month later"
    with fade
    pause

    scene bg university
    with dissolve

    show text "After a month, you have fully adjusted to university life.":
        pos(1000, 290)
    pause

    show text "After a month, you have fully adjusted to university life."
    pause

    show text "You and [friend] live together. You often study, go shopping together. Life is very comfortable and happy."
    pause

    show text "However, you have recently noticed that [friend] has picked up the habit of smoking."
    pause

    "On a weekend"

    scene bg bedroom
    with dissolve

    $showplayer()

    Mys "Finally finished my homework, wow it's already 7.30 pm, so hungry."
    Mys "I have to go to the kitchen and get something to eat."

    scene bg kitchen2
    with dissolve

    "When you enter the kitchen, you smell smoke. Then you notice [friend] is smoking."

    $showplayer()

    Mys "hi, [friend], why have you started smoking?"

    $showkevin()

    Kevin "I have to hand in assignments recently, so I've been under a lot of stress."
    Kevin "My friend told me to smoke if I am stressed, smoking would help me release my stress."
    Kevin "I tried it. It's true! Do you want to try it?"

    $hidekevin()
    $hideplayer()

    menu:

        "Of course! I want to try it.":
            $showkevin()

            $showplayer()

            Mys "cough! cough! cough!"
            Mys "It choking me, it's so uncomfortable."
            Mys "I suggest you stop smoking, it's bad for your health."
            Mys "There are other ways to release stress."

        "No, I don't want to.":
            $showkevin()

            $showplayer()

            Mys "Smoking is bad for my health, so I won't try it."
            Mys "I suggest you not to smoke either, there are other ways to release stress."

    Kevin "It's okay. We're in perfect health."

    "At this time, [friend] finishs smoking."
    "He drops the unextinguished butt next to the window, which is close to the curtain."
    "It makes you worried."


    Mys "Do you just leave your cigarette butt next to the curtain?"
    Mys "I think it could start a fire. It is dangerous."
    Mys "Universities often have fires. The University of Southampton had a fire that caused up to £50 million of damage."

    Kevin "I think you're worrying too much, the finished cigarette is not dangerous. "
    Mys "But...."
    Kevin "All right, I'm gonna do my homework."

    "You think [friend] is wrong and decide to ask Missy"
    jump askMissy

label askMissy:
    scene bg office
    with dissolve

    show Missy Smile at center:
         xalign 1.0
         linear 0.5 xalign 0.7

    Missy"Hi mys, what can you do for you"

    $showplayer()

    Mys "hi, Missy, my friend [friend] often throws cigarette butts very close to the curtains."
    Mys "I think it could start a fire, which is very dangerous."

    $hideplayer()

    show Missy Surprise at center:
         xalign 0.7

    Missy "It is indeed dangerous. You should stop him."

    show Missy Normal at center:
         xalign 0.7

    Missy "The causes of university fires are broadly: unattended cooking"
    Missy "candles left unattended or placed next to combustible material, carelessly discarded cigarettes, "
    Missy "heat sources next to curtains, experiments left unattended."
    Missy "Do you think [friend]'s behavior is among these dangerous behaviors?"

    menu:

        "I think it belongs to them.":
            $showplayer()

            Mys "[friend]'s behavior is among them. It may casue fire."

        "I don't think so.":
            $showplayer()

            Mys "[friend]'s behavior is not among these dangerous behaviors "
            Missy "Your are wrong, it definitely belongs to them."



    $hideplayer()

    Missy "For a fire to start three things need to bepresent at the same time:Oxygen, Fuel - something that will burn."
    Missy "And An ignition source - usually some form of heat, which can set the fuel alight."

    Missy "If you can remove any of these three you can prevent a fire."
    Missy "What factors can be removed to prevent fire?"
    menu:

        "Oxygen":
            $showplayer()
            Mys "I think we can remove the oxygen."
            Missy "That's not correct. Oxygen is present in the atmosphere. It can't usually be removed."
            Missy " You can try removing the other two factors."

        "Fuel":
            $showplayer()
            Mys "I think we can remove the Fuel."
            Missy "Yes! Oxygen is present in the atmosphere. It can't usually be removed."
            Missy " You can try removing the other two factors."

        "Ignition source":
            $showplayer()
            Mys "I think we can remove the ignition source."
            Missy "Yes! Oxygen is present in the atmosphere. It can't usually be removed."
            Missy " You can try removing the other two factors."

    $hideplayer()

    Missy "There are also a few things you should remember about fire."
    Missy "Handle discarded cigarette butts with care. "
    Missy "Discarded cigarette butts or even matches can start a fire if they are still hot and come into contact with combustible materials."
    Missy "Plugging too many appliances into one socket can lead to local overheating."
    Missy "Keep fire doors closed and evacuation routes clear in the event of a fire. "
    Missy "In the event of a fire, you'll use the evacuation routes. "
    Missy "These areas usually have fire doors which will stop the fire and smoke. "
    Missy "But if you leave the doors propped open, smoke and fire will spread more quickly to these areas and stop you or others from getting out."


    $showplayer()

    Mys "I get it."

    $hideplayer()

    Missy "Speaking of fire escapes, we have weekly alarm debugging in our buildings and halls of residence. "
    Missy "You should remember the sound of the alarm when it is commissioned. "
    Missy "If the alarm sounds during non-alarm commissioning times, flee the building immediately."
    Missy "Don't wait until someone tells you to leave, it may be too late."
    Missy "The green runner sign will take you to the nearest exit point. "

    show green runner:
        xalign 1.0 yalign 0.35
        linear 0.5 xalign 0.5

    Missy "Like this."

    hide green runner

    Missy "If you need to break the glass to get out in an emergency, you can do this! "
    Missy "This applies not only to this university but to most workplaces or public buildings in the UK, so it's worth remembering this. "
    Missy "Please remember that never use a lift during your escape."
    Missy "There is a high risk that the lift will break down which may cause you to be trapped inside."
    Missy "Finally, when you leave the building, make sure you go to the assembly point immediately."
    Missy "If you know someone is still inside, tell your supervisor, security or the fire brigade immediately. This could save someone's life."

    Missy "If you spot a fire first, pull the fire alarm."

    show fire alarm:
        xalign 1.0 yalign 0.35
        linear 0.5 xalign 0.5


    Missy "The fire alarm looks like this."

    hide fire alarm

    Missy "When you reach a safe location, contact the emergency services on 999."
    Missy "Tell a safety officer or emergency service officer that you have activated the alarm and where the source of the fire is."
    Missy "Give as many details as you can. Then go to the assembly point."
    Missy "Waitting until the emergency services or safety department say it is safe to re-enter."

    $showplayer()

    Mys "Thank you so much Missy, you have helped me a lot."

    show Missy Grin at center:
         xalign 0.7

    Missy " You're welcome, I'm happy to answer your questions."
    $hideplayer()
    hide Missy

    menu:
        "I want to hear Missy say it again":

            $showplayer()

            Mys "I want you to say it again, I forgot something."

            jump askMissy

        "I can remember Missy's words":
            Mys "That's enough, I already remembered Missy's words"

            jump CouldAgain

label CouldAgain:
    $close_firedoor = False

    scene bg kitchen
    with dissolve

    "A few days later, you find [friend] smoking in the kitchen again. He still puts the cigarette close to the curtain"

    $showplayer()

    Mys "[friend], I really don't think smoking is a good habit."

    $showkevin()

    Kevin "I'm very enjoying smoking right now, I think you should try it too."

    Mys "Oh my God, why did you put your cigarette so close to the curtains again??"
    Kevin "Relax, it's just a small cigarette."

    $hidekevin()
    $hideplayer()

    menu:
        "Just in case, i should stop him":

            $showkevin()

            $showplayer()

            Mys "This may start a fire."
            Mys "You should put out the cigarette and throw it in the adjacent bin, which is not far from the curtains."
            Kevin "Well, I don't want a fire either. What should I do?"

            $hidekevin()
            $hideplayer()

            menu:
                "Putting out cigarettes with water":
                    $showkevin()

                    $showplayer()

                    Mys "You should put out cigarettes with water and throw it in the trash"
                    Kevin "No problem, I get it."
                    jump exercise

                "Check for flammable items when throwing cigarette butts":
                    $showkevin()

                    $showplayer()

                    Mys "Check for flammable items when throwing butts, and remove them if any."
                    Kevin "No problem, I get it."
                    jump exercise

                "Throw your cigarette butts in the bin":
                    $showkevin()

                    $showplayer()

                    Mys "You should throw your cigarette butts in the bin."
                    Kevin "No problem, I get it."
                    $HaveFire=True
                    jump fire

        "I've warned him, It's better to let him handle it himself.":
                $showkevin()

                $showplayer()

                Mys "A small cigarette butt shouldn't start a big fire."
                Kevin "Haha, it's okay, I've been doing this for many times, relax."
                $HaveFire=True
                jump fire

    label fire:

        scene bg bedroom2
        with fade

        "Then you go back into the room and start studying.  "
        "Suddenly!"

        $showplayer()

        Mys "What is this smell?"
        Mys "It's so pungent."
        Mys "Hold on, this is the smell of flammable material being ignited!"
        Mys "It comes from the kitchen!"

        scene bg firedoor open
        with dissolve

        show fire:
            xalign 0.7 yalign 0.4

        show smoke:
            xalign 0.9 yalign -0.1

        "you rush to the kitchen quickly, and find that the kitchen fire is out of controll!"

        $showplayer()

        Mys "This fire is so big, I can't put it out!"
        Mys "There were other students in the halls of residence, I should pull the fire alarm to inform them!"
        "......"
        "Fire alarm sounded."
        Mys "OK, now it's time to run for my survival."

        $hideplayer()

        "When you escape, you find the kitchen fire door still open."



        menu:
            "The fire door needs to be closed ":

                $showplayer()

                Mys "I should close the fire door, which will stop the fire and smoke."

                scene bg firedoor close
                with dissolve

                $showplayer()

                Mys "The door has been closed."
                Mys "Now, it's time to run away."

                $ close_firedoor = True

            "The fire is spreading too fast, forget about the door":

                $ close_firedoor = False

                $showplayer()

                Mys "I don't have time to do this! I'm young, I don't want to die!"

        scene bg stair
        with fade

        "You run out of the dormitory, then you arrive at the stairway and spot the green runner sign."

        menu:
            "Follow the green runner sign is good for me":

                $showplayer()

                Mys "I should follow the green runner sign."
                Mys "It usually points to the nearest exit, it is suitable for use in emergency situations."

                $ use_stair=True

            "Lift is fast, I need to go downstairs as fast as possible":

                $ use_stair=False

                $showplayer()

                Mys "I live on the 18th floor."
                Mys "It's slow and tiring to walk down the stairs."
                Mys "I'd rather take the lift."

                scene bg lift
                with fade

                "Not long after you enter the lift, it suddenly stops."

                $showplayer()

                Mys "Oh, my God! How could the lift stop at such a critical moment!!"
                "It turns out that the fire is so large that it has burned out the wires. "
                "The lift is not working after the power goes out. You are trapped inside the lift. "
                "You can no longer escape from the building, so start again and choose carefully this time."

                jump CouldAgain

        if use_stair & close_firedoor!=True:

            scene bg runstair
            with dissolve

            show fire:
                xalign 0.7 yalign 0.4

            show smoke:
                xalign 0.9 yalign -0.1

            "As you are running down the stairs, you find that the fire has reached your floor."
            "Because you left the fire door open! It's spreading fast."
            "You can no longer escape from the building"

            $showplayer()

            Mys "Oh my god! I should have chosen another approach earlier!"

            "Start again with your choice, this time with caution."

            $hideplayer()

            jump CouldAgain
        jump successful

    label exercise:

        scene bg bedroom2
        with fade

        "Then you go back into the room and start studying.  "
        "Suddenly!"

        $showplayer()

        Mys "What is this smell?"
        Mys "It's so pungent."
        Mys "It comes from the kitchen!"

        scene bg firedoor open
        with dissolve

        show smoke:
            xalign 0.9 yalign -0.1

        $showplayer()

        Mys "The smoke is too thick! cough,cough....."
        "Then the fire alarm goes off. "
        Mys "The alarm is sounding. I should run away."
        "When you escape, you find the kitchen fire door still open"

        $hideplayer()

        menu:
            "The fire door needs to be closed ":

                $ close_firedoor = False

                Mys "I should close the fire door, which will stop the smoke."

                scene bg firedoor close
                with dissolve

                $showplayer()

                Mys "The door has been closed."
                Mys "Now, it's time to run away."

                $ close_firedoor = True

            "The fire is spreading too fast, forget about the door":

                Mys "I don't have time to do this! I'm young, I don't want to die!"

        scene bg stair
        with fade

        "You run out of the dormitory, then you arrive at the stairway and spot the green runner sign."

        menu:
            "Follow the green runner sign is good for me":

                $showplayer()

                Mys "I should follow the green runner sign."
                Mys "It usually points to the nearest exit, it is suitable for use in emergency situations."

                $ use_stair=True
            "Lift is fast, I need to go downstairs as fast as possible":

                $ use_stair=False

                $showplayer()

                Mys "I live on the 18th floor."
                Mys "It's slow and tiring to walk down the stairs."
                Mys "I'd rather take the lift."

                scene bg lift
                with fade

                "Not long after you enter the lift, it suddenly stops."

                $showplayer()

                Mys "Oh, my God! How could the lift stop at such a critical moment!!"
                "It turns out that to simulate a real fire, the staff have cut the power to the building."
                "The lift cannot operate without power."
                "You can no longer escape from the building, so start again and choose carefully this time."

                jump CouldAgain
        if use_stair & close_firedoor!=True:

            scene bg runstair
            with dissolve

            show smoke:
                xalign 0.9 yalign -0.1

            "As you are running down the stairs, you find that the smoke has reached your floor."
            "Because you left the fire door open! The smoke spreading fast. It's very thick."
            "You can no longer escape from the building"

            $showplayer()

            Mys "Oh my god! I should have chosen another approach earlier!"
            "Start again with your choice, this time with caution."

            jump CouldAgain

        jump successful
label successful:

    scene bg runstair
    with dissolve

    $showplayer()

    Mys "15th floor..."
    Mys "7th floor..."
    Mys"1st floor..."

    scene bg square
    with dissolve
    if HaveFire:

        $showplayer()

        Mys "Finally ran out, I should have called 999 immediately to inform the firefighters. "
        Mys "Then go to the designated area and wait."
        show Missy Sad at center:
             xalign 1.0
             linear 0.5 xalign 0.7
        Missy "The fire caused a lot of damage."
        Missy "This should never have happened."
        Mys "I am sorry about that. I should stop [friend]."
        Mys "But I still want to thank you, your knowledge was really helpful, thanks Missy."
        Mys "I have to learn seriously about health and safety."
    else:

        $showplayer()

        Mys " Finally ran out, so this was a drill. "
        Mys "The smoke was released in advance by the staff to simulate a real fire."
        Mys "Now I should go and wait in the designated area."
        Mys "Missy's knowledge was really helpful, thanks Missy."
        Mys "I have to learn seriously about health and safety."



label library:
    scene white
    with fade

    show text "After a couple of weeks, the deadline for the assignment is approaching."
    pause

    show text "You and [friend] decide to go to the library to study."
    pause

    scene bg library
    with dissolve

    "After a morning of learning, you are a little hungry."


    $showplayer()

    $showkevin()

    Kevin "I'm a bit hungry. My goodness, it's already 12:30!! "
    Kevin "[povname] do you want to go and get something to eat?"
    Mys "I'm a bit hungry too, so let's go and get something to eat."

    scene computer
    with dissolve

    $showplayer()


    $showkevin()


    Kevin "We have to put our phones, wallet and laptops away."
    Mys "Gosh, no need to go to all that trouble, we'll just go downstairs and get a meal."
    Mys "We will be back in a short time."

    Kevin "I think you should put them away."

    $hidekevin()
    $hideplayer()

    menu:
        "Putting away your personal belongings is better":

            $showplayer()


            $showkevin()

            Mys "Okay, I'll put them away."
            Kevin "Mobile phones, laptops and wallets are easy targets for thieves"
            Kevin "These items are very important to us. "
            Kevin "If any of them are lost or stolen, it can be an inconvenience. "
            Kevin "Don't leave these items unattended on campus, in restaurants or bars"
            Kevin "It only takes a second for someone to steal them."
            Mys" It does make sense, thieves are fast."

            scene lostcomputer
            with dissolve

            $showplayer()


            $showkevin()

            Mys "The computer has now been put away."
            Kevin "This should be fine now."
            Mys "Let's go."

            scene white
            with dissolve

            show text "When you back..."
            pause

            scene bg library
            with dissolve

            $showplayer()


            $showkevin()

            Kevin "Have you heard? "
            Mys "No, what happend?"
            Kevin "Someone just lost his computer because he left it on his desk when he went to the toilet"
            Mys "I'm lucky that I put the computer up,"
            Mys "or I may lost it too."
            Kevin "That's true."

        "I'll be back in just a few minutes, no need to be so nervous":

            $showplayer()


            $showkevin()

            Mys "It will take 2 minutes to buy a meal."
            Mys "However, it will take at least 5 minutes to put things away."
            Mys "It's too troublesome, I'll just leave it there."

            scene white
            with dissolve

            show text "When you back..."
            pause

            scene lostcomputer
            with dissolve

            $showplayer()

            $showkevin()


            Mys "Oh my god, where is my stuff? "
            Mys " My computer has my homework!!! "
            Mys "Not only do I have to spend buy a new computer and phone, "
            Mys "but I have to do my homework again!"
            Mys "It's totally too late! I don't have enough time!"

            Kevin "You should know that your property is not safe even in the school library."
            "In the end, you did not complete the assignment and did not pass this course."
            "Start the selection again, this time with care."

            jump library

label library2:
    scene white
    with dissolve

    show text "After another long period of study"
    pause

    scene bg library
    with dissolve

    $showplayer()

    $showkevin()

    Kevin "I'm so tired."
    Mys "I just found out that you're not in the right position to study."
    Kevin "It's true, I often get tired soon after I start studying. My back and eyes hurt so much."

    Mys "I have some suggestions for you."

    show adjust chair:
        zoom 0.8
        xalign 1.0 yalign 0.35

    Mys "Fisrt, you should adjust your chair so that Your lower back is supported by the backrest. "
    Mys "Second, feet are flat on the floor."
    Mys "Third, knees are roughly level with you hips."
    Mys "Then, forearms are approximately horizontal."

    hide adjust chair

    show adjust screen:
        zoom 0.8
        xalign 1.0 yalign 0.35

    Mys "Beside, you should also adjust your screen height so that Your eyes are about level with the top of the screen, looking down slightly. "
    Mys "lf the screen is too low, it will make you lean forward. "
    Mys "lf it is too high, it can cause neck ache. "

    hide adjust screen

    show keyboard:
        zoom 0.8
        xalign 1.0 yalign 0.35

    Mys "Adjust your mouse and keyboard."
    Mys "For mouse,it should close to you and the keyboard"
    Mys "Your wrist is level with elbow and arm relaxed and supported. You don't overreach to use it"
    Mys "For keyboard, you should have sufficient room in front so hands and wrist supported by desk."

    hide keyboard

    Kevin "Got it! I'll be careful next time!"
    Kevin "I've also noticed a problem with you."
    Mys "What's my problem?"
    Kevin "You often leave bags and other items on the path which can trip others. "
    Mys "That'true."
    Kevin "Every year, people trip over items left on the floor."
    Kevin "some fall and get injured as a result."
    Kevin "If you need to charge a laptop or other mobile device at work, "
    Kevin "make sure the power cord doesn't drag across the floor so people don't trip and fall."
    Kevin "library offers a laptop plug-in area. So we should try to use these whenever possible."

    $hidekevin()
    $hideplayer()

    menu:
        "leave bags and other items on the path, they are big enough that people can see them":

            $showplayer()


            $showkevin()

            Mys "It's okay, people can see what's on the road."

            "However, your bag trip over an elderly member of cleaning staff, causing her to land on her head. "
            "she is hospitalised and all your family's money go to compensate her. "
            "You have no money to continue with your studies"
            " Finally, you drop out of your University. "
            "Start your choice again, this time with care."
            jump library2

        "remove you items, they will cause inconvenience to people":

            $showplayer()


            $showkevin()

            Mys "Okay, I'll sort them out. "
            "Not long have you finished speaking, than a classmate's bag next to you have tripped over an elderly member of cleaning staff,"
            "causing her to land on her head and she was admitted to hospital."
            Mys "Gosh, I'm glad I took kevin's advice."
    "In the end, you successfully complete the assignment with a good grade."

    jump chapter2
