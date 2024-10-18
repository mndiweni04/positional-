import Work
import School
from Work import WorkMem


class UserOccu():
    def Specify(self):
        Name = input("What is your name? ")
        Surname = input("What is your surname? ")
        uID = int(input("Please input your ID: "))
        uOccupa = input(f"{Name} {Surname} please enter your occupation: ")

        match uOccupa:
            case "employee":
                objWork = WorkMem(Name, Surname, uID, uOccupa)
                print(objWork.addNewMem())

        """        
        if uOccupa == "work":
            objWork = WorkMem(Name, Surname, uID, uOccupa)
            objWork.addNewMem()
            return "heyy"
        else:
            return "not worker"
        """



    def disPlayAMem(self):
        Name = ""
        Surname = ""
        uOccupa = ""

        uID = int(input("Enter desired user ID: "))
        objWork = WorkMem(Name, Surname, uID, uOccupa)
        print(objWork.displayMem(uID))

    def displayMembers(self):
        Name = ""
        Surname = ""
        uID = 0
        uOccupa = ""

        objWork = WorkMem(Name, Surname, uID, uOccupa)
        print(objWork.displayAllMem())



def main():
    obj = UserOccu()
    print(obj.Specify())
    print(obj.displayMembers())
    print(obj.disPlayAMem())


if __name__ == "__main__":
    main()