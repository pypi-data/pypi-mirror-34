2nd UCCS Face Detection and Recognition Challenge
=================================================

This package implements the baseline algorithms and evaluation for the second version of the Unconstrained Face Detection and Open Set Recognition Challenge.
This package relies on the signal processing and machine learning libraries Bob_ and Caffe_.
For installation instructions and requirements of Bob_, please refer to the Bob_ web page and the Caffe_ web page.

.. note::
   Due to limitations of Bob_, this package will run only under Linux and MacOS operating systems.
   Particularly, it will not work under any version of Microsoft Windows, and maybe not under some other exotic operating systems.
   If you experience problems with the installation, we would suggest to run the experiments in a virtual environment, e.g., using `Oracle's VirtualBox`_.
   On request, we will generate a virtual image with this package pre-installed.


Dataset
-------

This package does not include the original image and protocol files for the competition.
Please register on the `Competition Website`_ and download the UCCS dataset from there.

Please extract all zip files **into the same directory** (the .zip files contain the appropriate directory structure).
This includes all ``training_*.zip`` and ``validation_*.zip`` files, as well as the ``protocol.zip`` and possibly the ``SampleDataSet.zip``.
The directory will be refereed to as ``YOUR-DATA-DIRECTORY`` below.


Installation
------------

The installation of this package follows the Buildout_ structure.
First, you will need to install Bob_ and Caffe_, ideally into the same conda environment.
Otherwise, please point the ``PYTHONPATH`` variable to where Caffe_ is installed.
Before continuing, please make sure that you can successfully import ``bob.measure`` and ``caffe``:

  $ conda activate bob_py3
  (bob_v3) $ python
  >>> import bob.measure
  >>> import caffe


After installing Bob_ and Caffe_ and extracting this package, please run the following command line to install this package and all of its requirements:

  ``buildout``

The installation procedure automatically generates executable files inside the ``bin`` directory, which can be used to run the baseline algorithms or to evaluate the baselines (and your) algorithm.

The networks that are used in our baselines can be downloaded from the Internet.
To run the face detector baseline, you will need to put the ``model`` directory of the `MTCNN v2`_ face detector into the base directory of this package.
To run the face recognition baseline, you will need to go to the `VGG v2`_ website, download the ``Vggface2_caffe_model.tar.gz``, and extract the ``senet50_ft.caffemodel`` and ``senet50_ft.prototxt`` into the same ``model`` directory.


Running the Baselines
---------------------

There are two scripts to run the baseline, one for each part.

Face Detection
~~~~~~~~~~~~~~

The first script is a face detection script, which will detect the faces in the validation (and test) set.
The baseline detector uses the `MTCNN v2` face detection module, where we had to lower the detection thresholds in order to detect most of the faces in the images -- still around 20 percent of the (mostly difficult) faces could not be detected using `MTCNN v2`_.
Additionally, there are a lot of background areas that are mistakenly marked as faces.

You can call the face detector baseline script using:

  ``./bin/baseline_detector.py``

Please refer to ``./bin/baseline_detector.py -h`` for possible options.
Here is a subset of options that you might want/need to use/change:

  ``--data-directory``: Specify the directory, where you have downloaded the UCCS dataset into.

  ``--result-file``: The file to write the detection results into; this will be in the required format.

  ``--which-set``: The set, for which the baseline detector should be run; possible values: ``training, validation, test, sample``; default: ``validation``.

  ``--verbose``: Increase the verbosity of the script; using ``--verbose --verbose`` or ``-vv`` is recommended; ``-vvv`` will write more information.

  ``--debug``: Run only over the specified number of images; for debug purposes only.

  ``--display``: Display the detected bounding boxes (green) and the ground truth (red); for debug purposes only.

  ``--parallel``: Run in the given number of parallel processes; can speed up the processing tremendously.

  ``--gpus``: Run the face detection using Caffe_ in GPU mode (this might not work depending on your setup of Caffe_); you can specify the device ids to use, typically only `0`; if not specified, runs in CPU mode

On a machine with 32 CPU cores, a good command line for the full baseline experiment would be:

  ``./bin/baseline_detector.py --data-directory YOUR-DATA-DIRECTORY -vv --parallel 32``

On a machine with 32 cores and two NVidia GPUs, a good command line for the full baseline experiment would be:

  ``./bin/baseline_detector.py --data-directory YOUR-DATA-DIRECTORY -vv --parallel 8 --gpus 0 1``

