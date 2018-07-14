from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Silverbot (object):

	def __init__(self, f_name = 'Undefined', l_name = 'Undefined', u_name = 'Undefined', passw = 'Undefined'):
		self.f_name = f_name
		self.l_name = l_name
		self.u_name = u_name
		self.passw = passw

	# Gmail signup automation
	def gBot(self):
		driver = webdriver.Firefox()
		driver.get("https://accounts.google.com/SignUp")
		time.sleep(1)

		# enter names
		driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(self.f_name)
		time.sleep(1)
		driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(self.l_name)
		time.sleep(1)

		# enter username
		driver.find_element_by_xpath('//*[@id="username"]').send_keys(self.u_name)
		time.sleep(1)

		# enter password and confirm
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/div/div[1]/input").send_keys(self.passw)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/div/div[1]/div/div[1]/input').send_keys(self.passw)
		time.sleep(1)

		# click submit button
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/content/span').click()
		time.sleep(1)
