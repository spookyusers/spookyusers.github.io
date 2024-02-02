# Birthday entry and lookup program. In progress.


birthdayquery = input("Who's birthday do you want to know? Use format 'firstnamelastname'.")

print(fam_member_info(birthdayquery))

class Family_member:
    def __init__(self,name,bday):
        self.name = name
        self.bday = bday
    def fam_member_info(self):
        print('Full name:',name)
        print('Birthday:',bday)

kymderriman = Family_member('Kym Derriman','July 14, 1986')
heatherderriman = Family_member('Heather Derriman, nea Kruchinsky','October 23, 1988')

