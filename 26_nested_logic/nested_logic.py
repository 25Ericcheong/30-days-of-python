actual = input()
actual = list(map(int, actual.split(" ")))

expected = input()
expected = list(map(int, expected.split(" ")))

actualDate, actualMonth, actualYear = actual[0], actual[1], actual[2]

expectedDate, expectedMonth, expectedYear  = expected[0], expected[1], expected[2]

fine = 0

if actualYear > expectedYear:
    fine = 10000
elif actualYear == expectedYear: #Same calender year
    if actualMonth > expectedMonth: #checking months
        fine = 500 * (actualMonth - expectedMonth)
    elif actualMonth == expectedMonth: #check dates now
        if actualDate > expectedDate:
            fine = 15 * (actualDate - expectedDate)
print(fine)
