
from flask import Flask, session, request


# import BluePrint
from Items.main import main

import json

@main.route('/askhelp', methods=['GET', 'POST'])
def askhelp():
    if request.method == 'GET':
      return "welcome to askfor_help"
    else:
      name = request.get_json()
      session['name'] = name

      print("name",name)
      print("session",session)
      
      # c = request.get_data()
      # d = json.loads(c.decode("utf-8"))
      # print("c",c)
      # print("d",d)

      return "receive name: " + name