# Who Wants to Be a Millionaire Game

A Python-based quiz game inspired by the popular TV show "Who Wants to Be a Millionaire". This game features multiple-choice questions in Ukrainian with lifeline options similar to the TV show format.

## Features

- Random selection of questions from a large question pool
- Multiple-choice format with 4 options per question
- Three types of lifelines (help options):
  1. 50/50: Eliminates two wrong answers
  2. Call a Friend: Provides a random answer (with high probability of being correct)
  3. Audience Vote: Shows percentage distribution of answers
- Score tracking system
- Questions on various topics including geography, science, literature, and general knowledge

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the files
2. Ensure you have Python 3.x installed
3. Place both files in the same directory

## Usage

1. Open terminal/command prompt
2. Navigate to the game directory
3. Run the game:

```bash
python game.py
```

## Game Rules

1. Each game consists of 7 random questions
2. For each question, you have four options to choose from
3. You can use each lifeline only once per game:
   - Type 'help' when prompted for an answer
   - Choose the lifeline you want to use (1-3)
4. Enter the number (1-4) corresponding to your answer choice
5. Your score increases with each correct answer

## Lifelines Explanation

- **50/50**: Removes two incorrect answers, leaving you with two choices (one correct and one incorrect)
- **Call a Friend**: Simulates asking a friend for help by providing a random answer (weighted towards the correct answer)
- **Audience Vote**: Shows a simulated audience vote distribution, with the correct answer typically receiving the highest percentage

## Question Format

Questions are stored in JSON format with the following structure:

```json
{
    "question": "Question text",
    "answers": {
        "correct": "Correct answer",
        "wrong1": "First wrong answer",
        "wrong2": "Second wrong answer",
        "wrong3": "Third wrong answer"
    }
}
```

## Contributing

To add new questions:

1. Open `questions.json`
2. Follow the existing question format
3. Add your new question to the array
4. Save the file

## Notes

- Each lifeline can only be used once per game
- The game is currently in Ukrainian language
- Questions are randomly selected, so you might see different questions each time you play

## Contacts

Email: <ch.sergey.rb@gmail.com>
