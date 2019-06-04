from magenta.models.melody_rnn import melody_rnn_generate
import tensorflow as tf
from config import PATH

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string('f', '', 'kernel')

FLAGS.bundle_file = PATH.bundle_file
FLAGS.output_dir = PATH.gen_dir
FLAGS.num_outputs = 10
FLAGS.num_steps = 128
FLAGS.primer_melody="[60]"
print(FLAGS.output_dir)
melody_rnn_generate.main(FLAGS)