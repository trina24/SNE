import andgate
import nandgate
import orgate
import notgate

flag = True

while(True):
    gate = raw_input('Choose gate [AND/NAND/OR/NOT] or type Q to quit \n').lower()
    if (gate == 'and'):
        chosengate = andgate.And()
    elif (gate == 'nand'):
        chosengate = nandgate.Nand()
    elif (gate == 'or'):
        chosengate = orgate.Or()
    elif (gate == 'not'):
        chosengate = notgate.Not()
    elif (gate == 'q'):
        flag = False
        break
    else:
        continue
    vector = raw_input('Type input vector \n')
    vector = vector.split()
    vector = [int(i) for i in vector]
    vector.append(1)
    result = chosengate.neuron_function(vector)
    print 'Result: ' + str(result)
