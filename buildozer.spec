[app]

title = Sifre Uretici
package.name = sifre_uretici
package.domain = org.burhan
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
icon.filename = icon.png
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Python modülleri
requirements = python3,kivy

# giriş noktası
entrypoint = main.py

# mimariler
android.archs = armeabi-v7a, arm64-v8a

# minimum Android API seviyesi
android.minapi = 21
android.api = 31
android.ndk = 23b
android.sdk = 31
android.gradle_dependencies = 

# debug ve log
log_level = 2

# buildozer çıktıları
[buildozer]
log_level = 2
warn_on_root = 1
