Cracking the coding interviews
===
# TODO
- [ ] [Technical tips](https://medium.freecodecamp.org/coding-interviews-for-dummies-5e048933b82b)
- [ ] [Other](https://medium.com/@nickciubotariu/ace-the-coding-interview-every-time-d169ce1fd3fc)
- [ ] [Top 10 questions per topic](https://www.geeksforgeeks.org/top-10-algorithms-in-interview-questions/)

# Interview tips

1. Ask questions about the problem to clarify it.
2. DON'T JUMP INTO THE CODE, **THINK AND DISCUSS**.
3. Don't stay muted for a while, clarify when you are thinking, "Can I think for a second?".
4. Think out loud.
5. Multiply the examples.
6. Ask for approval before coding, "Does it seem like a good strategy ?" "Should I start coding ?"

# Reflexes
1. Can **sorting** input data help me ?
2. Can **splitting** input data help me ? 
3. Can a **dictionary** help me ?
4. Can **multiple pointers** help me ?
5. Can a **frequency array** help me ?
6. Can **multiple pass** help me ?
7. Can **case-based reasoning** help me ?
8. Is there an **end** property ?

# Tricks
* Checking if $i \in Stack$ in $O(1)$: just keep updated a **is_in-array** `is_in_stack` where `is_in_stack[i]` tells whether $i \in Stack$.
* Sets with fewer than 64 possible items can be coded as integers. 
* For singly linked lists, creating **2 pointers** $n$ nodes apart may be handy. It is also applicable to every sequence of elements. (find the middle / $n^{th}$ from the end, a cycle...)
* Use **infinite boundaries** `float('inf')` or`math.inf`.
* Use **frequency arrays** when counting letters. A **counting sort** might also prove useful (as it is linear for frequencies) later on. 
* To find $a$ and $b$ in a array so that $a+b = c$, save every seen number in a set $S$ and for every new $i$, check if $c-i \in S$.

# Properties to look for
* **Sorted** &#10140; *Bisection search*.

* **iterative DFS** &#10140; stack

* **BFS** &#10140; queue
  * Need to keep track of the depth? &#8594; 2 queues

* **Optimal substructure** &#10140; *Dynamic programming* to compute all the optimal solution of size $0 \ldots n$  and deduce the solution.
    *  when it is possible to craft the optimal solution for an instance size $n$ using the solution to instances of size $i_1, \ldots, i_p < n$.
    * Can be on a pair of parameters, solution of size $(n, k)$ can be deduced from solution of size $(i, j)$ where $i \leq n$ and $j \leq k$.
    > **Examples:** subarray, knapsack, longest substring

# Strategies

## Do It Yourself

Solve an example with your brain and hands and see what "algorithm" you used.

## B.U.D.

**Bottlenecks**, **Unnecessary work**, **Duplicated work**
Walk through your best algorithm and look for these flaws.

## Space/Time tradeoffs

Can I save time by using more space ?

* Hash tables
* Frequency arrays
* Dynamic programming



# Data Structures

* **Stack** 
  * $O(1)$:  `l = []`, `l.append()`, `l.pop()`, `l[i]`, `len(l)`
  * $O(n)$:  `del l[i]`, `l[inf:sup:step]`
  * $O(nlog_2(n))$: `l.sort()`, `sorted(l)` 
* **Queue** 
  * $O(1)$:  `dq = deque()`,`dq.popleft()` ,  `dq.popleft()` + normal list operations except slices


* **Dictionary / Hashtable**
  * $O(1)$:  `dic = {}`, `key in dic`,  `dic[key]`, `del dic[key]` on average, worst case $O(n)$
* **Set**
  * $O(1)$:  `s = set([])`, `x in s`, `s.add(x)`, `del s[x]`
  * $O(n_1)$: `s1|s2 ` , `s1&s2` , `s1-s2`,  `s1^s2`
* **Heap / Priority Queue**
  * $O(1)$: `heap = []`
  * $O(log_2(n))$: `heappush, heappop`
  * $O(nlog_2(n) )$: `heap = heapfy([1, 5, 2, 3...])` 

# Recursion
```python
def f():
    # Base case
    ...
    # Recurisve calls
    ...
```

# Bisection search
Bisection search ends when `left` and `right` cross.
```python {.line-numbers}
def bisect(xs, key, f):
    left, right = 0, len(xs)
    
    while left < right:
        mid = left + (right - left) // 2     # avoid integer overflow
        if f(xs[mid], key): left  = mid + 1  # Move right
        else:               right = mid      # Move left
    
    return left
```
When will they cross ?
* `f(x, key) = x < key` &#10140; Move left when `x == key`
    * Index of the first occurrence of key
* `f(x, key) = x <= key` &#10140; Move right when `x == key`
    * Index of the last occurrence of key + 1
```python
bisect_left  = lambda xs,key: bisect(xs, key, lambda x,y: x<y)       # First
bisect_right = lambda xs,key: bisect(xs, key, lambda x,y: x<=y) - 1  # Last
```
* Might be necessary to check if the final value points to key

# Sorting algorithms

## Merge sort

1. Split the list in 2
2. Recursively sort the left-most part and right-most part
3. Merges these parts

```python {.line-numbers}
def fuse(t, i, j, k, aux):
    # fuse t[i:k] in aux[i:k] supposing t[i:j] and t[j:k] are sorted
    a, b = i, j  # iterators
    for s in range(i, k):
        if a == j or (b < k and t[b] < t[a]):
            aux[s] = t[b]
            b += 1
        else:
            aux[s] = t[a]
            a += 1
```

```python {.line-numbers}
def merge_sort(t):
    aux = [None] * len(t)

    def merge_rec(i, k):
        # merge sort t from i to k
        if k > i + 1:
            j = i + (k - i) // 2
            merge_rec(i, j)
            merge_rec(j, k)
            fuse(t, i, j, k, aux)
            t[i:k] = aux[i:k]
            
    merge_rec(0, len(t))
```

## Counting sort
1. Count the occurences of each possible values
2. Put the number of occurence times each value in the array, starting from the smallest one
```python {.line-numbers}
def counting_sort(array, maxval):
    """in-place counting sort
       O(n + maxval)"""
    m = maxval + 1
    # count the occurence of every possible value
    count = [0] * m  # /!\ 
    for a in array:
        count[a] += 1
    i = 0
    for a in range(m):
        for _ in range(count[a]):
            array[i] = a
            i += 1
    return array
```


# Dynamic programming
## Simple steps
1. **Recursive** solution
2. **Store** intermediate results
3. Bottom up (Optional)
>* Consider adding **dummy values** because things like `res[x][y]` may throw index errors.
> * It can be easier to find the size of the best solution and then **backtrack** to find the solution.
### Recursive solution
```python {.line-numbers}
#-- 1 Naive recursive solution
def f():
    # Base case
    ...
    # Recurisve calls
    ...
```
### Memoization
`@lru_cache(maxsize=None)`  can automate the memoization process by using a dictionary to store the result of function calls (less efficient than an array).
```python {.line-numbers}
#-- 2 Adding the memoization
res = [[-1] * len(X) for _ in range(len(Y))]  # a slot for every possible parameters
# @lru_cache(maxsize=None)
def f(x, y):
    # Base case
    ...
    # Already seen case
    if res[x][y] != -1:
        return res[x][y]
    # Recurisve calls
    ...  # Just update the res[x][y] slot
    return res[x][y]
```

### Bottom up
```python {.line-numbers}
#-- 3 Bottom up
def f(X, Y):
    res = [[-1] * len(X) for _ in range(len(Y))
           
    for x in range(1, len(X)):  # skipping dummy value
        for y in range(1, len(Y)):
            ... #  update the res[x][y] slot
            
    return res[-1][-1]
```

# int &#8596; char
```python
chr(65)   # -> 'A'
ord('A')  # -> 65
chr(97)   # -> 'a'
ord('a')  # -> 97
```

# Base conversion
```python {.line-numbers}
def basebTo10(x, b=2):  # Horner scheme
    u = 0
    for a in x:
        u = b * u + a
    return u


def base10Tob(q, b=2):
    s = ''
    while q > 0:
        q, r = divmod(q, b)
        s = str(r) + s
    return s
```
```python {.line-numbers}
# when our base is a power of 2
def base10toPowOf2(q, pow=1):
    s = '' 
    while q > 0 or not s: 
        q, s = q >> pow, str(q & pow) + s 
    return s

```
```python {.line-numbers}
#-- When there is no 0 in our base
# for instance counting excel columns
def base10tobNoZero(q, b=2):
    s = ''
    while q > 0 or not s:
        q, r = divmod(q - 1, b)  # -1 to remove 0
        s = chr(65 + r) + s
    return s
```


# Bitwise operators

## Operation
* `x << y` Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y. 

* `x >> y` Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y. 

* `x & y` Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.  Commutative and Associative.

* `x | y` Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.  Commutative and Associative.

* `~ x` Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1. 

* `x ^ y` Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1. Commutative and Associative.

## Coding sets on bits
Efficient when there is less than 64 possible values


| Set                                    | Binary         |
| -------------------------------------- | -------------- |
| $\emptyset$                            | `0`            |
| $\{i\}$                                | `1 << i`       |
| $\{0, 1, \ldots, n-1\}$                | `(1 << n) - 1` |
| $A \cup B$                             | `A | B`        |
| $A \cap B$                             | `A & B`        |
| $(A \setminus B) \cup (B \setminus A)$ | `A ^ B`        |
| $A \subseteq B$                        | `A & B == A`   |
| $i \in A$                              | `(1 << i) & A` |
| $\{min(A)\}$                           | `-A & A`       |


# Algorithms

You should ideally now about:

(Most are overkill for an interview but nice to know as a software engineer)

## Numeric/mathematical

* Kadane's algorithm
    * every subarray has an ending
    * the maximum subarray ending at the spot `i + 1 is either`
       1. maximum subarray ending at the spot `i` +  `A[i + 1]`
       2. `A[i + 1]`
* Boyer-Moore majority vote algorithm
    * find a candidate for the majority element
        1. keep a counter of the number of occurence of the current candidate while iterating through the list
        2. `++` if the current element is the candidate `--` otherwise
        3. if counter reaches 0, candidate = current candidate
    * check if the candidate is the majority element
* Quickselect / Median-of-medians
* Reservoir sampling
* Sieve of Eratosthenes
* Alias method
* Euclid's algorithm
    * if `b != 1` return  = `gcd(b, a % b)`
    * else return a
* Exponentiation by squaringMatrix exponentiation
    * Just square exponentiation with matrix
    * `res = res * a` if n odd
    * `a = a * a` otherwise
* Matrix exponentiation
    * use exponentiation by squaring
* Range minimum query

## Tree/graph

* BFS
    * stack or recursion
* DFS
    * queue
* Dijkstra's algorithm
* A* search
* Toposort
* Morris traversal
* Prim's algorithm
* Kruskal's algorithm
* Bellman-Ford algorithm
* Graham scan algorithm
* Ford-Fulkerson algorithm / Edmunds-Karp algorithm
* Floyd's cycle finding algorithm
* Closest pair of points algorithm
* Hopcroft-Karp algorithm

## String

* Longest common subsequence
    * `lcs[p][q]` = lcs ending at index `p` in str1 and `q` in str2 (DP)
    * `lcs[p][q]` = `str1[p] == str2[q] ? 1 + lcs[p-1][q-1] : max(lcs[p][q-1], lcs[p-1][q])`
* Rabin-Karp algorithm
* Knuth-Morris-Pratt algorithm
* Aho-Corasick algorithm
* Ukkonen's algorithm / SA-IS algorithm
* Manacher's algorithm

## Search

* [Bisection search](#bisection-search)
* Interpolation search
* Meta binary search

## Sorting

* [Merge sort](#merge-sort)
* Heap sort
* Quicksort + Three way partitioning + Median of three
* Dutch national flag algorithm

## Other

* Fisher-Yates shuffle
* Shunting-yard algorithm
* Minimax
* Mo's algorithm
* Square root decomposition
* Rolling hash


# Links
[Lot's of info](https://www.geeksforgeeks.org)

## Bloomberg
* [Bloomberg](https://www.geeksforgeeks.org/bloomberg-recruitment-process/)
* [Interview + know bloomberg](https://www.geeksforgeeks.org/bloomberg-interview-experience-set-5-entry-level-software-engineer/)
