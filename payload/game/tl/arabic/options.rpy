













define config.name = _("ALLBLACK Phase 2")





define gui.show_name = False




define config.version = "0.1"





define gui.about = _p("""{b}Original story{/b} : {a=https://twitter.com/fscchan}Anssen "{i}fsc{/i}" Augustus{/a}\n\n{b}Original character design{/b} : Ekkigo\n\n{b}Visual Novel adaptation{/b} : {a=https://twitter.com/mad_scientist92}Mad Scientist{/a}\n
    {b}Editor and Proofreader{/b} : {a=https://pyrrhaiphis.itch.io/}Charlotte Benton{/a} (PyrrhaIphis), {a=https://twitter.com/UltraShiko}UltraShiko{/a}\n
    {b}Hand-drawn background and main menu art{/b} : {a=https://www.pixiv.net/en/users/12079685}Satya Rizqi{/a}\n
    {b}Background photos{/b} : Unsplash photo collection, Cureus Journal, Pixabay, Pexels\n
    {b}Music and Sound Effects{/b} : Kevin MacLeod (Incompetech.com), Fesliyan Studios, SoundJay, FreeSound, ZapSplat, Purple Planet Music
""")






define build.name = "ALLBLACKPhase2"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True
























define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = Dissolve(2.0)
define config.end_splash_transition = Dissolve(2.0)
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 50





default preferences.afm_time = 15
















define config.save_directory = "ALLBLACKPhase2-1610189363"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.docx', None)
    build.classify('**.txt', None)









    build.documentation('*.html')
    build.documentation('*.txt')


    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("music", "all")
    build.classify("game/**.rpyc", "scripts")
    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")
    build.classify("game/**.webp", "images")
    build.classify("game/**.mp3","music")
    build.classify("game/**.wav","music")
    build.classify("game/**.flac","music")
    build.classify("game/**.ogg","music")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
