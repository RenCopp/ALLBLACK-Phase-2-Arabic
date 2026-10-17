



init python:



    def chromatic_function(child, offset=3, **properties):
        return Fixed(
            At(child, Transform(xoffset=0, gl_color_mask=(False, True, False, True))),
            At(child, Transform(xoffset=-offset, gl_color_mask=(True, False, False, True))),
            At(child, Transform(xoffset=offset, gl_color_mask=(False, False, True, True))),
            fit_first=True,
            **properties)




    Chromatic = renpy.curry(chromatic_function)   



init:

    python:

        import math

        class Shaker(object):
            
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
            
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                
                self.start = [ self.anchors.get(i, i) for i in start ]  
                self.dist = dist    
                self.child = child
            
            def __call__(self, t, sizes):
                
                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                
                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
                
                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                
                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):
            
            move = Shaker(start, child, dist=dist)
            
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)                                             


init:
    $ shakehard = Shake((0, 0, 0, 0), 2.0, dist=30)



init:

    image cg2 = Image("cg/cg2.jpg")
    image cg2a = im.Alpha("cg/cg2a.jpg", 0.5)
    image cg2b = im.Alpha("cg/cg2b.jpg", 0.5)
    image cg2c = im.Alpha("cg/cg2c.jpg", 0.5)
    image store_drunk = im.Alpha("bg/store.jpg", 0.5)
    image overpass_drunk = im.Alpha("bg/overpass.jpg", 0.2)
    image hotel_inverted_alpha = im.Alpha( im.MatrixColor("bg/child.png", im.matrix.invert()), 0.5)

    python hide:

        def gen_randmotion(count, dist, delay):
            
            import random
            
            args = [ ]
            
            for i in range(0, count):
                args.append(anim.State(i, None,
                                       Position(xpos=random.randrange(-dist, dist),
                                                ypos=random.randrange(-dist, dist),
                                                xanchor='left',
                                                yanchor='top',
                                                )))
            
            for i in range(0, count):
                for j in range(0, count):
                    
                    if i == j:
                        continue
                    
                    args.append(anim.Edge(i, delay, j, MoveTransition(delay)))
            
            return anim.SMAnimation(0, *args)

        store.randmotion = gen_randmotion(30, 30, 1.0)   



init python:
    def eyewarp(x):
        return x**1.33
    eye_open = ImageDissolve("transition/eye.png", .5, ramplen=58, reverse=False, time_warp=eyewarp)
    eye_open_slow = ImageDissolve("transition/eye.png", 1.0, ramplen=58, reverse=False, time_warp=eyewarp)
    eye_shut = ImageDissolve("transition/eye.png", .5, ramplen=58, reverse=True, time_warp=eyewarp)
    eye_shut_slow = ImageDissolve("transition/eye.png", 1.0, ramplen=58, reverse=True, time_warp=eyewarp)
image black:
    Solid("#000")
image white:
    Solid("#FFF")
image red:
    Solid("#ff0000")



image static:
    "transition/noise1.png" with Dissolve(0.2)
    0.1
    "transition/noise2.png" with Dissolve(0.2)
    0.1
    "transition/noise3.png" with Dissolve(0.2)
    0.1
    "transition/noise4.png" with Dissolve(0.2)
    0.1
    "transition/noise5.png" with Dissolve(0.2)
    repeat

image static2:
    im.Alpha("transition/noise1.png", 0.5) with Dissolve(0.2)
    0.1
    im.Alpha("transition/noise2.png", 0.5) with Dissolve(0.2)
    0.1
    im.Alpha("transition/noise3.png", 0.5) with Dissolve(0.2)
    0.1
    im.Alpha("transition/noise4.png", 0.5) with Dissolve(0.2)
    0.1
    im.Alpha("transition/noise5.png", 0.5) with Dissolve(0.2)
    0.1
    repeat



image ctc1 = Animation("gui/ctc/ctc1.webp", 0.3, "gui/ctc/ctc2.webp", 0.2, "gui/ctc/ctc3.webp", 0.5, "gui/ctc/ctc2.webp", 0.2, "gui/ctc/ctc1.webp", 0.3, xoffset=10, yoffset = 0)





transform center:
    xanchor 0.5 xpos 0.5 ypos 0.5

