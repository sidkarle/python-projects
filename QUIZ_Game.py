from mcq import question

question_prompt=[
    "which of the following is a extension for python files?\n(a).py\n(b).et\n(c).pn\n\n ",
    "what is the output for following print(a+b)for a=2 ,b=5?\n(a)3\n(b)7\n(c)9\n\n",
    "what is list in python represented by?\n(a)()\n(b)[]\n(c){}\n\n"
]

questions=[
    question(question_prompt[0],"a"),
    question(question_prompt[1],"b"),
    question(question_prompt[2],"b"),
]
answers = ['a' , 'b' , 'b']

def run_test(questions):
    score = 0
    j = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == answers[j]:
            score += 1

        j += 1
    print("you have scored" + (str(score)) + "/" + str(len(question_prompt))+"correct")

run_test(questions)
