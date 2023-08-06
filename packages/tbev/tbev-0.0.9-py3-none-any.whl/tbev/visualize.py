"""tbev.

Usage:
    tbev demo 
    tbev <pickle_file> [--logdir=<path>]

Options:
    -h --h    Show help screen
    --logdir=<path>  Location to store log files [default: ./logs/]

"""


import pickle
import tensorflow as tf
from tensorboard import main as tb
from tensorflow.contrib.tensorboard.plugins import projector
import os
from docopt import docopt
import urllib.request
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 


args = docopt(__doc__)


def generate_embeddings_from_pickle(pickle_path, logdir):
    embeddings_dict = pickle.load(open(pickle_path,"rb"))
    embedding_variable = tf.Variable(embeddings_dict['embedding'], name="embeddings")

    summary_writer = tf.summary.FileWriter(logdir)
    config = projector.ProjectorConfig()
    embedding = config.embeddings.add()
    embedding.tensor_name = embedding_variable.name
    embedding.metadata_path = 'metadata.tsv'
    # embedding.sprite.image_path = 'sprite.png'
    # embedding.sprite.single_image_dim.extend(dimensions)
    projector.visualize_embeddings(summary_writer, config)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        saver.save(sess, os.path.join(logdir,'model.ckpt'), 0)

        labels = embeddings_dict["labels"]

        labels_types = list(labels.keys())
        labels_values = []
        for i in range(len(labels[labels_types[0]])):
            labels_values_list = []
            for label_type in labels:
                labels_values_list.append(str(labels[label_type][i]))
            labels_values.append(labels_values_list)
        
        # print(labels_values)

        with open(os.path.join(logdir,embedding.metadata_path), 'w') as handle:
            if len(labels_types) > 1:
                handle.write("{}\n".format("\t".join(labels_types)))
            for label_value in labels_values:
                handle.write('{}\n'.format("\t".join(label_value)))
    
    tf.flags.FLAGS.logdir = logdir
    tb.main()


def main():
    if args["demo"]:
        generate_embeddings_from_pickle("./demo_word2vec_embeddings_zen.pkl","./logs/")
    else:
        generate_embeddings_from_pickle(args["<pickle_file>"],args["--logdir"])

        

if __name__ == '__main__':
    # print(args)
    main()