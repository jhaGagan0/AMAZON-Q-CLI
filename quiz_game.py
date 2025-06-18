python
#!/usr/bin/env python3

import random
import time
import sys
import os

# Expanded question pool organized by difficulty level
questions = {
    "easy": [
        {
            "question": "What is the capital of France?",
            "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
            "answer": "C",
            "fun_fact": "Paris is also known as the 'City of Light' or 'La Ville Lumière'!"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B",
            "fun_fact": "Mars gets its reddish color from iron oxide (rust) on its surface!"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["A. Elephant", "B. Giraffe", "C. Blue Whale", "D. Polar Bear"],
            "answer": "C",
            "fun_fact": "A blue whale's heart is the size of a small car and can be heard beating from 2 miles away!"
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["A. Gold", "B. Oxygen", "C. Osmium", "D. Oganesson"],
            "answer": "B",
            "fun_fact": "Oxygen makes up about 21% of Earth's atmosphere and 65% of the human body!"
        },
        {
            "question": "How many continents are there on Earth?",
            "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
            "answer": "C",
            "fun_fact": "The seven continents are Asia, Africa, North America, South America, Antarctica, Europe, and Australia!"
        },
        {
            "question": "Which animal is known as the 'King of the Jungle'?",
            "options": ["A. Tiger", "B. Lion", "C. Elephant", "D. Gorilla"],
            "answer": "B",
            "fun_fact": "Despite being called 'King of the Jungle', lions actually live in grasslands and plains!"
        },
        {
            "question": "What is the closest star to Earth?",
            "options": ["A. Proxima Centauri", "B. Polaris", "C. The Sun", "D. Alpha Centauri"],
            "answer": "C",
            "fun_fact": "The Sun is about 93 million miles (150 million km) from Earth!"
        },
        {
            "question": "Which country is home to the kangaroo?",
            "options": ["A. New Zealand", "B. South Africa", "C. Australia", "D. Brazil"],
            "answer": "C",
            "fun_fact": "Kangaroos can't walk backward - it's one reason they appear on Australia's coat of arms!"
        }
    ],
    "medium": [
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],
            "answer": "B",
            "fun_fact": "Shakespeare invented over 1,700 words that we still use today!"
        },
        {
            "question": "What year did World War II end?",
            "options": ["A. 1943", "B. 1944", "C. 1945", "D. 1946"],
            "answer": "C",
            "fun_fact": "WWII was the deadliest conflict in human history, with 70-85 million fatalities."
        },
        {
            "question": "Which country is home to the Great Barrier Reef?",
            "options": ["A. Brazil", "B. Australia", "C. Indonesia", "D. Mexico"],
            "answer": "B",
            "fun_fact": "The Great Barrier Reef is the world's largest coral reef system and can be seen from space!"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["A. Diamond", "B. Platinum", "C. Titanium", "D. Quartz"],
            "answer": "A",
            "fun_fact": "Diamonds are formed deep in the Earth under extreme heat and pressure over billions of years!"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"],
            "answer": "C",
            "fun_fact": "The Mona Lisa has no visible eyebrows or eyelashes!"
        },
        {
            "question": "Which element has the symbol 'Au' on the periodic table?",
            "options": ["A. Silver", "B. Gold", "C. Aluminum", "D. Argon"],
            "answer": "B",
            "fun_fact": "The symbol 'Au' comes from the Latin word 'aurum', meaning 'shining dawn'!"
        },
        {
            "question": "What is the capital of Japan?",
            "options": ["A. Seoul", "B. Beijing", "C. Tokyo", "D. Bangkok"],
            "answer": "C",
            "fun_fact": "Tokyo was formerly known as Edo until 1868!"
        },
        {
            "question": "Which planet has the most moons?",
            "options": ["A. Jupiter", "B. Saturn", "C. Uranus", "D. Neptune"],
            "answer": "B",
            "fun_fact": "Saturn has at least 82 moons, with new ones still being discovered!"
        }
    ],
    "hard": [
        {
            "question": "What is the smallest prime number?",
            "options": ["A. 0", "B. 1", "C. 2", "D. 3"],
            "answer": "C",
            "fun_fact": "2 is the only even prime number - all others are odd!"
        },
        {
            "question": "Which element has the atomic number 79?",
            "options": ["A. Silver", "B. Gold", "C. Platinum", "D. Mercury"],
            "answer": "B",
            "fun_fact": "All the gold ever mined in human history would fit into a cube about 21 meters on each side!"
        },
        {
            "question": "In which year was the first human heart transplant performed?",
            "options": ["A. 1957", "B. 1967", "C. 1977", "D. 1987"],
            "answer": "B",
            "fun_fact": "Dr. Christiaan Barnard performed the first successful heart transplant in Cape Town, South Africa!"
        },
        {
            "question": "Who discovered penicillin?",
            "options": ["A. Marie Curie", "B. Louis Pasteur", "C. Alexander Fleming", "D. Joseph Lister"],
            "answer": "C",
            "fun_fact": "Fleming discovered penicillin by accident when he noticed mold killing bacteria in a petri dish!"
        },
        {
            "question": "What is the capital of Mongolia?",
            "options": ["A. Astana", "B. Ulaanbaatar", "C. Bishkek", "D. Tashkent"],
            "answer": "B",
            "fun_fact": "Ulaanbaatar is the world's coldest capital city with an annual average temperature of -1.3°C!"
        },
        {
            "question": "Which of these scientists developed the theory of general relativity?",
            "options": ["A. Isaac Newton", "B. Niels Bohr", "C. Albert Einstein", "D. Stephen Hawking"],
            "answer": "C",
            "fun_fact": "Einstein's brain was removed during his autopsy and studied for decades afterward!"
        },
        {
            "question": "What is the chemical formula for sulfuric acid?",
            "options": ["A. H2SO3", "B. H2SO4", "C. HSO4", "D. H2S2O7"],
            "answer": "B",
            "fun_fact": "Sulfuric acid is the most produced chemical in the world by volume!"
        },
        {
            "question": "Which ancient wonder was located in Alexandria?",
            "options": ["A. Hanging Gardens", "B. Colossus of Rhodes", "C. Lighthouse (Pharos)", "D. Temple of Artemis"],
            "answer": "C",
            "fun_fact": "The Lighthouse of Alexandria was one of the tallest man-made structures for hundreds of years!"
        }
    ]
}

