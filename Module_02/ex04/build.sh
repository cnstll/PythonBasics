echo "Upgrading pip..."
python3 -m pip install --upgrade pip
echo "Installing setuptools..."
pip install --upgrade setuptools
echo "Installing build..."
pip install --upgrade build
echo "Building package..."
python3 -m build
