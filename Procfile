sass:     sass -C --watch ./stylesheets:./build/stylesheets
haml:     watchmedo shell-command --patterns="*.haml" --recursive --command='python render.py'
web:      pushd ./build; python -m SimpleHTTPServer; popd
