# this DDLC-esque script defines every single TIRESOME image so i can write
# this MONSTROSITY of a game easier

# pronouns
# plural is gonna be hard omg

# important note!! he is the default here bc it helps me with readability!!
# singular and plural differences do get tricky... coding makes my
# eyes explode in general so please ignore this fact!!

default he = "he"
default he2 = he.title()
default him = "him"
default his = "his"
default hers = "hers"
default himself = "himself"

default guy = "guy"
default bro = "bro"
default man = "man"
default gentleman = "gentleman"
default king = "king"
default bf = "boyfriend"

default plural = False
default they = "they"
default them = "them"
default their = "their"
default theirs = "theirs"
default themself = "themself"

#default nameboxname = "You"
default name = "Y/N" # "Senor Fishyboy"
default lowercase_name = "y/n"
default upper_name = "Y/N"

# other

default billIsHuman = False

# backgrounds

image bg black = "bg/bg_black.png"
image bg white = "bg/bg_white.png"
image bg cafe = "bg/bg_cafe_placeholder.png"
image bg placeholder = "bg/bg_placeholder.png"
image bg outside = "bg/bg_placeholder_outside.jpg"

## characters (the hellhole itself)

# warden

image warden = "warden/normal.png"
image warden 2 = "warden/normal2.png"
image warden oh = "warden/oh.png"
image warden push = "warden/push.png"
image warden think = "warden/well.png"
image warden think2 = "warden/well2.png"
image warden woah = "warden/woah.png"
image warden grr = "warden/hmm.png"
image warden shrug = "warden/shrug.png"
image warden blush = "warden/blush.png"

# afton

image vincent = "vincent/neutral.png"
image vincent smirk = "vincent/giggles.png"
image vincent huh = "vincent/huh.png"
image vincent bruh = "vincent/bruh.png"

image vincent paint = "vincent/paint/neutral.png"
image vincent paint golly = "vincent/paint/golly.png"
image vincent paint reveal = "vincent/paint/reveal.png"

image vincent william = "vincent/willy/neutral.png"
image vincent william plot = "vincent/willy/plotting.png"
image vincent william huh = "vincent/willy/huh.png"
image vincent william smirk = "vincent/willy/smirk.png"
image vincent william bruh = "vincent/willy/tankman_ugh.png"
image vincent william blush = "vincent/willy/blush.png"

image dave = "him/unhinged.png"

# sans

image sans = "sans/neutral.png" # check if this'll hide every sans and not just this one
image sans haha = "sans/neutral2.png"
image sans heh = "sans/heh.png"
image sans wink = "sans/wink.png"
image sans srs = "sans/srs.png"
image sans think = "sans/think.png"
image sans blush = "sans/blush.png"
image sans shock = "sans/shock.png"
image sans weiner = "sans/weiner.png" # hey kid you want a weiner in your mouth /ref

image sans b:
    "sans/blue_neutral.png"
    pause .3
    "sans/yellow_neutral.png"
    pause .3
    repeat
image sans bwink:
    "sans/blue_wink.png"
    pause .3
    "sans/yellow_wink.png"
    pause .3
    repeat

image sans ne = "sans/no_neutral.png"
image sans ne srs = "sans/no_srs.png"

# bill

image bill = "bill/neutral.png"
image bill 2 = "bill/neutral2.png"
image bill ugh = "bill/ugh.png"
image bill well = "bill/well.png"
image bill what = "bill/what.png"
image bill nerd = "bill/nerd.png"
image bill hmph = "bill/hmphh.png"

image bill human = "bill/human/neutral.png"
image bill human 2 = "bill/human/neutral2.png"
image bill human hmph = "bill/human/hmph.png"
image bill human smirk = "bill/human/smirk.png"
image bill human um = "bill/human/umm.png"
image bill human yipy = "bill/human/yay.png"
image bill human redeye = "bill/human/red.png"
image bill human blush = "bill/human/blush.png"

image bill human red = "bill/human/neutral.png"
image bill human red 2 = "bill/human/neutral.png"

# ronald reigen

image reigen = "reigen/neutral.png"
image reigen 2 = "reigen/neutral2.png"
image reigen huh = "reigen/huh.png"
image reigen oh = "reigen/oh.png"
image reigen oh2 = "reigen/oh2.png"
image reigen ofc = "reigen/ofc.png"

image reigen think = "reigen/think.png"
image reigen think2 = "reigen/think2.png"
image reigen blush = "reigen/blushes.png"

# benrey
image benrey = "benrey/neutral.png"
image benrey 2 = "benrey/neutral2.png"
image benrey bubbles = "benrey/bubbles.png"
image benrey point = "benrey/point.png"
image benrey point2 = "benrey/point2.png"
image benrey blush = "benrey/blush.png"
image benrey hm = "benrey/hm.png"
image benrey haha = "benrey/haha.png"


# demencia (im so spelling this wrong)

image demencia = "demencia/neutral.png"
image demencia 2 = "demencia/ofc.png"
image demencia wink = "demencia/yep.png"

# cameos

image kibble = "cameos/kibble.png"
## sounds

define audio.weiner = "audio/weiner.mp3"

define audio.sans = "audio/sans.ogg"

## every sexyman's love 4 u

default b_love = 0
default o_love = 0
default w_love = 0
default s_love = 0
default r_love = 0
default v_love = 0

# true ending stuff

default sansLove = 0
default reiLove = 0

## transforms

transform bounce:
    linear 3.0 xalign 1.0
    linear 3.0 xalign 0.0
    repeat

transform headright:
    linear 15 xalign 1.0

transform tcommon(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:

        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03


transform jitter(x = 640): # 0 is the left, 1 is the right
    linear 3.0 xalign 0.4
    linear 3.0 xalign 0.6
    repeat

transform hi: # current bug - hi, left will work, not the other way around </3
    yalign 1.0
    xcenter 0.5
    on show:
        alpha 0.0
        linear .5 alpha 1.0
    on hide:
        linear .5 alpha 0.0


# functions
init python:
    def love(int):
        w_love == w_love + int
        renpy.notify("wardens love 4 u: " + str(w_love))
        return


label splashscreen:
    scene bg white
    with Pause(1)

    show text "TW: Slight gore, cursing, and a bit of sexual references\nPlease be warned!" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    $ config.main_menu_music = "audio/meatball_parade.ogg"
    $ renpy.music.play(config.main_menu_music, fadein=1, loop=True)
    #play music "audio/meatball_parade.ogg" fadein 1.0

    show text "Drain Gang Presents..!" with dissolve
    with Pause(1)

    hide text with dissolve
    with Pause(1)

    return
