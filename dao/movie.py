from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, movies_query):

        return movies_query.all()

    def get_one(self, mid):

        return self.session.query(Movie).get(mid)

    def create(self, data):
        try:
            movie = Movie(**data)
            self.session.add(movie)
            self.session.commit()
            return movie
        except Exception as e:
            print(f"Failed to create movie: {e}")
            self.session.rollback()
            return None

    def update(self, movie):

        self.session.add(movie)
        self.session.commit()

        return ""

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()

        return ""
