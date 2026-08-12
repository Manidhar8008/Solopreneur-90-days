#!/usr/bin/env python3
"""No-dependency starter: turn a person's current situation into a simple first path."""

QUESTIONS = [
    ("occupation", "What do you do today? "),
    ("skill", "What are you best at? "),
    ("customer", "Who do you understand or have access to? "),
    ("problem", "What problem do you repeatedly see? "),
    ("hours", "How many hours per week can you use? "),
    ("goal", "What would you like to achieve in 90 days? "),
]

def main():
    print("\nSOLopreneur Pathfinder\n")
    answers = {}
    for key, q in QUESTIONS:
        answers[key] = input(q).strip()

    print("\nYOUR STARTING PATH\n")
    print(f"Occupation: {answers['occupation']}")
    print(f"Strength: {answers['skill']}")
    print(f"Customer access: {answers['customer']}")
    print(f"Problem hypothesis: {answers['problem']}")
    print(f"Available time: {answers['hours']}")
    print(f"90-day outcome: {answers['goal']}")

    print("\nNEXT 5 ACTIONS")
    print("1. Interview 3 people who experience the problem.")
    print("2. Write down the current workflow.")
    print("3. Quantify the cost of the problem.")
    print("4. Create one narrow offer.")
    print("5. Ask one real prospect to pay for the outcome.")

    print("\nRule: do not build software until the problem and buyer are clear.")

if __name__ == "__main__":
    main()
