from our_dice import Dice

def sortNumbers(*numbers):
    list = sorted(numbers)
    list.sort(reverse=True)
    return list

gamer1Dice = Dice()
gamer2Dice = Dice()
gamer3Dice = Dice()

for i in range(5):
    gamer1Dice.playDice()
    gamer2Dice.playDice()
    gamer3Dice.playDice()

print(f'gamer1: {gamer1Dice.getNumbers()}')
print(f'Sum of Gamer1: {gamer1Dice.getSum()}')
print('------------------------')

print(f'gamer2: {gamer2Dice.getNumbers()}')
print(f'Sum of Gamer2: {gamer2Dice.getSum()}')
print('------------------------')

print(f'gamer3: {gamer3Dice.getNumbers()}')
print(f'Sum of Gamer3: {gamer3Dice.getSum()}')
print('------------------------')

sortedNumbers = sortNumbers(gamer1Dice.getSum(),
                            gamer2Dice.getSum(),
                            gamer3Dice.getSum())

print('========================')
print(f'1등 : {sortedNumbers[0]}     WIN!!')
print(f'2등 : {sortedNumbers[1]} ')
print(f'3등 : {sortedNumbers[2]} ')
print('========================')