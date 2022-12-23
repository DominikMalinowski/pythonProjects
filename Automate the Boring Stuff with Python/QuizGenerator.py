
import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', \
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', \
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', \
           'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', \
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', \
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', \
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', \
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', \
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',\
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',\
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', \
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', \
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# generated quiz

for quiz_num in range(35):

    # utworzenie plików pytan i odpowiedzie
    quiz_file  = open('capital_quiz%s.txt' % (quiz_num + 1), 'w')
    answer_key = open('ca[ital_quiz_answer%s.txt' % (quiz_num + 1), 'w')

    # zapis naglowka quizu
    quiz_file.write('Imie i nazwisko:\n \nData:\n \nKlasa: \n\n')
    quiz_file.write((' ' * 20) + 'Quiz stolic stanow (Quiz %s)' % (quiz_num + 1))
    quiz_file.write('\n\n')

    # losowe ustawienie kolejnosci
    states = list(capitals.keys())
    random.shuffle(states)

    # intercja przez 50 stanow i utworzenie pytania dla kaŻdego z nich
    for question_number in range(50):

        #right and wrong answers
        correct_answer = capitals[states[question_number]]
        wrong_answer = list(capitals.values())
        del wrong_answer[wrong_answer.index(correct_answer)]
        wrong_answer = random.sample(wrong_answer, 3)
        answeer_options = wrong_answer + [correct_answer]
        random.shuffle(answeer_options)

        # zapis pytan i odpowiedzi w pliku
        quiz_file.write('%s. Co jest stolicą stanu $s?\n' % (question_number +1, states[question_number]))
        for i in range(4):
            quiz_file.write('  %s. %s\n' % ('ABCD'[i], answeer_options[i]))
            quiz_file.write('\n')

        # zapis odpowiedzi w pliku
        answer_key.write('%s. %s\n' % question_number + 1, 'ABCD'[answeer_options.index(correct_answer)])
        quiz_file.close()
        answer_key.close()