transform center_offset:
    xanchor 0.5 xpos 0.5 ypos 100

transform right_offset:
    xanchor 0.5 xpos 0.75 ypos 100

transform right_offset_surprised:
    xanchor 0.5 xpos 0.75 ypos 100
    linear 0.1 ypos 75
    linear 0.1 ypos 100

transform left_offset:
    xanchor 0.5 xpos 0.35 ypos 100



transform dash:
    xanchor 0.5 xpos 0.35 ypos 100
    linear 0.1 xpos 0.65
    linear 0.1 xpos 0.35

transform fightback:
    xanchor 0.5 xpos 0.75 ypos 100
    linear 0.1 xpos 0.4
    linear 0.1 xpos 0.75

transform kill:
    xanchor 0.5 xpos 0.75 ypos 100
    linear 0.1 xpos 0.4

transform thrown:
    xanchor 0.5 xpos 0.4 ypos 100
    linear 0.1 xpos 0.75

transform impact_small:
    xanchor 0.5 xpos 0.35 ypos 100
    linear 0.1 xpos 0.25
    linear 0.1 xpos 0.35

transform thug_dodge:
    xanchor 0.5 xpos 0.75 ypos 100
    linear 0.1 xpos 0.85
    linear 0.1 xpos 0.75

transform dodge:
    xanchor 0.5 xpos 0.35 ypos 100
    linear 0.1 xpos 0.3
    linear 0.1 xpos 0.35

transform fight:
    xanchor 0.5 xpos 0.3 ypos 100
    linear 0.1 xpos 0.35

transform kudakuda:
    xanchor 0.5 xpos 0.35 ypos 100
    linear 0.2 xpos 0.3
    linear 0.2 xpos 0.35

transform charge:
    xanchor 0.5 xpos 0.35 ypos 100
    linear 0.1 xpos 0.65
    linear 0.1 xpos 0.35

transform falldown:
    xanchor 0.5 xpos 0.35 ypos 100
    linear 0.1 ypos 70
    linear 0.2 xanchor 0.5 xpos 0.35 ypos 1100




transform ct_left_offset:
    xanchor 0.5 xpos 0.3 ypos 80



transform al_left_offset:
    xanchor 0.5 xpos 0.3 ypos 200

transform al_left_offset_surprised:
    xanchor 0.5 xpos 0.3 ypos 200
    linear 0.1 ypos 175
    linear 0.1 ypos 200



transform center_small:
    xanchor 0.5 xpos 0.5 ypos 300

transform left_small:
    xanchor 0.5 xpos 0.2 ypos 300

transform right_small:
    xanchor 0.5 xpos 0.8 ypos 300




transform base:
    xalign 0.0 yalign 0.0

transform sill:
    xanchor 0.5 xpos 0.5 ypos 0






image hotel_animated:
    "bg/hotel.jpg" with Dissolve(2.0)
    pause 2.0
    im.MatrixColor("bg/hotel.jpg", im.matrix.brightness(-0.2)) with Dissolve(2.0)
    pause 2.0
    repeat




define fast_fade = Fade(0.2, 0.0, 0.2)
define slow_fade = Fade(2.0, 0.0, 2.0)
define slow_dissolve = Dissolve(2.0)
define slow_slow_dissolve = Dissolve(3.0)
define fast_dissolve = Dissolve(0.2)
define eyeshut = ImageDissolve("transition/eyeshut.webp", 1.0, 8)
define eyeshut2 = ImageDissolve("transition/eyeshut2.png", 2.0, 8, reverse=True)
define vignette = ImageDissolve("transition/vignette.webp", 2.0, 8)
define eyeshutfast = ImageDissolve("transition/eyeshut.webp", .2, 8)
define eyeopenfast = ImageDissolve("transition/eyeshut.webp", .2, 8, reverse=True)
define shatter = ImageDissolve("transition/shatter.webp", 0.8, 8)
define steam = ImageDissolve("transition/steam.webp", 2.0, 8)
define flashbulb = Fade(2.0, 0.0, 2.0, color='#fff')
define wipeleft_fast = CropMove(0.4, "wipeleft")
define wiperight_fast = CropMove(0.4, "wiperight")
define teleport = ImageDissolve("transition/teleport.png", 1.0, 0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
