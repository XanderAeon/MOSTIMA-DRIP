# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("MOSTIMA")
define e = Character("Exusiai")
define u = Character("???")
image MOSTIMA = "images/MOSTIMA DRIP.png"
image MOSTIMA BLACK = "images/MOSTIMA BLACK.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room
    
    e "My name is Exusiai, and I'm a messenger for Penguin Logistics!"
    e "...Or at least I was supposed to be."
    e "Last month, I was transfered to Rhodes Island, an intependent paramilitary organization."
    e "Or was it pharmaceutical company? It's hard to tell."
    e "Everybody's nice and the pay is good, but I still don't know why the boss sent me here."
    e "It's kind of lonely without the rest of Penguin Logistics."
    e "Croissant is here too, but she's always going out to fight with that doctor."
    e "I'm supposed to train with a couple new recruits later today... I hope Texas is one of them."
    
    scene corridor
    
    e "Training time!"
    e "It's mostly Casters and Medics."
    e "I'll show these guys how to shoot!"
    e "...I hope that's why I was grouped with them. All the higher-ups are so ominous here, I don't always know what I should be doing."
    
    u "HEY!"
    e "...?"
    u "YO, EXUSIAI!"
    e "! It's...!"
    e "Mostima!!"
    "The ultramarine caster steps out of the crowd to meet me."
    
    show MOSTIMA BLACK
    
    e "...!"
    "I instinctively recoil after seeing Mostima in full."
    m "Yo, how's it going!? It's been a while!"
    e "Mostima, you..."
    m "...Hm? Ah, of course you noticed."
    e "I didn't think we would meet again like this already, but for you to show up like that..."
    m "People change, Exusiai."
    m "And ya know, right now, for me..."
    
    show MOSTIMA

    # These display lines of dialogue.

    m "I'M STRAIGHT FUCKIN DRIPPIN YO!!!!!"
    
    e "Holy shit."

    # This ends the game.

    return
