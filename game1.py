f = open('helloworld.html','w')

message = """<html>
<head></head>
<body><iframe src="https://scratch.mit.edu/projects/656775481/embed" allowtransparency="true" width="485" height="402" frameborder="0" scrolling="no" allowfullscreen></iframe></body>
</html>"""

f.write(message)
f.close()