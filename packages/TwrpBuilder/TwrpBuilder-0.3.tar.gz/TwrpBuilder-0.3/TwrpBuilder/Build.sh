#!/usr/bin/env bash
if [ "$1" -ne 1 ];then
 {
 exit 1
 }
fi
{
. build/envsetup.sh
lunch omni_$1-eng
make -j$(nproc --all) recoveryimage
}