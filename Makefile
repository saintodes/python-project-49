#Makefile
install:
		poetry install

brain-games:
		poetry run brain-games

build: # run poetry build
		poetry build

publish: #--dry-run poetry publishing
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl