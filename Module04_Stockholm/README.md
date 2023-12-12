To create the docker
```bash
make
```

then
```bash
make bash
```

to run the docker interactively.
infection files have been copied in /home/infection
You can then run the stockholm program


Program usage:
```bash
python3 stockholm.py [-h/--help] [-v/--version] [-r/--reverse] [-s/--silent]
```

The program simulates the propagation of a malware by encrypting files in a specific folder
Options:
	- -h/--help: displays program help
	- -v/--version: displays program version
	- -r/--reverse: reverse encryption of files
	- -s/--silent: silence program output