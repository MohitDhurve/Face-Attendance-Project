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
<h4>Student Login:</h4>
<p>After entering the scholar number and student name, the system attempts to match the provided information with the stored data.</p>
<h4>Camera Integration:</h4>
<p>The GUI includes a live camera feed for capturing images during student logins.</p>
<h4>Attendance Marking:</h4>
<p>Upon successful face recognition, the system marks attendance for the corresponding student and updates a CSV file.
Files and Directories:</p>

<h3>Files and Directories:</h3>
<h4>Student_face Directory:</h4>
<p>Contains images of known student faces.</p>
<h4>Clicked_face Directory:</h4>
<p>Stores images captured during the login process.</p>
<h4>Mainface Directory:</h4>
<p>Includes subdirectories for storing student CSV files and other resources.</p>

<h3>Additional Notes:</h3>
<ul>
  <li>The attendance is marked based on the matching of faces and corresponding scholar numbers.</li>
  <li>The program reads a CSV file ('data (1).csv') for scholar number and student name information.</li>
  <li>There is a reference to a timetable file ('NEW TIME TABLE.xlsx') for determining the current period.</li>
</ul>



<h3>Dependencies:</h3>

<p>The script depends on various libraries, such as Tkinter, PIL (Pillow), pandas, OpenCV, face_recognition, and datetime.</p>
<h3>Possible Improvements:</h3>
<ul>
  <li>Error handling and logging could be enhanced for better robustness.</li>
  <li>The code could be structured into functions for improved readability and maintainability.</li>
  <li>Consideration of security measures for face recognition systems, as they are susceptible to various attacks.</li>
</ul>




