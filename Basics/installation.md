Open a new terminal and go to your Downloads folder:

cd ~/Downloads

Use wget to retrieve the latest compressed Julia Linux Binaries:

wget https://julialang-s3.julialang.org/bin/linux/x64/1.8/julia-1.8.3-linux-x86_64.tar.gz

Extract the .tar.gz:

tar -xvzf julia-1.8.3-linux-x86_64.tar.gz

Copy the extracted folder to /opt:

sudo cp -r julia-1.8.3 /opt/

Finally, create a symbolic link to julia inside the /usr/local/bin folder:

sudo ln -s /opt/julia-1.8.3/bin/julia /usr/local/bin/julia


Finally, you can test your installation by re-opening a terminal and typing:

julia

Julia REPL