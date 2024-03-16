from mycroft import MycroftSkill, intent_file_handler


class OllamaFallback(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fallback.ollama.intent')
    def handle_fallback_ollama(self, message):
        self.speak_dialog('fallback.ollama')


def create_skill():
    return OllamaFallback()

