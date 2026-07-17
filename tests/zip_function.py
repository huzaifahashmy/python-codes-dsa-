lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,10]

start = [1, 3, 0, 5, 8, 5]
end   = [2, 4, 6, 7, 9, 9]
list_zipped = list(zip(lst1, lst2 ))



class solution():
    def max_meetings(self , arr1 , arr2):

        meet=[]

        n = len(arr1)
        meetings = list(zip(arr1, arr2))
        meetings.sort(key=lambda x : x[1])
        # we have to sort out i=on the basis of the end time

        count = 1 
        last_meeting = meetings[0][1]

        for i in range(1 , n):
            if meetings[i][0] > last_meeting:

                
                # we are checking weather if the meetings are overlapping or not 
                # which in this case it is not 
                count +=1 
                last_meeting = meetings[i][1]


        return count
    
class mate:
    def maxMeetings(self, start, end):
        meetings = list(enumerate(zip(start, end), start=1))
        
        # (index, (start, end))
        meetings.sort(key=lambda x: x[1][1])
        
        result = [meetings[0][0]]

        # here the first meeting will always be held , as we have already sorted the array by its ending time of the meeting 

        last_end = meetings[0][1][1]
        
        for i in range(1, len(meetings)):
            if meetings[i][1][0] > last_end:
                result.append(meetings[i][0])
                last_end = meetings[i][1][1]
        
        return result

    


print(mate().maxMeetings(start= start , end= end))



