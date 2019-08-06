from databases import *
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

# function for going to the home page
@app.route('/')
def home():
    return render_template('index.html',comments=query_all())

#function for viewing all the comments that people left
@app.route('/viewcomments')
def display_comments():
    return render_template('viewcomments.html', comments=query_all())

#function for going to the comment page and adding comments 
@app.route('/add', methods=['GET', 'POST'])
def add_comment_route():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        name = request.form['user_name']
        email = request.form['user_email']
        comment = request.form['user_comment']
        add_comment(name, email, comment)
        return redirect('/#contact')

#function for deleting a comment (not used at the moment)
@app.route('/delete/<int:id_num>', methods=['POST'])
def delete_comment_route(id_num):
	print(id_num)
	delete_comment_id(id_num)
	return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
