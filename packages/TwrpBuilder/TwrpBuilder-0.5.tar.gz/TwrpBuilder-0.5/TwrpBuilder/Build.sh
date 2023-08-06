#!/usr/bin/env bash
if [ "$#" -ne 1 ];then
 {
 echo "Failed to build "
 exit 1
 }
fi
{
. build/envsetup.sh
lunch omni_$1-eng
if [ $? -eq 0 ]; then
    make -j$(nproc --all) recoveryimage
    exit 0
fi
    exit -1
}