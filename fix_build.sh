#!/bin/bash

set -e

PROJECT="$HOME/HamResanAndroid"

echo "=== Enter project ==="
cd "$PROJECT"

echo "=== Removing old build cache ==="
rm -rf .buildozer

echo "=== Activating venv ==="
source venv/bin/activate

echo "=== Fix buildozer.spec ==="

sed -i '/android.p4a_whitelist_requirements/d' buildozer.spec
sed -i '/p4a.branch/d' buildozer.spec

if grep -q "^requirements =" buildozer.spec; then
    sed -i 's/^requirements =.*/requirements = python3,kivy==2.3.0,kivymd==1.2.0,pyjnius/' buildozer.spec
fi

cat >> buildozer.spec <<EOF

# fixed android settings
android.api = 34
android.minapi = 24
android.ndk_api = 24
EOF


echo "=== Updating build tools ==="
pip install --upgrade pip setuptools wheel Cython==3.1.2

echo "=== Cleaning buildozer ==="
buildozer android clean || true

echo "=== Starting build ==="
buildozer -v android debug
