#!/usr/bin/env python
import os
import shutil

home = os.path.expanduser('~') + '/'
files = {
		'bash/bashrc': '.bashrc',
		'bash/bash_profile': '.bash_profile',
		'vim/vimrc': '.vimrc',
		'git/gitconfig': '.gitconfig',
		'git/gitignore_global': '.gitignore_global',
		'hg/hgrc': '.hgrc',
		'vrapperrc': '.vrapperrc'
}

def get_backup_dir():
	backup_dir = home + ".dotfiles_backup%d"
	for i in range(100):
		t = backup_dir % i
		if not os.path.exists(t):
			return t + "/"
	raise ValueError("No backup dir possible")
backup_dir = get_backup_dir()

def main():
	for src, dest in files.iteritems():
		handle_conf(src, dest)

	handle_os_specific_conf()

	install_vim_packages()

def handle_conf(src, dest):
	abssrc = os.path.abspath(src)
	target = home + dest
	if os.path.exists(target):
		if os.path.islink(target):
			os.remove(target)
		else:
			backup_existing_file(target)

	os.symlink(abssrc, target)

	print "%s => %s" % (target, abssrc)

def backup_existing_file(target):
	ensure_backup_dir()
	print "backing up %s, saved in %s" % (target, backup_dir)
	shutil.move(target, backup_dir + os.path.basename(target))

def ensure_backup_dir():
	if not os.path.exists(backup_dir):
		os.mkdir(backup_dir)

def install_vim_packages():
	print "installing vim packages with vundle..."
	bundle_home = home + '.vim/bundle'
	if not os.path.exists(bundle_home):
		os.mkdir(bundle_home)
		os.system("git clone https://github.com/gmarik/vundle %s/vundle" %bundle_home)
	os.system("vim +BundleInsall +qall")

def handle_os_specific_conf():
	pass

if __name__ == "__main__":
	main()
