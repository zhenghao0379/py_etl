cd /usr/local/azkaban3.80.1/azkaban-exec-server
./bin/start-exec.sh 
curl -G "localhost:$(<./executor.port)/executor?action=activate" && echo
cd /usr/local/azkaban3.80.1/azkaban-web-server
./bin/start-web.sh 