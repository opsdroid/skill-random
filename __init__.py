from opsdroid.matchers import match_regex
from random import choice
from d20 import roll, SimpleStringifier

COIN_FLIP_RESPONSES = [
    "It landed on {result}",
    "You got {result}",
    "It's {result}"
]

@match_regex(r'roll a dic?e', case_sensitive=False)
async def roll_die(opsdroid, config, message):
    await message.respond("You rolled {}".format(roll("1d6").result))

@match_regex(r'roll( a)? (?P<dice>\d*d\d+.*)', case_sensitive=False)
async def roll_dice(opsdroid, config, message):
    try:
        await message.respond("You rolled {}".format(roll(message.regex.group('dice'),stringifier=SimpleStringifier())))
    except:
        await message.respond("Sorry, did you mean to roll dice? Try 'roll a d6' or 'roll 3d8+2'")

@match_regex(r'flip a coin', case_sensitive=False)
async def flip_a_coin(opsdroid, config, message):
    result = choice(["heads", "tails"])
    text = choice(COIN_FLIP_RESPONSES).format(result=result)
    await message.respond(text)
