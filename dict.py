from difflib import get_close_matches
import mysql.connector

con = mysql.connector.connect(
    user='ardit700_student',
    password='ardit700_student',
    host='108.167.140.122',
    database='ardit700_pm1database'
)
cursor = con.cursor()
query = cursor.execute('SELECT Expression FROM Dictionary')
db = cursor.fetchall()


# Get meaning of words
def translate():
    word = input('Enter a word: ')
    cursor.execute(f'SELECT * FROM Dictionary WHERE Expression = "{word}"')
    data = cursor.fetchall()

    # checking to see is meaning for word is available
    if data:
        for meaning in data:
            print(meaning[1])
    else:
        cursor.execute('SELECT Expression FROM Dictionary')
        data = cursor.fetchall()
        words = []
        for wrd in data:
            words.append(wrd[0])
        similar = get_close_matches(word, words, cutoff=0.8)
        if len(similar) > 0:
            while True:
                ans = input(f'do you mean \'{similar[0]}\', enter yes or no: ')
                if ans.lower() == 'yes':
                    cursor.execute(f'SELECT * FROM Dictionary WHERE Expression = "{similar[0]}"')
                    data = cursor.fetchall()
                    for meaning in data:
                        print(meaning[1])
                    break
                elif ans.lower() == 'no':
                    print('word is incorrect')
                    break

        else:
            print('word is incorrect')


translate()
