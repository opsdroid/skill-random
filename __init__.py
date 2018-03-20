from opsdroid.matchers import match_regex
import random


DICE_ROLL_RESPONSES = [
    "The dice says {number}",
    "You rolled a {number}",
    "It's a {number}"
]


COIN_FLIP_RESPONSES = [
    "It landed on {result}",
    "You got {result}",
    "It's {result}"
]


@match_regex(r'roll a dice', case_sensitive=False)
async def roll_a_dice(opsdroid, config, message):
    number = random.randint(1,6)
    text = random.choice(DICE_ROLL_RESPONSES).format(number=number)
    await message.respond(text)


@match_regex(r'flip a coin', case_sensitive=False)
async def flip_a_coin(opsdroid, config, message):
    result = random.choice(["heads", "tails"])
    text = random.choice(COIN_FLIP_RESPONSES).format(result=result)
    await message.respond(text)
