# ddlcmod — original fan-made DDLC story content
# Uses the player's existing DDLC installation and its original assets.
# No DDLC assets are redistributed by this file.
# Compatible target: Ren'Py 6.99.x / DDLC 1.1.1.

# Start the mod before DDLC's normal start label, while preserving the
# original game if the player later returns to it.
init python:
    config.label_overrides["start"] = "dlcm_start"

# Mod characters use the same presentation style as DDLC, but are separate
# Character objects so this file does not depend on the original script's
# variable definitions.
define dlcm_mc = Character("MC", color="#a0a0a0")
define dlcm_s = Character("Sayori", color="#ffaaaa")
define dlcm_n = Character("Natsuki", color="#ff7db8")
define dlcm_y = Character("Yuri", color="#c8a2ff")
define dlcm_m = Character("Monika", color="#6fc7a8")

# Persistent progress makes the mod feel like a real replayable route.
default dlcm_day = 1
default dlcm_s_affection = 0
default dlcm_n_affection = 0
default dlcm_y_affection = 0
default dlcm_m_affection = 0
default dlcm_poem_style = ""
default dlcm_fragments = []
default dlcm_seen_fragment = False
default dlcm_secret = False

def dlcm_pick_poem_word(word, style):
    # The player's word choices determine who notices the poem most.
    if style == "sayori":
        dlcm_s_affection += 1
    elif style == "natsuki":
        dlcm_n_affection += 1
    elif style == "yuri":
        dlcm_y_affection += 1
    elif style == "monika":
        dlcm_m_affection += 1
    return word

label dlcm_start:
    $ config.label_overrides.pop("start", None)
    scene black
    with dissolve
    "There is something different about the classroom today."
    "Not different enough to scare you."
    "Just different enough that you notice."
    jump dlcm_day1

label dlcm_day1:
    scene bg residential_day
    with dissolve
    dlcm_mc "Another day."
    "The walk to school feels exactly the same as always."
    "Until someone nearly tackles you from behind."
    show sayori 1a at t11
    dlcm_s "Ehehe! Good morning!"
    dlcm_mc "Sayori!"
    dlcm_s "You looked so serious, I thought you were going to walk right past me."
    dlcm_mc "I was thinking about the Literature Club."
    dlcm_s "Oh! Then you're definitely coming today, right?"
    menu:
        "Of course. I promised." :
            $ dlcm_s_affection += 2
            dlcm_s "Yay! I knew you would!"
        "I'll see how I feel." :
            $ dlcm_s_affection += 1
            dlcm_s "That's not a no! I'll take it!"
    scene bg school
    with dissolve
    "After classes, you finally step into the clubroom."
    show monika 1a at t11
    dlcm_m "Welcome to the Literature Club!"
    show natsuki 1a at t21
    show yuri 1a at t22
    dlcm_n "He actually came."
    dlcm_y "I'm glad you decided to join us."
    show sayori 1b at t31
    dlcm_s "See? I told you!"
    dlcm_m "Since you're here, why don't you write a poem with us?"
    jump dlcm_poem

label dlcm_poem:
    scene bg club_day
    with dissolve
    "You take out a blank sheet of paper."
    "The others are writing. You decide to try something different."
    "Instead of typing a poem all at once, you choose the words that shape it."
    menu:
        "sunshine":
            $ dlcm_pick_poem_word("sunshine", "sayori")
        "marshmallow":
            $ dlcm_pick_poem_word("marshmallow", "natsuki")
        "entropy":
            $ dlcm_pick_poem_word("entropy", "yuri")
        "analysis":
            $ dlcm_pick_poem_word("analysis", "monika")
    menu:
        "happiness":
            $ dlcm_pick_poem_word("happiness", "sayori")
        "cute":
            $ dlcm_pick_poem_word("cute", "natsuki")
        "desire":
            $ dlcm_pick_poem_word("desire", "yuri")
        "future":
            $ dlcm_pick_poem_word("future", "monika")
    menu:
        "rainbow":
            $ dlcm_pick_poem_word("rainbow", "sayori")
        "anime":
            $ dlcm_pick_poem_word("anime", "natsuki")
        "universe":
            $ dlcm_pick_poem_word("universe", "yuri")
        "question":
            $ dlcm_pick_poem_word("question", "monika")
    "Your poem is finished."
    "It is short. A little strange. But it is yours."
    jump dlcm_poem_share

label dlcm_poem_share:
    scene bg club_day
    show sayori 1a at t11
    dlcm_s "Can I read yours first?"
    if dlcm_s_affection >= 2:
        dlcm_s "I really like this one. It feels warm."
    else:
        dlcm_s "It's kind of mysterious!"
    show natsuki 1a at t21
    dlcm_n "My turn."
    if dlcm_n_affection >= 2:
        dlcm_n "Okay... this actually has some good lines."
    else:
        dlcm_n "It's not my style, but I guess it works."
    show yuri 1a at t22
    dlcm_y "There is an interesting rhythm to it."
    if dlcm_y_affection >= 2:
        dlcm_y "I'd like to talk about it more later."
    show monika 1a at t11
    dlcm_m "I think you're going to fit in here."
    "For the first time, the club feels like somewhere you belong."
    jump dlcm_day1_end

