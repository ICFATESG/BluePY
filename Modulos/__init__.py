#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from threading import Thread
from time import sleep
import bluePy
app = Flask(__name__)


class Th(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        #self.num = num


    def run(self):
        defo=False
        while defo==False:
            sleep(10)
            bluePy.varrer(bluePy)




a = Th(1)
a.start()

@app.route('/macs', methods=['GET'])
def get_tasks():
    return bluePy.mac

if __name__ == '__main__':
    app.run()
