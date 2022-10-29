label main:
    scene bg black with fade
    #$ renpy.notify("The Cafe")
    pause 1.0

    you "I think I lost them."
    "Clenching my fists,{w=0.3} I walk outside of the dirty alleyway."
    "It was a lucky escape!"
    "But... unfortunately, my clothes are super tattered. And I don't even have anywhere else to go..."
    "Being lost here sucks!{w=0.1} I don't even know my way back, since I dropped my phone...{w=0.3} ugh!"
    "Well, whatever.{w=0.1} They can take my home and my phone."
    "I hear my stomach grumble. {size=+5}{w=0.2}fuck{w=0.2}{/size} I'm hungry"
    "At least I still have my wallet!"
    "Opening the wallet, I see{w=0.3} that they have also taken my credit cards, my ID's, my everything{w=0.3}; ...except ten bucks."
    "I guess that was nice of them. I should really get something to eat while I'm at it...{w=0.2} and a new identity as well."
    "Leaving the alleyway, I look around for somewhere to get some food."

    scene bg outside with fade
    pause 1.0
    "A cafe I'd never seen before was right nearby."
    "I've never heard of this place,{w=0.2} but everywhere else was expensive cosmetic stores."
    "I read the title of the cafe, just in case I could rate it on Yel--{nw}"
    "...On second thought, nevermind. I forgot I still don't have my phone."
    you "Calling the police would've been so much easier right now!! Dammit!!"
    "Without any more time to waste, I rush into the cafe. Hopefully they ignore my dirty appearance."

    scene bg cafe with fade
    $ renpy.notify("The Cafe")
    pause 1.0
    "The cafe was a nice sight. As pretty as your average cafe could be."
    "The visuals were relaxing, and it felt very homely. Perfect for those looking to relax or bring their computer to pretend to use it in public."
    "I walk up to the counter and read the menu and stare at the pasteries. No one else was here, so I took all the time I want."

    $ w = Character("???")
    show warden push at hi
    w "Darn it! The cupcakes squished all together again!"
    "The man in the purple suit stared at the deformed mess of cupcakes, and tried to fix them to look nicer."
    "He notices me and looks up at me."
    show warden 2
    w "Ah, hello, welcome to--{nw}" # add ma'am, sir, mx
    show warden woah
    extend " Goodness gracious! What happened to you? Are you okay?"
    you "It's a long story, can I get a--"
    w "No, it's not! I'm sorry if you're in a rush or anything, but you should get cleaned up!"
    you "It's fine, and I'm not in any rush."
    show warden think2
    w "I'm sorry, but here at SuperCafe, I can't allow this. Just read our plaque!"
    show warden think
    "I look up at the plaque."
    you "{i}We shall never deny a guest, even the most ridiculous request.{/i}"
    "What the hell does that mean??"
    show warden think2
    w "Under SuperCafe's rules, my employees and I will have to help you."
    show warden think
    menu:
        "Accept his help":
            pass

        "Run for my life":
            jump gtfo

    you "...Fine, fine! You guys can help me, though I only have 10 bucks."
    show warden 2
    w "Not a problem! We barely get customers anyway, so we'll be more than happy to help you!"
    show warden
    "The man in the purple suit gives me a big, friendly smile. I guess I should be grateful. It's not like I have anywhere else to go."
    define w = Character("The Warden", image="warden")
    show warden 2
    w "I'm the Warden, the owner of SuperCafe. It's nice to meet you!"
    show warden
    you "It's nice to meet you too."
    show bill at hi, right
    $ b = Character("???")
    b "HEY BOSS!! THE KITCHEN'S ON FIRE!!"
    b "LOOKS LIKE THE ONCELER GOT IN AGAIN!!"
    show warden woah
    w "Again?? This is the 5th time this week!"
    show warden oh
    w "Could you maybe help this poor customer? I'll have to extinguish it."
    b "SURE THING."
    hide warden
    show bill at center with move
    $ b = Character("Bill Cipher")
    b "I'M BILL. CAN I TAKE YOUR--{nw}"
    show bill what
    extend " WHAT HAPPENED TO YOU?" with vpunch
    you "Long story. Can I please get two cupcakes and a coffee?"
    show bill 2
    b "AAALRIGHT. THAT'LL BE EIGHT BUCKS." # 8 dollars
    "I put the 10 bucks on the counter."
    menu:
        "Let him keep the change":
            you "Keep the change."
            $ b_love = b_love + 10
            $ renpy.notify("Bill's love for you: " + str(b_love))
            show bill
            b "THANK YOU! GLAD TO SEE SOMEONE HAS SOME KINDNESS AROUND HERE."
            pass
        "Horde the change for yourself":
            b "WOULD YOU LIKE YOUR MONEY BACK?"
            you "I believe you owe me two bucks."
            "He slides back a dollar and a few cents."
            pass
    "The triangle gives me the delicacies and my coffee."
    b "ENJOY nerd"
    call billConfession # this will ONLY happen if you a little hacker
    hide bill

    scene bg placeholder with fade
    $ renpy.notify("The Table")
    pause 1.0
    "I eat my food, being grateful that a place as cute as this doesn't have people to stare at my appearance.{p=0.3}Heck, I'm glad everyones been so nice."
    "It is a {i}little{/i} jarring to see that someone looks like they came straight out of a war. I can see why they'd react so negatively."
    "Oh well, though."
    show sans weiner at hi
    $ s = Character("???", who_font="fonts/ComicSansMS3.ttf", who_color="#ffffff", what_color="#ffffff", what_font="fonts/ComicSansMS3.ttf", window_background="gui/sans_textbox.png")
    play sound "audio/weiner.ogg"
    s "* hey kid do you want a weiner in your mouth"
    show sans
    s "* oops.{w=0.3} sorry{w=0.1} my demons"
    $ s = Character("sans", who_font="fonts/ComicSansMS3.ttf", who_color="#ffffff", what_color="#ffffff", what_font="fonts/ComicSansMS3.ttf", window_background="gui/sans_textbox.png", callback=sans_voice)
    play music sans
    show sans haha
    s "* nice to meet you, human. i'm sans the skeleton."
    s "* say, you look tattered up. that's crazy!"
    "Suddenly, my ragged clothes and bruises turn right back to normal..??" with hpunch
    s "* there ya go. my boss would probably be freakin' out if he saw ya like that."
    you "Oh, thanks Sans!"
    s "* no problem, [bro]. happy to help."
    show sans think
    s "* hey,{nw}"
    show sans
    extend " knock knock."
    you "Who's there?"
    s "* bone."
    you "Bone...{w=0.3} who?"
    show sans haha
    s "* bonejour."
    menu:
        "Laugh so hard":
            "You giggle a bunch and snort a little."
            you "Sans, that joke was hilarious!"
            show sans haha
            s "* pfft, thanks [bro]. always happy to tell a joke or two."
            $ s_love = s_love + 10
            $ renpy.notify("Sans' love for you: " + str(s_love))
            call sansConfession
            pass

        "Insult his joke":
            you "Dude that joke was dogshit."
            s "* geez. fuck you too, i guess."
            $ s_love = s_love - 10
            $ renpy.notify("Sans' love for you: " + str(s_love))
            pass
    s "* well, welcome to SuperCafe."
    show sans b
    s "*fart*"
    s "sorry i farted"
return


label gtfo:
    you "Yeah, no. {w=0.2}Not doing this today. I'll go eat at McDonald's."
    show warden woah
    w "What?? No, come back!"
    scene bg black with fade
    pause 1.0
    "not today ending{p}(how rude)"
return
