

import urllib.request,json

from .models import Source,Articles

api_key=None

base_url_source=None

base_url_articles=None

def configure_request(app):
    global api_key,base_url_source,base_url_articles
    api_key = app.config['NEWS_API_KEY']
    base_url_source=app.config['BASE_URL_SOURCES']
    base_url_articles=app.config['BASE_URL_ARTICLES']

def get_source():
    '''
    Function that gets the json response to our url request
    '''

    get_source_url = base_url_source.format(api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        news_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)


    return source_results


def process_results(source_list):

    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        source_object = Source(id,name,description)
        source_results.append(source_object)
    return source_results
def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''

 
    get_articles_url = base_url_articles.format(id,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_article_results(articles_results_list)
           
    return articles_results

