def convert(miles):
    in_km=miles*1.609344
    return in_km

miles=int(input("enter the miles you want to convert to km: "))
km=convert(miles)
print(km)