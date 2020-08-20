class Remove:
    def define_remove(self, command):
        self.command = command
        self.start_remove()

    def start_remove(self):
        self.command.main.OS.system('clear')
        self.get_remove_filename()
        self.confirm_remove()
        self.get_remove_answer()
    
    def get_remove_filename(self):
        self.HOST_FILENAME = input("Masukkan nama host (tanpa .conf) >>> ")

    def confirm_remove(self):
        self.command.main.OS.system('clear')
        self.CONFIRM_REMOVE = input('Apakah anda yakin akan menghapus ' + self.HOST_FILENAME + ".conf?\n(y|n) >>> ")

    def get_remove_answer(self):
        if self.CONFIRM_REMOVE not in ('y', 'Y', 'n', 'N'):
            self.confirm_remove()
        elif self.CONFIRM_REMOVE in ('y', 'Y'):
            self.run_remove_host()
        else:
            self.start_remove()

    def run_remove_host(self):
        self.command.main.shell(
            "a2dissite " + self.HOST_FILENAME + ".conf "
            + "&& sudo systemctl restart apache2 "
            + "&& sudo rm " + self.command.main.CONF_DIR + self.HOST_FILENAME + ".conf "
            + "&& sudo nano /etc/hosts"
        )
        self.command.main.OS.system('clear')
        print("Berhasil!")