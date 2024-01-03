from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
import cv2
import face_recognition
import os
from datetime import datetime
import csv


STUDENT_FACE_DIRECTORY = 'Student_face'
MANIT_LOGO_PATH = 'C:/Users/dhurv/PycharmProjects/aiproject/gui_logo/manitlogo.png'
STUDENT_LOGO_PATH = 'C:/Users/dhurv/PycharmProjects/aiproject/gui_logo/studentlogo.png'
CLICKED_FACE_PATH = 'clicked_face'

# Initialize cap as a global variable
cap = None
camera_update_flag = True
camera_label = None

# store face encodings in this list
clicked_student_face_encoding = []
known_student_face_encodings = []


def match(scholar_number, name):
    df = pd.read_csv('data (1).csv')
    x = df['Scholar No'].tolist()
    y = df['Name of Student'].tolist()
    for a, b in zip(x, y):
        if a == scholar_number and b == name:
            return True
    return False


def clear_widgets(window):
    for widget in window.winfo_children():
        widget.destroy()


def load_known_student_face_encodings():
    for file_name in os.listdir(STUDENT_FACE_DIRECTORY):
        student_image = face_recognition.load_image_file(os.path.join(STUDENT_FACE_DIRECTORY, file_name))
        face_location = face_recognition.face_locations(student_image)
        if len(face_location) > 0:
            face_encoding = face_recognition.face_encodings(student_image, [face_location[0]])[0]
            known_student_face_encodings.append(face_encoding)
    # print('unknown ', known_student_face_encodings)


def encode_face(filename):
    try:
        image = face_recognition.load_image_file(filename)
        face_location = face_recognition.face_locations(image)
        if len(face_location) > 0:
            face_encoding = face_recognition.face_encodings(image, face_location)[0]
            return face_encoding
    except Exception as e:
        print(f"Error encoding face: {e}")
        return None


def check_matching_face():
    if clicked_student_face_encoding:
        for student_encoding in known_student_face_encodings:
            match_result = face_recognition.compare_faces([student_encoding], clicked_student_face_encoding[0])
            if True in match_result:
                return True
    return False


def attendence():
    df = pd.read_excel('NEW TIME TABLE.xlsx')
    columns_to_fill = ['FOURTH PERIOD', 'SIXTH PERIOD']
    df[columns_to_fill] = df[columns_to_fill].fillna(value='')
    dic = {
        'FIRST PERIOD': '10:00:00 AM - 11:00:00 AM',
        'SECOND PERIOD': '11:00:00 AM - 12:00:00 PM',
        'THIRD PERIOD': '12:00:00 PM - 01:00:00 PM',
        'FOURTH PERIOD': '02:00:00 PM - 03:00:00 PM',
        'FIFTH PERIOD': '03:00:00 PM - 04:00:00 PM',
        'SIXTH PERIOD': '04:15:00 PM - 05:15:00 PM'
    }
    day = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4
    }

    current_time_str = datetime.now().strftime("%I:%M:%S %p")
    current_time = datetime.strptime(current_time_str, "%I:%M:%S %p").time()

    current_datetime = datetime.now()
    current_day = current_datetime.strftime("%A")

    if current_day in day:
        x = day[current_day]
    # print(x,current_day)
    colunm = {'FIRST PERIOD': 1,
              'SECOND PERIOD': 2,
              'THIRD PERIOD': 3,
              'FOURTH PERIOD': 4,
              'FIFTH PERIOD': 5,
              'SIXTH PERIOD': 6}

    for key, value in dic.items():
        start_time_str, end_time_str = value.split(' - ')
        start_time = datetime.strptime(start_time_str, "%I:%M:%S %p").time()
        end_time = datetime.strptime(end_time_str, "%I:%M:%S %p").time()

        if start_time <= current_time <= end_time:
            # z = df[key][current_day]  # Access DataFrame based on the current period and day
            if key in colunm:
                y = colunm[key]
            # print(y,key)
            # print(df.iloc[x, y])

            return df.iloc[x, y]

    # return 'No matching period found for the current time.'


def update_attendance_csv(scholar_number, subject):
    filename = f'C:/Users/dhurv/PycharmProjects/aiproject/mainface/student_csv/{scholar_number}.csv'

    # Check if the file exists, if not create it
    if not os.path.exists(filename):
        create_student_csv(scholar_number, [subject])

    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    # Check if the student has already marked attendance for the current subject in the current hour
    marked = False
    for row in rows:
        if row['Subject Name'] == subject and row['Attendence'] == '1':
            marked = True
            break

    if not marked:
        for row in rows:
            if row['Subject Name'] == subject:
                row['Attendence'] = '1'

        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Subject Name', 'Attendence']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)


