import json
import random

QUESTIONS_COUNT = 7

INSTRUCTION = """
    INSTRUCTION:
    Welcome to the "Who Wants to Be a Millionaire" game! Answer the questions correctly to win money!
    You can use the following hints:
    1. 50/50: eliminates two wrong answers.
    2. Call a friend: gives a random correct answer.
    3. Votes: shows the percentage of people who chose each option.
"""

INVITE_TO_ENTER_ANSWER = """
    Enter number or the answer OR 'help' for help
"""

CHOOSE_HELP = """
    Choose help:
    1. 50/50
    2. Call to friend
    3. Votes
"""

random_questions = []
used_help = {'50/50': False, 'call_friend': False, 'votes': False}

def set_all_variables():
    global random_questions

    with open('questions.json', 'r', encoding='utf-8') as file:
        all_questions = json.load(file)

    random_questions = random.sample(all_questions, QUESTIONS_COUNT)

def apply_5050(answers):
    # Remove two wrong answers randomly
    wrong_answers = [answer for answer in answers.values() if answer != answers['correct']]
    random.shuffle(wrong_answers)
    answers_to_remove = wrong_answers[:2]
    remaining_answers = [ans for ans in answers.items() if ans[1] not in answers_to_remove]
    return dict(remaining_answers)

def call_friend(answers):
    # Randomly choose one of the answers to be "correct"
    return random.choice(list(answers.items()))[1]

def show_votes(answers):
    # This function simulates the votes and shows percentages for each answer
    # We assume the correct answer gets 70% of the votes, the others get 10% each
    vote_distribution = {
        answers['correct']: 70,
        answers['wrong1']: 10,
        answers['wrong2']: 10,
        answers['wrong3']: 10
    }
    return vote_distribution

def play_game():
    global INSTRUCTION, INVITE_TO_ENTER_ANSWER, random_questions, CHOOSE_HELP, used_help
    print(INSTRUCTION)

    user_final_score = 0

    for question_index in range(len(random_questions)):
        question = random_questions[question_index]['question']
        answers = random_questions[question_index]['answers']
        print(question)

        all_answers = [
            ("1", answers["correct"]),
            ("2", answers["wrong1"]),
            ("3", answers["wrong2"]),
            ("4", answers["wrong3"])
        ]
        random.shuffle(all_answers)  # перемешиваем варианты ответов
    
        answer_number = 1
        this_answers = {}
        for is_correct, answer in all_answers:
            print(f'{answer_number}: {answer}')
            this_answers[answer_number] = answer
            answer_number += 1

        # Начальный выбор ответа
        user_choice = input(INVITE_TO_ENTER_ANSWER)
        while user_choice not in ['1', '2', '3', '4', 'help']: 
            print("Enter correct answer")

        if user_choice in ['1', '2', '3', '4']:
            if this_answers[int(user_choice)] == answers['correct']:
                user_final_score += 1
                print("CORRECT!")
            else:
                print("Incorrect(")
        else:
            print(CHOOSE_HELP)
            user_choice = input('Enter your choice: ')
            while user_choice not in ['1', '2', '3']:
                print('Enter correct choice')
                user_choice = input('Enter your choice: ')
            
            # Применяем подсказку
            if user_choice == '1' and not used_help['50/50']:
                used_help['50/50'] = True
                remaining_answers = apply_5050(answers)
                print("50/50 Hint: The remaining answers are:")
                for idx, ans in enumerate(remaining_answers.values(), start=1):
                    print(f'{idx}: {ans}')
                # Запрашиваем новый выбор ответа после подсказки
                user_choice = input(INVITE_TO_ENTER_ANSWER)
                while user_choice not in ['1', '2', '3', '4']:
                    print("Enter correct answer")
                    user_choice = input(INVITE_TO_ENTER_ANSWER)
                if this_answers[int(user_choice)] == answers['correct']:
                    user_final_score += 1
                    print("CORRECT!")
                else:
                    print("Incorrect(")

            elif user_choice == '2' and not used_help['call_friend']:
                used_help['call_friend'] = True
                friend_answer = call_friend(answers)
                print(f"Call to friend: The friend thinks the answer is: {friend_answer}")
                # Запрашиваем новый выбор ответа после подсказки
                user_choice = input(INVITE_TO_ENTER_ANSWER)
                while user_choice not in ['1', '2', '3', '4']:
                    print("Enter correct answer")
                    user_choice = input(INVITE_TO_ENTER_ANSWER)
                if this_answers[int(user_choice)] == answers['correct']:
                    user_final_score += 1
                    print("CORRECT!")
                else:
                    print("Incorrect(")

            elif user_choice == '3' and not used_help['votes']:
                used_help['votes'] = True
                vote_distribution = show_votes(answers)
                print("Votes distribution:")
                for answer, percentage in vote_distribution.items():
                    print(f"{answer}: {percentage}%")
                # Запрашиваем новый выбор ответа после подсказки
                user_choice = input(INVITE_TO_ENTER_ANSWER)
                while user_choice not in ['1', '2', '3', '4']:
                    print("Enter correct answer")
                    user_choice = input(INVITE_TO_ENTER_ANSWER)
                if this_answers[int(user_choice)] == answers['correct']:
                    user_final_score += 1
                    print("CORRECT!")
                else:
                    print("Incorrect(")
                    
            else:
                print("You've already used this help!")
                continue  # Возвращаемся к вопросу, если помощь уже использована

        print(f"Your final score = {user_final_score}")

if __name__ == '__main__':
    set_all_variables()
    play_game()
