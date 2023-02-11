#--------------------------
#### Zeta function  
#--------------------------
#, let’s define a function that will sum
# the first terms of the Riemman Zeta function (see Wiki)

function sum_zeta(s,nterms)
    x = 0
    for n in 1:nterms
        x = x + (1/n)^s
    end
    return x
end

#print(sum_zeta(2,100000))

#--------------------------
#Euler Equation 
#--------------------------
#"[The Euclidean algorithm] is the granddaddy of all algorithms, because it is the oldest nontrivial algorithm that has survived to the present day." - Donald Knuth, The Art of Computer Programming

#--------------------------
### Fibonnaci series
#--------------------------
function calc_fib(n)
    if n == 0
        return 0
    elseif n == 1 
        return 1
    else
        return calc_fib(n-1) + calc_fib(n-2)
    end
end

#print(calc_fib(19))

#--------------------------
### Bubble Sort 
#--------------------------
#We are given with an input array which is supposed to be sorted in
# ascending order

function bubble_sort(arr, n)
    temp_swap = 0

    for i in 1:n
        for j in 1:n-i
            if arr[j] > arr[j+1]
                temp_swap = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp_swap
            end
        end
    end
    return arr  
end
print("sorted array:")
print(bubble_sort([4,3,2,1], 4))

#--------------------------
#Quick Sort
#--------------------------




#--------------------------
#Euclid's algorithm
#--------------------------
function compute_gcd(m,n)

    while (n > 0)
        r = m % n;
        m = n;
        n = r;
    end 
    return m
end
print("\n Greater common divisor: ")
print(compute_gcd(20,5))