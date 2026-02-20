class Validator:

    @staticmethod
    def validate_email(email):
        if "@" in email and "." in email:
            return "Valid Email"
        return "Invalid Email"


print(Validator.validate_email("test@gmail.com"))
