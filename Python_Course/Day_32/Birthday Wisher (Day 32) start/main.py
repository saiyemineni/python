import smtplib


my_mail = "saiyemineni321@gmail.com"
connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user= my_mail, password="Sa!duke321")
connection.sendmail(from_addr=my_mail, to_addrs="saiyemineni10@gmail.com", msg="Hello")

connection.close()