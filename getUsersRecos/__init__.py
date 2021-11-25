import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, doc:func.DocumentList) -> func.HttpResponse:
    
    logging.info('Python HTTP trigger function processed a request.')
  
    users_json = []

    for user in doc:
        user_json = {
           "id": user['id'],
           "items": user['items']
        }
        users_json.append(user_json)
    print("json", user_json)
    return func.HttpResponse(

            json.dumps(users_json[0:5]),
            status_code=200,
            mimetype="application/json"            
    )