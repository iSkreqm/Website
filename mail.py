python -m file:///C:/Users/paulJ/Desktop/SpaceWebSite/contact.html 8000

def create_message(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_string())}



#970936697644-oc8l16pfsdq2u3r77k0k1m99259hb4ba.apps.googleusercontent.com
#AIzaSyCmly5xbitdtPTNeTMtwfE3FDOI5uFwo5o

