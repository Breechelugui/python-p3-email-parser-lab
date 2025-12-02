import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string
    
    def parse(self):
        # Split by commas and/or spaces
        parts = re.split(r'[,\s]+', self.email_string)
        
        # Filter for valid email addresses using regex
        emails = [part for part in parts if re.match(r'^[^@]+@[^@]+\.[^@]+$', part)]
        
        # Return unique emails sorted alphabetically
        return sorted(list(set(emails)))