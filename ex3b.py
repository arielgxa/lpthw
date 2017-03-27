# This script calculates the amount of money I will receive in the next Monash
# pay cycle.

# Declare hourly rates
hourly_2089 = 131.04 # Normal without doctoral qualifications or full subject co-ordination duties
hourly_2088 = 87.36 # Repeat without doctoral qualifications or full subject co-ordination duties
hourly_2091 = 43.68 # Marking - Standard

# Standard weekly working hours
weekly_2089_hours = 2
weekly_2088_hours = 2

# Number of tutorial weeks completed in this pay cycle
tutorial_weeks = 2

# Accrued marking hours
marking_hours = 0

# Payments
scholarship = 1007.62
tutoring = (
            tutorial_weeks * ((hourly_2089 * weekly_2089_hours) +
            (hourly_2088 * weekly_2088_hours)) +
            (hourly_2091 * marking_hours)
           )

# Calculate total
amount_to_receive = scholarship + tutoring

print "Scholarship:", scholarship
print "Tutoring:", tutoring
print "Total:", amount_to_receive

# Let's see if the changes get pushed to Git.
