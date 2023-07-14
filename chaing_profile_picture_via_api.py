from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64

# Replace with your service account credentials and list of user emails
SERVICE_ACCOUNT_FILE = './assets/adept-parsec-390920-314f53b1a9d7.json'
USER_EMAILS = ['uchitosato@gmail.com', 'afoucher7255@gmail.com']

# Authenticate using a service account key file
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=['https://www.googleapis.com/auth/admin.directory.user'])

# Build the Admin SDK Directory API client
service = build('admin', 'directory_v1', credentials=creds)

# Loop through each user and update their profile photo with a new image file
for user_email in USER_EMAILS:
    try:
        # Get the user's current profile photo
        user = service.users().get(userKey=user_email, projection='full').execute()
        photo_data = user['thumbnailPhotoUrl'].split(',')[1]
        photo_bytes = base64.b64decode(photo_data)

        # Update the user's profile photo with a new image file
        with open('./assets/profile_picture/new.jpg', 'rb') as file:
            new_photo_data = base64.b64encode(file.read()).decode('utf-8')
        new_photo_url = f'data:image/jpeg;base64,{new_photo_data}'
        user['thumbnailPhotoUrl'] = new_photo_url
        service.users().update(userKey=user_email, body=user).execute()
        print(f'Profile photo updated successfully for {user_email}.')
    except HttpError as error:
        print(f'An error occurred for {user_email}: {error}')
