#import Pkg; Pkg.add("Plots")

using Plots
x = 1:20; y = rand(20); # These are the plotting data
plot(x,y, label="my label")