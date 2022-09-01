init python:
    GuessMoney=False
    isNumber=False
    ReLab1=False
    ReLab2=False
    ReLab3=False
    ReLab4=False
    ReLab5=False
    ec=0
    lentKevin=False
    wearclothe=False
    wearsandals=False
    score=0
    retrain1=False
    retrain2=False
    retrain3=False
    retrain4=False
    retrain5=False
    qq1=False
    qq2=False
    Lab1=False
    Lab2=False
    Lab3=False
    Lab4=False
    Lab5=False

    isshow=True

    def scoring(mark):

        global score

        score+=mark

        if score>=200:
            score=0

        return score



label chapter2:
    $count=0


    $retrain=False

    scene white
    with dissolve

    show text "chapter2"
    pause

    show text "After a painful exam week, your long-awaited summer holiday finally arrive."
    pause

    show text "You have made many fulfilling travel plans."
    pause

    show text "But! A virus called the Covid-19 suddenly begin to spread rapidly in the world."
    pause

    show text "Sudden pandemic causes travel restrictions."
    pause

    show text "It puts a damper on all your travel plans."
    pause

    show text "You have to stay inside the school for the whole holiday."
    pause

    show text "And your parents tell you that you must be responsible for your own living expenses for the summer."
    pause

    show text "As the impact of the lockdown on the economy is huge."
    pause

    show text "In order to earn money for the summer holidays, you decide to get a job."
    pause
        #After your screening, you have decided to attend
        #(options can be added, restaurant waiter, courier)

    scene bg bedroom
    with fade

    $showplayer()

    Mys "I have to get a job, or I won't have any money to buy food!!!"
    Mys "Missy said I could go to her office if I have difficulty, so I could ask her."

    scene bg office
    with fade

    $showplayer()

    show Missy Normal at center:
        xalign 0.7

    Mys "Hi Missy, I have  some difficulties recently."
    Missy "Hi, Mys, what difficulties are you having?"
    Mys "Due to the covid-19 epidemic, our family is in a financial situation."
    Mys "I have to earn my own living for the summer,"
    Mys "so I want to know if you could help me find a job."
    Missy "Wow, what a coincidence, I have just recently received a notice from the university. "
    Missy "I'm going to be in charge of recruiting cleaning staff for the new lab building. "
    Missy "They will be paid. I think this is a great option for you."
    Mys "Fantastic, can you sign me up?"
    Missy "No problem, Guess how much money you will get?"

label guess:
    python:
        # Ask player to enter his/her name
            isNumber=False
            money = renpy.input("Please enter the salary you expect here: ")

            if money.isdigit():

                isNumber=True

                money=int(money)

                if money>=5000:
                    GuessMoney=True
    if not isNumber:
        Missy "You didn't input a number, please input a number."
        jump guess

    if GuessMoney:
        Missy "That's right, the school pays the staff [money]£ a month."
        Mys "What??? Are you serious??"
        Missy "Of course!"
    else:
        Missy "That's not correct, it's more than your expect"
        jump guess

    Mys "[money]£ is a lot. "
    Mys "It is enough to live on for a month. "
    Mys "Thank you very much."
