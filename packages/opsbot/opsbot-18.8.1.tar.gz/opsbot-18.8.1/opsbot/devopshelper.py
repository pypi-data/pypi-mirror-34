import os
import string
import random

class OpsbotHelper:
    current_dir = None
    target_os = "ubuntu"
    target_os_version = "18.04"
    password_length = 32

    user_passwords = {}

    def __init__(self):
        self.current_dir =  os.path.dirname(os.path.realpath(__file__))

    def opsbot_setting(self, params):
        field = params[0]
        value = params[1]
        #script = "#Set {field} = {value}".format(field = field, value = value)
        script= ""
        if field == "password_length": 
            self.password_length = int(value)
            script += "#set password_length = {}".format( self.password_length)
        elif field == "target_os_version":
            self.target_os_version = value
            script += "#check os version {}".format(self.target_os_version)
            if self.target_os_version not in ["16.10", "18.04"]:
                print "Build Fail!"
                print "{} version {} not support".format(self.target_os, self.target_os_version)
                quit()
        elif field =="target_os":
            self.target_os = value
            if  self.target_os != "ubuntu":
                print "Build Fail!"
                print "OS {} not support".format(self.target_os)
                quit()

        return script

    def opsbot_env(self, params):
        #print "env name"
        env_name = params[0]

        script =  "#install {}\n".format(env_name)
        envshFile = open("{}/template/env/{}.sh".format(self.current_dir, env_name))
        script += envshFile.read()+"\n"

        if(env_name == "lamp"):
            #TODO : gen password.
            #TODO: set password & auth-type
            self.user_passwords['root'] = {}
            self.user_passwords['root']['mysql'] = self.random_password()

            self.user_passwords['phpmyadmin'] = {}
            self.user_passwords['phpmyadmin']['mysql'] = self.random_password()


            if self.target_os_version == "18.04":
                script +=  "\n#Fix Mysql on ubuntu 18.04 . Change root auth type \n"
                fixFile = open("{}/template/fix/mysql-change-root-auth-type.sh".format(self.current_dir))
                script += fixFile.read() + "\n"
            
            if self.target_os_version == "18.04":
                script +=  "\n#Fix phpmyadmin on php72. Upgrade phpmyadmin to version 4.8 \n"
                fixFile = open("{}/template/fix/phpmyadmin-upgrade-48.sh".format(self.current_dir))
                script += fixFile.read() + "\n"
        
        return script +"\n"
    

    def random_password(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(self.password_length))

    def opsbot_account(self):
        script = """
#-----------------------------------------
# SAVE BELOW PASSWORDS & DELETE THIS FIlE AFTER JOB DONE!
# "SUDO -S" BEFORE RUN THIS SCRIPT.
#-----------------------------------------
"""

        for user in self.user_passwords:
            for service in self.user_passwords[user]:
                varname = "{}_{}_password".format(user, service)
                script += "{}=\"{}\"\n".format(varname, self.user_passwords[user][service])
        return script
    
    def opsbot_user_unix(self, username):
        script = "## account unix \n"
        f = open("{}/template/user/{}.sh".format(self.current_dir, "unix"))
        sh = f.read()
        return script + sh.format(username=username)     

    def opsbot_user_mysql(self, username, prefix):
        script = "## account mysql \n"
        f = open("{}/template/user/{}.sh".format(self.current_dir, "mysql"))
        sh = f.read()
        return script + sh.format(username=username, prefix=prefix)          

    def opsbot_user_mongodb(self, username, prefix):
        script = "## account mongodb \n"
        f = open("{}/template/user/{}.sh".format(self.current_dir, "mongodb"))
        sh = f.read()
        return script + sh.format(username=username, prefix=prefix)          


    def opsbot_user(self, params):
        username = params[0]
        script = "#create user {}\n".format(username)

        self.user_passwords[username] = {}
        self.user_passwords[username]['unix'] = self.random_password()
        script += self.opsbot_user_unix(username) + "\n"

        #TODO: parse param here
        mongo_enabled = False
        mysql_enabled = False
        database_prefix = username
        #print params
        for param in params:
            if param == "--mongodb" or param == "--mongo":
                mongo_enabled = True
            elif param == "--mysql":
                mysql_enabled = True
            elif str(param).startswith("--database-prefix="):
                database_prefix = str(param).split("=")[1]
        #print "mongo_enable {} mysql_enable {} database_prefix {}".format(mongo_enabled, mysql_enable, database_prefix)       

        if mysql_enabled:
            self.user_passwords[username]['mysql'] = self.random_password()
            script += self.opsbot_user_mysql(username, database_prefix) + "\n"

        if mongo_enabled:
            self.user_passwords[username]['mongodb'] = self.random_password()
            script+= self.opsbot_user_mongodb(username, database_prefix) + "\n"

        return script

    def opsbot_site(self, params):
        site = params[0]
        owner = params[1]
        path = "public_html"

        script = "#create site {}\n".format(site)

        f = open("{}/template/site/vhost.sh".format(self.current_dir))
        sh = f.read()
        f.close()
        script += sh.format(site=site, path=path)   +"\n" 

        f = open("{}/template/site/rule.sh".format(self.current_dir))
        sh = f.read()
        f.close()
        script += sh.format(site=site, owner=owner)  

        return script +"\n" 
        

    def opsbot_begin_block(self, params):
        #if params[0] == "setting":
        #    return ""
        script =  """#---------------------------------------------------
#  BEGIN {}
#---------------------------------------------------""".format(params[0])
        # if params[0] == 'env':
        #     script+= "\napt update\n"
        return script
