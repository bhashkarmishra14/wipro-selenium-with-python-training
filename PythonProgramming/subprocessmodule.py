# subprocess module
#execute external system command
#interact with OS processess
#capture output , error and return codes
#control the process execution
#run the OS level commands - linux , mac, windows
import subprocess
# subprocess.run() - run command and wait
#subprocess.Popen() - run process asynchronsly
#subprosse.PIPE - capture the output
#subprosse.CompleteProcess- result
#subprosse.TimeoutExpired - time out exception
#subprosse.CalledProcessorError- command failure
result = subprocess.run("dir" , shell = True , capture_output = True , text = True)
print(result)
result = subprocess.run("ipconfig" , shell = True , capture_output = True , text = True)
print(result)
result = subprocess.run("python --version" , shell = True , capture_output = True , text = True)
print(result)
#print(result.stderr)





