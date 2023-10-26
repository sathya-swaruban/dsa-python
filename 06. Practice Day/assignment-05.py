# lex_auth_0127717001465856001076

class Train:
    def __init__(self, train_name, source, destination, passenger_capacity_per_compartment, passenger_goods_ratio):
        self.__train_name = train_name
        self.__source = source
        self.__destination = destination
        self.__passenger_capacity_per_compartment = passenger_capacity_per_compartment
        self.__passenger_goods_ratio = passenger_goods_ratio

    def get_train_name(self):
        return self.__train_name

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def get_passenger_capacity_per_compartment(self):
        return self.__passenger_capacity_per_compartment

    def get_passenger_goods_ratio(self):
        return self.__passenger_goods_ratio

    def __str__(self):
        return ('Train {} travels from {} to {} with a capacity of {} passenger per compartment and the passenger to '
                'goods ratio is {}.').format(
            self.__train_name,
            self.__source,
            self.__destination,
            self.__passenger_capacity_per_compartment,
            self.__passenger_goods_ratio
        )


if __name__ == '__main__':
    train1 = Train('Lokmanya', 'Bangalore', 'Mumbai', 60, 5)
    train2 = Train('Rajdhani', 'Mumbai', 'Chandigarh', 75, 5)
    print(train1)
    print(train2)
