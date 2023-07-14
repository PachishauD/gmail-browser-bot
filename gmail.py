import imaplib
import email

# Login to your Gmail account
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('your_email@gmail.com', 'your_password')

# Select the inbox folder
mail.select('inbox')

# Search for unread messages
status, response = mail.search(None, 'UNSEEN')

# Get the list of message IDs
message_ids = response[0].split()

# Loop through each message ID and fetch the message
for message_id in message_ids:
    status, response = mail.fetch(message_id, '(RFC822)')
    email_data = response[0][1]
    message = email.message_from_bytes(email_data)

    # Print the subject and sender of the message
    print('Subject:', message['Subject'])
    print('From:', message['From'])

# Logout of your Gmail account
mail.logout()