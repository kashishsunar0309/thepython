"""from survey import AnonsymousSurvey
def test_store_single_response():
    "Test that a single response is stored properly."
    question = "what language did you first learn to speak?"
    language_survey = AnonsymousSurvey(question)
    language_survey.store_response("English")
    assert 'English' in language_survey.responses
def test_store_three_responses():
    '''Test that three individual responses are stored properly.'''
    question = "what language did you first learn to speak?"
    language_survey = AnonsymousSurvey(question)
    responses = ["English","Spanish","Mandrain"]
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses
    """
#BELOW USING FIXTURE_TEST_PROGRAM
''''
import pytest
from survey import AnonsymousSurvey
@pytest.fixture
def language_survey():
    """a survey that will be available to all test function."""
    question = "What language did you first learn to speak?"
    language_survey = AnonsymousSurvey(question)
    return language_survey
def test_store_single_response(language_survey):
    """Test that a single response is stored propely."""
    language_survey.store_response("English")
    assert "English" in language_survey.responses
def test_store_three_response(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ["English","Spanish","Mandarin"]
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses'''