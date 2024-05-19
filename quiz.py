print("WELCOME TO QUIZ\n")
question = ["who is father of computer", "what operating system did google develop?", "What does the acronym VPN stand for?",
             "who founded apple computer","What does the acronym DNS stand for?",
             "What is the full form of E-Mail?","WWW stands for"]

answer = ["charles babbage", "android", "virtual private network",
           "steve jobs", "domain name system", "electronic mail", "world wide web"]



qlength=len(question)
alength=len(answer)

def startquiz(question,answer):
    score = 0
    for i in range (qlength):
        uanswer =input(question[i]+"\n your answer:").lower()
        if (uanswer == answer[i]):
         print("Correct answer\n")
         score+=1   
        else:
            print("Wrong answer")
    print("your final score is ",score)


startquiz(question,answer)     