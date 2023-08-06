import argparse
from cs200.scraper import get_url
from cs200.summarizer import analyze_data

# Default outline for cs200 
def default_cli():
    
# Initialize ArgumentParser instance.
    parser = argparse.ArgumentParser()

    parser.add_argument("--c", "--concept", help="The concept to simplify", type=str)

    args = parser.parse_args()

    concept = args.c

    print(default_main(concept))

# Function with default options loaded for quickstart usage. 
def default_main(concept):
    
    req = get_url(concept)

    summarization = analyze_data(concept, req)

    return summarization[:5]

if __name__ == "__main__":
    print(main())


