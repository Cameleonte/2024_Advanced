guests_number = int(input())

vip = set()
regular = set()

for _ in range(guests_number):
    reservation_code = input()
    if reservation_code[0].isdigit():
        vip.add(reservation_code)
    else:
        regular.add(reservation_code)

guest_came = input()
arrived_guests = set()

while guest_came != 'END':
    arrived_guests.add(guest_came)
    guest_came = input()

list_guests = vip | regular
not_arrived = sorted(list_guests - arrived_guests)
print(len(not_arrived))
print(*not_arrived, sep='\n')
