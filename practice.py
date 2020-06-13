import random


def run(*kid):
    print(f"{kid} ran")


def swing(*kid):
    print(f"{kid} is playing on the swing")


def slide(*kid):
    print(f"{kid} is playing on slide")


def hide_and_seek(*kid):
    print(f"{kid} is playing hide and seek")


running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Maybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

for kid in running_kids:
    run(kid)
for kid in swinging_kids:
    swing(kid)
for kid in sliding_kids:
    slide(kid)
for kid in hiding_kids:
    hide_and_seek(kid)


def create_person(first_name, last_name, age, occupation):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "occupation": occupation
    }


taylor = create_person("Taylor", "Catroll", 30, "visionary")


my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))
print(my_randoms)
# Generate a list of numbers 1..10
numbers_1_to_10 = range(1, 11)
# Iterate from 1 to 10
for number in numbers_1_to_10:
    the_numbers_match = False
    # Iterate your random number list here
    if number in my_randoms:
        # Does my_randoms contain number? Change the boolean.
        the_numbers_match = True

    if the_numbers_match:
        print(f'{number} is in the random list')
    else:
        print(f'{number} is not in the random list')


def chicken_monkey(nums):
    for num in nums:
        if num % 5 == 0 & num % 7 == 0:
            print("ChickyChickyParmParm")
        elif num % 7 == 0:
            print("ParmParm")
        elif num % 5 == 0:
            print("ChickyChicky")
        else:
            print(num)


example = range(1, 101)

chicken_monkey(example)


def cacl_dollars():
    piggyBank = {
        "pennies": 342,
        "nickels": 9,
        "dimes": 32,
        "quarters": 65
    }
    dollarAmount = piggyBank["pennies"] / 100 + piggyBank["nickels"] / \
        20 + piggyBank["dimes"] / 10 + piggyBank["quarters"] / 4
    print("dollar amount :", dollarAmount)


cacl_dollars()
