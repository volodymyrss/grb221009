COPY?=ej

draft:
	make -C paper draft pdf

push-copy:
	cp -fv paper/main.tex paper-$(COPY)/
	cp -fv paper/figs/* paper-$(COPY)/figs/
	(cd paper-$(COPY)/; git add main.tex main.bbl figs/*; git commit -a -m "upstream update"; git push)

pull-copy:
	(cd paper-$(COPY)/; git pull)
	git clone paper paper-branch-for-merge-$(COPY) || true
	(cd paper-branch-for-merge-$(COPY); git checkout -b $(COPY); cp -fv ../paper-$(COPY)/main.tex .; git commit -a -m "$(COPY) copy  update") || true
	#(cd paper; git remote add $(COPY) ../paper-branch-for-merge-$(COPY); git fetch $(COPY) $(COPY))


store-pull:
	rsync --exclude '*0.2.2[0-4]*' --exclude  '*0.2.19*' -avu me:/tmp/nb2w-store/ /tmp/nb2w-store/
	rsync --exclude '*0.2.2[0-4]*' --exclude  '*0.2.19*' -avu me:~/.cache/odafunction/ ~/.cache/odafunction/
	rsync --exclude '*0.2.2[0-4]*' --exclude  '*0.2.19*' -avu me:/tmp/urivalue/ /tmp/urivalue/
	#rsync --exclude '*0.2.2[0-4]*' --exclude  '*0.2.19*' -avu me:~/.cache/oda-api ~/.cache/oda-api
