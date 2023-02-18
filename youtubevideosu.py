# class Person:
#     def __init__(self,name,year):
#         self.name = name
#         self.year = year
#         print('calisti')


#     def intro(self):
#         print('hello there.i am' + self.name)
        

# p1 = Person(name = 'ucal',year = 1994)
# print(p1.intro())

# p2 = Person(name = 'eflatun',year = 5555555555)
# print(p2.intro())
 


# class Cirkle:
#     pi = 3.14
#     def __init__(self,yaricap = 1):
#         self.yaricap = yaricap

#     def cevre_hesapla(self):
#         return 2 * self.pi + self.yaricap 

#     def alanhesapla(self):
#         return self.pi * (self.yaricap ** 2)   
    
# c1 = Cirkle(5)
# print(f'cevrenin hesabi {c1.cevre_hesapla()} ve cevrenin alani {c1.alanhesapla()}')    


# class Person():
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#         print('adam yaradildi')
#     def who_am_i(self):
#         pass    


# class Student(Person):
#     def __init__(self,fname,lname):
#         Person.__init__(self,fname,lname)
#         print('student create')

# s1 = Student('arif','sahbazov')
# print(s1.fname,s1.lname)       
# **********************************************************************************
#Question
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def chekAnswer(self,answer):
        return self.answer == answer    
# q1 = Question('en yaxsi programlama dili hansidir?',['phyton','javascript','c#','java'],'phyton')    
# q2 = Question('en mehsur programlama dili hansidir?',['javascript','c#','phyton','java'],'phyton')    
# q3 = Question('en cok qazandiran programlama dili hansidir?',['phyton','c#','javascript','java'],'phyton')  
# print(q1.chekAnswer('phyton'))
# 
#   
#quiz
# lst = [q1,q2,q3]
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionindex = 2
    def getQuestion(self):
        return  self.questions[self.questionindex]
    def displayQuestion(self):
        question = self.getQuestion()   
        print(f'Soru {self.questionindex + 1}: {question.text }')


        for q in question.choices:
            print('-' +  q)


        answer = input('cavab:  ') 
        print(question.chekAnswer(answer))
  



q1 = Question('en yaxsi programlama dili hansidir?',['phyton','javascript','c#','java'],'phyton')    
q2 = Question('en mehsur programlama dili hansidir?',['javascript','c#','phyton','java'],'phyton')    
q3 = Question('en cok qazandiran programlama dili hansidir?',['phyton','c#','javascript','java'],'phyton')  

questions = [q1,q2,q3]


quiz = Quiz(questions)
question = quiz.getQuestion()
# print(question.text)
quiz.displayQuestion()

 
    


