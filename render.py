import haml
import mako.template
import mako.lookup
import os

# Build the template lookup.
lookup = mako.lookup.TemplateLookup(["templates"],
    preprocessor=haml.preprocessor
)

# parse all haml files which don't start with _
for filename in os.listdir('./templates'):
    if filename[0] != '_' and filename.split('.')[-1] == 'haml':
        template_name = filename.split('.')[0]

        # Retrieve a template.
        template = lookup.get_template('%s.haml' % template_name)

        destination_file = './build/%s.html' % template_name

        # Render!
        print("Rendering %s.haml to %s" % (template_name, destination_file))
        with open(destination_file, 'w') as fh:
            try:
                fh.write(template.render())
            except:
                print(mako.exceptions.text_error_template().render())
