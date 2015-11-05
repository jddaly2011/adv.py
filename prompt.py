import cmd

class Prompt(cmd.Cmd):
    """Simple command processor example."""
#    prompt = '\t> '
            
    def default(self, line):
        print 'default(%s)' % line
        return line
