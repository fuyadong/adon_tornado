# -*- coding: utf-8 -*-

import tornado
import textwrap
import random


class WidgetHandler(tornado.web.RequestHandler):
    def get(self, widget_id):
        self.write(widget_id+' ,from get method!')

    # curl http://localhost:8000/widget/10 -d wid=2
    def post(self, *args, **kwargs):
        widget_id = self.get_argument('wid', 1)
        # widget_id = args[0]
        self.write(widget_id + ' ,from post method')


class ReverseHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print("args={0}".format(args))
        self.write(args[0][::-1])


class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ", friendly user!")

    def write_error(self, status_code, **kwargs):
        self.write("Gosh! You caused a %d error." % status_code)


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html', page_title="Burt's Books", header_text="Books")


class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb, difference=noun3)


class GetBooksHandler(tornado.web.RequestHandler):
    def get(self):
        # books = ["Python Learning", "Learning Machine", "Restful Web Services"]
        # self.render('book.html', title="We Book", header="Books that are great",
        #             books=books)
        books = []
        data = self.application.db.test_collection.find()
        for book in data:
            if book.get('isbn'):
                books.append(book)
        self.render(
            "recommended.html",
            page_title="Burt's Books | Recommended Reading",
            header_text="header text",
            books=books
        )


class BookEditHandler(tornado.web.RequestHandler):
    def get(self, isbn=None):
        print(">>>isbn:{0}".format(isbn))
        book = dict()
        if isbn:
            coll = self.application.db.test_collection
            book = coll.find_one({'isbn': isbn})
        self.render(
            "book_edit.html",
            page_title="Burt's Books",
            header_text="Edit book",
            book=book
        )

    def post(self, *args, **kwargs):
        import time
        isbn = self.get_argument("isbn")

        book_fields = ['date_released', 'isbn', 'description', 'title', 'image', 'author', 'subtitle']
        book = dict()
        coll = self.application.db.test_collection
        if isbn:
            book = coll.find_one({'isbn': isbn})
        for key in book_fields:
            book[key] = self.get_argument(key, None)
        if isbn:
            coll.save(book)
        else:
            book['date_added'] = int(time.time())
            coll.insert(book)
        self.redirect('/books')


class AlphaMge(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('alpha_mge_index.html')

    @staticmethod
    def alpha(text):
        mapped = dict()
        for line in text.split('\r\n'):
            for word in [x for x in line.split(' ') if len(x) > 0]:
                if word[0] not in mapped: mapped[word[0]] = []
                mapped[word[0]].append(word)
        return mapped

    def post(self, *args, **kwargs):
        source_text = self.get_argument('source')
        text_to_change = self.get_argument('change')
        source_map = self.alpha(source_text)
        change_lines = text_to_change.split('\r\n')
        self.render('munged.html', source_map=source_map, change_lines=change_lines, choice=random.choice)


class WordHandler(tornado.web.RequestHandler):
    def get(self, word, *args, **kwargs):
        db = self.application.db
        coll = db.test_collection
        # word_doc = coll.find({'name': word})[0]
        word_doc = coll.find_one({'name': word})
        if word_doc:
            del word_doc['_id']
            self.write(word_doc)
        else:
            self.set_status(404)
            self.write({'error': "word not found"})

    def post(self, *args, **kwargs):
        coll = self.application.db.test_collection
        word, = args
        definition = self.get_argument("definition")
        word_doc = coll.find_one({'name': word})
        if word_doc:
            word_doc['definition'] = definition
            coll.save(word_doc)
        else:
            word_doc = {'name': word, 'definition': definition}
            coll.insert(word_doc)

        del word_doc['_id']
        self.write(word_doc)
