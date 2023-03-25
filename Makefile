SHELL := /bin/bash

container=app_summary_log
image=image_python_summary_log
image_base=python:3.8

.PHONY: build
build:
	docker build -t $(image) --rm .


.PHONY: run
run:
	docker run -it \
		--name $(container) \
		--volume $$(pwd)/sre-intern-test:/home/sre-intern-test \
		--rm $(image)


.PHONY: start
start:
	make build;
	make run;


.PHONY: finish
finish:
	# docker stop $(container);
	docker rm -f $(container);
	docker rmi -f $(container);
	docker rmi -f $(image_base);
	docker rmi -f $(image);


.PHONY: restart
restart:
	make finish;
	make start;


.PHONY: test
test:
	pytest --verbose tests/;