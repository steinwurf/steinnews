import re


#file_in and file_out may be the same
def write_next_version(file_in, file_out):
    # Read in the file
    with open(file_in, 'r') as file :
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

    found = False
    for key in version:
        if found:
            #making sure to set lower tier version numbers to zero
            version[key] = '0'
        if key==levelstr:
            version[key] = str(int(version[key]) + 1)
            found = True;

    new_version_str = version['Major:'] + "." + version['Minor:'] + "." + version['Patch:']

    # Replace in the target text to write new version
    output = re.sub(r'(Latest\n-+\n)', r'\1* tbd\n\n' + new_version_str + '\n-------\n', content, flags = re.M)

    # Write the file out again
    with open(file_out, 'w') as file:
      file.write(output)


