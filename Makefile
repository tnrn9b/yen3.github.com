all:
	nikola build

deploy:
	nikola build
	nikola github_deploy
