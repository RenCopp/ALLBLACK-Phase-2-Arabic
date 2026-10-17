image theoblink:
    "sprites/theo/eyes_open.png"
    3.0
    "sprites/theo/eyes_half.png"
    0.1
    "sprites/theo/eyes_closed.png"
    0.5
    "sprites/theo/eyes_half.png"
    0.1
    repeat

layeredimage theo1:
    always:
        "sprites/theo/theobase1.png"
    attribute sweat:
        "sprites/theo/sweat.png"
    group eyes:
        attribute close:
            "sprites/theo/eyes_closed.png"
        attribute half_close:
            "sprites/theo/eyes_half.png"
        attribute picek:
            "sprites/theo/eyes_picek.png"
        attribute blink default:
            "theoblink"
    group eyebrows:
        attribute neutral:
            "sprites/theo/eyebrow_neutral.png"
        attribute angry default: 
            "sprites/theo/eyebrow_angry.png"
        attribute sad: 
            "sprites/theo/eyebrow_sad.png"
    group mouth:
        attribute shut:
            "sprites/theo/mouth_closed.png"
        attribute open:
            "sprites/theo/mouth_open.png"
        attribute shout:
            "sprites/theo/mouth_shout.png"
        attribute pain:
            "sprites/theo/mouth_pain.png"

layeredimage theo2:
    always:
        "sprites/theo/theobase2.png"
    attribute sweat:
        "sprites/theo/sweat.png"
    group eyes:
        attribute close:
            "sprites/theo/eyes_closed.png"
        attribute half_close:
            "sprites/theo/eyes_half.png"
        attribute picek:
            "sprites/theo/eyes_picek.png"
        attribute blink default:
            "theoblink"
    group eyebrows:
        attribute neutral:
            "sprites/theo/eyebrow_neutral.png"
        attribute angry default: 
            "sprites/theo/eyebrow_angry.png"
        attribute sad: 
            "sprites/theo/eyebrow_sad.png"
    group mouth:
        attribute shut:
            "sprites/theo/mouth_closed.png"
        attribute open:
            "sprites/theo/mouth_open.png"
        attribute shout:
            "sprites/theo/mouth_shout.png"
        attribute pain:
            "sprites/theo/mouth_pain.png"

layeredimage theo3:
    always:
        "sprites/theo/theobase3.png"
    attribute sweat:
        "sprites/theo/sweat.png"
    group eyes:
        attribute half_close:
            "sprites/theo/eyes_half.png"
        attribute picek:
            "sprites/theo/eyes_picek.png"
        attribute close:
            "sprites/theo/eyes_closed.png"    
        attribute blink:
            "theoblink"
    group eyebrows:
        attribute neutral:
            "sprites/theo/eyebrow_neutral.png"
        attribute angry default: 
            "sprites/theo/eyebrow_angry.png"
        attribute sad: 
            "sprites/theo/eyebrow_sad.png"
    group mouth:
        attribute shut default:
            "sprites/theo/mouth_closed.png"
        attribute open:
            "sprites/theo/mouth_open.png"
        attribute shout:
            "sprites/theo/mouth_shout.png"
        attribute pain:
            "sprites/theo/mouth_pain.png"
    attribute hand default:
        "sprites/theo/theooverlay3.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
