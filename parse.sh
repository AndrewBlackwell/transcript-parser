export PARSER_HOST=0.0.0.0
export PARSER_PORT=5001

cd src
echo Program is running, listen to $PARSER_HOST:$PARSER_PORT
python3 server.py