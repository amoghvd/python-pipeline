import random

def roll_dice() -> int:
    # Returns a random integer between 1 and 6
    return random.randint(1, 6)

def get_fortune(name: str) -> str:
    # Returns a personalized fortune message
    fortunes = [
        "will discover a hidden talent today!",
        "will write bug-free code on the first try!",
        "should drink a glass of water and take a stretch break.",
        "will have exceptional luck with Python today!"
    ]
    selected_fortune = random.choice(fortunes)
    return f"Hello {name}, you {selected_fortune}"

def is_even(number: int) -> bool:
    # Checks if a given number is even
    return number % 2 == 0

if __name__ == "__main__":
    print("--- Running Python App ---")
    print(get_fortune("Amogh"))
    print(f"Dice Roll: {roll_dice()}")
    print(f"Is 42 even? {is_even(42)}")
