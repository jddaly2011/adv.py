class Item(object):
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Thing(Item):
    def __init__(self, name, description, value, shortnames):
        self.shortnames = shortnames
        super(Thing, self).__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nShortnames:{}".format(self.name, self.description, self.value. self.shortnames)

class Pen(Thing):
    def __init__(self):
        super(Pen, self).__init__(name="A pen",
                                   description="It's a sweet pen that has 4 different colored inks.",
                                   value=10, 
                                   shortnames=['pen','biro'])

class USB(Thing):
    def __init__(self):
        super(USB, self).__init__(name="A USB stick",
                                   description="It's a USB stick in the shape of a slice of pizza.",
                                   value=10, 
                                   shortnames=['usb'])

class cake(Thing):
    def __init__(self):
        super(cake, self).__init__(name="A birthday cake",
                                   description="It's a bithday cake that says 'happy goddam birthday larry are you happy now?'",
                                   value=10, 
                                   shortnames=['cake'])


class id_badge(Thing):
    def __init__(self):
        super(id_badge, self).__init__(name="An ID badge",
                                   description="An ID Badge that says 'CYR CO/Larry Melman'",
                                   value=10, 
                                   shortnames=['id', 'badge'])







class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super(Weapon, self).__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Rock(Weapon):
    def __init__(self):
        super(Rock, self).__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super(Dagger,self).__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)


class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super(Gold, self).__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)
