import logging
import codecs
import azure.functions as func
from typing import List
import random
import os

DEFAULT_BAD_JOKES_FILEPATH = "BadJokeAPI/jokes.dat"

def load_jokes(path: str) -> List[str]:
    jokes = []

    with codecs.open(path,"r") as input_file:
        for line in input_file:
            jokes.append(line)

    return jokes

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    logging.info("Importing Bad Jokes")
    jokes = load_jokes(DEFAULT_BAD_JOKES_FILEPATH)
    
    logging.info("Select bad joke randomly")
    pos = random.randint(0,len(jokes))
    joke = jokes[pos]
    
    return func.HttpResponse(f"{joke}")
    
