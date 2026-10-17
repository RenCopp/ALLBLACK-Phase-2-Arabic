label start:

    $ quick_menu = True

    $ save_name = "η - Kindred Spirits"
    $ scene_name = "η - Kindred Spirits"
    $ bgm_name = "Breath"

    scene black
    play music "bgm/breath.mp3"

    $ text_var1 = _( "{font=nasal.ttf}{size=+10}η - Kindred Spirits \n(Part Seven){/size}{/font}" )

    show text text_var1 at center with dissolve
    pause 3.0
    hide text with dissolve


    $ achievement.grant("Achievement01_Start")
    init:
        $ achievement.register("Achievement01_Start")
        $ achievement.sync()

    $ achievement.sync()


    pw "{font=NotoSansArabic.ttf}{cps=20}{vspace=250}{color=00ff00}25 يونيو 2010\n\nفندق Strand Garden Motel\nوسط اسطنبول\n\n17:58\n\n\n{/color}{/cps}{/font}"
    nvl clear

    scene hotel_animated with dissolve
    $ renpy.pause (1.0, hard=True)

    show theo1 close shut sweat at center_offset with dissolve

    "يمكن أن يسرع معدل ضربات القلب وتنفسك بسبب النفوذ الناجم عن التنبؤ."

    "لكن عدم الصبر هو مجرد محفز الانتظار نفسه هو السبب"

    "التوقعات تجعلني ألاحظ أشياء كثيرة"

    "على سبيل المثال، أنا فقط لاحظت أن الحقائب كانت تشكل تحت عيني منذ أمس"

    "هذا منطقي، لم يكن لديّ سوى كوابيس مؤخراً"

    "منذ مومباسا، بالكاد كنت قادرا على الراحة على الإطلاق."

    "لكني أشعر بشعور مختلف عن ما كنت أشعر به في الماضي"

    "في ذلك الوقت لم أستطع النوم بسبب عدم الراحة والقلق، ولكن الآن لا أستطيع النوم بسبب الحماس."

    "وعندما كنت مستلقيا على السرير مع الساعة التصلب باستمرار والجو من الخارج، وأنا مستلقيا هنا، بانتظار صبيحة قادمة"

    "الوقت قاسي، يجب أن أعترف، أشعر وكأنه للأبد كلما كنت أنتظر، ومع ذلك يطير كلما كنت أستمتع."

    "{i}يجب أن تكون هنا في أي لحظة الآن.{i}"

    "{i}-أين هي؟{i}"

    "{i}هل ستأتي أم لا؟{i}"

    "كلما تحققت من الوقت، أستمر في طرح الأسئلة نفسها."

    "هذا ما تفعله عدم الصبر: يجعلني عالقاً في حلقة لا نهاية لها تحطم آمالي مراراً وتكراراً."

    show theo1 blink shut

    play sound "sfx/knock.mp3"
    "*طَرْق* *طَرْق*" with hpunch

    "اثنين من الضربات الصلبة تتردد في الغرفة؛ أصوات كسر لي من الانتظار القلق والعمل لي الارتفاع في الإثارة."

    scene flashback with dissolve
    $ renpy.pause (1.0, hard=True)

    "قابلتها في محطة الحافلات و أنتظرتها لمدة ساعتين"

    "ما زلت لا أعرف من هي، لكنني تمكنت من تأكيد هويتها كالشكل الأبيض من أحلامي."

    "أنا متحمسة، ليس فقط لأنها شخص من الماضي، ولكن شخص ما الذي يمكن أن يقول لي من أنا أيضا!"

    "إذا كانت هي التي ادعت أنها، ثم أنا لا أرى أي سبب لاثقة بها."

    scene hotel_animated with dissolve
    $ renpy.pause (1.0, hard=True)

    show theo1 shut sweat at center_offset with dissolve

    "ومع ذلك لا أستطيع أن أوقف الشعور بالتوتر"

    "ما كنت أبحث عنه في الأسبوع الماضي هو الآن يقف خلف الباب"

    play sound "sfx/doorhandle.wav"

    scene black with fade

    "مع القلق، أَمْشِي وَأَمْسَكُ مِنْ المُسْتَمْسَكِ."

    "وهناك كانت تلك الشخصية الصغيرة، تلك الشعر، و تلك الخصائص الوجهية، يجب أن تكون تلك الشخصية من أحلامي!"

    stop music fadeout 1.0

    scene corridor with wipeleft
    $ renpy.pause (1.0, hard=True)

    $ bgm_name = "Remembrance"
    play music "bgm/remembrance.mp3" fadein 1.0

    show alicia1 tears sad uuu at center_offset with dissolve

    "{i}[Vicky?]{/i}"

    "لا... هذه الفتاة لا يمكن أن تكون هي."

    "تبدو كشخص من ماضيّ، لكنّي لا أشعر بالحنين حولها..."

    scene cg1a:
        xalign 0.0 yalign 1.0
        linear 2.0 yalign 0.0

    t "آه .."

    "عندما رأيت الدموع تلمع من تحت عينيها، قبلتني."

    "لقد دفنت وجهها في صدري لم أستطع إلا أن أشعر بالقلق قليلاً لقد قابلتها بعد كل شيء"

    t "أنا...{w=1}...أوه"

    t "هلا تركتني، رجاءً؟"

    scene cg1b at base with dissolve

    al0 "-كلا ."

    "إنها تقول إنها تبحث عني منذ سنتين، لكن لماذا تبكي؟"

    "ربما هي سعيدة جداً لأنها وجدتني أخيراً؟"

    "لكن قبضتها كانت تصبح أكثر صرامة في كل ثانية أريد إنهاء هذا قبل أن يخرج من السيطرة"

    scene cg1c at base with dissolve

    "أَحْفِضُ ذراعِي حولها، خارج عُناقِها."

    "قريباً تركتني، وضعت يدها على صدري بدلاً من ذلك"

    "انها تضحك بينما لا تزال تخفي وجهها بعيدا عني."

    scene black with fade

    "بما أنني أعرف أنها تحتاج إلى هذا، أمتنع عن تركها تذهب."

    "استغرق الأمر وقتاً، لكنها تركتني في النهاية."

    scene corridor with wiperight
    $ renpy.pause (1.0, hard=True)

    show alicia1 tears sad smile at center_offset with dissolve

    "لحسن الحظ لم أكن بحاجة إلى حملها لفترة طويلة."

    al0 "إذاً، كيف حالك؟"

    t "أنا بخير، إذا كان هذا ما تسأله."

    al0 "لقد تغيرت كثيراً"

    t "ما الذي تعنيه؟"

    al0 "هل يمكننا التحدث بالداخل؟"

    "عندما أفكر بالأمر، ما زلنا نقف أمام الباب، نسيتُ ذلك لفترة."

    t "...أوه{w=1}بالطبع، ادخل"

    scene hotel_animated with wipeleft
    $ renpy.pause (1.0, hard=True)

    show alicia1 sad smile at al_left_offset with dissolve
    show theo1 sweat shut at right_offset with dissolve

    "يبدو أنها تتعارض مع الغرفة، لكن أعتقد أن هذا الفندق كان من أضعف المرتبات في المدينة"

    "عندما جلست في النهاية على السرير، انضمت إليها."

    t "ما الذي تعنيه بأنني تغيرت؟"

    "ابتساماتها الممتعة مختلفة تماماً عن الابتسامات السخيفة التي رأيتها على وجوه الجميع خلال الأسبوع الماضي"

    show alicia1 closehappy smilewide

    al0 "لقد أصبحت أطول"

    t "{cps=15}.....{/cps}"

    "ومع ذلك، هي تخرج نفس الهراء."

    "على عكس يومي المشرف الذي لعب معي فقط لإثارة لي، الطريقة التي هذه الفتاة تستهزئني تبدو مختلفة."

    "بطريقة ما، كلماتها لا تتركني أشعر بالإهانة."

    t "هاه؟"

    show alicia1 blink normal smile

    al0 "حقاً، المرة الماضية كنا تقريباً بنفس الارتفاع، والآن عليّ الوقوف على رأسي فقط للحفاظ على اتصال بالعين..."

    show alicia1 shut

    al0 "انظر إلى شعرك، متى كانت آخر مرة قطعتها؟"

    hide theo1 at right_offset
    show theo3 close_happy sad smile at right_offset

    t "{cps=15}.....{/cps}"

    "إنها تتصرف مثل الشخصية البيضاء"

    "ملاحظة التشابه يجعلني غير قادرة على منع ضحكي."

    "أجابتها جعلتني أخفي ضحكًا خلف يدي."

    al0 "ما الذي تضحكين عليه؟"

    t "آسفة، استمر"

    al0 "{cps=15}....{/cps}"

    t "شيء ما جعلني أضحك."

    show alicia1 sad smile

    al0 "أنت حقاً لا تتذكر، أليس كذلك؟"

    "لقد تغيرت مزاجها، لكن تلك الابتسامة كانت لا تزال موجودة... هل هذه نفس الفتاة التي بكت في صدري منذ لحظة؟"

    al0 "ما الذي حدث لك؟"

    hide theo3 at right_offset
    show theo1 sweat shut at right_offset_surprised

    t "{cps=15}.....{/cps}"

    show theo1 sweat close

    t "لو كنت أعرف الإجابة، أنا أشك أنني لن أكون هنا."

    al0 "أنت حقاً لا تعرف؟"

    show theo1 sweat shut

    t "لست متأكداً، لا أتذكر الكثير قبل ستة أيام"

    show alicia1 sad openbit

    al0 "-ما الذي حدث؟"

    hide theo1 at right_offset
    show theo3 sweat close pain at right_offset

    t "كل ما أتذكره هو أنني وجدت في البحر ويقال بأنني مسؤولة عن سقوط طائرة تابعة لـ (جرايله إينهورن)"

    al0 "هل كنتِ كذلك؟"

    t "كما قلت لا أستطيع أن أتذكر"

    t "لقد مررت بالكثير في الأسبوع الماضي"

    al0 "لقد مرنا بالكثير"

    hide theo3 at right_offset
    show theo1 sweat shut at right_offset

    t "هل أوقفتم المطر؟"

    al0 "هاه؟"

    t "في اليوم الأول الذي أتذكره، أوقفت من سقوط المطر."

    "أخذت مذكراتي من حقيبتي كنت أكتب مغامراتي من هذا الأسبوع فيها"

    "قد تجعل الأمور أسهل بالنسبة لها لفهمها"

    show alicia1 normal shut

    al0 "كيف يكون ذلك ممكناً؟"

    show theo1 picek sweat open

    t "أتمنى لو كنت أعرف نفسي ولكنني كنت أحلم بهذه الأحلام المجنونة منذ الحادث"

    "أَقُولُ، أَحْضُرُ مذكراتيُ إلى مكانِي الأصلي على السريرِ."

    hide theo1 at right_offset
    show theo3 picek sweat pain at right_offset

    t "حدثت لي أشياء غريبة في وقتٍ ما شعرتُ وكأنّي أتطير"

    show alicia1 normal openbit

    al0 "ماذا يوجد في ذلك الكتاب؟"

    hide theo3 at right_offset
    show theo1 shut at right_offset

    t "سجل كل حلم تقريباً ومعظم التشوهات التي شهدتها خلال الأسبوع الماضي"

    al0 "هل يمكنني قراءتها؟"

    t "بالتأكيد، أنا أؤمن أنك في ذلك."

    al0 "هاه؟"

    "أعطيتها الكتاب الأسود المغطى بالجلد والذي قبلته بهدوء، ثم تتصفح عبر الصفحات، ركزت على قراءة ما كتبته."

    t "لذا، في اليوم الأول، وجدتني مجموعة من الصيادين أغرق في البحر."

    t "بعد أن أنقذوني، قالوا لي أن المساعدة ستنتظرنا عندما نصل إلى المرفأ."

    t "لكن قبل أن نتمكن من الهبوط، كان علينا أن نتجاوز عاصفة، وذلك عندما..."

    show alicia1 smile

    al0 "خط يدك تغير"

    t "هاه؟"

    al0 "لقد تحسنت خط يدك، لم يعد هناك إشارات و علامات ضفدع لا يمكن قراءتها"

    t "هيا، أنا جاد هنا!"

    show alicia1 closehappy sad smilewide

    al0 "حسناً، أنا آسفة"

    al0 "هيّا"

    t "....."

    "على الرغم من أنّني أفكر في ذلك، فمن الرائع حقاً..."

    show alicia1 blink normal smile

    t "سفينتهم كانت على وشك الانهيار لكن العاصفة انتهت بسببي"

    t "لم أستطع تغيير الطقس من المطر إلى الشمس، لكنني تمكنت من منع المياه من الهبوط بطريقة ما."

    show alicia1 blink normal openbit

    "إنها تبصق عينيها أثناء قراءة مذكراتي و الشيء الوحيد الذي أزعجها هو أنني أنهيت القصة"

    al0 "هذا لا يبدو ممكناً"

    t "ومع ذلك، نجوت"

    t "في اليوم التالي وصلنا إلى مومباسا وكما قال أحد الصيادين كان هناك شخص ما ينتظرني هناك"

    al0 "مهلاً، ماذا يوجد في الهند؟"

    show theo1 sweat

    t "نعم، تلك الصفحة،"

    hide theo1 at right_offset
    show theo3 picek sweat pain at right_offset

    t "{cps=15}.....{/cps}"

    "لقد خدشت رأسي آمل أن أتوقف بأي طريقة ممكنة"

    t "الطائرة تحطمت، لا أعرف التفاصيل، لكن أعتقد أن هذا هو المكان الذي يجب أن أذهب إليه"

    al0 "الهند، ها."

    al0 "إستمري"

    hide theo3 at right_offset
    show theo1 shut at right_offset

    t "أين كنت؟"

    t "لذا وصلت إلى مومباسا، ثلاثة رجال قاموا بمهاجمة لي، لكنني تمكنت من الهرب."

    t "أيضاً، أنقذت فتاة، لكنني فقدتها أثناء العمل."

    show alicia1 angry openbit

    al0 "مهلاً، هل هذا يعني أن الفوضى في مومباسا في الأخبار كانت"

    show theo1 close

    t "أجل، لقد كنت أنا"

    show theo1 blink

    t "على أية حال، بعد ذلك حصلت على هاتف من أحد مطاردي."

    t "باستخدام ذلك الهاتف، دعتني (يومي) إلى هنا، وقالت إنها تستطيع أن تخبرني من أنا."

    show alicia1 normal shut

    al0 "أعتقد أن هذا لم ينجح بشكل جيد، وإلا لكنت تعرف اسمك."

    show theo1 sweat close pain

    t "{cps=15}-نعم ...{/cps}"

    "لقد أنفذت، كل من الإحباط والتأكيد."

    show theo1 blink shut

    t "هل أنت أو نحن من هنا؟"

    show alicia1 smile

    al0 "كلاّ، كلاّ منّا قطعنا طريق طويل."

    show theo1 sweat

    t "إذن، ما الذي يمكنك أن تخبرني به، آنسة...{w=1}...أوه"

    "أنا أتأخر لأنني نسيت اسمها بالفعل."

    "ظننت أنني قد حفظتها، لكن بين حين أخبرتني بإسمها في محطة الحافلات وحتى الآن، كان عقلي مشغولاً جداً بكل شيء آخر ونسيت."

    show alicia1 closehappy

    "أنا لا أعرف لماذا، ولكن نسيتي اسمها تجعلها تبتسم."

    "إنها تغلق مذكراتي وتعيدها لي"

    al "(أليسا)"

    show theo1 sad

    t "حسناً، آسفة"

    al "أنا لا ألومك، كما قلت، لقد قطعنا طريقًا طويلًا، حدث الكثير خلال العامين الماضيين"

    show theo1 angry

    t "هل تعرف ما الذي قد يحدث لي؟"

    show alicia1 normal blink smile

    al "بالتأكيد، منذ عامين، تم أخذك من دار الأيتام"

    al "ليس لدينا وقت للتفاصيل الآن، ولكن قضيت تلك السنتين في محاولة للعثور عليك."

    show theo1 sweat

    t "انتظر{w=1} دار الأيتام؟{w=1} هل تقول أننا كلانا..."

    show alicia1 shut

    al "أجل، لقد عشت في دار الأيتام (إيدلوايس) بقدر ما أعرف، عشت هناك طوال حياتك"

    al "لقد عشت هناك سنة فقط قبل أن تكوني... {w=1}ذهبوا"

    t "{cps=15}هاه ..{/cps}"

    "في منزل (فيكي) ، أتذكر رؤية عائلة قريبة، وشعرت أنني لم أذوق أبداً هذا الفاخرة، ومع ذلك أشعر أنني لم أكن وحيدة، حتى الآن."

    show alicia1 sad

    al "لقد بحثت لفترة طويلة، ولكن لم أكن أعتقد أنني سأجدك بهذه السهولة."

    show theo1 open

    t "انتظر{w=1} ما الذي تفعله هنا؟"

    show alicia1 normal

    al "كنت أراقب (أراسكا يومي) ، ظننت أنها قد تعرف مكانك"

    show theo1 shut

    t "حسناً، لقد وجدتني"

    al "أجل، هذا شيء جيد، لكن..."

    t "ـ ماذا؟"

    show alicia1 angry

    al "لا أعلم ما الذي تفعله معها، لكن أريدك أن تستمر في القيام بذلك."

    show theo1 open

    t "هاه؟"

    al "لا تفهمني بشكل خاطئ، إيجادك كان دائماً أولويتي، لكن لم أتوقع منك أن تظهر هنا."

    t "لا أعرف ماذا أفعل مع (يومي) أيضاً، لكن وجودك يجعلني أشعر أنني لا أحتاجها بعد الآن."

    show alicia1 openbit at al_left_offset_surprised
    show theo1 neutral

    al "لا، لا!"

    "إنها ترفع نطاقها بينما تتراجع وتفزعني قليلاً"

    al "أَنا آسفُ، لكنّي أَحتاجُك لَعْمَل هذا."

    t "أنا لا أفهم"

    al "اسمع، هل تتذكر عن"

    play sound "<from 1.0 to 3.0>sfx/static.mp3"
    show static
    $ renpy.pause (2.0,hard=True)
    stop sound
    hide static

    stop music fadeout 1.0
    $ bgm_name = "---"

    hide theo1 at right_offset
    show theo3 close angry pain at right_offset_surprised

    t "-أوه!"

    scene black with fast_fade

    "من دون أي مكان شعرت وكأن شيئا ثقب رأسي؛ انها تلك الألم الحاد مرة أخرى."

    "الإحساس يجعلني أصرخ بينما أمسك الجانب الأيسر من وجهي."

    play music "sfx/ringing.mp3"

    "عندما بدأ الألم يزداد حادًا، غزت صوتًا صاخبًا على سماعي."

    "كدت أن أفقد التوازن، و اضطررت إلى استخدام يدي الأخرى لدعم."



    scene hotel inverted with dissolve
    show hotel_inverted_alpha at randmotion



    "الصور الشبحية للأشخاص الذين يشبهون الأطفال بألوان مختلفة تظهر في هذه الغرفة."

    "لقد رأيت هذا من قبل، إنه تماماً مثل الهلوسة التي رأيتها في سفينة الأردن."

    "الفرق الوحيد هو أن هذه المرة الرؤية أقل غامضة من ذلك الحين، ومع ذلك الألم هو أيضا أكثر شدة."

    stop music fadeout 1.0

    scene black with fade

    play sound "sfx/bodyfallhard.wav"

    "ضعيفاً، سمعت ضحكًا بريءًا ومتلاعبًا مدفونًا في الداخل، تماماً كما أصبحت يدي ضعيفة جدًا لا يمكن أن تحملي." with vpunch

    play sound "sfx/giggle.mp3"

    al "———! ———!"

    scene cg2_blur
    show cg2c at randmotion
    show cg2b at randmotion
    show cg2a at randmotion

    play music "sfx/ringing.mp3" fadein 0.1

    "الغرفة تصبح مظلمة، ولكنني أستطيع أن أشعر أن (أليسا) ترتعش جسدي، وأسمعها تدعو اسمي، اسمي الحقيقي."

    al "———! ———!"

    "إنها تتصل أثناء هز جسدي المتساقط"

    al "———! ———! ———!"

    "الصوت الصوتي صاخب بما فيه الكفاية لأجعلها غير قادرة على سماعها ومع ذلك ما زلت أستطيع سماع صوتها"

    "لقد ساعدتني دعوتها مرات عديدة، وهذه المرة، مثل السحر، صوتها فعل ذلك مرة أخرى."

    stop music fadeout 1.0

    scene black with slow_fade

    "ببطء، اختفى الوهم والضوضاء بدأت أستعيد السيطرة على جسدي"

    scene cg2_blur
    with eye_open_slow
    $ renpy.pause (0.5, hard=True)
    scene black
    with eye_shut_slow
    $ renpy.pause (0.5, hard=True)
    scene cg2
    with eye_open_slow
    $ renpy.pause (1.0, hard=True)

    $ bgm_name = "Breath"

    play music "bgm/breath.mp3" fadein 1.0

    "أولاً أقوم بأسهل شيء: أغمض."

    "لثانية واحدة الظلام هو كل ما أراه، ولكن عندما أعيد فتح عيناي، كل شيء يعود إلى طبيعته."

    "على الرغم من أنني أستطيع التحرك، ما زلت لا أستطيع الوقوف."

    "ثم أدركت أنني لا أتنفس، أنا أتنفس بعمق، وأملأ رئتاي بالهواء النقي."

    "في منتصف القيام بذلك، أبدأ في استعادة قوتي."

    "على الرغم من أنني لم أتعافى تماماً، ما زلت أحاول الوقوف"

    al "هل أنتِ بخير؟"

    "هذا أول شيء أسمعه بعد استعادة حواسي وجهها هو الشيء الثاني الذي أدركه"

    t "أجل، أنا بخير"

    al "أنفك ينزف"

    show red with fast_dissolve
    hide red with fast_dissolve

    "سماع ذلك، أنا على الفور مسح شفتي العلوي."

    scene cg2_blur

    "بينما أفعل ذلك، تستمر في فحص وجهي، وأعتقد أنها لاحظت الحقائب تحت عيني."

    al "متى كانت آخر مرة نمت فيها؟"

    t "لا تقلق بشأن هذا أنا بخير"

    al "لا، لا، لا، يمكننا مواصلة هذا لاحقاً، حسناً؟"

    "ما زلت مشوشاً بسبب ما مررت به، لقد ترك جسدي مشلولاً، لم أشعر بأي شيء عندما وضعت جسدي على السرير."

    "بينما أنظر نحو السقف، أدرك أن الهلوسة لم تنتهي بعد."

    "أشعر بنفس الشعور تقريباً، باستثناء حركة قصيرة صغيرة تحت رأسي."

    "لكن كانت (أليسا) تضع وسادة تحت رأسي، وبعد ذلك، أستطيع أن أرى وجهها ينظر إلي،"

    al "سنستمر بهذا لاحقاً، حسناً؟"

    "على الرغم من أنني ما زلت متوتراً، فأنا أفهم أنها تأخذ إجازتها، لا أريد ذلك."

    t "إلى أين أنت ذاهب؟"

    al "يجب أن ترتاح، وأنا لدي أشياء لأقوم بها..."

    scene hotel_animated with dissolve
    show alicia1 sad shut at center_offset with dissolve

    "أريد إيقافها، لكني لا أستطيع حتى الجلوس، كل ما يمكنني فعله هو محاولة التوصل إليها بينما تتجه نحو الباب."

    "بعد أن فتحت الباب، وقفت هناك لفترة، في العتبة، وتحول لتلقي نظرة عليّ."

    show alicia1 sad smile

    "اعتقدت أن إشارتي أوقفتها في الواقع، لكن لا، إنها تبتسم لي."

    al "أراك لاحقاً"

    stop music fadeout 1.0

    scene black with fade

    al "(فرنو)"

    play sound "sfx/doorhandle.wav"

    "صوتها، أكثر هدوءاً من أي وقت مضى، يدفعني إلى الاستسلام من الجانب الآخر من الغرفة"

    "أتنفس ونفسي وأغلق عيناي، و أترك النعاس يسيطر."

    "............"

    "أنام، لا أحلام لكنها لا تسعدني."

    "جسدي يستريح، ومع ذلك عقلي لا يزال نشطاً، مما يجعلني قلق."

    "على الرغم من ذلك، أرفض الاستيقاظ، ليس حتى بعد ثلاث ساعات على الأقل. رأسي يشعر بسهولة أكثر، على الرغم من أنني ما زلت أشعر ببطء."

    al0 "(فرنو) ؟"

    scene hotel_dark
    with eye_open_slow
    $ renpy.pause (0.5, hard=True)
    scene black
    with eye_shut_slow
    $ renpy.pause (0.5, hard=True)
    scene hotel_dark
    with eye_open_slow
    $ renpy.pause (1.0, hard=True)

    play music "bgm/breath.mp3" fadein 1.0

    "لم أستيقظ بمفردي صوت جعلني أفتح عيني"

    "إنّها صوت (أليسا) ، لكنّها لم تتصل بي."

    show white_girl at sill with dissolve

    "بينما أفتح عيني أرى نسخة شبح بيضاء من (أليسا) تقف بجانب السرير"

    "عدم وجود الإضاءة في الغرفة لا يؤثر على حيوية شخصيتها."

    "على عكس النسخة الحقيقية منها التي رأيتها سابقاً، هي ترتدي ثوباً سلفاً."

    "إنّها تنظر إليّ مع ذراعيها مغطاة خلف ظهرها."

    "إرتفعت على كوع واحد، نظرت إليها بينما عينيها الخفيفة تراقبني."

    al0 "ابحث عني"

    "بعد أن نتبادل النظر لثانية قصيرة، فتحت فمها، وتطلق بعض الكلمات."

    "بعد فترة وجيزة من ذلك تلتفت وتمشى نحو الباب."

    hide white_girl with dissolve

    "الغريب، قبل أن تتمكن من الوصول إلى الباب تتلاشى في الهواء."



    "لا بدّ أنّي ما زلت أحلم، لأتأكّد من ذلك، أضرب نفسي." with hpunch

    "لا يؤلمني ذلك، لكن الشعور بالضرب يشجعني على الاعتقاد بأنني مستيقظ"

    "عيناي لا تزال تحاول التأقلم رغم أن عيناي مفتوحة كل ما أراه هو الظلام"

    "المفتاح بالقرب من الباب، لذا يجب أن أخرج من السرير."

    "جسدي صلب، أمدد ظهري و ذراعي و ساقي قبل أن أمشي نحو مفاتيح الضوء"

    "لكن نظرتي تمسك بشيء أراه من زاوية عيني في الشارع تحت النافذة"

    "بدلاً من المضي قدماً نحو مفتاح الضوء، أقترب من النافذة للحصول على نظرة أفضل."

    scene street_night with wiperight
    $ renpy.pause (1.0, hard=True)

    show white_alicia at center_offset with dissolve

    "أعلم أنني لا أحلم ومع ذلك على الرصيف أمام الفندق أرى شبح (أليسا) البيضاء"

    "إنها تقف هناك تحدق في نافذة هذه الغرفة"

    "على عكس الشبح الذي رأيته للتو، الشكل بالخارج يبدو مثل (أليسا) التي رأيتها بعد ظهر اليوم."

    "حتى بعد فترة من الزمن، تبقى واقفة في نفس المكان دون أن تتحرك أو تتحرك عينيها."

    "على الرغم من أنني أقف بجانب النافذة، انها فقط تنظر في نافذة هذه الغرفة؛ كما لو أنها ليست أنا التي تنظر إليها."



    scene hotel_animated with dissolve
    $ renpy.pause (1.0, hard=True)

    "{cps=15}{i}[Find me].{/i}{/cps}"

    "الشبح في هذه الغرفة قال ذلك في وقت سابق والآن شخصية مختلفة من نفس الشخص يقف خارج مثل تمثال أعتقد أنني يجب أن أتبعها"

    "عندما أرتدي سترتي مرة أخرى أخرج من الغرفة ثم من المبنى"

    scene street_night with wipeleft
    $ renpy.pause (1.0, hard=True)

    show white_alicia_small at left_small with dissolve

    "من هنا أستطيع أن أرى الشبح الأبيض لا يزال يقف عبر الشارع يحدق في الغرفة التي أقيم فيها."

    "بعد التحقق لفترة وجيزة من حركة المرور القريبة، بدأت في الركض عبر الشارع."

    "كلما اقتربت، كلما رأيت الشبح بشكل أفضل."

    "بينما ما زلت أعبر الطريق، ألتفت وأبحث في الغرفة التي أقيم فيها."

    "لدي رؤية واضحة من هنا مما يجعلني أتساءل لماذا تنظر إليها"

    hide white_alicia_small at left_small with dissolve

    "عندما ألتفت مرة أخرى لاحظت أنّها قد رحلت"

    show white_alicia_small at right_small with dissolve

    "أنظر حولي، ثم أجدها تسير على ما يرام، قد انزلق بعيدا بينما كنت مشتت."

    "في البداية اعتقدت أن هذا كان مجرد توهين آخر ولكن عندما أرى كيف يتفاعل عندما اقترب هذا يشبه رؤية أكثر من توهين"

    "بدأت السير أسرع قليلاً، ليس بما فيه الكفاية للوصول إليها، فقط بما فيه الكفاية لمواجهتها."

    scene street_night_blur with dissolve
    play sound "<from 0.0 to 1.0>sfx/thump.wav"

    "بعد متابعتها لفترة، ألاحظ أنه كلما أمضيت وقتا أطول في متابعتها، كلما أصبحت رأسي أكثر ثقلًا."

    scene street_night with dissolve

    "في الوقت الحالي ليس كثيراً، بالكاد أشعر به، لذا أختار تجاهله."

    scene store with wiperight
    $ renpy.pause (1.0, hard=True)

    show white_alicia_small at center_small with dissolve

    "بعد بضعة كتلة توقف أمام نافذة متجر هدايا"

    "الآن أستطيع وضع يدي على الحائط المجاور لتخفيف صداعي"

    "لا أستطيع أن أتوقف عن التساؤل عما تنظر إليه في نافذة المتجر."

    "{cps=15}{i}[Was she window shopping?.]{/i}{/cps}"

    "إنها تقف هناك بأيديها داخل جيوب سترتها لفترة طويلة"

    scene store
    show store_drunk at randmotion
    play sound "<from 0.0 to 1.0>sfx/thump.wav"

    "أريد الاقتراب منها لكن كلما اقتربت من شبحها كلما زادت صداعي"

    "ولهذا السبب أمتنع عن القيام بذلك"

    scene store with dissolve

    show white_alicia_small at center_small with dissolve

    "{cps=15}{i}[There can't be that much merchandise behind that window.]{/i}{/cps}"

    "بدأت أتساءل عن سبب بقائها طويلاً لحسن الحظ بدأت تتحرك مجدداً"



    hide white_alicia_small with dissolve

    "عندما تستأنف المشي يجب أن أتوقف عن الراحة على الحائط"

    "ألقي نظرة على نافذة المتجر التي كانت تنظر إليها"

    "المتجر مجرد متجر تذكارات، لم أكن أعرف أنها تحب هذا النوع من الأشياء."

    "لديّ وقتاً قصيراً فقط لأفحص عرض المتجر، قبل أن أذهب بعيداً عنها، أبتعد عن المتجر وألتحق بها."

    show white_alicia_small at left_small with dissolve

    "مرة أخرى تمشي لبعض الوقت، بضعة كتلة أخرى، حتى تتحول إلى الشارع الخلفي بين مبنىين."

    hide white_alicia_small with dissolve

    play sound "sfx/footstep_run_pavement.mp3"

    "عندما ألاحظ أنها خارجة عن نظري، أسرع سرعتي."

    scene street_night with wipeleft
    $ renpy.pause (1.0, hard=True)

    "لم أكن سريعاً بما فيه الكفاية عندما وصلت إلى الزقاق الخلفي اختفى شبح (أليسا)"

    "اللعنة."

    "من المضحك أنّ شيئاً إثريّاً يفوقني، على الرغم من أنّ الشبح قد رحل، إلاّ أنّ الصداع لا يزال قائماً."

    "على الرغم من أنني لا أملك أي أثر على الإطلاق، أنا أستمر في متابعة الشارع حتى أصل إلى نهاية الشارع."

    "من الآن فصاعداً، سأكون بمفردي"

    "حتى الآن، لا يوجد أي إشارة إلى أين كان الشبح يقودني"

    "لأكون صادقاً، لا أعرف حتى لماذا اتبعتها."

    "لفترة من الوقت، ركضت في الشوارع بلا هدف حتى لا أتذكر إلى أي مدى ركضت."

    u "ساعدني"

    "التردد حول الشارع تحت الجسر هو صرخة."

    "إنه ينتهي بشكل مفاجئ قبل أن يعرف ما يريد قوله."

    "على الرغم من عدم الوضوح، سمعت أنه كان يصرخ من أجل المساعدة، أشك أن أي شخص آخر سمع ذلك في هذا المكان المعزول."

    "الصرخة كانت قصيرة جدا، لم يكن كافيا بالنسبة لي لتحديد مصدرها."

    "لكن أشعر وكأنه جاء من قبلي"

    play sound "sfx/footstep_run_pavement.mp3"

    "بدأت أسرع تحت الجسر العلوي"

    scene overpass:
        ypos 0
        linear 1.0 ypos -800
    $ renpy.pause (1.0, hard=True)

    "أول شيء فكرت به بعد سماع ذلك الصراخ هو (أليسا)"

    "الصوت يتذبذب ضد هذا المكان مما يجعل من الصعب عليّ تأكيد ما إذا كان صوتها أم لا."

    "أتساءل لماذا قادني الشبح إلى هنا أم كان أنا فقط؟"

    "في الوقت الحالي، لا يمكنني أن أضيع الوقت على القلق بشأن ذلك، لأن شخص ما قد يكون في خطر."

    "المكان مظلم المصادر الوحيدة للضوء هنا هي مصابيح الشوارع على الرصيف أحيانا مصابيح سيارات المرور"

    "لكن حتى تلك الأضواء بالكاد تصل إلى هنا"

    "الركض هنا أيضاً صعب لقد دخلت في بركان قدمي تعثرت على شيء كل بضعة خطوات"

    scene overpass_blur:
        ypos -800
    with dissolve
    play sound "<from 0.0 to 1.0>sfx/thump.wav"    

    "لكن كما لو لم يكن هذا كافياً، يجب أن أجري مع هذا الألم الذي يحرق رأسي."

    stop music fadeout 1.0

    $ bgm_name = "Paranoia"
    play music "bgm/paranoia.mp3" fadein 1.0

    scene overpass:
        ypos -800
    with dissolve

    u "ساعدوني!"

    "بعد لحظة، سمعت صراخًا آخر، لم يكن صاخباً كما كان من قبل، لأنّها تصرخ مع التنفس المجهد."

    "تحت ظل هذا الجسر المرتفع هناك شخصيتين يطاردان الآخرين"

    show thug_dark at right_offset with dissolve

    "الأولى امرأة، من المحتمل أنها عاملة في المكتب بحسب ملابسها، والثانية رجل قصير جداً."

    "أنا فقط أستطيع التعرف على صورتهم؛ من المستحيل أن أرى خصائصهم في مثل هذا البيئة المظلمة."

    "على الرغم من ذلك، أستطيع أن أرى لماذا المرأة خائفة من الرجل؛ هو يحمل سكين."

    "المرأة عالقة في الزاوية، لا تستطيع التحرك، فجأة الرجل يبدأ بالتحميل"

    scene overpass_effect:
        ypos -800
    with dissolve

    play sound "sfx/footstep_run_pavement.mp3"

    show thug_dark at right_offset

    "هذا خطير، أعلم، خاصة في حالتي، ولكن بدلاً من الهرب، أركض نحو الرجل."

    hide thug_dark
    show thug knife at thug_dodge
    show theo1 blink pain at dash

    play sound "sfx/jab.mp3"

    "قبل أن يتمكن من مهاجمة المرأة، أركض عليه وأمسك معصمه، مما يمنعه من التقدم أكثر." with hpunch

    show thug knife at fightback
    show theo1 at dodge

    play sound "sfx/punch.mp3"

    "الرجل سريع جداً قبل أن أستطع أن أمسك به بيدي الأخرى أيضاً، هو أمسك بيدي الحرة" with vpunch

    hide theo1
    show theo2 blink pain at left_offset

    "الآن نحن في مواجهة محرجة، كل واحد يحتفظ بيد الآخر في محاولة لإيقافه."

    "يجب أن أتحرر لو كان أطول يمكنني أن أضربه بالرأس في وجهه"

    show thug knife at fightback
    play sound "sfx/punch.mp3"
    show theo2 picek at impact_small

    "{i}[Ugh!]{/i}" with vpunch

    "بينما ما زلت أبحث عن طريقة للتحرر، ركلني في الأمعاء."

    "الضربة قوية بما فيه الكفاية لتخدير يدي اليسرى لعدة ثوان"

    hide theo2
    show theo1 picek shut at dodge

    "أشعر بأن قبضتي تتلاشى أطلق سراح معصمه وأقفز للخلف، وأخرج من نطاق الهجوم"

    show theo1 blink

    "عندما أنظر إلى الوراء، أجد المرأة قد غادرت."

    show theo1 open sweat

    "{cps=15}{i}[What—]{/i}{/cps}"

    "لقد استغرقت وقتاً طويلاً في النظر إلى الوراء ولم يضيع تلك الفرصة"

    hide theo1
    show theo2 shut sweat at left_offset

    "عندما أعود إليه، هو يتقدم بالفعل."

    play sound "sfx/whoosh.flac"

    show thug knife at fightback
    show theo2 picek at dodge

    "عندما كان على بعد خطوتين فقط، قفز وطلق ركلة دائرية نحو أذني اليسرى." with hpunch

    "تحركاته سريعة و مخادعة، كنت تقريبا غير قادرة على قراءة حركته و الكتلة."

    show theo2 blink open

    "لكن انعكاسي بدأ و استطعت رفع يدي وحماية جانب رأسي"

    show theo2 shut at kudakuda

    "أطلق نفسي عليه مع قبضتي مسدودة خلف رأسي، وبناء بعض الزخم للهجوم القادم."

    "عندما يهبط، يجب أن يكون هناك لحظة قصيرة عندما يعود إلى توازن."

    show theo2 shout at charge
    show thug knife at thug_dodge
    play sound "sfx/whoosh.flac"

    "لقد دفعت قبضتي مباشرةً نحو وجهه، لكن لدهشتي، يتجنبها."

    hide theo2
    show thug knife open at fightback
    show theo1 picek shut at dodge
    play sound "sfx/whoosh.flac"

    "لقد دفع سكينه نحو بطني، لكنني تمكنت من الهرب عن طريق الخطوة اليمنى."

    hide theo1
    hide thug knife
    show thug sigh sweat at thug_dodge
    show theo2 pain at charge

    play sound "sfx/jab.mp3"

    "بعد أن وصلت إلى جانبه، أضغط على الذراع التي لا تزال تدفع إلى الأمام، مما يجعله يفقد قبضته على السكين."

    play sound "<from 0.0 to 2.0>sfx/knife.wav"

    "السكين يطير خارج يده." with vpunch

    "من الصعب تحديد أين هبطت في مثل هذه البيئة المظلمة، ولكن بالنظر إلى الصوت الذي أصدرته عندما كان على الأرض، لا أعتقد أنه بعيد جدا."

    hide theo2
    show theo1 surprised open sweat at left_offset

    "كنت مشتتة جداً في الاستماع حتى لم أدرك أنه كان يعد يد مباشرةً تحت وجهي"

    play sound "sfx/jab.mp3"
    show theo1 surprised open sweat at impact_small
    show thug at fightback

    "لقد أطلق ضربة أعلى لا أستطيع تجنبها" with vpunch

    show theo1 at falldown
    play sound "sfx/bodyfallhard.wav"

    "أقدامه تتواصل مع ذقني، يضربني حتى سقطت على ركبتي."

    hide thug
    show thug at right_offset

    "على الرغم من أنني مفتوحة لمزيد من الهجمات، هو لا يواصل الهجوم."

    "وبدلاً من ذلك يبحث عن سكينه الذي سقط في الظلام"

    scene overpass_blur:
        ypos -800
    with dissolve
    show overpass_drunk at randmotion:
        ypos -800
    play sound "<from 0.0 to 1.0>sfx/thump.wav"

    "في هذه الأثناء، بدأت أشعر بألم حاد في رأسي مرة أخرى."

    "هذا الصداع هائل جداً حتى أنني لا أستطيع حتى الوقوف، ناهيك عن التعافي من ضربته."

    "والآن أدرك أن أنفي بدأ ينزف مجدداً"

    show red with fast_dissolve
    hide red with fast_dissolve

    "هو ما زال يبحث عن سكينه وأنا أعلم أنني لست في أي حالة للقتال."

    play sound "sfx/footstep_run_pavement.mp3"

    "أُستفيدُ من هذه الفرصةِ لِمُحَارَبَةِ على قدميِ، تَوَلَّي وَرَكضَ."

    scene overpass_blur:
        ypos -800
    with dissolve

    "هذا الصداع يحد من قوتي؛ لا أستطيع الركض بأقصى سرعة لأنني في كل خطوة أشعر بالخسارة قد أفقد التوازن."

    play sound "sfx/footstep_run_pavement.mp3"

    "لم أذهب بعيداً عندما أسمع خطوات صاخبة تتردد تحت الجسر العلوي، قادمة من ورائي."

    show thug knife at center_offset with dissolve

    "عندما أنظر فوق كتفي، أرى أن الرجل القصير يندفع نحوي، مع السكين في يده."

    "إنه يركض أسرع مني، لن يستغرق وقتاً طويلاً حتى يصل إليه."

    hide thug knife with dissolve

    "أنا اقترب من حافة ظلال هذا الجسر العلوي"

    "لكن قبل أن أخرج، يجب أن ألتفت لأنّه يكتسب"

    show thug sigh knife at kill
    show theo3 picek pain sweat at impact_small

    play sound "sfx/whoosh.flac"

    "عندما ألتفت، وجدتُه يطير نحوي، يُرْمِي سكينَهُ نحو رقبتي."

    hide theo3
    show theo2 picek pain sweat at impact_small
    show thug knife sweat at thrown

    "على الرغم من أنني بالكاد لدي وقت كاف للاستجابة، أتمكن من القبض على معصمه وإعادة توجيه هجومه، باستخدام زخماته ضدّه."

    "لقد تعثّر، لكنه لا يسقط" with hpunch

    show thug knife open at fightback
    show theo2 picek pain at impact_small

    "بعد أن استعاد التوازن، يلتفت ويتهمني."

    hide theo2
    show theo3 picek pain sweat at kudakuda

    "صداعي وقدرته على مواجهة الهجمات تحطمتني"

    play sound "sfx/punch.mp3"

    show thug knife sigh sweat at fightback
    show theo3 at falldown

    play sound "sfx/bodyfallhard.wav" 

    "اعتقدت انه سوف يضرب جسدي العلوي، ولكن بدلا من ذلك كتفه..." with vpunch

    stop music fadeout 1.0

    hide theo3 with dissolve
    hide thug with dissolve

    "عندما يمسك بي، يستمر في الضغط حتى يضعني على الحائط خلفي." with hpunch

    scene black with fade

    play sound "sfx/jab.mp3"

    "قبل أن أستطع التفاعل، قام بإغلاق رقبتي بذراعيه اليسرى" with hpunch

    "هذا سيء، هو يمكن أن ينتهي مني بينما في هذا الموقف."

    play sound "sfx/honk.mp3"

    scene white with flashbulb

    "يرفع السكين في يده اليمنى، ولكن بينما كنت على وشك التفاعل، تمر شاحنة فجأة في الشارع خلفه."

    "مصابيحها العلوية أعمرتني لثانية، مما يزيد من الألم من صداعي."

    scene overpass_blur with eye_open_slow:
        ypos -800
    $ renpy.pause (0.5, hard=True)
    show thug_blur knife at center_offset with dissolve

    "أنا في موقف بلا أمل"

    "هذا يجب أن يكون فرصة ذهبية إذا أراد إنهائي، ولكن الإضراب لا يأتي."

    "حتى بعد أن تمر الشاحنة وأضواءها لم تعد تجعلني أعمى، يده مجرد معلقة في الهواء."

    thug "{cps=15}...........{/cps}."



    "شيء ما جعله يتردد لا أعرف ما، ولكن هذه فرصة بالنسبة لي"

    play sound "sfx/punch.mp3"

    show thug_blur knife open

    "أرتفع بمضربتي وأضربه في وجهه" with vpunch

    hide thug_blur with dissolve

    play sound ["sfx/bodyfallhard.wav","sfx/footstep_run_pavement.mp3"]

    "لقد تعطل التوازن و يسترخي قبضته علي قبل أن يتعافى أحتفظ بهذه الفرصة للهرب" with vpunch

    play music "sfx/traffic.mp3"

    scene traffic with wipeleft
    $ renpy.pause (0.5, hard=True)

    al0 "إنتظر (فيرنو)"

    "لقد خرجت من ظل الجسر إلى الشارع"

    "دون حتى التحقق من أي سيارة قادمة، بدأت عبر الشارع."

    "ولكن عندما أسمع صوت يدعو اسمي من الخلف، أوقف في منتصف الشارع وأنظر إلى الوراء."

    stop music fadeout 1.0

    "{cps=15}{i}[That voice...why?]{/i}{/cps}"

    show alicia1 sad openbit at center_offset with dissolve

    "عندما ألتفت أرى (أليسا) تكشف عن نفسها عن طريق الخروج من الظلال"

    "نتبادل نفس النظرة الغريبة المضطربة"

    "لا أحد منا يبدو أنه يفهم ما الذي يفعله الآخر هنا"

    f "ما الذي تفعله لها"

    show alicia1 angry openwide

    al "(فرنو) ، كن حذراً"

    play sound "sfx/honk.mp3"
    show cg3 with flashbulb:
        xpos 500
        linear 1.0 xpos 0
    $ renpy.pause (0.5, hard=True)

    "قبل أن أتمكن من إنهاء جملتي، تشير إلى يساري."

    "ألتفت لأبحث وأرى شاحنة أخرى تتقدم نحوي."

    "كنت متفاجئة جداً حتى لم أسمعها قادمة، وعندما أدركتها أخيراً، تأخرت جداً للتفاعل."

    play sound ["sfx/tire.mp3","sfx/crash.mp3"]

    scene black with shakehard

    "بعد أن يغرقني الضوء من مصابيحها، أستطيع أن أشعر بقوة ترميني إلى الهواء وقوة أخرى عند الهبوط على الأرض."

    play sound "sfx/bodyfallhard.wav"

    "مضحك، انها لا تؤلم كما توقعت انها ستعمل." with vpunch

    play music "bgm/remembrance.mp3" fadein 1.0

    scene night_sky_blur with dissolve
    $ renpy.pause (1.0, hard=True)

    "الشيء التالي الذي يمكنني رؤيته هو السماء الليلية لا أشعر بأي شيء لكني مازلت أستطيع أن أنظر حولي"

    "وجدت نفسي مستلقية على الرصيف شيء ثقيل يضعني على الأرض"

    scene cg2d_blur with dissolve
    $ renpy.pause (0.5, hard=True)

    "أخشى الأسوأ عندما أنظر إلى جسدي، بدلاً من ذلك أجد (أليسا) متجمدة فوقي."

    "{cps=15}{i}[Wait—did she just...]{/i}{/cps}"

    show eyeshut2 with slow_slow_dissolve

    "شعوري يصبح ضعيفاً، لا أستطيع حتى التفكير بما حدث للتو."

    "بينما أفقد قوتي، يسقط رأسي على الأرض، مما يعرض لي مشهد نفس السماء الليلية التي رأيتها من قبل."

    "قبل أن أفقد وعائي، تدخل (أليسا) مجال رؤيتي، تصرخ بشيء."

    "ربما تتصل بإسمي، لكن لا أستطيع سماع ما تقول."

    "على الرغم من أنني قبل إغلاق عيني أستطيع سماع صوتها يتردد في عقلي"

    scene cg2e_blur with dissolve

    nar "{size=+15}{cps=15}{vspace=370}{space=50}{i}لقد وجدتني{/i}{/cps}{/size}"

    nvl clear

    stop music fadeout 1.0

    scene black with fade

    "مرة أخرى يسيطر الظلام، ولكن كالعادة انتصاره هو مؤقت."

    "لتستمر..."


    return






    stop music fadeout 1.0


    scene orphanage with dissolve
    show madam at right_offset
    show theo_child at ct_left_offset

    m "اليوم نرحب بأجزاء جديدة في عائلتنا"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
