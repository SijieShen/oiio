#!/usr/bin/env python 

command += oiiotool ("src/bad.exr --fixnan black -o black.exr")
command += oiiotool ("src/bad.exr --fixnan box3 -o box3.exr")
command += info_command ("src/bad.exr", "--stats", safematch=True)
command += info_command ("black.exr", "--stats", safematch=True)
command += info_command ("box3.exr", "--stats", safematch=True)

# Outputs to check against references
outputs = [ "black.exr", "box3.exr", "out.txt" ]
