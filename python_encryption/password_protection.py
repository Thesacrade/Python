from zxcvbn import zxcvbn
from getpass import getpass 
import bcrypt   

def check_password_strength(password):
    result = zxcvbn(password)
    score = result['score']
    feedback = result['feedback']
    
    if score < 2:
        print("Password is weak. Consider using a stronger password.")
        if feedback['warning']:
            print("Warning:", feedback['warning'])
        if feedback['suggestions']:
            print("Suggestions:", ''.join(feedback['suggestions']))
    else:
        print("Password is strong.")

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt) 
    return hashed

def verify_password(password, hashed):
    password = getpass("Enter your password again to verify: ")   
    if bcrypt.checkpw(password.encode(), hashed):
        return "Password is correct, access granted"
    else:
        return "Wrong Password, Access Denied." 

if __name__ == "__main__":
    password = getpass("Enter a password to check its strength: ")
    check_password_strength(password)
    hashed_password = hash_password(password)
    print(verify_password(password, hashed_password))

    
