class Https:
    def define_https(self, command):
        self.command = command
        self.start_https()

    def start_https(self):
        self.command.main.OS.system('clear')
        self.get_https_input()
        self.get_https_sample()
        self.change_https_sample()
        self.preview_https_conf()
        self.get_confirm_https_check()

    def get_https_input(self):
        self.HTTPS_FILENAME  = input("Masukkan nama file host (tanpa .conf) >>> ")
        self.HTTPS_ROOT      = input("Masukkan lokasi root website >>> ")
        self.HTTPS_DOMAIN    = input("Masukkan nama domain >>> ")
        self.SSL_FILE       = input("Masukkan nama file ssl >>> ")
        self.SSL_KEY        = input("Masukkan nama file ssl key >>> ")

    def get_https_sample(self):
        gethttpssample           = open("sample/Https.txt", 'r')
        self.GET_HTTPS_SAMPLE    = gethttpssample.read()
        gethttpssample.close()

    def change_https_sample(self):
        C1      = self.GET_HTTPS_SAMPLE.replace("#DIR#", self.command.main.SITE_DIR)
        C2      = C1.replace("#DOMAIN#", self.HTTPS_DOMAIN)
        C3      = C2.replace("#ROOT#", self.command.main.SITE_DIR + "/" + self.HTTPS_ROOT)
        C4      = C3.replace("#SSLFILE#", self.command.main.SSL_DIR + self.SSL_FILE)
        C5      = C4.replace("#SSLKEY#", self.command.main.SSL_DIR + self.SSL_KEY)
        self.SAMPLE_HTTPS_HAS_CHANGE = C5

    def preview_https_conf(self):
        self.command.main.OS.system('clear')
        self.CONFIRM_HTTPS = input(self.SAMPLE_HTTPS_HAS_CHANGE + '\n\nApakah data sudah benar? (y|n) >>> ')

    def get_confirm_https_check(self):
        if self.CONFIRM_HTTPS not in ('y', 'Y', 'n', 'N'):
            self.preview_https_conf()
        elif self.CONFIRM_HTTPS in ("y", "Y"):
            self.create_https_conf()
        else:
            self.start_https()

    def create_https_conf(self):
        self.command.main.shell(
            "echo '" + self.SAMPLE_HTTPS_HAS_CHANGE + "' >> tmp/" + self.HTTPS_FILENAME + ".conf" 
            + "&& sudo mv tmp/" + self.HTTPS_FILENAME + ".conf " + self.command.main.CONF_DIR 
            + " && sudo a2ensite " + self.HTTPS_FILENAME + ".conf && sudo nano /etc/hosts"
            )
        self.command.main.OS.system('clear')
        print('Berhasil!')
