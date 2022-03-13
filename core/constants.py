REQUESTED = 'REQUESTED'
ASSIGNED = 'ASSIGNED'
STARTED = 'STARTED'
IN_PROGRESS = 'IN_PROGRESS'
COMPLETED = 'COMPLETED'

TRIP_STATUS = ((REQUESTED, "Trip Requested"),
               (ASSIGNED, "Driver Assigned"),
               (STARTED, "Trip Started"),
               (IN_PROGRESS, "Trip In-progress"),
               (COMPLETED, "Trip Completed"))

AVAILABLE = 'AVAILABLE'
BUSY = 'BUSY'

USER_TRIP_STATUS = ((AVAILABLE, "Available for ride"),
                    (BUSY, "In Flight"))

DRIVER = 'DRIVER'
PASSENGER = 'PASSENGER'

USER_TYPE = ((DRIVER, "Driver"),
             (PASSENGER, "Passenger"))