def create_student_csv(scholar_number):
    filename = f'C:/Users/dhurv/PycharmProjects/aiproject/mainface/student_csv/{scholar_number}.csv'
    subjects = ['Data Science', 'AI', 'CN', 'Statistical Modeling', 'Compiler Design', 'OS','CN LAB','OS LAB','COMPILER LAB']
    try:
        if not os.path.exists(filename):
            with open(filename, mode='w', newline='') as csvfile:
                fieldnames = ['Subject Name', 'Attendence']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                print('create ho rahi  hi ',filename)
                for subject in subjects:
                    print(subject)
                    writer.writerow({'Subject Name': subject, 'Attendence': 0})
        # else:
        #     print(f"File already exists for scholar {scholar_number}.")
    except Exception as e:
        print(f"Error creating CSV file for scholar {scholar_number}: {str(e)}")


def back_to_main_page(x):
    x.destroy()
    front_win()


def save_photo(frame, scholar_number, log1):
    global cap
    load_known_student_face_encodings()
    # Specify the full file path where you want to save the photo
    filename = f'C:/Users/dhurv/PycharmProjects/aiproject/mainface/clicked_face/{scholar_number}.png'
    cv2.imwrite(filename, frame)
    if cap is not None:
        cap.release()
    clear_widgets(log1)
    x = log1
    # student_details(scholar_number, x, filename)
    A = '{} : Information'.format(scholar_number)
    x.title(A)
    face_encoding = encode_face(filename)
    if len(face_encoding) > 0:
        clicked_student_face_encoding.append(face_encoding)
        # print(clicked_student_face_encoding)
    # print('KNOWN FACE',clicked_student_face_encoding)
    period = attendence()

    if check_matching_face() is True:
        L = Label(x, text=f"Scholar Number: {scholar_number}\nPeriod: {period}", fg='red')
        L.pack()
        # Z = period

        # print(key,value,z)
        subject_list = ['Data Science', 'AI', 'CN', 'Statistical Modeling', 'Compiler Design', 'OS', 'CN LAB', 'OS LAB', 'COMPILER LAB']
        if period in subject_list:
            L1 = Label(x, text='{} Attendence marked '.format(period), fg='green')
            L1.pack()
            create_student_csv(scholar_number)
            update_attendance_csv(scholar_number, period)
            L2 = Label(x)
            L2.pack()
            btn = Button(x, text='Go to login Page', command=lambda: front_win())
            btn.pack()
        else:
            btn = Button(x, text='Go to login Page', command=lambda: back_to_main_page(x))
            btn.pack()
    else:
        L = Label(x, text='{} not found'.format(scholar_number), fg='red')
        L.pack()


def student_login(main_window, scholar_number, student_name):
    global cap, camera_label

    if match(scholar_number, student_name):
        clear_widgets(main_window)
        log1 = main_window
        log1.title('Student Info')

        camera_frame = Frame(log1, width=100, height=200)
        camera_frame.pack()

        def update_camera():
            global cap, camera_update_flag
            if cap is not None and camera_update_flag:
                ret, frame = cap.read()
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    photo = ImageTk.PhotoImage(Image.fromarray(frame))
                    camera_label.config(image=photo)
                    camera_label.image = photo
                    camera_label.after(10, update_camera)

        camera_label = Label(camera_frame, height=400, width=300)
        camera_label.pack()

        cap = cv2.VideoCapture(0)
        update_camera()

        student_info = "Name: {}\nScholar Number: {}".format(student_name, scholar_number)
        L = Label(log1, text=student_info)
        L.pack()

        captured_frame = Frame(log1, width=400, height=200)
        captured_frame.pack()

        def capture_and_save(scholar_number, log1):
            ret, frame = cap.read()
            if ret:
                save_photo(frame, scholar_number, log1)

        save_button = Button(captured_frame, text="Save Photo", state=NORMAL,
                             command=lambda: capture_and_save(scholar_number, log1))
        save_button.pack()

        log1.mainloop()
    else:
        l = Label(main_window, text='Student Not Found', fg='red', font=("Helvetica", 15))
        l.pack()


def front_win():
    main_window = Tk()
    main_window.title('MANIT Bhopal Online Attendance')
    main_window.minsize(600, 600)
    main_window.maxsize(600, 600)

    l1 = Label(main_window, text='ONLINE ATTENDANCE', font=("Helvetica", 20))
    l1.pack()

    image = Image.open(MANIT_LOGO_PATH)
    image = image.resize((150, 150))
    photo = ImageTk.PhotoImage(image)
    l2 = Label(main_window, image=photo)
    l2.photo = photo  # Keep a reference to the photo to avoid garbage collection
    l2.pack()

    scholar_number = StringVar()
    student_name = StringVar()

    l1 = Label(main_window, text='Scholar Number', fg='blue', font=("Helvetica", 15), anchor="center")
    l1.pack()
    scholar = Entry(main_window, textvariable=scholar_number, font=("Helvetica", 15))
    scholar.pack()

    l2 = Label(main_window, text='Student Name (in capital)', fg='blue', font=("Helvetica", 15), anchor="center")
    l2.pack()
    dob = Entry(main_window, textvariable=student_name, font=("Helvetica", 15))
    dob.pack()

    btn = Button(main_window, text='Log in', bg='blue', fg='white',
                 command=lambda: student_login(main_window, scholar_number.get(), student_name.get()))
    btn.pack()

    main_window.mainloop()


if __name__ == '__main__':
    front_win()
    # attendence()