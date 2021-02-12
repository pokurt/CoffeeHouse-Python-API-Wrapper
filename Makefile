install:
	@pre-commit run --all-files
	@python3 setup.py install --user
	@rm -rf dist/ && rm -rf *.egg-info && rm -rf build/

uninstall:
	@python3 -m pip uninstall coffeehouse -y

release:
	@pre-commit run --all-files
	@python3 setup.py sdist
	@python3 setup.py sdist bdist_wheel

upload:
	@pre-commit run --all-files
	@twine upload dist/*

clean:
	@pre-commit run --all-files
	@rm -rf dist/ && rm -rf *.egg-info && rm -rf build/
	@echo cleaned all local builds

test:
	@pre-commit run --all-files
