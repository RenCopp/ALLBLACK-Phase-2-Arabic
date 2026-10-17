layeredimage thug:
    always:
        "sprites/thug/thug base.png"
    attribute sweat:
        "sprites/thug/sweat.png"
    attribute knife:
        "sprites/thug/knife.png"
    group mouth:
        attribute shut default:
            "sprites/thug/mouth_shut.png"    
        attribute sigh:
            "sprites/thug/mouth_sigh.png"       
        attribute open:
            "sprites/thug/mouth_open.png"       

layeredimage thug_blur:
    always:
        im.Blur("sprites/thug/thug base.png", 2.0)
    attribute sweat:
        im.Blur("sprites/thug/sweat.png", 2.0)
    attribute knife:
        im.Blur("sprites/thug/knife.png", 2.0)
    group mouth:
        attribute shut default:
            im.Blur("sprites/thug/mouth_shut.png", 2.0)
        attribute sigh:
            im.Blur("sprites/thug/mouth_sigh.png", 2.0)       
        attribute open:
            im.Blur("sprites/thug/mouth_open.png", 2.0)           
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
