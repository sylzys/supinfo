import logging
import http.client, urllib
import requests
import json, joblib, os
import azure.functions as func



##### FETCHING RECOMMANDATIONS FROM AZURE INFERENCE ####

def get_recos(userId):
    data = {
        "userId": userId
    }

    # body = json.dumps(data)
    logging.info("body")
    logging.info(data)
    url = 'http://539d067e-e78e-46cc-863d-e251bf8177c7.francecentral.azurecontainer.io/score'
    api_key = '' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json'}


    try:

        resp = requests.get(url, params=data, headers=headers)
        return resp.json()

    except:
        logging.info("The request failed with status code: " )
        
def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('Python HTTP trigger function processed a request.')
    mode = req.params.get('mode')
    userId = req.params.get('userId')
    
    ##### FETCHING POST PARAMETERS IF NEEDED ####
    if not mode:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            mode = req_body.get('mode')
    if not userId:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            userId = req_body.get('userId')

    if userId:
        resp = get_recos(userId)
        return func.HttpResponse(resp)
    else:
        
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
