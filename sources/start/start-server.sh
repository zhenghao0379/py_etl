# start exec
cd /usr/local/azkaban3.80.1/azkaban-exec-server
./bin/start-exec.sh 
curl -G "localhost:$(<./executor.port)/executor?action=activate" && echo

# start web
cd /usr/local/azkaban3.80.1/azkaban-web-server
./bin/start-web.sh 