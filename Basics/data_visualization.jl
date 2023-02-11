function calc_fib(n)
    if n == 0
        return 0
    elseif n == 1 
        return 1
    return calc_fib(n-1) + calc_fib(n-2)

end

function calc_fib2(n)
    if n == 0
        return 0
    elseif n == 1 
        return 1
end

#print(calc_fib(0))