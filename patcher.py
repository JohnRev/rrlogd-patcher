#!/usr/bin/env python3
import re

infile = 'rrlogd'
outfile = 'rrlogd_patch'

with open(infile, "rb") as f:
   data = f.read()

data = bytearray(data);

patterns = [b"\xF2\x04\x03\xFF\xF7\x4B\xFF", b"\xF2\x04\x03\xFF\xF7\x45\xFF", b"\x33\x46\x4B\xA8\x10\x22"]
replaces = [b"\xF2\x04\x03\xE3\x20\x4B\xFF", b"\xF2\x04\x03\xE3\x20\x45\xFF", b"\x33\x46\x47\xA8\x10\x22"]

patterns1886 = [b"\x10\x22\x01\x21\x4B\xA8\xF8\xF7\xC0\xEA", b"\x01\x21\x4B\xA8\xF8\xF7\xA8\xEA\x01\xA8", b"\xFF\xF7\x44\xFF\x03\xAA\x31\x46\x38\x46"]
replaces1886 = [b"\x10\x22\x01\x21\x47\xA8\xF8\xF7\xC0\xEA", b"\x01\x21\x47\xA8\xF8\xF7\xA8\xEA\x01\xA8", b"\xAF\xF3\x00\x80\x03\xAA\x31\x46\x38\x46"]

patterns += patterns1886
replaces += replaces1886

matches = [0,0,0,0,0,0];
for i in range(len(patterns)):
   pattern = patterns[i]
   replace = bytearray(replaces[i])
   regex = re.compile(pattern)
   for match_obj in regex.finditer(data):
       matches[i] = matches[i]+1;
       offset = match_obj.start()
       print ("Original %08X: "%offset, ', '.join("%02X"%(ch) for ch in data[offset:offset+len(pattern)]))
       print ("Patched  %08X: "%offset, ', '.join("%02X"%(ch) for ch in replace))
       data[offset:offset+len(pattern)] = replace

success = ((matches[0] == 1 and matches[1] == 0) or (matches[0] == 0 and matches[1] == 1)) and matches[2] == 1
success1886 = matches[3]==1 and matches[4]==1 and matches[5]==1

if(success or success1886):
   print("Patch appears to be successful. Writing to outfile")
   with open(outfile, "wb") as f:
      f.write(data)
   print("The patched rrlogd has been written to %s" % outfile)
else:
  print("Patch has failed")
