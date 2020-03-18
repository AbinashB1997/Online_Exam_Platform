import os, sys
from os import listdir
from os.path import isfile, join
import re
from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

def success_msg():
    return str("Thank you for your interest in GS Lab." + '\n' + '\n' + "You are shortlisted for the next round" + '\n' + '\n' + 'you have scored ')

def failure_msg():
    return str("Thank you for your interest in GS Lab." + '\n' + "We regret to inform you that we will not be able to take your candidature forward at this time.")

def runIT(is_present):
    #Create a folder where user's output will be stored. Lets call it user_out
    folders = [x[0] for x in os.walk('User/')]
    for i in range(1, len(folders)):
        if(folders[i] not in is_present):
            onlyfiles = [f for f in listdir(folders[i]) if isfile(join(folders[i], f))]

            #Create the folder for each users in the Admin folder
            userName = folders[i][folders[i].index('/', 2) + 1 : ]
            os.system('mkdir Admin/user_out/output_' + userName)

            # print(onlyfiles)
            if(len(onlyfiles) > 0):
                for files in onlyfiles:
                    Question_Number = list(map(int, re.findall(r'\d+', files)))[0]
                    if(files[files.index('.') + 1 : ] == 'py'):
                        if (os.stat(folders[i] + '/' + files).st_size == 0):
                            continue
                        else:
                            os.system('python3 ' + folders[i] + '/' + files + ' < ' + 'Admin/input.in/inp' + str(Question_Number) + '.txt' + ' > ' + 'Admin/user_out/output_' + userName + '/out' + str(Question_Number) + '.txt')
                    if(files[files.index('.') + 1 : ] == 'java'):
                        if (os.stat(folders[i] + '/' + files).st_size == 0):
                            continue
                        else:
                            os.system('javac ' + folders[i] + '/' + files)
                            os.system('java -cp ' + folders[i] + '/ ' + files[ : files.index('.')] + ' < ' + 'Admin/input.in/inp' + str(Question_Number) + '.txt' + ' > ' + 'Admin/user_out/output_' + userName + '/out' + str(Question_Number) + '.txt')
                    if(files[files.index('.') + 1 : ] == 'cpp'):
                        if (os.stat(folders[i] + '/' + files).st_size == 0):
                            continue
                        else:
                            os.system('g++ ' + folders[i] + '/' + files)
                            os.system('./a.out ' + ' < ' + 'Admin/input.in/inp' + str(Question_Number) + '.txt' + ' > ' + 'Admin/user_out/output_' + userName + '/out' + str(Question_Number) + '.txt')

def sender():
    return str('abinash.biswal@gslab.com')
def receiver():
    return str('abinashbiswal248@gmail.com')

def token():
    return str('frawrczyqooeolcm')

def send_email(user, pwd, recipient, subject, body, data):
    msg = MIMEMultipart()
    print('data is = ', data)
    msg.attach(MIMEText(data))
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, msg.as_string())
        server.close()
        del msg
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")
# Get User Output in Admin deirectory

@app.route('/testing', methods=['POST'])
@cross_origin()
def testing():

    #Copy folders into Users

    regNumber = request.get_json()['reg']
    os.system('cp -R ../data/'+regNumber + ' ./User')
    os.system('rm -R ../data/'+regNumber)
    os.system('mkdir ./Admin/user_out')
    is_present = set()

    reg_file = open('registration_number.txt', 'r+')
    reg_num = reg_file.readlines()

    for id in reg_num:
        is_present.add(id[ : id.index('\n')])

    print('set is : ', is_present)
    # if(os.path.isdir('./Admin/user_out')):
    #     os.system('rm -R ./Admin/user_out')
    runIT(is_present)
    # Iterate in UserOut to list all the output folder of users
    folders = [x[0] for x in os.walk('./Admin/user_out')]

    if(len(folders) > 0):
        curr_passed_testcase = 0
        total_testcases = 0
        onlyfiles = [f for f in listdir('./Admin/input.in') if isfile(join('./Admin/input.in', f))]
        print('current files are = ', onlyfiles)
        for inp_files in onlyfiles:
            f = open('./Admin/input.in/' + inp_files, "r")
            line = f.readline()
            total_testcases += int(line[ : line.index('\n')])
            f.close()
        print('total testcases = ', total_testcases)
        for Currfolder in range(1, len(folders)):
            is_calculation_done = False
            fol = folders[Currfolder]
            rev = fol[: : -1]
            regNum = rev[ : rev.index('_')][: : -1]
            if(regNum not in is_present):
                is_calculation_done = True
                reg_file.write(regNum + '\n') # Add the Registration Number in the set
                files = [f for f in listdir(folders[Currfolder]) if isfile(join(folders[Currfolder], f))]
                print('folder: ', folders[Currfolder])
                print('file name: ', files)
                for Currfile in files:
                    OutFile_Admin = open("./Admin/output.in/" + Currfile, "r")
                    OutFile_User = open(folders[Currfolder] + "/" + Currfile, "r")
                    print('matching ' + "./Admin/output.in/" + Currfile + " ---- with ---- " + folders[Currfolder] + "/" + Currfile)
                    Question_Number = list(map(int, re.findall(r'\d+', Currfile)))[0]
                    TC_PASSED = 0
                    file1 = OutFile_Admin.readlines()
                    file2 = OutFile_User.readlines()
                    for ans_num in range(len(file2)):
                        if(file2[ans_num][-2] == ' '):
                            file2[ans_num] = file2[ans_num][ : -2] + file2[ans_num][-1]
                    hold = file2[-1]
                    if(hold[-1] == '\n'):
                        file2[-1] = hold[ : hold.index('\n')]
                    print(file1)
                    print(file2)

                    for answer in range(len(file1)):
                        if(file1[answer] == file2[answer]):
                            TC_PASSED += 1

                    OutFile_Admin.close()
                    OutFile_User.close()
                    print('total TC: ', total_testcases)
                    print('passed TC: ', TC_PASSED)

                    curr_passed_testcase += TC_PASSED
                os.system('rm -rf ' + folders[Currfolder])
                percentage = "{:.2f}".format((curr_passed_testcase / total_testcases) * 100.00)
                print('percentage = ' + percentage)

                #Email to Candidate

                msgCandidate = ""
                if(float(percentage) > 75.0):    # Criteria is set to >= 75% (This is an example)
                    msgCandidate += success_msg() + percentage + ' %'
                else:
                    msgCandidate += failure_msg()
                send_email(sender(), token(), receiver(), 'REPORT', 'Your exam result', msgCandidate)

                #Email to HR

                msgHR = ""
                if(float(percentage) > 75.0):
                    msgHR += str(regNum) + "has cleared the online test with " + percentage + ' %'
                else:
                    msgHR += str(regNum) + " did not able to clear the test"
                send_email(sender(), token(), "abinashbiswal247@gmail.com", 'REPORT', 'Your exam result', msgHR)
            else:
                print('Already done!')
                # os.system('rm -R ./Admin/user_out')
            # os.system('rm -R ./Admin/user_out')
    return "job done!"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5001, debug = True)