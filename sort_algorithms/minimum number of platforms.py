class solution():
    def minimum(self , arr , dep):
        n = len(arr)
        trains  = []
        for i in range(n):
            trains.append((arr[i] , dep[i]))


        trains.sort()
        last_train = trains[0][1]
        count = 1
        print(last_train)

        ## id the last train > than the upcoming train , then just increment the platforms 
        # first arrival after the first train 
        print(trains)

        for i in range( 1, n):
            if last_train > trains[i][0]:

                count +=1
                last_train  = trains[i][1]

            else:  # no trains are interfering 
                last_train = trains[i][1]

        return count
    

        # print(trains)
        # print(last_train)
        # [900, 1235, 1100], dep[] = [1000, 1240, 1200]



class Sol:
    def minimum(self, arr, dep):
        n = len(arr)

        arr.sort()
        dep.sort()

        i = 1   # arrival pointer
        j = 0   # departure pointer

        platforms = 1
        max_platforms = 1

        while i < n and j < n:
            if arr[i] <= dep[j]:  # arrival before the departure 
                platforms += 1
                i += 1
            else:     # this implies that departure before the arrival 
                platforms -= 1
                j += 1

            max_platforms = max(max_platforms, platforms)

        return max_platforms

# solution().minimum([900, 940, 950, 1100, 1500, 1800] , [910, 1200, 1120, 1130, 1900, 2000])

print(solution().minimum([900, 940, 950, 1100, 1500, 1800] , [910, 1200, 1120, 1130, 1900, 2000]))

print(solution().minimum([900, 1235, 1100] , [1000, 1240, 1200]))
