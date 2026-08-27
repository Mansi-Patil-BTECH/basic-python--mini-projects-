#typing speed tester
import time #time module is imported to calculate the time taken by the user to type the given text
import random 

sentences = ["Python is a programming language",
"it is easy to read and understand",
"it is used for mainly everything like web development, data science etc.",]

def measure_accuracy(user_input, test_sentence):
    correct_chars = sum(1 for a, b in zip(user_input, test_sentence) if a == b)
    accuracy = (correct_chars / len(test_sentence)) * 100
    return accuracy

def typing_test():
    test_sentence = random.choice(sentences)
    print("Type as faster as you can")
    print("----------------------------------------")
    print(test_sentence)
    print("----------------------------------------")
    input("press enter when you are ready!")
    print("----------------------------------------")
    start_time= time.time() #will measure the time taken
    user_input = input ("\n Start typing: \n")
    print("----------------------------------------")
    end_time = time.time() #records the time taken
    time_taken = end_time - start_time 
    word_count = len (test_sentence.split(" "))
    accuracy = measure_accuracy(user_input, test_sentence)

    print("Result : ")
    print (f"Time taken: {time_taken} seconds")
    print(f"Words typed: {word_count}")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Typing speed: {word_count / (time_taken /60):.2f} words per minute")

typing_test()