label training:

    scene white
    with dissolve

    show text "With the help of Missy, you have managed to get a job. "
    pause

    show text "The job involves cleaning the laboratory building for our University."
    pause

    show text "The first thing you need to do is get the relevant training."
    pause

    scene bg classroom
    with dissolve

    show Missy Normal at center:
        xalign 0.7

    Missy "I'm here today to give a training session."
    Missy "Cleaning in the laboratory is different from normal cleaning work. "

    $showplayer()

    Mys "what's the difference?"

    $hideplayer()

    Missy "When cleaning a laboratory, you not only have to clean the laboratory environment, "
    Missy "but also clean the laboratory instruments and sort out the laboratory equipment. "
    Missy "If the laboratory equipment becomes inoperable or causes a safety problem due to your improper handling, "
    Missy "These are losses that the school cannot afford."
    Missy "Therefore you need to be trained."
    Missy "Now, I would like to tell you about the things to look out for when cleaning."
    Missy "We have laboratories for various subjects in this building"

    $showplayer()

    Mys "How many laboratories do we have? "
    Missy "Five!"
    Mys "Got it."

    $hideplayer()

    Missy "These laboratories carry out important experiments in the next semester, "
    Missy "which can affect the international reputation of our school. "
    Missy "So your work is very demanding and important."

    Missy "There are many sorts of signs in the laboratory."
    Missy "First, you need to be clear about what these standards mean."

    show red circul at center:
        zoom 1.5
        xalign 0.5 yalign 0.15
    Missy "Circular signs with a red border and diagonal line are prohibition signs."
    Missy "For this sign, it means you must not do something. ln this example, no smoking."
    hide red circul

    show red sign at center:
        zoom 1.5
        xalign 0.5 yalign 0.15
    Missy "Red signs are also used for fire-related equipment such as fire fighting equipment."
    hide red sign

    show blue sign at center:
        zoom 1.5
        xalign 0.5 yalign 0.15
    Missy "Blue signs are mandatory signs. "
    Missy "This means that you MUST do something, such as wear hearing protection in this case."
    hide blue sign

    show yellow sign at center:
        zoom 1.5
        xalign 0.5 yalign 0.15
    Missy "Yellow triangular signs are used to warn against hazards, such as electrical dangers as shown here."
    hide yellow sign

    show green sign at center:
        zoom 1.5
        xalign 0.5 yalign 0.15
    Missy "Green signs indicate safe conditions such as emergency escape routes or where to get first aid."
    hide green sign

    Missy "Always remember to wear PPE when entering certain laboratories."
    $showplayer()

    Mys "But what is PPE? "
    $hideplayer()

    Missy "Sorry my fault!"
    Missy "Personal protective equipment, or PPE, is designed to protect you from injury or illnesses caused by exposure to something harmful. "
    Missy "lt should be supplied and used wherever there are risks that cannot be adequately controlled by other means."
    Missy "PPE includes familiar items like safety glasses and gloves, "
    Missy "but also things like face-shields, goggles, hard hats, safety shoes, hi-visibility vests, and earplugs."
    Missy "lf you have been provided with PPE, ensure you know how to wear it correctly."
    Missy "PPE has to be selected for the particular hazard. "
    Missy "For example there are many different types of gloves, "
    Missy "some protect against heat or cold, or sharp edges,"
    Missy "while others are designed to protect the user from different types of chemical exposure."
    Missy "Make sure you use the correct type."
    Missy "One size does not fit everyone. For your PPE to be effective it must fit you properly."

    $showplayer()

    Mys "What happens if the PPE breaks down? "
    $hideplayer()

    Missy "lf your PPE is faulty or damaged, speak to me."
    Missy "I will send it to you after the training."
    Missy "PPE assigned for wear in laboratories and workshops should not be used at home."

    $showplayer()

    Mys "But these PPEs can be used in many places in daily life. "
    Missy "Even so you are still forbidden to use it anywhere other than in the laboratory."
    Mys "That's a shame."
    $hideplayer()


    Missy "Even in labs where you don't need to wear personal protective equipment, "
    Missy "you should dress appropriately and wear the right clothes and shoes. "
    Missy "For example, tie your long hair at the back of your head and keep it inside your clothes. "
    Missy "If headwear must be worn, it must be secured and fit snugly. "
    Missy "Loose clothing can be dangerous when near certain machines, so try to choose tight-fitting clothes. "
    Missy "Open-toed sandals must be prohibited."
    Missy "This is because any chemical spills or heavy objects dropped on the toes can cause serious injury!"


    Missy "Next, I'll talk about what to look for in a specific lab."

    if isshow:

        menu Labb:
            "Electrical Lab":
                $Lab1=True

                jump ElectricalLab

            "Chemistry Lab":
                $Lab2=True

                jump ChemistryLab

            "Mechanical Lab":
                $Lab3=True

                jump MechanicalLab

            "Bio Lab":
                $Lab4=True

                jump BioLab

            "Nuclear Lab":
                $Lab5=True
                jump NuclearLab

            "Finish Lab" if Lab1 and Lab2 and Lab4 and Lab4 and Lab5:
                $isshow=False
                jump waste



label ElectricalLab:

    if retrain1:

        scene bg office
        with fade

        show Missy Normal at center:
            xalign 0.7

    Missy "Firstly, the electrical lab."
    Missy "When handling any electrical equipment, "
    Missy "you must ensure that cables do not create a tripping hazard or drag across sinks or heating unit equipment."
    Missy "Do not overload plug sockets or plug one extension lead into another. "
    Missy "Do not place items that may leak or spill on top of the equipment."
    Missy "Do not use the equipment unless you have been shown how to use it properly. "
    Missy "If the equipment is labelled as faulty, please never touch it. "

    show labdonotuse at center:
        zoom 1.5
        xalign 0.5 yalign 0.15

    Missy "Like this sign."

    hide labdonotuse

    Missy "The school will have professional maintenance staff to deal with it."
    if Lab1 and isshow:
        jump Labb

    if retrain1:

        jump choose1

