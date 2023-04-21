from parsons import MobilizeAmerica, Table
import logging

# Set the logger level
logging.basicConfig(level=logging.INFO)

# Create a MobilizeAmerica object by instantiating the class.
ma = MobilizeAmerica()
logging.info("The MobilizeAmerica object was created!")

# Set the parameters
org_id = '1076'
timeslot_start = '>= 2023-05-01 01:00:00AM'
timeslot_end = '<= 2025-05-01 01:00:00AM'
filename = 'events_may_2023.csv'

# Get events happening in May 2023 and onwards
logging.info(f"Getting events from {timeslot_start} onwards...")
events = ma.get_events(organization_id=org_id,
                       timeslot_start=timeslot_start,
                       timeslot_end=timeslot_end,
                       max_timeslots=0)

# Export events to CSV
logging.info("Exporting events to CSV...")
events.to_csv(filename)