def make_sandwich(*ingredients):
    print("\nI want my sandwich to include:")
    for ingredient in ingredients:
        print(f"{ingredient}")

make_sandwich("bacon", "lettuce", "tomato")
make_sandwich("peanut butter", "jelly")