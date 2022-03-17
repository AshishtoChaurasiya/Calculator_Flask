#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
cal=Flask(__name__) #Flask Instance
@cal.route('/')
def Calculator():
    return render_template("D://Html//app.html")
@cal.route('/cal',methods=['POST'])
def operation_result():
    if(request.method=='POST'):
        First=request.form['Input1']
        Second=request.form['Input2']
        operation=request.form['operation']
        try:
            input1=int(First)
            input2=int(Second)
            
            # the operation on webpage is addition
#           #Through eval funtion less lines will be used. 
            a=str(input1)+str(operation)+str(input2)
            result=eval(a)
#            Through using Condtion line by line 
#             if operation == "+":
#                 result = input1 + input2
#             elif operation == "-":
#                 result = input1 - input2
#             elif operation == "*":
#                 result = input1 * input2
#             elif operation == "/":
#                 result = input1 / input2
#             elif operation == "%":
#                 result = input1 % input2
#             else:
#                 operation = "//"
#                 result = input1 // input2
            return render_template("D://Html//app.html",input1=input1,input2=input2,operation=operation,result=result)
        except ZeroDivisionError:
            return render_template("D://Html//app.html",input1=input1,input2=input2,operation=operation,result="Input number",error="You can't divide by zero")
if __name__ =="__main__":
    cal.run()


# In[ ]:





# In[ ]:




