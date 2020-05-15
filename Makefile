.PHONY: test format dev

dev:
	pipenv run dev

test:
	pipenv run test

format:
	pipenv run format