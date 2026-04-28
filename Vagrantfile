Vagrant.configure("2") do |config|

  config.vm.box      = "generic/ubuntu2204"
  config.vm.hostname = "playwright-vm"

  config.vm.synced_folder ".", "/home/vagrant/app",
    type: "rsync",
    rsync__exclude: [".git/", ".vagrant/", "__pycache__/", "test-results/"]

  config.vm.provider "hyperv" do |hv|
    hv.vmname  = "playwright-practice"
    hv.memory  = 2048
    hv.cpus    = 2
    hv.auto_start_action = "Nothing"
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update -y
    apt-get install -y python3 python3-pip git curl
    pip3 install pytest pytest-playwright
    playwright install chromium --with-deps
    echo "--- VM ready ---"
  SHELL

end