#Makefile
install:
		poetry install

brain-games:
		poetry run brain-games

brain-even:
		poetry run brain-even

brain-calc:
		poetry run brain-calc

brain-gcd:
		poetry run brain-gcd

brain-progression:
		poetry run brain-progression

brain-prime:
		poetry run brain-prime

build: # run poetry build
		poetry build

publish: #--dry-run poetry publishing
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

lint: #launching linter flake8
		poetry run flake8 brain_games

force-reinstall:
		pip install --force-reinstall dist/*.whl