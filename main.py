import pyttsx3





answer_yes = ["Yes"]
answer_no = ["No"]
answer_1 = ["Needles"]
answer_2 = ["me"]

engine = pyttsx3.init()
engine.say("""
Hello My Friend, I will offer you $1000, if you can correctly answer this three questions.
      If you answer the wrong answer i will go kill your entire family.
A old man comes up to you and asks you for money, do you give him the money(Yes/No)
""")  # write a command inside
engine.runAndWait()


ans1 = input(">>")

if ans1 in answer_yes:
    engine = pyttsx3.init()
    engine.say("\nAre you dumb?, He is clearly a theif you just lost your money and your entire family!\n")
    engine.runAndWait()
    exit()

if ans1 in answer_no:
    engine = pyttsx3.init()
    engine.say(
        "\nGood job my boy i knew you weren't dumb, You can move on two the second question, Would you let me fuck your mom\n")
    engine.runAndWait()

ans2 = input(">>")

if ans2 in answer_yes:
    engine = pyttsx3.init()
    engine.say("""
          \nGood, you can go to the last question!

           This is your last question so think hard okay?, What has eyes but cannot see?\n""")
    engine.runAndWait()

if ans2 in answer_no:
    engine =pyttsx3.init()
    engine.say("\nYa i think you know what gonna happen, Well you're dead ,Bye\n")
    engine.runAndWait()
    exit()

ans3 = input(">>")

if ans3 in answer_1:
    engine =pyttsx3.init()
    engine.say("\nCongrats bro, Here is your $1000\n")
    engine.runAndWait()

if ans3 in answer_2:
    engine =pyttsx3.init()
    engine.say("\nYou sold bruh, your family is already dead btw\n")
    engine.runAndWait()
    exit()
