#This is budget calculator
def Budget(Net_Income,Gym,Food,Rent,Transport,Child):
    Surplus=Net_Income-Gym-Food-Rent-Transport-Child
    return(Surplus)

print(Budget(45000,700,2500,5000,2500,10000))