#import libraries

from flask import Flask,render_template,request
import qrcode
from io import BytesIO
from base64 import b64encode

#create flask app
app = Flask(__name__)

# make flask home page render index.html file 
# flask renders the index.html file from the "templates" folder
@app.route('/')
def home():
    return render_template('index.html')

# gets flask to request data from the "link" input field in my html document using POST
# uses qrcode library to generate a qr code using the data provided and then saves the image to the computer's memory
@app.route('/', methods=['POST'])
def generateQR():
    memory = BytesIO()
    data = request.form.get('link')
    img = qrcode.make(data)
    img.save(memory)
    memory.seek(0)

    base64_img = "data:image/png;base64," + \
        b64encode(memory.getvalue()).decode('ascii')
    #sends generated image back to index.html to be rendered on the webpage
    return render_template('index.html', data=base64_img)


if __name__ == '__main__':
    app.run(debug=True)