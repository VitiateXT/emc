import sys
import time

start = time.time()

print(r"""
███████╗███╗   ███╗ ██████╗
██╔════╝████╗ ████║██╔════╝
█████╗  ██╔████╔██║██║     
██╔══╝  ██║╚██╔╝██║██║     
███████╗██║ ╚═╝ ██║╚██████╗
╚══════╝╚═╝     ╚═╝ ╚═════╝
Export Markdown to Code//v0.1
""")

print('Time for Startup: ' + str(time.time() - start), 'seconds')

if len(sys.argv) != 2:
    print('\nUsage: emp.py <markdown_file>')
    sys.exit(1)

if not sys.argv[1].endswith('.md'):
    print('\nPlease provide a markdown file')
    sys.exit(1)

print('\nStandard language is Python')
print('\nIf you want to change the language, pless enter it in the next line or press Enter to continue with Python.')
language = input('\nEnter the language: ') or 'python' 

def find_code_block(markdown_file):
    code_blocks = []
    in_code_block = False
    first = True
    first_line = True
    for line in markdown_file:
        if (line.startswith('```' + language) and first) or (line.startswith('```') and not first):
            in_code_block = not in_code_block
            if first_line:
                print('\nFound code block for ' + language + ' in ' + sys.argv[1])
                first_line = False
            code_blocks.append('\n')
            if first:
                first = False
            else:
                first = True
            continue
        if in_code_block:
            code_blocks.append(line)
    return code_blocks

if language != 'python':
    extension = input('\nEnter the file extension: ') or language
    if extension.startswith('.'):
        extension = extension[1:]
    filename = (str(sys.argv[1]).split('.')[0] + '.' + extension)
else:
    filename = (str(sys.argv[1]).split('.')[0] + '.py')

outfile = open(filename, 'w')
print(f'\nSearching for {language} code blocks in {sys.argv[1]}')
outfile.writelines(find_code_block(open(str(sys.argv[1]), 'r')))
print(f'\nFile {filename} has been created')
outfile.close()
