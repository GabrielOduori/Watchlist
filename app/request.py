from app import app
import urllib.request, json
from models import movie

Movie = movie.Movie

# Getting the API key

api_key = app.config['MOVIE_API_KEY']

# Getting the movie base URL
base_url = app.config['MOVIE_API_BASE_URL']
# base_url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

def get_movies(category):
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        # movie_results = None
        movie_results = []

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)


    return movie_results


def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)
    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_reponse = json.loads(movie_details_data)
        
        movie_object = None
        
        if movie_details_reponse:
            id = movie_details_reponse.get('id')
            title = movie_details_reponse.get('original_title')
            overview = movie_details_reponse.get('overview')
            poster = movie_details_reponse.get('poster_path')
            vote_average  = movie_details_reponse.get('vote_average')
            vote_count = movie_details_reponse.get('vote_count')
            movie_object = Movie(id,title,overview,poster, vote_average,vote_count)
            
    return movie_object
        
        
        
def process_results(movie_list):
    """
    Function that processes the movie result and 
    transforms them into a list of objects
    Args:
        movie_list:A list of dictionaries that contain movie details
    Return:
        movie_results: A list of movie objects
    """
    movie_results = []
    
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')
        
        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            # movie_object = Movie()
            movie_results.append(movie_object)
 
    return movie_results