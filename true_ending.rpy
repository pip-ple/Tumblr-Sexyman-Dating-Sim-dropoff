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
          $ reiLove = reiLove + 20
          $ renpy.notify("im not typing this in class: " + reiLove)
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
          $ sansLove = sansLove + 10
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
  
  scene bg black with fade
  call mainLoop
return
