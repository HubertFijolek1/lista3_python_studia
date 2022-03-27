class Bus():
    #klasa, której atrybutem jest numer linii autobusowej
    bus_line_numbers = [1,2,3,4,5,6,7,8,9,10]

class Timetable():
    # zadaniem tej klasy jest pokazywanie rozkładów jazdy na dany
    # dzień. Powinna posiadać atrybuty takie jak nazwa przystanku, godzina odjazdu
    # autobusu. Można dokonać założenia z jaką częstotliwością jeździ dany autobus
    # np. co 10 minut. Format wyświetlanych danych [godzina:minuty]
    def __init__(self,bus_line_numbers):
        self.bus_numbers = bus_line_numbers
    def show_timetable(self,select_bus): 
        #zalozenie ze autobusy jezdzą co 15 minut
        if select_bus in self.bus_numbers:
            print(f"Bus number {select_bus} has the following timetable:")
            for i in range (24):
                for j in range(0,60,15):
                    if j == 0:
                        print(f'{i}:{j}0' , end = ", ")
                    else:
                        print(f'{i}:{j}' , end = ", ")
        else:
            print("There is no such bus")


class Passenger():
    # klasa, która “opisuje” pasażera linii autobusowej, pasażer ma
    # różne rodzaje ulgi. 
    discount_in_percent = {"blind" : 37,
                           "teacher" : 33,
                           "student" : 51,
                           "disabled child" : 78,
                           "soldier" : 77} 
    def print_it(self,person):
        if person in self.discount_in_percent.keys():
            print(f"The discount for the {person} is {self.discount_in_percent[person]}%")
        else:
            print('We do not have a discount for a given person')
    

class Ticket():
    # klasa, która “opisuje” ceny biletów - w zależności od ulgi Pasażera
    def __init__(self, discount_in_percent):
        self.discount = discount_in_percent

    def discounted_ticket_price(self,person,ticket_price = 3):
        if person in self.discount.keys():
            print(f'The ticket price for the {person} is {(ticket_price - ticket_price *  self.discount[person] * 0.01)}zł ')
        else:
            print('There is no discount for that person')
 
discount = Passenger()
discount.print_it('student')
print()

ticket_price = Ticket(discount.discount_in_percent)
ticket_price.discounted_ticket_price('blind')
print()

bus = Bus()
timetable = Timetable(bus.bus_line_numbers)
timetable.show_timetable(7)