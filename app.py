# from flask import Flask, render_template, request, redirect, url_for, flash
# import mysql.connector as msql
# import csv
# import subprocess

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # MySQL connection
# password = 'hello'
# conect = msql.connect(user='root', host='localhost', passwd=password, database='JEE_Mains')
# cursor = conect.cursor()

# # Pipeline execution function
# # def run_pipeline(num_students, prefix):
# #     try:
# #         # Passing user input to your external script
# #         subprocess.run(['python3', 'generate_master_data.py', str(num_students), prefix], check=True)
# #         subprocess.run(['python3', 'generate_test_data.py'], check=True)
# #         subprocess.run(['python3', 'generate_percentile_rank.py'], check=True)
# #     except subprocess.CalledProcessError as e:
# #         return f"An error occurred while running the pipeline: {e}"

# # Home page
# @app.route('/')
# def index():
#     return render_template('index.html')

# # # Route to display form and run the pipeline
# # @app.route('/run_pipeline', methods=['GET', 'POST'])
# # def pipeline_route():
# #     if request.method == 'POST':
# #         # Get user input from the form
# #         num_students = request.form['num_students']
# #         prefix = request.form['prefix']

# #         # Run the pipeline with the user input
# #         error_message = run_pipeline(num_students, prefix)

# #         if error_message:
# #             flash(error_message)
# #             return redirect(url_for('pipeline_route'))
# #         else:
# #             flash('Pipeline executed successfully.')
# #             return redirect(url_for('index'))
    
# #     return render_template('run_pipeline.html')

# # Route 1: Get Markscard by Registration ID
# @app.route('/marks_by_regid', methods=['GET', 'POST'])
# def marks_by_regid():
#     if request.method == 'POST':
#         regid = request.form['regid']
#         cursor.execute(f"SELECT * FROM Student_FinalScores WHERE Reg_ID = '{regid}'")
#         result = cursor.fetchall()

#         if not result:
#             flash('Invalid Registration ID.')
#             return redirect(url_for('marks_by_regid'))

#         return render_template('marks_by_regid.html', result=result[0])

#     return render_template('marks_by_regid.html')

# # Route 2: Get Toppers and save to CSV
# @app.route('/toppers', methods=['GET', 'POST'])
# def toppers():
#     if request.method == 'POST':
#         no = request.form['number']
#         cursor.execute(f'SELECT Reg_ID, Student_Name, Final_Rank, Total1, Total2, Total_Percentile, Math_Percentile, Phy_Percentile, Chem_Percentile FROM Student_FinalScores ORDER BY Final_Rank LIMIT {no}')
#         toppers_list = cursor.fetchall()

#         with open('Toppers.csv', 'w') as file:
#             writer = csv.writer(file)
#             writer.writerow(('Registration ID', 'Student Name', 'Final Rank', 'Attempt 1 Total', 'Attempt 2 Total', 'Overall Percentile', 'Maths Percentile', 'Physics Percentile', 'Chemistry Percentile'))
#             for row in toppers_list:
#                 writer.writerow(row)

#         flash('Toppers CSV file has been created successfully.')
#         return redirect(url_for('toppers'))

#     return render_template('toppers.html')

# # Route 3: Get students in a rank range
# @app.route('/rank_range', methods=['GET', 'POST'])
# def rank_range():
#     if request.method == 'POST':
#         lower_rank = request.form['lower_rank']
#         upper_rank = request.form['upper_rank']
#         cursor.execute(f'SELECT Reg_ID, Student_Name, Final_Rank, Total1, Total2, Total_Percentile, Math_Percentile, Phy_Percentile, Chem_Percentile FROM Student_FinalScores WHERE Final_Rank BETWEEN {lower_rank} AND {upper_rank} ORDER BY Final_Rank')
#         rank_list = cursor.fetchall()

#         with open('Ranklist.csv', 'w') as file:
#             writer = csv.writer(file)
#             writer.writerow(('Registration ID', 'Student Name', 'Final Rank', 'Attempt 1 Total', 'Attempt 2 Total', 'Overall Percentile', 'Maths Percentile', 'Physics Percentile', 'Chemistry Percentile'))
#             for row in rank_list:
#                 writer.writerow(row)

#         flash(f'Rank list for ranks between {lower_rank} and {upper_rank} has been created successfully.')
#         return redirect(url_for('rank_range'))

#     return render_template('rank_range.html')

# # Route 4: Get students in marks range
# @app.route('/marks_range', methods=['GET', 'POST'])
# def marks_range():
#     if request.method == 'POST':
#         lower_marks = request.form['lower_marks']
#         upper_marks = request.form['upper_marks']
#         cursor.execute(f'SELECT Reg_ID, Student_Name, Final_Rank, Total1, Total2, Total_Percentile, Math_Percentile, Phy_Percentile, Chem_Percentile FROM Student_FinalScores WHERE GREATEST(Total1, Total2) BETWEEN {lower_marks} AND {upper_marks} ORDER BY Final_Rank')
#         marks_list = cursor.fetchall()

#         with open('Markbandlist.csv', 'w') as file:
#             writer = csv.writer(file)
#             writer.writerow(('Registration ID', 'Student Name', 'Final Rank', 'Attempt 1 Total', 'Attempt 2 Total', 'Overall Percentile', 'Maths Percentile', 'Physics Percentile', 'Chemistry Percentile'))
#             for row in marks_list:
#                 writer.writerow(row)

