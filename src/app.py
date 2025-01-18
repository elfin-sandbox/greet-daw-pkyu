from flask import Flask, render_template, request

app = Flask(__name__)

names = {1: "Yvan", 2: "Yuan", 3: "Gabo", 4: "Sean"}

@app.route('/', methods=['GET', 'POST'])
def greet_person():
    greeting = ""
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            if number in names:
                greeting = f"HASHASHASHAH {names[number]}, pakyu!"
            else:
                greeting = "Invalid number. Please enter a number between 1 and 4."
        except ValueError:
            greeting = "Invalid input. Please enter a valid number."
    return render_template('index.html', greeting=greeting)

if __name__ == "__main__":
    app.run(debug=True)