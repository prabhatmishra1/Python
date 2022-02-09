''' Find in between words '''
import re


s = 'abcdaRAMbcnmdaSHIYAbabcmp'

res = re.findall('^a[A-Z]b$',s)

print(res)