label ChemistryLab:

    if retrain2:

        scene bg office
        with fade

        show Missy Normal at center:
            xalign 0.7

    Missy "Next, chemistry lab."
    Missy "Avoiding chemicals entering the body in the chemistry lab. "
    Missy "Chemicals can enter the body in four main ways. "
    Missy "lngestion, by swallowing and transferring chemicals from hand to mouth when eating or smoking without first washing your hands."
    Missy "lnhalation, by breathing in gases, fumes, mist or dusts. "
    Missy "Once breathed insome substances can attack the nose, throat or lungs,"
    Missy "while others get into the bodythrough the lungs and harm other parts, e.g.the liver."
    Missy "lnjection, by skin puncture."
    Missy "Hypodermic needle injuries can involveinfectious agents or very harmful substances and care should be taken when using them."
    Missy "Direct contact with the skin. "
    Missy "Some substances damage skin, while others passthrough it and damage other parts of the body."
    Missy "Some vapours, gases and dusts are irritating to eyes."
    Missy "Corrosive liquid splashes can permanently damage eyesight."
    Missy "The safety signs associated with chemical hazards are diamond in shape with a red border."
    Missy "Here are some of the common ones."

    show chemistrysign at center:
        zoom 1.5
        xalign 0.5 yalign 0.15

    Missy "Please remember them."

    hide chemistrysign

    if Lab2 and isshow:
        jump Labb

    if retrain2:

        jump choose2

label MechanicalLab:

    if retrain3:

        scene bg office
        with fade

        show Missy Normal at center:
            xalign 0.7

    Missy "In a mechanical laboratory, you should avoid hurting the machine, or avoid the machine hurting you."

    Missy "If used incorrectly, the machine or equipment may cause you injury by touching or entangling any moving parts;"
    Missy "crushed between moving parts and fixed structures -for example -wall;"
    Missy "hit by objects or materials ejected by machines."

    show machsign at center:
        zoom 1.0
        xalign 0.5 yalign 0.15

    Missy "Some typical yellow triangular warning signs of mechanical hazards are shown."
    Missy "To reduce the risk of injury, you must ensure that you are supervised and follow any instructions given. "

    hide machsign

    Missy "Wear any personal protective equipment provided for your use. "
    Missy "Know the location of the emergency stop button on workshop equipment. You may need it!"
    Missy "Make sure any loose clothing and anything that might get tangled or caught is securely fastened before you start work."
    Missy "Never attempt to bypass or remove any guards or interlocks - they are there to protect you."
    if Lab3 and isshow:
        jump Labb

    if retrain3:

        jump choose3

label BioLab:

    if retrain4:

        scene bg office
        with fade

        show Missy Normal at center:
            xalign 0.7

    Missy "Next up is the bio lab. "
    Missy "When you enter the lab, check for warnings firstly, Biological hazards are identified by this warning sign."

    show biosign at center:
        zoom 1.5
        xalign 0.5 yalign 0.15

    Missy "To reduce the risk of becoming infected, here are some do's and don'ts."

    hide biosign

    Missy "Do not do anything to increase the risk of passing hazardous materials from your hands into your mouth. "
    Missy "This is why eating, drinking, applying cosmetics and storing food in labs are all prohibited."
    Missy "Never pipette by mouth."
    Missy "Do minimize aerosols and splashes, and deal with spills immediately."
    Missy "Do disinfect working surfaces after use."
    Missy "Do wash your hands before leavingthe work area."
    Missy "Wear your lab coat only in the lab."
    Missy "Keep your work area clean and tidy."
    Missy "Keep writing and experimental areas separate."
    if Lab4 and isshow:
        jump Labb

    if retrain4:

        jump choose4

label NuclearLab:

    if retrain5:

        scene bg office
        with fade

        show Missy Normal at center:
            xalign 0.7

    Missy "Finally, there is the nuclear laboratory. "
    Missy "Different types of ionising and non-ionising radiation produce different types of damage."
    Missy "Some not detected by our senses, so you may not know they are present or if you are being effected."
    Missy "When working with any type of radiation source you must follow all instructions,"
    Missy "wear PPE as required,"
    Missy "do not eat, drink, or chew gum in any area designated for work with radioactive materials."
    Missy "Here are some warning signs."

    show nuclearsign at center:
        zoom 1.0
        xalign 0.5 yalign 0.15

    Missy "Don't forget them."

    hide nuclearsign
    if Lab5 and isshow:
        jump Labb

    if retrain5:

        jump choose5

