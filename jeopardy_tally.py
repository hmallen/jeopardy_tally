import datetime
import logging
import sys

logging.basicConfig(level=logging.DEBUG)
#logging.setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)

total_questions = 61


def print_help():
    print('Type \'y\' for a correct answer.')
    print('Type \'n\' for an incorrect answer.')
    print('Type \'r\' to remove the previous answer.')
    print('Type \'d\' for a Double Jeopardy answer, then \'y\' or \'n\' as usual.')
    print('Type \'q\' when done with game. Results will be logged to file.')
    print()
    print('Type \'h\' to see this help menu.')
    print()


def quit_game(correct, incorrect, dj):
    tally_file = datetime.datetime.now().strftime('%m%d%Y') + '.txt'
    
    percentage_correct = correct / (correct + incorrect)

    missed_questions = total_questions - (correct + incorrect)
    
    tally = str(correct) + ', ' + str(incorrect) + ', ' + str(dj) + ', ' + str(percentage_correct) + ', ' + str(missed_questions)

    with open(tally_file, 'w') as file:
        file.write('Correct, Incorrect, Double Jeopardy Correct, Percentage Correct, Missed Questions')
        file.write(tally + '\n')


if __name__ == '__main__':
    try:
        print_help()
        print('Press any key when ready..')
        start_input = input()
        print('Beginning game. Ready for answer input.')
        print()
        
        correct_count = 0
        incorrect_count = 0
        dj_count = 0
        while (True):
            dj_added = False
            
            response = input('Answer (y/n) [r/d/q/h]: ')
            print()

            if response == 'y':
                correct_count += 1
            elif response == 'n':
                incorrect_count += 1
            elif response == 'd':
                print('Double jeopardy!')
                dj_response = input('Answer: ')
                if dj_response == 'y':
                    correct_count += 1
                    dj_count += 1
                    dj_added = True
                elif dj_response == 'n':
                    incorrect_count += 1
            elif response == 'r':
                if response_last['response'] == 'y':
                    correct_count -= 1
                    if response_last['dj'] == True:
                        dj_count -= 1
                elif response_last == 'n':
                    incorrect_count -= 1
            elif response == 'h':
                print_help()
            elif response == 'q':
                quit_game(correct_count, incorrect_count, dj_count)
                break

            response_last = {'response': response, 'dj': dj_added}

            print('Correct: ', correct_count)
            print('Incorrect: ', incorrect_count)
            print('Double Jeopardy Correct: ', dj_count)
            print()

        print('Good game!')
        print()

    except Exception:
        logger.exception('Exception raised.')
        logger.exception(e)

    except KeyboardInterrupt:
        logger.info('Exit signal received.')
        sys.exit()
