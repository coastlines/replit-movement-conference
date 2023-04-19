from parsons import MobilizeAmerica

ma = MobilizeAmerica()

org_id = '1'

events = ma.get_events(org_id)

print(events)