label dlcm_day1_end:
    scene bg residential_day
    with dissolve
    "On the way home, you notice a folded piece of paper beneath the fence."
    menu:
        "Pick it up":
            $ dlcm_fragments.append("day1")
            $ dlcm_seen_fragment = True
            "The page contains a sentence written in handwriting you don't recognize."
            "REMEMBER THAT YOU CHOSE TO BE HERE."
        "Leave it alone":
            "You keep walking."
    $ dlcm_day = 2
    jump dlcm_day2

label dlcm_day2:
    scene bg club_day
    with dissolve
    "The next afternoon, the club is already busy."
    show sayori 1b at t11
    dlcm_s "You came back!"
    show natsuki 1a at t21
    dlcm_n "Obviously he came back."
    show yuri 1a at t22
    dlcm_y "Still, it's nice to see you again."
    show monika 1a at t31
    dlcm_m "Today, let's make things a little more interesting."
    dlcm_m "We're going to share what we think a good story needs."
    menu:
        "A happy ending":
            $ dlcm_s_affection += 1
            "Sayori smiles immediately."
        "A satisfying twist":
            $ dlcm_n_affection += 1
            "Natsuki nods like you finally said something sensible."
        "A feeling that lingers":
            $ dlcm_y_affection += 1
            "Yuri looks thoughtful."
        "Someone who knows the reader is watching":
            $ dlcm_m_affection += 2
            show monika 2b at t11
            dlcm_m "...That's an interesting answer."
    "The conversation continues until the sunlight starts to fade."
    jump dlcm_day2_secret

label dlcm_day2_secret:
    scene bg club_day
    show monika 1d at t11
    dlcm_m "Could you stay for a minute?"
    dlcm_mc "Sure. What's up?"
    dlcm_m "Have you ever had the feeling that a story was looking back at you?"
    dlcm_mc "That's... a weird way to put it."
    dlcm_m "I know. Forget I asked."
    hide monika
    "For one second, the room seems to flicker."
    "When you blink, everything is normal."
    if dlcm_seen_fragment:
        "The folded page from yesterday is suddenly on your desk."
        $ dlcm_secret = True
        "There is a second sentence underneath the first."
        "DON'T LET HER READ THE LAST PAGE."
    else:
        "A blank sheet of paper sits on your desk."
    $ dlcm_day = 3
    jump dlcm_day3

label dlcm_day3:
    scene bg club_day
    with dissolve
    "By the third day, the club has developed a routine."
    show sayori 1a at t11
    dlcm_s "I brought snacks!"
    show natsuki 1c at t21
    dlcm_n "You mean I brought snacks."
    show yuri 1a at t22
    dlcm_y "I brought another book."
    show monika 1a at t31
    dlcm_m "And I brought something for everyone."
    "Monika places four identical pages on the desk."
    dlcm_m "A final poem. Everyone writes one line."
    menu:
        "Write about friendship":
            $ dlcm_s_affection += 2
            "You write: Sometimes being understood is enough."
        "Write about being yourself":
            $ dlcm_n_affection += 2
            "You write: I don't need to be perfect to be real."
        "Write about the unknown":
            $ dlcm_y_affection += 2
            "You write: The darkest page is still a page."
        "Write about the reader":
            $ dlcm_m_affection += 2
            "You write: Someone is always there when the page turns."
    if dlcm_secret:
        "Your hand stops."
        "The sentence on the hidden page is still in your pocket."
        "DON'T LET HER READ THE LAST PAGE."
    jump dlcm_final_choice

label dlcm_final_choice:
    scene bg club_day
    show monika 1a at t11
    dlcm_m "So? Ready to show me?"
    menu:
        "Show Monika the page":
            if dlcm_secret:
                jump dlcm_glitch
            else:
                jump dlcm_good_end
        "Keep the page":
            jump dlcm_good_end

label dlcm_good_end:
    scene bg school
    with dissolve
    "The club stays open late."
    "You talk, laugh, argue about books, and write until the sky turns dark."
    "For once, there is no perfect ending."
    "Just another day to come back tomorrow."
    jump dlcm_epilogue

label dlcm_glitch:
    scene black
    with dissolve
    stop music
    "The moment Monika touches the page, the text disappears."
    "..."
    show monika 1d at t11
    dlcm_m "You weren't supposed to find that."
    dlcm_mc "Find what?"
    dlcm_m "The part of the story that isn't finished yet."
    "The screen goes white."
    scene black
    "END OF ACT ONE"
    "A new page has been added to the collection."
    $ dlcm_fragments.append("secret_act_one")
    jump dlcm_epilogue

label dlcm_epilogue:
    scene black
    with fade
    "DDLCMOD"
    "ACT ONE COMPLETE"
    ""
    "Days completed: [dlcm_day]"
    "Hidden pages found: [len(dlcm_fragments)]"
    "Thank you for reading."
    return
