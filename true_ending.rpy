# https://www.renpy.org/doc/html/
define k = Character("Kibble")

label trueEnd:

return


label sansrei:
    define k = Character("Kibble")
    show sans at hi
    show reigen at hi, left
    s "* sans"
    s "* sans"
    s "* sans"
    s "* weiner"

    show reigen blush
    r "{i}(What the hell?? He's so cute??){/i}"
    show sans wink
    s "* hey bbg. do ya like what ya see?"
    r "..!!"
    menu:
        "Attempt to stop the two":
            if s_love > r_love:
                "You attempt to distract Sans."
                you "Hey Sans! Come check out this deformed baby!"
                show kibble at right
                k "Hi!!1!1!1!11!"
                s "* woah [bro]. that is one deformed baby."
                k "Poop"
                r "Tf??? Is that a ghost?? Don't worry, I can get rid of it!"
                "Reigen throws salt onto the deformed baby."
                hide kibble
                "The baby explodes."
                show reigen think 2
                r "{i}(It actually worked??){/i}"
                show reigen ofc
                r "Haha! Exterminated!"
                s "* good job."
                $ reiLove += 20
                $ renpy.notify("Reigen's love for Sans: " + str(reiLove))
                r "Thank you~"
                call mainLoop

            else:
                "I attempt to distract Reigen."
                you "Reigen! Look! A deformed baby!"
                show kibble at hi, right
                k "deez nuts"
                show sans shock
                show reigen huh
                r "What? Eww!!"
                show sans bwink
                "Sans uses his powers to destroy the baby."
                hide kibble
                s "* gottem."
                r "Thanks so much, Sans!"
                $ sansLove += 10
                $ renpy.notify("Sans' love for Reigen: " + str(sansLove))
                show sans blush
                s "* n-no problem bro."
                call mainLoop

        "Let them continue on":
            pass
    show reigen oh2
    r "I just might. What's it to ya?"
    s "* heh. you're a cutie"
    show reigen blush
    extend " let's go out sometime. to grillby's. my treat."
    $ reiLove += 150
    $ renpy.notify("Reigen's love for Sans: " + str(reiLove))
    show reigen think2
    r "Grill... by's..?"
    s "* yep!"
    show reigen blush
    r "I just-{nw}"
  # note to add a shaking effect
    r "I um-{nw}"
    r "I--{nw}"
    "Reigen covers his face."
    r "..A-Alright."
    show sans blush
    s "* sweet. meet me at closing time."
    hide reigen
    "Reigen giggles off like a teenager."
    $ r_love = 0
    $ s_love = 0
    # they're just that loyal to one another <3
    scene bg black with fade
    call mainLoop
return

label sansrei2:
    show sans at hi
    s "* oh hey [bro]."
    s "* you know reigen? the dude with the blonde-ish hair?"
    show sans blush
    s "* haha.. um."
    s "* we're...{w=0.3} we're dating."
    s "* ...yeah."
    you "I'm happy for you, Sans!"
    show sans
    s "* thanks a bunch, [bro]."
    show sans wink
    s "* i've never really been happier."
    show sans heh
    s "* well...{w=0.3} aside from that time me and papyrus went trash collecting."
    s "* who knew about the stuff you'd find in a dump?"
    s "* one man's trash is another man's treasure!"
    show sans blush
    s "* but still. he means the world to me."
    s "* ...and, i'd honestly never want anyone else."
return











# random space









label williamReveal:
show vincent at hi
v "Oh, why hello [name]!"
v ""
$ williamReveal = True

return

label billReveal:
$ billIsHuman = True

return



# renpy.call ()
init python:
  def addLove(characterName, amount):
    firstLetter = characterName[:1]
    
    eval(firstLetter[0] + "_love" += amount)
     $ renpy.notify(str(characterName) + " love for you: " + str(eval(firstLetter[0] + "_love"))
