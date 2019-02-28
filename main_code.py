
print(" This is a word based fighting mini game\n"
      "you would be able to fight with ACTION words like kick, punch, uppercut and shoot.\n"
      "the three main ENEMY in this game are 'ironman', 'batman' and 'spiderman'\n"
      "you need to fight them until they are all dead.\n"
      "to fight, you need to input the action and the enemy name EG 'punch ironman'.\n"
      "'punch ironman' would reduce the enemy's life by 1\n"
      "FIGHTING CODES ARE \n"
      "1. action enemy   ... note: there must be space in between the action and the enemy name.\n"
      "2. if you spell any word incorrectly, enemy would attack and your life would reduce by 2'\n"
      "3. if you did not write any word before pressing the enter key, enemy would attack\n"
      "and your life would be reduced by 2\n"
      "4. if you life reaches zero, Game over\n"
      "5. you can check your health by typing \n"
      "      examine health\n"
      "6. you can also check your enemy's health by typing\n"
      "      examine enemy name(spiderman or batman or ironman)\n"
      " you have a total of 20 lives, ironman = 10 lives, batman = 15 lives, spiderman = 20 lives\n"
      "7. To exit the Game, Type: 'close game'\n"
      "ENJOY THE GAME YOU CAN START.")

class GameObject:
    class_name = ""
    desc = ""
    objects = {}


    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc

    def close_game(self):
        return GameObject.objects[self.class_name].close()


class Health(GameObject):

    def __init__(self, name):
        self.class_name = "health"
        self.health = 20
        self._desc = "You are fine, your health is {}".format(self.health)
        super().__init__(name)

    @property
    def desc(self):
        health_line = ""
        list1 = [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]
        list2 =[21,22,23,24,25,26,27,28,29,30]
        list3 = [11,12,13,14,15,16,17,18,19,20]
        list4 = [1,2,3,4,5,6,7,8,9,10]
        if self.health >= 50:
            return self._desc
        elif self.health in list1:
            health_line = "You are getting weaker, your health is {}.".format(self.health)
        elif self.health in list2:
            health_line = "You are receiving some cruel punches.\nYour health is {}".format(self.health)
        elif self.health in list3:
            health_line = "they are kicking your 'ass'.\n Get your self together and get back to the game\n your " \
                          "health is {}".format(self.health)
        elif self.health in list4:
            health_line = "You are about to die.\n Do you want to end your life like this?\n Your life is{}".format(self.health)
        elif self.health <= 0:
            health_line = "You are dead."
        return  health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


health = Health("my_health")


class IronMan(GameObject):

    def __init__(self, name):
        self.class_name = "ironman"
        self.health = 10

        self._desc = "A very strong man, he can crush you with his fist."
        super().__init__(name)

    @property
    def desc(self):
        health_line = ""

        if self.health >= 10:
            return self._desc
        elif self.health == 7:
            health_line = "Yea keep hitting him hard. He is getting weaker.health {}".format(self.health)
        elif self.health == 6:
            health_line = "Yea keep hitting him hard. He is getting weaker.health {}".format(self.health)
        elif self.health == 5 or self.health == 4 or self.health == 3:
            health_line = "The irons are falling off .. coomon! uppercut! health {}".format(self.health)
        elif self.health == 2 or self.health == 1:
            health_line = "about to die.health {}".format(self.health)
        elif self.health <= 0:
            health_line = "Iron man is dead \n Good Job."
        return  health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


ironman = IronMan("iron")


class SpiderMan(GameObject):

    def __init__(self, name):
        self.class_name = "spiderman"
        self.health = 15


        self._desc = "A very flexible man He can capture you with his Web."
        super().__init__(name)

    @property
    def desc(self):
        health_line = ""

        if self.health >= 15:
            return self._desc
        elif self.health == 7:
            health_line = "Yea keep hitting him hard. He is getting weaker.health {}".format(self.health)
        elif self.health == 6:
            health_line = "Yea keep hitting him hard. He is getting weaker.health {}".format(self.health)
        elif self.health == 5 or self.health == 4 or self.health == 3:
            health_line = "spider man's health is low .. coomon! uppercut! health {}".format(self.health)
        elif self.health == 2 or self.health == 1:
            health_line = "about to die. health {}".format(self.health)
        elif self.health <= 0:
            health_line = "spider man is dead \n Good Job."
        return health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


