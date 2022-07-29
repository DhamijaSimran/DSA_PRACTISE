from datetime import datetime
import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def Email_function(data, receivers, sender_address):
    receiver_address = receivers

    # Setup the MIME
    message = MIMEMultipart('alternative')
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'GPDIP:LONG RUNNING JOBS FOUND'

    try:
        # Create SMTP session for sending the mail
        session = smtplib.SMTP(host='GROSMTP.amer.pfizer.com', port=25)
        session.starttls()
        body = """<h3><b>FOR YOUR AWARENESS: LONG RUNNING JOBS FOUND.</b></h3>\n
        <p> The below jobs have been running for more than twice the average time it usually takes for them to 
        complete. </p> 
        """
        for i in data:
            body = body + "{job_id} has been running for {seconds}. It's average run time is {avg_run}\n".format(job_id=i[0],seconds=i[2],avg_run=i[1])

        body = MIMEText(body, 'html')
        message.attach(body)
        session.sendmail(sender_address, receiver_address, message.as_string())
        session.quit()
        print('Mail Sent')
    except Exception as e:
        print(e)

def get_long_running_jobs(script_run_time):
    try:
        connection = mysql.connector.connect()
        cursor = connection.cursor()

        started_job = 'select job_id,job_start_ts,job_status,timestampdiff(second,job_start_ts,current_timestamp) as result from GPDIP.job_run where job_status=\'STARTED\' '
        cursor.execute(started_job)
        result = cursor.fetchall()
        started_jobs = [(i[0].strip(), float(i[3])) if i[3] is not None else 0 for i in result]

        avg_run = 'select job_id,avg(timestampdiff(second,job_start_ts,job_end_ts)) as result from GPDIP.job_run where job_status=\'COMPLETED\' group by job_id;'
        cursor.execute(avg_run)
        average_time = cursor.fetchall()
        averages = {i[0].strip(): float(i[1]) if i[1] is not None else 0 for i in average_time}

        cursor.close()
        connection.close()

        long_run_jobs = []
        not_long_running = []
        not_found = []
        for i in started_jobs:
            if i[0] in averages.keys():
                if i[1] >= (averages[i[0]] * 2):
                    # print('LONG RUNNING JOB: '+str(i[0])+'.AVERAGE TIME: '+str(final_average[i[0]])+' .CURRENT TIME TAKEN: '+str(i[1]))
                    long_run_jobs.append((i[0].strip(), averages[i[0]], i[1]))
                else:
                    # print('NOT LONG RUNNING JOB: '+str(i[0])+'.AVERAGE TIME: '+ str(final_average[i[0]])+' .CURRENT TIME TAKEN: '+str(i[1]))
                    not_long_running.append((i[0].strip(), averages[i[0]], i[1]))
            else:
                not_found.append((i[0].strip(), i[1]))

        if len(long_run_jobs)>0:
            segregate_lrj(script_run_time,long_run_jobs)
            receivers = ['abhinav.dubey@pfizer.com']
            Email_function(long_run_jobs,receivers)

    except Exception as e:
        print(e)


def segregate_lrj(script_run_time,long_run_jobs):
    # calculate new jobs added in the last 15 mins to lrj
    # last - from script_run_time


script_run_time = datetime.datetime.now()
get_long_running_jobs(script_run_time)