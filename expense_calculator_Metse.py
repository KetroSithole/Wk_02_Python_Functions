def house_expense(net_income,bond,elecricity,water,insurance,garden_service):
    surplus = net_income - bond - elecricity - water - insurance - garden_service
    return(surplus)

print(house_expense(20000,7500,850,1300,350,680))