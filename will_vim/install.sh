#!/bin/sh

if [ -e ~/.vimrc ] ;then
	echo Do backup ~/.vimrc first!
	exit
fi

if [ -e ~/.vim ]; then
	echo Do backup ~/.vim first!
	exit
fi

VIM_FOLDER=$PWD
ln -s ${VIM_FOLDER}/vimrc ~/.vimrc
ln -s ${VIM_FOLDER} ~/.vim

