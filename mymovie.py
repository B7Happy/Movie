import media
import mmovie

# Class instantiating section:
theri = media.Movie("Theri",
                    "Theri is a 2016 Indian Tamil-language action drama film"
                    " written and directed by Atlee",
                    "https://upload.wikimedia.org/wikipedia/en/d/db/Theri_poster.jpg",  # noqa
                    "https://www.youtube.com/watch?v=ZK4uGLpkAKk")  # noqa

kabali = media.Movie("Kabali", "Kabali is a upcoming Indian"
                    " Tamil-language action of Superstar Rajini ",
                    "https://upload.wikimedia.org/wikipedia/en/9/9e/Rajinikanth_in_Kabali.jpg",  # noqa
                    "https://www.youtube.com/watch?v=9mdJV5-eias")   # noqa

thani_Oruvan = media.Movie("Thani Oruvan",
                            "Thani Oruvan is a 2015 Indian"
                            " Tamil-language action drama film",
                            "https://upload.wikimedia.org/wikipedia/en/f/f1/Thani_Oruvan.jpg",   # noqa
                            "https://www.youtube.com/watch?v=r5Lih8rKd6k")   # noqa

premam = media.Movie("Premam",
                     "Premam is a 2015 Indian"
                     " Malaylam-language romance drama film",
                     "https://upload.wikimedia.org/wikipedia/en/3/32/Premam_film_poster.jpg",   # noqa
                     "https://www.youtube.com/watch?v=ethACON2IQ4")   # noqa

# Appending movies into a list called movies:
movies = [kabali, theri, premam, thani_Oruvan]

# Calling the external rendering function:
mmovie.open_movies_page(movies)
