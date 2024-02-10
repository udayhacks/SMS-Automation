import pandas as pd
import os
from twilio.rest import Client

# Twilio Account SID and Auth Token
# account_sid = 'your_account_sid'
# auth_token = 'your_auth_token'
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Read Excel file
file_path = 'students_attendance.xlsx'
df = pd.read_excel(file_path)

# Define threshold for attendance percentage
attendance_threshold = 70

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    student_name = row['Name']
    attendance_percentage = row['Attendance']

    # Check if attendance percentage is less than threshold
    if attendance_percentage < attendance_threshold:
    #    print(str(row['Mobile_Number']))
        # Send SMS to student's mobile number
        message = f"Dear {student_name}, your attendance is very low ({attendance_percentage}%). Please improve."
        # Replace 'to' with the student's phone number
        to_phone_number = str(row['Mobile_Number'])  # Replace with the student's phone number
        print(str(to_phone_number))
        print("uday")
        # Send message using Twilio
        client.messages.create(
            body=message,
            from_='+16593365023',
            to="+91"+to_phone_number
        )
        print(f"Message sent to {student_name} at {to_phone_number}")
