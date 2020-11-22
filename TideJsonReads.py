import json

#Future James River tide variables 
def jTideReads(d,t): #days and tides should be in string format to be read correctly (e.g. d= 'd1', t ='h2')
    with open('jTide.json', 'r') as f:
        value = json.loads(f.read())
        tideTime = value[d+t]
        return tideTime



#Future Piankatank River tide variables 
def pTideReads(d,t): #days and tides should be in string format to be read correctly (e.g. d= 'd1', t ='h2')
    with open('pTide.json', 'r') as f:
        value = json.loads(f.read())
        tideTime = value[d+t]
        return tideTime



#Future York River tide variables 
def yTideReads(d,t): #days and tides should be in string format to be read correctly (e.g. d= 'd1', t ='h2')
    with open('yTide.json', 'r') as f:
        value = json.loads(f.read())
        tideTime = value[d+t]
        return tideTime



if __name__ == ('__main__'):
    print(jTideReads('d1', 'h2'))
    print(jTideReads('d3', 'h1'))
    print(jTideReads('d6', 'h2'))

