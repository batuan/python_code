#read file
import json

class FindYear:
    def maximumPopulation(self, logs) -> int:
        dates = []
        for _, birth, death in logs:
            dates.append((birth, 1)) # 1 mean this year a person is born
            dates.append((death, -1))# -1 mean this year, a person is dead, population decease by 1
            
        dates.sort() # we sort the data by year
    
        population = max_population = max_year = 0
        # iterate by all year and calculate the population by each row in dataset.
        for year, change in dates: #O(n)
            population += change
            if population > max_population:
                max_population = population
                max_year = year
        
        return max_year

    def maximum_population_by_count_population(self, logs):
        list_birth=[]
        list_death=[]
        for _, birth, dead in logs:
            list_birth.append(birth)
            list_death.append(dead)

        max_year = max(list_death)
        min_year= min(list_birth)
        population=[0]*(max_year-min_year+1) # mean the range of min_y, max_y
        
        #calculate number of population born and deadth each year
        for _, birth, death in logs: #O(n)
            population[birth-min_year] += 1
            population[death-min_year] -= 1

        max_population=population[0]
        max_year=min(list_birth)    

        #calculate number of population each year:
        for i in range(1, len(population)):
            population[i]+=population[i-1]
            if population[i] > max_population:
                max_population = population[i]
                max_year=i+min_year
        
        return max_year
    # complexity O(n): just iterate all data set


    def maximumPopulation_by_iterate(self, logs) -> int:
        list_birth=[]
        list_death=[]
        for _, birth, dead in logs:
            list_birth.append(birth)
            list_death.append(dead)
        min_y = min(list_birth)
        max_y = max(list_death)
        max_p=0
        year=0
        for i in range(min_y, max_y): #O(m)
            total=0
            for j in range(0,len(list_birth)): #O(n)
                if list_birth[j]<=i and list_death[j]>=i:
                    total+=1
            if total>max_p:
                max_p=total
                year=i
        return year
    # complexity: n*m
    # with n is size of data and m is size of (max_year-min_year)    

    def maximum_population_by_dict(self, data):
        dict_birth={}
        dict_death={}
        min_y=10000
        max_y=0
        #O(n)
        for _, birth, death in data: 
            if birth not in dict_birth.keys():
                dict_birth[birth]=1
            else:
                dict_birth[birth] +=1
            if death not in dict_death.keys():
                dict_death[death]=1
            else:
                dict_death[death] +=1

            if birth<min_y:
                min_y=birth
            if death>max_y:
                max_y=death
        population=year=max_p=0
        #O(m)
        for y in range(min_y, max_y):
            population = population + dict_birth.get(y, 0) - dict_death.get(y, 0)
            if population>max_p:
                year=y
                max_p=population
        return max_p, year
#the complexity is O(n+m) = O(n)

if __name__ == "__main__":
    #load file
    FILE_NAME='./data_small.json'
    file = open(FILE_NAME, 'r')
    data=json.loads(file.read())
    file.close()

    #solution
    solution = FindYear()
    print(solution.maximumPopulation(data))
    print(solution.maximumPopulation_by_iterate(data))
    print(solution.maximum_population_by_count_population(data))
    print(solution.maximum_population_by_dict(data)[1])
