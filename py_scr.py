import os

os.system('git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git')

os.system('export PATH="$PATH:/home/nas/depot_tools"')

os.system('mkdir ~/chromium && cd ~/chromium')

os.system('fetch --nohooks --no-history chromium')

os.system('cd src')

os.system('build/install-build-deps.sh')

os.system('gclient runhooks')

os.system('gn gen out/Default')



#Then follow instructions for quic:

os.system('ninja -C out/Default quic_server quic_client')

os.system('mkdir /tmp/quic-data')
os.system('cd /tmp/quic-data')
os.system('wget -p --save-headers https://www.example.org')
os.system('cd ../home/nas/chromium/src')

#Add line to html:
#X-Original-Url: https://www.example.org/

os.system('cd net/tools/quic/certs')
os.system('./generate-certs.sh')
os.system('cd -')


