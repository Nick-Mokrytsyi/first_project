""" Дана строка (большАя строка, лучше взять на английском).
    Выведите слово, которое в этой строке встречается чаще всего.
    Если таких слов несколько, выведите последнее.
    Задачу необходимо решить с использованием словаря.
"""
import re as filter
import pprint as pp

my_string = "OM: Fundamentally, CrossFit is a GPP program: “general physical preparedness”. " \
            "What that means is we specialise in not specialising." \
            " No aspect of fitness is more important than another in CrossFit." \
            " Some people want to be Mo Farah, arguably one of the greatest runners in the world, " \
            "or they might want to be a strongman: big and strong but gets out of breath just running to their car." \
            " We want to meet in the middle, where you have aerobic capacity, strength, flexibility." \
            " When we’re designing workouts it can be anything: 5K run, 10K run, a deadlift, " \
            "a combination of all those things into one workout. Any combination you can come up with," \
            " we want to explore that. Zack will find this at The CrossFit Games: if you think you’ve figured " \
            "out what CrossFit is, Dave Castro – who designs the workouts for the Games – will come up with something" \
            "unique you’d never thought of. Nothing’s off the table. That’s what makes our sport unique. You have " \
            "to be good at so many different aspects of fitness. If you’re a 100 metres athlete you know your " \
            "discipline is the 100 metres sprint. With CrossFit you can turn up to competition and be confronted " \
            "with something you’ve never tried or experienced before and we’ve got to learn on the fly and get used " \
            "to the movement. That happens at the Games quite often, but because athletes are so well-rounded and " \
            "experienced in different areas of fitness they can basically do it on the spot and crack on." \
            " "

my_string_1 = "Apple, orange, banana, kiwi, watermelon2, strawberry, cherry, lime, lemon, avocado " \
              "Avocado, orange, mango, mAngo, Mango, kiwi, apple, banana 1saf 124 @#@"

filtered_my_string = filter.sub("[^A-Za-z]", " ",
                                my_string).lower()  # Delete all punctuation and numbers from the text/string;
my_dict = {}
for word in filtered_my_string.split():  # Split the string to words;
    if my_dict.get(word, None):
        my_dict[word] += 1
    else:
        my_dict[word] = 1
max_count = max(my_dict, key=my_dict.get)
pp.pprint(my_dict)
print(f'The most common repeat in the  text is the word --> {max_count}:{my_dict[max_count]} times;')

