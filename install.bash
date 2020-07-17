# install_IMU.bash
# July 14 2020
# gnss-ins-sim is actually a lib
pip install numpy
pip install matplotlib
pip install opencv-python
git clone https://github.com/Aceinna/gnss-ins-sim.git
cd gnss-ins-sim
python setup.py install
