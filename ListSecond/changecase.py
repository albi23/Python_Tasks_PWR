import os
import sys


def run_bash_script(path: str, direction: str):
    output_file_format = ",,"
    if direction in "-u":
        output_file_format = "^^"
    command = 'find ' + path + ' -type f  -exec bash -c ' \
                               '\'file_name=${1##*/};file_ext=${file_name##*\.};file_without_extension=${file_name%\.*};file_path=${1%\/*\.*};' \
                               'mv -T -v -i \"$1\" \"${file_path}/${file_without_extension' + output_file_format + '}.${file_ext}\"\' -- {} \;'
    print(os.popen(command).read())


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage : python changecase path -u/-l")
        print("        -l -> lower case,  -u -> upper case")
        exit(1)

    run_bash_script(sys.argv[1], sys.argv[2])
