# ddlcmod — original fan-made DDLC content
# Drop this file into a DDLC-compatible game's game/ folder.
# It does not include or redistribute DDLC's original assets.

default dlcm_points = 0
default dlcm_day = 1
default dlcm_seen = 0
default dlcm_fragments = []
default dlcm_route = "club"

init python:
    import random

    # 10 x 10 x 10 = 1000 original, runtime-generated literary fragments.
    dlcm_themes = [
        "hope", "memory", "friendship", "curiosity", "change",
        "courage", "loneliness", "dreams", "identity", "discovery"
    ]
    dlcm_places = [
        "the empty classroom", "a rain-lit library", "the school rooftop",
        "a quiet train platform", "the festival hallway", "the clubroom after sunset",
        "a tiny garden", "the computer lab", "a moonlit street", "a room full of books"
    ]
    dlcm_motifs = [
        "a paper crane", "a cracked pencil", "a warm cup of tea", "an unfinished poem",
        "a blue ribbon", "a forgotten notebook", "a blinking cursor", "a paper star",
        "a key with no lock", "a page with no ending"
    ]

    dlcm_fragments_all = []
    for theme in dlcm_themes:
        for place in dlcm_places:
            for motif in dlcm_motifs:
                dlcm_fragments_all.append(
                    "At %s, someone discovered %s and wrote one small sentence about %s. "
                    "The sentence was not perfect, but it carried %s forward." %
                    (place, motif, theme, theme)
                )

    def dlcm_get_fragment():
        unseen = [i for i in range(1000) if i not in dlcm_fragments]
        if not unseen:
            return 1000, "Every fragment has been found. The collection is complete."
        i = random.choice(unseen)
        dlcm_fragments.append(i)
        return i + 1, dlcm_fragments_all[i]

label start:
    scene black
    with fade
    "A new page waits behind the familiar classroom door."
    jump dlcm_intro

label dlcm_intro:
    scene black
    "Welcome to ddlcmod."
    "This is an original fan-made expansion built around poems, choices, secrets, and collectible fragments."
    "There are 1,000 collectible literary fragments to discover."
    menu:
        "Open the clubroom":
            $ dlcm_route = "club"
            jump dlcm_club
        "Start a quiet reading":
            $ dlcm_route = "reading"
            jump dlcm_reading
        "Look for a hidden page":
            $ dlcm_route = "secret"
            jump dlcm_secret

label dlcm_club:
    "The clubroom is unusually quiet today."
    "A blank notebook sits on the desk."
    menu:
        "Write something hopeful":
            $ dlcm_points += 2
            "You write until the blank page no longer feels empty."
        "Ask for a challenge":
            $ dlcm_points += 1
            "A challenge appears: find three fragments before tomorrow."
        "Search the bookshelf":
            $ dlcm_points += 1
            jump dlcm_fragment
    jump dlcm_day_end

label dlcm_reading:
    "You turn a page and find a sentence that seems to have been written for you."
    $ dlcm_points += 1
    menu:
        "Keep reading":
            jump dlcm_fragment
        "Close the book":
            "Sometimes stopping is part of reading."
    jump dlcm_day_end

label dlcm_secret:
    "Behind the monitor is a tiny folded page."
    "It has no name, only a number."
    jump dlcm_fragment

label dlcm_fragment:
    $ dlcm_id, dlcm_text = dlcm_get_fragment()
    $ dlcm_seen = len(dlcm_fragments)
    "Fragment [dlcm_id] / 1000"
    "[dlcm_text]"
    "Collection progress: [dlcm_seen] / 1000"
    menu:
        "Find another fragment":
            jump dlcm_fragment
        "Return to the clubroom":
            jump dlcm_day_end
        "End today's reading":
            jump dlcm_day_end

label dlcm_day_end:
    $ dlcm_day += 1
    "Day [dlcm_day]."
    if len(dlcm_fragments) >= 1000:
        "The entire collection is complete."
        "The last page is blank. This time, you get to decide what goes there."
    else:
        "The notebook remains open. There are still [1000 - len(dlcm_fragments)] fragments waiting."
    return
