import os
import random
import datetime

def save_uploaded_files(request, UPLOAD_DIRECTORY):
    TEMP_DIRECTORY = datetime.datetime.now().strftime('%Y_%m_%d_') + str(random.randint(100000000,999999999))
    os.mkdir(os.path.join(UPLOAD_DIRECTORY, TEMP_DIRECTORY))
    
    uploaded_file_1 = request.FILES['file_1']
    filename_to_save_to = os.path.join(UPLOAD_DIRECTORY, TEMP_DIRECTORY, str(uploaded_file_1))

    with open(filename_to_save_to, 'wb+') as destination:
        for chunk in uploaded_file_1.chunks():
            destination.write(chunk)

    uploaded_file_2 = request.FILES['file_2']
    filename_to_save_to = os.path.join(UPLOAD_DIRECTORY, TEMP_DIRECTORY, str(uploaded_file_2))
    
    with open(filename_to_save_to, 'wb+') as destination:
        for chunk in uploaded_file_2.chunks():
            destination.write(chunk)

    path_to_uploaded_files = os.path.join(UPLOAD_DIRECTORY, TEMP_DIRECTORY)
    return path_to_uploaded_files

def remove_temp_files(UPLOAD_DIRECTORY):
    todays_prefix = datetime.datetime.now().strftime('%Y_%m_%d_')
    yesterdays_prefix = (datetime.datetime.now() - datetime.timedelta(days = 1)).strftime('%Y_%m_%d_')
    directories = glob.glob(UPLOAD_DIRECTORY + '/*/')
    old_directories = [x for x in directories if not (x.startswith(todays_prefix) or x.startswith(yesterdays_prefix)]
    for directory in old_directories:
        files = glob.glob(os.path.join(directory + '/*.*'))
        for file in files:
            os.remove(file)
        os.rmdir(directory)


#Input is results of df.to_html()
#This will modify the table to have bootstrap formatting, as well as make the headers into radio buttons.
#There is a glitch here:
#   - The buttons have the little circle inside of them....
def modify_html_headers(html_string, columns):
    without_header = re.sub(r'\<table.*\/tr\>\s+\<\/thead','<thead', html_string.replace('\n',''))
    header = '<div class="btn-group btn-group-toggle" data-toggle="buttons"><table class="table table-striped"><tr><td></td>'
    for col in columns:
        header += '<td><div class="btn-group" ><label class="btn btn-secondary"><input id = "{}" type="radio" checked autocomplete="off">{}</label></div></td>'.format(col,col)
    header +='</tr>'
    return (header + without_header + '</div>')




import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

def send_mail(send_from, send_to, subject, body, files=None):
    assert isinstance(send_to, list)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('username', 'password')

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    email_body = MIMEText(body, 'html')
    
    msg.attach(email_body)
    
    for f in files or []:
        with open(f, "rb") as file_:
            part = MIMEApplication(
                file_.read(),
                Name=str(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % os.path.split(f)[-1]
        msg.attach(part)

    server.sendmail(send_from, send_to, msg.as_string())
    server.close()
