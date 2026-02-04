import json
from chatbot.preprocess import preprocess_text
from chatbot.matcher import find_best_match

class StudentSupportChatbot:
    def __init__(self, faq_path):
        with open(faq_path, "r") as file:
            self.faq_data = json.load(file)

    def get_response(self, user_input):
        user_words = preprocess_text(user_input)
        return find_best_match(user_words, self.faq_data)