spiderman = SpiderMan("spider")

class BatMan(GameObject):

    def __init__(self, name):
        self.class_name = "batman"
        self.health = 20


        self._desc = "A very strong man dresses like a bat."
        super().__init__(name)


    @property
    def desc(self):
        health_line = ""
        if self.health >= 18:
            return self._desc
        elif self.health == 7:
            health_line = "Yea keep hitting him hard. He is getting weaker.health {}".format(self.health)
        elif self.health == 6:
            health_line = "Yea keep hitting him hard. He is getting weaker.health {}".format(self.health)
        elif self.health == 5 or self.health == 4 or self.health == 3:
            health_line = "His costumes are falling off .. coomon! uppercut!health {}".format(self.health)
        elif self.health == 2 or self.health == 1:
            health_line = "about to die.health {}".format(self.health)
        elif self.health <= 0:
            health_line = "Iron man is dead \n Good Job."
        return health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


batman = BatMan("bat")

class Game(GameObject):
    def __init__(self, name):
        self.class_name = "game"
        super().__init__(name)

    def close(self):
        exit()

game = Game("game")


def punch(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Health or type(thing) == IronMan or type(thing) == SpiderMan or type(thing) == BatMan:
            thing.health -= 1
            if thing.health <= 0:
                msg = "You killed the {}!".format(thing.class_name)
            else:
                msg = "You Punched the {}".format(thing.class_name)
    else:
        msg = "There is no {} here.".format(noun)
    return msg


def uppercut(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Health or type(thing) == IronMan or type(thing) == SpiderMan or type(thing) == BatMan:
            thing.health -= 2
            if thing.health <= 0:
                msg = "You killed the {}!".format(thing.class_name)
            else:
                msg = "You gave {} an strong uppercut".format(thing.class_name)
    else:
        msg = "There is no {} here.".format(noun)
    return msg


def kick(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Health or type(thing) == IronMan or type(thing) == SpiderMan or type(thing) == BatMan:
            thing.health -= 2
            if thing.health <= 0:
                msg = "You killed the {}!".format(thing.class_name)
            else:
                msg = "You kicked the {}".format(thing.class_name)
    else:
        msg = "There is no {} here.".format(noun)
    return msg

def shoot (noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Health or type(thing) == IronMan or type(thing) == SpiderMan or type(thing) == BatMan:
            thing.health -= 3
            if thing.health <= 0:
                msg = "You killed the {}!".format(thing.class_name)
            else:
                msg = "You shot the {}".format(thing.class_name)
    else:
        msg = "There is no {} here.".format(noun)
    return msg


def wound(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Health:
            thing.health -= 2
            if thing.health <= 0:
                print("You have been killed by the enemy")
                exit()


def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here.".format(noun)

def close(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].close_game()
    else:
        return "There is no {} here.".format(noun)


def get_input():
    wlist = ["examine", "punch", "kick", "uppercut", "shoot", "close"]
    wlist2 = ["ironman", "health", "batman", "spiderman", "game"]
    command = input(": ").split()
    if not command :
        print("you have been hit by the enemy")
        wound("health")
        get_input()
    elif len(command) == 1:
        print("you have been hit by the enemy")
        wound("health")
        get_input()
    elif len(command) == 1 and command[0] not in wlist:
        print("you have been hit by the enemy")
        wound("health")
        get_input()
    elif len(command) >= 3:
        print("you have been hit by the enemy")
        wound("health")
        get_input()
    elif len(command) == 2 and command[0] not in wlist or command[1] not in wlist2:
        print("You have been hit by the enemy")
        wound("health")
        get_input()
    else:
        verb_word = command[0]
        if verb_word in verb_dict:
            verb = verb_dict[verb_word]

    # initial input
    #  if there exist the first word is in the caller tuple Verb_dict... this contain a caller to the functions.

        else:
            print("unknown verb{} ".format(verb_word))
            return
    # else print unknown verb plus the wrong caller...(first word)

        if len(command) >= 2:
            noun_word = command[1]
            print(verb(noun_word))
    # if there are more than one word in the input, then this would activate.

        else:
            print(verb("nothing"))







verb_dict = {
    "examine": examine,
    "punch": punch,
    "kick": kick,
    "uppercut": uppercut,
    "shoot": shoot,
    "close": close

}

while True:
    get_input()