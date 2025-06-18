from js import document
import random

def a_chance_at_victory(*args, **kwargs):
    output = document.getElementById("output")
    output.innerHTML = "<br>🎲 <strong>Welcome to A Chance At Victory!</strong><br>"

    points = 0

    weapons = {
        "Greatsword": "*2 points on attack",
        "Sharp Rock": "+3 points",
        "Mouse": "+1 point IF you attack, +2 points IF you get attacked or IF you do nothing",
        "Shield": "+6 points IF you get attacked",
    }

    weapon_choice = random.choice(list(weapons.items()))
    output.innerHTML += f"You got a <strong>{weapon_choice[0]}</strong>! This weapon gives you: {weapon_choice[1]}<br>"

    die_one = random.randint(1,6)
    die_two = random.randint(1,6)
    total = die_one + die_two
    output.innerHTML += f"You rolled a <strong>{die_one}</strong> and a <strong>{die_two}</strong>. Total: <strong>{total}</strong><br>"

    spinner = ["Attack!", "Get Attacked :(", "Do Nothing..."]
    action = random.choice(spinner)
    output.innerHTML += f"You spun: <em>{action}</em><br>"

    attack_multiplier = 1

    if weapon_choice[0] == "Greatsword":
        attack_multiplier = 2
    elif weapon_choice[0] == "Sharp Rock":
        points += 3
    elif weapon_choice[0] == "Mouse":
        points += 1 if action == "Attack!" else 2
    elif weapon_choice[0] == "Shield" and action == "Get Attacked :(":
        points += 6

    points += total

    if action == "Attack!":
        atk_points = 5 * attack_multiplier
        points += atk_points
    elif action == "Get Attacked :(":
        points -= 5

    output.innerHTML += f"<br>🎯 Game over! You got <strong>{points}</strong> points!<br>"

    if points < 0:
        output.innerHTML += "💀 You lose. You beat 0 enemies.<br>"
    elif points <= 7:
        output.innerHTML += "⚔️ You beat one enemy.<br>"
    elif points <= 13:
        output.innerHTML += "⚔️⚔️ You beat two enemies!<br>"
    elif points <= 19:
        output.innerHTML += "⚔️⚔️⚔️ You beat three enemies!!<br>"
    else:
        output.innerHTML += "🏆 You win! ALL FOUR enemies defeated!!!<br>"

