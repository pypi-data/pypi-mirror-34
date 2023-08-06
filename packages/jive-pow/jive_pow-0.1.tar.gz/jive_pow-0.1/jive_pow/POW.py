from hashlib import sha256

def hash(x):
	device = sha256()
	device.update(str(x))
	return device.hexdigest()

def int_sum(a_hash):
	return sum([int(x) for x in a_hash if x < 'a'])

def nth_prime(n):
	primes = [1,2] ; i = 2; n = n
	while len(primes) < n:
		bad = False
		for j in primes:
			if i%j==0 and j>1:
				bad = True
				break
		if not bad:
			primes.append(i)
		i+=1
	return primes[-1]

def is_prime(x):
	primes = [1,2] ; i = 2
	while primes[-1] < x:
		bad = False
		for j in primes:
			if i%j==0 and j>1:
				bad = True
				break
		if not bad:
			primes.append(i)
		i+=1
	return x in primes

def proof_of_work(start,stop):
	counter = start; solns = 0
	while counter < stop:
		test_hash = hash(nth_prime(counter))
		hash_sum = int_sum(test_hash)
		if is_prime(hash_sum):
			solns+=1
		counter+=1
	return solns
