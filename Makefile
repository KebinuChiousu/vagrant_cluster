generate:
	python3 generate.py

create:
	python3 generate.py
	vagrant up

destroy:
	vagrant destroy -f
	rm -rf .vagrant

start:
	vagrant up --no-provision

suspend:
	vagrant suspend

stop:
	vagrant halt

status:
	vagrant status

clean:
	rm -rf .vagrant
