draft:
	ddpaper --data draftdata/ 634522c9c32e5b2d52230e81/main.tex  --mode macros > 634522c9c32e5b2d52230e81/macros.tex
	ddpaper --data draftdata/ 634522c9c32e5b2d52230e81/main.tex > 634522c9c32e5b2d52230e81/rendered.tex
	cat 634522c9c32e5b2d52230e81/rendered.tex
