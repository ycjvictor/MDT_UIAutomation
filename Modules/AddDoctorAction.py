# -*- coding: utf-8 -*-
# @Time : 2020-07-15 11:08
# @Author : Yinchengjie
# @Email : yinchengjie@zhehekeji.com
# @File: AddDoctorAction.py
# @Project : MDT_UIAutomation
# @Software: PyCharm
import time
from selenium import webdriver
from pageObjects.AddDoctorPage import AddDoctorPage
from config.VarConfig import *
from util.SelectorUtils import SelectorUtils
from util.ParseConfigurationFile import ParseConfigFile
class AddDoctorAction(object):

    def __init__(self, driver):
        self.driver = driver
        self.AddDoctor = AddDoctorPage(self.driver)
        self.parseCF = ParseConfigFile()
        self.AddDoctorOptions = self.parseCF.getItemsSection('AddDoctorPage')

    def addDoctorAction(self,doctor_name,doctor_IdNumber,doctor_Number,doctor_phoneNumber,doctor_email,doctor_remarks):
        self.AddDoctor.doctorNameInput().send_keys(doctor_name)
        self.loginOptions['AddDoctorPage.usernameInput'.lower()].split('>')[1]
        SelectorUtils().selector_choose(self.driver,)




    def addDoctorAutoAction(self):
        i = 0
        while(i):
            self.AddDoctor.doctorNameInput().send_keys('Doctor'+i)
            SelectorUtils().selector_choose(self.driver,)







if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.get("http://47.96.183.143/#/pm/manage/project-list")
    browser.maximize_window()

    An = AnnouncementInterpretaionAction(browser)
    An.AnnouncementInterpretaionAction()