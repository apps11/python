import re
class validation :

    def mobvalidation(self , emob) :
        pattern = re.compile(r'\d{10}')
        if pattern.match(emob):
            return True
        else:
            print("Enter valid Mobile number")
            return False

    def emailvalidation(self , eemail) :
        pattern = re.compile(r'[\w.-]+@[\w.-]+')
        if pattern.match(eemail):
            return True
        else:
            print("Enter valid Email id")
            return False
