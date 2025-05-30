from flask import Flask,request,render_template
from flask.views import MethodView
from extension import db
from models import Book
import config
from sqlalchemy import select
from flask_cors import CORS
import sqlite3 as sql

app = Flask(__name__)
# cors.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config.from_object(config) ##用MySQL还是sqlite需自己配置
db.init_app(app)
@app.route('/')
def index():
    return render_template('index1.html')
##自定义指令
@app.cli.command()
def create():
    db.drop_all() ##删除旧的表
    db.create_all() ##创建新的表
    Book.init_db()##初始化

##api类
class BookApi(MethodView):
    def get(self,book_number):
        if book_number is None:
            stmt = select(Book)
            books: list[Book] = db.session.execute(stmt).scalars().all()
            results = [
                {
                    'book_number': book.book_number,
                    'book_name': book.book_name,
                    'book_type': book.book_type,
                    'book_prize': book.book_price,
                    'book_publisher': book.book_publisher,
                    'book_author': book.book_author,
                } for book in books
            ]
            return {
                'code': 200,
                'status': 'success',
                'message': '数据查询成功',
                'results': results
            }

        book: Book = db.session.get(Book, book_number)
        return {
            'code': 200,
            'status': 'success',
            'message': '数据查询成功',
            'result': {
                'book_number': book.book_number,
                'book_name': book.book_name,
                'book_type': book.book_type,
                'book_prize': book.book_price,
                'book_publisher': book.book_publisher,
                'book_author': book.book_author,
            }
        }

    def post(self ,book_number):
        form = request.json
        book = Book()
        book.book_number = form.get('book_number')
        book.book_name = form.get('book_name')
        book.book_type = form.get('book_type')
        book.book_price = form.get('book_prize')
        book.book_author = form.get('book_author')
        book.book_publisher = form.get('book_publisher')
        db.session.add(book)
        db.session.commit()

        return {
            'code': 200,
            'status': 'success',
            'message': '数据添加成功'
        }

    def delete(self, book_number):
        book: Book = db.session.get(Book, book_number)
        db.session.delete(book)
        db.session.commit()
        return {
            'code': 200,
            'status': 'success',
            'message': '数据删除成功'
        }
    def put(self, book_number):
        book: Book = db.session.get(Book, book_number)
        book.book_number = request.json.get('book_number')
        book.book_type = request.json.get('book_type')
        book.book_name = request.json.get('book_name')
        book.book_prize = request.json.get('book_price')
        book.book_publisher = request.json.get('book_publisher')
        book.author = request.json.get('author')
        db.session.commit()
        return {
            'code': 200,
            'status': 'success',
            'message': '数据修改成功'
        }

##defaults 默认传参，view_func 函数视图
book_view = BookApi.as_view('book_api')

app.add_url_rule('/books/',defaults={'book_number':None},
                 view_func=book_view,methods=['GET','Post',])
app.add_url_rule('/books/<int:book_number>',view_func=book_view,
                 methods=['GET','POST','DELETE','Put'],)

if __name__ == '__main__':
    app.run(debug=True)