generate:
	python3 generate.py

create:
	python3 generate.py
	vagrant up

destroy:
	vagrant destroy -f
	rm -rf .vagrant

status:
	vagrant status

clean:
	rm -rf .vagrant
