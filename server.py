from flask import Flask
import random
rand_num = random.randint(0,9)
#creating app from flask application
app = Flask(__name__)

#when user hits up home route/path that is going to be home page; python decorator
@app.route('/')
def home_page():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')

@app.route('/<int:number>')
def user_guess(number):
    if number < rand_num:
        return ('<h1>Too low, try again!</h/1>'
                '<img src="<div style="width:100%;height:0;padding-bottom:75%;position:relative;"><iframe src="https://giphy.com/embed/OKq2SI9ioDxtK" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/up-crittersup-bootingdogs-OKq2SI9ioDxtK">')
    elif number > rand_num:
        return ('<h1>Too high, try again!</h1>'
                '<img src="<div style="width:100%;height:0;padding-bottom:100%;position:relative;"><iframe src="https://giphy.com/embed/l4FGjrCVCnu01XOFi" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/barkpost-jump-l4FGjrCVCnu01XOFi">')
    else:
        return('<h1>Woo Hoo!  You are correct</h1>'
               '<img src="<div style="width:100%;height:0;padding-bottom:100%;position:relative;"><iframe src="https://giphy.com/embed/3o7abAHdYvZdBNnGZq" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/dog-puppy-dottie-3o7abAHdYvZdBNnGZq">')
#special attribute tap into name of class, funciton, method, descriptor name run as a script; denotes file
#currently being run
if __name__ == "__main__":
     #execute only if run as a script; tap into our app; debug mode on automates updates and provides pin for debugger
     app.run(debug=True)

