import random


def leet_converter(message):
    """
    Converter to leet https://v2.cryptii.com/text/leetspeak
    """

    replacement = (
        ('hacker', 'haxor'), ('otherf', '*therf'), ('uck', '*ck'), ('hacker', 'HaX0R'), ('elite', '1337'), ('a', '4'), ('e', '3'),
        ('l', '1'), ('o', '0'), ('t', '7'), ('i', '1'), ('A', '4'), ('E', '3'), ('B', '8'), ('c', 'k'),
        ('L', '1'), ('O', '0'), ('T', '7'), ('A', '@'), ('a', '@'), ('I', '1'), ('C', 'K'), ('s', 'z'),
        ('S', '2'), ('f', 'Ph'), ('o', 'ø'), ('E', '£'), ('E', 'ε'), ('j', '¿'), ('s', 'ŝ'), ('u', 'µ'),
        ('E', '€'), ('f', 'ƒ')
    )

    replacements = random.sample(replacement, 5)

    for old, new in replacements:
        message = message.replace(old, new)

    return message


emoji = [
    '@( * O * )@',
    'ô¿ô',
    '(-.-)Zzz...',
    '-@-@-',
    'd[ o_0 ]b',
    'ε(´סּ︵סּ`)з',
    ' c[○┬●]כ ',
    '龴ↀ◡ↀ龴',
    '☁ ▅▒░☼‿☼░▒▅ ☁',
    '✌⊂(✰‿✰)つ✌',
    'ˁ˚ᴥ˚ˀ',
    '^⨀ᴥ⨀^',
    '✌(◕‿-)✌',
    '(╯°□°）╯︵ ┻━┻'
    '(✖╭╮✖)',
    '(✿ ♥‿♥) ',
    ' (╯︵╰,)',
    ' ‹^› ‹(•_•)› ‹^›',
    '(<>..<>)',
    '༼☉ɷ⊙༽',
    'ب_ب'
]
