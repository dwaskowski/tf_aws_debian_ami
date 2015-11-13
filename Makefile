.PHONEY: all

all: debian_amis.tf.json

debian_amis.tf.json:
	python get_ami_for_tf.py > debian_amis.tf.json

clean:
	rm -f debian_amis.tf.json

