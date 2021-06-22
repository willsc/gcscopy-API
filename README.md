# gcscopy-API

```
❯ uvicorn main:app --reload
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [24815] using statreload
INFO:     Started server process [24817]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

```

![image](https://user-images.githubusercontent.com/5571330/121816794-8afcdf00-cc75-11eb-8d7e-18e9d228ad12.png)


```
#!/usr/local/bin/python3


import os, sys
import stat

def  listfiles(path):

     filelist=[]

     dirs = os.listdir( path )
     for file in dirs:
         filelist.append(file)
     return(filelist)



def deltree(target):
    print("deltree", target)
    for d in os.listdir(target):
        try:
            deltree(target + '/' + d)
        except OSError:
            os.remove(target + '/' + d)

    os.rmdir(target)




if __name__ == '__main__':

     foo=listfiles('./foo2')
     print(foo)

     deltree('./foo2/foodir-2')
```
