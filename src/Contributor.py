
class Contributor:

    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
    
    def improve_skill(self, skill_name):
        self.skills[skill_name]+=1

    def __str__(self):
        return self.name + "\n" + str(self.skills) + "\n"
