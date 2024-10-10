fo = open("foo.txt", "wb")
s=bytes("Python is a great language.r'\n Yeah its great!!\n","utf8");
type(s)
fo.write(s);

# Close opend file
fo.close()