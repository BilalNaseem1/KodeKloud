# Basic Linux Commands

```bash
pwd
ls
mkdir
mkdir -p india/mumbai # -p is for creating parent directories

pushd and popd # remebers directories

mv [file] [destination] # move file
cp [file] [destination] # copy file
rm [file] [destination] # remove file

rm -r # recursive
ls -l # long list
ls -a # include hidden
```

## Reading
```bash
# reading contents of a file
cat city.txt

# replacing data in the file
cat > city.txt # will ask for prompt

more city.txt # view file in dcrollable manner
less city.txt

```

## Help commands
```bash
whatis date
date --help
apropos
```

## Bash Shell
```bash
echo $shell

# changing shell
chsh

# setting custom aliases for commands
alias dt=date
echo 'alias up=uptime' >> ~bob/.profile

# command history
history
```
### Environment Variable
```bash
# see list of all environment variables
env

# setting an environment variable
export OFFICE=caleston

echo $LOGNAME
```
- When a user issues an external command into the shell, the shell uses a path variable to search for these external commands.
- to see list of directories defined in the path variable `$PATH`
```bash
echo $PATH

# check location of command
which obs-studio
which python3

# if path to program is not defined in the path variable
export PATH=$PATH:/opt/obs/bin
echo 'export PROJECT=MERCURY' >> /home/bob/.profile
```