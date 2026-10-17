# ALLBLACK Phase 1 Arabic localization support.
# Remove this file, its compiled .rpyc, and game/tl/arabic to uninstall.

# Arabic is the default when the game starts. The language buttons still allow
# another language to be selected for the current session.
init -99 python:
    config.language = "arabic"
    # Apply RTL immediately on startup. The language-change callback runs
    # only after the first interaction, which leaves the opening text left-
    # aligned when Arabic is selected as the default language.
    config.rtl = True

    # Ren'Py 7.3 can leave text fragments following inline tags (for example
    # {w=1}) as UTF-8 byte strings. Its bidi extension accepts Unicode only,
    # so normalize every RTL text segment before shaping it.
    _allblack_original_rtl_paragraph = renpy.text.text.Layout.rtl_paragraph

    def _allblack_unicode_rtl_paragraph(self, paragraph):
        fixed = []
        for text_style, segment in paragraph:
            if isinstance(segment, str):
                segment = segment.decode("utf-8", "replace")
            fixed.append((text_style, segment))
        return _allblack_original_rtl_paragraph(self, fixed)

    renpy.text.text.Layout.rtl_paragraph = _allblack_unicode_rtl_paragraph

    # Ren'Py 7.3 reverses wrapped RTL lines after assigning slow-text times.
    # That leaves the lower line with earlier timestamps, so it appears all at
    # once after the upper line finishes. Preserve the original timing values
    # (including pauses), but assign them in visual reading order: top to
    # bottom, and right to left within each line.
    _allblack_original_layout_init = renpy.text.text.Layout.__init__

    def _allblack_rtl_line_timing(self, *args, **kwargs):
        _allblack_original_layout_init(self, *args, **kwargs)

        # Size-only layouts return before Ren'Py creates the `lines` member.
        # They do not draw slow text and require no timing correction.
        lines = getattr(self, "lines", None)
        if not renpy.config.rtl or not lines:
            return

        timed_glyphs = []
        reading_order = []

        for line in lines:
            for glyph in line.glyphs:
                if glyph.time >= 0:
                    timed_glyphs.append(glyph)

            for glyph in reversed(line.glyphs):
                if glyph.time >= 0:
                    reading_order.append(glyph)

        times = sorted(glyph.time for glyph in timed_glyphs)

        for glyph, glyph_time in zip(reading_order, times):
            glyph.time = glyph_time

        self.max_time = renpy.text.text.textsupport.max_times(lines)

    renpy.text.text.Layout.__init__ = _allblack_rtl_line_timing

    def _allblack_arabic_language_changed():
        config.rtl = (renpy.game.preferences.language == "arabic")

    if _allblack_arabic_language_changed not in config.change_language_callbacks:
        config.change_language_callbacks.append(_allblack_arabic_language_changed)

    _allblack_previous_replace_text = config.replace_text

    def _allblack_replace_text(value):
        if _allblack_previous_replace_text is not None:
            value = _allblack_previous_replace_text(value)
        if renpy.game.preferences.language == "arabic":
            value = value.replace(u"Chapter : ", u"الفصل: ")
            value = value.replace(u"Playtime  ", u"مدة اللعب  ")
            value = value.replace(u"Now Playing : ", u"المقطوعة الحالية: ")
        return value

    config.replace_text = _allblack_replace_text

# The original save/load screen reads these before a chapter has necessarily
# assigned them. Defaults prevent the pre-existing NameError on the main menu.
default scene_name = ""
default bgm_name = ""

