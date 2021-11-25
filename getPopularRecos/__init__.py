import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, doc:func.DocumentList) -> func.HttpResponse:
    
    logging.info('Python HTTP trigger function processed a request.')
  
    articles_json = []

    for article in doc:
        article_json = {
           "id": article['article_id']
        }
        articles_json.append(article_json)

    return func.HttpResponse(
            json.dumps(articles_json),
            status_code=200,
            mimetype="application/json"            
    )