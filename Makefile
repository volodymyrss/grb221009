draft:
	make -C 634522c9c32e5b2d52230e81

push-copies:
	cp paper/main.tex paper/figs/* paper-ej/
	cp paper/main.tex paper/figs/* paper-pu/
	(cd paper-ej/; git commit -a -m "upstream update"; git push)
	(cd paper-pu/; git commit -a -m "upstream update"; git push)
