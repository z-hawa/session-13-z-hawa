from collections import namedtuple


nycnamedtuple=namedtuple('NYCParkingTickets',['SummonsNumber', 'PlateID', 'RegistrationState', 'PlateType', 'IssueDate', 'ViolationCode', 'VehicleBodyType', 'VehicleMake', 'ViolationDescription'])


def add_columns_to_namedtuple(column):
    column=column.split(",")
    return nycnamedtuple(*column)





def return_namedtuple():
    with open("nyc_parking_tickets_extract-1.csv",errors='ignore',encoding='utf-8') as nycparkingtickets:
        next(nycparkingtickets)
        for i in nycparkingtickets:
            yield add_columns_to_namedtuple(i)


        
print(next(return_namedtuple()))
global dict_of_carmaker_violations
dict_of_carmaker_violations={}


def add_to_dict(column):
    column=column.split(",")
    num=dict_of_carmaker_violations.get(column[-2],0)
    num+=1
    dict_of_carmaker_violations.update({column[-2]:num})

def return_dict_of_violations():
    with open("nyc_parking_tickets_extract-1.csv",errors='ignore',encoding='utf-8') as nycparkingtickets:
        next(nycparkingtickets)
        for i in nycparkingtickets:
            add_to_dict(i)
        return dict_of_carmaker_violations

print(return_dict_of_violations())