# Install Cloudflare Warp and Cloudflared on Ubuntu
echo "Installing Cloudflare packages..."

# Detect Ubuntu codename (like focal, jammy, noble)
UBUNTU_CODENAME=$(lsb_release -cs)

# ---- Install Cloudflare Warp ----
echo "Setting up Cloudflare Warp repository..."

curl -fsSL https://pkg.cloudflareclient.com/pubkey.gpg | sudo gpg --yes --dearmor -o /usr/share/keyrings/cloudflare-warp-archive-keyring.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/cloudflare-warp-archive-keyring.gpg] https://pkg.cloudflareclient.com/ bookworm main" | sudo tee /etc/apt/sources.list.d/cloudflare-client.list

# ---- Install Cloudflared ----
echo "Setting up Cloudflared repository for Ubuntu codename: $UBUNTU_CODENAME..."

sudo mkdir -p --mode=0755 /usr/share/keyrings
curl -fsSL https://pkg.cloudflare.com/cloudflare-main.gpg | sudo tee /usr/share/keyrings/cloudflare-main.gpg >/dev/null

echo "deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] https://pkg.cloudflare.com/cloudflared $UBUNTU_CODENAME main" | sudo tee /etc/apt/sources.list.d/cloudflared.list

# ---- Install packages ----
sudo apt update
sudo apt install -y cloudflare-warp cloudflared

echo "✅ Cloudflare Warp and Cloudflared installation complete."