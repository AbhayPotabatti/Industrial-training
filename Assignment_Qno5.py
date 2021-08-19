#Wrote program of train of 340m long is running at a speed of 45km/hr.
#What time will it take to cross a 160 mlong tunnel

train_lenght=340
tunnel_lenght=160
total=train_lenght + tunnel_lenght
speed=45
mps=5/18

#Calculating time to cross the tunnel
time=total/(45*mps)

print("Total time taken by train to cross the tunnel is ",time)
