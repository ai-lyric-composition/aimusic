#!/usr/bin/env bash
BUNDLE_PATH=/home/pirl/Downloads/performance_with_dynamics_and_modulo_encoding.mag
CONFIG=performance_with_dynamics_and_modulo_encoding

performance_rnn_generate \
--config=${CONFIG} \
--bundle_file=${BUNDLE_PATH} \
--output_dir=/tmp/performance_rnn/generated \
--num_outputs=10 \
--num_steps=3000 \
--primer_melody="[60,61,62,64,65,67,69]" \
--pitch_class_histogram:"[2, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]"