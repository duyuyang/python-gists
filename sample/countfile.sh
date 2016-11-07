# Example output:
#/var/save/Task/fs 340
#/var/save/Task/fs/dir1 84
#/var/save/Task/fs/dir1/dir1 4

#TARGET_FILE_SYSTEM=/var/save/Task/fs
TARGET_FILE_SYSTEM=/Users/duyuyang/tmp

get_file_number() {
  NUM=$(find $1 -maxdepth 1 -type f | wc -l)
  echo $1 ${NUM}
}

get_directories() {
  LIST=($(find $1 -type d))
  for dir in "${LIST[@]}"; do
    get_file_number $dir
  done
}

#get_file_number ${TARGET_FILE_SYSTEM}
get_directories ${TARGET_FILE_SYSTEM}
