hour = int(input("what's the time? "))
minute= int(input("what's the time? "))
second= int(input("what's the time? "))
hour2=int(input("what's the time? "))
minute2=int(input("what's the time? "))
second2 = int(input("what's the time? "))

totalhour=int((hour2-hour)*3600)
totalmin=int((minute2-minute)*60)
totalsec=int(second2-second)

print (totalhour+totalmin+totalsec)
