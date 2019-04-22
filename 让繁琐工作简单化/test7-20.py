# creat Regex,to match "num/num/num,"
import re
# testRegex = re.compile(r'\d\d|\d{1,3}(\,\d{1,3})+')
# testRegex = re.compile(r'\d|\d\d|\d\d\d\,(\d{2})?')
testRegex = re.compile(r'^(\d{1,3})(,\d{3})*$')
text = str(input())
mo = testRegex.findall(text)
print(mo)
