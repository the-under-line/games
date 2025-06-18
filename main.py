from js import document
import random
    
    
def a_chance_at_victory(*args, **kwargs):
    output = document.getElementById("output")
    output.innerHTML = "Welcome to A Chance At Victory!"
    points = 0
    
    # Bag
    weapons = {
        "Greatsword": "*2 points on attack",
        "Sharp Rock": "+3 points",
        "Mouse": "+1 point IF you attack, +2 points IF you get attacked or IF you do nothing",
        "Shield": "+6 points IF you get attacked",
    }
    # input("Pull a random weapon from the bag (type 'choose' to choose): ")
    weapon_choice = random.choice(list(weapons.items()))
    output.innerHTML = f"You got a {weapon_choice[0]}! This weapon gives you {weapon_choice[1]}!\n"
    
    # Dice
    # input("Roll 2 die for your starting points (type 'roll' to roll): ")
    die_one = random.randint(1,6)
    die_two = random.randint(1,6)
    total = die_one+die_two
    output.innerHTML = f"You got a {die_one} on your first die and a {die_two} on your second die! This totals to {total}!\n"
    
    # Spinner
    # input("Spin a spinner: will you attack, get attacked, or do nothing (type 'spin' to spin)?: ")
    spinner = ["Attack!", "Get Attacked :(", "Do Nothing..."]
    action = random.choice(spinner)
    output.innerHTML = f"You got {action}\n"
    
    # Final
    attack_multiplier = 1
    
    if weapon_choice[0] == "Greatsword":
        attack_multiplier = 2
    elif weapon_choice[0] == "Sharp Rock":
        points += 3
    elif weapon_choice[0] == "Mouse":
        if action == "Attack!":
            points += 1
        else:
            points += 2
    elif weapon_choice[0] == "Shield":
        if action == "Get Attacked :(":
            points += 6
    
    
    points += total
    
    
    if action == "Attack!":
        atk_points = 5 * attack_multiplier
        points += atk_points
    elif action == "Get Attacked :(":
        points -= 5
    
    output.innerHTML = f"Game is over! You got {points} points!"
    
    if points < 0:
        output.innerHTML = "You lose. You beat 0 enemies."
    elif points <= 7:
        output.innerHTML = "You beat one enemy."
    elif points <= 13:
        output.innerHTML = "You beat two enemies!"
    elif points <= 19:
        output.innerHTML = "You beat three enemies!!"
    elif points >= 20:
        output.innerHTML = "You win! You beat ALL FOUR enemies!!!!"
