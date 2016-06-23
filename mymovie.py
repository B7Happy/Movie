import media
import mmovie

theri = media.Movie("Theri", "Theri is a 2016 Indian Tamil-language action drama film written and directed by Atlee","https://upload.wikimedia.org/wikipedia/en/d/db/Theri_poster.jpg","https://www.youtube.com/watch?v=ZK4uGLpkAKk")

kabali = media.Movie("Kabali","Kabali is a upcoming Indian Tamil-language action of Superstar Rajini ","https://upload.wikimedia.org/wikipedia/en/9/9e/Rajinikanth_in_Kabali.jpg","https://www.youtube.com/watch?v=9mdJV5-eias")

thani_Oruvan = media.Movie("Thani Oruvan","Thani Oruvan is a 2015 Indian Tamil-language action drama film","https://upload.wikimedia.org/wikipedia/en/f/f1/Thani_Oruvan.jpg","https://www.youtube.com/watch?v=r5Lih8rKd6k")

premam = media.Movie("Premam","Premam is a 2015 Indian Malaylam-language romance drama film","https://upload.wikimedia.org/wikipedia/en/3/32/Premam_film_poster.jpg","https://www.youtube.com/watch?v=ethACON2IQ4")


movies = [ kabali ,theri, premam, thani_Oruvan,  ]
mmovie.open_movies_page(movies)
