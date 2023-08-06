def bold(data):
    import re
    #print("inside bold: "+data)
    return re.sub(r'\*\*([\*\w\n\s.<>]*)\*\*',r'<b>\1</b>',data) #([\*\w\n\s.<>]*)

def italics(data):
    import re
    #print("inside italics"+data)
    return re.sub(r'//([<a-z>]*)([^http:][<>/\w\n]*)([/<a-z>]*)//',r'<i>\1\2\3</i>',data)

def underline(data):
    import re
    #print("inside underline"+data)
    return re.sub(r'__([<a-z>]*)(.*[\w\n]*)([/<a-z>]*)__',r'<u>\1\2\3</u>',data)

def strike(data):
    import re
    #print("inside underline"+data)
    return re.sub(r'\$\$([<a-z>]*)(.*[\w\n]*)([/<a-z>]*)\$\$',r'<strike>\1\2\3</strike>',data)

def newline(data):
    import re
    return re.sub(r'([^>{1}])\n',r'\1<br>\n',data)

def bullets(data):
    import re
    b = re.sub(r'^[^a-zA-Z0-9]*((\*\s.*[\w<>]+\n)+)',r'<ul>\n\1</ul>\n',data, flags = re.M)
    b = re.sub(r'^\*\s((.*[\w<>]+\n))',r'<li>\1</li>',b, flags = re.M)
    return b

def numbers(data):
    import re
    n = re.sub(r'^[^a-zA-Z0-9]*(([0-9]+.{1}\s{1}.*[\w<>]+\n)+)',r'<ol>\n\1</ol>\n',data, flags = re.M)   
    n = re.sub(r'^[0-9]+.\s{1}((.*[\w<>]+\n))',r'<li>\1</li>',n, flags = re.M)
    return n

def link(data):
    import re
    return re.sub(r'\[(\w+)\]\(([\w:/.]+)\)',r'<a href= "\2">\1</a>',data)

def space(data):
    import re
    return data.replace(" ", "&nbsp;")
