import logging
import json
import azure.functions as func

def extract_palyndromes(text:str):
    
    palyndromes = []

    text = text.lower()
 
    for token in text.split():
        token = token.lower()
        token = ''.join(filter(str.isalnum,token))
        if is_palyndrome(token):
            palyndromes.append(token)

    return list(set(palyndromes))


def is_palyndrome(token:str) -> bool:

    if token is None or len(token) <=1:
        return False

    i = 0
    j = len(token)-1

    while(i<j):
        if token[i] != token[j]:
            return False
        i+=1
        j-=1
    return True

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        request_json = req.get_json()
        return_values =[]
        
        for value in request_json.get("values",[]):
            recordId = value.get('recordId')
            data = value.get('data')

            palyndromes = extract_palyndromes(data.get("title")+" "+data.get("abstract"))

            return_value = {
                "recordId":recordId,
                "data":{
                    "palyndromes": palyndromes
                }
            }

            return_values.append(return_value)

        response = {
            "values":return_values
        }

        return func.HttpResponse(json.dumps(response),headers={"Content-Type":"application/json"})

    except ValueError:
        return func.HttpResponse("Invalid body",status_code=400)