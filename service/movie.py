from flask import request
from dao.model.movie import Movie
from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        movies_query = Movie.query
        args = request.args

        director_id = args.get("director_id")
        if director_id is not None:
            movies_query = movies_query.filter(Movie.director_id == director_id)

        genre_id = args.get("genre_id")
        if genre_id is not None:
            movies_query = movies_query.filter(Movie.genre_id == genre_id)

        year = args.get("year")
        if year is not None:
            movies_query = movies_query.filter(Movie.year == year)

        return self.dao.get_all(movies_query)

    def create(self, data):
        created_movie = self.dao.create(data)
        if created_movie:
            return created_movie
        else:
            return None

    def update(self, mid, data):
        movie = self.get_one(mid)

        fields_to_update = ["title", "description", "trailer", "year", "rating"]
        for field in fields_to_update:
            setattr(movie, field, data.get(field))

        return self.dao.update(movie)

    def update_partial(self, mid, data):
        movie = self.get_one(mid)

        fields_to_update = ["title", "description", "trailer", "year", "rating"]
        for field in fields_to_update:
            if field in data:
                setattr(movie, field, data.get(field))

        return self.dao.update(movie)

    def delete(self, mid):
        return self.dao.delete(mid)
