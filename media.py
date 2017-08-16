import webbrowser

class Movie():
    """"The class provides a way to store movie related information"""
    # constructor for class Movie with 3 variables:
    # 1) movie_title, 2) poster_image, 3) trailer_url
    def __init__(self, movie_title, poster_image, trailer_url):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    # function for showing movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

        
