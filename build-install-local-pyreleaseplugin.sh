# Build Python Release Plugin
python3 setup.py clean build bdist_wheel

#Install Python Release Plugin locally
pip3 install dist/pyreleaseplugin-0.2.15-py3-none-any.whl 

# Show Python Release Plugin installed using pip3, to confirm installation
pip3 show pyreleaseplugin 