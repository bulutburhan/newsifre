[app]

title = ZeusApp
package.name = sifre_uretici
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1

[buildozer]

log_level = 2
warn_on_root = 1

[app.android]

android.api = 31
android.minapi = 21
android.ndk = 25.2.9519653
android.private_storage = True
android.permissions = INTERNET
android.sdk = 33.0.2
android.accept_sdk_license = True
