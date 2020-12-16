import random
import pyfiglet
from lib.leet import leet_converter
from termcolor import colored

def after_start():
    fontList = ["3-d", "3x5", "5lineoblique", "alligator", "alligator2", "alphabet", "avatar",
                "banner", "banner3-D", "banner3", "banner4", "barbwire", "basic", "bell", "big", "bigchief",
                "binary", "block", "bubble", "bulbhead", "calgphy2", "caligraphy", "catwalk", "chunky", "coinstak",
                "colossal", "computer", "contessa", "contrast", "cosmic", "cosmike", "cricket", "cyberlarge",
                "cybermedium", "cybersmall", "diamond", "digital", "doom", "drpepper",
                "eftifont", "eftirobot", "eftitalic", "eftiwater", "epic",
                "fender", "fourtops", "fuzzy", "goofy", "gothic", "graffiti", "hollywood", "invita", "italic", "ivrit",
                "jazmine", "jerusalem", "katakana",
                "kban", "larry3d", "lcd", "lean", "letters", "linux", "lockergnome", "marquee", "maxfour",
                "mike", "mini", "mirror", "mnemonic", "morse", "moscow", "nancyj-fancy", "nancyj-underlined",
                "nancyj", "nipples", "ntgreek", "o8", "ogre", "pawp", "peaks", "pebbles", "pepper", "poison",
                "puffy", "pyramid", "rectangles", "relief", "relief2", "rev", "roman", "rot13", "rounded",
                "rowancap", "rozzo", "runic", "sblood", "script", "serifcap", "shadow", "slant",
                "slide", "slscript", "small", "smisome1", "smkeyboard", "smscript", "smshadow", "smslant",
                "smtengwar", "speed", "stampatello", "standard", "starwars", "stellar", "stop", "straight",
                "tanja", "tengwar", "term", "thick", "thin", "ticks", "ticksslant", "tinker-toy",
                "tombstone", "trek", "tsalagi", "univers", "usaflag", "weird"]
    fontValue = random.choice(fontList)

    colorList = ["grey","red","green","yellow","blue","magenta","cyan","white"]
    randomColor = random.choice(colorList)

    banner= leet_converter("mr_chatrobot")
    ascii_banner = pyfiglet.figlet_format(banner, font=fontValue)
    ascii_banner_colored = colored(ascii_banner, randomColor)
    print(ascii_banner_colored)

