#!/usr/bin/env python3
import os
from os import path
import shutil
import yaml
import jinja2


def parse_yml(yml_file):
    config = None

    with open(yml_file, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
            #print(vagrant_config)
        except yaml.YAMLError as exc:
            print(exc)

    return config

def generate_vagrantfile():

    vagrant_yml = ''

    if path.exists('vagrant.override.yml'):
        vagrant_yml = 'vagrant.override.yml'
    else:
        vagrant_yml = 'vagrant.yml'

    config = parse_yml(vagrant_yml)

    file = open('Vagrantfile', 'w+')
    file.write(load_template().render(config))
    file.close()


def generate_users():
    dir_path = path.dirname(os.path.realpath(__file__))

    if not path.exists(path.join(dir_path,"users.yml")):
        shutil.copy(path.join(dir_path,"default/users.yml"),dir_path)

    config = parse_yml('users.yml')

    for user in config['users']:
        keyfile = 'users/' + user['username'] + '.pub'
        if not path.exists(keyfile):
             file = open(keyfile, 'w+')
             file.close


def generate_hosts():

    vagrant_yml = ''

    if path.exists('vagrant.override.yml'):
        vagrant_yml = 'vagrant.override.yml'
    else:
        vagrant_yml = 'vagrant.yml'

    config = parse_yml(vagrant_yml)
    vagrant = config['vagrant']

    file = open('hosts', 'w')
    for node in vagrant['nodes']:
      if 'private_network' in node:
        file.write(node['private_network']['ip'] + ' ' + node['hostname'] +'\n')
    file.close()


def load_template(template_path='Vagrantfile.j2'):
    return (jinja2.Environment(autoescape=True,
                               loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
                .get_template(template_path))


def generate_artifacts():
    generate_users()  
    generate_vagrantfile()
    generate_hosts()

if __name__ == '__main__':
    generate_artifacts()