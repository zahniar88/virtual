import os
from subprocess import call
from vendor.dotenv import load_dotenv
from app.Command import Command
from app.Http import Http
from app.Https import Https
from app.Remove import Remove

load_dotenv()

class Main(Command, Http, Https, Remove):
    def start_main(self):
        self.remove_tmp()
        self.CONF_DIR   = os.getenv('CONF_DIR') + "/"
        self.SSL_DIR    = os.getenv("SSL_DIR") + "/"
        self.SITE_DIR   = os.getenv("SITE_DIR")
        self.OS         = os
        self.define_command(self)

    def remove_tmp(self):
        os.system('rm tmp/*')

    def shell(self, cmd):
        call(
            'echo {} | sudo -S {}'.format(os.getenv('ROOT_PASSWORD'), cmd), 
            shell=True)

Main().start_main()