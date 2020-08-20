class Command:
    def define_command(self, main):
        self.main = main
        self.start_command()

    def start_command(self):
        self.main.OS.system('clear')
        self.get_command_menu()
        self.get_command_menu()
        self.show_command_menu()
        self.get_command_selection()

    def get_command_menu(self):
        getmenu = open(self.main.CURRENT_DIR + 'sample/Menu.txt', 'r')
        self.GET_MENU = getmenu.read()
        getmenu.close()

    def show_command_menu(self):
        self.USER_SELECT_MENU = input(self.GET_MENU)

    def get_command_selection(self):
        if self.USER_SELECT_MENU not in ('1', '2', '3', '0'):
            self.start_command()
        elif self.USER_SELECT_MENU == "1":
            self.main.define_http(self)
        elif self.USER_SELECT_MENU == "2":
            self.main.define_https(self)
        elif self.USER_SELECT_MENU == "3":
            self.main.define_remove(self)
        else:
            self.main.OS.system("clear")
            print("Bye")