# Lists for varied feedback messages
correct_messages = [
    "Great job! 🎉",
    "You're on fire! 🔥",
    "Nailed it! 👏",
    "Brilliant! ✨",
    "That's correct! 🌟",
    "Spot on! 🎯",
    "You're crushing it! 💪",
    "Absolutely right! 🧠",
    "Perfect answer! 👌",
    "You know your stuff! 🤓"
]

incorrect_messages = [
    "Oops! But you got this 💪",
    "Not quite, but good try!",
    "Shake it off and move on 🚀",
    "Almost there! Keep going! 🌈",
    "Don't worry, next one's yours! 🍀",
    "Learning happens in mistakes! 📚",
    "That's tricky! Let's continue! 🧩",
    "Nice effort! Next question awaits! ⏭️",
    "Keep your spirits up! 🌞",
    "No worries, you're still awesome! ⭐"
]

# Performance messages based on score percentage
performance_messages = {
    (0, 20): "Keep exploring! Knowledge is a journey, not a destination! 🌱",
    (21, 40): "Good effort! A little more practice and you'll be a quiz master! 📈",
    (41, 60): "Not bad at all! You've got a solid foundation of knowledge! 🏗️",
    (61, 80): "Great job! You really know your stuff! 🎓",
    (81, 99): "Excellent work! You're nearly at genius level! 🧠",
    (100, 100): "Perfect score! You're officially a quiz genius! 🏆"
}

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slowly(text, delay=0.03):
    """Print text with a slight delay for better UX."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def display_progress_bar(current, total, width=30):
    """Display a text-based progress bar."""
    filled_width = int(width * current / total)
    bar = '█' * filled_width + '░' * (width - filled_width)
    return f"[{bar}] Question {current}/{total}"

def get_user_name():
    """Get the user's name for personalization."""
    clear_screen()
    print("=" * 60)
    print_slowly("👋 Welcome to the ULTIMATE KNOWLEDGE QUEST! 👋")
    print("=" * 60)

    while True:
        name = input("\nWhat's your name, adventurer? ").strip()
        if name:
            return name
        print("Come on, don't be shy! Tell me your name.")

