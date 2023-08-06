import argparse
from cs200.scraper import get_url
from cs200.summarizer import analyze_data

class Default_CLI:

    def __init__(self):

        parser = argparse.ArgumentParser()

        parser.add_argument("--c", "--concept", help="The concept to simplify", type=str)
        parser.add_argument("--l", "--limit", help="The amount of results to be returned", type=int, default=5)

        args = parser.parse_args()

        self.concept = args.c
        self.limit = args.l


    def return_summarization(self):

        # Obtain text from wikipedia page.
        try:
            res = get_url(self.concept)
        # Apply regex to response text.
            resCompiled = analyze_data(self.concept, res)
            return resCompiled[:self.limit]
    
        except Exception as e:
            return "REQUEST ERROR"        
    
    
