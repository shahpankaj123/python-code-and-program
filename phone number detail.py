import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number=input("enter your ph-number:")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print("Detail of your phone number:")
print(phone)
print(car)
print(time)
print(reg)
