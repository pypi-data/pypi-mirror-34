"""tbev.

Usage:
    tbev demo 
    tbev <pickle_file> [--logdir=<path>]

Options:
    -h --h    Show help screen
    --logdir=<path>  Location to store log files [default: ./logs/]

"""

from docopt import docopt
args = docopt(__doc__)


import sys
from colorama import init, deinit, Fore, Back, Style
init()


def print_info(s):
    print(Fore.GREEN+"[INFO] "+Style.RESET_ALL+s)

def print_error(s, terminate=False):
    print(Fore.RED+"[ERROR] "+Style.RESET_ALL+s)
    if terminate:
        sys.exit()

import pickle
print_info("Loading tensorflow")
try:
    import tensorflow as tf
except ImportError:
    print_error("Could not import tensorflow. Make sure it is installed", True)


from tensorboard import main as tb
from tensorflow.contrib.tensorboard.plugins import projector
import os
import urllib.request
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 



def verify_embeddings_dict(embeddings_dict):
    try:
        embddings = embeddings_dict["embedding"]
    except KeyError:
        print_error("Embeddings not found in pickle file", True)
    
    try:
        labels = embeddings_dict["labels"]
    except KeyError:
        print_error("Labels not found in pickle file", True)
    
    num_samples = len(embddings)

    for label in labels:
        if len(labels[label]) != num_samples:
            print_error("Number of labels: {} is not equal to number of embeddings: {} != {}".format(label,
                                                                                                     len(labels[label]),
                                                                                                     num_samples), True)
    



def generate_embeddings_from_pickle(pickle_path, logdir):
    print_info("Loading embeddings pickle")
    embeddings_dict = pickle.load(open(pickle_path,"rb"))
    print_info("Verifying embeddings")
    verify_embeddings_dict(embeddings_dict)
    print_info("Embeddings verified successfully")
    embedding_variable = tf.Variable(embeddings_dict['embedding'], name="embeddings")

    summary_writer = tf.summary.FileWriter(logdir)
    config = projector.ProjectorConfig()
    embedding = config.embeddings.add()
    embedding.tensor_name = embedding_variable.name
    embedding.metadata_path = 'metadata.tsv'
    # embedding.sprite.image_path = 'sprite.png'
    # embedding.sprite.single_image_dim.extend(dimensions)
    projector.visualize_embeddings(summary_writer, config)

    print_info("Creating embeddings checkpoint")

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
        print_info("Creating labels metadata")
        with open(os.path.join(logdir,embedding.metadata_path), 'w') as handle:
            if len(labels_types) > 1:
                handle.write("{}\n".format("\t".join(labels_types)))
            for label_value in labels_values:
                handle.write('{}\n'.format("\t".join(label_value)))
    
    print_info("Logs created at {}".format(os.path.abspath(logdir)))
    tf.flags.FLAGS.logdir = logdir
    print_info("Starting Tensorboard")
    tb.main()


def main():
    if args["demo"]:
        generate_embeddings_from_pickle("./demo_word2vec_embeddings_zen.pkl","./logs/")
    else:
        generate_embeddings_from_pickle(args["<pickle_file>"],args["--logdir"])

        

if __name__ == '__main__':
    # print(args)
    main()