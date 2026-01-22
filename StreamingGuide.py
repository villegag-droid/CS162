# Author: Gerardo Villegas
# GitHub username: villegag-droid
# Date: Oct 15th, 2025
# Description: Defines Movie, StreamingService, and StreamingGuide classes to manage movies and also searches for them on each service.

class Movie:
    # Represents a movie with a title, genre, director, and year.

    def __init__(self, title, genre, director, year):
        self._title = title
        self._genre = genre
        self._director = director
        self._year = int(year)

    def get_title(self):
        return self._title
    
    def get_genre(self):
        return self._genre
    
    def get_director(self):
        return self._director
    
    def get_year(self):
        return self._year
    
    def __str__(self):
        # Return a readable string representation of the movie.(so i could make sure everything was right)
        return f"\n{self._title}, {self._genre}, {self._director}, {self._year}"


class StreamingService:
    # Represents a streaming service with a catalog of movies.

    def __init__(self, name):
        self._name = name
        self._catalog = []

    def get_name(self):
        return self._name
    
    def get_catalog(self):
        return self._catalog

    def add_movie(self, movie):
        # Add a movie to the catalog if not already present.
        if movie not in self._catalog:
            self._catalog.append(movie)
        print(f"\n{movie.get_title()} added to list")

    def delete_movie(self, title):
        # Remove a movie from the catalog by title.
        for movie in self._catalog:
            if movie.get_title() == title:
                self._catalog.remove(movie)
                print(f"\n{title} removed from catalog.\n")

    def __str__(self):
        # Return a readable string of the service name and its movies.
        movie_list = [str(movie) for movie in self._catalog]
        movie_str = "\n".join(movie_list)
        return f"\n{self._name}, {movie_str}"


class StreamingGuide:
    # Represents a guide of multiple streaming services.

    def __init__(self):
        self._streams = []

    def add_streaming_service(self, service):
        self._streams.append(service)

    def delete_streaming_service(self, name):
        for service in self._streams:
            if service.get_name() == name:
                self._streams.remove(service)
                print(f"\n{name} removed from guide.\n")

    def who_streams_this_movie(self, title):
        # Return a dictionary containing the title, year, and list of services 
        # that stream the given movie. Returns None if the movie is not found.
        stream_sites = []
        movie_year = None

        for service in self._streams:
            for movie in service.get_catalog():
                if movie.get_title() == title:
                    stream_sites.append(service.get_name())
                    movie_year = movie.get_year()

        if stream_sites:
            return {
                "title": title,
                "year": movie_year,
                "services": stream_sites
            }
        else:
            return None
        

