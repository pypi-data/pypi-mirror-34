import faspmanager2
import transferspec
import sys

class TransferListener(faspmanager2.ITransferListener):
    def __init__(self, fnToCall):
        faspmanager2.ITransferListener.__init__(self)
        self.fnToCall = fnToCall
    def transferReporter(self, xferId, message):
        self.fnToCall(xferId, message)

def TestFunction(xferId, message):
    print( xferId + "  "+ message)

transferReporter = TransferListener(TestFunction)
transferReporter.thisown = 0
ts = transferspec.TransferSpec()
path1 = transferspec.NodePath()
path1.source = "{path to file}"
ts.paths = [path1]
ts.remote_host = "{remote host}"
ts.direction = "send"
ts.remote_user = "{remote user}"
ts.authentication = "password"
ts.remote_password = "{password}"
ts.destination_root = "Upload"
ts.target_rate_kbps = 5000
ts.ssh_port = 22
ts.fasp_port = 33001

strTs = "{\"transfer_specs\": [{\"transfer_spec\": {\"paths\": [{\"source\": \"{path to file}\", \"destination\": \"/{folder name}\"}], \"direction\": \"send\", \"target_rate_kbps\": 700000, \"source_root\": \"\", \"min_rate_cap_kbps\": 0, \"tags\": {\"aspera\": {\"node\": {\"storage_credentials\": {\"token\": {\"iam_cookie\": \"{cookie}\"}, \"type\": \"token\"}}}}, \"ssh_port\": 33001, \"remote_host\": \"ats-sl-stage.dev.aspera.io\", \"target_rate_cap_kbps\": 1250000, \"min_rate_kbps\": 0, \"token\": \"{token}\", \"cipher\": \"aes-128\", \"sshfp\": null, \"rate_policy\": \"fair\", \"rate_policy_allowed\": \"fair\", \"fasp_port\": 33001, \"http_fallback\": false, \"overwrite_policy\":\"always\", \"lock_min_rate\": true, \"remote_user\": \"xfer\", \"destination_root\": \"/{folder name}\"}}]}"
print(strTs)

xferId = "6a31a3b4-3b89-4af4-99ab-1b7b2fdd279e"
configuration = None
try:
    faspmanager2.startTransfer(xferId, configuration, strTs, transferReporter)
    while faspmanager2.isRunning(xferId):
        pass
    faspmanager2.stopTransfer(xferId)
except ValueError:
    print "File list upload failed. Illegal argument."
    sys.exit(1)
except:
    print "You have an exception. File upload failed."
    sys.exit(1)

print("File list upload complete\n")
