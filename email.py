# Program to simulate Email message

# Created a class Email with four variables
# constructor created as per the requirements
class Email:

    def __init__(self, from_address, email_contents):
        self.from_address = from_address
        self.is_spam = False
        self.has_been_read = False
        self.email_contents = email_contents

    # created class methods to modify the class variables
    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True

    #  This special method is called by Python when you use the 'print' command on an object
    #  Overrides method in an object

    def __str__(self):
        output = f'Sender : {self.from_address} \n'
        output += f'Body : \n\t {self.email_contents}'
        return output


# Created the main function to handle the menu options
def main():

    # Initializing the list of email objects
    inbox = []

    # A block of code that returns the email contents of the list object for the provided index
    # and also has_been_read will be changed to True by calling mark_as_read method
    def get_email(list_number):
        if 0 < list_number <= len(inbox):
            requested_email = inbox[list_number - 1]
            requested_email.mark_as_read()
            contents = requested_email
        else:
            print("Invalid Index Provided")
            contents = ""
        return contents

    # A block of code that makes a new email object using email address and contents
    def add_email(sender, contents):
        new_email = Email(sender, contents)
        return new_email

    # A block of code that returns the number of emails in the inbox
    def get_count():
        return len(inbox)

    # A block of code that returns a list of emails that have not been read
    def get_unread_emails():
        count = 0
        unread_emails = []
        for index, email in enumerate(inbox, 1):
            if not email.has_been_read:
                unread_emails.append(email)
        return unread_emails

    # A block of code that returns a list of emails that have been marked as spam
    def get_spam_emails():
        spam_emails = []
        for index, email in enumerate(inbox, 1):
            if email.is_spam:
                spam_emails.append(email)
        return spam_emails

    # A block of code that deletes the email from the list of emails based on the user entered index
    def delete(index_input):
        for index, email in enumerate(inbox, 1):
            if index == index_input:
                inbox.remove(email)
                print(f'Deleted email \n {email}')
                break

    # Creating a variable to handle the user choices
    user_choice = ""

    # Using while loop to handle the user inputs for the menu
    while user_choice != "q":
        user_choice = input('''What would you like to do -
        c - count of all emails 
        r  - read
        ms - mark spam
        s  - send email
        ur - list unread emails
        sm - list spam emails
        d  - delete email
        q  - quit
        ? ''')

        # Using if/elif/else conditions to check the input choices and print the output
        # For user choice 'C', calling the get_count function and printing the number of messages
        if user_choice == "c":
            count_of_emails = get_count()
            print(f'Number of messages in the store :{count_of_emails}')

        # For user choice 'r', calling the get_email function by using user_input and printing the email
        elif user_choice == "r":
            # Eg: if user enters '1' ,then we will mark the email with index 0 as read
            user_input = int(input("Please enter the number in the email list to read:"))
            print(f'{get_email(user_input)}')

        # For user choice 'ms', calling the mark_as_spam class method to mark a email as spam based on the user_input
        elif user_choice == "ms":
            # Eg: if user enters '1' ,then we will mark the email with index 0 as spam
            user_input = int(input("Please enter the number of the email from the list to mark as spam:"))
            if 0 <= user_input-1 < len(inbox):
                inbox[user_input-1].mark_as_spam()
                print(f'Email that is marked as spam:{inbox[user_input-1]}')
            else:
                print("Invalid Index Provided")

        # For user choice 's', calling the add_email function to make a new email object
        elif user_choice == "s":
            input_sender = input("Provide the email id of the sender: ")
            input_content = input("Provide the message contents: ")
            inbox.append(add_email(input_sender,input_content))

        # For user choice 'ur', calling the get_unread_emails function and printing the unreadEmails
        elif user_choice == 'ur':
            unreadEmails = get_unread_emails()
            if len(unreadEmails) > 0:
                print('******** Unread Emails ********* ')
                for email in unreadEmails:
                    print(f'{email}')
                    print('**************************')
            else:
                print('No Unread emails.')

        # For user choice 'sm', calling the get_spam_emails function and printing the spamEmails
        elif user_choice == 'sm':
            spamEmails = get_spam_emails()
            if len(spamEmails) > 0:
                print('******** Spam Emails ********* ')
                for email in spamEmails:
                    print(f'{email}')
                    print('**************************')
            else:
                print('No Spam emails.')

        # For user choice 'd', calling the delete function that deleted the email based on the user_input
        elif user_choice == "d":
            # Eg: if user enters '1' ,then we will delete the email with index 0
            user_input = int(input("Please enter the number in the email list that you would like to delete:"))
            delete(user_input)

        # For user choice 'q', print 'Goodbye' and exit
        elif user_choice == "q":
            print("Goodbye")

        # if the user enters invalid input the prints a message
        else:
            print("Oops - incorrect input")


# Program starts here
main()
