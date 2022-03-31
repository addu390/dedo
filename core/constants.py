REQUESTED = 'REQUESTED'
ASSIGNED = 'ASSIGNED'
STARTED = 'STARTED'
IN_PROGRESS = 'IN_PROGRESS'
COMPLETED = 'COMPLETED'
DOCUMENT = 'DOCUMENT'
DRUG = 'DRUG'
OTHERS = 'OTHERS'

TRIP_STATUS = ((REQUESTED, "Trip Requested"),
               (ASSIGNED, "Driver Assigned"),
               (STARTED, "Trip Started"),
               (IN_PROGRESS, "Trip In-progress"),
               (COMPLETED, "Trip Completed"))

ITEM_TYPE = ((DOCUMENT, "Confidential"),
             (DRUG, "Prescribed Drugs"),
             (OTHERS, "Everything else"))

AVAILABLE = 'AVAILABLE'
BUSY = 'BUSY'

USER_TRIP_STATUS = ((AVAILABLE, "Available for ride"),
                    (BUSY, "In Flight"))

DRIVER = 'DRIVER'
CUSTOMER = 'CUSTOMER'

USER_TYPE = ((DRIVER, "Driver"),
             (CUSTOMER, "Customer"))
