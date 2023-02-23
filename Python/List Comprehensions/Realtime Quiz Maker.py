answers = ["C", "B", "C", "A", "D", "A", "B", "D", "D", "C"]

responses = ["C", "B", "C", "A", "D", "A", "B", "D", "D", "C"]

if responses[-1] == answers[len(responses)-1]:
    correct = True
else:
    correct = False
if not correct:
    del responses[-1]
    print("Sorry, pelase try the last question again!")


elif len(responses) < len(answers):
    print("Quiz is not complete yet.")
    correct = str(len(responses))
    print("you've got" + correct +
          "answers correct so far, pelase add an answer for the next question.")
else:
    print("Well done, you have completed the quiz!")
