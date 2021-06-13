#!/usr/local/bin/python3


from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE
import sys
app = FastAPI()

def runcommand (command):
    proc = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True,
                            universal_newlines=True)
    std_out, std_err = proc.communicate()
    return proc.returncode, std_out, std_err





@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/copy/{bucket_path:path}")
async def cpy(bucket_path: str ):
     copyfolderlist = ["SIM_INPUT", "job_history", "PRICING_INPUT", "AGGREGATION_INPUT", "PROTOBUF_TRADES", "AGGREGATION_OUTPUT/results_pb/", "PRICING_OUPUT"]
     listlength  = len(copyfolderlist)
     check='gsutil -q stat  gs://%s/' % (bucket_path)
     code, out, err = runcommand(check);
     print("Return code: {}".format(code));
     print("stdout:");print(out);
     print("stderr:");print(err);

     for i in range(listlength):
         print(copyfolderlist[i])
        #cmd = 'gsutil -m -o \"GSUTIL:parallel_thread_count=1\" -o \"GSUTIL:sliced_object_download_max_components=60\"  cp -r gs://%s/%s /%s' % (bucket_path, copyfolderlist[i], destination)
        #cmd = 'gsutil -m -o \"GSUTIL:parallel_process_count=1\" -o \"GSUTIL:sliced_object_download_max_components=60\"  cp -r gs://%s/%s /%s' % (bucket_path, copyfolderlist[i], destination)
        #cmd = 'gsutil cp -r gs://%s/%s /%s' % (bucket_path, copyfolderlist[i], destination)
        #cmd = 'gsutil cp -r gs://%s/ /%s' % (bucket_path,  destination)
         cmd = 'gsutil cp -r gs://%s/%s /Users/cwills/API-work/bucket-api/foo' % (bucket_path, copyfolderlist[i])
         subprocess.run(cmd, shell=True)
     return cmd 

