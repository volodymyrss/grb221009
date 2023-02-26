COPY?=ej

draft:
	make -C paper

push-copy:
	cp -fv paper/main.tex paper/figs/* paper-$(COPY)/
	(cd paper-$(COPY)/; git add main.tex main.bbl figs/*; git commit -a -m "upstream update"; git push)

pull-copy:
	(cd paper-$(COPY)/; git pull)
	git clone paper paper-branch-for-merge-$(COPY) || true
	(cd paper-branch-for-merge-$(COPY); git checkout -b $(COPY); cp -fv ../paper-$(COPY)/main.tex .; git commit -a -m "$(COPY) copy  update") || true
	#(cd paper; git remote add $(COPY) ../paper-branch-for-merge-$(COPY); git fetch $(COPY) $(COPY))

