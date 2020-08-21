class Http:
    def define_http(self, command):
        self.command = command
        self.start_http()

    def start_http(self):
        self.command.main.OS.system('clear')
        self.get_http_input()
        self.get_http_sample()
        self.change_http_sample()
        self.preview_http_conf()
        self.get_confirm_http_check()

    def get_http_input(self):
        self.HTTP_FILENAME  = input("Masukkan nama file host (tanpa .conf) >>> ")
        self.HTTP_ROOT      = input("Masukkan lokasi root website >>> ")
        self.HTTP_DOMAIN    = input("Masukkan nama domain >>> ")

    def get_http_sample(self):
        gethttpsample           = open(self.command.main.CURRENT_DIR + "sample/Http.txt", 'r')
        self.GET_HTTP_SAMPLE    = gethttpsample.read()
        gethttpsample.close()

    def change_http_sample(self):
        C1      = self.GET_HTTP_SAMPLE.replace("#DIR#", self.command.main.SITE_DIR)
        C2      = C1.replace("#DOMAIN#", self.HTTP_DOMAIN)
        C3      = C2.replace("#ROOT#", self.command.main.SITE_DIR + "/" + self.HTTP_ROOT)
        self.SAMPLE_HTTP_HAS_CHANGE = C3

    def preview_http_conf(self):
        self.command.main.OS.system('clear')
        self.CONFIRM_HTTP = input(self.SAMPLE_HTTP_HAS_CHANGE + '\n\nApakah data sudah benar? (y|n) >>> ')

    def get_confirm_http_check(self):
        if self.CONFIRM_HTTP not in ('y', 'Y', 'n', 'N'):
            self.preview_http_conf()
        elif self.CONFIRM_HTTP in ("y", "Y"):
            self.create_http_conf()
        else:
            self.start_http()

    def create_http_conf(self):
        self.command.main.shell(
            "echo '" + self.SAMPLE_HTTP_HAS_CHANGE + "' >> " + self.command.main.CURRENT_DIR + "tmp/" + self.HTTP_FILENAME + ".conf" 
            + "&& sudo mv " + self.command.main.CURRENT_DIR + "tmp/" + self.HTTP_FILENAME + ".conf " + self.command.main.CONF_DIR 
            + " && sudo a2ensite " + self.HTTP_FILENAME + ".conf && sudo nano /etc/hosts"
            + "&& sudo systemctl restart apache2"
            )
        self.command.main.OS.system('clear')
        print('Berhasil!')
