# Copyright (C) 2009 The Android Open Source Project
# Copyright (c) 2011-2013, The Linux Foundation. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import common
import re

"""Custom OTA commands for gprimelte devices"""

def FullOTA_InstallEnd(info):

    info.script.Print("Mounting /system...")
    info.script.AppendExtra('ifelse(is_mounted("/system"), ui_print("/system is mounted."), run_program("/sbin/mount", "/system"));')

    info.script.Print("Detecting device variant ...")

    # SM-G530W
    info.script.AppendExtra('ifelse(is_substring("G530W", getprop("ro.bootloader")), ui_print("Device is SM-G530W. Updating build.prop ..."));')
    info.script.AppendExtra('ifelse(is_substring("G530W", getprop("ro.bootloader")), run_program("/sbin/sed", "-i", "s/gprimelte/gprimeltecan/g", "/system/build.prop"));')

    # SM-G530T1
    info.script.AppendExtra('ifelse(is_substring("G530T1", getprop("ro.bootloader")), ui_print("Device is SM-G530T1. Updating build.prop ..."));')
    info.script.AppendExtra('ifelse(is_substring("G530T1", getprop("ro.bootloader")), run_program("/sbin/sed", "-i", "s/gprimelte/gprimeltemtr/g", "/system/build.prop"));')
    info.script.AppendExtra('ifelse(is_substring("G530T1", getprop("ro.bootloader")), ui_print("Copying files ..."));')
    info.script.AppendExtra('ifelse(is_substring("G530T1", getprop("ro.bootloader")), run_program("/sbin/cp", "-dpR", "/system/mtr/*", "/system/"));')

    # SM-G530T
    info.script.AppendExtra('ifelse(is_substring("G530TU", getprop("ro.bootloader")), ui_print("Device is SM-G530T. Updating build.prop ..."));')
    info.script.AppendExtra('ifelse(is_substring("G530TU", getprop("ro.bootloader")), run_program("/sbin/sed", "-i", "s/gprimelte/gprimeltetmo/g", "/system/build.prop"));')
    info.script.AppendExtra('ifelse(is_substring("G530TU", getprop("ro.bootloader")), ui_print("Copying files ..."));')
    info.script.AppendExtra('ifelse(is_substring("G530TU", getprop("ro.bootloader")), run_program("/sbin/cp", "-dpR", "/system/tmo/*", "/system/"));')

    info.script.AppendExtra('ifelse(is_substring("G530TT", getprop("ro.bootloader")), ui_print("Device is SM-G530T. Updating build.prop ..."));')
    info.script.AppendExtra('ifelse(is_substring("G530TT", getprop("ro.bootloader")), run_program("/sbin/sed", "-i", "s/gprimelte/gprimeltetmo/g", "/system/build.prop"));')
    info.script.AppendExtra('ifelse(is_substring("G530TT", getprop("ro.bootloader")), ui_print("Copying files ..."));')
    info.script.AppendExtra('ifelse(is_substring("G530TT", getprop("ro.bootloader")), run_program("/sbin/cp", "-dpR", "/system/tmo/*", "/system/"));')

    info.script.AppendExtra('delete_recursive("/system/tmo/");')
    info.script.AppendExtra('delete_recursive("/system/mtr/");')

def FullOTA_PostValidate(info):
    # run e2fsck
    info.script.Print("Checking the file system on /system...")
    info.script.AppendExtra('run_program("/sbin/e2fsck", "-fy", "/dev/block/bootdevice/by-name/system");')
    # resize2fs: run and delete
    info.script.Print("Resizing /system to maximal size...")
    info.script.AppendExtra('run_program("/sbin/resize2fs", "-p", "/dev/block/bootdevice/by-name/system");')
    # run e2fsck
    info.script.Print("Checking the file system on /system again after resize...")
    info.script.AppendExtra('run_program("/sbin/e2fsck", "-fy", "/dev/block/bootdevice/by-name/system");')
