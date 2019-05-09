w=[10, 7, 5, 18, 12, 20, 15]
M,total=35,0
solutionSet=[]
def findSubset(inputSet,total,M,solutionSet):
    if (total == M):
        print("Solution:",solutionSet)
    elif (total > M or len(inputSet) == 0):
        return
    else:
        solutionSet.append(inputSet[0])
        findSubset(inputSet[1:],total + inputSet[0],M,solutionSet)
        del solutionSet[-1]
        findSubset(inputSet[1:],total,M,solutionSet)
findSubset(w,total,M,solutionSet)

