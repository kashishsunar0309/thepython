from survey import AnonsymousSurvey
#define a question , and make a survey.
question = 'what language did you first learn to speak?'
language_survey = AnonsymousSurvey(question)
#Show the question , and store responses to the question
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)
#Show the survey results.
print("\n Thank you to everyone who participate in the survey!")
language_survey.show_results()