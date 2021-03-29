import allure

import pytest

def  test_attach_text():

    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)



def test_attach_html():

    allure.attach("<body>这是一段htmlbody</body>","html模块",attachment_type=allure.attachment_type.HTML)


def test_attach_photo():
    allure.attach.file("E:/open_test/resource/cake.jpg",name="这是一个图片",attachment_type=allure.attachment_type.JPG)