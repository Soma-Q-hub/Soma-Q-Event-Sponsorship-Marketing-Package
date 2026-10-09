#!/usr/bin/env python3
"""Generate the four explainer posters (helpers in posterkit.py)."""
from posterkit import *

# 1) the loop ------------------------------------------------------------------------------------------------------
b = f'<rect width="2425" height="3625" fill="{LINEN}"/>\n' + eyebrow(175, 330, "THE PRESSURE LOOP")
b += lines(175, 560, ["Interrupt the loop that", "drains your energy", "and clarity."], 176, 178, DEEP, family="DM Serif Display")
b += lines(175, 1090, ["When something stressful happens, your body and mind can feed", "each other without your noticing. Seeing the loop is the first step", "to changing it."], 56, 70, INK)
b += '<g transform="translate(175,1300)">{{LOOP:light:gloss}}</g>\n{{FOOTER:light}}\n'
write("poster_loop", "Poster: The Pressure Loop", b)

# 2) the shift -----------------------------------------------------------------------------------------------------
b = f'<rect width="2425" height="3625" fill="{PALE}"/>\n' + eyebrow(175, 330, "THE SOMA-Q SHIFT")
b += lines(175, 560, ["Choose your response", "instead of reacting."], 176, 178, DEEP, family="DM Serif Display")
b += lines(175, 960, ["Three questions, asked in order. Each one keeps pressure from running the moment."], 56, 70, INK)
steps = [("1", "Notice", "What just got activated?", "Meet it with curiosity, not judgment.", "Catch it early, before it becomes a reaction."),
         ("2", "Locate", "Where do I feel it in my body?", "Chest, throat, belly, jaw, shoulders, legs.", "Find the signal while it is still small."),
         ("3", "Choose", "What helps me stay with myself right now?", "Slow exhale, orient, pause, return to the body.", "Come back to steady, then decide.")]
for i, (n, t, q, h, o) in enumerate(steps):
    y = 1130 + i * 600
    b += f'<rect x="175" y="{y}" width="2075" height="540" rx="50" fill="{WHITE}" stroke="{DEEP}" stroke-width="8"/>\n'
    b += f'<circle cx="440" cy="{y+270}" r="145" fill="{DEEP}"/><text x="440" y="{y+318}" text-anchor="middle" font-family="DM Serif Display" font-size="150" fill="{WHITE}">{n}</text>\n'
    b += lines(670, y + 150, [t], 118, 0, DEEP, family="DM Serif Display")
    b += lines(670, y + 255, [q], 60, 0, INK, weight="700")
    b += lines(670, y + 335, [h], 50, 0, INK)
    b += lines(670, y + 440, [o], 52, 0, DEEP, family="DM Serif Display", style="italic")
b += lines(175, 3020, ["The goal is not to stop the thought. The goal is to recognize the pattern of activation,", "meet it with curiosity, allow it, and shift."], 42, 54, DEEP, family="DM Serif Display", style="italic")
b += "{{FOOTER:light}}\n"
write("poster_shift", "Poster: The Soma-Q Shift", b)

# 3) what changes ---------------------------------------------------------------------------------------------------
b = f'<rect width="2425" height="3625" fill="{LINEN}"/>\n' + eyebrow(175, 330, "WHAT CHANGES")
b += lines(175, 560, ["What this work is", "built to restore."], 176, 178, DEEP, family="DM Serif Display")
b += lines(175, 960, ["Three outcomes, held under pressure and lasting after the work ends."], 56, 70, INK)
b += '<g transform="translate(262,1120) scale(.99)">{{OUTCOMES:light}}</g>\n'
for x, a, c in [(430, "Energy that returns,", "not just a day off."), (1212, "Thinking straight", "when decisions land."), (2000, "Present in the work", "and the people in it.")]:
    b += lines(x, 2990, [a], 48, 0, DEEP, weight="700", anchor="middle") + lines(x, 3050, [c], 48, 0, INK, anchor="middle")
b += "{{FOOTER:light}}\n"
write("poster_outcomes", "Poster: What changes", b)

# 4) where do you feel it ---------------------------------------------------------------------------------------------
b = f'<rect width="2425" height="3625" fill="{LINEN}"/>\n' + eyebrow(175, 330, "TRY IT HERE")
b += lines(175, 560, ["Where do you feel", "pressure first?"], 176, 178, DEEP, family="DM Serif Display")
b += lines(175, 960, ["Place a dot where it shows up for you. Noticing it early is how you", "interrupt the loop and keep your energy and clarity."], 56, 70, INK)
b += '<g transform="translate(162,1130) scale(1.0)">{{BODYMAP:light}}</g>\n'
b += lines(1212, 3040, ["Then ask: what do I usually do next?"], 60, 0, DEEP, family="DM Serif Display", style="italic", anchor="middle")
b += "{{FOOTER:light}}\n"
write("poster_where", "Poster: Where do you feel pressure first", b)
print("posters ok")
