 #!/usr/bin/python
 # -*- coding: utf-8 -*-
  
import argparse
import os
import pprint
from constant import CONSTANT
from devopshelper import OpsbotHelper

def init():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    templateFile =  open(dir_path+"/template/"+".opsbot.template", "r")
    templateText = templateFile.read()
    templateFile.close()

    devopsFile = open(CONSTANT.DEFAULT_OPSBOT_PLAN,"w+")
    devopsFile.write(templateText)
    devopsFile.close()

    print "File .opsbot created"
    print "Please open .opsbot file to write your devops plan."
    return 0

def build():    
    devopsFile = open(CONSTANT.DEFAULT_OPSBOT_PLAN,"r")
    lines = devopsFile.readlines()
    current_block = ""
    
    commands = []
    for line in lines:
        sline = line.strip()
        
        if (sline == "setting" or sline == "env" or sline == "user" or sline == "site"):
            current_block = sline
            commands.append({"command": "begin_block", "params":[current_block]})
        elif sline != "" and not sline.startswith("#"):
            params = sline.split(" ")
            commands.append({"command": current_block, "params":params})

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(commands)

    scriptblocks = []
    sh = ""
    opsbot = OpsbotHelper()
    for command in commands:
        functionName = "opsbot_" + command['command']
        method_to_call = getattr(opsbot, functionName)
        result = method_to_call(command['params'])
        if (result != ""):
            scriptblocks.append(result)
            #sh += result + "\n"

    #passwords.
    firstblock = opsbot.opsbot_account()
    sh = "\n".join([firstblock]+scriptblocks)

    #print sh

    cout = open(CONSTANT.DEFAULT_OUTPUT_BASH, "wb")
    cout.write(sh)
    cout.close()

    print "Build complete! "
    print "Type ./opsbot_generated.sh to run automatically devops "
    #begin run

    return 0

def main():
    parser = argparse.ArgumentParser(description=u'I\'m Opsbot. I can help you build the best devops scripts.')
    subparsers = parser.add_subparsers(help='Avaiable commands',  dest='command')

    subparsers.add_parser('init', help='Create .opsbot file, where you will write devops plan')

    build_parser = subparsers.add_parser('build', help='Build .opsbot file. export devops scripts')
    build_parser.add_argument('--output', '-o', help='The output bash script file path')

    PARSER = parser.parse_args()
    if PARSER.command == "init" :
        init()
    elif PARSER.command == "build":
        build()

if __name__ == "__main__":
    main()


