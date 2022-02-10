from project.dao.base import BaseDAO


class GenreDAO(BaseDAO):
    def __init__(self, session, module):
        super().__init__(session, module)
        self.session = session
        self.module = module
        self.message = "жанр"