label waste:
    Missy "Please dispose of the waste generated in the laboratory correctly."
    Missy "Different laboratories or workshops have different waste disposal systems. "
    Missy "Please ensure that waste is disposed of in the correct waste disposal system. "
    Missy "A special reminder is to never put sharp objects such as glass or needles into plastic bags. "
    Missy "This is because they may puncture the plastic bags."

label collectPPE:
    Missy "That's what I'm trying to say. "
    Missy "I know there are a lot of points to be aware of, "
    Missy "but that's why you are paid very well. "
    Missy "If something goes wrong on the job, all the damage will be paid for by you. "
    Missy "And you will lose your well-paid job. "
    Missy "Please be careful when working!"

    $showplayer()
    Mys "It sounds like such a hassle, "
    Mys "but I'm willing to spend the time and experience to clean it for my living expenses."

    Missy "Now, Please come to me to collect your PPE."

    Mys "Wow, this PPE looks so advanced."
    Mys "I'll keep it well."

label Evening:

    $lentKevin=False

    scene bg kitchen2
    with dissolve

    "Evening."

    $showplayer()

    $showkevin()

    Kevin "So you're back, how was the training today?"
    Mys "There are so many situations to be aware of when working."
    Mys "It's not an easy job."
    Kevin "What do you have in your hand? "
    Kevin "It looks very advanced."
    Mys "This is the PPE we may have to wear at work."
    Mys "It can protect us from injury."
    Kevin "Wow, I'm baking a pizza and the baking tray is too hot."
    Kevin "Can I borrow the glove inside your PPE?"
    Kevin "I'll try it out and see if it works."

    $hideplayer()
    $hidekevin()

    menu:
        "Lend it to Kevin":

            $showplayer()

            $showkevin()

            Mys "I can lend it to you, I would also like to know if the PPE's will work."
            Kevin "Thank you so much."
            "Kevin accidentally touched the knife while using it, resulting in a very small crack in the glove"
            Kevin "It's over, but there's a crack in the glove. "
            Kevin "But the crack is so small, it shouldn't matter. "
            Kevin "It's better not to tell Mys. Or he'll argue with me. That's terrible."
            Kevin "I'm done with it. Give it back to you."
            Mys "How does it feel?"
            Kevin "It's really good quality, thanks a lot."

            $lentKevin=True

        "Don't want to lend to Kevin":

            $showplayer()

            $showkevin()

            Mys "I'm very sorry, Missy said they are forbidden in the house because of the risk of damage when using them at home."
            Kevin" Well, it's okay, I'll think of another way."
label Day2:

    $score=0
    $wearclothe=False
    $wearsandals=False

    scene bg bedroom2
    with dissolve

    "Day2"

    $showplayer()

    Mys "The first day of work, I need to prepare well. "
    "I can't lose my job on the first day."
    Mys "I should pick out the right clothes to wear for work."
    Mys "Let's start by looking at the temperature today..."
    Mys "what? I can't believe it."
    Mys "It's 36 degrees Celsius. It's so hot!"
    Mys "I want to wear something cooler."

    $hideplayer()
    menu:

        "Wear loose clothing":

            $showplayer()

            $wearclothe=True

            Mys "wearing loose clothing makes me cool, which is a wise choice."
        "Wear close-fitting clothing":

            $showplayer()


            Mys "I should wear close-fitting clothing in the laboratory."

    $hideplayer()

    menu:
        "Wearing trainers":

            $showplayer()


            Mys "Wearing trainers makes it easier for me to do my job."
        "Wearing sandals with a missed toe":

            $showplayer()


            $wearsandals=True

            Mys "Wearing sandals can make me very comfortable and cool."

    Mys "Going to work next."

label work:

    scene bg electrical
    with fade

    $showplayer()

    Mys "Let's start by cleaning up the electrical lab."
    Mys "Oh my god!! It's such a mess, all sorts of wires are tangled together."
    Mys "The plugs are not used properly."
    Mys "Some are full and some are not plugged in at all."
    Mys "The floor was also covered in stains. "
    Mys "Started cleaning!!"
    Mys "First I should tidy up the wires."

    $hideplayer()

