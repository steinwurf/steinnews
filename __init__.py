import re


#file_in and file_out may be the same
def write_next_version(file_in, file_out):
    # Read in the file
    with open('NEWS.rst', 'r') as file :
      content = file.read()


    latest_sections = re.split(r'\d\.\d\.\d\n-+', content, flags = re.M)[0]

    #order in the 'or' clause is important - higher order comes first
    levelstr = re.fullmatch(r'.*(Major:|Minor:|Patch:).*', latest_sections, flags = re.M|re.DOTALL)[1]

    old_version = re.findall(r'(\d)\.(\d)\.(\d)\n-+', content, flags = re.M)[0] 
    
    #bump version
    version = {
        'Major:': old_version[0],
        'Minor:': old_version[1],
        'Patch:': old_version[2],
        }

    version[levelstr] = str(int(version[levelstr]) + 1)

    new_version_str = version['Major:'] + "." + version['Minor:'] + "." + version['Patch:']

    # Replace in the target text to write new version
    output = re.sub(r'(Latest\n-+\n)', r'\1* tbd\n\n' + new_version_str + '\n-------\n', content, flags = re.M)

    #content = re.sub(r'(Latest)', r'blablabla', content, flags = re.M)

    #print(content)

    # Write the file out again
    with open('output.rst', 'w') as file:
      file.write(output)


