from flask import render_template
from app import app
# Views

@app.route('/')
def index():
    '''
    View root page function that retruns index 
    page and its data
    '''
    
    title = 'Home - Welcome to the best movie review website online'
    # message = 'Hello World Children'
    return render_template('index.html', title=title)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    Vie movie page function returna the
    movie details page and its data
    '''
    return render_template('movie.html', id=movie_id)