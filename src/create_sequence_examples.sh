CONFIG='performance_with_dynamics'

performance_rnn_create_dataset \
--config=${CONFIG} \
--input=/tmp/notesequences.tfrecord \
--output_dir=/tmp/performance_rnn/sequence_examples \
--eval_ratio=0.10
