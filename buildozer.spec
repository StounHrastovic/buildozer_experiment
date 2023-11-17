[app]
# 1 Title of your application
title = gudvindoker

# 2 Package name
package.name = gudvin15

# 3 Package domain (needed for android/ios packaging)
package.domain = org.test

# 4 Source code directory
source.dir = .

# 5 Source files to include
source.include_exts = py,png,jpg,kv,atlas

# 6 Application version
version = 0.1

# 7 Application requirements
requirements = python3,kivy

# 8 (str) Application entry point
source.entry_point = v14.11Gudvin1.py

# 9 (list) List of source files
source.files = v14.11Gudvin1.py

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = /build

# (str) Package name
package.name = gudvin15

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# Supported orientations
orientation = portrait

# Android specific
fullscreen = 0  # Set to 1 for fullscreen
android.api = 31
android.minapi = 21
android.ndk = 23b
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True

# Python for android (p4a) specific
p4a.branch = master
# p4a.branch = develop

