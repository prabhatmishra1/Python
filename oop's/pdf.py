import  pypandoc

con=pypandoc.convert_file('readme.md' ,'epub', outputfile= 'readme.epub')

assert con ==" "

print("conversation has been done")
