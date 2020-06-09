.PHONY: test format dev prod clean docs

clean:
	rm -rf dist *.egg-info .pytest_cache

up:
	docker-compose up -d

down:
	docker-compose down

docs:
	# start docusaurus server
	$(MAKE) -C docs dev

docs-deploy:
	$(MAKE) \
		GIT_USER=ianre657 \
		-C docs deploy

shell:
	docker-compose exec api-server bash