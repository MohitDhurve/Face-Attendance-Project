# Face-Attendance-Project
<h3>Functionality:</h3>


<ul>
  <li>The program uses the Tkinter library for creating a graphical user interface (GUI).</li>
  <li>It integrates the OpenCV library to capture and process video frames from a camera.</li>
  <li>Face recognition is implemented using the face_recognition library.</li>
  <li>The system matches a student's face with known faces stored in the 'Student_face' directory.</li>

</ul>

<h3>Key Components:</h3>

<h4>Main Window:</h4>
<p>The main window contains fields for entering the scholar number and student name, along with a login button.</p> 
Student Login: After entering the scholar number and student name, the system attempts to match the provided information with the stored data.
Camera Integration: The GUI includes a live camera feed for capturing images during student logins.
Attendance Marking: Upon successful face recognition, the system marks attendance for the corresponding student and updates a CSV file.
Files and Directories:

Student_face Directory: Contains images of known student faces.
Clicked_face Directory: Stores images captured during the login process.
Mainface Directory: Includes subdirectories for storing student CSV files and other resources.
Additional Notes:

The attendance is marked based on the matching of faces and corresponding scholar numbers.
The program reads a CSV file ('data (1).csv') for scholar number and student name information.
There is a reference to a timetable file ('NEW TIME TABLE.xlsx') for determining the current period.
Dependencies:

The script depends on various libraries, such as Tkinter, PIL (Pillow), pandas, OpenCV, face_recognition, and datetime.
Possible Improvements:

Error handling and logging could be enhanced for better robustness.
The code could be structured into functions for improved readability and maintainability.
Consideration of security measures for face recognition systems, as they are susceptible to various attacks.
