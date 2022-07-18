echo "Upgrading pip..."
python3 -m pip install --upgrade pip
echo "Installing build..."
python3 -m pip install --upgrade build
echo "Building package..."
python3 -m build --sdist --wheel
echo "Building packages..."
pip install ./dist/my_minipack-1.0.0-py3-none-any.whl