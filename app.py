from flask import Flask, request

#  RENDER Settings start command needs      gunicorn app:app

# The Flask application object must be available at the top level
app = Flask(__name__) 
MAGIC_WORD = 'fred'
magic_word_count = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global magic_word_count  # 🔑 FIX 1: Declares intent to modify the global variable
    
    # Initial message for GET request or failure case
    result = f"<span style='color:red'> Try the magic word 'fred'. Total count: {magic_word_count}</span>"
    
    # Logic for handling form submission (POST request)
    if request.method == 'POST':
        my_input = request.form.get('myText01')
        
        if my_input == MAGIC_WORD:
            magic_word_count += 1
            
            # Use Python's f-string formatting to display the count
            result = f"<b style='color:green'> That's correct! </b> The magic word has been entered {magic_word_count} times."
        else:
            # On failure, still show the current count
            result = f"<span style='color:red'> Try the magic word 'fred'. Total count: {magic_word_count}</span>"
    # HTML template with the dynamic result
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>t2a27</title>
    </head>
    <body>
        <h3 align=center>t2a27-render-python-nolan</h3>
        <form action="/" method="post">
            <label for="myText01">Enter Text:</label>
            <input type="text" id="myText01" name="myText01">
            <input type="submit" value="Submit">
        </form>
        {result}
    </body>
    </html>
    """
    return html_content

# --- REMOVE THIS BLOCK FOR PRODUCTION DEPLOYMENT ---
# if __name__ == '__main__':
#     app.run(debug=True)
# ----------------------------------------------------
