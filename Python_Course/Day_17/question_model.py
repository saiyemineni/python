class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


new_question = Question("What is question?", "True")
print(new_question.text)
print(new_question.answer)
