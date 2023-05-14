from flask import Flask, render_template, request

app = Flask(__name__)

poll_data = {
    'Cat': 0,
    'Dog': 0,
    'Fish': 0
}

@app.route('/', methods=['GET', 'POST'])
def poll():
    if request.method == 'POST':
        selected_option = request.form['poll_option']
        poll_data[selected_option] += 1
        return render_template('result.html', option=selected_option)
    else:
        return render_template('poll.html')

@app.route('/results')
def results():
    return render_template('results.html', data=poll_data)

if __name__ == '__main__':
    app.run()

