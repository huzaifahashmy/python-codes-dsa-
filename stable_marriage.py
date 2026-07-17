class Solution:
    def stableMarriage(self, men, women):
        n = len(men)

        wife = [-1] * n
        husband = [-1] * n
        next_choice = [0] * n

        # ranking for women
        rank = []
        for w in range(n):
            r = {}
            for i, m in enumerate(women[w]):
                r[m] = i
            rank.append(r)

        free_men = list(range(n))  # only track free men

        #we are using a queue to track free (stack would also work, but queue is more intuitive here)
        # stack like appraoch we have used 


        while free_men:
            m = free_men.pop(0)

            w = men[m][next_choice[m]]
            next_choice[m] += 1
            # if the woman is free, then we can match them
            if husband[w] == -1:
                husband[w] = m
                wife[m] = w
            else:
                # else we need to check if the ranking of the current husband is better than the new one
                current = husband[w]

                if rank[w][m] < rank[w][current]:
                    husband[w] = m
                    wife[m] = w

                    wife[current] = -1
                    free_men.append(current)
                else:

                    # else she refuses the new proposal
                    
                    free_men.append(m)

        return wife