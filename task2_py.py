#task 1.1.2
def double_letter(my_str):
    return ''.join([char*2 for char in my_str])
#print(double_letter("works"))

#task1.1.3
def four_dividers(number):
    return ', '.join([str(x) for x in range(1, number + 1) if x % 4 == 0])

#print(four_dividers(9))

#task1.3.1
def intersection(list_1, list_2):
    return [x for x in list_1 if x in list_2]

#print(intersection([1, 2, 3, 4], [8, 3, 9]))


#task 2.2.2
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def birthday(self):
        self.age += 1
    
    def get_age(self):
        return self.age
    
dog1 = Dog("mufasa",3)
dog1.birthday()
dog2 = Dog("humus",6)
#print(dog1.get_age())
#print(dog2.get_age())

#task2.3.3
class Dog_2:
    count_animals = 0

    def __init__(self, name="Dogo", age=0):
        self._name = name
        self._age = age
        Dog_2.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name
    
dog3 = Dog_2("momo",5)
dog4 = Dog_2()
#print(dog3.get_name())
#print(dog4.get_name())
dog4.set_name("huwan")
#print(dog4.get_name())
#print(Dog_2.count_animals)



#task 4.1.2
def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    
    translated_words = (words.get(word, word) for word in sentence.split())
    translated_sentence = ' '.join(translated_words)
    
    return translated_sentence

#print(translate("el gato esta en la casa"))

#task 4.2.2
def parse_ranges(ranges_string):
    ranges = (rng.split('-') for rng in ranges_string.split(','))
    numbers = (str(num) for start, end in ranges for num in range(int(start), int(end) + 1))
    return numbers

#print(list(parse_ranges("1-2,4-4,8-10")))


#task 4.3.4
def get_fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

#fibo_gen = get_fibo()
#print(next(fibo_gen))
#print(next(fibo_gen))
#print(next(fibo_gen))
#print(next(fibo_gen))

#task4.4
def gen_secs():
    sec = 0
    while True:
        yield sec
        sec = (sec + 1) % 60


def gen_minutes():
    minute = 0
    while True:
        yield minute
        minute = (minute + 1) % 60


def gen_hours():
    hour = 0
    while True:
        yield hour
        hour = (hour + 1) % 24


def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)
                if sec == 59:
                    break
            if minute == 59:
                break
        if hour == 23:
            break


def gen_years(start=2023):
    year = start
    while True:
        yield year
        year += 1


def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    days_in_month = {
        1: 31,
        2: 29 if leap_year else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    days = days_in_month[month]
    day = 1
    while day <= days:
        yield day
        day += 1


def gen_date():
    for year in gen_years():
        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, time)



# date_gen = gen_date()
# for i in range(1, 10000000):
#     date = next(date_gen)
#     if i % 1000000 == 0:
#             print(date)


#task5.1.2
import winsound

freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }
notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
for note in notes.split("-"):
    frequency = freqs[note.split(",")[0]]
    duration = int(note.split(",")[1])
    #winsound.Beep(frequency, duration)

#task5.2.2

# numbers = iter(list(range(1, 101)))
# for i in numbers:
#     print(i)
#     next(numbers)
#     next(numbers)

#task5.2.3
from itertools import combinations

bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
target_amount = 100

valid_combinations = []
for r in range(1, len(bills) + 1):
    for combination in combinations(bills, r):
        if sum(combination) == target_amount:
            sorted_combination = sorted(combination, reverse=True)
            if sorted_combination not in valid_combinations:
                valid_combinations.append(sorted_combination)

# for combination in valid_combinations:
#     print(combination)

#task5.3.2
class MusicNotes:
    def __init__(self):
        self.notes = [
            [55, 110, 220, 440, 880],
            [61.74, 123.48, 246.96, 493.92, 987.84],
            [65.41, 130.82, 261.64, 523.28, 1046.56],
            [73.42, 146.84, 293.68, 587.36, 1174.72],
            [82.41, 164.82, 329.64, 659.28, 1318.56],
            [87.31, 174.62, 349.24, 698.48, 1396.96],
            [98, 196, 392, 784, 1568]
        ]
        self.current_octave = 0
        self.current_note = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_octave >= len(self.notes[0]):
            raise StopIteration

        frequency = self.notes[self.current_note][self.current_octave]
        self.current_note += 1

        if self.current_note >= len(self.notes):
            self.current_note = 0
            self.current_octave += 1

        return frequency


notes = MusicNotes()
# for frequency in notes:
#     print(frequency)
