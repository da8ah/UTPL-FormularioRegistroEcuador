import re

def validar_correo(correo: str):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    is_valid = None

    if re.search(regex, correo):   
        is_valid = True   
    else:   
        is_valid = False  

    regex_edu = r'\b.edu\b' 

    is_educational = None

    if re.search(regex_edu, correo):
        is_educational = True
    else:
        is_educational = False 

    print(is_valid, is_educational)
 
#To validate uncomment and run the script
# def main():
#     validar_correo('afyaguana@utpl.edu.ec')

# if __name__ == '__main__':
#     main()