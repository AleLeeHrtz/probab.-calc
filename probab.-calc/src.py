#arr = [16, 18, 20]

def cal(porcentaje, powpos, powneg, pascRow, position):
    porcentajeneg = 1 - porcentaje
    porcentaje = porcentaje ** powpos
    porcentajeneg = porcentajeneg ** powneg

    return porcentaje * porcentajeneg * pascRow[position]


def pascRow(n):
    row = [1]
    for i in range(n):
        row.append(row[i] * (n - i) / (i + 1))
    return row
def calWrapper(noOfTrueEvents, noOfTotalEvents):

    if noOfTrueEvents > noOfTotalEvents:
        print("Error. True events is bigger than total events.")
        return
    n = 5  # number of events
    sum = 0
    row = pascRow(noOfTotalEvents)
    for i in range(noOfTrueEvents):  # number of events being true
        sum = sum + cal(.25, i, noOfTotalEvents - i, row, i)

    print(sum)