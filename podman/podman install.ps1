wsl --set-default-version 2
systeminfo | Select-String "Hyper-V"

wsl --version
winver

# Download Fedora rootfs
Invoke-WebRequest -Uri "https://github.com/fedora-cloud/docker-brew-fedora/blob/45/x86_64/fedora-20260322.tar" -OutFile "$env:TEMP\fedora.tar.xz"

# Import into WSL
wsl --import Fedora "$env:USERPROFILE\WSL\Fedora" "$env:TEMP\fedora.tar.xz"

# Set as default
wsl --set-default Fedora

# Inside WSL2 Fedora
sudo dnf install -y podman

# Test
podman --version
podman run hello-world