from flask import request
from flask_restx import Resource, Namespace
from container import movie_service
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):

        movies = movie_service.get_all()

        return movies_schema.dump(movies), 200

    def post(self):
        req_json = request.json
        created_movie = movie_service.create(req_json)

        if created_movie:
            return "", 201, {"location": f"/movies/{created_movie.id}"}
        else:
            return "Failed to create movie", 500


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):

        movie = movie_service.get_one(mid)

        return movie_schema.dump(movie), 200

    def put(self, mid):

        req_json = request.json
        req_json["id"] = mid

        movie_service.update(mid, req_json)

        return "", 204

    def patch(self, mid):

        req_json = request.json
        req_json["id"] = mid

        movie_service.update_partial(mid, req_json)

        return "", 204

    def delete(self, mid: int):

        movie_service.delete(mid)

        return "", 204
