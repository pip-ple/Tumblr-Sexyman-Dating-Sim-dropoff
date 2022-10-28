# https://www.renpy.org/doc/html/
define k = Character("Kibble")

label trueEnd:

return


label sansrei:

  show sans at hi
  show reigen at hi, left
  s "* sans"
  s "* sans"
  s "* sans"
  s "* weiner"
  
  show reigen blush 
  r "{i}(What the hell?? He's so cute??){/i}"
  show sans heh
  s "* hey bbg. do ya like what ya see?"
  r "..!!"
  menu:
    "Attempt to stop the two.":
      python:
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
          show reigen
          r "What? Eww!!"
          show sans blue wink
          "Sans uses his powers to destroy the baby."
          s "* gottem."
          r "Thanks so much, sans!"
          $ sansLove += 10
          $ renpy.notify("yeah" + sansLove)
          show sans blush
          s "* n-no problem bro."
          
          call mainLoop
    "Let them continue on":
      pass
  show reigen hmph
  r "I just might. What's it to ya?"
  s "* heh. you're a cutie"
  show reigen blush
  extend " let's go out sometime. to grillby's. my treat."
  $ reiLove += 150
  $ renpy.notify("Reigen's love for Sans: " + str(reiLove))
  r "Grill... by's..?"
  s "* yep!"
  r "I just-{nw}"
  # note to add a shaking effect
  r "I um-{nw}"
  r "I--{nw}"
  "Reigen covers his face"
  r "..A-Alright."
  show sans blush
  s "* sweet. meet me at closing time."
  "Reigen giggles off like a teenager."
  $ r_love = 0
  $ s_love = 0
  # they're just that loyal to one another <3
  scene bg black with fade
  call mainLoop
return

label sansRei2:
  show sans at hi, right
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
  show sans
  s "* but still. he means the world to me"
  
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
