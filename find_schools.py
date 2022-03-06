import re
line1 = 'The George Washington University, Washington, DC, USA.'
line2 = 'Department of Pathology, University of Oklahoma Health Sciences Center, Oklahoma City, USA. adekunle-adesina@ouhsc.edu'

matchlist = ['Hospital','University','Institute','School','School','Academy'] # define all keywords that you need look up
p = re.compile('^(.?),\s+(.?),(.*?)\.')   # regex pattern to match

# We use a list comprehension using 'any' function to check if any of the item in the matchlist can be found in either group1 or group2 of the pattern match results
line1match = [m.group(1) if any(x in m.group(1) for x in matchlist) else m.group(2) for m in re.finditer(p,line1)]
line2match = [m.group(1) if any(x in m.group(1) for x in matchlist) else m.group(2) for m in re.finditer(p,line2)]

print (line1match)

print (line2match)