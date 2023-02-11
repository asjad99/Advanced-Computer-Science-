import Pkg; 
Pkg.add("HypertextLiteral")

using Plots, StatsBase, Statistics, HypertextLiteral


function simulate(N, p)
	v = fill(0, N, N)
	t = 0 
	
	while any( v .== 0 ) && t < 100
		t += 1
		
		for i= 1:N, j=1:N
			if rand() < p && v[i,j]==0
				v[i,j] = t
			end					    
		end
		
	end
	
	return v
end

simulation = simulate(10, 0.1)