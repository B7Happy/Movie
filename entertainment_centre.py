import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=Bj4gS1JQzjk")

#print(toy_story.storyline)

avatar = media.Movie("Avatar","A marine on an alien planete","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=d1_JBMrrYw8")

#print(avatar.storyline)
#avatar.show_trailer()

theri = media.Movie("Theri", "Theri is a 2016 Indian Tamil-language action drama film written and directed by Atlee","https://upload.wikimedia.org/wikipedia/en/d/db/Theri_poster.jpg","https://www.youtube.com/watch?v=ZK4uGLpkAKk")
#theri.show_trailer()

ratatouille = media.Movie("Ratatouille","A rat is a chef in Paris","https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg","https://www.youtube.com/watch?v=0IAI-iTKobY")

movies = [toy_story, avatar, theri, ratatouille]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)

