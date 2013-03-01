'''
Created on Mar 1, 2013

@author: Kristoffer
'''
from collections import Counter
from time import time
import sys
import multiprocessing as MP
from IPython.parallel import Client

def factorize(n):
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors
        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            p += 2
        else:
            p += 1


if __name__ == "__main__":
    
    start = time()  
    if sys.argv[-1] == 's':
        unique_factors = [len({}.fromkeys(factorize(i)).keys()) for i in range(2, 500001) ]
        print dict(Counter(unique_factors))
    
    if sys.argv[-1] == 'm':
        pool = MP.Pool(processes=(MP.cpu_count()*2))
        factors = pool.map_async(factorize, xrange(2, 500001), chunksize=1000)
        print dict(Counter(map(lambda list_: len({}.fromkeys(list_).keys()), factors.get())))
        
    if sys.argv[-1] == 'i':
        try:
            client = Client()
        except IOError:
            sys.exit("IOError: Make sure to run 'ipcluster start -n 4' first")
        
        dview = client[:]
        @dview.parallel(block=True)
        def count_unique_factors(n):
            if n < 2:
                return []
            factors = []
            p = 2
    
            while True:
                if n == 1:
                    return len({}.fromkeys(factors).keys())
                r = n % p
                if r == 0:
                    factors.append(p)
                    n = n / p
                elif p * p >= n:
                    factors.append(n)
                    return len({}.fromkeys(factors).keys())
                elif p > 2:
                    p += 2
                else:
                    p += 1
            

        unique_factors = count_unique_factors.map(xrange(2, 500001))
        print dict(Counter(unique_factors))
        
            
    elapsed = time() - start
    print 'elapsed:', elapsed
