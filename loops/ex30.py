#liste = [1,2,3,4] ->no need for that
#range() -> liste oluşturur

for i in  range(1,5,1): #range(start,stop,step)
    print(i)

rng = range(10) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] no start no step 
                #default values -> start 0 , step 1 

sonuc = list(rng)
print(sonuc)


for n in range(50,250):
     if(n % 2 == 0):
        print(n)