To run a small-scale experiment, i.e., to display the detected faces on 20 images, a good command line might be:

  ``./bin/baseline_detector.py --data-directory YOUR-DATA-DIRECTORY -vvv --display --debug 20``

.. note::
   The ``--display`` option requires Matplotlib_ to be installed and set up properly.
   Display does not work in parallel mode.

By default, the face detection score file will be written to ``./results/UCCS-v2-detection-baseline-validation.txt``.

Face Recognition
~~~~~~~~~~~~~~~~

For face recognition, we utilize the `MTCNN v2`_ face detector to detect all the faces (see above) and make sure that the bounding boxes with the highest overlap to the ground truth labels are used.
For each of the detected bounding boxes in the training set, we enlarge the bounding box with a factor of 1.3 and extract features using the ``pool5/7x7_s1`` layer of the `VGG v2`_ recognition module, which we normalize to unit Euclidean length.
The template enrollment stage simply computes the average of the training set features for each of the known subjects.
To account for the fact that we have unknown subjects in the training and test set, we also enroll one gallery template including all known unknown subjects labeled as ``-1``.

For a probe image, we assume that we do not have any labels (this is what the test set will look like).
Hence, we run the `MTCNN v2`_ detector to detect faces (which will include several background regions).
For each bounding box, we extract the `VGG v2`_ feature as above, and compute **cosine similarities** to all gallery templates including the unknown template.
The highest 10 similarities are stored into the score file -- except when the unknown label (``-1``) is amongst the highest scores, in which case only the scores up to the ``-1`` label are stored.
This means that when the highest score is with the ``-1`` label, only one value is stored in the score file.

You can call the face recognition baseline script using:

  ``./bin/baseline_recognizer.py``

Please refer to ``./bin/baseline_recognizer.py -h`` for possible options.
Here is a subset of options that you might want/need to use/change:

  ``--data-directory``: Specify the directory, where you have downloaded the UCCS dataset into

  ``--result-file``: The file to write the recognition results into; this will be in the required format

  ``--verbose``: Increase the verbosity of the script; using ``--verbose --verbose`` or ``-vv`` is recommended; ``-vvv`` will write more information

  ``--temp-dir``: Specify the directory, where temporary files are stored; these files will be computed only once and reloaded if present

  ``--force``: Ignore existing temporary files and always recompute everything

  ``--debug``: Run only over the specified number of identities; for debug purposes only; will modify file names of temporary files and result file

  ``--parallel``: Run in the given number of parallel processes; can speed up the processing tremendously

On a machine with 32 CPU cores, a good command line would be:

  ``./bin/baseline_recognizer.py --data-directory YOUR-DATA-DIRECTORY -vv --parallel 32``

When using Caffe_ in GPU mode with two NVidia GPUs, a good command line would be:

  ``./bin/baseline_recognizer.py --data-directory YOUR-DATA-DIRECTORY -vv --parallel 2 --gpus 0 1``

By default, the face recognition score file will be written to ``./results/UCCS-v2-recognition-baseline-validation.txt``.


Evaluation
----------

The provided evaluation scripts will be usable to evaluate the validation set only, not the test set (since the test set labels are not given to the participants).
You can use the evaluation scripts for two purposes:

1. To plot the baseline results in comparison to your results.
2. To make sure that your score file is in the desired format.

If you are unable to run the baseline experiments on your machine, we provide the score files for the validation set on the `competition website`_.


Face Detection Evaluation
~~~~~~~~~~~~~~~~~~~~~~~~~

As the ground-truth is usually larger than the face, we do not punish bounding boxes that are smaller than the ground truth.
Therefore, the union (the denominator) takes into account only one fourth of the ground truth bounding box -- or the intersection area, whichever is larger:

.. math::
   O(G,D) = \frac{|G \cap D|}{|G \cup D|} = \frac{G \cap D}{\max\{\frac{|G|}4, |G \cap D|\} + |D| - |G \cap D|}

where :math:`|\cdot|` is the area operator.
Hence, when the detected bounding box :math:`D` covers at least a fourth of the ground-truth bounding box :math:`G` and is entirely contained inside :math:`G`, an overlap of 1 is reached.

The face detection is evaluated using the Free Receiver Operator Characteristic (FROC) curve, which plots the percentage of correctly detected faces over the total number of false alarms (detected background regions).
Different points on the FROC curve can be obtained for different detector confidence values.
This plot can be created using:

  ``./bin/evaluate_detector.py``