#         flash(f'Marks list for range between {lower_marks} and {upper_marks} has been created successfully.')
#         return redirect(url_for('marks_range'))

#     return render_template('marks_range.html')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import mysql.connector as msql
import csv
import io

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL connection
password = 'hello'
conect = msql.connect(user='root', host='localhost', passwd=password, database='JEE_Mains')
cursor = conect.cursor()

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Route 1: Get Markscard by Registration ID
@app.route('/marks_by_regid', methods=['GET', 'POST'])
def marks_by_regid():
    if request.method == 'POST':
        regid = request.form['regid']
        cursor.execute(f"SELECT * FROM Student_FinalScores WHERE Reg_ID = '{regid}'")
        result = cursor.fetchall()

        if not result:
            flash('Invalid Registration ID.')
            return redirect(url_for('marks_by_regid'))

        return render_template('marks_by_regid.html', result=result[0])

    return render_template('marks_by_regid.html')

# Route 2: Get Toppers and save to CSV
@app.route('/toppers', methods=['GET', 'POST'])
def toppers():
    if request.method == 'POST':
        no = request.form['number']
        cursor.execute(f'SELECT Reg_ID, Student_Name, Final_Rank, Total1, Total2, Total_Percentile, Math_Percentile, Phy_Percentile, Chem_Percentile FROM Student_FinalScores ORDER BY Final_Rank LIMIT {no}')
        toppers_list = cursor.fetchall()

        # Create a CSV in memory
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(('Registration ID', 'Student Name', 'Final Rank', 'Attempt 1 Total', 'Attempt 2 Total', 'Overall Percentile', 'Maths Percentile', 'Physics Percentile', 'Chemistry Percentile'))
        for row in toppers_list:
            writer.writerow(row)

        # Create a response object and set the correct headers
        response = make_response(output.getvalue())
        response.headers['Content-Disposition'] = 'attachment; filename=Toppers.csv'
        response.headers['Content-Type'] = 'text/csv'
        return response

    return render_template('toppers.html')

# Route 3: Get students in a rank range
@app.route('/rank_range', methods=['GET', 'POST'])
def rank_range():
    if request.method == 'POST':
        lower_rank = request.form['lower_rank']
        upper_rank = request.form['upper_rank']
        cursor.execute(f'SELECT Reg_ID, Student_Name, Final_Rank, Total1, Total2, Total_Percentile, Math_Percentile, Phy_Percentile, Chem_Percentile FROM Student_FinalScores WHERE Final_Rank BETWEEN {lower_rank} AND {upper_rank} ORDER BY Final_Rank')
        rank_list = cursor.fetchall()

        # Create a CSV in memory
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(('Registration ID', 'Student Name', 'Final Rank', 'Attempt 1 Total', 'Attempt 2 Total', 'Overall Percentile', 'Maths Percentile', 'Physics Percentile', 'Chemistry Percentile'))
        for row in rank_list:
            writer.writerow(row)

        # Create a response object and set the correct headers
        response = make_response(output.getvalue())
        response.headers['Content-Disposition'] = 'attachment; filename=Ranklist.csv'
        response.headers['Content-Type'] = 'text/csv'
        return response

    return render_template('rank_range.html')

# Route 4: Get students in marks range
@app.route('/marks_range', methods=['GET', 'POST'])
def marks_range():
    if request.method == 'POST':
        lower_marks = request.form['lower_marks']
        upper_marks = request.form['upper_marks']
        cursor.execute(f'SELECT Reg_ID, Student_Name, Final_Rank, Total1, Total2, Total_Percentile, Math_Percentile, Phy_Percentile, Chem_Percentile FROM Student_FinalScores WHERE GREATEST(Total1, Total2) BETWEEN {lower_marks} AND {upper_marks} ORDER BY Final_Rank')
        marks_list = cursor.fetchall()

        # Create a CSV in memory
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(('Registration ID', 'Student Name', 'Final Rank', 'Attempt 1 Total', 'Attempt 2 Total', 'Overall Percentile', 'Maths Percentile', 'Physics Percentile', 'Chemistry Percentile'))
        for row in marks_list:
            writer.writerow(row)

        # Create a response object and set the correct headers
        response = make_response(output.getvalue())
        response.headers['Content-Disposition'] = 'attachment; filename=Markbandlist.csv'
        response.headers['Content-Type'] = 'text/csv'
        return response

    return render_template('marks_range.html')

# Route 5: Delete a student by Registration ID
@app.route('/delete_student', methods=['GET', 'POST'])
def delete_student():
    if request.method == 'POST':
        regid = request.form['regid']

        # Check if the student exists in the database
        cursor.execute(f"SELECT * FROM Student_master WHERE Reg_ID = '{regid}'")
        result = cursor.fetchone()

        if not result:
            flash('Invalid Registration ID.')
            return redirect(url_for('delete_student'))

        # If the student exists, delete the record
        cursor.execute(f"DELETE FROM Student_master WHERE Reg_ID = '{regid}'")
        conect.commit()

        flash(f'Student with Registration ID {regid} has been deleted successfully.')
        return redirect(url_for('delete_student'))

    return render_template('delete_student.html')


if __name__ == '__main__':
    app.run(debug=True)
