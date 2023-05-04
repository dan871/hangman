import random
MAX_TRIES = 6
HANGMAN_PHOTOS = {1: """    x-------x""", 2:"""   x-------x
    |
    |
    |
    |
    |""", 3: """    x-------x
    |       |
    |       0
    |
    |
    |""", 4: """    x-------x
    |       |
    |       0
    |       |
    |
    |""", 5:  """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""",7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}
HANGMAN_ASCII_ART = """Welcome to the game hangman
         _    _                                         
        | |  | |                                        
        | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
        |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | |  | | (_| | | | | (_| | | | | | | (_| | | | |
        |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                             __/ |                      
                            |___/
        """ 



def check_valid_input(letter_guessed, old_letters_guessed):
        """פונקציה שמימשתם בסוף היחידה בנושא רשימות.
להזכירכם, זאת פונקציה בוליאנית שמקבלת תו ורשימת אותיות שהמשתמש ניחש בעבר. הפונקציה בודקת שני דברים: את תקינות הקלט והאם חוקי לנחש אות זו (כלומר, השחקן לא ניחש אות זו בעבר) ומחזירה אמת או שקר בהתאם."""      
        char_len = len(letter_guessed)

        if(char_len > 1 or letter_guessed.isalpha() == False or (letter_guessed.isalpha()== False and char_len > 1)):
                print("you have entered a wrong column ")
                return False
        if(letter_guessed.lower() in old_letters_guessed):
                return False

        else: return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
        """פונקציה שמימשתם בסוף היחידה בנושא רשימות.
להזכירכם, הפונקציה משתמשת בפונקציה check_valid_input כדי לדעת אם התו תקין ולא ניחשו אותו בעבר או התו אינו תקין ו/או נמצא כבר ברשימת הניחושים.
אם התו איננו תקין או שכבר ניחשו את התו בעבר, הפונקציה מדפיסה את התו X (כאות גדולה), מתחתיו את רשימת האותיות שכבר נוחשו ומחזירה שקר. אם התו תקין ולא ניחשו אותו בעבר - הפונקציה מוסיפה את התו לרשימת הניחושים ומחזירה אמת."""
        update = check_valid_input(letter_guessed, old_letters_guessed)
        if(update == True):
                old_letters_guessed.append(letter_guessed.lower())
                return True
        else:
                print("X")
                print(" -> ".join(sorted(old_letters_guessed)))
                return False
                
             
def show_hidden_word(secret_word, old_letters_guessed):
        """פונקציה שמימשתם בסוף היחידה בנושא לולאות.
להזכירכם, זאת פונקציה שמחזירה מחרוזת אשר מורכבת מאותיות ומקווים תחתונים. המחרוזת מציגה את האותיות מתוך הרשימה old_letters_guessed שנמצאות במחרוזת secret_word במיקומן המתאים, ואת שאר האותיות במחרוזת (אותן השחקן טרם ניחש) כקווים תחתונים."""
        guess_len = len(secret_word)
        x = len(old_letters_guessed) - 1
        tmp = ['_ ']*guess_len
        while(x != -1):
                for num in range(0,guess_len,1):
                        
                        if(tmp[num] == '_ '):
                                
                                if(old_letters_guessed[x] == secret_word[num]):
                                
                                        tmp[num] = old_letters_guessed[x]
                                else: tmp[num] = '_ '
                x -= 1     
                
        return " ".join(tmp)

def check_win(secret_word, old_letters_guessed):
        """פונקציה שמימשתם בסוף היחידה בנושא לולאות.
להזכירכם, זאת פונקציה בוליאנית שמחזירה אמת אם כל האותיות שמרכיבות את המילה הסודית נכללות ברשימת האותיות שהמשתמש ניחש. אחרת, הפונקציה מחזירה שקר."""
        tmp = show_hidden_word(secret_word, old_letters_guessed)
        count = tmp.count('_ ')
        if(count > 0):
                return False
        else: return True

def print_hangman(num_of_tries):
        """מדפיסה את המצב הנוכחי של האיש תלוי"""
        return HANGMAN_PHOTOS[num_of_tries]



def choose_word(file_path, index):
        """פונקציה שמימשתם בסוף היחידה בנושא קבצים.
להזכירכם, הפונקציה מקבלת כפרמטרים: מחרוזת המייצגת נתיב לקובץ טקסט המכיל מילים מופרדות ברווחים, ומספר שלם המייצג מיקום של מילה מסוימת בקובץ.
הפונקציה מחזירה טאפל המורכב משני איברים בסדר הבא: (1) מספר המילים השונות בקובץ (2) מילה במיקום שהתקבל כארגומנט לפונקציה (index).
מומלץ לשנות את ערכי החזרת הפונקציה, כך שתחזיר רק ערך אחד: את המילה במיקום index, שתשמש בתור המילה הסודית לניחוש."""
        with open("chat.txt") as file_path:
                words = file_path.readlines()[0].split()
                return (len(list(dict.fromkeys(words))),words[index%len(words)-1])

                
def main():
        print(HANGMAN_ASCII_ART,MAX_TRIES)
        num_try = 1
        old_letters = []
        file_name = input("pls enter the file name you want to take a word from ")
        index_word = int(input("pls enter an index for the word you want to pick from the file to play with "))
        different_words, guess_index = choose_word(file_name,index_word)   
        print("    " + show_hidden_word(guess_index,old_letters))
        print("\n" + print_hangman(num_try))
        while(check_win(guess_index,old_letters) != True):
                guess_char = input("pls enter a char that you want to cheack if it is in the word ")
                if(try_update_letter_guessed(guess_char,old_letters) == True):
                        if(guess_char not in show_hidden_word(guess_index,old_letters)):
                                num_try += 1
                print("    " + show_hidden_word(guess_index,old_letters))
                if(num_try == 7):
                        print(print_hangman(num_try))
                        print("\n the game is over, you lost :( ")
                        break

                print("\n" + print_hangman(num_try))
                print(old_letters)
        
        if(num_try != 7):
                print("\n congrats! you have won the game :) ")

       

main()