This script has several options, some of which need to be specified, see ``./bin/evaluate_detector.py -h``:

  ``--data-directory``: Specify the directory, where you have downloaded the UCCS dataset into

  ``--result-files``: A list of all files containing detection (or recognition) results

  ``--labels``: A list of labels for the algorithms; must be the same number and in the same order as ``--result-files``

  ``--froc-file``: The name of the output .pdf file containing the FROC plot; default is ``UCCS-v2-FROC.pdf``

  ``--log-x``: will plot the horizontal axis in logarithmic scale

  ``--only-present``: will ignore any file for which no detection exists (for debug purposes only, i.e., when detector ran with the ``--debug`` option)

  ``--verbose``: Increase the verbosity of the script; using ``--verbose --verbose`` or ``-vv`` is recommended

To plot the baseline FROC curve (which is shown on the `competition website`_), execute:

  ``./bin/evaluate_detector.py --data-directory YOUR-DATA-DIRECTORY --result-files results/UCCS-v2-detection-baseline-validation.txt --labels Baseline --log-x -vv``

.. note::
   If you have run the face recognition baseline, you can also use the face recognition result file for plotting the FROC curve:

     ``./bin/evaluate_detector.py --data-directory YOUR-DATA-DIRECTORY --result-files results/UCCS-v2-recognition-baseline-validation.txt --labels Baseline --log-x -vv``


Face Recognition Evaluation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open set face recognition is evaluated using the Detection and Identification Rate (DIR) curve, which plots the percentage of correctly detected and identified faces over the total number of false identifications.
Based on various values of the false identifications, several score thresholds are computed.
A face is said to be identified correctly if the recognition score is greater than the threshold and the correct identity has the highest recognition score for that face.
The number of correctly identified faces is computed, and divided by the total number of known faces.
For more details, please refer to [1]_.

.. note::
   By default only rank 1 recognition is performed, but the evaluation can be done using any rank up to 10 (the upper bound of allowed labels per face).
   Providing more than one identity label per face will increase the number of false alarms, and may only have an impact on higher rank evaluations.

.. note::
   Unknown identities or background regions labeled with label -1 or not labeled at all will be ignored (i.e., will not decrease performance).
   Labeling an unknown identity or a background region with any other label than -1 will result in a false alarm -- only the maximum score per bounding box will be considered.

The DIR plot can be created using:

  ``./bin/evaluate_recognizer.py``

As usual, the script has several options, which are similar to ``./bin/evaluate_detector.py`` above, see ``./bin/evaluate_recognizer.py -h`` for a complete list:

  ``--data-directory``: Specify the directory, where you have downloaded the UCCS dataset into

  ``--result-files``: A list of all files containing recognition results

  ``--labels``: A list of labels for the algorithms; must be the same number and in the same order as ``--result-files``

  ``--dir-file``: The name of the output .pdf file containing the DIR plot; default is ``UCCS-v2-DIR.pdf``

  ``--log-x``: will plot the horizontal axis in logarithmic scale

  ``--only-present``: will ignore any file for which no detection exists (for debug purposes only, i.e., when recognizer ran with the ``--debug`` option)

  ``--verbose``: Increase the verbosity of the script; using ``--verbose --verbose`` or ``-vv`` is recommended

  ``--rank``: Use the given rank to plot the DIR curve


To plot the baseline Rank 1 DIR curve (which is shown on the `competition website`_), execute:

  ``./bin/evaluate_recognizer.py --data-directory YOUR-DATA-DIRECTORY --result-files results/UCCS-v2-recognition-baseline-validation.txt --labels Baseline --log-x -vv``


Trouble Shooting
----------------

In case of trouble with running the baseline algorithm or the evaluation, please contact us via email under: opensetface@vast.uccs.edu


.. _bob: http://www.idiap.ch/software/bob
.. _oracle's virtualbox: https://www.virtualbox.org
.. _matplotlib: http://matplotlib.org
.. _buildout: http://www.buildout.org
.. _competition website: http://vast.uccs.edu/Opensetface
.. _caffe: http://caffe.berkeleyvision.org/installation.html
.. _mtcnn v2: https://github.com/walkoncross/mtcnn-caffe-zyf
.. _vgg v2: http://www.robots.ox.ac.uk/~vgg/data/vgg_face2

.. [1] **P. Jonathon Phillips, Patrick Grother, and Ross Micheals** "Evaluation Methods in Face Recognition" in *Handbook of Face Recognition*, Second Edition, 2011.
