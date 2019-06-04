import os
class FILE:
    bundle_melody = 'attention_rnn.mag'

class PATH:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(root_dir, 'output')
    bundle_dir = os.path.join(output_dir, 'bundle')
    bundle_file = os.path.join(bundle_dir, FILE.bundle_melody)
    gen_dir = os.path.join(output_dir, 'generated')