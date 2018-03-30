import subprocess as s
import re
cmd = "ver"
#p = s.Popen(cmd,stdout=s.PIPE,stderr=s.PIPE,shell=True
p = s.Popen(["ver"],stdout=s.PIPE,stderr=s.PIPE,shell=False)

(out,err) = p.communicate()
#print("Output:")
#print(out)
m = re.search("\[Version (.*)\]",str(out))
#print(m.group())
version = m.group(1)
print("Version: %s"%version)
