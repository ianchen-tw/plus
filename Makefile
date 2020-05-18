.PHONY: test format dev prod clean

clean:
	rm -rf dist *.egg-info .pytest_cache

up:
	docker-compose up -d

down:
	docker-compose down

shell: up
	docker-compose exec api-server bash