name: Build Kivy APK

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repo
        uses: actions/checkout@v4

      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y zip unzip openjdk-17-jdk python3-pip \
            libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
            libmtdev-dev libgl1-mesa-dev libgles2-mesa-dev \
            libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev \
            libavcodec-dev libavformat-dev libswscale-dev \
            libjpeg-dev libfreetype6-dev libncurses5 \
            adb

          pip install --upgrade pip setuptools Cython virtualenv
          pip install buildozer

          mkdir -p ~/.buildozer/android/platform
          yes | sdkmanager --licenses || true

      - name: Build APK
        run: |
          buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: sifre_uretici.apk
          path: bin/*.apk
