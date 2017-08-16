import fresh_tomatoes
import media

# create instance of class Movie with required input: 1) movie name, 2) movie poster, 3) trailer url

inception = media.Movie('Inception',
                        'http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-4.jpg',
                        'https://www.youtube.com/watch?v=YoHD9XEInc0')

prestige = media.Movie('Prestige',
                        'https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg',
                        'https://www.youtube.com/watch?v=o4gHCmTQDVI')

sicario = media.Movie('Sicario',
                        'https://upload.wikimedia.org/wikipedia/en/4/4b/Sicario_poster.jpg',
                        'https://www.youtube.com/watch?v=G8tlEcnrGnU')

the_dark_knight = media.Movie('The Dark Knight',
                        'https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg',
                        'https://www.youtube.com/watch?v=EXeTwQWrcwY')

the_illusionist = media.Movie('The Illusionist',
                        'https://upload.wikimedia.org/wikipedia/en/6/6a/The_Illusionist_Poster.jpg',
                        'https://www.youtube.com/watch?v=i0xO64icGSY')

there_will_be_blood = media.Movie('There will be blood',
                     'http://www.gstatic.com/tv/thumb/movieposters/171565/p171565_p_v8_af.jpg',
                     'https://www.youtube.com/watch?v=FeSLPELpMeM')


# create list of instances of the class Movie created above
# this list is used as input for freshtomatoes.open_movies_page() function
movies = [inception, prestige, sicario, the_dark_knight, the_illusionist, there_will_be_blood]
fresh_tomatoes.open_movies_page(movies)

