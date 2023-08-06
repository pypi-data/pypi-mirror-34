import os
import sys
import shutil
import fileinput
from CythonManager.conf import templates

def replaceAllInFile(file_, searchExp, replaceExp):
    for line in fileinput.input(file_, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp, replaceExp)
        sys.stdout.write(line)

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

def build():

    allowed_types = ('int', 'float', 'double', 'void')

    c_file = sys.argv[2]
    h_file = sys.argv[3]
    name = sys.argv[4]

    touch(str(name)+'.pxd')
    touch(str(name)+'.pyx')
    
    shutil.copy2(templates.__path__[0]+'/setup.py', 'setup.py')

    replaceAllInFile('setup.py', '{name}', str(name))

    with open(c_file) as file:
        c_lines = file.readlines()
        #c_lines = [x.strip() for x in c_lines]

    with open(h_file) as file:
        h_lines = file.readlines()
        h_lines = [x.strip() for x in h_lines]

    functions = []
    cython_funcs = []

    for line in h_lines:
        if line.startswith(allowed_types) and line.endswith(');'):
            line = line[:-1]
            functions.append(line)

    with open(str(name)+'.pxd', 'w') as file:
        file.write('cdef extern from '+'"'+c_file+'":'+'\n')

        for func in functions:
            func = func.split(' ')
            if not func[1].startswith('C_'):
                func[1] = 'C_'+func[1]
            func = ' '.join(func)
            file.write('    '+func+'\n')

    for func in functions:
        func = func.split(' ')
        type_ = func[0]
        
        if func[1].startswith("C_"):
            func[1] = func[1][2:]

        func[0] = 'cpdef'
            
        new_func = func[1:]

        for i in range(len(new_func)):
            for types in allowed_types:
                new_func[i] = new_func[i].replace(types, '')

        new_func = ' '.join(new_func)

        if not new_func.startswith('C_'):
            new_func = 'C_'+new_func

        if type_ != 'void':
            func_content = ':\n    return '+str(name)+'.'+new_func
        else:
            func_content = ':\n    '+str(name)+'.'+new_func

        func = ' '.join(func)+func_content
        cython_funcs.append(func)


    with open(str(name)+'.pyx', 'w') as file:
        file.write('cimport '+str(name)+'\n\n')

        for func in cython_funcs:
            file.write(func+'\n\n')

    with open(c_file, 'w') as file:
        for line in c_lines:
            if line.startswith(allowed_types):
                line = line.split(' ')
                if not line[1].startswith('C_'):
                    line [1] = 'C_'+line[1]
                line = ' '.join(line)

            if line != '\n':
                file.write(line+'\n')

    with open(h_file, 'w') as file:
        for line in h_lines:
            if line.startswith(allowed_types):
                line = line.split(' ')
                if not line[1].startswith('C_'):
                    line [1] = 'C_'+line[1]
                line = ' '.join(line)

            file.write(line + '\n')


