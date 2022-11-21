# Set up db_name
export DB_NAME=$1
sudo -u postgres bash -c "dropdb $DB_NAME"
sudo -u postgres bash -c "createdb $DB_NAME"
python load_sample.py