# # string concatenation (aka how to put strings together)
# # suppose we want to craete string taht says ("subscribe to ____")

# youtuber = " Yusuf Ozen"   # some string variable


# # a few days to do this

# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("adjective : ")
verb1 = input("verb1 : ")
verb2 = input("verb2 : ")
famous_person = input("famous person : ")



madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
