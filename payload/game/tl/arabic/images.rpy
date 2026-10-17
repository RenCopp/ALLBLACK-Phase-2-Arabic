




image hotel = "bg/hotel.jpg"
image hotel_dark = im.MatrixColor("bg/hotel.jpg", im.matrix.contrast(0.7) * im.matrix.brightness(-0.3))
image flashback = im.Grayscale("bg/flashback.jpg")
image corridor = "bg/corridor.jpg"
image hotel inverted = im.MatrixColor("bg/hotel.jpg", im.matrix.invert())
image street_night = "bg/street_night.jpg"
image street_night_blur = im.Blur("bg/street_night.jpg", 2.0)
image store = "bg/store.jpg"
image store_blur = im.Blur("bg/store.jpg", 2.0)
image overpass = "bg/overpass.jpg"
image overpass_effect = "bg/overpass_effect.jpg"
image overpass_blur = im.Blur("bg/overpass.jpg", 3.0)
image traffic = "bg/traffic.jpg"
image night_sky = "bg/night_sky.jpg"
image night_sky_blur = im.Blur("bg/night_sky.jpg", 3.0)
image eyeshut2 = "transition/eyeshut2.png"

image orphanage = "bg/orphanage.jpg"





image alicia = ConditionSwitch("_last_say_who == 'al'", "sprites/al.png","not _last_say_who == al",im.MatrixColor("sprites/al.png", im.matrix.contrast(0.7) * im.matrix.brightness(-0.2)))
image white_girl = (im.Scale("sprites/white girl.webp", 1920, 1080, bilinear=True))
image white_alicia_small = (im.FactorScale("sprites/alicia/aliciaghost.png", 0.8, bilinear=True))
image white_alicia = "sprites/alicia/aliciaghost.png"

image thug_dark = im.MatrixColor(
    "sprites/thug/thug base.png",
    im.matrix.brightness(-1))

image madam = "sprites/sample madam.png"
image theo_child = "sprites/sample theo child.png"




image cg1a = "cg/cg1a.jpg"
image cg1b = "cg/cg1b.jpg"
image cg1c = "cg/cg1c.jpg"
image cg2 = "cg/cg2.jpg"
image cg2_blur = im.Blur("cg/cg2.jpg", 2.0)
image cg2d_blur = im.Blur("cg/cg2d.jpg", 2.0)
image cg2e_blur = im.Blur("cg/cg2e.jpg", 2.0)
image cg3 = (im.FactorScale("cg/cg3.jpg", 0.6, bilinear=True))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
