class UniModule:

    def __init__(self, code, name, year, credit, grade = None, PFP = None, discovery = None):
        self.code = code
        self.name = name
        self.year = year
        self.credit = credit

        if grade is None:
            self.grade = 0
        else:
            self.grade = grade

        if PFP is None:
            self.PFP = False
        else:
            self.PFP = PFP

        if discovery is None:
            self.discovery = False
        else:
            self.discovery = discovery

    def display_details(self):

        if self.PFP:
            Npfp = ""
        else:
            Npfp = "N"

        if self.discovery:
            Ndisc = ""
        else:
            Ndisc = "N"

        print("{}:Y{}:{}CR:{}GRD:{}PFP:{}Disc".format(self.code, self.year, self.credit, self.grade, Npfp, Ndisc))

class Transcript:

    def __init__(self):
        self.modules = []

    def add_module(self, item):
        if not isinstance(item, UniModule):
            print("expected item be an instance of UniModule.")
        elif item in self.modules:
            print("module already exists!")
        else:
            self.modules.append(item)

    def print_transcript(self):
        for item in self.modules:
            item.display_details()

COMP1012 = UniModule("COMP1011", "Intro to Prog.", 1, 10, grade=75, discovery=True)
COMP1121 = UniModule("COMP1121", "Databases", 1, 10, PFP=True)
COMP1211 = UniModule("COMP1211", "Comp. Arch.", 1, 10, grade=80, PFP=True)
t_student1 = Transcript()
t_student1.add_module(COMP1012)
t_student1.add_module(COMP1121)
t_student1.add_module(COMP1211)
t_student1.print_transcript()
        