import smtplib
# import gmail
import imaplib
import os
import email 

userid="abhiram.natarajan@gmail.com"
passwd="Abhi5598$"
class Mail:
	def send_mail(self,From,to,subject,Message):
		# FROM = "abhiram.natarajan@gmail.com"
		# TO = "abhiram.natarajan@gmail.com"
		# SUBJECT = "TEST"
		# TEXT = "testing API calls"
		FROM=From
		TO=to
		SUBJECT=subject
		TEXT=Message
		# Prepare actual message
		message = """Subject: %s\n\n%s
		""" % ( SUBJECT, TEXT)
		try:
			server = smtplib.SMTP("smtp.gmail.com", 587)
			server.ehlo()
			server.starttls()
			server.login(userid, passwd)
			server.sendmail(FROM, TO, message)
			server.close()
			print('successfully sent the mail')
		except:
			print ("failed to send mail")

	def show_mails(self,query):
		
		SMTP_SERVER = "imap.gmail.com"
		SMTP_PORT   = 993
		mail = imaplib.IMAP4_SSL(SMTP_SERVER)
		mail.login(userid,passwd)
		
		# play with your gmail...
		x=mail.select('inbox')
		
		type, data = mail.search(None, 'ALL')
		mail_ids = data[0]
		

		id_list = mail_ids.split()   
		
		
		latest_email_id = int(id_list[-1])


		
		#last 5 emails shown, can be customised
		for i in range(latest_email_id,latest_email_id-10, -1):
			typ, data = mail.fetch(str(i), '(RFC822)' )
			message=""

			for response_part in data:
				k=''
				if isinstance(response_part, tuple):
					msg = email.message_from_string(response_part[1].decode())
					# print(msg)
					x=str(msg)
					# print(x)
					# input()
					for j in range(x.find("charset=\"UTF-8\""),x.find("--00",x.find("charset=\"UTF-8\""))):
						k+=x[j]
					
					k=k[17:]
					email_subject = msg['subject']
					email_from = msg['from']
					if email_from.find(query)!=-1 or email_subject.find(query)!=-1:
						message+='From : ' +str(email_from) + '\n'
						message+='Subject : ' + email_subject + '\n'
						message+="Message : "+k
						return message
					print('From : ' +str(email_from) + '\n')
					print ('Subject : ' + email_subject + '\n')
					# ch=input("press b to view body, any other key to continue")
					# if ch=='b':
					# 	if msg.is_multipart():
					# 		#display body only is b pressed
					# 		for payload in msg.get_payload():
								
					# 			print(payload.get_payload())
					# 	else:
					# 		print(msg.get_payload())

	def SendLatestMails(self):
		SMTP_SERVER = "imap.gmail.com"
		SMTP_PORT   = 993
		mail = imaplib.IMAP4_SSL(SMTP_SERVER)
		mail.login(userid,passwd)
		return_list=[]
		# play with your gmail...
		x=mail.select('inbox')
		response=''
		type, data = mail.search(None, 'ALL')
		mail_ids = data[0]
		

		id_list = mail_ids.split()   
		
		
		latest_email_id = int(id_list[-1])

		message=""
		
		#last 10 email shown, can be customised
		for i in range(latest_email_id,latest_email_id-40, -1):
			typ, data = mail.fetch(str(i), '(RFC822)' )
		

			for response_part in data:
				k=''
				if isinstance(response_part, tuple):
					msg = email.message_from_string(response_part[1].decode())
					x=str(msg)
					# print(x)
					# input()
					for j in range(x.find("charset=\"UTF-8\""),x.find("--00",x.find("charset=\"UTF-8\""))):
						k+=x[j]
					
					k=k[17:]
					email_subject = msg['subject']
					email_from = msg['from']
					# print('From : ' +str(email_from) + '\n')
					# message+='From : ' +str(email_from) + '\n'
					# print ('Subject : ' + email_subject + '\n')
					# message+='Subject : ' + email_subject + '\n'
					# email_from+="  "+email_subject
					# print("Message :"+k)
					message="Message :"+k
					obj=Mail()
					response=obj.classify(k)
					# Linux specific
					# os.system('echo  "\a"')
					# os.system('notify-send "Inbox: ' + email_from+'" -t 2000')
					return_list.append(email_from)
					return_list.append(email_subject)
					return_list.append(message)
					return_list.append(response)
					message=""
		return return_list
	def LatestMails(self):
		SMTP_SERVER = "imap.gmail.com"
		SMTP_PORT   = 993
		mail = imaplib.IMAP4_SSL(SMTP_SERVER)
		mail.login(userid,passwd)
		
		# play with your gmail...
		x=mail.select('inbox')
		
		type, data = mail.search(None, 'ALL')
		mail_ids = data[0]
		

		id_list = mail_ids.split()   
		
		
		latest_email_id = int(id_list[-1])

		message=""
		
		#last 1 email shown, can be customised
		for i in range(latest_email_id,latest_email_id-1, -1):
			typ, data = mail.fetch(str(i), '(RFC822)' )
		

			for response_part in data:
				k=''
				if isinstance(response_part, tuple):
					msg = email.message_from_string(response_part[1].decode())
					x=str(msg)
					# print(x)
					# input()
					for j in range(x.find("charset=\"UTF-8\""),x.find("--00",x.find("charset=\"UTF-8\""))):
						k+=x[j]
					
					k=k[17:]
					email_subject = msg['subject']
					email_from = msg['from']
					print('From : ' +str(email_from) + '\n')
					message+='From : ' +str(email_from) + '\n'
					print ('Subject : ' + email_subject + '\n')
					message+='Subject : ' + email_subject + '\n'
					email_from+="  "+email_subject
					print("Message :"+k)
					message+="Message :"+k
					obj=Mail()
					obj.classify(k)
					# Linux specific
					# os.system('echo  "\a"')
					# os.system('notify-send "Inbox: ' + email_from+'" -t 2000')
					return message
	def search_mail(self,from_a):
		SMTP_SERVER = "imap.gmail.com"
		SMTP_PORT   = 993
		mail = imaplib.IMAP4_SSL(SMTP_SERVER)
		mail.login(userid,passwd)
		
		# play with your gmail...
		x=mail.select('inbox')
		
		type, data = mail.search(None, 'ALL')
		mail_ids = data[0]
		

		id_list = mail_ids.split()   
		
		
		latest_email_id = int(id_list[-1])


		
		#last 50 emails searched for content, can be customised
		for i in range(latest_email_id,latest_email_id-50, -1):
			typ, data = mail.fetch(str(i), '(RFC822)' )
		

			for response_part in data:
				if isinstance(response_part, tuple):
					msg = email.message_from_string(response_part[1].decode())
					x=str(msg)
					# print(msg)
					# input()
					k=''
					email_subject = msg['subject']
					email_from = msg['from']
					if email_from.find(from_a.lower())>=0:
						
						for j in range(x.find("charset=\"UTF-8\""),x.find("--00",x.find("charset=\"UTF-8\""))):
							k+=x[j]
					
						k=k[17:]
						email_subject = msg['subject']
						email_from = msg['from']
						print('From : ' +str(email_from) + '\n')
						print ('Subject : ' + email_subject + '\n')
						email_from+="  "+email_subject
						print("Message :"+k)


	def classify(self,sentence, show_details=False):
		if sentence.find("love")>=0:
			# print ("%s \n classification: %s" % (sentence, [["love",0.924456185832424]]))
			# print("Respond normally. Dont push your luck too much.")
			return "\nResponse: Respond normally. Dont push your luck too much."
		elif sentence.find("surp")>=0 :
			# print ("%s \n classification: %s" % (sentence, ["surprise",0.951237812487172831]))
			# print("Respond carefully based on the content. If its a gradual movement carry on, else make sure to explain the reason behind the reciepient's surprise")
			return "\nResponse: Respond carefully based on the content. If its a gradual movement carry on, else make sure to explain the reason behind the reciepient's surprise"
		elif sentence.find("ang")>=0 or sentence.find("hate")>=0 or sentence.find("argh")>=0 :
			# print ("%s \n classification: %s" % (sentence, [["angry",0.91878324298328]]))
			# print("Respond apologetically. Be careful with your wordings to prevent any further arguments.")
			return "\nResponse: Respond apologetically. Be careful with your wordings to prevent any further arguments."
		elif sentence.find("fine")>=0 or sentence.find("okay")>=0 or sentence.find("doing")>=0 :
			# print ("%s \n classification: %s" % (sentence, [["worry",0.9487137812892]]))
			# print("Respond with how you feel right now. If everything is fine, reply positively so the reciepient doesn't get stressed out")
			return "\nResponse: Respond with how you feel right now. If everything is fine, reply positively so the reciepient doesn't get stressed out"
		elif sentence.find("yay")>=0 or sentence.find("happy")>=0 or sentence.find("wow")>=0 :
			# print ("%s \n classification: %s" % (sentence, [["happiness",0.988818781283721]]))
			# print("The reciepient seems happy. Keep up the conversation")
			return "\nResponse: The reciepient seems happy. Keep up the conversation"
		elif sentence.find("relief")>=0 or sentence.find("finally")>=0 or sentence.find("relieving")>=0 :
			# print("%s \n classification: %s" % (sentence, [["relief",0.9287418712381]]))
			# print(" Respond reassuringly, sympathize, or say that you were happy to help")
			return "\nResponse: Respond reassuringly, sympathize, or say that you were happy to help"
		elif sentence.find("welcome")>=0 or sentence.find("good morn")>=0 or sentence.find("how are you")>=0 or sentence.find("ello")>=0 or sentence.find("Hi")>=0 :
			# print ("%s \n classification: %s" % (sentence, [["greeting",0.9287418712381]]))
			# print("Respond with a greeting before getting into context. be very specific if this is a professional mail")
			return "\nResponse: Respond with a greeting before getting into context. be very specific if this is a professional mail"
		else:
			# print("%s \n classification: %s" % (sentence, [["neutral",0.82641274174123]]))
			# print("No emotion detected. respond casually")
			return "\nResponse: No emotion detected. respond casually"
# obj=Mail()
# # obj.send_mail("abhiram.natarajan@gmail.com","abhiram.natarajan@gmail.com","Yolo!@#","Testing lolol")
# obj.search_mail("jyothi")
