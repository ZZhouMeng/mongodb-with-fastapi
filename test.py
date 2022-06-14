import re

text = '[confidence:79]'
confidence = re.search('confidence:(?P<all>\d+)', text).group('all')
print(confidence)
