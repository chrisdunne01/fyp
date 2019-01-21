from flask import Flask, render_template, request
import subprocess
import csv
import os
import schedule
from threading import Timer
import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import render_template
# from app import app
from forms import LoginForm


app = Flask(__name__)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)









# s = sched.scheduler(time.time, time.sleep)

# REMEMBER TO POST
@app.route('/')
def index():

    #test = subprocess.call(['./exec_cameraScan.py'])
	#output = subprocess.check_output(['./cameraScan.py'])
	#if 'success' in output:
	#	status = 'Device Connected'
	#ttl = output.split()[12].replace('ttl=', '')
	#time = output.split()[13].replace('time=','')
	#transmitted = output.split()[20]
	#recieved = output.split()[23]

	#subprocess.call(['/home/pi/NMS/monitor_temp.py'])
	#temperature = open("/home/pi/cpu_temp.csv", "r")
	#last_temperature = temperature.readlines()[-1]

    #

    # devicetype = request.form['devicetype']
    #
    # #output = subprocess.check_output(['python cameraScan.py', ipaddress])
    #
    # # if unsuccessfull output print cant connect and give user option to add
    # # else : add to csv file
    #
    # row = [ipaddress, devicetype]
    # print ipaddress, devicetype


    # with open('testfile.csv', 'a') as csvFile:
    #     writer = csv.writer(csvFile)
    #     writer.writerow(row)


    #    output = subprocess.check_output(['python', 'cameraScan.py', ipaddress])


    # this works
    # ipaddress = request.form['ipaddress']
    # devicetype = request.form['devicetype']
    # row = [ipaddress, devicetype]
    # with open('testfile.csv', 'a') as csvFile:
    #     writer = csv.writer(csvFile)
    #     writer.writerow(row)


    #
    # ipaddress = request.form['ipaddress']
    # devicetype = request.form['devicetype']
    #
    #
    # output = subprocess.check_output(['python', 'cameraScan.py', ipaddress])
    # print(output)
    #
    # ttl = output.split()[11].replace('ttl=', '')
    # time = output.split()[12].replace('time=','')
    # transmitted = output.split()[19]
    # recieved = output.split()[22]
    # connection = output.split()[33]
    # row = [ipaddress, connection, devicetype, ttl, time, transmitted, recieved]
    #
    #
    # if 'success' in output:
    #     with open('testfile.csv', 'a') as csvFile:
    #         writer = csv.writer(csvFile)
    #         writer.writerow(row)
    # else:
    #     print('CHRIS NOT A SUCCESS')
    #
    # with open('testfile.csv', 'r') as f:
    #     content = f.read()
    #     print('chris 0')
    #     for i in content:
    #         print i
        # reader = csv.reader(f, delimiter="\t")
        # for i in reader:
        #     print('chris 1')
        #
        #     print i[0]
        #     print('chris')

    with open('testing.csv', 'r') as f:
        content = f.read()
        test = content.split('\n')
        print(content)
        for x in test:
            # print(x)
            output = subprocess.check_output(['python', 'cameraScan.py', x])
            if 'success' in output:
                print('1testing',x)
                print('CHRIS HELP')

            elif 'Failed' in output:
                print('0testing', x)
                print('CHRIS HELP')


        # print('CHRISTOPHER',test)
        # print('chris 0')
        # for i in content:
        #     print i

    return render_template('index.html')

@app.route('/', methods=['Post'])
def index_post():
    ipaddress = request.form['ipaddress']
    devicetype = request.form['devicetype']

    row = [ipaddress, devicetype]
    with open('testfile.csv', 'ar') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)

    with open('testfile.csv', 'r') as f:
        content = f.read()
    return render_template('index.html', content=content)

# @app.route('/', methods=['Get'])
# def index_get():
#     with open('testfile.csv.csv', 'r') as f:
#         content = f.read()
#         print(content)
#         # test = content.split('\n')
#         # for x in test:
#         #     # print(x)
#         #     output = subprocess.check_output(['python', 'cameraScan.py', x])
#         #     if 'success' in output:
#         #         print('1testing',x)
#         #         print('CHRIS HELP')
#         #
#         #     elif 'Failed' in output:
#         #         print('0testing', x)
#         #         print('CHRIS HELP')
#
#
#     return render_template('index.html', content = content)
#



# @app.route('/', methods=['GET'])
# def reiterate():
#     with open('testing.csv', 'rw') as f:
#         content = f.read()
#         test = content.split('\n')
#         for x in test:
#             # print(x)
#             output = subprocess.check_output(['python', 'cameraScan.py', x])
#             if 'success' in output:
#                 print('1',x)
#                 print('CHRIS HELP')
#                 f.write("testing")
#                 status = "on"
#             elif 'Failed' in output:
#                 print('0', x)
#                 print('CHRIS HELP')
#                 status = "off"
#             return status
#
#
# schedule.every(1).minute.do(reiterate)


# @app.route('/', methods=['GET','POST'])
# def monitor():
#     with open('testfile.csv') as csvfile:
#         readCSV = csv.reader(csvfile, delimiter=',')
#         for row in readCSV:
#             print('CHRIS ', row[0])

@app.route('/deviceinfo', methods=['GET','POST'])
def index_test1():
    deviceinfo = subprocess.check_output(['./exec_deviceDetails.py'])
    return render_template('deviceinfo.html', deviceinfo=deviceinfo)
#
# @app.route('/', methods=['POST'])
# def getValue():
#     ipaddress = request.form['ipaddress']
#     devicetype = request.form['devicetype']
#     row = [ipaddress, devicetype]
#     with open('testfile.csv', 'a') as csvFile:
#         writer = csv.writer(csvFile)
#         writer.writerow(row)


@app.route('/portscan')
def portscanning_start():
    return render_template('portscan.html')

@app.route('/portscan', methods=['POST'])
def portscanning_FINSIH():
    ipaddress = request.form['ipaddress_portscan']
    ports = subprocess.check_output(['./portScan.py', ipaddress])
    return render_template('portscan.html', ports=ports )
#
@app.route('/upload')
def scripts():
    ls = subprocess.check_output(['ls', 'axis'])
    print(ls)
    list = ls.split('\n')
    print(list)
    # list = []
    #
    # list.append(test)
    # print(list)

    return render_template('scripts.html', list=list)

#
# @app.route('/upload')
# def upload_file():
#     return render_template('scripts.html')

@app.route('/upload', methods=['POST'])
def execute_files():
    for i in request.form:
        print('CHRISTOPHER THIS IS I',i)
        if i.startswith('comment.'):
            TEST = i.partition('.')[-1]
        # why = subprocess.check_output(['python ', TEST, ''])
        why = os.system('python /axis/' + TEST + '192.168.0.100 CHRISDUNNE')
        print('chris this is os', why)
        # TEST VARIABLE will be used to build the command
        # You need to get the parameters passing through and execute the command then
    return render_template('scripts.html')


    # id = request.form('')
    # https://stackoverflow.com/questions/32022568/get-value-of-a-form-input-by-id-python-flask

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
    # elif request.method == 'GET':
    #     ls = subprocess.check_output(['ls', 'axis'])
    #     print(ls)
    # return render_template('scripts.html', ls=ls)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