translate arabic python:
    # Noto Sans Arabic supplies Arabic shaping; DejaVu Sans supplies Latin,
    # Greek, arrows, and UI symbols that would otherwise appear as squares.
    # Spaces and the ASCII punctuation present in Noto must also stay in the
    # Noto run. If spaces fall through to DejaVu, Ren'Py 7.3 splits an Arabic
    # sentence into separate word segments and reverses their order.
    _allblack_arabic_font = FontGroup() \
        .add("NotoSansArabic.ttf", 0x0020, 0x0021) \
        .add("NotoSansArabic.ttf", 0x002c, 0x002e) \
        .add("NotoSansArabic.ttf", 0x0030, 0x003a) \
        .add("NotoSansArabic.ttf", 0x0600, 0x06ff) \
        .add("NotoSansArabic.ttf", 0x0750, 0x077f) \
        .add("NotoSansArabic.ttf", 0x08a0, 0x08ff) \
        .add("NotoSansArabic.ttf", 0xfb50, 0xfdff) \
        .add("NotoSansArabic.ttf", 0xfe70, 0xfeff) \
        .add("DejaVuSans.ttf", None, None)

    style.default.font = _allblack_arabic_font
    style.default.language = "unicode"

    gui.text_font = _allblack_arabic_font
    gui.name_text_font = _allblack_arabic_font
    gui.interface_text_font = _allblack_arabic_font
    gui.button_text_font = _allblack_arabic_font
    gui.choice_button_text_font = _allblack_arabic_font

    # Mirror the dialogue region and align Arabic text to its right edge.
    gui.dialogue_text_xalign = 1.0
    gui.nvl_text_xpos = 1150
    gui.nvl_text_xalign = 1.0
    gui.nvl_thought_xpos = 1080
    gui.nvl_thought_xalign = 1.0
    gui.nvl_button_xpos = 830
    gui.nvl_button_xalign = 1.0

    style.say_dialogue.text_align = 1.0
    style.nvl_dialogue.text_align = 1.0
    style.nvl_thought.text_align = 1.0
    style.history_text.text_align = 1.0

# The stock Preferences screen lists only the bundled languages. This small
# overlay adds a way to return to Arabic after selecting another language.
screen allblack_arabic_language_button():
    if renpy.get_screen("preferences"):
        textbutton "Arabic / العربية":
            action Language("arabic")
            text_font _allblack_arabic_font
            xalign 0.98
            yalign 0.96

init -98 python:
    if "allblack_arabic_language_button" not in config.overlay_screens:
        config.overlay_screens.append("allblack_arabic_language_button")

# Final style guard: the original project defines the say styles in the
# generated GUI file, and those definitions can override RTL alignment when
# the translated screen is loaded. Apply the Arabic font and text-box layout
# after all GUI definitions have been read.
init -97 python:
    _allblack_font_guard = FontGroup() \
        .add("NotoSansArabic.ttf", 0x0020, 0x0021) \
        .add("NotoSansArabic.ttf", 0x002c, 0x002e) \
        .add("NotoSansArabic.ttf", 0x0030, 0x003a) \
        .add("NotoSansArabic.ttf", 0x0600, 0x06ff) \
        .add("NotoSansArabic.ttf", 0x0750, 0x077f) \
        .add("NotoSansArabic.ttf", 0x08a0, 0x08ff) \
        .add("NotoSansArabic.ttf", 0xfb50, 0xfdff) \
        .add("NotoSansArabic.ttf", 0xfe70, 0xfeff) \
        .add("DejaVuSans.ttf", None, None)

    style.say_dialogue.font = _allblack_font_guard
    style.say_dialogue.language = "unicode"
    # Keep the dialogue widget anchored inside its original 60px inset and
    # align only the glyphs within its 1700px text area. Setting xalign on the
    # widget itself moved its right anchor to x=60 and clipped almost all text.
    style.say_dialogue.xalign = 0.0
    style.say_dialogue.xanchor = 0.0
    style.say_dialogue.text_align = 1.0
    style.say_dialogue.layout = "subtitle"
    style.say_label.font = _allblack_font_guard
    style.say_label.language = "unicode"
    style.say_label.xalign = 0.0
    style.say_label.xanchor = 0.0
    style.say_label.text_align = 1.0
    style.nvl_dialogue.font = _allblack_font_guard
    style.nvl_dialogue.language = "unicode"
    style.nvl_dialogue.xalign = 1.0
    style.nvl_dialogue.text_align = 1.0