label choose1:

    if retrain1:

        $ retrain1=False
        scene bg electrical
        with fade

    menu:
        "Place the wire against the wall":

            $showplayer()


            Mys "I should place the wire against the wall."
            $ec=1

        "Untie the wires and keep the board from overloading":

            $showplayer()


            Mys "I should untie the wires and keep the board from overloading."
            $ec=2

        "Check that the wires will not drag the appliance before tidying":

            $showplayer()


            Mys "I should check that the wires will not drag the appliance before tidying."
            $ec=3

        "Select all of the above":

            $showplayer()


            Mys "I should select all of the above."

            $ec=0
            $ReLab1=True
            $scoring(20)

        "I want to retrain":

            $retrain1=True
            jump ElectricalLab

    Mys "Finally finished, now it's time to sweep the floor."

    scene bg chemistry
    with dissolve

    $showplayer()

    Mys "Next is the chemistry lab."
    Mys "My role is not only to clean the floor, but also to clean up the lab equipment."
    Mys "There are chemical waste products that could harm me."
    Mys"First I need to recall how chemicals get into the body."

    $hideplayer()

label choose2:

    if retrain2:

        $ retrain2=False
        scene bg chemistry
        with fade

    menu:
        "Through the mouth and skin ":

            $showplayer()


            Mys "Chemicals enter through mouth and skin."
            Mys "I should have a mask, clothes, and gloves ready."

        "Through the skin and nose":

            $showplayer()


            Mys "Chemicals enter through skin and nose."
            Mys "I should have a mask, clothes ready."

        "Through the mouth, skin,nose, eyes and by injection":

            $showplayer()


            $ReLab2=True
            $score=scoring(20)

            Mys "Chemicals enter through the mouth, skin,nose, eyes and by injection."
            Mys "I should be prepared with a mask, clothes, gloves, glasses."

        "Through the nose, skin and eyes":

            $showplayer()


            Mys "Chemicals enter through the nose, skin and eyes."
            Mys "I should have a mask, glasses and gloves ready."

        "I want to retrain":

            $retrain2=True
            jump ChemistryLab

    if lentKevin:

        "While cleaning the cup containing sulphuric acid, you suddenly feel a sharp pain."
        Mys "It hurts so much. What happpened?"
        Mys "How did the sulfuric acid get to my skin?"
        Mys "Why does my glove have a small crack?."
        Mys "It must have been broken when it was loaned to kevin!"
        Mys "Missy is right, I shouldn't use PPE at home."
        "Let's choose again."

        jump Evening


    Mys "cleaned up, now it's time to get into the mechanical lab."

    scene bg mechanical
    with dissolve

    $showplayer()

    Mys "I'm so tired, but I still have to clean the mechanical lab."
    "When cleaning, you find that some of the machinery's guards are also dirty."

    $hideplayer()

label choose3:

    if retrain3:

        $ retrain3=False
        scene bg mechanical
        with fade

    menu:

        "remove the guards and clean them":

            $showplayer()


            Mys "It shouldn't be a problem to take them off, clean them and put them back on."
            Mys "My Obsessive-compulsive disorder won't allow that dust to exist!"


        "Ignore them":

            $showplayer()


            $ReLab3=True
            $score=scoring(20)

            Mys "Missy said we shouldn't touch those devices."
            Mys "I'll leave them alone."

        "I want to retrain":

            $retrain3=True
            jump MechanicalLab

    if wearclothe:

        "You are cleaning up and suddenly find that your clothes are stuck inside the machine."
        Mys "Oh my god, how did it get stuck inside the machine."
        Mys "I wear clothes that are too baggy!"
        Mys "Missy said not to wear anything too baggy."
        Mys "It's over, the clothes and the machine are broken"
        "At this point Missy passed by and"

        show Missy Rage at center:
            xalign 0.7

        Missy "Mys!"
        Missy "You broke the machine. You're fired!"
        "Please choose again, this time with care."

        jump Day2


    Mys "Clean up is done, now it's time to move on to the biology lab."

    scene bg bio
    with dissolve

    $showplayer()

    Mys "I seem to need to sort out my clothes after entering or exiting. "

    $hideplayer()

