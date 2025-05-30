from extension import db

class Book(db.Model):
    __tablename__ = 'book'
    book_number = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(225), nullable=False)
    book_author = db.Column(db.String(225), nullable=False)
    book_price = db.Column(db.Float, nullable=False)
    book_type = db.Column(db.String(225), nullable=False)
    book_publisher = db.Column(db.String(225))

    @staticmethod
    def init_db():
        rets = [
            (1,'re0 1','rem',99.9,'小说','月昴出版社'),
            (2,'re0 2','ram',99.9,'小说','月昴出版社')
        ]
        for ret in rets:
            book = Book()
            book.book_number = ret[0]
            book.book_name = ret[1]
            book.book_author = ret[2]
            book.book_price = ret[3]
            book.book_type = ret[4]
            book.book_publisher = ret[5]
            db.session.add(book)
        db.session.commit()



