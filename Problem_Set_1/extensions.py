file_name= input('File name: ')
period_position=file_name.rfind('.')
extension=file_name[period_position:].lower().strip()

if extension == '.gif':
    result= 'image/gif'
elif extension == '.jpg' or  extension=='.jpeg':
    result= 'image/jpeg'
elif extension == '.png':
    result= 'image/png'
elif extension == '.pdf':
    result= 'application/pdf'
elif extension == '.txt':
    result= 'text/plain'
elif extension == '.zip':
    result= 'application/zip'
else:
 result = 'application/octet-stream'
##print(period_position)
##print(extension)
print (result)


