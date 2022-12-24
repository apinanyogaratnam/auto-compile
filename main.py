import os
import sys

def main() -> None:
    arguments = sys.argv[1:]

    file_extension = None
    command = None
    clear = '--clear' in arguments or '-c' in arguments

    try:
        file_extension = arguments[0]
    except Exception as error:
        print('second argument must be a file extension')
        sys.exit(1)

    if not file_extension:
        print('no file extension specified')
        sys.exit(1)

    try:
        command = arguments[1]
    except Exception as error:
        print('third argument must be a command')
        sys.exit(1)

    if not command:
        print('third argument must be a command')
        sys.exit(1)

    path = os.path.abspath(os.getcwd())

    filelist = []
    for root, dirs, files in os.walk(path):
        for file in files:
            #append the file name to the list
            file_path = os.path.join(root,file)
            if '/.git/' not in file_path and file_path.endswith(file_extension):
                filelist.append(file_path)

    files = []
    #print all the file names
    for name in filelist:
        with open(name) as file:
            files.append(file.read())
        print(f'monitoring dir: {name}')

    # detecting file change
    while True:
        for i, name in enumerate(filelist):
            with open(name) as file:
                file_content = file.read()
                if files[i] == file_content:
                    continue

                if clear:
                    os.system('clear')

                print(f'detected change: {name}')
                os.system(command)
                files[i] = file_content


if __name__ == '__main__':
    main()
