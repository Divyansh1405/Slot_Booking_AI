from flask import Flask, render_template, request
import joblib
from database import init_db, book_slot, is_slot_booked

app = Flask(__name__)
model = joblib.load('model/slot_predictor.pkl')
init_db()

day_mapping = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
               'Friday': 4, 'Saturday': 5, 'Sunday': 6}
slot_mapping = {'09:00-10:00': 0, '10:00-11:00': 1, '11:00-12:00': 2,
                '12:00-01:00': 3, '01:00-02:00': 4}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    day = request.form['day']
    time_slot = request.form['time_slot']

    day_code = day_mapping.get(day, -1)
    time_code = slot_mapping.get(time_slot, -1)

    if day_code == -1 or time_code == -1:
        return render_template('index.html', message="Invalid input.")

    prediction = model.predict([[day_code, time_code]])[0]

    if is_slot_booked(day, time_slot):
        message = f"⚠️ Slot on {day} at {time_slot} is already booked."
    else:
        book_slot(name, day, time_slot)
        message = f"✅ Booking confirmed for {name} on {day} at {time_slot}."

    return render_template('index.html', prediction=round(prediction, 2), message=message)

if __name__ == '__main__':
    app.run(debug=True)
