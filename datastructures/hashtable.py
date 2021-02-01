# hashing: transforming a key to a memory address for fast storage and lookup of data.
# load factor: number of full / total capacity
# use load factor to find amount of probes possible for linear probing
# collision resolution:
# linear probing: find first place where 2 buckets clash then use...
#clash index + probe of each index % tablesize      to find next clash
# primary clustering is where duplicate key values are stored close together after a 
#linear probe
#secondary clustering is providing an offset between probe sequence, it is better if this
#is non-linear or a function of the key (double hashing, i*probe(key))
#quadratic probing is i**2 but beware despite the spread it can lead to infinite loop so
#need to detect if load factor > 50% because that's not good
# seperate chaining is using a linked list to store duplicate key values in same bucket
# hash tables are terrible for deletion but good for storage and deletion
# contents not stored in order so need to be sorted
# good for really large unordered datasets