def display_welcome(name):
    """Display personalized welcome message and game instructions."""
    clear_screen()
    print("=" * 60)
    print_slowly(f"🎮 WELCOME TO THE KNOWLEDGE QUEST, {name.upper()}! 🎮")
    print("=" * 60)
    print_slowly("\nPrepare for an adventure through the realms of knowledge!")
    print_slowly("You'll face 5 challenging questions on your quest.")
    print_slowly("Choose wisely between options A, B, C, or D for each question.")
    print_slowly("Let's see if you have what it takes to become a Knowledge Master!\n")
    print("=" * 60)
    input("\nPress Enter to begin your quest...")

def get_difficulty():
    """Get the difficulty level from the user."""
    clear_screen()
    print("=" * 60)
    print_slowly("🔍 SELECT YOUR CHALLENGE LEVEL:")
    print_slowly("1. Easy - For knowledge apprentices 🌱")
    print_slowly("2. Medium - For knowledge seekers 🔎")
    print_slowly("3. Hard - For knowledge masters 🧙")
    print("=" * 60)

    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice == '1':
            return "easy"
        elif choice == '2':
            return "medium"
        elif choice == '3':
            return "hard"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def ask_question(question_data, question_num, total_questions):
    """Ask a question and return whether the answer was correct."""
    clear_screen()
    print("=" * 60)
    progress = display_progress_bar(question_num, total_questions)
    print(progress)
    print("=" * 60)
    print_slowly(question_data["question"])
    print("=" * 60)

    for option in question_data["options"]:
        print_slowly(option)

    while True:
        answer = input("\nYour answer (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            is_correct = answer == question_data["answer"]
            return is_correct
        else:
            print("Invalid choice. Please enter A, B, C, or D.")

def display_result(is_correct, question_data):
    """Display whether the answer was correct or not with fun feedback."""
    print("\n" + "=" * 60)

    if is_correct:
        message = random.choice(correct_messages)
        print_slowly(f"{message}")
        print_slowly(f"The correct answer is indeed {question_data['answer']}.")
    else:
        message = random.choice(incorrect_messages)
        print_slowly(f"{message}")
        print_slowly(f"The correct answer was {question_data['answer']}.")

    print_slowly(f"\n✨ Fun Fact: {question_data['fun_fact']}")
    print("=" * 60)
    input("\nPress Enter to continue your quest...")

def run_quiz(difficulty, name, num_questions=5):
    """Run the quiz with the selected difficulty level."""
    quiz_questions = questions[difficulty].copy()
    random.shuffle(quiz_questions)
    score = 0

    for i, question_data in enumerate(quiz_questions[:num_questions], 1):
        is_correct = ask_question(question_data, i, num_questions)
        if is_correct:
            score += 1
        display_result(is_correct, question_data)

    return score

def get_performance_message(score, total):
    """Get a performance message based on score percentage."""
    percentage = (score / total) * 100

    for (lower, upper), message in performance_messages.items():
        if lower <= percentage <= upper:
            return message

    return "Great effort on your knowledge quest!"

def display_final_score(score, difficulty, name, total_questions=5):
    """Display the final score and closing message."""
    clear_screen()
    print("=" * 60)
    print_slowly("🏆 QUEST COMPLETED! 🏆")
    print("=" * 60)

    percentage = (score / total_questions) * 100
    print_slowly(f"\n{name}, you scored {score} out of {total_questions} on {difficulty.capitalize()} difficulty!")
    print_slowly(f"That's {percentage:.1f}% correct!")

    performance_message = get_performance_message(score, total_questions)
    print_slowly(f"\n{performance_message}")

    print("=" * 60)
    print_slowly(f"\nThanks for playing the Knowledge Quest, {name}!")
    print_slowly("Every quest brings new wisdom. Will you embark on another?")

def play_again():
    """Ask if the user wants to play again."""
    print("\n" + "=" * 60)
    while True:
        choice = input("\nWould you like to play again? (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

def main():
    """Main function to run the quiz game."""
    try:
        name = get_user_name()
        display_welcome(name)

        while True:
            difficulty = get_difficulty()
            score = run_quiz(difficulty, name)
            display_final_score(score, difficulty, name)

            if not play_again():
                clear_screen()
                print_slowly(f"Farewell, {name}! May your quest for knowledge never end! 👋")
                break

    except KeyboardInterrupt:
        clear_screen()
        print_slowly("\nQuest terminated. Until we meet again, brave adventurer! 👋")
        sys.exit(0)

if __name__ == "__main__":
    main()
