class NPC:
    def __init__(self, name, description):
        self.name = name


class CFO(NPC):
    def __init__(self):
        NPC.__init__(self, name="CFO", description = "A large white rabbit wearing a top hat and waistcoat")
    
