class Movie:
    def __init__(self, title, duration, rating, seats):
        self.title = title
        self.duration = duration
        self.rating = rating
        self.available_seats = seats
    
    def __str__(self):
        return f"{self.title} | {self.duration} min | Rated: {self.rating} | Seats left: {self.available_seats}"
    

class Booking:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def view_movies(self):
        if not self.movies:
            print("No movies available.")
        else:
            for i, movie in enumerate(self.movies):
                print(f"{i + 1}. {movie}")

    def book_ticket(self, index, tickets = 1):
        if 0 <= index < len(self.movies):
            movie = self.movies[index]
            if movie.available_seats >= tickets:
                movie.available_seats -= tickets
                print(f"Booked {tickets} ticket(s) for '{movie.title}'.")
            else:
                print("Not enough seats available.")
        else:
            print('Invalid Selcetion')

# Sample usage
booking_system = Booking()

# Add some movies
booking_system.add_movie(Movie("Inception", 148, "PG-13", 50))
booking_system.add_movie(Movie("Avengers: Endgame", 181, "PG-13", 100))
booking_system.add_movie(Movie("Coco", 105, "PG", 20))

# View movies
booking_system.view_movies()

# Book a ticket (e.g., 1st movie, 2 tickets)
booking_system.book_ticket(0, 2)

# Check again
booking_system.view_movies()