# Set up db_name

if [[ $# -eq 0 ]] ; then
    echo 'Need to specify DB_NAME, please retry again'
    exit 0
fi

export DB_NAME=$1
echo "Start dropping db $DB_NAME if exists"
sudo -u postgres bash -c "dropdb $DB_NAME --if-exists"
echo "Start creating db $DB_NAME"
sudo -u postgres bash -c "createdb $DB_NAME"
echo "Start loading samples for db $DB_NAME"
python load_sample.py
