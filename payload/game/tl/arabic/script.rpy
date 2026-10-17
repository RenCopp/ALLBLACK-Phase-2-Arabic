

init -100 python:
    def callback(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx/keyboard.mp3", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")




init:

    define nar = Character(None, ctc="ctc1",  kind=nvl, ctc_position="nestled")
    define nar2 = Character(None, ctc="ctc1",  kind=nvl, xalign=0.5, yalign=0.5, ctc_position="nestled")

    define u = Character("???", who_prefix="{color=[u_color]}", who_suffix="{/color}", what_prefix="{color=[u_color]}", what_suffix="{/color}", kind=nvl, italic=False, what_italic=False, ctc="ctc1", ctc_position="nestled")
    default u_color = "#66c1e0"

    define up = Character("???", who_prefix="{color=[up_color]}", who_suffix="{/color}", what_prefix="{color=[up_color]}" + '[[', what_suffix= ']' + "{/color}" , kind=nvl, italic=True, what_italic=True, ctc="ctc1", ctc_position="nestled")
    default up_color = "#66c1e0"

    define ut = Character(_("Theodore?"), who_prefix="{color=[ut_color]}", who_size=28, who_suffix="{/color}", what_prefix="{color=[ut_color]}" + '[[', what_suffix= ']' + "{/color}" , kind=nvl, who_italic=True, what_italic=True, ctc="ctc1", ctc_position="nestled")
    default ut_color = "#66c1e0"

    define ap = Character("???", who_prefix="{color=[ap_color]}", who_suffix="{/color}", what_prefix="{color=[ap_color]}" + '[[', what_suffix= ']' + "{/color}" , kind=nvl, italic=True, what_italic=True, ctc="ctc1", ctc_position="nestled")
    default ap_color = "#ff80df"

    define al = Character("???", who_prefix="{color=[al_color]}", who_suffix="{/color}", what_prefix="{color=[al_color]}" , what_suffix= "{/color}" , kind=nvl, italic=True, what_italic=True, ctc="ctc1", ctc_position="nestled")
    default al_color = "#ff80df"

    define p = Character("???", who_prefix="{color=[p_color]}", who_suffix="{/color}", what_prefix="{color=[p_color]}", what_suffix="{/color}", kind=nvl, italic=True, what_italic=True, ctc="ctc1", ctc_position="nestled")
    default p_color = "#b3b3cc"

    define boss = Character("???", who_prefix="{color=[boss_color]}", who_suffix="{/color}", what_prefix="{color=[boss_color]}", what_suffix="{/color}", kind=nvl, ctc="ctc1", ctc_position="nestled")
    default boss_color = "#ffff4d"

    define ein = Character(_("Einhorn?"), who_prefix="{color=[ein_color]}", who_size=28, who_suffix="{/color}", what_prefix="{color=[ein_color]}", what_suffix="{/color}", kind=nvl, ctc="ctc1", ctc_position="nestled")
    default ein_color = "#ffff4d"



    define pw = Character(None, kind=nvl, callback=callback, what_xalign=0.5, window_xalign=0.5, window_yalign=0.5, what_text_align=0.5, ctc="ctc1", ctc_position="nestled")

    define sub = Character(None,
                            what_size=22,
                            what_color="000000",
                            what_layout="subtitle",
                            what_xalign=0.5,
                            what_text_align=0.5,
                            window_background=None,
                            window_yminimum=700,
                            window_xfill=True,
                            window_xalign=0.5)



init:
    define narrator = Character(ctc="ctc1", ctc_position="nestled")


    define f = Character(_("Ferno"), color="66c1e0",  ctc="ctc1", bold = True, ctc_position="nestled")
    define t = Character(_("Theodore"), color="66c1e0",  ctc="ctc1", bold = True, ctc_position="nestled")
    define girl0 = Character(_("Girl"), color="ffffff",  ctc="ctc1", bold = True, ctc_position="nestled")
    define al0 = Character(_("???"), color="#ff80df",  ctc="ctc1", bold = True, ctc_position="nestled")
    define al = Character(_("Alisa"), color="#ff80df",  ctc="ctc1", bold = True, ctc_position="nestled")
    define u = Character(_("???"), color="#c7c7c7",  ctc="ctc1", bold = True, ctc_position="nestled")
    define m = Character(_("Magdalene"), color="#a86165",  ctc="ctc1", bold = True, ctc_position="nestled")
    define thug = Character(_("Thug"), color="#c7c7c7",  ctc="ctc1", bold = True, ctc_position="nestled")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
