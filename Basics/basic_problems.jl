
#, let’s define a function that will sum
# the first terms of the Riemman Zeta function (see Wiki)

function sum_zeta(s,nterms)
    x = 0
    for n in 1:nterms
        x = x + (1/n)^s
    end
    return x
end

print(sum_zeta(2,100000))

### Fibnaci series

