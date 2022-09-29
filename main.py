import sys
from subprocess import Popen, PIPE, STDOUT

from capturing import Capturing

parent = "../5HQ1P/5HQ1P-Interpreter/"
sys.path.insert(1, parent)

from basic import Core
core = Core()

from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/compile-sq")
def hello(code: str = Form()):
  with Capturing() as output:
    result, error = core.run('<index.sq>', code)
  
  if error:
    return error.as_string()
  elif output:
    return output
  else:
      if len(result.elements) == 1:
          return(repr(result.elements[0]))
      else:
          return(repr(result))