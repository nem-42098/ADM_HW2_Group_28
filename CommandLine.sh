#!/bin/bash
RED='\033[0;31m'
NOCOLOR='\033[0m'
echo
echo "Getting all profiles with description longer than 100 characters."
echo "The data must be in the same directory of the shell file."
echo "Writing into results.txt ..."

if test -f "instagram_posts.csv";
then
awk -F'\t' '{if (length($8)>100) {(profile=$4); if(profile=="") print("User Was Not Found!"); else print(profile)}}' instagram_posts.csv > result.txt
echo
echo "The profiles list is saved in results.txt"

else
echo
echo -e "${RED}Could not found the .csv file. Please place the shell file and instagram_posts.csv in the same directory.${NOCOLOR}"
fi

echo

