# A dictionary that stores questions and answers.
# Have a variable that tracks the score of the player.
# Loop through the dictionary using the key values pairs.
# Display each question to the user and allow them to answer.
# Tell them if they are right or wrong.
# Show the final result when quiz is completed.


Quiz = {
    "Question_1": {
        "Question": "What is the capital of Ghana?",
        "Answer": "Accra"
    },

    "Question_2": {
        "Question": "In which year did Ghana gain independence?",
        "Answer": "1957"
    },

    "Question_3": {
        "Question": "Who was Ghana's first president?",
        "Answer": "Kwame Nkrumah"
    },

    "Question_4": {
        "Question": "How was Ghana formerly known?",
        "Answer": "Gold Coast"
    },

    "Question_5": {
        "Question": "Who was Ghana’s first prime minister?",
        "Answer": "Kwame Nkrumah"
    },

    "Question_6": {
        "Question": "Who became Ghana’s president on 7 January 2001?",
        "Answer": "John Kufuor"
    },

    "Question_7": {
        "Question": "Who overthrew the government of Kofi Busia and established military rule in Ghana in 1972?",
        "Answer": "Ignatius Kutu Acheampong"
    },

    "Question_8": {
        "Question": "Who designed the Ghana coat of arms?",
        "Answer": "Amon Kotei"
    },

    "Question_9": {
        "Question": "Who composed the national anthem of Ghana?",
        "Answer": "Philip Gbeho"
    },

    "Question_10": {
        "Question": "What is the name of the Ghanaian man who served as the seventh Secretary-General of the United Nations for ten years?",
        "Answer": "Kofi Annan"
    },
}

Score = 0

for key, value in Quiz.items():
    print(value['Question'])
    Answer = input('Answer: ')

    if Answer.lower() == value['Answer'].lower():
        print('Correct')
        Score += 1
        print("Your score is: " + str(Score))
        print("")
        print("")

    else:
        print("Incorrect!")
        print('The correct answer is: ' + value['Answer'])
        print('Your score is: ' + str(Score))
        print("")
        print("")


print("Your total score is " + str(Score) + " out of 10 questions.")
print("Your percentage score is " + str(int(Score/10 * 100)) + "%")
print("")
