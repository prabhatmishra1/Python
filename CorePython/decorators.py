# decorators with arguments in python
from functools import wraps

'''def  function1(function):
   def wrapper(*args,**kwargs):
        print("Hello")
        function(*args,**kwargs)
   return wrapper

@function1
def  function2(name,lastname):
     print("%s  %s" %(name,lastname))


function2("prabhat","mishra")'''


'''def smart_div(function):
      def inner(a,b):
          if a<b:
            a,b=b,a
            return function(a,b)
          else:
             return  function(a,b) 
      return inner   

@smart_div
def  div(a,b):
      print(a/b)
      
div(2,4)'''

def the_decorator(arg1, arg2):
    def _method_wrapper(view_method):
        

        def _arguments_wrapper( *args, **kwargs) :
            """
            Wrapper with arguments to invoke the method
            """
            print(ag1)
       
            #do something with arg1 and arg2

            return view_method( *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper

@the_decorator("an_argument", "another_argument")
def event_dashboard():
  print(event_dashboard())    
