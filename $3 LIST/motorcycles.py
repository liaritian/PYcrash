motorcycles = ['honda' , 'yamaha' , 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

print(motorcycles)
pop_motor = motorcycles.pop()

print(motorcycles)
print(pop_motor)