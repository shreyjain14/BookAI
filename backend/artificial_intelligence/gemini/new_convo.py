from backend.artificial_intelligence.gemini.gemini_api import model


def new_convo():
    return model.start_chat(history=[])

