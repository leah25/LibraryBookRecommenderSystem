import redis
from django.conf import settings
from .models import Book

r = redis.StrictRedis(host=settings.REDIS_HOST,
                       port=settings.REDIS_PORT,
                       db=settings.REDIS_DB)
class Recommender(object):
    def get_book_key(self, id):
        return 'book:{}:purchased_with'.format(id)
    def books_bought(self, books):
        book_ids = [p.id for p in books]
        for book_id in book_ids:
            for with_id in book_ids:
                    if book_id != with_id:
                           r.zincrby(self.get_book_key(book_id),
                                     with_id,
                                     amount=1)