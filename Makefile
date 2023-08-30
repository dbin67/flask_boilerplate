all: build up

update:
	docker-compose exec flask flask --app apps db migrate
	docker-compose exec flask flask --app apps db upgrade

build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

re: down build up