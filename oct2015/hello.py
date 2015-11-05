import cmd

class Prompt(cmd.Cmd):
    """Simple command processor example."""
    
    def precmd(self, line):
        print 'precmd(%s)' % line
        return (line)



if __name__ == '__main__':
    HelloWorld().cmdloop()
