#   A deep thought.
import sys

def main():
    """
    #   Description: Check if 42 or forty two is in inputted text
    
    """
    #   List of possible arguments
    Arg = ['42', 'forty two']

    #  Prompt user for input
    prompt = input("Check if 42 or forty two is in inputted text:").replace('-', ' ').lower()

    try:
        #   Ensure that this exist in prompted message
        if prompt.strip() not in Arg:
            raise Exception("No, 42 or forty two was not found in inputted text")

    except Exception as e:

        return sys.exit(f"{e}")

    return sys.exit("Yes, 42 or forty two was found in inputted text")


if __name__ == '__main__':

    main()
