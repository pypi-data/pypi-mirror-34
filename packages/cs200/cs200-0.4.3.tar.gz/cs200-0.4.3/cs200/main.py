import argparse
from cs200.scraper import get_url
from cs200.summarizer import analyze_data

    
class Controller:
            
    def __init__(self):
            self.headless_mode = None
        
    def return_summarization(self, **kwargs):

        # Obtain text from wikipedia page.
        try:
            if self.headless_mode:
                res = get_url(self.concept)
        # Apply regex to response text.
                resCompiled = analyze_data(self.concept, res)

        # Return the summarized text until the limit prescribed by user. 
                return resCompiled[:self.limit]

        # If arguments are not used...
            elif self.headless_mode == None:
                self.concept = kwargs.get("concept")
                self.limit = kwargs.get("limit")
                
                res = get_url(self.concept)
                 
        # Apply regex to response text.
                resCompiled = analyze_data(self.concept, res)

        # Return the summarized text until the limit prescribed by user. 
                return resCompiled[:self.limit]
    
        except Exception as e:
            return "REQUEST ERROR"        
    
    
    def init_args(self):

        self.headless_mode = True
        
        parser = argparse.ArgumentParser()

        parser.add_argument("--c", "--concept", help="The concept to simplify", type=str, default="computers")
        parser.add_argument("--l", "--limit", help="The amount of results to be returned", type=int, default=5)

        args = parser.parse_args()

        self.concept = args.c
        
        self.limit = args.l
