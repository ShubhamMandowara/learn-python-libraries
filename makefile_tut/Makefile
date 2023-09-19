create_poetry_env:
	echo "Creating poetry environment"
	poetry init 
	cat requirements.txt | xargs poetry add

create_format:
	black . # format
	pylint . # to get score of your code
