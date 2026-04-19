import cmd

class MyShell(cmd.Cmd):
    intro = "MyShell: Type help or ? to list commands.\n"
    prompt = "(myshell) "

    def do_hello(self, arg):
        print("Hello, world!")

    def do_exit(self, arg):
        print("Exiting...")
        return True

if __name__ == '__main__':
    MyShell().cmdloop()
```

Kodni ishga tushirish uchun Python skriptini ishga tushirib, `hello` va `exit` buyruqlarini kiritib ko'ring.
