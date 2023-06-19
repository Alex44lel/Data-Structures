import unittest

def can_two_movies_fill_flight(movie_lengths, flight_length):
    # Movie lengths we've seen so far
    
    movie_set = set()
    
    for movie in movie_lengths:
        appropiate_lenght = flight_length - movie
        
        if appropiate_lenght in movie_set:
            return True
        
        movie_set.add(movie)
    # We never found a match, so return False
    return False
