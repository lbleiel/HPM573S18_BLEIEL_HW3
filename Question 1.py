# Homework 3 - Question 1
# HPM 573

class Patient:

    def __init__(self, name):
        self.name = name

    def discharge(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes")


class EmergencyPatient(Patient):

    def __init__(self, name):
        Patient.__init__(self, name)
        self.expCost = 1000

    def discharge(self):
        print(self.name, "Emergency")


class HospitalizedPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)
        self.expCost = 2000

    def discharge(self):
        print(self.name, "Hospitalized")


class Hospital:
    def __init__(self):
        self.cost = 0
        self.patients = []

    def admit(self, patients):
        self.patients.append(patients)

    def discharge_all(self):
        for patients in self.patients:
            patients.discharge()
            self.cost += patients.expCost

    def get_total_cost(self):
        return(self.cost)

P1 = EmergencyPatient('P1')
P2 = EmergencyPatient('P2')
P3 = EmergencyPatient('P3')
P4 = HospitalizedPatient('P4')
P5 = HospitalizedPatient('P5')

YNHH = Hospital()
YNHH.admit(P1)
YNHH.admit(P2)
YNHH.admit(P3)
YNHH.admit(P4)
YNHH.admit(P5)

YNHH.discharge_all()
print(YNHH.get_total_cost())
