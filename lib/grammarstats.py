class GrammarStats:
    def __init__(self):
        self.total_text_checked = 0
        self.passed_texts = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        result = text[0].isupper and text[-1] in ".?!"
        if result:
            self.passed_texts += 1
        self.total_text_checked += 1
        return result

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.total_text_checked == 0:
            return 0 
        return (self.passed_texts / self.total_text_checked) * 100
