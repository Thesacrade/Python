from zxcvbn import zxcvbn

def check_password_strength(password):
    result = zxcvbn(password)
    score = result['score']
    feedback = result['feedback']
    
    if score < 2:
        print("Password is weak. Consider using a stronger password.")
        if feedback['warning']:
            print("Warning:", feedback['warning'])
        if feedback['suggestions']:
            print("Suggestions:", " ".join(feedback['suggestions']))
    else:
        print("Password is strong.")

if __name__ == "__main__":
    password = input("Enter a pasword to check its strength: ")
    check_password_strength(password)
    
