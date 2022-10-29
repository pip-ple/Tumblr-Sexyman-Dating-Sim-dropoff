label dressup:
    scene bg black with fade
    show demencia at hi, left
    d "Heyyyyy!"
    show demencia wink at center with move
    d "Welcome to [config.name]!"
    d "Before ya start playing, lets customize your appearance."
    show demencia 2 at left with move
    d "First things first, what's your name?"
    python:
        name = renpy.input("What's your name?", length=32)
        name = name.strip() or "Y/N"
        lowercase_name = name.lower() or "y/n"
        upper_name = name.upper() or "Y/N"
    show demencia wink at center with move
    d "Sweet! Nice to meet you [name]!"
    show demencia 2 at left with move
    d "Next up,{w=0.5} pronouns!"
    menu: # shoutout to pronouns page for being a great reference!
        "What are your most preferred pronouns?"

        "He/Him":
            $ hers = "his"
            pass
        "She/Her":
            $ he = "she"
            $ him = "her"
            $ his = "hers"
            $ himself = "herself"
            pass
        "They/Them":
            $ plural = True
            pass
        "It/Its":
            $ he = "it"
            $ him = "it"
            $ his = "its"
            $ hers = "its"
            $ himself = "itself"
        "No pronouns/name pronouns":
                $ he = "[name]"
                $ him = "[name]"
                $ his = "[name]'s"
                $ hers = "[name]'s"
                $ himself = "[name]self" # this is where things get tricky sadly, i can't make the perfect pronoun strategy for this case
                # sorry in advance to all my fellow no pronoun users!!
        "Other, or neopronouns":
            d "Awesome! Let's get you set up!"
            menu:
                d "First of all, are your pronouns singular or plural?\nExamples:\nSingular: Is she friendly? | Plural: Are they friendly?"
                "Singular":
                    pass
                "Plural":
                    $ plural = True
                    pass
            d "Great! This will get pretty repetitive, so I'll try making things easier for ya."
            if not plural:
                python:
                    he = renpy.input("Subject pronoun? (Example: {b}She{/b} walked down the stairs.)", length=15)
                    he = he.strip() or "ze"
                python:
                    him = renpy.input("Object pronoun? (Example: I think I like {b}him{/b}.)", length=15)
                    him = him.strip() or "zir"
                python:
                    his = renpy.input("Posessive determiner? (Example: That was probably {b}his{/b} mom.)", length=15)
                    his = his.strip() or "zir"
                python:
                    hers = renpy.input("Possessive pronoun? (Example: Do you think that bag was {b}hers{/b}?)", length=15)
                    hers = hers.strip() or "zirs"
                python:
                    himself = renpy.input("Reflexive? (Example: He should be ashamed of {b}himself{/b}.)", length=15)
                    himself = himself.strip() or "zirself"
                #d "If you had any trouble, try using {a="https://en.pronouns.page/" + "[he]"}this{/a} or {a="https://en.pronouns.page/:" + "[he]"}this{/a} link! It might help if it loads! Press the \"Back\" button to switch one!"
                # im gonna cry i cant concatenate links </3
                d "Press the \"Back\" button below to edit if you made any misspellings!"
                d "Be careful, though. Right now there's no quick teleports to change anything, so try to be spot on!"
                d "You can change your pronouns each new game, as well--{w=0.3} these won't be forever stuck to you if anything!"
            else:
                python:
                    they = renpy.input("Subject pronoun? (Example: {b}They{/b} walked down the stairs.)", length=15)
                    they = they.strip() or "xe"
                python:
                    them = renpy.input("Object pronoun? (Example: I think I like {b}them.{/b})", length=15)
                    them = them.strip() or "xem"
                python:
                    their = renpy.input("Posessive determiner? (Example: That was probably {b}their{/b} mom.)", length=15)
                    their = their.strip() or "xyr"
                python:
                    theirs = renpy.input("Possessive pronoun? (Example: Do you think that bag was {b}theirs{/b}?)", length=15)
                    theirs = theirs.strip() or "xyrs"
                python:
                    themself = renpy.input("Reflexive? (Example: They should be ashamed of {b}themself.{/b})", length=15)
                    themself = themself.strip() or "xemself"
                #d "If you had any trouble, try using this {a="https://en.pronouns.page/" + "[they]"}link{/a}! It might help if it loads! Press the \"Back\" button to switch one!"
                d "Press the \"Back\" button below to edit if you made any misspellings!"
                d "Be careful, though. Right now there's no quick teleports to change anything, so try to be spot on!"
                d "You can change your pronouns each new game, as well--{w=0.3} these won't be forever stuck to you if anything!"
    d "Next up..."
    menu:
        d "What words would you prefer being called by?\nExample: This guy is hilarious!"

        "Guy/man/gentleman/bro":
            pass
        "Lady/woman/queen/girl":
            $ guy = "girl"
            $ bro = "gal"
            $ man = "woman"
            $ gentleman = "lady"
            $ king = "queen"
            $ bf = "girlfriend"

        "Person/partner/lord": # apologies for the lack of terms here, i had a hard time brainstorming and researching
                $ guy = "person"
                $ bro = "kid"
                $ man = "person"
                $ gentleman = "delightful person"
                $ king = "lord"
                $ bf = "partner" # debating whether to put partner or s/o
        "Custom":
            python:
                guy = renpy.input("Replacing \"guy\"? Example: That {b}guy{/b} over there.)", length=15)
                guy = guy.strip() or "person"
            python:
                bro = renpy.input("Replacing \"bro\"? Example: This {b}bro/gal{/b} is so cool!)", length=15)
                bro = bro.strip() or "kid"
            python:
                man = renpy.input("Replacing \"man/woman/person\"? Example: She is such a nice {b}person{/b}.)", length=15)
                man = man.strip() or "person"
            python:
                gentleman = renpy.input("Replacing \"gentleman/lady\"? Example: Such a friendly {b}lady{/b}!", length=15)
                gentleman = gentleman.strip() or "gentleperson"
            python:
                king = renpy.input("Replacing \"king/queen/monarch\"? Example: Yass {b}queen{/b}!", length=15)
                king = king.strip() or "monarch"
            python:
                bf = renpy.input("Replacing \"boyfriend/girlfriend/partner\"? Example: Oh, them? They're my {b}girlfriend{/b}.", length=15)
                bf = bf.strip() or "significant other"
    show demencia at center with move
    d "Amazing, sorry if that may have taken a while!"
    d "Now then!"
    d "Here there would be appearance talk, but right now we don't have the necessary assets!"
    show demencia at left with move
    d "You got this, [bro]! Hope you become the [bf] of the finest sexymen straight from Tumblr!" # see the readability helps!!
    d "Ta-ta for now! Enjoy the game <3"
    call main
    #call sans4
return
