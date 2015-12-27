all:
	nikola build
deploy:
	nikola build
	cd output && git add posts/*  categories/* && git commit -a -m "automatic push" && git push -u origin master
