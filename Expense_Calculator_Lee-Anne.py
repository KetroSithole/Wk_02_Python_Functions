def Hospital_Bills(Net_Income,vaccination,x_rays,cast,stitches,emergency_room_visit):
    Bill=Net_Income-vaccination-x_rays-cast-stitches-emergency_room_visit
    return(Bill)
print(Hospital_Bills(20000,1200,2500,800,500,800))
