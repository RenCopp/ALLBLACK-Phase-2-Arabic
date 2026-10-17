image aliciablink:
    "sprites/alicia/eyes_open.png"
    5.0
    "sprites/alicia/eyes_half.png"
    0.1
    "sprites/alicia/eyes_closed.png"
    0.5
    "sprites/alicia/eyes_half.png"
    0.1
    repeat

layeredimage alicia1:
    always:
        "sprites/alicia/aliciabase1.png"
    attribute tears:
        "sprites/alicia/add_tears.png"
    attribute sweat:
        "sprites/alicia/add_sweat.png"
    attribute scary:
        "sprites/alicia/add_scary.png"
    attribute angryemote:
        "sprites/alicia/add_angry.png"
    group eyes:
        attribute close:
            "sprites/alicia/eyes_closed.png"
        attribute closehappy:
            "sprites/alicia/eyes_closedhappy.png"
        attribute blink default:
            "aliciablink"
    group eyebrows:
        attribute normal default:
            "sprites/alicia/eyebrow_normal.png"
        attribute angry: 
            "sprites/alicia/eyebrow_angry.png"
        attribute sad: 
            "sprites/alicia/eyebrow_sad.png"
    group mouth:
        attribute shut:
            "sprites/alicia/mouth_shut.png"
        attribute uuu:
            "sprites/alicia/mouth_uuu.png"    
        attribute openbit:
            "sprites/alicia/mouth_openbit.png"
        attribute openwide:
            "sprites/alicia/mouth_openwide.png"
        attribute sigh:
            "sprites/alicia/mouth_sigh.png"
        attribute smile:
            "sprites/alicia/mouth_smile.png"
        attribute smilewide:
            "sprites/alicia/mouth_smilewide.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
