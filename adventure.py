
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    CEND      = '\33[0m'
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CBLINK2   = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'

    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'

    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m'

# https://pages.mtu.edu/~suits/notefreqs.html
class musicnotes:
    C0 = 16.35
    D0 = 18.35
    E0 = 20.60
    F0 = 21.83
    G0 = 24.50
    A0 = 27.50
    B0 = 30.87
    C1 = 32.70
    D1 = 36.71
    E1 = 41.20
    F1 = 43.65
    G1 = 49.00
    A1 = 55.00
    B1 = 61.74
    C2 = 65.41
    D2 = 73.42
    E2 = 82.41
    F2 = 87.31
    G2 = 98.00
    A2 = 110.00
    B2 = 123.47
    C3 = 130.81
    D3 = 146.83
    E3 = 164.81
    F3 = 174.61
    G3 = 196.00
    A3 = 220.00
    B3 = 246.94
    C4 = 261.63
    D4 = 293.66
    E4 = 329.63
    F4 = 349.23
    G4 = 392.00
    A4 = 440.00
    B4 = 493.88
    C5 = 523.25
    D5 = 587.33
    E5 = 659.25
    F5 = 698.46
    G5 = 783.99
    A5 = 880.00
    B5 = 987.77
    C6 = 1046.50
    D6 = 1174.66
    E6 = 1318.51
    F6 = 1396.91
    G6 = 1567.98
    A6 = 1760.00
    B6 = 1975.53
    C7 = 2093.00
    D7 = 2349.32
    E7 = 2637.02
    F7 = 2793.83
    G7 = 3135.96
    A7 = 3520.00
    B7 = 3951.07
    C8 = 4186.01
    D8 = 4698.63
    E8 = 5274.04
    F8 = 5587.65
    G8 = 6271.93
    A8 = 7040.00
    B8 = 7902.13

#https://en.wikipedia.org/wiki/Note_value
class notevalues:
    value = 1000
    breve = 2 * value
    semibreve = 1 * value
    minim = 0.5 * value
    crotchet = 0.25 * value
    quaver = (1/8) * value
    semiquaver = (1/16) * value
    demisemiquaver = (1/32) * value

class CharacterType(object):
    name = ''
    strengthBonus = 0
    enduranceBonus = 0
    dexterityBonus = 0
    wisdomBonus = 0
    inteligenceBonus = 0
    def __init__(self, name, strengthBonus, enduranceBonus, dexterityBonus, wisdomBonus, inteligenceBonus):
        self.name = name
        self.strengthBonus = strengthBonus
        self.enduranceBonus = enduranceBonus
        self.dexterityBonus = dexterityBonus
        self.wisdomBonus = wisdomBonus
        self.inteligenceBonus = inteligenceBonus

CharacterTypes = [
    CharacterType('Warrior', 10, 10, 10, 10, 10),
    CharacterType('Wizard', 10, 10, 10, 10, 10),
    CharacterType('Archer', 10, 10, 10, 10, 10),
    CharacterType('Rogue', 10, 10, 10, 10, 10),
]

class Character(object):
    name = ''
    characterType = ''
    strength = 0
    endurance = 0
    dexterity = 0
    wisdom = 0
    inteligence = 0

    def __init__(self, name, strength, endurance, dexterity, wisdom, inteligence):
        self.name = name
        self.strength = strength
        self.endurance = endurance
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.inteligence = inteligence
    def displayStats(self):
        print('strength : {0}'.format(self.strength))
        print('endurance : {0}'.format(self.endurance))
        print('dexterity : {0}'.format(self.dexterity))
        print('wisdom : {0}'.format(self.wisdom))
        print('inteligence : {0}'.format(self.inteligence))

def introduction():
    print(bcolors.CBLUEBG + 'Greeting in the * Adventure !!' + bcolors.ENDC)

def characterChoice():
    print('Please choose one the following Class:')
    for i in range(len(CharacterTypes)):
        print('{0} - {1}'.format(i + 1, CharacterTypes[i].name))
    while 1:
        choice = input('Enter choice number: ')
        try:
            choice = int(choice)
        except:
            print("--error-- please enter a valid choice:")
            continue
        else:
            if choice < 1 or choice > len(CharacterTypes):
                print("--error-- please enter a valid in range:")
                continue
            break
        break
    typeChoice = CharacterTypes[choice - 1]
    print(bcolors.OKGREEN + bcolors.BOLD + 'You choice the {0}!'.format(typeChoice.name) + bcolors.ENDC)
    return typeChoice

def enterName():
    name = input('Enter your champion name: ')
    print('Hello {0}{1}{2}!'.format(bcolors.OKGREEN, name, bcolors.ENDC))
    return name

class Room(object):
    left = ''
    rigth = ''
    up = ''
    down = ''
    content = []

    # def __init__(self):
    #     self.left = Room()
    #     self.rigth = Room()
    #     self.up = Room()
    #     self.down = Room()

    def __init__(self, left, right, up, down, content = []):
        self.left = left
        self.rigth = right
        self.up = up
        self.down = down
        self.content = content

class Inn():
    tender = ''
    shop = ''

class Dungeon():
    rooms = []

def generateDungeon():
    import random
    nbRooms = random.randint(2, 5) 
    print(nbRooms)

    i = 0
    while i < nbRooms:
        break

class npc():
    name = ''
    sex = ''

# import winsound
# winsound.Beep(int(musicnotes.F4), int(notevalues.crotchet))
# winsound.Beep(int(musicnotes.A4), int(notevalues.crotchet))
# winsound.Beep(int(musicnotes.B4), int(notevalues.minim))
# winsound.Beep(int(musicnotes.F4), int(notevalues.crotchet))
# winsound.Beep(int(musicnotes.A4), int(notevalues.crotchet))
# winsound.Beep(int(musicnotes.B4), int(notevalues.minim))

# winsound.Beep(int(musicnotes.F4), int(notevalues.crotchet))
# winsound.Beep(int(musicnotes.A4), int(notevalues.crotchet))
# winsound.Beep(int(musicnotes.B4), int(notevalues.crotchet))
# winsound.Beep(int(musicnotes.E5), int(notevalues.crotchet))
# winsound.Beep(int(musicnotes.B4), int(notevalues.minim))
# winsound.Beep(int(musicnotes.E4), int(notevalues.crotchet))
# winsound.Beep(int(musicnotes.D4), int(notevalues.crotchet))

# # winsound.Beep(int(musicnotes.E4), int(notevalues.crotchet))
# # winsound.Beep(int(musicnotes.G4), int(notevalues.crotchet))
# # winsound.Beep(int(musicnotes.C4), int(notevalues.semibreve))
# # winsound.Beep(int(musicnotes.B4), int(notevalues.semibreve))

# # winsound.Beep(int(musicnotes.C4), int(notevalues.semibreve))
# # winsound.Beep(int(musicnotes.C4), int(notevalues.semibreve))
# # winsound.Beep(int(musicnotes.C4), int(notevalues.semibreve))

generateDungeon()
introduction()
Character.name = enterName()
Character.characterType = characterChoice()
