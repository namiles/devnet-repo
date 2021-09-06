"""Model for aircraft flights."""


class Flight:

    def __init__(self, number):
        #using _ avoids name clash with the number method
        #by convention, implemenation details start with underscore
        if not number [:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'. Make sure airline code is capitalized.")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")
        self._number = number

    def number(self):
        return self._number
    
    def airline_code(self):
        return self._number[:2]


class Aircraft:
    
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration
    
    def model(self):
        return self._model

test_flight = Flight("SN876")
print(test_flight.number())
print(test_flight.airline_code())