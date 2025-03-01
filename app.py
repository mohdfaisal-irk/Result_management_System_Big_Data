from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('Output/student_data.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        student_id = request.form['student_id'].strip()
        student_info = df[df['Student_ID'] == student_id]

        if not student_info.empty:
            student_data = student_info.iloc[0].to_dict()
            result = {
                "name": student_data["Name"],
                "age": student_data["Age"],
                "city": student_data["City"],
                "marks": {
                    "Electronics": student_data["Electronics"],
                    "Programming": student_data["Programming"],
                    "Database": student_data["Database"],
                    "Data Science": student_data["Data Science"],
                    "Mathematics": student_data["Mathematics"],
                    "DSA": student_data["DSA"]
                },
            }
        else:
            result = "Student ID not found!"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
