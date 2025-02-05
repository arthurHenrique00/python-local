import multiprocessing

results = []

def calc_square(numbers):
    global results
    for i in numbers:
        print('square: ', str(i*i))
        results.append(i*i)
        print('within a result: ' + str(results))

if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr, ))
    p1.start()
    p1.join()
    print('result: '+str(results))
    print('Success')