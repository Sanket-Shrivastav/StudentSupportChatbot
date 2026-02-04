def find_best_match(user_words, faq_data):
    for intent in faq_data.values():
        for keyword in intent["keywords"]:
            if keyword in user_words:
                return intent["answer"]
    return "Sorry, I couldn't understand your question. Please contact student support."
