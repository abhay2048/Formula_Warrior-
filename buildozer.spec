[app]
title = Formula Warrior
package.name = formula_warrior
package.domain = org.yourname
source.dir = .
source.include_exts = py,png,jpg,json,kv
version = 0.1
requirements = python3,kivy==2.2.1,plyer
orientation = portrait
icon.filename = assets/icon.png
android.api = 33
android.minapi = 21
android.ndk = 25b
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
