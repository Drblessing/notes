# Add Monero repository
curl -s https://raw.githubusercontent.com/monero-project/monero/master/utils/gpg_keys/binaryfate.asc | sudo apt-key add -
echo "deb https://downloads.getmonero.org/cli ubuntu main" | sudo tee /etc/apt/sources.list.d/monero.list

# Update and install
sudo apt update

