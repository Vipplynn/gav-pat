class Patient:
    def __init__(self, first, middle, last, address, city, state, zip, number, name_emer, num_emer):
        self.first = first
        self.middle = middle
        self.last = last
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.number = number
        self.name_emer = name_emer
        self.num_emer = num_emer

    def set_first(self, first):
        self.first = first

    def set_middle(self, middle):
        self.middle = middle

    def set_last(self, last):
        self.last = last
    
    def set_address(self, address):
        self.address = address

    def set_city(self,city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_zip(self, zip):
        self.zip = zip
    
    def set_number(self, number):
        self.number = number

    def set_name_emer(self, name_emer):
        self.name_emer = name_emer

    def set_num_emer(self, num_emer):
        self.num_emer = num_emer


    def get_first(self):
        return self.first 

    def get_middle(self):
        return self.middle

    def get_last(self):
        return self.last
    
    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip(self):
        return self.zip
    
    def get_number(self):
        return self.number

    def get_name_emer(self):
        return self.name_emer 

    def get_num_emer(self):
        return self.num_emer

def main():
    pat1 = Patient('first', 'middle', 'last', 'address', 'city', 'state', 'zip', 'number', 'name_emer', 'num_emer')
    
    pat1.set_first('John')
    pat1.set_middle('Andrew')
    pat1.set_last('Smith')
    pat1.set_address('8231 Go Street')
    pat1.set_city('Vancouver')
    pat1.set_state('B.C.')
    pat1.set_zip('V73 T4R')
    pat1.set_number('(872)-092-7238')
    pat1.set_name_emer('Julia Smith')
    pat1.set_num_emer('(739)-938-8238')

    pro1 = Procedure('pro', 'date', 'prac', 'charge')
    pro2 = Procedure('pro', 'date', 'prac', 'charge')
    pro3 = Procedure('pro', 'date', 'prac', 'charge')

    pro1.set_pro('Physical Exam')
    pro1.set_date('2021-10-28')
    pro1.set_prac('Dr. Irvine')
    pro1.set_charge(int(250))

    pro2.set_pro('X-ray')
    pro2.set_date('2021-10-28')
    pro2.set_prac('Dr. Jamison')
    pro2.set_charge(int(500))
    
    pro3.set_pro('Blood test')
    pro3.set_date('2021-10-28')
    pro3.set_prac('Dr. Smith')
    pro3.set_charge(int(200))

    print("Patient:")
    print(f'{pat1.get_last()}, {pat1.get_first()} {pat1.get_middle()} ')
    print(f'{pat1.get_address()}, {pat1.get_city()}, {pat1.get_state()} | {pat1.get_zip()}')
    print(f'{pat1.get_number()}')
    print()
    print("Emergency Contact:")
    print(f'{pat1.name_emer} | {pat1.num_emer}')
    print()
    print("Procedures:")
    print()
    print(f'{pro1.get_pro()}, {pro1.get_date()}, {pro1.get_prac()}, {pro1.get_charge()}')


main()