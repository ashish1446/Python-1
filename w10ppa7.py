# -*- coding: utf-8 -*-
"""w10ppa7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x7_M042zwV55DlTaoCavvHK0c0t9-2UP
"""

class Question:
    '''
    Question is a class that is defined in the prefix code.
    Define a class named NAT that is a sub-class of Question with the following specification:
    Attributes
    Only those attributes that are specific to the derived class are mentioned below. 
    The rest have to be inherited from the base class.

    answer: int, numerical answer for this question
    Methods
    Only those methods that are specific to the derived class are mentioned below. 
    The rest have to be inherited from the base class.

    (1) __init__: Accept the arguments statement, marks and answer.
    Call the constructor of the base class with the first two arguments,
    and assign answer to the corresponding attribute of the derived class.
    (2) update_answer: Accept an argument named answer and update the corresponding attribute of the class with this new answer.
    '''
    
    def __init__(self, statement, marks):
        self.statement = statement
        self.marks = marks

    def print_question(self):
        print(self.statement)

    def update_marks(self, marks):
        self.marks = marks

class NAT(Question):
    def __init__(self,statement,marks,answer):
        super().__init__(statement,marks)
        self.answer = answer

    def update_answer(self,other):
        self.answer = other
