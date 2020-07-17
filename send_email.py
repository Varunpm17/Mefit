#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:18:27 2020

@author: varunmeduri
"""
# Python code to illustrate Sending mail with attachments 
# from your Gmail account  
  
# libraries to be imported 
import os
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
   
fromaddr = "vpmeduri@gmail.com"
toaddr = "gauravmohan00@gmail.com"
   
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = fromaddr 
  
# storing the receivers email address  
msg['To'] = toaddr 
  
# storing the subject  
msg['Subject'] = "Daily MeFit Reports"
  
# string to store the body of the mail 
body = "Body_of_the_mail"
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent
rootdir = os.getcwd()
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file
        if file.endswith(".txt"):
            filename = file 
            print(file)
            attachment = open(filepath, "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
  
# To change the payload into encoded form  
  
# encode into base64 
            encoders.encode_base64(p) 
   
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
            msg.attach(p) 
  
        
        '''filename = file.split(".txt")[0]
        print(filename)
        for i in range(10):
            if filename == "report" + str(i):
                filepath = "/Users/varunmeduri/Desktop/MeFit/" + str(filename) + ".txt"
                attachment = open(filepath, "rb")
                print("Yes")
                '''
#filename = "report3.txt"
#attachment = open("/Users/varunmeduri/Desktop/MeFit/report3", "rb") 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(fromaddr, "Purnim@123") 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
  
# terminating the session 
s.quit()
