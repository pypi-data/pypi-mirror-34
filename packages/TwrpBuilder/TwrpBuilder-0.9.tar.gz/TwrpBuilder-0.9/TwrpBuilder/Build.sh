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
    if [ $? -eq 0 ];then
    cd out/target/product/$1/
    mv recovery.img TWRP_$1-$(date +%d%m%y).img
    exit 0
    fi
    exit -1
fi
    exit -1
}