label choose4:

    if retrain4:

        $ retrain4=False
        scene bg bio
        with fade

    menu:
        "Disinfect clothing on entry and exit":

            $showplayer()


            $ReLab4=True
            $score=scoring(20)

            Mys "I should disinfect the clothes, biology labs are very sensitive to bacteria."

        "Enter directly after putting on PPE":

            $showplayer()


            Mys "The PPE is of very good quality and clean, and it is fine without sterilisation."

        "I want to retrain":

            $retrain4=True
            jump BioLab

    if wearsandals:

        "When cleaning biological lab equipment,"
        "bacteria-laden liquids fly up to your toes due to the sandals you're wearing."
        "After cleaning up, you forget to clean your toes."
        "When you go back home, you unfortunately get a fungal infection. "
        "You can't work for the whole holiday. "
        "Please choose again, this time with care."

        jump Day2



    Mys "Clean up is done, now it's time to get into the nuclear lab."

    scene bg nuclear
    with dissolve

    $showplayer()

    "While cleaning you suddenly get hungry."
    Mys "I'm so hungry, it's been a busy morning. "
    Mys "I need to get some energy."
    Mys "I brought a sandwich in the morning."
    Mys "It's time to eat it."

    $hideplayer()

label choose5:

    if retrain5:

        $ retrain5=False
        scene bg nuclear
        with fade

    menu:
        "Can't see anything dirty, eat sandwich for energy":

            $showplayer()


            Mys "Eat the sandwich before you work, it will give me more energy."

        "It's better to eat after cleaning":

            $showplayer()


            $ReLab5=True
            $score=scoring(20)

            Mys "Missy said there was radiation in the nuclear lab. "
            Mys "I can't see this radiation."
            Mys "It's still dangerous to take off the PPE. "
            Mys "Let's eat after cleaning up."

        "I want to retrain":

            $retrain5=True
            jump NuclearLab

    Mys "finally finished the job! I can rest now."
    Mys "I have to report to Missy about my work."

    scene bg office
    with dissolve

    $showplayer()

    show Missy Normal at center:
        xalign 0.7

    Mys "Hi, Missy I am here to give you a report about my work."
    Missy "No need to report, there are security cameras in every lab. I can see everything."

    if ReLab1==False:

        if ec==1:

            Missy "You didn't notice that the wire is overloaded, so the wire is overloaded causing damage to the instrument."

        elif ec==2:

            Missy "You moved the appliance while unplugging the cord.That caused damage to the appliance."

        elif ec==3:

            Missy "You didn't put the wire in the corner so that the wire tripped up people."


    if ReLab2==False:

        Missy "I saw that you did not wear the PPE correctly, even if there was no safety incident this time it was still very dangerous."



    if ReLab3==False:

        Missy "You touched the guards of the machinery. "
        Missy "After you finished cleaning, the staff found that the guards were broken,"
        Missy "so you should pay for the damage."


    if ReLab4==False:

        Missy "You did not sterilize before entering the biological laboratory. "
        Missy "That caused the death of experimental bacteria we cultivated."
        Missy "This was a failure in your work."


    if ReLab5==False:

        Missy "You ate in a nuclear laboratory."
        Missy "That behaviour is very dangerous. "
        Missy "It could expose you to radiation. "
        Missy "You should not behave in that way."

    Missy "I have rated your performance. You score is [score]"

    if score==100:

        Missy "You finished your job without any mistakes and performed very well. Well done!"
        Mys "Thanks! I will definitely work hard!"
        "Your job pays well, and therefore your quality of life is high."
        "Well done!"


        jump chapter3

    elif score>=80:

        Missy "You made some mistakes at work, but people always make mistakes sometimes."
        Missy "You didn't make many mistakes. Try better next time."
        Missy "But this work does not allow you to make any mistakes."
        Missy "I've decided to give you another job. "
        menu aks:
            "Inquire about job content":
                $qq1=True
                Mys "What is this job?"
                Missy "As our university is an internationally renowned school, many letters are collected every day."
                Missy "Your task will be to answer them. "
                jump aks
            "Ask about salary":
                $qq2=True
                Mys "What is the salary of this job?"
                Missy "This job allows you to make some mistakes, but the pay is much lower. "
                Missy "It's about £1,500 a month."
                jump aks
            "No more question" if qq1 and qq2 :
                Mys "Although reluctantly, I have to accept it."
                "You can't buy expensive food and clothes because of the low salary. "
                "During summer vacation, your quality of life is not high."


        jump chapter3

    elif score<80:
        Missy "You are unable to do this job because you have made too many mistakes. "
        Missy "I am very sorry, but you are fired."
        "Let's start the selection again, this time with care."

        $scoring(200)

        jump training
#jump chapter3
