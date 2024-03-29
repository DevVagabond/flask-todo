# Signifies our desired python version
# Makefile macros (or variables) are defined a little bit differently than traditional bash, keep in mind that in the Makefile there's top-level Makefile-only syntax, and everything else is bash script syntax.
PYTHON = python3

# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY = help setup test run clean

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "------------------------------------"

# This generates the desired project file structure
# A very important thing to note is that macros (or makefile variables) are referenced in the target's code with a single dollar sign ${}, but all script variables are referenced with two dollar signs $${}
setup:
	virtualenv venv
	@echo "Virtualenv created"
	source /venv/bin/activate
	@echo "Virtualenv activated"
	pip install -r requirements.txt
	@echo "Requirements installed"
	@echo "run 'make run' command to start the server"



# The ${} notation is specific to the make syntax and is very similar to bash's $()
# This function uses pytest to test our source files
test:
	${PYTHON} -m pytest

run:
	flask run -p 3000

# In this context, the *.project pattern means "anything that has the .project extension"
clean:
	rm -r *.project