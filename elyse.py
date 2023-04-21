from parsons import MobilizeAmerica, Table

ma = MobilizeAmerica()

print("Pulling events!")

org_id = '1'

events = [ma.get_events(org_id)]

print(events)
