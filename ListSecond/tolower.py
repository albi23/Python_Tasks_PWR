import os
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Missing input path directory ")
        exit(1)

    command = 'find ' + sys.argv[1] + ' -type f  -exec bash -c \'file_name=${1##*/};file_path=${1%\/*\.*};mv -T -v -i \"$1\" \"${file_path}/${file_name,,}\"\' -- {} \;'
    print(command)
    print(os.popen(command).read())
