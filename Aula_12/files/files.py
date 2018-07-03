from flask import Flask, render_template, request, send_file, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from io import BytesIO


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///filestorage.db'

db = SQLAlchemy(app)


class FileContents(db.Model):
    __tablename__='files'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), unique=True, nullable=False)
    data = db.Column(db.LargeBinary)

    def __repr__(self):
        return '<File %r>' % self.name


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/redirect', methods=['POST'])
def redirect():
    return render_template('uploadpage.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputFile']
    newFile = FileContents(name=file.filename, data=file.read())
    db.session.add(newFile)
    db.session.commit()
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    lista=[]
    for row in db.session.query(FileContents.name.label('name_label')).all():
        lista.append(row.name_label)
    return render_template('download.html', lista=lista)

@app.route('/downloadfile/<nome>', methods=['GET', 'POST'])
def downloadfile(nome):
    file_data = FileContents.query.filter_by(name=nome).first()
    if (file_data):
        return send_file(BytesIO(file_data.data), attachment_filename=nome, as_attachment=True)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
