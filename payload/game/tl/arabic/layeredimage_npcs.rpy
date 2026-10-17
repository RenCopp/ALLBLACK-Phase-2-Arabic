layeredimage thug:
    always:
        "الـ (سبريتس) والـ (ثغ) والـ (ثغ)"
    attribute sweat:
        "السبيتات/الثغ/العرق"
    attribute knife:
        "الـ (سبريتس) / الـ (ثغ) / السكين"
    group mouth:
        attribute shut default:
            "الـ (سبريتس) / (ثغ) / (الفم)"    
        attribute sigh:
            "الـ (سبريتس) / الـ (ثغ) / الفم"       
        attribute open:
            "الـ\"سبريتس\"/الـ\"ثغ\"/الـ\"فم\""       

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
