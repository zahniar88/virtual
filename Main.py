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
        self.OS             = os
        self.CURRENT_DIR    = os.path.dirname(os.path.realpath(__file__)) + '/'
        self.remove_tmp()
        self.CONF_DIR       = os.getenv('CONF_DIR') + "/"
        self.SSL_DIR        = os.getenv("SSL_DIR") + "/"
        self.SITE_DIR       = os.getenv("SITE_DIR")
        self.define_command(self)

    def remove_tmp(self):
        os.system('rm ' + self.CURRENT_DIR + 'tmp/*.conf')

    def shell(self, cmd):
        call(
            'echo {} | sudo -S {}'.format(os.getenv('ROOT_PASSWORD'), cmd), 
            shell=True)

# checking file env
if os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/.env"):
    Main().start_main()
else:
    os.system('clear')
    print("File .env tidak ditemukan")
