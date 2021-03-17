cd ..
mkdir data
cd data
wget https://s3.amazonaws.com/nist-srd/SD19/by_class.zip
unzip by_class.zip
rm by_class.zip
mkdir writer

cd ../get_data
python preprocess.py